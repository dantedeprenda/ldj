import numpy as np

from ldj.tasks.moderation_shift import halves


def _cats():
    rng = np.random.default_rng(0)
    return rng.choice(np.array(["0", "2", "3"]), size=900)


def test_halves_partition_one_platform_and_are_fixed_by_seed():
    cats = _cats()
    for p in ("0", "2", "3"):
        pool, test = halves(cats, p, seed=0)
        both = np.concatenate([pool, test])
        assert set(both) == set(np.flatnonzero(cats == p))  # only that platform, all of it
        assert len(np.intersect1d(pool, test)) == 0
        assert abs(len(pool) - len(test)) <= 1
        again = halves(cats, p, seed=0)
        assert np.array_equal(pool, again[0]) and np.array_equal(test, again[1])
    assert not np.array_equal(halves(cats, "0", seed=0)[0], halves(cats, "0", seed=1)[0])


def test_source_pool_and_target_halves_never_overlap_across_platforms():
    cats = _cats()
    src_pool, _ = halves(cats, "0")
    tgt_pool, tgt_test = halves(cats, "2")
    for a, b in ((src_pool, tgt_pool), (src_pool, tgt_test), (tgt_pool, tgt_test)):
        assert len(np.intersect1d(a, b)) == 0


def test_control_test_half_is_disjoint_from_its_label_pool():
    cats = _cats()
    pool, test = halves(cats, "3")
    assert len(np.intersect1d(pool, test)) == 0 and (cats[test] == "3").all()
