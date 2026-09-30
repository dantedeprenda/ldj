"""X1 arm (a): calibration of the zero-shot judge, raw vs Platt-scaled on the k labels.

    uv run python scripts/x1_calibration.py configs/x1_t1.yaml

Platt scaling is monotone (with a positive slope), so ranking and the thresholds a rule picks
are unchanged; this reports what can change: Brier score and 10-bin expected calibration error
on the test split, mean over label seeds. It also reports the largest within-category AUROC
change, which should be 0 unless a fitted slope came out negative. Reads results/<name>/preds.npz.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import yaml

from ldj import metrics
from ldj.run import kname
from ldj.tasks import load_task


def ece(p: np.ndarray, y: np.ndarray, bins: int = 10) -> float:
    edges = np.linspace(0, 1, bins + 1)
    which = np.clip(np.digitize(p, edges[1:-1]), 0, bins - 1)
    return float(
        sum(
            abs(p[which == b].mean() - y[which == b].mean()) * (which == b).mean()
            for b in range(bins)
            if (which == b).any()
        )
    )


def main(config: str) -> int:
    cfg = yaml.safe_load(Path(config).read_text())
    task = load_task(cfg["task"])
    preds = np.load(Path("results") / cfg["name"] / "preds.npz")
    yt, ct = task.y[task.test], task.categories[task.test]
    ident = np.arange(len(yt))[None, :]
    raw_name, platt_name = "gemma_judge_0shot", "gemma_judge_0shot_platt"
    raw = preds[f"{raw_name}|all|{cfg['seeds'][0]}"]  # zero-shot: the same for every k
    lines = [
        f"# X1 arm (a): judge calibration, {cfg['name']} (exploratory)",
        "",
        f"Raw judge: Brier {np.mean((raw - yt) ** 2):.4f}, ECE {ece(raw, yt):.4f}.",
        "",
        "| k | Platt Brier | Platt ECE | max within-AUROC change vs raw |",
        "|---|---|---|---|",
    ]
    raw_within = float(metrics.within_rows(raw, yt, ct, ident)[0])
    for k in [None if k == "all" else int(k) for k in cfg["ks"]]:
        seeds = cfg["seeds"] if k is not None else cfg["seeds"][:1]
        ps = [preds[f"{platt_name}|{kname(k)}|{s}"] for s in seeds]
        brier = np.mean([np.mean((p - yt) ** 2) for p in ps])
        e = np.mean([ece(p, yt) for p in ps])
        dw = max(abs(float(metrics.within_rows(p, yt, ct, ident)[0]) - raw_within) for p in ps)
        lines.append(f"| {kname(k)} | {brier:.4f} | {e:.4f} | {dw:.4f} |")
    out = Path("results") / cfg["name"] / "calibration.md"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
