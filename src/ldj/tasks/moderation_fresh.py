"""T1-fresh: 5,000 Measuring Hate Speech comments that T1 never used.

Same source, eligibility (>= 3 annotations), label (consensus score > 0.5), reviewer rule and
costs as ``moderation.load``. The 5,000 comments T1 used are reproduced exactly (the same seeded
permutation of the eligible comments) and excluded; a new seed then draws 5,000 of the remaining
12,352 and splits them into a 3,000 pool and a 2,000 test set. This tests repeatability on the
same source, not transfer to another platform.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ldj.task import Task
from ldj.tasks.moderation import FILE


def used_ids(df, min_annotations: int = 3, seed: int = 0, n: int = 5000) -> set:
    """The comment ids ``moderation.load`` selects (same eligibility, order and permutation)."""
    counts = df.groupby("comment_id").size()
    ids = np.sort(counts[counts >= min_annotations].index.to_numpy())
    pick = np.random.default_rng(seed).permutation(len(ids))[:n]
    return set(ids[pick].tolist())


def load(
    root: str = "data/t1",
    n_train: int = 3000,
    n_test: int = 2000,
    min_annotations: int = 3,
    seed: int = 2026,
    t1_seed: int = 0,
    split_seed: int | None = None,
    review_cost: float = 0.25,
    label_cost: float = 0.25,
) -> Task:
    import pandas as pd

    df = pd.read_parquet(
        Path(root) / FILE,
        columns=[
            "comment_id",
            "annotator_id",
            "platform",
            "hatespeech",
            "hate_speech_score",
            "text",
        ],
    )
    used = used_ids(df, min_annotations, t1_seed)
    counts = df.groupby("comment_id").size()
    keep = counts[counts >= min_annotations].index
    df = df[df.comment_id.isin(keep) & ~df.comment_id.isin(used)]
    df = df.sort_values(["comment_id", "annotator_id"])
    rng = np.random.default_rng(seed)
    reviewer = df.groupby("comment_id", sort=True).sample(n=1, random_state=seed)
    comments = df.groupby("comment_id", sort=True).agg(
        text=("text", "first"),
        score=("hate_speech_score", "first"),
        platform=("platform", "first"),
    )
    comments["reviewer_says"] = (
        reviewer.set_index("comment_id").hatespeech.reindex(comments.index) == 2
    )
    pick = rng.permutation(len(comments))[: n_train + n_test]
    comments = comments.iloc[np.sort(pick)]
    y = (comments.score.to_numpy() > 0.5).astype(float)
    # split_seed re-draws only the pool/test split of the same 5,000 comments (exploratory
    # follow-up to W5); None keeps the pre-registered split exactly.
    split_rng = rng if split_seed is None else np.random.default_rng([seed, split_seed])
    order = split_rng.permutation(len(comments))
    train, test = np.sort(order[:n_train]), np.sort(order[n_train:])
    return Task(
        name="t1_fresh",
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
            "seed": seed,
            "excludes": f"the {len(used)} comments T1 used (seed {t1_seed})",
        },
    )
