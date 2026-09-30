import numpy as np
import pytest

from ldj.labels import vote_label, vote_labels
from ldj.task import Task


def _task():
    votes = [
        np.array([1, 1, 1]),
        np.array([0, 0, 0]),
        np.array([1, 0, 1, 0, 1]),
        np.array([1, 0, 0, 1]),
        np.array([1, 1, 0]),
        np.array([0, 1, 1]),
    ]
    t = Task(
        "toy",
        list("abcdef"),
        [""] * 6,
        np.array([1, 0, 1, 0, 1, 0.0]),
        [""] * 6,
        [0, 1, 2, 3],
        [4, 5],
        1.0,
        1.0,
    )
    t.meta["votes"] = votes
    return t, votes


def test_unanimous_items_get_their_vote_and_test_is_untouched():
    t, _ = _task()
    for src in ("one_vote", "majority3"):
        s = vote_labels(t, src, seed=3)
        assert s.y[0] == 1 and s.y[1] == 0  # unanimous
        assert s.y[4] == t.y[4] and s.y[5] == t.y[5]  # test labels unchanged
        assert t.y.tolist() == [1, 0, 1, 0, 1, 0]  # original untouched


def test_seeded_and_order_independent():
    t, votes = _task()
    a = vote_labels(t, "one_vote", seed=7).y
    b = vote_labels(t, "one_vote", seed=7).y
    assert np.array_equal(a, b)
    # an item's label depends only on (seed, item), not on which items are in train
    assert vote_label(votes[3], "one_vote", 7, 3) == a[3]


def test_majority3_is_majority_of_three_distinct_annotators():
    votes = np.array([1, 0, 1, 0, 1, 0, 0])
    for seed in range(50):
        rng = np.random.default_rng([seed, 9])
        pick = rng.choice(len(votes), 3, replace=False)
        assert vote_label(votes, "majority3", seed, 9) == int(votes[pick].sum() >= 2)
    with pytest.raises(ValueError):
        vote_label(np.array([1, 0]), "majority3", 0, 0)
    with pytest.raises(ValueError):
        vote_label(votes, "median", 0, 0)
