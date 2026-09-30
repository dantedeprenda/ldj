"""Prioritized screening with heuristic and certified stopping (results/w7_t2/).

Every arm produces a complete screening order of a review's pool (labels are revealed as records
are screened, so active learning can adapt); stopping rules are then applied to that order.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import hypergeom
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TARGET = 0.95
ALPHA = 0.05


def seed_pair(y: np.ndarray, rng: np.random.Generator) -> list[int]:
    """One random relevant and one random irrelevant record (screened first, counted)."""
    return [int(rng.choice(np.flatnonzero(y == 1))), int(rng.choice(np.flatnonzero(y == 0)))]


def _desc(score: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Indices by descending score, ties broken at random."""
    return np.lexsort((rng.random(len(score)), -np.asarray(score, float)))


def static_order(score: np.ndarray, seeds: list[int], rng: np.random.Generator) -> np.ndarray:
    rest = np.array([i for i in _desc(score, rng) if i not in set(seeds)], dtype=int)
    return np.concatenate([np.array(seeds, dtype=int), rest])


def features_order(x: np.ndarray, y: np.ndarray, seeds: list[int], rng) -> np.ndarray:
    """(b): a logistic head on the seed records' question answers ranks the rest."""
    x = np.where(np.isnan(x), 0.5, x)
    head = LogisticRegression(C=1.0, max_iter=2000).fit(x[seeds], y[seeds].astype(int))
    return static_order(head.predict_proba(x)[:, 1], seeds, rng)


def active_order(
    tfidf,
    y: np.ndarray,
    seeds: list[int],
    rng: np.random.Generator,
    batch: int = 10,
    prior: np.ndarray | None = None,
) -> np.ndarray:
    """(c)/(d): retrain every ``batch`` screened records and screen the top unscreened ones.
    With ``prior`` (d), priority = mean of the model's rank and the prior's rank."""
    n = len(y)
    screened = list(seeds)
    seen = np.zeros(n, bool)
    seen[seeds] = True
    tie = rng.random(n)
    while len(screened) < n:
        lab = np.array(screened)
        model = LogisticRegression(C=1.0, class_weight="balanced", max_iter=1000)
        model.fit(tfidf[lab], y[lab].astype(int))
        todo = np.flatnonzero(~seen)
        p = model.predict_proba(tfidf[todo])[:, 1]
        if prior is not None:
            p = (_ranks(p) + _ranks(prior[todo])) / 2
        pick = todo[np.lexsort((tie[todo], -p))][:batch]
        screened += pick.tolist()
        seen[pick] = True
    return np.array(screened, dtype=int)


def _ranks(v: np.ndarray) -> np.ndarray:
    """Fractional ranks in [0, 1], higher value = higher rank."""
    order = np.argsort(v, kind="stable")
    r = np.empty(len(v))
    r[order] = np.arange(len(v))
    return r / max(len(v) - 1, 1)


def tfidf_matrix(texts: list[str]):
    return TfidfVectorizer(sublinear_tf=True, min_df=2, stop_words="english").fit_transform(texts)


def heuristic_stop(y_order: np.ndarray, run: int = 50, skip: int = 2) -> int:
    """Records screened when ``run`` consecutive irrelevant ones have been seen (seeds excluded);
    the whole pool if never."""
    streak = 0
    for t, v in enumerate(y_order[skip:], start=skip + 1):
        streak = 0 if v == 1 else streak + 1
        if streak >= run:
            return t
    return len(y_order)


def h0_pvalue(y_order: np.ndarray, t: int, every: int = 5, target: float = TARGET) -> float:
    """Minimum over windows (j, t] of P(X <= k), X ~ Hypergeom(N_pool - j, K_tar, t - j), the
    Callaghan & Mueller-Hansen test of H0: recall < target after t screened records."""
    n_pool = len(y_order)
    cum = np.concatenate([[0], np.cumsum(y_order)])
    r_t = cum[t]
    j = np.arange(0, t, every)
    n = t - j
    k = r_t - cum[j]
    big_n = n_pool - j
    k_tar = np.floor(r_t / target - cum[j]).astype(int) + 1
    p = np.where(k_tar > big_n, 0.0, hypergeom.cdf(k, big_n, np.minimum(k_tar, big_n), n))
    return float(p.min())


def certified_stop(y_order: np.ndarray, alpha: float = ALPHA, every: int = 5) -> int:
    """First t (checked every ``every`` records) where the H0 p-score is below ``alpha``."""
    n = len(y_order)
    for t in range(every, n + 1, every):
        if h0_pvalue(y_order, t, every) < alpha:
            return t
    return n


def outcome(y_order: np.ndarray, t: int) -> dict:
    n, rel = len(y_order), int(y_order.sum())
    recall = float(y_order[:t].sum() / rel) if rel else 1.0
    return {"screened": t, "work_saved": 1 - t / n, "recall": recall, "met": recall >= TARGET}
