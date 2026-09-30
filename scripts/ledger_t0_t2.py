"""Whole-workflow ledgers for T0 (routing, money) and T2 (screening, finite pools). Exploratory.

    uv run python scripts/ledger_t0_t2.py

T0: a label is one run of the cheap model on a prompt plus automatic grading (no human), priced at
the mean cheap-model cost. A certified policy sends its automated share ``a`` of prompts to the
cheap model and the rest to the strong model; Jev features also pay the Jev call per prompt. Cost
per prompt = a x cheap + (1 - a) x strong (+ Jev). Compared with always-strong and always-cheap.
Accuracy: automated prompts at the realized selective risk from the X4 rows; the rest at the strong
model's overall test accuracy (an approximation: the strong model's accuracy on the deferred
subset is not stored). This is a cost-quality trade, not a free saving: always-strong is more
accurate, and certification only bounds how much accuracy the automated share gives up.

T2: each review is a finite pool. A certified policy auto-rejects a share of the records not yet
screened; screening decisions saved = automated share x (review size - B). The B labels are
screenings of pool items anyway, so they add no cost. GBP 1.175 per record at 1.56 USD/GBP
(src/ldj/tasks/screening.py). Draws that certify nothing save nothing.

Writes results/ledger_t0.{md,csv} and results/ledger_t2.{md,csv}.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import yaml

VOLUMES = [1_000, 10_000, 100_000]
JEV_USD = 5.18e-05  # mean Jev router cost per prompt (routing paper, seed 42, k = 25 file)
USD_PER_RECORD = 1.175 * 1.56


def _certified(names: list[str]) -> pd.DataFrame:
    parts = []
    for n in names:
        f = Path("results") / n / "rows.parquet"
        if f.exists():
            parts.append(pd.read_parquet(f))
    r = pd.concat(parts)
    r = r[r["arm"] == "certified"].copy()
    useful = r["certified"] & (r["automated"] > 0)
    r["auto"] = np.where(useful, r["automated"], 0.0)
    r["risk"] = np.where(useful, r["realized"], 0.0)
    return r


def ledger_t0() -> str:
    d = np.load("data/t0/llmrouterbench.npz", allow_pickle=True)
    te = d["test"]
    cheap, strong = float(d["cheap_cost"][te].mean()), float(d["strong_cost"][te].mean())
    acc_cheap = float(d["y"][te].mean())
    acc_strong = float(d["strong_correct"][te].mean())
    label = float(d["cheap_cost"].mean())
    r = _certified(["x4_t0", "x4_t0_arms2"])
    out = []
    for (method, f, b), g in r.groupby(["method", "f", "B"]):
        a, risk = g["auto"].to_numpy(), g["risk"].to_numpy()
        extra = JEV_USD if method == "jev_features" else 0.0
        per_prompt = a * cheap + (1 - a) * strong + extra
        acc = a * (1 - risk) + (1 - a) * acc_strong
        rec = {
            "method": method,
            "f": f,
            "B": b,
            "auto_mean": a.mean(),
            "usd_per_prompt": per_prompt.mean(),
            "accuracy": acc.mean(),
        }
        for v in VOLUMES:
            saved = v * (strong - per_prompt) - b * label
            rec[f"saved_vs_strong_{v}"] = saved.mean()
            rec[f"p_win_{v}"] = (saved > 0).mean()
        out.append(rec)
    t = pd.DataFrame(out)
    t.to_csv("results/ledger_t0.csv", index=False)
    lines = [
        "# T0 ledger: routing cost vs quality (exploratory)",
        "",
        (
            f"Always-cheap: ${cheap:.5f}/prompt, accuracy {acc_cheap:.3f}. Always-strong: "
            f"${strong:.5f}/prompt, accuracy {acc_strong:.3f}. A label = one cheap-model run "
            f"(${label:.5f}), graded automatically. Policy accuracy approximates deferred prompts at "
            "the strong model's overall accuracy. **A cost-quality trade, not a free saving.** Best "
            "certified cell per (method, B) by savings at 10k prompts; picked after seeing results."
        ),
        "",
        (
            "| method | f | B | automated | $/prompt | accuracy (approx., optimistic) | saved vs always-strong @10k | "
            "@100k | P(saves) @10k |"
        ),
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for (_, _), g in t[t["B"] >= 100].groupby(["method", "B"]):
        x = g.loc[g["saved_vs_strong_10000"].idxmax()]
        lines.append(
            f"| {x['method']} | {x['f']:.2f} | {x['B']} | {x['auto_mean']:.3f} | "
            f"{x['usd_per_prompt']:.5f} | {x['accuracy']:.3f} | "
            f"${x['saved_vs_strong_10000']:+.2f} | ${x['saved_vs_strong_100000']:+.2f} | "
            f"{x['p_win_10000']:.0%} |"
        )
    text = "\n".join(lines) + "\n"
    Path("results/ledger_t0.md").write_text(text)
    return text


def ledger_t2() -> str:
    from ldj.tasks import load_task

    cfg = yaml.safe_load(Path("configs/x4_t2.yaml").read_text())
    task = load_task(cfg["task"])
    groups = [task.subset(c) for c in np.unique(task.categories)]
    size = {g.name: len(g.train) + len(g.test) for g in groups}
    r = _certified(["x4_t2", "x4_t2_arms2"])
    r["review"] = r["group"].str.split("/").str[-1]
    r["N"] = r["group"].map(size)
    r["saved_records"] = r["auto"] * (r["N"] - r["B"])
    per = (
        r.groupby(["review", "method", "f", "B"])
        .agg(
            N=("N", "first"),
            useful=("auto", lambda a: float((a > 0).mean())),
            auto=("auto", "mean"),
            saved_records=("saved_records", "mean"),
        )
        .reset_index()
    )
    per["saved_usd"] = per["saved_records"] * USD_PER_RECORD
    per.to_csv("results/ledger_t2.csv", index=False)
    tot = (
        per.groupby(["method", "f", "B"])
        .agg(
            reviews=("review", "nunique"),
            certifying=("useful", lambda u: int((u > 0).sum())),
            saved_records=("saved_records", "sum"),
            saved_usd=("saved_usd", "sum"),
        )
        .reset_index()
    )
    all_records = sum(size.values())
    lines = [
        "# T2 ledger: screening decisions saved (exploratory)",
        "",
        (
            f"15 reviews, {all_records:,} records in total; ${USD_PER_RECORD:.2f} per screening "
            "decision. Labels are screenings of pool items, so they add no cost. Mean over 500 draws; "
            "a draw that certifies nothing saves nothing. Best certified cell per (method, B) by "
            "records saved; picked after seeing results."
        ),
        "",
        (
            "| method | f | B | reviews able to run B | reviews certifying | records saved (all "
            "reviews) | share of all records | $ saved |"
        ),
        "|---|---|---|---|---|---|---|---|",
    ]
    for (_, _), g in tot.groupby(["method", "B"]):
        x = g.loc[g["saved_records"].idxmax()]
        lines.append(
            f"| {x['method']} | {x['f']:.2f} | {x['B']} | {x['reviews']} | {x['certifying']} | "
            f"{x['saved_records']:,.0f} | {x['saved_records'] / all_records:.1%} | "
            f"${x['saved_usd']:,.0f} |"
        )
    best = per.loc[per.groupby("review")["saved_records"].idxmax()]
    lines += [
        "",
        "Best cell per review:",
        "",
        "| review | records | method | f | B | useful | records saved | $ saved |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for _, x in best.sort_values("saved_records", ascending=False).iterrows():
        if x["saved_records"] == 0:
            lines.append(
                f"| {x['review']} | {x['N']} | nothing certifies at any B | | | | 0 | $0 |"
            )
            continue
        lines.append(
            f"| {x['review']} | {x['N']} | {x['method']} | {x['f']:.2f} | {x['B']} | "
            f"{x['useful']:.2f} | {x['saved_records']:,.0f} | ${x['saved_usd']:,.0f} |"
        )
    missing = sorted({k.split("/")[-1] for k in size} - set(per["review"]))
    if missing:
        lines += ["", f"Too small for any budget (B + 100 unlabeled > pool): {', '.join(missing)}."]
    text = "\n".join(lines) + "\n"
    Path("results/ledger_t2.md").write_text(text)
    return text


def main() -> int:
    print(ledger_t0())
    print(ledger_t2())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
