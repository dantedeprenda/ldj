"""E-bridge on T0: value of escalating from the cheap to the strong model.

    uv run python scripts/bridge_t0.py [../routing-success-prediction/results/llmrouterbench_test]

Reuses the routing paper's saved per-prompt predictions (no refitting, no API calls) and LDJ's T0
export, which holds both models' correctness and cost on every prompt. The default is the cheap
model (pool[0]); the fallback is the strongest (pool[-1]).

Design, fixed before any E-bridge number was computed (2026-09-30): the saved predictions cover the
test split only, so no threshold is tuned. Each score escalates its top share of test prompts at
escalation rates fixed in advance (10/20/30/50%). Scores: difficulty = 1 − P(cheap right) and
benefit = P(strong right) − P(cheap right), from each router's success heads; random and oracle
bound them. Net repair is averaged over the five label seeds; the interval resamples prompts.
The benefit score needs heads for both models, so its label budget is twice the difficulty
score's (k executions of each model). Exploratory: these data have been seen by the routing paper.
Writes results/bridge_t0/report.{md,json}.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ldj import bridge
from ldj.tasks import load_task

RATES = [0.10, 0.20, 0.30, 0.50]
METHODS = ["jev_features", "tfidf_logreg", "bgeL_logreg", "bge_logreg"]
KS = ["25", "None"]  # routing result folders: seed<s>_k<k>
SEEDS = [42, 999, 2024, 2025, 3407]


def load_scores(root: Path, method: str, k: str, seed: int, pos: dict) -> np.ndarray | None:
    f = root / f"seed{seed}_k{k}" / f"{method}.jsonl"
    if not f.exists():
        return None
    p = np.full((len(pos), 3), np.nan)
    for line in f.read_text().splitlines():
        r = json.loads(line)
        if r["id"] in pos and r["p"] is not None:
            p[pos[r["id"]]] = r["p"]
    return None if np.isnan(p).any() else p


def main(root: str) -> int:
    root = Path(root)
    task = load_task({"name": "t0", "benchmark": "llmrouterbench"})
    test = np.asarray(task.test)
    ids = np.asarray(task.ids, dtype=object)
    pos = {i: j for j, i in enumerate(ids[test])}

    def paired(idx):
        return bridge.Paired(
            task.y[idx].astype(int),
            (task.human_correct[idx] >= 0.5).astype(int),
            task.auto_cost[idx],
            task.review_cost[idx],
        )

    pt = paired(test)
    tables = {"train": bridge.table(paired(np.asarray(task.train))), "test": bridge.table(pt)}
    out: dict = {"pool": task.meta["pool"], "tables": tables, "rows": []}
    for rate in RATES:
        base = {"rate": rate}
        rnd = [bridge.escalate_top(np.zeros(pt.n), rate, seed=s) for s in SEEDS]
        orc = [bridge.oracle_mask(pt, rate)]
        for name, masks in [("random", rnd), ("oracle", orc)]:
            o = [bridge.outcome(pt, m) for m in masks]
            out["rows"].append(
                {**base, "policy": name, "k": "-", **_mean(o), "net_ci": bridge.net_ci(pt, masks)}
            )
        for m in METHODS:
            for k in KS:
                ps = [load_scores(root, m, k, s, pos) for s in SEEDS]
                if any(p is None for p in ps):
                    continue
                for score_name, fn in [
                    ("difficulty", lambda p: 1 - p[:, 0]),
                    ("benefit", lambda p: p[:, -1] - p[:, 0]),
                ]:
                    masks = [bridge.escalate_top(fn(p), rate, seed=s) for p, s in zip(ps, SEEDS)]
                    o = [bridge.outcome(pt, mk) for mk in masks]
                    out["rows"].append(
                        {
                            **base,
                            "policy": f"{m}:{score_name}",
                            "k": "all" if k == "None" else k,
                            **_mean(o),
                            "net_ci": bridge.net_ci(pt, masks),
                        }
                    )
    dest = Path("results/bridge_t0")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "report.json").write_text(json.dumps(out, indent=1, default=float))
    (dest / "report.md").write_text(_markdown(out))
    print(_markdown(out))
    return 0


def _mean(outcomes: list[dict]) -> dict:
    keys = [
        "accuracy",
        "cost",
        "repaired",
        "broken",
        "net_per_item",
        "repair_rate_escalated",
        "break_rate_escalated",
    ]
    return {k: float(np.mean([o[k] for o in outcomes])) for k in keys}


def _markdown(out: dict) -> str:
    t, tr = out["tables"]["test"], out["tables"]["train"]
    lines = [
        "# E-bridge on T0: value of escalating cheap → strong (exploratory)",
        "",
        f"Default: {out['pool'][0]}. Fallback: {out['pool'][-1]}.",
        "",
        (
            "| split | n | both right | only cheap right (escalating breaks) | only strong right "
            "(escalating repairs) | both wrong | escalation value | cheap $ | strong $ |"
        ),
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for name, x in [("train", tr), ("test", t)]:
        lines.append(
            f"| {name} | {x['n']} | {x['both_right']} | {x['only_default_right']} | "
            f"{x['only_fallback_right']} | {x['both_wrong']} | {x['escalation_value']:+.3f} | "
            f"{x['default_cost']:.5f} | {x['fallback_cost']:.5f} |"
        )
    lines += [
        "",
        (
            "Escalating the top-scored share of test prompts (mean over 5 label seeds; interval "
            "resamples prompts). Net = (repaired − broken) / all prompts."
        ),
        "",
        (
            "| rate | policy | k | accuracy | $/prompt | repaired | broken | net | 95% CI | "
            "repair rate among escalated |"
        ),
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in out["rows"]:
        m, lo, hi = r["net_ci"]
        lines.append(
            f"| {r['rate']:.0%} | {r['policy']} | {r['k']} | {r['accuracy']:.3f} | "
            f"{r['cost']:.5f} | {r['repaired']:.1f} | {r['broken']:.1f} | {m:+.4f} | "
            f"[{lo:+.4f}, {hi:+.4f}] | {r['repair_rate_escalated']:.3f} |"
        )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    raise SystemExit(
        main(
            sys.argv[1] if len(sys.argv) > 1 else "../routing-success-prediction/results/llmrouterbench_test"
        )
    )
