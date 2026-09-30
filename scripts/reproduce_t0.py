"""Check this harness against the routing paper's saved results (no API calls).

    uv run ldj run configs/t0_reproduce.yaml
    uv run python scripts/reproduce_t0.py ../routing-success-prediction/results/llmrouterbench_test/metrics.json

Compares mean within-category AUROC per (method, k) with the paper's pipeline ('raw' variant).
Exits non-zero unless every cell matches to 1e-4.
"""

import json
import sys
from pathlib import Path

import numpy as np

NAMES = {  # harness -> paper
    "jev_features": "jev:features",
    "tfidf_logreg": "tfidf_logreg",
    "tfidf_knn10": "knn10",
    "bge_logreg": "bge_logreg",
    "bge_knn": "bge_knn",
    "bgeL_logreg": "bgeL_logreg",
    "bgeL_knn": "bgeL_knn",
}


def main(paper_metrics: str) -> int:
    ours = json.loads(Path("results/t0_reproduce/records.json").read_text())
    ref = json.loads(Path(paper_metrics).read_text())
    worst, cells = 0.0, 0
    for m, pm in NAMES.items():
        for k in ["25", "50", "100", "200", "all"]:
            a = [r["within_auroc"] for r in ours if r["method"] == m and r["k"] == k]
            kk = None if k == "all" else int(k)
            b = [
                r["by_category"]["within"]
                for r in ref
                if r["router"] == pm and r.get("k") == kk and r.get("variant") == "raw"
            ]
            gap = abs(np.mean(a) - np.mean(b))
            worst, cells = max(worst, gap), cells + 1
            flag = "" if gap < 1e-4 else "  <-- MISMATCH"
            print(f"{m:14s} k={k:>4s} harness {np.mean(a):.4f} paper {np.mean(b):.4f}{flag}")
    print(f"{cells} cells, max |difference| = {worst:.6f}")
    return 0 if worst < 1e-4 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
