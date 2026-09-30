import numpy as np
import pytest

from ldj import bridge


def _paired():
    # items: both right, only default, only fallback, both wrong, only fallback, both right
    d = np.array([1, 1, 0, 0, 0, 1])
    f = np.array([1, 0, 1, 0, 1, 1])
    return bridge.Paired(d, f, np.full(6, 1.0), np.full(6, 10.0))


def test_table_cells_and_escalation_value():
    t = bridge.table(_paired())
    assert (
        t["both_right"],
        t["only_default_right"],
        t["only_fallback_right"],
        t["both_wrong"],
    ) == (
        2,
        1,
        2,
        1,
    )
    assert t["escalation_value"] == pytest.approx((2 - 1) / 6)
    assert t["discordant_share"] == pytest.approx(3 / 6)


def test_outcome_matches_brute_force():
    p = _paired()
    rng = np.random.default_rng(0)
    for _ in range(50):
        mask = rng.random(6) < 0.5
        o = bridge.outcome(p, mask)
        final = [p.fallback_ok[i] if mask[i] else p.default_ok[i] for i in range(6)]
        assert o["accuracy"] == pytest.approx(np.mean(final))
        assert o["cost"] == pytest.approx(np.mean([10.0 if m else 1.0 for m in mask]))
        assert o["net_per_item"] == pytest.approx(o["accuracy"] - p.default_ok.mean())


def test_escalate_top_rate_and_random_ties():
    s = np.array([0.9, 0.5, 0.5, 0.5, 0.1, 0.0])
    m = bridge.escalate_top(s, 0.5)
    assert m.sum() == 3 and m[0]
    # a constant score escalates a random subset, not the first items
    picks = {tuple(bridge.escalate_top(np.zeros(20), 0.25, seed=k)) for k in range(5)}
    assert len(picks) > 1


def test_oracle_is_an_upper_bound():
    p = _paired()
    rng = np.random.default_rng(1)
    for rate in (1 / 6, 2 / 6, 3 / 6):
        best = bridge.outcome(p, bridge.oracle_mask(p, rate))["net_per_item"]
        for _ in range(30):
            other = bridge.outcome(p, bridge.escalate_top(rng.random(6), rate))["net_per_item"]
            assert other <= best + 1e-12


def test_net_ci_brackets_mean_and_rejects_bad_input():
    p = _paired()
    mean, lo, hi = bridge.net_ci(p, [bridge.oracle_mask(p, 0.5)])
    assert lo <= mean <= hi
    with pytest.raises(ValueError):
        bridge.Paired(np.array([1, 2]), np.array([1, 0]), np.ones(2), np.ones(2))


def test_frontier_matches_outcome_and_at_cost_interpolates():
    p = _paired()
    s = np.array([0.1, 0.9, 0.8, 0.5, 0.7, 0.2])
    cost, acc = bridge.frontier(p, s)
    for m in range(7):
        o = bridge.outcome(p, bridge.escalate_top(s, m / 6))
        assert acc[m] == pytest.approx(o["accuracy"]) and cost[m] == pytest.approx(o["cost"])
    mid = (cost[1] + cost[2]) / 2
    assert bridge.at_cost(cost, acc, mid) == pytest.approx((acc[1] + acc[2]) / 2)
    assert np.isnan(bridge.at_cost(cost, acc, cost[-1] + 1))
    # bootstrap weights of 2 on every item change nothing
    c2, a2 = bridge.frontier(p, s, w=np.full(6, 2.0))
    assert np.allclose(c2, cost) and np.allclose(a2, acc)


def test_report_csv_end_to_end(tmp_path):
    import pandas as pd

    p = _paired()
    f = tmp_path / "paired.csv"
    pd.DataFrame(
        {
            "item": list("abcdef"),
            "default_ok": p.default_ok,
            "fallback_ok": p.fallback_ok,
            "default_cost": p.default_cost,
            "fallback_cost": p.fallback_cost,
            "risk": [0.1, 0.9, 0.8, 0.5, 0.7, 0.2],
        }
    ).to_csv(f, index=False)
    text = bridge.report_csv(str(f), ["risk"], [0.5])
    assert "| 2 | 1 | 2 | 1 | +0.167 |" in text and "| 50% | risk |" in text
    bad = tmp_path / "bad.csv"
    pd.DataFrame(
        {"default_ok": [1], "fallback_ok": [None], "default_cost": [1], "fallback_cost": [2]}
    ).to_csv(bad, index=False)
    with pytest.raises(ValueError):
        bridge.report_csv(str(bad), [], [0.5])
