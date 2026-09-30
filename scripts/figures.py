"""Figures for the exploratory results (reads existing results only; runs no experiment).

    uv run --with matplotlib python scripts/figures.py

Writes results/figures/fig{1..7}_*.{png,svg}. Captions and sources: docs/report.md.
Palette: the dataviz reference categorical slots 1-4 (validated light mode; slots 3-4 sit below
3:1 contrast, so every series is direct-labeled), status critical for invalid cells, recessive
grid and axes. matplotlib is not a project dependency (hence ``--with``).
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import pandas as pd

OUT = Path("results/figures")
S1, S2, S3, S4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"  # categorical slots, fixed order
CRIT = "#d03b3b"  # status: critical (invalid)
SURF, INK, INK2, MUTED, GRID, BASE = (
    "#fcfcfb",
    "#0b0b0b",
    "#52514e",
    "#898781",
    "#e1e0d9",
    "#c3c2b7",
)
DESCRIPTIVE = "Best share per budget picked after seeing results (descriptive)."

plt.rcParams.update(
    {
        "figure.facecolor": SURF,
        "axes.facecolor": SURF,
        "savefig.facecolor": SURF,
        "axes.edgecolor": BASE,
        "axes.labelcolor": INK2,
        "axes.titlecolor": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": INK,
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "legend.frameon": False,
        "lines.linewidth": 2,
        "lines.markersize": 6,
    }
)


def _summary(*names: str) -> pd.DataFrame:
    return pd.concat([pd.read_csv(f"results/{n}/summary.csv") for n in names])


def _best(s: pd.DataFrame, method: str) -> pd.DataFrame:
    """Per B, the certified cell with the highest mean automation for ``method``."""
    c = s[(s.arm == "certified") & (s.method == method)]
    return c.loc[c.groupby("B")["automated"].idxmax()].sort_values("B")


def _label_end(ax, x, y, text, color, dy=0.0):
    ax.annotate(
        text,
        (x, y),
        xytext=(6, dy),
        textcoords="offset points",
        va="center",
        color=INK2,
        fontsize=8,
    )
    ax.plot([x], [y], "o", color=color, markersize=6, markeredgecolor=SURF, markeredgewidth=1.5)


def _save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:  # log axes: label only the chosen major ticks
        ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    fig.tight_layout(rect=(0, 0.07, 1, 0.93))  # room for the suptitle above and the note below
    fig.savefig(OUT / f"{name}.png", dpi=200, bbox_inches="tight")
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def fig1() -> None:
    panels = [
        (
            "T1 moderation (error <= 0.10)",
            _summary("x4_t1", "x4_t1_arms2"),
            [
                ("gemma_features_judge", "features + judge", S1),
                ("gemma_features", "features", S2),
                ("gemma_judge_0shot", "direct judge", S3),
            ],
        ),
        (
            "T0 routing (risk <= 0.133)",
            _summary("x4_t0", "x4_t0_arms2"),
            [
                ("jev_features", "Jev features", S1),
                ("tfidf_logreg", "text methods\n(TF-IDF; bge similar)", S2),
            ],
        ),
        (
            "T2 screening (recall >= 0.95, per review)",
            _summary("x4_t2", "x4_t2_arms2"),
            [
                ("gemma_features_judge", "features, with or\nwithout judge (same)", S1),
                ("gemma_judge_0shot", "direct judge", S3),
            ],
        ),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.4), sharey=True)
    for ax, (title, s, methods) in zip(axes, panels):
        for m, lab, col in methods:
            b = _best(s, m)
            b = b[b.B >= 25]
            ax.plot(b.B, b.automated, color=col, label=lab)
            _label_end(
                ax, b.B.iloc[-1], b.automated.iloc[-1], lab, col, dy={S1: 6, S2: 0, S3: -6}[col]
            )
        ax.set_xscale("log")
        ax.set_xticks([25, 50, 100, 200, 400, 800], ["25", "50", "100", "200", "400", "800"])
        ax.set_title(title, loc="left")
        ax.set_xlabel("label budget B")
        ax.set_ylim(0, 0.75)
        ax.set_xlim(20, 2500)
    axes[0].set_ylabel("certified automation (share of items)")
    fig.suptitle(
        "Certified automation rises with labels on T1 and, with Jev, on T0; T2 stays near zero",
        x=0.01,
        ha="left",
        fontsize=11,
        fontweight="bold",
    )
    fig.text(
        0.01,
        0.005,
        DESCRIPTIVE + " Mean over 500 draws; draws that certify nothing count as 0.",
        color=MUTED,
        fontsize=8,
    )
    _save(fig, "fig1_frontier")


def fig2() -> None:
    s = _summary("x4_t1", "x4_t1_arms2")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.4))
    for m, lab, col in [
        ("gemma_features_judge", "features + judge", S1),
        ("gemma_judge_0shot", "direct judge", S3),
    ]:
        b = _best(s, m)
        b = b[b.B >= 100]
        a1.plot(b.B, b.useful, color=col, marker="o", label=lab)
        _label_end(a1, b.B.iloc[-1], b.useful.iloc[-1], lab, col)
        off = -0.06 if col == S1 else 0.06
        x = b.B * (1 + off)
        a2.vlines(x, b.auto_p10, b.auto_p90, color=col, linewidth=2, label=f"{lab}: p10-p90")
        a2.plot(x, b.auto_p50, "o", color=col, markeredgecolor=SURF, markeredgewidth=1.5)
        a2.plot(x, b.automated, "_", color=INK2, markersize=10)
        a2.annotate(
            lab,
            (x.iloc[-1], b.auto_p90.iloc[-1]),
            xytext=(6, 0),
            textcoords="offset points",
            color=INK2,
            fontsize=8,
            va="center",
        )
    for ax in (a1, a2):
        ax.set_xscale("log")
        ax.set_xticks([100, 200, 400, 800], ["100", "200", "400", "800"])
        ax.set_xlim(80, 1600)
        ax.set_xlabel("label budget B")
    a1.set_ylim(0, 1.05)
    a1.set_ylabel("share of draws with a useful certificate")
    a1.set_title("How often a certificate automates anything", loc="left")
    a2.set_ylim(0, 0.9)
    a2.set_ylabel("automation per draw")
    a2.set_title("Spread across draws (bar p10-p90, dot median, dash mean)", loc="left")
    fig.suptitle(
        "T1: features + judge usually certifies from 200 labels; the direct judge rarely does",
        x=0.01,
        ha="left",
        fontsize=11,
        fontweight="bold",
    )
    fig.text(0.01, 0.005, DESCRIPTIVE, color=MUTED, fontsize=8)
    _save(fig, "fig2_useful_spread")


def fig3() -> None:
    tasks = [
        ("T1", ("x4_t1", "x4_t1_arms2")),
        ("T0", ("x4_t0", "x4_t0_arms2")),
        ("T2", ("x4_t2", "x4_t2_arms2")),
    ]
    rng = np.random.default_rng(0)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for i, (task, names) in enumerate(tasks):
        s = _summary(*names)
        for arm, col, dx in [("certified", S1, -0.18), ("heuristic", S2, 0.18)]:
            v = s[s.arm == arm].violation.to_numpy()
            ax.scatter(
                i + dx + rng.uniform(-0.08, 0.08, len(v)),
                v,
                s=14,
                color=col,
                edgecolor=SURF,
                linewidth=0.8,
                label=arm if i == 0 else None,
            )
    ax.axhline(0.05, color=INK2, linewidth=1, linestyle="--")
    ax.annotate(
        "target: at most 5% of draws violate",
        (2.45, 0.05),
        xytext=(0, 6),
        textcoords="offset points",
        ha="right",
        color=INK2,
        fontsize=8,
    )
    ax.set_xticks([0, 1, 2], [t for t, _ in tasks])
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylabel("share of draws that violate the target")
    ax.legend(loc="upper left", title=None)
    ax.set_title(
        "Certificates stay under the 5% line; reusing all labels (heuristic) breaks it often",
        loc="left",
    )
    fig.text(
        0.01,
        0.005,
        "Each dot is one (method, fit share, budget) cell, 500 draws. Violations "
        "judged on the test split.",
        color=MUTED,
        fontsize=8,
    )
    _save(fig, "fig3_violations")


def fig4() -> None:
    rows = []
    for name, lab, col, per_label in [
        ("x4_t1_arms2", "consensus (3 votes per label)", S1, 3),
        ("x4_t1_votes_one", "one vote", S2, 1),
        ("x4_t1_votes_maj3", "majority of 3 votes", S3, 3),
    ]:
        b = _best(pd.read_csv(f"results/{name}/summary.csv"), "gemma_features_judge")
        b = b.assign(actions=b.B * per_label, lab=lab, col=col)
        rows.append(b[(b.actions >= 150) & (b.actions <= 2500)])
    single = _best(pd.read_csv("results/x4_t1_single/summary.csv"), "gemma_features")
    single = single.assign(actions=single.B, lab="one annotator, features only", col=S4)
    rows.append(single[(single.actions >= 150)])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 3.6))
    for b in rows:
        col, lab = b.col.iloc[0], b.lab.iloc[0]
        a1.plot(b.actions, b.automated, color=col, marker="o", label=lab)
        a2.errorbar(
            b.actions,
            b.violation,
            yerr=[b.violation - b.violation_lo, b.violation_hi - b.violation],
            color=col,
            marker="o",
            capsize=3,
            label=lab,
        )
        bad = b[~b.consistent.astype(bool)]
        a2.scatter(
            bad.actions,
            bad.violation,
            s=90,
            facecolor="none",
            edgecolor=CRIT,
            linewidth=1.5,
            zorder=5,
        )
    a2.axhline(0.05, color=INK2, linewidth=1, linestyle="--")
    a2.annotate(
        "target 5%", (160, 0.05), xytext=(0, 5), textcoords="offset points", color=INK2, fontsize=8
    )
    maj = rows[2]
    worst = maj.loc[maj.violation.idxmax()]
    a2.annotate(
        "majority-of-3: fails\n(circled = inconsistent with 5%)",
        (worst.actions, worst.violation),
        xytext=(-150, -8),
        textcoords="offset points",
        color=CRIT,
        fontsize=8,
        arrowprops={"arrowstyle": "-", "color": CRIT},
    )
    for ax in (a1, a2):
        ax.set_xscale("log")
        ax.set_xticks([200, 400, 800, 1600], ["200", "400", "800", "1600"])
        ax.set_xlabel("annotation actions (labels x votes per label)")
    a1.set_ylabel("certified automation")
    a1.set_title("Automation", loc="left")
    a1.legend(loc="upper left", fontsize=8)
    a2.set_ylabel("share of draws that violate (vs consensus)")
    a2.set_title("Validity against the consensus reference", loc="left")
    fig.suptitle(
        "A certificate holds only for the labels it was computed on",
        x=0.01,
        ha="left",
        fontsize=11,
        fontweight="bold",
    )
    fig.text(
        0.01,
        0.005,
        DESCRIPTIVE + " Test labels are the consensus in every series.",
        color=MUTED,
        fontsize=8,
    )
    _save(fig, "fig4_label_source")


def fig5() -> None:
    t = pd.read_csv("results/ledger_t1.csv")
    pick = [
        ("consensus", "gemma_features_judge", 400, "features + judge, B = 400", S1),
        ("consensus", "gemma_features_judge", 200, "features + judge, B = 200", S2),
        ("consensus", "gemma_judge_0shot", 400, "direct judge, B = 400", S3),
    ]
    vols = [1_000, 10_000, 100_000]
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for labels, m, b, lab, col in pick:
        g = t[(t.labels == labels) & (t.method == m) & (t.B == b)]
        if g.empty:
            continue
        r = g.loc[g.saved_10000.idxmax()]
        y = [r[f"saved_{v}"] for v in vols]
        ax.plot(vols, y, color=col, marker="o", label=lab)
        _label_end(ax, vols[-1], y[-1], lab, col)
    ax.axhline(0, color=BASE, linewidth=1)
    ax.set_xscale("log")
    ax.set_xticks(vols, ["1k", "10k", "100k"])
    ax.set_xlim(700, 900_000)
    ax.set_ylim(-1.2, 0.7)
    ax.set_xlabel("items handled")
    ax.set_ylabel("human checks saved vs always-review (share)")
    ax.set_title(
        "On T1, certification pays from a few thousand items; label cost dominates below",
        loc="left",
    )
    fig.text(
        0.01,
        0.005,
        "Consensus label = 5.66 annotation actions (mean); $0.25 per check. " + DESCRIPTIVE,
        color=MUTED,
        fontsize=8,
    )
    _save(fig, "fig5_ledger_t1")


def fig6() -> None:
    r = pd.read_parquet("results/w7_t2/rows.parquet")
    m = (
        r.groupby(["arm", "rule"])
        .agg(saved=("work_saved", "mean"), recall=("recall", "mean"), met=("met", "mean"))
        .reset_index()
    )
    arms = [
        ("a_judge_static", "judge ranking (static)"),
        ("b_features_static", "features ranking (static)"),
        ("c_active", "active learning"),
        ("d_active_llm", "active learning + judge"),
    ]
    fig, ax = plt.subplots(figsize=(8.5, 3.4))
    for yi, (arm, name) in enumerate(arms):
        y = len(arms) - 1 - yi
        g = m[m.arm == arm].set_index("rule")
        c, h = g.loc["certified_95"], g.loc["heuristic_50"]
        ax.plot([c.saved, h.saved], [y, y], color=GRID, linewidth=3, zorder=1)
        for x, col in [(c, S1), (h, S2)]:
            ax.scatter(x.saved, y, s=70, color=col, edgecolor=SURF, linewidth=1.5, zorder=3)
            ax.annotate(
                f"recall {x.recall:.2f}; {x.met:.0%} of runs >= 0.95",
                (x.saved, y),
                xytext=(0, 9),
                textcoords="offset points",
                ha="center",
                color=INK2,
                fontsize=7.5,
            )
    ax.set_yticks(range(len(arms)), [n for _, n in arms][::-1])
    ax.set_ylim(-0.6, len(arms) - 0.3)
    ax.set_xlim(0, 0.8)
    ax.set_xlabel("work saved (share of records never screened), mean over 15 reviews")
    ax.grid(axis="y", visible=False)
    ax.scatter([], [], s=70, color=S1, label="certified stopping (recall >= 0.95, 95%)")
    ax.scatter([], [], s=70, color=S2, label="heuristic stopping (50 irrelevant in a row)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.25), ncol=2, fontsize=8)
    fig.suptitle(
        "Screening: certified stopping keeps recall but saves ~15%; heuristic saves more and "
        "misses",
        x=0.01,
        ha="left",
        fontsize=11,
        fontweight="bold",
    )
    fig.text(
        0.01,
        0.005,
        "15 T2 reviews x 30 runs. Certified = Callaghan & Muller-Hansen hypergeometric rule; "
        "it holds only under active learning.",
        color=MUTED,
        fontsize=8,
    )
    _save(fig, "fig6_screening")


def fig7() -> None:
    rows = pd.DataFrame(json.loads(Path("results/bridge_t0/report.json").read_text())["rows"])
    rows["net"] = rows.net_ci.apply(lambda c: c[0])
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
    for ax, k, title in [
        (axes[0], "25", "Heads fit on 25 labels"),
        (axes[1], "all", "Heads fit on all 3,606 labels"),
    ]:
        for pol, lab, col, ls, dy in [
            ("oracle", "oracle (upper bound)", MUTED, "--", 0),
            ("random", "random", MUTED, ":", -8),
            ("jev_features:difficulty", "difficulty (Jev)", S2, "-", 8),
            ("jev_features:benefit", "benefit (Jev)", S1, "-", 0),
        ]:
            g = rows[(rows.policy == pol) & (rows.k.isin([k, "-"]))].sort_values("rate")
            ax.plot(
                g.rate, g.net, color=col, linestyle=ls, marker="o" if ls == "-" else None, label=lab
            )
            ax.annotate(
                lab,
                (g.rate.iloc[-1], g.net.iloc[-1]),
                xytext=(6, dy),
                textcoords="offset points",
                color=INK2,
                fontsize=8,
                va="center",
            )
        ax.axhline(0, color=BASE, linewidth=1)
        ax.set_xlim(0.05, 0.75)
        ax.set_xticks([0.1, 0.2, 0.3, 0.5], ["10%", "20%", "30%", "50%"])
        ax.set_xlabel("share of prompts escalated to the strong model")
        ax.set_title(title, loc="left")
    axes[0].set_ylabel("net accuracy gain (repaired - broken) / prompts")
    fig.suptitle(
        "With many labels, escalating by predicted benefit beats difficulty at low rates; "
        "all far below the oracle",
        x=0.01,
        ha="left",
        fontsize=11,
        fontweight="bold",
    )
    fig.text(
        0.01,
        0.005,
        "T0 test split (1,328 prompts); routing paper's saved predictions; "
        "mean over 5 label seeds. Exploratory.",
        color=MUTED,
        fontsize=8,
    )
    _save(fig, "fig7_bridge")


def main() -> int:
    for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7):
        f()
        print("done", f.__name__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
