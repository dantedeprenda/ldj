import numpy as np
import pytest

from ldj import allocate
from ldj.methods.base import BaseRate, Method
from ldj.methods.llm import Precomputed, QuestionFeatures
from ldj.task import Task
from ldj.tasks import synthetic


class Stored(Method):
    """A zero-shot scorer reading a fixed score per item."""

    needs_labels = False

    def __init__(self, p, name="stored"):
        super().__init__()
        self.p, self.name = np.asarray(p, float), name

    def predict(self, task, idx):
        return self.p[idx]


class Spy(Method):
    """A learned method that records which items it was fit on and asked to score."""

    name = "spy"

    def __init__(self):
        super().__init__()
        self.fits, self.preds = [], []

    def fit(self, task, lab):
        self.fits.append(np.asarray(lab).copy())
        return self

    def predict(self, task, idx):
        self.preds.append(np.asarray(idx).copy())
        return task.features["oracle"][idx, 0] * 0.8 + 0.1


CFG = {"budgets": [25, 50], "fit_shares": [0, 0.1, 0.5], "reps": 5, "seed": 0, "min_rest": 20}


def test_fit_and_cert_disjoint_and_never_test(monkeypatch):
    task = synthetic.load(n=400)
    seen = []
    orig = allocate.certified_threshold

    def spy_cert(policy, p_rest, p_cert, y_cert):
        seen.append(len(p_cert))
        return orig(policy, p_rest, p_cert, y_cert)

    monkeypatch.setattr(allocate, "certified_threshold", spy_cert)
    m = Spy()
    rows = allocate.run_group(
        task, [m], allocate.Policy("classify", alpha=0.2), heuristic=False, **CFG
    )
    test = set(task.test.tolist())
    for fit in m.fits:
        assert not set(fit.tolist()) & test
    cert = [r for r in rows if r["arm"] == "certified"]
    assert {r["f"] for r in cert} == {0.1, 0.5}  # learned methods never get f = 0
    for r in cert:
        assert r["n_fit"] + r["n_cert"] == r["B"] and r["n_fit"] >= 1
    assert seen == [r["n_cert"] for r in cert]


def test_draw_split_is_disjoint_and_from_train():
    task = synthetic.load(n=400)
    m = Spy()
    allocate.run_group(task, [m], allocate.Policy("classify", alpha=0.2), heuristic=False, **CFG)
    # each predict call scores rest + cert + test; rest and cert come from train only
    for fit, pred in zip(m.fits, m.preds, strict=True):
        n_test = len(task.test)
        pool_part = pred[:-n_test]
        assert np.array_equal(pred[-n_test:], task.test)
        assert set(pool_part.tolist()) <= set(task.train.tolist())
        assert not set(fit.tolist()) & set(pool_part.tolist())
        assert len(fit) + len(pool_part) == len(task.train)


def test_zero_shot_only_f0_and_scored_once():
    task = synthetic.load(n=400)
    calls = []

    class Counting(Stored):
        def predict(self, task, idx):
            calls.append(len(idx))
            return super().predict(task, idx)

    z = Counting(task.features["oracle"][:, 0] * 0.8 + 0.1)
    rows = allocate.run_group(task, [z], allocate.Policy("accept", alpha=0.3), **CFG)
    assert calls == [task.n]
    cert = [r for r in rows if r["arm"] == "certified"]
    assert {r["f"] for r in cert} == {0.0} and all(r["n_fit"] == 0 for r in cert)
    assert {r["arm"] for r in rows} == {"certified", "heuristic"}


def test_deterministic_given_seed():
    task = synthetic.load(n=400)
    ms = lambda: [
        Stored(task.features["oracle"][:, 0] * 0.8 + 0.1),
        QuestionFeatures(Precomputed("oracle")),
        BaseRate(),
    ]
    cfg = {**CFG, "policy": {"kind": "classify", "alpha": 0.2}}
    a = allocate.run(task, ms(), cfg)
    b = allocate.run(task, ms(), cfg)
    assert a.equals(b)
    c = allocate.run(task, ms(), {**cfg, "seed": 1})
    assert not a.equals(c)


def test_budget_leaving_too_small_a_pool_is_skipped():
    task = synthetic.load(n=400)  # 200 in the train pool
    rows = allocate.run_group(
        task,
        [Stored(np.full(400, 0.5))],
        allocate.Policy("accept", alpha=0.2),
        budgets=[150, 190],
        fit_shares=[0],
        reps=2,
        min_rest=20,
    )
    assert {r["B"] for r in rows} == {150}


def test_policy_needs_alpha():
    with pytest.raises(ValueError):
        allocate.Policy("accept")


def test_classify_conf_loss():
    pol = allocate.Policy("classify", alpha=0.1)
    conf, loss = pol.conf_loss(np.array([0.9, 0.2, 0.6]), np.array([1, 1, 0.0]))
    assert np.allclose(conf, [0.4, 0.3, 0.1]) and loss.tolist() == [0, 1, 1]


def _big_task(n_train, n_test, rng):
    """conf ~ U(0, 1), P(wrong | conf) = 0.4 (1 - conf): selective risk above lambda is
    0.2 (1 - lambda). A huge test split makes test risk ~ population risk."""
    n = n_train + n_test
    p = rng.random(n)
    y = (rng.random(n) >= 0.4 * (1 - p)).astype(float)  # accept policy: wrong when y = 0
    task = Task(
        "big",
        [str(i) for i in range(n)],
        [""] * n,
        y,
        [""] * n,
        np.arange(n_train),
        np.arange(n_train, n),
        1.0,
        1.0,
    )
    return task, p


def test_certified_arm_is_valid_heuristic_is_not():
    rng = np.random.default_rng(5)
    task, p = _big_task(3000, 40000, rng)
    reps = 400
    rows = allocate.run_group(
        task,
        [Stored(p)],
        allocate.Policy("accept", alpha=0.10),
        budgets=[400],
        fit_shares=[0],
        reps=reps,
        min_rest=100,
    )
    cert = [r for r in rows if r["arm"] == "certified"]
    heur = [r for r in rows if r["arm"] == "heuristic"]
    tol = 0.05 + 3 * np.sqrt(0.05 * 0.95 / reps)
    assert np.mean([r["violated"] for r in cert]) <= tol
    assert np.mean([r["certified"] for r in cert]) > 0.3
    assert np.mean([r["violated"] for r in heur]) > 0.2  # reused labels overshoot


def test_recall_arm_is_valid():
    rng = np.random.default_rng(6)
    n_train, n_test = 3000, 40000
    n = n_train + n_test
    y = (rng.random(n) < 0.3).astype(float)
    p = np.where(y == 1, rng.random(n), rng.random(n) ** 3)  # positives U(0, 1)
    task = Task(
        "rec",
        [str(i) for i in range(n)],
        [""] * n,
        y,
        [""] * n,
        np.arange(n_train),
        np.arange(n_train, n),
        1.0,
        1.0,
    )
    reps = 300
    rows = allocate.run_group(
        task,
        [Stored(p)],
        allocate.Policy("recall", target=0.95),
        budgets=[800],
        fit_shares=[0],
        reps=reps,
        min_rest=100,
        heuristic=False,
    )
    tol = 0.05 + 3 * np.sqrt(0.05 * 0.95 / reps)
    assert np.mean([r["violated"] for r in rows]) <= tol
    assert np.mean([r["automated"] for r in rows]) > 0.05


def test_summary_and_b_star():
    task = synthetic.load(n=400)
    cfg = {**CFG, "reps": 20, "policy": {"kind": "classify", "alpha": 0.2}}
    ms = [
        Stored(task.features["oracle"][:, 0] * 0.8 + 0.1),
        QuestionFeatures(Precomputed("oracle")),
    ]
    s = allocate.summarize(allocate.run(task, ms, cfg))
    assert set(s["arm"]) == {"certified", "heuristic"}
    assert (s["n"] == 20).all()
    best, bstar = allocate.b_star(s)
    assert list(best["B"]) == sorted(best["B"])
    assert bstar is None or bstar in (25, 50)
    assert "B*" in allocate.markdown(s, best, bstar)


def test_single_annotator_labels_flip_only_wrong_train_calls():
    from ldj.allocate import single_annotator_labels

    y = np.array([1, 0, 1, 0, 1, 0.0])
    hc = np.array([1, 0, 0, 1, 0, 0.0])  # items 1, 2 wrong in train; 4, 5 wrong in test
    t = Task("toy", list("abcdef"), [""] * 6, y, [""] * 6, [0, 1, 2, 3], [4, 5], 1.0, hc)
    s = single_annotator_labels(t)
    assert s.y.tolist() == [1, 1, 0, 0, 1, 0]  # train flipped where wrong; test untouched
    assert t.y.tolist() == [1, 0, 1, 0, 1, 0]  # original unchanged
    with pytest.raises(ValueError):
        single_annotator_labels(Task("r", ["a"], [""], [1.0], [""], [0], [], 1.0, 0.8))


def test_summarize_reports_useful_spread_and_exact_violation_interval():
    import pandas as pd
    from scipy.stats import beta

    # 10 resamples: 4 useful (2 of them violate), 1 trivially certified (automates nothing)
    rows = pd.DataFrame(
        {
            "method": "m",
            "arm": "certified",
            "f": 0.0,
            "B": 100,
            "rep": range(10),
            "certified": [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            "automated": [0.4, 0.3, 0.2, 0.1, 0.0, 0, 0, 0, 0, 0],
            "auto_per_label": 0.0,
            "violated": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        }
    )
    s = allocate.summarize(rows, delta=0.05).iloc[0]
    assert s["useful"] == pytest.approx(0.4)  # the trivial certificate is not counted
    assert s["violation"] == pytest.approx(0.2)
    assert s["violation_if_useful"] == pytest.approx(0.5)
    assert s["violation_lo"] == pytest.approx(beta.ppf(0.025, 2, 9))
    assert s["violation_hi"] == pytest.approx(beta.ppf(0.975, 3, 8))
    assert s["auto_p50"] == pytest.approx(0.0) and s["auto_p90"] > 0.2
    assert bool(s["consistent"]) == (beta.ppf(0.025, 2, 9) <= 0.05)


def test_features_plus_judge_is_frozen_once_per_task():
    from test_x1 import FakeAnswerer, FakeJudge

    from ldj.methods.llm import QuestionsPlusJudge

    class CountingJudge(FakeJudge):
        calls = 0

        def predict(self, task, idx):
            CountingJudge.calls += 1
            return super().predict(task, idx)

    rng = np.random.default_rng(9)
    task, p = _big_task(400, 300, rng)
    x = rng.random((task.n, 3))
    m = QuestionsPlusJudge(FakeAnswerer(x), CountingJudge(p), "q")
    rows = allocate.run_group(
        task,
        [m],
        allocate.Policy("accept", alpha=0.2),
        budgets=[100],
        fit_shares=[0.5],
        reps=5,
        min_rest=100,
    )
    assert len(rows) == 10 and CountingJudge.calls == 1  # read once, not per refit
