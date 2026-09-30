"""T1: content moderation. Is this comment hate speech? (Measuring Hate Speech, CC-BY-4.0)

Kennedy et al., https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech. One row
per (comment, annotator); each comment has a Rasch-scaled ``hate_speech_score`` built from all its
annotations. PROVISIONAL choices, to be frozen in the T1 pre-registration:

- y = 1 when ``hate_speech_score > 0.5`` (the dataset card's approximate hate-speech cut).
- Only comments with >= 3 annotations, so the consensus does not rest on the reviewer alone.
- The reviewer is one of the comment's real annotators, drawn with a fixed seed; they call it
  hate speech when their ``hatespeech`` rating is 2. ``human_correct`` is whether that call
  matches y. Caveat: their rating also feeds the consensus score, which flatters them slightly.
- Category = platform (within-platform AUROC).
- A fixed random subsample (default 3,000 train pool, 2,000 test) keeps LLM costs bounded.
- Review and label cost: $0.25 per comment (45 s at $20/h).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ldj.task import Task

FILE = "measuring-hate-speech.parquet"


def download(root: str = "data/t1") -> Path:
    from huggingface_hub import hf_hub_download

    return Path(
        hf_hub_download(
            "ucberkeley-dlab/measuring-hate-speech", FILE, repo_type="dataset", local_dir=root
        )
    )


def load(
    root: str = "data/t1",
    n_train: int = 3000,
    n_test: int = 2000,
    min_annotations: int = 3,
    seed: int = 0,
    review_cost: float = 0.25,
    label_cost: float = 0.25,
) -> Task:
    import pandas as pd

    path = Path(root) / FILE
    if not path.exists():
        path = download(root)
    df = pd.read_parquet(
        path,
        columns=[
            "comment_id",
            "annotator_id",
            "platform",
            "hatespeech",
            "hate_speech_score",
            "text",
        ],
    )
    counts = df.groupby("comment_id").size()
    keep = counts[counts >= min_annotations].index
    df = df[df.comment_id.isin(keep)].sort_values(["comment_id", "annotator_id"])
    rng = np.random.default_rng(seed)
    # One reviewer per comment: a seeded random annotation row.
    reviewer = df.groupby("comment_id", sort=True).sample(n=1, random_state=seed)
    comments = df.groupby("comment_id", sort=True).agg(
        text=("text", "first"),
        score=("hate_speech_score", "first"),
        platform=("platform", "first"),
    )
    comments["reviewer_says"] = (
        reviewer.set_index("comment_id").hatespeech.reindex(comments.index) == 2
    )
    ids = comments.index.to_numpy()
    pick = rng.permutation(len(ids))[: n_train + n_test]
    comments = comments.iloc[np.sort(pick)]
    y = (comments.score.to_numpy() > 0.5).astype(float)
    # Every annotator's call per selected comment (1 = rated hate speech, i.e. rating 2), for
    # label-source experiments (ldj.labels). Uses no randomness, so the Task arrays are unchanged.
    calls = (df.hatespeech == 2).groupby(df.comment_id, sort=True).agg(list)
    votes = [np.asarray(calls[c], dtype=np.int8) for c in comments.index]
    order = rng.permutation(len(comments))
    train, test = np.sort(order[:n_train]), np.sort(order[n_train:])
    return Task(
        name="t1_moderation",
        ids=[str(i) for i in comments.index],
        texts=comments.text.tolist(),
        y=y,
        categories=comments.platform.astype(str).to_numpy(),
        train=train,
        test=test,
        review_cost=review_cost,
        human_correct=(comments.reviewer_says.to_numpy() == (y == 1)).astype(float),
        label_cost=label_cost,
        auto_negative=True,
        meta={
            "source": "ucberkeley-dlab/measuring-hate-speech",
            "min_annotations": min_annotations,
            "seed": seed,
            "votes": votes,  # per item, every annotator's 0/1 call
        },
    )
