"""E-bridge on T0 at equal cost: can any escalation policy beat always using the mid model?

    uv run python scripts/bridge_t0_equal_cost.py [../routing-success-prediction/results/llmrouterbench_test]

Needs data/t0/llmrouterbench_pool.npz (``scripts/export_t0_pool.py``). The routing paper's best
fixed choice is the mid-priced model (deepseek-r1). Each policy starts from the cheap model and
escalates prompts in score order; its accuracy is read off where its cost equals always-mid's
test cost, and always-mid's accuracy is subtracted. A positive difference would beat the best
fixed model at equal cost.

Design, fixed before computing (2026-09-30): target cost = always-mid's mean cost on the test
split; scores from the routing paper's saved success heads (no refitting): cheap -> strong by
difficulty 1 - P(cheap) and by benefit P(strong) - P(cheap); random and oracle bounds. (A
cheap -> mid policy is left out: at always-mid's cost it must escalate everything, so it equals
always-mid by construction.) Mean over the 5 label seeds; 95% interval from 500
prompt bootstraps (the same resample for the policy and the baseline). Reading the curve at a
fixed cost uses test costs, not test outcomes. Exploratory: the routing data have been seen.
Writes results/bridge_t0/equal_cost.{md,json}.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ldj import bridge

sys.path.insert(0, str(Path(__file__).parent))
from bridge_t0 import KS, METHODS, SEEDS, load_scores

B = 500


def main(root: str) -> int:
    root = Path(root)
    pool = np.load("data/t0/llmrouterbench_pool.npz", allow_pickle=True)
    main_npz = np.load("data/t0/llmrouterbench.npz", allow_pickle=True)
    test = main_npz["test"]
    ids = pool["ids"][test]
    pos = {i: j for j, i in enumerate(ids)}
    ok, cost = pool["correct"][test].astype(int), pool["cost"][test]
    names = [str(x) for x in pool["pool"]]
    n = len(test)
    rng = np.random.default_rng(0)
    weights = [np.ones(n)] + [np.bincount(rng.integers(0, n, n), minlength=n) for _ in range(B)]

    def pair(fb):
        return bridge.Paired(ok[:, 0], ok[:, fb], cost[:, 0], cost[:, fb])

    to_strong = pair(-1)
    target = [float((w * cost[:, 1]).sum() / w.sum()) for w in weights]
    mid_acc = [float((w * ok[:, 1]).sum() / w.sum()) for w in weights]

    def diff(p, scores):
        """Per bootstrap weight: mean over seeds of acc at the mid's cost, minus mid's acc."""
        out = []
        for w, tgt, base in zip(weights, target, mid_acc):
            vals = [bridge.at_cost(*bridge.frontier(p, s, seed=k, w=w), tgt) for k, s in scores]
            out.append(np.mean(vals) - base)
        d = np.array(out)
        lo, hi = np.nanpercentile(d[1:], [2.5, 97.5])
        return float(d[0]), float(lo), float(hi)

    rows = []
    oracle = 2.0 * to_strong.repair + 1.0 * ~to_strong.breaks
    rows.append(("oracle (cheap -> strong)", "-", diff(to_strong, [(0, oracle)])))
    rows.append(
        ("random (cheap -> strong)", "-", diff(to_strong, [(s, np.zeros(n)) for s in SEEDS]))
    )
    for m in METHODS:
        for k in KS:
            ps = [load_scores(root, m, k, s, pos) for s in SEEDS]
            if any(p is None for p in ps):
                continue
            kk = "all" if k == "None" else k
            rows += [
                (
                    f"{m}: difficulty -> strong",
                    kk,
                    diff(to_strong, [(s, 1 - p[:, 0]) for p, s in zip(ps, SEEDS)]),
                ),
                (
                    f"{m}: benefit -> strong",
                    kk,
                    diff(to_strong, [(s, p[:, -1] - p[:, 0]) for p, s in zip(ps, SEEDS)]),
                ),
            ]
    fixed = {nm: (float(ok[:, j].mean()), float(cost[:, j].mean())) for j, nm in enumerate(names)}
    lines = [
        "# E-bridge on T0 at equal cost vs always-mid (exploratory)",
        "",
        "Always-X on test: "
        + "; ".join(f"{nm} acc {a:.3f} at ${c:.5f}" for nm, (a, c) in fixed.items()),
        "",
        (
            "Accuracy of each policy at always-mid's cost, minus always-mid's accuracy "
            "(positive = beats the best fixed model at equal cost)."
        ),
        "",
        "| policy | k | difference | 95% CI |",
        "|---|---|---|---|",
    ]
    for name, k, (d, lo, hi) in rows:
        lines.append(f"| {name} | {k} | {d:+.4f} | [{lo:+.4f}, {hi:+.4f}] |")
    dest = Path("results/bridge_t0")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "equal_cost.md").write_text("\n".join(lines) + "\n")
    (dest / "equal_cost.json").write_text(
        json.dumps({"fixed": fixed, "rows": rows}, indent=1, default=float)
    )
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(
        main(
            sys.argv[1] if len(sys.argv) > 1 else "../routing-success-prediction/results/llmrouterbench_test"
        )
    )
