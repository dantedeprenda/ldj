"""Confirmatory analysis for W5 (preregistration/W5.md), written before the results exist.

    uv run python scripts/w5_analyze.py

Reads results/w5_t1_fresh/rows.parquet. Outcome: certified automation per draw, unconditional
(a draw whose certificate automates nothing counts as 0). Paired differences over the 500 draws;
95% interval from 10,000 bootstrap resamples of the draws (seed 0). H3: Clopper–Pearson 95%
interval of the rule's unconditional violation rate, lower end <= 0.05 at every B.
Writes results/w5_t1_fresh/w5.{md,json}.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from ldj import certify

RULE = {200: 0.25, 400: 0.25, 800: 0.50}  # f per B, preregistration/default-rule.md
C1 = ("gemma_judge_0shot", 0.0)
C2 = ("gemma_features", 0.50)
DELTA = 0.05
B_BOOT = 10_000


def per_draw(rows: pd.DataFrame, method: str, f: float, b: int) -> pd.DataFrame:
    g = rows[(rows.arm == "certified") & (rows.method == method) & (rows.B == b)]
    g = g[np.isclose(g.f, f)].sort_values("rep")
    auto = np.where(g.certified & (g.automated > 0), g.automated, 0.0)
    return pd.DataFrame(
        {"rep": g.rep.to_numpy(), "auto": auto, "violated": g.violated.to_numpy().astype(int)}
    )


def paired(a: pd.DataFrame, c: pd.DataFrame) -> dict:
    m = a.merge(c, on="rep", suffixes=("_rule", "_cmp"))
    # completeness (added before any result existed): every draw present and paired
    assert len(a) == len(c) == len(m) == 500, (len(a), len(c), len(m))
    d = (m.auto_rule - m.auto_cmp).to_numpy()
    idx = np.random.default_rng(0).integers(0, len(d), size=(B_BOOT, len(d)))
    lo, hi = np.percentile(d[idx].mean(axis=1), [2.5, 97.5])
    return {
        "n": len(d),
        "rule": float(m.auto_rule.mean()),
        "cmp": float(m.auto_cmp.mean()),
        "diff": float(d.mean()),
        "ci95": [float(lo), float(hi)],
        "supported": bool(lo > 0),
    }


def main() -> int:
    out = Path("results/w5_t1_fresh")
    rows = pd.read_parquet(out / "rows.parquet")
    res: dict = {"comparisons": {}, "h3": {}}
    for b, f in RULE.items():
        rule = per_draw(rows, "gemma_features_judge", f, b)
        for name, (m, fc) in {"C1_judge": C1, "C2_fixed_split": C2}.items():
            res["comparisons"][f"B{b}_{name}"] = paired(rule, per_draw(rows, m, fc, b))
        k, n = int(rule.violated.sum()), len(rule)
        lo, hi = float(certify.cp_lower(k, n, 0.025)), float(certify.cp_upper(k, n, 0.025))
        res["h3"][f"B{b}"] = {
            "violations": k,
            "n": n,
            "rate": k / n,
            "ci95": [lo, hi],
            "consistent": lo <= DELTA,
            "useful": float((rule.auto > 0).mean()),
            "auto_p10_p50_p90": np.percentile(rule.auto, [10, 50, 90]).tolist(),
        }
    h1 = res["comparisons"]["B400_C1_judge"]
    h2 = res["comparisons"]["B400_C2_fixed_split"]
    h3 = all(v["consistent"] for v in res["h3"].values())
    res["verdicts"] = {"H1": h1["supported"], "H2": h2["supported"], "H3": h3}
    lines = [
        "# W5 confirmatory results (pre-registered: preregistration/W5.md)",
        "",
        (
            f"- **H1 (primary)**, B = 400, rule vs direct judge: {h1['rule']:.3f} vs {h1['cmp']:.3f}, "
            f"difference {h1['diff']:+.3f} [{h1['ci95'][0]:+.3f}, {h1['ci95'][1]:+.3f}]: "
            f"**{'supported' if h1['supported'] else 'not supported'}**"
        ),
        (
            f"- **H2**, B = 400, rule vs fixed 50/50 split: {h2['rule']:.3f} vs {h2['cmp']:.3f}, "
            f"difference {h2['diff']:+.3f} [{h2['ci95'][0]:+.3f}, {h2['ci95'][1]:+.3f}]: "
            f"**{'supported' if h2['supported'] else 'not supported'}**"
        ),
        # Pre-registered criterion unchanged: CP lower end <= delta at every B. Passing it only
        # means excess violations were not detected, so it is labeled "not contradicted".
        f"- **H3**, guarantee at every B: **{'not contradicted by this test' if h3 else 'not supported (excess violations detected)'}**",
        "",
        (
            "| B | rule f | violation [95% CI] | useful | automation p10 / p50 / p90 | vs judge | "
            "vs fixed split |"
        ),
        "|---|---|---|---|---|---|---|",
    ]
    for b, f in RULE.items():
        h = res["h3"][f"B{b}"]
        c1 = res["comparisons"][f"B{b}_C1_judge"]
        c2 = res["comparisons"][f"B{b}_C2_fixed_split"]
        p = h["auto_p10_p50_p90"]
        lines.append(
            f"| {b} | {f:.2f} | {h['rate']:.3f} [{h['ci95'][0]:.3f}, {h['ci95'][1]:.3f}] | "
            f"{h['useful']:.2f} | {p[0]:.3f} / {p[1]:.3f} / {p[2]:.3f} | "
            f"{c1['diff']:+.3f} [{c1['ci95'][0]:+.3f}, {c1['ci95'][1]:+.3f}] | "
            f"{c2['diff']:+.3f} [{c2['ci95'][0]:+.3f}, {c2['ci95'][1]:+.3f}] |"
        )
    lines += ["", "B = 200 and 800 comparisons are secondary (reported, not tested)."]
    (out / "w5.md").write_text("\n".join(lines) + "\n")
    (out / "w5.json").write_text(json.dumps(res, indent=1))
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
