"""A small synthetic task for tests: the word 'positive' marks y = 1, with label noise."""

from __future__ import annotations

import numpy as np

from ldj.task import Task


def load(n: int = 400, seed: int = 0, noise: float = 0.1) -> Task:
    rng = np.random.default_rng(seed)
    y = (rng.random(n) < 0.4).astype(float)
    shown = np.where(rng.random(n) < noise, 1 - y, y)
    filler = ["alpha", "beta", "gamma", "delta", "omega"]
    texts = [
        " ".join(rng.choice(filler, 6)) + (" positive" if s else " negative") + f" item{i}"
        for i, s in enumerate(shown)
    ]
    cats = np.where(np.arange(n) % 2 == 0, "a", "b")
    idx = rng.permutation(n)
    return Task(
        name=f"synthetic_{seed}",
        ids=[f"s{i}" for i in range(n)],
        texts=texts,
        y=y,
        categories=cats,
        train=np.sort(idx[: n // 2]),
        test=np.sort(idx[n // 2 :]),
        review_cost=0.25,
        human_correct=0.9,
        label_cost=0.25,
        features={"oracle": np.stack([shown, rng.random(n)], axis=1)},
    )
