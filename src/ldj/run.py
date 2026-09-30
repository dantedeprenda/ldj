"""Run a config: every method x label budget x seed, scored and priced on the test split.

Per (method, k, seed) the method is fit on the k labeled items and scores the test split.
Thresholds for the cost policy come from cross-fitted scores on the same k labeled items only
(never from test). Everything is saved so tables can be recomputed offline:

    results/<name>/preds.npz      test scores, keyed "<method>|<k>|<seed>"
    results/<name>/records.json   one record per (method, k, seed)
    results/<name>/summary.md     mean discrimination and cost tables
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.model_selection import StratifiedKFold

from ldj import metrics
from ldj.cache import CallCache
from ldj.cost import Prices, aggregate, choose_thresholds, item_costs, recall_threshold
from ldj.methods import build_methods
from ldj.methods.base import Method
from ldj.task import Task, k_shot
from ldj.tasks import load_task

_log = logging.getLogger(__name__)


def kname(k: int | None) -> str:
    return "all" if k is None else str(k)


def draw(task: Task, k: int | None, seed: int, cfg: dict) -> np.ndarray:
    """Labeled set. ``min_each`` applies only below ``min_each_below`` (a pre-registered rule
    for tiny budgets); otherwise draws are uniform, as in the routing paper."""
    rule = cfg.get("draw", {})
    small = k is not None and k < rule.get("min_each_below", 0)
    return k_shot(task.train, k, seed, y=task.y, min_each=rule.get("min_each", 0) if small else 0)


def cross_fit(method: Method, task: Task, lab: np.ndarray, folds: int = 5) -> np.ndarray | None:
    """Out-of-fold scores on the labeled items; None when an outcome has < 2 labels."""
    y = task.y[lab]
    minority = int(min(y.sum(), len(y) - y.sum()))
    if minority < 2:
        return None
    out = np.empty(len(lab))
    split = StratifiedKFold(n_splits=min(folds, minority), shuffle=True, random_state=0)
    for tr, te in split.split(lab, y):
        out[te] = method.fit(task, lab[tr]).predict(task, lab[te])
    return out


def run(cfg: dict[str, Any], out_root: str = "results") -> list[dict]:
    """``per_category: true`` fits every method separately inside each category (e.g. each
    systematic review: its own k labels, its own thresholds) and pools the test predictions,
    so pooled metrics compare methods on the same items."""
    task = load_task(cfg["task"])
    cache = CallCache(cfg.get("cache", ".cache/calls.sqlite"))
    methods = build_methods(cfg["methods"], cache, max_usd=cfg.get("max_usd"))
    ks = [None if k == "all" else int(k) for k in cfg["ks"]]
    seeds = cfg["seeds"]
    prices = [Prices(**p) for p in cfg.get("prices", [])]
    rules = list(cfg.get("threshold_rules", ["empirical", "ucb"]))
    rules += [
        f"recall{round(100 * t)}_{r}"
        for t in cfg.get("recall_targets", [])
        for r in ("empirical", "ucb")
    ]
    out = Path(out_root) / cfg["name"]
    out.mkdir(parents=True, exist_ok=True)
    groups = _groups(task, cfg)
    yt, ct = task.y[task.test], task.categories[task.test]
    ident = np.arange(len(task.test))[None, :]
    preds: dict[str, np.ndarray] = {}
    records: list[dict] = []
    for m in methods:
        for k in ks:
            if getattr(m, "only_ks", None) and kname(k) not in m.only_ks:
                continue
            for seed in seeds if k is not None else seeds[:1]:
                t0 = time.perf_counter()
                p = np.empty(len(task.test))
                inference = np.zeros(len(task.test))
                parts: dict[tuple, list] = {}
                n_lab = n_pos = 0
                for sub, where in groups:
                    lab = draw(sub, k, seed, cfg)
                    n_lab, n_pos = n_lab + len(lab), n_pos + int(sub.y[lab].sum())
                    ps = m.fit(sub, lab).predict(sub, sub.test)
                    inf = getattr(m, "cost_", None)
                    m.__dict__.pop("cost_", None)
                    p[where] = ps
                    if inf is not None:
                        inference[where] = inf
                    if not prices or not getattr(m, "policies", True):
                        continue
                    p_cv = cross_fit(m, sub, lab)
                    for pr in prices:
                        for rule in rules:
                            t_lo, t_hi = _thresholds(sub, lab, p_cv, pr, rule)
                            c = item_costs(sub, sub.test, ps, t_lo, t_hi, pr, inference=inf)
                            parts.setdefault((pr, rule), []).append(
                                (c, sub.y[sub.test], t_lo, t_hi)
                            )
                preds[f"{m.name}|{kname(k)}|{seed}"] = p
                if inference.any():
                    preds[f"cost:{m.name}|{kname(k)}|{seed}"] = inference
                rec = {
                    "method": m.name,
                    "k": kname(k),
                    "seed": seed,
                    "n_lab": n_lab,
                    "n_pos_lab": n_pos,
                    "within_auroc": float(metrics.within_rows(p, yt, ct, ident)[0]),
                    "auroc": metrics.auroc(p, yt),
                    "aurc": metrics.aurc(p, yt),
                    "risk_at_50": metrics.risk_at(p, yt, 0.5),
                    "inference_usd_per_item": float(inference.mean()),
                    "policies": [],
                }
                if cfg.get("wss"):
                    rec["wss95"] = _mean_wss(p, yt, ct)
                for (pr, rule), got in parts.items():
                    label = n_lab * task.label_cost / pr.volume / len(groups)
                    s = aggregate([g[0] for g in got], label, np.concatenate([g[1] for g in got]))
                    s["thresholds"] = [[float(g[2]), float(g[3])] for g in got]  # per group
                    rec["policies"].append({**pr.__dict__, "rule": rule, **s})
                rec["seconds"] = round(time.perf_counter() - t0, 2)
                records.append(rec)
                print(
                    f"{m.name:22s} k={kname(k):>4s} seed={seed:<5d} "
                    f"within={rec['within_auroc']:.3f} auroc={rec['auroc']:.3f} "
                    f"({rec['seconds']}s)",
                    flush=True,
                )
            _save(out, preds, records, cfg, task)  # checkpoint after every budget
        spent = sum(getattr(b, "new_spend", 0.0) for b in _backends(m))
        if spent:
            print(f"  {m.name}: new spend ${spent:.4f}", flush=True)
    _save(out, preds, records, cfg, task)
    return records


def _save(out: Path, preds, records, cfg, task) -> None:
    np.savez_compressed(out / "preds.npz", **preds)
    (out / "records.json").write_text(json.dumps(records, indent=1, default=float))
    (out / "summary.md").write_text(summary(cfg, task, records))


def _groups(task: Task, cfg: dict) -> list[tuple[Task, np.ndarray]]:
    """(sub-task, positions of its test items within task.test) per category, or the whole
    task."""
    if not cfg.get("per_category"):
        return [(task, np.arange(len(task.test)))]
    return [
        (task.subset(c), np.flatnonzero(task.categories[task.test] == c))
        for c in np.unique(task.categories)
    ]


def _thresholds(sub: Task, lab, p_cv, pr: Prices, rule: str) -> tuple[float, float]:
    if p_cv is None:
        return -np.inf, np.inf  # no evidence: defer everything
    if rule.startswith("recall"):
        target, kind = rule[len("recall") :].split("_")
        return recall_threshold(sub, lab, p_cv, int(target) / 100, rule=kind)
    return choose_thresholds(sub, lab, p_cv, pr, rule=rule)


def _mean_wss(p, y, cats) -> float:
    """n-weighted mean WSS@95 over categories with at least MIN_CLASS positives."""
    num = den = 0.0
    for c in np.unique(cats):
        mk = cats == c
        if y[mk].sum() >= metrics.MIN_CLASS:
            num += metrics.wss(p[mk], y[mk]) * mk.sum()
            den += mk.sum()
    return num / den if den else float("nan")


def _backends(m: Method) -> list:
    found = []
    for obj in (m, getattr(m, "answerer", None)):
        b = getattr(obj, "backend", None)
        if b is not None:
            found.append(b)
    return found


def summary(cfg: dict, task: Task, records: list[dict]) -> str:
    methods = list(dict.fromkeys(r["method"] for r in records))
    ks = list(dict.fromkeys(r["k"] for r in records))
    yt = task.y[task.test]
    lines = [
        f"# {cfg['name']}",
        "",
        (
            f"Task {task.name}: {task.n:,} items, train {len(task.train):,}, test "
            f"{len(task.test):,} ({yt.mean():.1%} positive)."
        ),
        "",
        "## Within-category AUROC (mean over seeds)",
        "",
        "| method | " + " | ".join(f"k={k}" for k in ks) + " |",
        "|---|" + "---|" * len(ks),
    ]
    for m in methods:
        cells = []
        for k in ks:
            v = [r["within_auroc"] for r in records if r["method"] == m and r["k"] == k]
            cells.append(f"{np.nanmean(v):.3f}" if v else "")
        lines.append(f"| {m} | " + " | ".join(cells) + " |")
    pol = [p for r in records for p in r["policies"]]
    if pol:
        lines += [
            "",
            "## Cost per item with thresholds set from the k labels (mean over seeds)",
            "",
        ]
        combos = list(dict.fromkeys((p["c_fp"], p["c_fn"], p["rule"]) for p in pol))
        for c_fp, c_fn, rule in combos:
            lines += [
                f"### c_fp=${c_fp}, c_fn=${c_fn}, rule={rule}",
                "",
                "| method | " + " | ".join(f"k={k}" for k in ks) + " |",
                "|---|" + "---|" * len(ks),
            ]
            for m in methods:
                cells = []
                for k in ks:
                    v = [
                        (p["cost_per_item"], p["defer_rate"])
                        for r in records
                        if r["method"] == m and r["k"] == k
                        for p in r["policies"]
                        if (p["c_fp"], p["c_fn"], p["rule"]) == (c_fp, c_fn, rule)
                    ]
                    cells.append(
                        f"${np.mean([a for a, _ in v]):.4f} "
                        f"({np.mean([b for _, b in v]):.0%} deferred)"
                        if v
                        else ""
                    )
                lines.append(f"| {m} | " + " | ".join(cells) + " |")
            lines.append("")
    return "\n".join(lines) + "\n"
