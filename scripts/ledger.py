"""W3 / E1: whole-workflow accounting for T1 moderation (exploratory).

    uv run python scripts/ledger.py

Per X4 draw, a certified policy automates a share ``a`` of items and sends the rest to a person.
Over a stream of V items, a team pays for:

- labels: B labels x annotation actions per label, at the review price. A consensus label is the
  Rasch score over every annotation of the comment: 5.66 annotations on average in T1's train
  pool (median 3; the mean sets total cost). One annotator's label = 1. A 3-action consensus row
  is kept as a labeled sensitivity (it was the original, too-low count; see results.md erratum);
- reviews of the items the policy does not automate: (1 - a) x V, at the review price;
- model calls on all V items (Gemma features / judge; embeddings and TF-IDF counted as $0).

Compared with always reviewing (V reviews). Review price $0.25 per comment (45 s at $20/h), with $0.10 and $1.00 as sensitivity. Volumes 1k / 10k / 100k are
scenarios, not measured volumes. Certified error stays <= 0.10 with probability >= 0.95 on the
automated share; errors on reviewed items are the reviewer's own, the same as always-review.
Break-even V = actions on labels / mean automated share. Writes results/ledger_t1.md.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

RUNS = {  # results dir -> [(label source, annotation actions per label), ...]
    "x4_t1": [("consensus", 5.66), ("consensus @3 (too low)", 3)],
    "x4_t1_arms2": [("consensus", 5.66), ("consensus @3 (too low)", 3)],
    "x4_t1_single": [("one annotator", 1)],
}
INFERENCE = {  # USD per item, from the pre-registered T1 run's records
    "gemma_features": 5.7e-05,
    "gemma_judge_0shot": 1.3e-05,
    "gemma_features_judge": 5.7e-05 + 1.3e-05,
}
VOLUMES = [1_000, 10_000, 100_000]
PRICES = [0.10, 0.25, 1.00]


def main() -> int:
    parts = []
    for name, sources in RUNS.items():
        f = Path("results") / name / "rows.parquet"
        if not f.exists():
            print(f"missing {f}; skipped")
            continue
        r0 = pd.read_parquet(f)
        r0 = r0[r0["arm"] == "certified"].copy()
        r0["automated"] = np.where(r0["certified"] & (r0["automated"] > 0), r0["automated"], 0.0)
        for source, actions in sources:
            parts.append(r0.assign(labels=source, actions=actions))
    rows = pd.concat(parts)
    rows["infer"] = rows["method"].map(INFERENCE).fillna(0.0)
    out = []
    for (labels, method, f, b), g in rows.groupby(["labels", "method", "f", "B"]):
        a = g["automated"].to_numpy()
        act = float(g["actions"].iloc[0])
        setup = act * b
        rec = {
            "labels": labels,
            "method": method,
            "f": f,
            "B": b,
            "auto_mean": a.mean(),
            "breakeven_V": setup / a.mean() if a.mean() > 0 else np.inf,
        }
        for v in VOLUMES:
            saved = a * v - setup  # human checks saved vs always-review, per draw
            rec[f"saved_{v}"] = saved.mean() / v
            rec[f"p_win_{v}"] = (saved > 0).mean()
            for price in PRICES:
                usd = saved * price - g["infer"].to_numpy() * v
                rec[f"usd_{v}_{price}"] = usd.mean()
        out.append(rec)
    t = pd.DataFrame(out)
    t.to_csv("results/ledger_t1.csv", index=False)
    lines = [
        "# T1 whole-workflow ledger (exploratory; certified arm, error <= 0.10)",
        "",
        (
            "Human checks saved vs always-review, as a share of V (mean over draws; draws that "
            "certify nothing save nothing and still pay for labels), the share of draws that save "
            "anything, and dollars saved at $0.25 per review. Best cell per (labels, B) by saved "
            "share at V = 10k, plus the direct judge. **Descriptive: picked after seeing results.**"
        ),
        "",
        (
            "| labels | method | f | B | break-even V | saved @1k | @10k | @100k | P(win) @10k | "
            "$ saved @10k | @100k |"
        ),
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    pick = []
    for (labels, b), g in t.groupby(["labels", "B"]):
        pick.append(g.loc[g["saved_10000"].idxmax()])
        judge = g[g["method"] == "gemma_judge_0shot"]
        if len(judge) and pick[-1]["method"] != "gemma_judge_0shot":
            pick.append(judge.iloc[0])
    for r in pick:
        be = "never" if not np.isfinite(r["breakeven_V"]) else f"{r['breakeven_V']:,.0f}"
        lines.append(
            f"| {r['labels']} | {r['method']} | {r['f']:.2f} | {r['B']} | {be} | "
            f"{r['saved_1000']:+.1%} | {r['saved_10000']:+.1%} | {r['saved_100000']:+.1%} | "
            f"{r['p_win_10000']:.0%} | ${r['usd_10000_0.25']:,.0f} | ${r['usd_100000_0.25']:,.0f} |"
        )
    Path("results/ledger_t1.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
