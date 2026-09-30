import numpy as np
import pandas as pd
from test_allocate import Stored, _big_task

from ldj import allocate, parallel


def test_split_resamples_give_identical_rows():
    rng = np.random.default_rng(7)
    task, p = _big_task(600, 2000, rng)
    kw = {"fit_shares": [0], "reps": 12, "min_rest": 100, "seed": 3, "group": 0}
    pol = allocate.Policy("accept", alpha=0.10)
    seq = allocate.run_group(task, [Stored(p)], pol, budgets=[100, 200], **kw)
    parts = []
    cache = {}
    for b in (200, 100):  # any order, any chunking
        for ids in ([7, 8, 9, 10, 11], [0, 1, 2], [3, 4, 5, 6]):
            parts += allocate.run_group(
                task, [Stored(p)], pol, budgets=[b], rep_ids=ids, cache=cache, **kw
            )
    pd.testing.assert_frame_equal(parallel.canonical(seq), parallel.canonical(parts))


def test_units_cover_each_affordable_budget_and_resample_once():
    rng = np.random.default_rng(8)
    small, _ = _big_task(150, 100, rng)
    big, _ = _big_task(1000, 100, rng)
    cfg = {"budgets": [25, 100, 800], "reps": 120, "min_rest": 100}
    got = parallel.units(cfg, [small, big], chunk=50)
    seen = {(g, b, r) for g, b, ids in got for r in ids}
    want = {
        (g, b, r)
        for g, pool in ((0, 150), (1, 1000))
        for b in (25, 100, 800)
        if b + 100 <= pool
        for r in range(120)
    }
    assert seen == want and sum(len(ids) for *_, ids in got) == len(want)
