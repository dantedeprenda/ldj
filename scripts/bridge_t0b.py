"""E-bridge on TwinRouterBench (T0b): escalating from the cheapest to the strongest pool model.

    uv run python scripts/bridge_t0b.py [../routing-success-prediction/results/twinrouterbench_test]

Needs data/t0/twinrouterbench_pool.npz (scripts/export_t0b_pool.py). Same design as
scripts/bridge_t0.py and bridge_t0_equal_cost.py, fixed before computing (2026-09-30): the routing
paper's saved success heads (no refitting); each score escalates its top share of test prompts at
10/20/30/50%; difficulty = 1 - P(cheap), benefit = P(strong) - P(cheap); mean over 5 label seeds;
prompt bootstrap. Equal cost: each cheap -> strong policy is read off at the cost of every
intermediate fixed model (always-mid, always-mid_high) and compared with that model's accuracy.
Exploratory: these data have been seen by the routing paper. Writes results/bridge_t0b/report.md.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ldj import bridge

sys.path.insert(0, str(Path(__file__).parent))
from bridge_t0 import SEEDS

RATES = [0.10, 0.20, 0.30, 0.50]


def load_scores(root: Path, method: str, k: str, seed: int, pos: dict, n_models: int):
    """Per-prompt P(success) for every pool model from a routing result file (None if absent)."""
    f = root / f"seed{seed}_k{k}" / f"{method}.jsonl"
    if not f.exists():
        return None
    p = np.full((len(pos), n_models), np.nan)
    for line in f.read_text().splitlines():
        r = json.loads(line)
        if r["id"] in pos and r["p"] is not None:
            p[pos[r["id"]]] = r["p"]
    return None if np.isnan(p).any() else p


METHODS = ["jev-4k_features", "jev_features", "tfidf_logreg", "bgeL_logreg", "bge_logreg"]
KS = ["25", "None"]
B = 500


def main(root: str) -> int:
    root = Path(root)
    pool = np.load("data/t0/twinrouterbench_pool.npz", allow_pickle=True)
    test = np.load("data/t0/twinrouterbench.npz", allow_pickle=True)["test"]
    ids = pool["ids"][test]
    pos = {i: j for j, i in enumerate(ids)}
    ok, cost = pool["correct"][test].astype(int), pool["cost"][test]
    names = [str(x) for x in pool["pool"]]
    n = len(test)
    p = bridge.Paired(ok[:, 0], ok[:, -1], cost[:, 0], cost[:, -1])
    t = bridge.table(p)
    rng = np.random.default_rng(0)
    weights = [np.ones(n)] + [np.bincount(rng.integers(0, n, n), minlength=n) for _ in range(B)]
    mids = list(range(1, len(names) - 1))

    scores = {
        "random": [(s, np.zeros(n)) for s in SEEDS],
        "oracle": [(0, 2.0 * p.repair + 1.0 * ~p.breaks)],
    }
    for m in METHODS:
        for k in KS:
            ps = [load_scores(root, m, k, s, pos, len(names)) for s in SEEDS]
            if any(x is None for x in ps):
                continue
            kk = "all" if k == "None" else k
            scores[f"{m}: difficulty ({kk})"] = [(s, 1 - x[:, 0]) for x, s in zip(ps, SEEDS)]
            scores[f"{m}: benefit ({kk})"] = [(s, x[:, -1] - x[:, 0]) for x, s in zip(ps, SEEDS)]

    fixed = "; ".join(
        f"{nm} {ok[:, j].mean():.3f} at ${cost[:, j].mean():.5f}" for j, nm in enumerate(names)
    )
    lines = [
        "# E-bridge on TwinRouterBench: cheapest -> strongest (exploratory)",
        "",
        f"Always-X on test ({n} prompts): {fixed}.",
        "",
        (
            f"Four cells: both right {t['both_right']}; only cheap right {t['only_default_right']}; "
            f"only strong right {t['only_fallback_right']}; both wrong {t['both_wrong']}. "
            f"Escalation value {t['escalation_value']:+.3f}."
        ),
        "",
        "## Net repair per prompt at fixed escalation rates (mean over seeds; 95% CI over prompts)",
        "",
        "| policy | " + " | ".join(f"{r:.0%}" for r in RATES) + " |",
        "|---|" + "---|" * len(RATES),
    ]
    rows = {}
    for name, sc in scores.items():
        cells = []
        for r in RATES:
            masks = [
                bridge.oracle_mask(p, r) if name == "oracle" else bridge.escalate_top(s, r, seed=k)
                for k, s in sc
            ]
            cells.append(bridge.net_ci(p, masks))
        rows[name] = cells
        lines.append(
            f"| {name} | "
            + " | ".join(f"{c[0]:+.3f} [{c[1]:+.3f}, {c[2]:+.3f}]" for c in cells)
            + " |"
        )
    lines += ["", "## Equal cost: accuracy minus the fixed model's, at that model's cost", ""]
    lines += [
        "| policy | " + " | ".join(f"vs always-{names[j]}" for j in mids) + " |",
        "|---|" + "---|" * len(mids),
    ]
    eq = {}
    for name, sc in scores.items():
        cells = []
        for j in mids:
            out = []
            for w in weights:
                tgt = float((w * cost[:, j]).sum() / w.sum())
                base = float((w * ok[:, j]).sum() / w.sum())
                vals = [bridge.at_cost(*bridge.frontier(p, s, seed=k, w=w), tgt) for k, s in sc]
                out.append(np.mean(vals) - base)
            d = np.array(out)
            lo, hi = np.nanpercentile(d[1:], [2.5, 97.5])
            cells.append((float(d[0]), float(lo), float(hi)))
        eq[name] = cells
        lines.append(
            f"| {name} | "
            + " | ".join(f"{c[0]:+.3f} [{c[1]:+.3f}, {c[2]:+.3f}]" for c in cells)
            + " |"
        )
    dest = Path("results/bridge_t0b")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "report.md").write_text("\n".join(lines) + "\n")
    (dest / "report.json").write_text(
        json.dumps({"table": t, "fixed_rates": rows, "equal_cost": eq}, indent=1, default=float)
    )
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(
        main(
            sys.argv[1]
            if len(sys.argv) > 1
            else "../routing-success-prediction/results/twinrouterbench_test"
        )
    )
