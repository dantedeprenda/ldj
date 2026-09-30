"""T2 per review, with the review as the unit of inference.

    uv run python scripts/t2_reviews.py

X4's pooled T2 summaries mix reviews and treat the 500 resamples of one review as if they were
independent evidence. Here each review is summarized on its own (useful-certificate share,
automation, violation over its resamples), and statements about reviews in general use the
review as the unit: the mean over eligible reviews with a 95% interval from 10,000 bootstrap
resamples of reviews. A review is eligible at B if it can afford B labels (min_rest = 100).
Reads results/x4_t2{,_arms2,_recall90}/rows.parquet. Writes results/t2_reviews.{md,csv}.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

RUNS = {"x4_t2": "recall 0.95", "x4_t2_arms2": "recall 0.95", "x4_t2_recall90": "recall 0.90"}


def main() -> int:
    parts = []
    for name, target in RUNS.items():
        f = Path("results") / name / "rows.parquet"
        if f.exists():
            r = pd.read_parquet(f)
            parts.append(r[r["arm"] == "certified"].assign(target=target))
    rows = pd.concat(parts)
    rows["useful"] = rows["certified"] & (rows["automated"] > 0)
    rows["auto"] = np.where(rows["useful"], rows["automated"], 0.0)
    per = (
        rows.groupby(["target", "group", "method", "f", "B"])
        .agg(
            useful=("useful", "mean"),
            auto=("auto", "mean"),
            violation=("violated", "mean"),
            cert_pos=("cert_pos", "mean"),
        )
        .reset_index()
    )
    per.to_csv("results/t2_reviews.csv", index=False)
    rng = np.random.default_rng(0)
    out = []
    for key, g in per.groupby(["target", "method", "f", "B"]):
        a = g["auto"].to_numpy()
        idx = rng.integers(0, len(a), size=(10_000, len(a)))
        lo, hi = np.percentile(a[idx].mean(axis=1), [2.5, 97.5])
        out.append(
            {
                "target": key[0],
                "method": key[1],
                "f": key[2],
                "B": key[3],
                "reviews": len(a),
                "reviews_certifying": int((g["useful"] > 0.5).sum()),
                "mean_auto": a.mean(),
                "lo": lo,
                "hi": hi,
                "max_violation": g["violation"].max(),
            }
        )
    t = pd.DataFrame(out)
    best = t.loc[t.groupby(["target", "B"])["mean_auto"].idxmax()].sort_values(["target", "B"])
    lines = [
        "# T2 by review (review = unit of inference)",
        "",
        "Best (method, f) per target and B by mean automation over eligible reviews (descriptive).",
        "`reviews certifying` = reviews where most resamples give a useful certificate.",
        "",
        (
            "| target | B | method | f | eligible reviews | reviews certifying | mean automation "
            "[95% CI over reviews] | worst per-review violation |"
        ),
        "|---|---|---|---|---|---|---|---|",
    ]
    for _, r in best.iterrows():
        lines.append(
            f"| {r['target']} | {r['B']} | {r['method']} | {r['f']:.2f} | {r['reviews']} | "
            f"{r['reviews_certifying']} | {r['mean_auto']:.3f} [{r['lo']:.3f}, {r['hi']:.3f}] | "
            f"{r['max_violation']:.3f} |"
        )
    Path("results/t2_reviews.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
