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

import json
from pathlib import Path

import numpy as np
import yaml

from ldj import metrics
from ldj.cost import Prices, item_costs
from ldj.run import _groups, kname
from ldj.tasks import load_task


def analyze(
    config: str,
    exclude_audit: bool = False,
    task=None,
    preds_dir: str | None = None,
    out_dir: str | None = None,
) -> int:
    """``task``, ``preds_dir`` and ``out_dir`` let a packaged fixture (``ldj reproduce``) supply
    the test labels and saved predictions without downloading the dataset; by default they come
    from the config and results/<name>/."""
    cfg = yaml.safe_load(Path(config).read_text())
    an = cfg["analysis"]
    src = Path(preds_dir) if preds_dir else Path("results") / cfg["name"]
    out = Path(out_dir) if out_dir else src
    out.mkdir(parents=True, exist_ok=True)
    preds = np.load(src / "preds.npz")
    records = json.loads((src / "records.json").read_text())
    task = task if task is not None else load_task(cfg["task"])
    seeds = cfg["seeds"]
    ks = [None if k == "all" else int(k) for k in cfg["ks"]]
    keep = np.ones(len(task.test), bool)  # test positions scored
    suffix = ""
    if exclude_audit:
        audit = json.loads(Path(f"results/audit_{cfg['name']}.json").read_text())
        keep = ~np.isin(np.asarray(task.ids, dtype=object)[task.test], audit["disagree_ids"])
        suffix = "_audit"
    yt, ct = task.y[task.test][keep], task.categories[task.test][keep]
    b = an.get("B", 2000)
    rng = np.random.default_rng(0)
    draws = metrics.stratified_draws(ct, rng, b)
    sdraws = metrics.seed_draws(len(seeds), b, rng)
    methods = {r["method"] for r in records}
    primary = an["primary"]
    baselines = [m for m in an["baselines"] if m in methods]
    others = [m for m in an.get("others", []) if m in methods]

    def p_of(m, k, s):
        key = f"{m}|{kname(k)}|{s if k is not None else seeds[0]}"
        return preds[key][keep] if key in preds.files else None

    def within(m, k):
        rows = [p_of(m, k, s) for s in seeds]
        if any(r is None for r in rows):
            return None
        return np.stack([metrics.within_rows(r, yt, ct, draws) for r in rows])

    rule_k = an.get("rule_k", 25)
    means = {m: float(np.nanmean(within(m, rule_k)[:, 0])) for m in baselines}
    best = max(baselines, key=lambda m: (means[m], -baselines.index(m)))
    lines = [
        f"# Pre-registered analysis: {cfg['name']}",
        "",
    ]
    if exclude_audit:
        lines += [
            (
                f"**Label-noise sensitivity:** {int((~keep).sum())} test items the blind audit "
                f"marked differently are removed; {int(keep.sum())} remain."
            ),
            "",
        ]
    lines += [
        f"Primary method: **{primary}**. Best text baseline at k = {rule_k} (pre-registered "
        f"rule): **{best}** ({means[best]:.3f}; others: "
        + ", ".join(f"{m} {v:.3f}" for m, v in means.items() if m != best)
        + ").",
        "",
        "## A. Within-category AUROC, primary minus comparator (95% CI, hierarchical bootstrap)",
        "",
        "| k | comparator | primary | comparator | diff | 95% CI | seeds won |",
        "|---|---|---|---|---|---|---|",
    ]
    payload: dict = {"best_baseline": best, "baseline_means_at_rule_k": means, "a": [], "b": []}
    comparators = [best] + [m for m in baselines if m != best] + others
    for k in ks:
        f = within(primary, k)
        if f is None:
            continue
        for c in comparators:
            g = within(c, k)
            if g is None:
                continue
            diff = f - g
            d, lo, hi = metrics.ci(metrics.seed_boot(diff, sdraws))
            won = int((diff[:, 0] > 0).sum())
            row = {
                "k": kname(k),
                "comparator": c,
                "primary": float(np.nanmean(f[:, 0])),
                "comparator_auroc": float(np.nanmean(g[:, 0])),
                "diff": d,
                "ci95": [lo, hi],
                "seeds_won": won,
                "best_baseline": c == best,
            }
            payload["a"].append(row)
            tag = " (best)" if c == best else ""
            lines.append(
                f"| {kname(k)} | {c}{tag} | {row['primary']:.3f} | "
                f"{row['comparator_auroc']:.3f} | {d:+.3f} | [{lo:+.3f}, {hi:+.3f}] | "
                f"{won}/{len(seeds)} |"
            )

    cost = an.get("cost")
    if cost:
        pr = Prices(c_fp=cost["c_fp"], c_fn=cost["c_fn"], volume=cost.get("volume", 10_000))
        groups = _groups(task, cfg)

        def item_cost(m, k, s):
            rec = next(
                (
                    r
                    for r in records
                    if r["method"] == m
                    and r["k"] == kname(k)
                    and r["seed"] == (s if k is not None else seeds[0])
                ),
                None,
            )
            if rec is None:
                return None
            pol = next(
                (
                    p
                    for p in rec["policies"]
                    if p["c_fp"] == pr.c_fp and p["c_fn"] == pr.c_fn and p["rule"] == cost["rule"]
                ),
                None,
            )
            if pol is None:  # method without cost policies (SetFit, pre-registered)
                return None
            p = preds[f"{m}|{kname(k)}|{s if k is not None else seeds[0]}"]  # all test items
            inf_key = f"cost:{m}|{kname(k)}|{s if k is not None else seeds[0]}"
            inf = preds[inf_key] if inf_key in preds.files else np.zeros(len(task.test))
            out_c = np.empty(len(task.test))
            for (sub, where), (t_lo, t_hi) in zip(groups, pol["thresholds"], strict=True):
                out_c[where] = item_costs(
                    sub, sub.test, p[where], t_lo, t_hi, pr, inference=inf[where]
                )["cost"]
            return out_c[keep] + pol["label_cost_per_item"]

        lines += [
            "",
            (
                f"## B. Cost per item (c_fp=${pr.c_fp}, c_fn=${pr.c_fn}, rule="
                f"{cost['rule']}), primary minus comparator; negative = primary cheaper"
            ),
            "",
            "| k | comparator | primary $ | comparator $ | diff $ | 95% CI |",
            "|---|---|---|---|---|---|",
        ]
        for k in ks:
            fc = [item_cost(primary, k, s) for s in seeds]
            if any(x is None for x in fc):
                continue
            fc = np.stack(fc)
            for c in comparators:
                gc = [item_cost(c, k, s) for s in seeds]
                if any(x is None for x in gc):
                    continue
                gc = np.stack(gc)
                diff = np.stack([(fc[i] - gc[i])[draws].mean(axis=1) for i in range(len(seeds))])
                d, lo, hi = metrics.ci(metrics.seed_boot(diff, sdraws))
                row = {
                    "k": kname(k),
                    "comparator": c,
                    "primary_usd": float(fc.mean()),
                    "comparator_usd": float(gc.mean()),
                    "diff": d,
                    "ci95": [lo, hi],
                }
                payload["b"].append(row)
                lines.append(
                    f"| {kname(k)} | {c} | {row['primary_usd']:.4f} | "
                    f"{row['comparator_usd']:.4f} | {d:+.4f} | [{lo:+.4f}, {hi:+.4f}] |"
                )
    (out / f"analysis{suffix}.md").write_text("\n".join(lines) + "\n")
    (out / f"analysis{suffix}.json").write_text(json.dumps(payload, indent=1, default=float))
    print("\n".join(lines))
    return 0
