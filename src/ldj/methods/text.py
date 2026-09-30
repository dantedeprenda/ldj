"""Text baselines: TF-IDF and sentence embeddings, each with a logistic head or kNN.

Same settings as the routing paper so its numbers reproduce: TF-IDF (20k features, 1-2
grams, sublinear tf) refit on each labeled set; embeddings of the text cut to ``max_chars``;
kNN = mean label of the 10 cosine-nearest labeled items.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from ldj.methods.base import LogisticHead, Method
from ldj.task import Task, fit_text


def knn_scores(xl, xt, yl: np.ndarray, k: int = 10) -> np.ndarray:
    nn = NearestNeighbors(n_neighbors=min(k, xl.shape[0]), metric="cosine").fit(xl)
    _, nbrs = nn.kneighbors(xt)
    return yl[nbrs].mean(axis=1)


class Tfidf(Method):
    def __init__(self, head: str = "logreg", k: int = 10):
        super().__init__()
        self.head, self.k = head, k
        self.name = "tfidf_logreg" if head == "logreg" else f"tfidf_knn{k}"

    def fit(self, task, lab):
        self.vec_ = TfidfVectorizer(max_features=20000, ngram_range=(1, 2), sublinear_tf=True)
        self.xl_ = self.vec_.fit_transform([task.texts[i] for i in lab])
        self.yl_ = task.y[lab]
        if self.head == "logreg":
            self.model_ = LogisticHead().fit(self.xl_, self.yl_)
        return self

    def predict(self, task, idx):
        xt = self.vec_.transform([task.texts[i] for i in idx])
        if self.head == "logreg":
            return self.model_.predict(xt)
        return knn_scores(self.xl_, xt, self.yl_, self.k)


class EmbeddingStore:
    """Unit-norm embeddings of every item of a task, computed once and cached on disk.

    The cache file name hashes the model and the exact texts, so a cache built by the routing
    paper for the same texts is reused as is.
    """

    def __init__(
        self,
        model: str = "BAAI/bge-base-en-v1.5",
        max_chars: int = 2000,
        cache_dir: str | Path = ".cache/embeddings",
        device: str | None = None,
        batch_size: int = 32,
    ):
        self.model, self.max_chars = model, max_chars
        self.cache_dir, self.device, self.batch_size = Path(cache_dir), device, batch_size
        self._vectors: dict[str, np.ndarray] = {}

    def matrix(self, task: Task) -> np.ndarray:
        if task.name not in self._vectors:
            self._vectors[task.name] = self._load_or_embed(task)
        return self._vectors[task.name]

    def _load_or_embed(self, task: Task) -> np.ndarray:
        texts = [fit_text(t, self.max_chars) for t in task.texts]
        digest = hashlib.sha256("\x00".join([self.model, *texts]).encode()).hexdigest()[:16]
        path = self.cache_dir / f"{self.model.replace('/', '__')}_{digest}.npy"
        if path.exists():
            return np.load(path)
        # One encoder per store, reused across tasks: loading a fresh copy per task (e.g. per
        # systematic review) kept the old copies in GPU memory until the machine swapped.
        if getattr(self, "_encoder", None) is None:
            from sentence_transformers import SentenceTransformer

            self._encoder = SentenceTransformer(self.model, device=self.device)
        encoder = self._encoder
        vectors = encoder.encode(
            texts,
            batch_size=self.batch_size,
            normalize_embeddings=True,
            show_progress_bar=False,
            convert_to_numpy=True,
        ).astype(np.float32)
        path.parent.mkdir(parents=True, exist_ok=True)
        np.save(path, vectors)
        return vectors


class Embedding(Method):
    def __init__(self, store: EmbeddingStore, label: str, head: str = "logreg", tune=False, k=10):
        super().__init__()
        self.store, self.head, self.tune, self.k = store, head, tune, k
        self.name = f"{label}_logreg" if head == "logreg" else f"{label}_knn"

    def fit(self, task, lab):
        e = self.store.matrix(task)
        self.xl_, self.yl_ = e[lab], task.y[lab]
        if self.head == "logreg":
            self.model_ = LogisticHead(tune=self.tune).fit(self.xl_, self.yl_)
        return self

    def predict(self, task, idx):
        xt = self.store.matrix(task)[idx]
        if self.head == "logreg":
            return self.model_.predict(xt)
        return knn_scores(self.xl_, xt, self.yl_, self.k)
