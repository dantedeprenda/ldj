"""T1 platform shift: certify on one Measuring Hate Speech platform, deploy
on another.

The task keeps all of T1's 5,000 comments (so cached LLM answers match item by item). Each platform
is split once (seed 0) into a pool half and a test half. ``train`` is the source platform's pool
half (labels and the naive threshold grid come from here); ``test`` is the target platform's test
half; ``meta["target_pool"]`` is the target's pool half, whose unlabeled scores may build the grid.
Source = target gives the in-platform control.
"""

from __future__ import annotations

import numpy as np

from ldj.task import Task
from ldj.tasks import moderation


def halves(categories: np.ndarray, platform: str, seed: int = 0) -> tuple[np.ndarray, np.ndarray]:
    """(pool half, test half) of one platform's items, fixed by ``seed``."""
    idx = np.flatnonzero(categories == str(platform))
    perm = np.random.default_rng([seed, int(platform)]).permutation(idx)
    cut = len(perm) // 2
    return np.sort(perm[:cut]), np.sort(perm[cut:])


def load(source_platform: int, target_platform: int, seed: int = 0, **t1_kwargs) -> Task:
    base = moderation.load(**t1_kwargs)
    src_pool, _ = halves(base.categories, str(source_platform), seed)
    tgt_pool, tgt_test = halves(base.categories, str(target_platform), seed)
    return Task(
        name=f"t1_shift_{source_platform}to{target_platform}",
        ids=base.ids,
        texts=base.texts,
        y=base.y,
        categories=base.categories,
        train=src_pool,
        test=tgt_test,
        review_cost=base.review_cost,
        human_correct=base.human_correct,
        label_cost=base.label_cost,
        auto_negative=base.auto_negative,
        meta={
            **base.meta,
            "source_platform": source_platform,
            "target_platform": target_platform,
            "target_pool": tgt_pool,
        },
    )
