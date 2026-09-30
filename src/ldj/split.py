"""Chronological, grouped split of an event log for a workflow evaluation.

    ldj split events.csv --time created_at --group order_id --dev-share 0.6 --cohort-share 0.2 \
        --out split.csv

Every row gets a ``period``:

- ``dev``: the earlier period. Choose prompts, thresholds and policies here, as often as needed.
- ``eval``: the later period. Touched once, after the policy is frozen.

Within ``eval``, a random ``cohort`` (seeded) is the audit sample: label it without looking at
scores, and pass it to ``ldj audit`` as ``role = audit`` (the column ``audit_role`` already says
``audit`` or ``deploy`` for eval rows). Rates estimated on the cohort are unbiased for the eval
period; an enriched sample of rare cases is a separate diagnostic and cannot replace it.

**Sampling unit.** By default (``cohort_unit="group"``) the cohort is ``cohort_share`` of the eval
*groups*, drawn at random, with every row of a drawn group in the cohort. Rows of one group (an
order, a shipment) are correlated, and the audit's Clopper–Pearson certificate assumes independent
draws, so the independent unit is the group. ``one_per_group=True`` then marks ONE random row per
cohort group as the audit item (``audit_item = 1``, ``audit_role = audit``); the group's other
rows return to ``deploy`` (unlabeled items the policy runs on; they are not labeled for the
audit), so ``ldj audit`` receives one independent item per group and its guarantee is about groups
as sampled. ``cohort_unit="row"`` draws individual rows (the earlier behavior); it warns when eval
groups have more than one row, because clustered rows understate uncertainty.

Groups (an order, a shipment) never straddle the boundary. A group is placed by its first event;
a group whose events span the boundary goes to ``eval`` by default (``spanning="later"``), so no
dev decision can have seen part of an eval group; ``spanning="drop"`` removes such groups instead.
Both choices are reported.

Optional leakage check: with ``decision_time`` and ``available_at`` columns, rows whose information
became available after the decision was made are flagged (``leak = 1``) and counted; they must not
be used as model inputs.
"""

from __future__ import annotations

import warnings
from typing import Any

import numpy as np
import pandas as pd


def _times(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        raise ValueError(f"no column {col!r}")
    if df[col].isna().any():
        raise ValueError(
            f"{col!r} is missing in {int(df[col].isna().sum())} rows; fix or drop them"
        )
    try:
        return pd.to_datetime(df[col], errors="raise", utc=True)
    except (ValueError, TypeError) as e:
        raise ValueError(f"{col!r} has values that are not times: {e}") from e


def split(
    df: pd.DataFrame,
    time: str,
    group: str | None = None,
    dev_until: str | None = None,
    dev_share: float = 0.6,
    cohort_share: float = 0.2,
    seed: int = 0,
    spanning: str = "later",
    decision_time: str | None = None,
    available_at: str | None = None,
    cohort_unit: str = "group",
    one_per_group: bool = False,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Returns (rows with ``period``, ``cohort``, ``audit_item``, ``audit_role`` and optionally
    ``leak``, report)."""
    if spanning not in ("later", "drop"):
        raise ValueError("spanning must be 'later' or 'drop'")
    if cohort_unit not in ("group", "row"):
        raise ValueError("cohort_unit must be 'group' or 'row'")
    if not 0 < cohort_share <= 1:
        raise ValueError("cohort_share must be in (0, 1]")
    out = df.copy()
    t = _times(out, time)
    g = out[group].astype(str) if group else pd.Series(np.arange(len(out)).astype(str), out.index)
    if group and out[group].isna().any():
        raise ValueError(f"{group!r} is missing in {int(out[group].isna().sum())} rows")
    first = t.groupby(g).transform("min")
    last = t.groupby(g).transform("max")
    if dev_until is not None:
        boundary = pd.to_datetime(dev_until, utc=True)
    else:
        if not 0 < dev_share < 1:
            raise ValueError("dev_share must be in (0, 1)")
        starts = t.groupby(g).min().sort_values()
        boundary = starts.iloc[min(int(np.floor(dev_share * len(starts))), len(starts) - 1)]
    # a group is dev only if all its events are before the boundary
    is_dev = last < boundary
    span = (first < boundary) & ~is_dev
    n_span_groups = int(g[span].nunique())
    if spanning == "drop":
        out = out[~span]
        t, g, is_dev = t[~span], g[~span], is_dev[~span]
    out["period"] = np.where(is_dev, "dev", "eval")
    rng = np.random.default_rng(seed)
    is_eval = out["period"].to_numpy() == "eval"
    eval_idx = np.flatnonzero(is_eval)
    gv = g.to_numpy()
    cohort = np.zeros(len(out), dtype=int)
    if cohort_unit == "group":
        eval_groups = np.unique(gv[is_eval])
        k = round(cohort_share * len(eval_groups))
        chosen = rng.choice(eval_groups, size=k, replace=False) if k else np.array([], dtype=object)
        cohort[is_eval & np.isin(gv, chosen)] = 1
    else:
        k = round(cohort_share * len(eval_idx))
        pick = rng.choice(eval_idx, size=k, replace=False) if k else np.array([], dtype=int)
        cohort[pick] = 1
    audit_item = cohort.copy()
    if one_per_group:
        audit_item[:] = 0
        in_cohort = np.flatnonzero(cohort == 1)
        order = rng.permutation(in_cohort)  # random row per group: first in a random order
        _, first_pos = np.unique(gv[order], return_index=True)
        audit_item[order[first_pos]] = 1
    out["cohort"] = cohort
    out["audit_item"] = audit_item
    out["audit_role"] = np.where(is_eval, np.where(audit_item == 1, "audit", "deploy"), "")
    per_group = pd.Series(gv[cohort == 1]).value_counts()
    audit_groups = int(pd.Series(gv[audit_item == 1]).nunique())
    audit_rows = int(audit_item.sum())
    eval_multi = int((pd.Series(gv[is_eval]).value_counts() > 1).sum())
    warn: list[str] = []
    if cohort_unit == "row" and eval_multi:
        warn.append(
            f"row-level cohort: {eval_multi} eval groups have more than one row; rows of a group "
            "are correlated, so the audit sample is not independent (use cohort_unit='group')"
        )
    if audit_rows > 1.5 * audit_groups:
        warn.append(
            f"the audit has {audit_rows} rows but only {audit_groups} independent groups; "
            "certificates computed on the rows overstate the evidence (use one_per_group=True)"
        )
    for w in warn:
        warnings.warn(w, UserWarning, stacklevel=2)
    report: dict[str, Any] = {
        "rows": len(out),
        "boundary": str(boundary),
        "rows_by_period": {p: int((out["period"] == p).sum()) for p in ("dev", "eval")},
        "groups_by_period": {
            p: int(g[out["period"].to_numpy() == p].nunique()) for p in ("dev", "eval")
        },
        "cohort_unit": cohort_unit,
        "cohort_groups": int(per_group.size),
        "cohort_rows": int(cohort.sum()),
        "cohort_rows_per_group": {
            "max": int(per_group.max()) if len(per_group) else 0,
            "mean": round(float(per_group.mean()), 3) if len(per_group) else 0.0,
        },
        "one_per_group": one_per_group,
        "audit_rows": audit_rows,
        "independent_audit_groups": audit_groups,
        "warnings": warn,
        "groups_spanning_boundary": n_span_groups,
        "spanning_rule": spanning,
        "seed": seed,
    }
    if decision_time or available_at:
        if not (decision_time and available_at):
            raise ValueError("give both decision_time and available_at")
        leak = (_times(out, available_at) > _times(out, decision_time)).astype(int)
        out["leak"] = leak.to_numpy()
        report["rows_with_information_after_decision"] = int(leak.sum())
    # sanity: no group in both periods; a group-level cohort never splits a group
    both = set(g[out["period"].to_numpy() == "dev"]) & set(g[out["period"].to_numpy() == "eval"])
    assert not both, "a group landed in both periods"
    if cohort_unit == "group":
        mixed = pd.Series(cohort[is_eval]).groupby(gv[is_eval]).nunique()
        assert (mixed <= 1).all(), "a cohort group was split"
    return out, report
