import numpy as np
import pytest
from scipy.stats import binom

from ldj import certify


def test_cp_upper_matches_binomial_test_brute_force():
    # the bound is the alpha where P(X <= e | n, alpha) crosses delta
    delta = 0.05
    for n in [1, 5, 25, 60]:
        for e in range(n + 1):
            u = float(certify.cp_upper(e, n, delta))
            if e == n:
                assert u == 1.0
                continue
            assert binom.cdf(e, n, u) == pytest.approx(delta, abs=1e-9)
            for a in np.linspace(0.01, 0.99, 99):
                assert (u <= a) == (binom.cdf(e, n, a) <= delta + 1e-12)
    assert float(certify.cp_upper(0, 0, delta)) == 1.0


def test_min_accepted_known_values():
    assert certify.min_accepted(0.10, 0.05) == 29  # 0.9^29 = 0.047 < 0.05 < 0.9^28
    assert certify.min_accepted(0.05, 0.05) == 59  # the screening "59 positives" figure
    for a, d in [(0.1, 0.05), (0.21, 0.05), (0.05, 0.1)]:
        n = certify.min_accepted(a, d)
        assert certify.cp_upper(0, n, d) <= a < certify.cp_upper(0, n - 1, d)


def test_pool_thresholds_give_requested_coverage():
    pool = np.arange(1000) / 1000
    for c in [0.01, 0.25, 0.5, 1.0]:
        t = certify.pool_thresholds(pool, [c])[0]
        assert (pool >= t).mean() == pytest.approx(c)


def test_coverage_grid_starts_where_zero_errors_could_pass():
    g = certify.coverage_grid(200, 0.10, 0.05)
    assert g[0] == pytest.approx(0.29) and g[-1] == pytest.approx(1.0)  # 2 x 29 / 200
    assert np.all(np.diff(g) > 0)
    assert certify.coverage_grid(10, 0.10, 0.05).tolist() == [1.0]


def _naive_risk(conf, loss, thresholds, alpha, delta, method):
    """Loop version of certify_risk to check the vectorized one against."""
    m = len(thresholds)
    level = delta if method == "fixed_sequence" else delta / m
    passed = []
    for t in thresholds:
        acc = conf >= t
        n, e = int(acc.sum()), int(loss[acc].sum())
        u = 1.0 if n == 0 or e == n else float(certify.cp_upper(e, n, level))
        passed.append(u <= alpha)
    if method == "fixed_sequence":
        best = -1
        for i, ok in enumerate(passed):
            if not ok:
                break
            best = i
        return best
    return max([i for i, ok in enumerate(passed) if ok], default=-1)


@pytest.mark.parametrize("method", ["fixed_sequence", "bonferroni"])
def test_certify_risk_matches_brute_force(method):
    rng = np.random.default_rng(3)
    for _ in range(200):
        n = int(rng.integers(0, 80))
        conf = np.round(rng.random(n), 1)  # coarse, so ties are common
        loss = (rng.random(n) < 0.3 * (1 - conf)).astype(float)
        thr = np.sort(rng.random(int(rng.integers(1, 15))))[::-1]
        alpha = float(rng.choice([0.1, 0.2, 0.3]))
        cert = certify.certify_risk(conf, loss, thr, alpha, 0.05, method)
        assert cert.index == _naive_risk(conf, loss, thr, alpha, 0.05, method)
        assert cert.counts.tolist() == [int((conf >= t).sum()) for t in thr]


def test_certify_recall_matches_brute_force():
    rng = np.random.default_rng(4)
    for _ in range(200):
        n = int(rng.integers(0, 300))
        y = (rng.random(n) < 0.3).astype(float)
        s = np.round(np.where(y == 1, rng.random(n) ** 0.5, rng.random(n)), 2)
        thr = np.sort(rng.random(int(rng.integers(1, 15))))
        cert = certify.certify_recall(s, y, thr, 0.9, 0.05)
        best = -1
        for i, t in enumerate(thr):
            n_pos, miss = int(y.sum()), int(((s < t) & (y == 1)).sum())
            if not (n_pos and certify.cp_lower(n_pos - miss, n_pos, 0.05) >= 0.9):
                break
            best = i
        assert cert.index == best


def test_grid_order_is_checked():
    with pytest.raises(ValueError):
        certify.certify_risk([0.5], [0], [0.1, 0.9], 0.1)
    with pytest.raises(ValueError):
        certify.certify_recall([0.5], [1], [0.9, 0.1])


def test_nothing_certified_automates_nothing():
    out = certify.risk_outcome([0.9, 0.1], [1, 1], float("nan"), 0.1)
    assert out == {"coverage": 0.0, "risk": 0.0, "violated": False}
    out = certify.recall_outcome([0.9, 0.1], [1, 1], float("nan"), 0.95)
    assert out["work_saved"] == 0.0 and out["recall"] == 1.0


# Simulations with known population curves: the realized violation rate over many draws of
# the certification sample must stay at or below delta. Tolerance is 3 binomial SEs.

REPS = 2000
DELTA = 0.05
TOL = DELTA + 3 * np.sqrt(DELTA * (1 - DELTA) / REPS)


def _true_risk(lam):
    # conf ~ U(0, 1) and P(wrong | conf) = 0.4 (1 - conf), so risk among conf >= lam is
    # 0.2 (1 - lam)
    return 0.2 * (1 - lam)


def _simulate_risk(n_cal, alpha, rule, rng):
    cov = certify.coverage_grid(n_cal, alpha, DELTA)
    thr = 1 - cov  # exact population quantiles of U(0, 1)
    viol = certified = 0
    for _ in range(REPS):
        conf = rng.random(n_cal)
        loss = (rng.random(n_cal) < 0.4 * (1 - conf)).astype(float)
        if rule == "naive":  # loosest threshold whose observed risk is <= alpha
            ok = [loss[conf >= t].mean() <= alpha if (conf >= t).any() else False for t in thr]
            i = max([j for j, o in enumerate(ok) if o], default=-1)
        else:
            i = certify.certify_risk(conf, loss, thr, alpha, DELTA, rule).index
        if i >= 0:
            certified += 1
            viol += _true_risk(thr[i]) > alpha
    return viol / REPS, certified / REPS


@pytest.mark.parametrize("method", ["fixed_sequence", "bonferroni"])
def test_risk_certificate_is_valid_in_simulation(method):
    rng = np.random.default_rng(11)
    for n_cal in [50, 300, 1000]:
        rate, power = _simulate_risk(n_cal, 0.10, method, rng)
        assert rate <= TOL, (n_cal, rate)
    assert power > 0.6  # at n = 1,000 it should usually certify something


def test_naive_rule_violates_so_the_check_has_teeth():
    rate, _ = _simulate_risk(300, 0.10, "naive", np.random.default_rng(12))
    assert rate > 0.3


def test_fixed_sequence_valid_when_risk_is_not_monotone():
    # the riskiest items are the most confident ones: fixed-sequence must still hold delta
    rng = np.random.default_rng(13)
    n_cal, alpha = 400, 0.15
    thr = 1 - certify.coverage_grid(n_cal, alpha, DELTA)

    def p_wrong(c):
        return np.where(c > 0.9, 0.6, 0.05)

    def true_risk(lam):  # mean of p_wrong over U(lam, 1)
        hi = max(1 - max(lam, 0.9), 0)
        return (0.6 * hi + 0.05 * (1 - lam - hi)) / (1 - lam)

    viol = 0
    for _ in range(REPS):
        conf = rng.random(n_cal)
        loss = (rng.random(n_cal) < p_wrong(conf)).astype(float)
        i = certify.certify_risk(conf, loss, thr, alpha, DELTA).index
        viol += i >= 0 and true_risk(thr[i]) > alpha
    assert viol / REPS <= TOL


def test_recall_certificate_is_valid_in_simulation():
    # positives score U(0, 1), so rejecting below t has true recall 1 - t
    rng = np.random.default_rng(14)
    thr = np.linspace(0, 0.3, 61)
    for n_cal, prev in [(200, 0.3), (1000, 0.3)]:
        viol = certified = 0
        for _ in range(REPS):
            y = (rng.random(n_cal) < prev).astype(float)
            s = np.where(y == 1, rng.random(n_cal), rng.random(n_cal) ** 3)
            cert = certify.certify_recall(s, y, thr, 0.95, DELTA)
            if cert.certified and cert.threshold > 0:
                certified += 1
                viol += 1 - cert.threshold < 0.95
        assert viol / REPS <= TOL, (n_cal, viol / REPS)
    assert certified / REPS > 0.5  # ~300 positives should usually save some work
