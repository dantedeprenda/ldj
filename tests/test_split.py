import numpy as np
import pandas as pd
import pytest

from ldj.split import split


def _events(n_groups=300, seed=0):
    rng = np.random.default_rng(seed)
    rows = []
    for gid in range(n_groups):
        start = pd.Timestamp("2026-01-01") + pd.Timedelta(days=int(rng.integers(0, 90)))
        for _ in range(int(rng.integers(1, 4))):
            t = start + pd.Timedelta(hours=int(rng.integers(0, 72)))
            rows.append({"order_id": f"o{gid}", "created_at": t.isoformat()})
    return pd.DataFrame(rows)


@pytest.mark.filterwarnings("ignore:the audit has")
def test_groups_never_cross_periods_and_spanning_goes_later():
    df = _events()
    out, rep = split(df, "created_at", "order_id", dev_share=0.6, seed=1)
    periods = out.groupby("order_id")["period"].nunique()
    assert (periods == 1).all()
    t = pd.to_datetime(out["created_at"], utc=True)
    boundary = pd.to_datetime(rep["boundary"])
    assert (t[out["period"] == "dev"] < boundary).all()
    assert rep["groups_spanning_boundary"] >= 0
    dropped, rep2 = split(df, "created_at", "order_id", dev_share=0.6, spanning="drop")
    te = pd.to_datetime(dropped.loc[dropped["period"] == "eval", "created_at"], utc=True)
    assert (te >= boundary).all()  # no eval group has an event before the boundary
    n_span_rows = len(df) - len(dropped)
    assert rep2["spanning_rule"] == "drop" and (n_span_rows > 0) == (
        rep["groups_spanning_boundary"] > 0
    )


@pytest.mark.filterwarnings("ignore:the audit has")
def test_cohort_only_within_eval_random_and_deterministic():
    df = _events()
    a, rep = split(df, "created_at", "order_id", cohort_share=0.25, seed=7)
    b, _ = split(df, "created_at", "order_id", cohort_share=0.25, seed=7)
    c, _ = split(df, "created_at", "order_id", cohort_share=0.25, seed=8)
    assert a.equals(b)
    assert not (a["cohort"] == c["cohort"]).all()
    assert (a.loc[a["cohort"] == 1, "period"] == "eval").all()
    assert rep["cohort_groups"] == round(0.25 * rep["groups_by_period"]["eval"])
    assert set(a.loc[a["period"] == "eval", "audit_role"]) <= {"audit", "deploy"}
    assert (a.loc[a["period"] == "dev", "audit_role"] == "").all()


@pytest.mark.filterwarnings("ignore:the audit has")
def test_dev_until_and_refusals():
    df = _events()
    _, rep = split(df, "created_at", "order_id", dev_until="2026-02-15")
    assert rep["boundary"].startswith("2026-02-15")
    bad = df.copy()
    bad.loc[3, "created_at"] = None
    with pytest.raises(ValueError, match="missing"):
        split(bad, "created_at", "order_id")
    bad2 = df.copy()
    bad2.loc[3, "created_at"] = "not a time"
    with pytest.raises(ValueError):
        split(bad2, "created_at", "order_id")


def test_leak_check_flags_information_after_decision():
    df = pd.DataFrame(
        {
            "created_at": ["2026-01-01", "2026-01-02", "2026-01-03"],
            "decided_at": ["2026-01-01T10:00", "2026-01-02T10:00", "2026-01-03T10:00"],
            "carrier_update_at": ["2026-01-01T09:00", "2026-01-02T11:00", "2026-01-03T09:00"],
        }
    )
    out, rep = split(df, "created_at", decision_time="decided_at", available_at="carrier_update_at")
    assert out["leak"].tolist() == [0, 1, 0]
    assert rep["rows_with_information_after_decision"] == 1


@pytest.mark.filterwarnings("ignore:the audit has")
def test_group_cohort_never_splits_a_group_and_honors_share():
    df = _events(n_groups=400)
    out, rep = split(df, "created_at", "order_id", cohort_share=0.3, seed=3)
    ev = out[out["period"] == "eval"]
    assert (ev.groupby("order_id")["cohort"].nunique() == 1).all()
    assert rep["cohort_groups"] == round(0.3 * ev["order_id"].nunique())
    assert rep["cohort_rows"] == int(ev["cohort"].sum())
    assert rep["cohort_rows_per_group"]["max"] >= 1


def test_one_per_group_gives_one_independent_audit_row_per_group():
    df = _events(n_groups=400)
    a, rep = split(df, "created_at", "order_id", cohort_share=0.3, seed=4, one_per_group=True)
    b, _ = split(df, "created_at", "order_id", cohort_share=0.3, seed=4, one_per_group=True)
    assert a.equals(b)
    aud = a[a["audit_role"] == "audit"]
    assert (aud.groupby("order_id").size() == 1).all()
    assert set(aud["order_id"]) == set(a.loc[a["cohort"] == 1, "order_id"])
    assert rep["audit_rows"] == rep["independent_audit_groups"] == rep["cohort_groups"]
    # the other rows of a cohort group return to deploy, unlabeled for the audit
    rest = a[(a["cohort"] == 1) & (a["audit_item"] == 0)]
    assert (rest["audit_role"] == "deploy").all()
    assert rep["warnings"] == []


def test_row_level_cohort_warns_when_groups_have_several_rows():
    df = _events(n_groups=300)
    with pytest.warns(UserWarning, match="row-level cohort"):
        _, rep = split(df, "created_at", "order_id", cohort_unit="row", seed=5)
    assert any("row-level" in w for w in rep["warnings"])
    # without a group column every row is its own group: no warning
    single = df.drop(columns="order_id")
    import warnings as _w

    with _w.catch_warnings():
        _w.simplefilter("error")
        split(single, "created_at", cohort_unit="row", seed=5)
