"""One format for every decision task, plus label-budget draws.

A task is a binary decision over text items. ``y[i] = 1`` is the outcome the automated system
may act on alone (the cheap model suffices, the comment is hateful, the abstract is included).
For each item the task also records what acting and deferring cost and whether the human
reviewer would have got it right, so every method is priced by one cost model
(:mod:`ldj.cost`).

``auto_negative`` says whether a confident negative can be acted on without a human. In
moderation and screening both outcomes can be automated. In routing a predicted failure of the
cheap model *is* the escalation, so negatives always go to the reviewer (the strong model).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class Task:
    name: str
    ids: list[str]
    texts: list[str]
    y: np.ndarray  # (n,) 0/1
    categories: np.ndarray  # (n,) str; "" when the task has none
    train: np.ndarray  # indices a method may draw labels from
    test: np.ndarray  # indices it is scored on; never labeled
    review_cost: np.ndarray  # (n,) USD to defer the item to the reviewer
    human_correct: np.ndarray  # (n,) P(reviewer's decision is right), realized 0/1 or a rate
    auto_cost: np.ndarray | None = None  # (n,) USD of acting automatically (routing: cheap model)
    label_cost: float = 0.0  # USD to obtain one training label
    auto_negative: bool = True
    features: dict[str, np.ndarray] = field(default_factory=dict)  # precomputed, (n, d) each
    meta: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        n = len(self.texts)
        self.y = np.asarray(self.y, dtype=float)
        self.categories = np.asarray(self.categories, dtype=str)
        self.train = np.asarray(self.train, dtype=int)
        self.test = np.asarray(self.test, dtype=int)
        self.review_cost = np.broadcast_to(np.asarray(self.review_cost, float), (n,)).copy()
        self.human_correct = np.broadcast_to(np.asarray(self.human_correct, float), (n,)).copy()
        if self.auto_cost is None:
            self.auto_cost = np.zeros(n)
        for name, arr in [("ids", self.ids), ("y", self.y), ("categories", self.categories)]:
            if len(arr) != n:
                raise ValueError(f"{self.name}: {name} has {len(arr)} entries, texts has {n}")
        if not set(np.unique(self.y)) <= {0.0, 1.0}:
            raise ValueError(f"{self.name}: y must be 0/1")
        if np.intersect1d(self.train, self.test).size:
            raise ValueError(f"{self.name}: train and test overlap")

    @property
    def n(self) -> int:
        return len(self.texts)

    def subset(self, category: str) -> Task:
        """The items of one category as a task of their own (e.g. one systematic review)."""
        keep = np.flatnonzero(self.categories == category)
        pos = {int(i): j for j, i in enumerate(keep)}
        return Task(
            name=f"{self.name}/{category}",
            ids=[self.ids[i] for i in keep],
            texts=[self.texts[i] for i in keep],
            y=self.y[keep],
            categories=self.categories[keep],
            train=np.array([pos[int(i)] for i in self.train if int(i) in pos], dtype=int),
            test=np.array([pos[int(i)] for i in self.test if int(i) in pos], dtype=int),
            review_cost=self.review_cost[keep],
            human_correct=self.human_correct[keep],
            auto_cost=self.auto_cost[keep],
            label_cost=self.label_cost,
            auto_negative=self.auto_negative,
            features={k: v[keep] for k, v in self.features.items()},
            meta=self.meta,
        )


def k_shot(
    train: np.ndarray, k: int | None, seed: int, y: np.ndarray | None = None, min_each: int = 0
) -> np.ndarray:
    """The labeled examples a method may learn from; ``None`` means the whole train split.

    ``min_each = 0`` draws uniformly, exactly as the routing paper did (so its numbers
    reproduce). ``min_each > 0`` guarantees that many of each outcome, the rule for very small
    budgets where a uniform draw can contain only one outcome.
    """
    if k is None or k >= len(train):
        return np.asarray(train)
    rng = np.random.default_rng(seed)
    if not min_each:
        return np.sort(rng.choice(train, k, replace=False))
    if y is None:
        raise ValueError("min_each needs y")
    pos, neg = train[y[train] == 1], train[y[train] == 0]
    if 2 * min_each > k or len(pos) < min_each or len(neg) < min_each:
        raise ValueError(f"cannot draw {min_each} of each outcome in k={k}")
    forced = np.concatenate(
        [rng.choice(pos, min_each, replace=False), rng.choice(neg, min_each, replace=False)]
    )
    rest = np.setdiff1d(train, forced)
    return np.sort(np.concatenate([forced, rng.choice(rest, k - 2 * min_each, replace=False)]))


def fit_text(text: str, max_chars: int | None) -> str:
    """Truncate to ``max_chars`` keeping the head (task statement) and the tail (latest part)."""
    if not max_chars or len(text) <= max_chars:
        return text
    head = max_chars // 3
    tail = max_chars - head - 5
    return f"{text[:head]}\n...\n{text[-tail:]}"
