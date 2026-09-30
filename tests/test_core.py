import numpy as np
import pytest

from ldj import metrics
from ldj.cost import Prices, choose_thresholds, item_costs, summarize
from ldj.task import Task, k_shot


def test_auroc_and_ties():
    y = np.array([0, 0, 1, 1.0])
    assert metrics.auroc(np.array([0.1, 0.2, 0.8, 0.9]), y) == 1.0
    assert metrics.auroc(np.full(4, 0.5), y) == 0.5


def test_risk_coverage_ties_give_expected_risk():
    # all tied: accepting i items has expected risk = base failure rate at every i
    y = np.array([1, 0, 1, 1.0])
    rc = metrics.risk_coverage(np.full(4, 0.3), y)
    assert np.allclose(rc, 0.25)
    assert metrics.aurc(np.array([0.9, 0.1, 0.8, 0.7]), y) == pytest.approx(
        np.mean([0, 0, 0, 0.25])
    )


def test_within_needs_min_class():
    y = np.array([1.0] * 5 + [0.0] * 5)
    cats = np.array(["a"] * 10)
    ident = np.arange(10)[None, :]
    assert np.isnan(metrics.within_rows(np.linspace(0, 1, 10), y, cats, ident)[0])


def test_k_shot_uniform_matches_paper_rule_and_min_each():
    train = np.arange(100)
    rng = np.random.default_rng(42)
    assert np.array_equal(k_shot(train, 25, 42), np.sort(rng.choice(train, 25, replace=False)))
    y = np.zeros(100)
    y[:3] = 1
    lab = k_shot(train, 5, 0, y=y, min_each=1)
    assert len(lab) == 5 and y[lab].sum() >= 1 and (1 - y[lab]).sum() >= 1
    assert k_shot(train, None, 0) is train


def test_task_rejects_overlap():
    with pytest.raises(ValueError):
        Task("x", ["a", "b"], ["a", "b"], [0, 1], ["", ""], [0], [0], 1.0, 1.0)


def _toy(auto_negative=True):
    y = np.array([1, 1, 1, 0, 0, 0.0])
    return Task(
        "toy",
        list("abcdef"),
        list("abcdef"),
        y,
        [""] * 6,
        [0, 1, 2],
        [3, 4, 5],
        review_cost=1.0,
        human_correct=1.0,
        auto_negative=auto_negative,
    )


def test_item_costs_actions():
    t = _toy()
    pr = Prices(c_fp=10, c_fn=5, volume=1)
    idx = np.arange(6)
    p = np.array([0.9, 0.9, 0.1, 0.9, 0.5, 0.1])
    c = item_costs(t, idx, p, 0.2, 0.8, pr)
    # right pos, right pos, wrong neg (5), wrong pos (10), defer (1), right neg
    assert c["cost"].tolist() == [0, 0, 5, 10, 1, 0]
    t2 = _toy(auto_negative=False)
    c2 = item_costs(t2, idx, p, 0.2, 0.8, pr)
    assert c2["cost"].tolist() == [0, 0, 1, 10, 1, 1]  # negatives are deferred


def test_choose_thresholds_matches_brute_force():
    rng = np.random.default_rng(1)
    n = 40
    y = (rng.random(n) < 0.5).astype(float)
    t = Task(
        "r",
        [str(i) for i in range(n)],
        ["x"] * n,
        y,
        [""] * n,
        np.arange(n),
        [],
        review_cost=rng.random(n),
        human_correct=0.9,
        auto_cost=rng.random(n) * 0.1,
    )
    p = np.round(np.clip(y * 0.3 + rng.random(n) * 0.7, 0, 1), 1)  # ties on purpose
    lab = np.arange(n)
    for rule in ["empirical", "ucb"]:
        for pr in [Prices(1, 1), Prices(5, 0.5), Prices(0.1, 3)]:
            t_lo, t_hi = choose_thresholds(t, lab, p, pr, rule=rule)
            got = summarize(t, lab, p, t_lo, t_hi, pr, 0)["cost_per_item"]
            if rule == "empirical":
                cands = np.concatenate([[-np.inf], np.unique(p), [np.inf]])
                best = min(
                    summarize(t, lab, p, lo, hi, pr, 0)["cost_per_item"]
                    for hi in cands
                    for lo in cands
                    if lo < hi
                )
                assert got == pytest.approx(best)


def test_synthetic_end_to_end(tmp_path):
    from ldj.run import run

    cfg = {
        "name": "synthetic_e2e",
        "task": {"name": "synthetic"},
        "cache": str(tmp_path / "calls.sqlite"),
        "methods": [
            {"type": "base_rate"},
            {"type": "tfidf"},
            {"type": "questions", "label": "oracle", "answerer": {"precomputed": "oracle"}},
            {
                "type": "judge",
                "label": "stub",
                "backend": {"kind": "stub"},
                "instruction": "Is the item positive?",
                "shots": [0, 4],
            },
        ],
        "ks": [10, 50, "all"],
        "seeds": [0, 1],
        "draw": {"min_each": 1, "min_each_below": 25},
        "prices": [{"c_fp": 1.0, "c_fn": 1.0, "volume": 1000}],
    }
    records = run(cfg, str(tmp_path))
    by = {(r["method"], r["k"], r["seed"]): r for r in records}
    assert by[("oracle_features", "50", 0)]["auroc"] > 0.8
    assert by[("stub_0shot", "10", 0)]["auroc"] > 0.8  # stub reads the word 'positive'
    assert by[("base_rate", "50", 0)]["auroc"] == 0.5
    assert (tmp_path / "synthetic_e2e" / "summary.md").exists()
    pol = by[("oracle_features", "all", 0)]["policies"]
    assert {p["rule"] for p in pol} == {"empirical", "ucb"}
    # a good predictor at c_fp = c_fn = $1 should cost less than deferring everything ($0.25 +
    # 10% reviewer error)
    assert pol[0]["cost_per_item"] < 0.25 + 0.1


def test_wss_perfect_and_random():
    y = np.array([1.0] * 10 + [0.0] * 90)
    assert metrics.wss(np.linspace(1, 0, 100), y) == pytest.approx(0.90 - 0.05)
    assert abs(metrics.wss(np.zeros(100), y)) < 0.1  # all tied: about no work saved


def test_recall_threshold_rules():
    from ldj.cost import recall_threshold

    n = 200
    y = np.array([1.0] * 40 + [0.0] * 160)
    t = Task(
        "s",
        [str(i) for i in range(n)],
        ["x"] * n,
        y,
        [""] * n,
        np.arange(n),
        [],
        review_cost=1.0,
        human_correct=0.9,
    )
    p = np.concatenate([np.linspace(0.5, 1, 40), np.linspace(0, 0.6, 160)])
    lo, hi = recall_threshold(t, np.arange(n), p, 0.95, "empirical")
    assert hi == np.inf and (p[y == 1] > lo).mean() >= 0.95 and (p <= lo).mean() > 0.5
    # 40 positives cannot certify 95% recall at 90% confidence: reject nothing
    assert recall_threshold(t, np.arange(n), p, 0.95, "ucb")[0] == -np.inf


def test_per_category_run(tmp_path):
    from ldj.run import run

    cfg = {
        "name": "percat",
        "task": {"name": "synthetic", "n": 600},
        "cache": str(tmp_path / "c.sqlite"),
        "methods": [{"type": "tfidf", "heads": ["logreg"]}, {"type": "category_prior"}],
        "ks": [20, "all"],
        "seeds": [0, 1],
        "per_category": True,
        "wss": True,
        "draw": {"min_each": 1, "min_each_below": 25},
        "prices": [{"c_fp": 1.0, "c_fn": 5.0}],
        "recall_targets": [0.95],
    }
    records = run(cfg, str(tmp_path))
    r = next(r for r in records if r["method"] == "tfidf_logreg" and r["k"] == "all")
    assert r["n_lab"] == 300 and r["within_auroc"] > 0.8 and r["wss95"] > 0
    rules = {p["rule"] for p in r["policies"]}
    assert rules == {"empirical", "ucb", "recall95_empirical", "recall95_ucb"}
