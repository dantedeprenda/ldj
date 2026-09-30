"""Train-pool label sources built from individual annotators' calls.

T1 comments carry every annotator's 0/1 call (``task.meta["votes"]``). This module replaces the
train-pool labels (fitting and certification) with:

- ``one_vote``: one randomly chosen annotator's call per item (a fresh seeded draw, independent of
  the fixed reviewer behind ``human_correct`` / ``allocate.single_annotator_labels``);
- ``majority3``: the majority of 3 annotators drawn at random without replacement per item.

Test labels stay the consensus, so certificates built on these labels are judged against it.
Each item's draw is seeded by (seed, item index), so it does not depend on which items are
labeled or in what order.
"""

from __future__ import annotations

from dataclasses import replace

import numpy as np

from ldj.task import Task

SOURCES = ("one_vote", "majority3")


def vote_label(votes: np.ndarray, source: str, seed: int, item: int) -> int:
    rng = np.random.default_rng([seed, item])
    votes = np.asarray(votes, int)
    if source == "one_vote":
        return int(votes[rng.integers(len(votes))])
    if source == "majority3":
        if len(votes) < 3:
            raise ValueError(f"item {item} has {len(votes)} annotations; majority3 needs 3")
        return int(votes[rng.choice(len(votes), 3, replace=False)].sum() >= 2)
    raise ValueError(f"unknown label source {source!r}; use one of {SOURCES}")


def vote_labels(task: Task, source: str, seed: int = 0) -> Task:
    """The task with train-pool labels replaced by ``source``; test labels untouched."""
    votes = task.meta.get("votes")
    if votes is None:
        raise ValueError(f"{task.name}: no per-annotator votes in task.meta")
    y = task.y.copy()
    for i in np.asarray(task.train):
        y[i] = vote_label(votes[i], source, seed, int(i))
    return replace(task, y=y)
