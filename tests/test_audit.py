import numpy as np
import pytest

from ldj.allocate import Policy
from ldj.audit import audit, markdown


def _data(n_audit, seed=0, n_deploy=5000):
    rng = np.random.default_rng(seed)
    n = n_audit + n_deploy
    s = rng.random(n)
    y = (rng.random(n) < 0.02 + 0.6 * (1 - s)).astype(float) == 0  # high score = right
    return s[:n_audit], y[:n_audit].astype(float), s[n_audit:]


def test_enough_audit_labels_support_a_policy():
    s_a, y_a, s_d = _data(1500)
    r = audit(s_a, y_a, s_d, Policy("accept", alpha=0.10))
    assert r["verdict"] == "supported" and 0 < r["automated_share"] <= 1
    assert r["bound"] <= 0.10
    assert "Verdict: supported" in markdown(r)


def test_few_audit_labels_are_insufficient_and_say_why():
    s_a, y_a, s_d = _data(30)
    r = audit(s_a, y_a, s_d, Policy("accept", alpha=0.10))
    assert r["verdict"] == "insufficient evidence" and r["automated_share"] == 0
    assert "at least 29 audit items" in r["what_would_help"]
    assert "Assumptions" in markdown(r)


def test_recall_needs_enough_positives():
    rng = np.random.default_rng(1)
    s_a, s_d = rng.random(200), rng.random(2000)
    y_a = (rng.random(200) < 0.05).astype(float)
    r = audit(s_a, y_a, s_d, Policy("recall", target=0.95))
    assert r["verdict"] == "insufficient evidence"
    assert "at least 59 positives" in r["what_would_help"]


def test_rejects_bad_input():
    with pytest.raises(ValueError):
        audit([0.5], [2], [0.1], Policy("accept", alpha=0.1))
    with pytest.raises(ValueError):
        audit([0.5], [1], [], Policy("accept", alpha=0.1))


def test_nan_scores_are_refused():
    s_a, y_a, s_d = _data(100)
    s_d = s_d.copy()
    s_d[3] = np.nan
    with pytest.raises(ValueError, match="NaN"):
        audit(s_a, y_a, s_d, Policy("accept", alpha=0.10))
