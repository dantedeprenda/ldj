import numpy as np
from scipy.stats import hypergeom

from ldj import screening_al as sa


def _order(rng, n=600, rel=40, sep=1.0):
    y = np.zeros(n, int)
    y[rng.choice(n, rel, replace=False)] = 1
    score = rng.normal(0, 1, n) + sep * y
    return y[np.argsort(-score, kind="stable")]


def test_h0_pvalue_matches_one_window_by_hand():
    y = np.array([1, 1, 0, 1, 0, 0, 0, 0, 0, 0] + [0] * 90)
    t, every = 10, 10  # only the window j = 0: all 10 records, 3 relevant seen
    k_tar = int(np.floor(3 / 0.95 - 0)) + 1
    want = hypergeom.cdf(3, 100, k_tar, 10)
    assert abs(sa.h0_pvalue(y, t, every) - want) < 1e-12


def test_certified_stop_keeps_recall_heuristic_does_not():
    rng = np.random.default_rng(0)
    runs = 150
    cert_ok = heur_ok = 0
    for _ in range(runs):
        yo = _order(rng, sep=0.8)  # a weak ranker
        cert_ok += sa.outcome(yo, sa.certified_stop(yo))["met"]
        heur_ok += sa.outcome(yo, sa.heuristic_stop(yo))["met"]
    assert cert_ok / runs >= 0.93
    assert heur_ok < cert_ok


def test_certified_stop_valid_on_random_order_and_saves_work_on_good_ranker():
    rng = np.random.default_rng(1)
    ok = 0
    for _ in range(100):
        y = np.zeros(600, int)
        y[rng.choice(600, 40, replace=False)] = 1
        ok += sa.outcome(y, sa.certified_stop(y))["met"]
    assert ok / 100 >= 0.93
    good = _order(np.random.default_rng(2), sep=4.0)
    assert sa.outcome(good, sa.certified_stop(good))["work_saved"] > 0.3


def test_orders_are_permutations_starting_with_seeds():
    rng = np.random.default_rng(3)
    n = 120
    y = (rng.random(n) < 0.2).astype(int)
    texts = [("cancer trial " if v else "unrelated topic ") + f"w{rng.integers(0, 30)}" for v in y]
    tf = sa.tfidf_matrix(texts)
    seeds = sa.seed_pair(y, rng)
    for order in (
        sa.static_order(rng.random(n), seeds, rng),
        sa.features_order(rng.random((n, 4)), y, seeds, rng),
        sa.active_order(tf, y, seeds, rng, batch=10),
        sa.active_order(tf, y, seeds, rng, batch=10, prior=rng.random(n)),
    ):
        assert sorted(order.tolist()) == list(range(n)) and order[:2].tolist() == seeds
    # active learning on separable text finds relevant records early
    al = sa.active_order(tf, y, seeds, rng, batch=10)
    assert y[al[: int(y.sum()) + 10]].mean() > 0.6
