"""Pre-registered comparisons for a finished run (no API calls).

    uv run python scripts/analyze.py configs/t1.yaml
    uv run python scripts/analyze.py configs/t1.yaml --exclude-audit

Reads results/<name>/{preds.npz,records.json} and the config's ``analysis`` block:

    analysis:
      primary: gemma_features         # the method the hypotheses are about
      baselines: [tfidf_logreg, ...]  # text baselines; the strongest at k = rule_k is "best"
      others: [gemma_judge_0shot]     # further comparisons (reported, two-sided)
      rule_k: 25
      cost: {c_fp: 1.0, c_fn: 1.0, rule: ucb}   # the primary cost setting
      B: 2000

A. Within-category AUROC, primary minus each comparator, at every k: hierarchical paired
   bootstrap (resample label seeds, and test items within category), as in the routing paper.
B. Cost per item at the primary cost setting, primary minus each comparator, same bootstrap,
   from item costs recomputed with the thresholds each run chose on its own k labels.
Writes results/<name>/analysis.{md,json}.

``--exclude-audit`` is the pre-registered label-noise sensitivity check: the same analysis with
the test items the blind audit marked differently (results/audit_<name>.json) removed. Fitting
and thresholds are untouched (they use training labels only). Writes analysis_audit.{md,json}.
"""

from __future__ import annotations

import sys

from ldj.analysis import analyze

if __name__ == "__main__":
    raise SystemExit(analyze(sys.argv[1], exclude_audit="--exclude-audit" in sys.argv[2:]))
