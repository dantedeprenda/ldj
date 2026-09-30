"""Total cost of a decision policy, and choosing its thresholds from the k labels alone.

A policy thresholds a method's scores: act "positive" when p >= t_hi, act "negative" when
p <= t_lo (only if the task allows automated negatives), and defer everything in between to
the reviewer. Per item it pays:

- inference: what the method spent scoring the item;
- acting: ``auto_cost`` (routing: the cheap model's answer), plus the error cost if the action
  is wrong (``c_fp`` for a wrong positive, ``c_fn`` for a wrong negative);
- deferring: ``review_cost``, plus the error cost times the chance the reviewer is wrong
  (reviewers are scored with real or published error rates, never as an oracle);
- labels: ``k * label_cost`` spread over the ``volume`` items the policy will handle.

Error costs are assumptions, so results are reported over a range of them.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.stats import beta

from ldj.task import Task


@dataclass(frozen=True)
class Prices:
    c_fp: float  # USD for acting positive on a negative item
    c_fn: float  # USD for acting negative on a positive item (or a reviewer missing one)
    volume: int = 10_000  # items the policy will handle; label cost is spread over these


def item_costs(
    task: Task, idx, p, t_lo: float, t_hi: float, prices: Prices, inference=None
) -> dict[str, np.ndarray]:
    """Per-item cost and action ('pos', 'neg', 'defer') for items ``idx`` scored ``p``."""
    y = task.y[idx]
    pos = p >= t_hi
    neg = (p <= t_lo) & ~pos if task.auto_negative else np.zeros(len(idx), bool)
    defer = ~pos & ~neg
    wrong_cost = np.where(y == 1, prices.c_fn, prices.c_fp)  # cost if the final decision errs
    hc = task.human_correct[idx]
    cost = np.where(pos, task.auto_cost[idx] + np.where(y == 0, prices.c_fp, 0.0), 0.0)
    cost += np.where(neg, task.auto_cost[idx] + np.where(y == 1, prices.c_fn, 0.0), 0.0)
    cost += np.where(defer, task.review_cost[idx] + (1 - hc) * wrong_cost, 0.0)
    if inference is not None:
        cost = cost + inference
    err = np.where(pos, y == 0, 0.0) + np.where(neg, y == 1, 0.0) + np.where(defer, 1 - hc, 0.0)
    return {"cost": cost, "error": err, "defer": defer, "pos": pos, "neg": neg}


def aggregate(parts: list[dict[str, np.ndarray]], label_per_item: float, y: np.ndarray) -> dict:
    """Summary over items pooled from one or more ``item_costs`` results (e.g. one per review).
    ``y`` is the pooled outcome vector, for recall."""
    c = {key: np.concatenate([d[key] for d in parts]) for key in parts[0]}
    auto = ~c["defer"]
    return {
        "cost_per_item": float(c["cost"].mean() + label_per_item),
        "label_cost_per_item": float(label_per_item),
        "error_rate": float(c["error"].mean()),
        "defer_rate": float(c["defer"].mean()),
        "auto_error_rate": float(c["error"][auto].mean()) if auto.any() else float("nan"),
        # screening view: share of items no human looks at, and share of positives not
        # auto-rejected (the reviewer's own misses are in error_rate, not here)
        "work_saved": float(auto.mean()),
        "machine_recall": float((~c["neg"])[y == 1].mean()) if (y == 1).any() else float("nan"),
    }


def summarize(task: Task, idx, p, t_lo, t_hi, prices: Prices, k: int, inference=None) -> dict:
    c = item_costs(task, idx, p, t_lo, t_hi, prices, inference)
    out = aggregate([c], k * task.label_cost / prices.volume, task.y[idx])
    return {**out, "t_lo": float(t_lo), "t_hi": float(t_hi)}


def recall_threshold(
    task: Task, lab, p_lab, target: float = 0.95, rule: str = "empirical", level: float = 0.9
) -> tuple[float, float]:
    """Screening policy: auto-reject the lowest-scored items, send the rest to a human, and
    keep at least ``target`` of the positives. Returns (t_lo, +inf); nothing is auto-accepted.

    ``empirical``: allow the misses the labeled positives permit (floor((1 - target) * n_pos)).
    ``ucb``: allow m misses only if the ``level`` lower confidence bound on recall still meets
    ``target`` (needs about 45 labeled positives before any work can be saved at 95%/0.9).
    With no labeled positives nothing is rejected.
    """
    y = task.y[lab]
    pos = np.sort(np.asarray(p_lab, float)[y == 1])
    n_pos = len(pos)
    if n_pos == 0:
        return -np.inf, np.inf
    if rule == "ucb":
        m = -1
        for misses in range(n_pos):
            s = n_pos - misses
            lower = beta.ppf(1 - level, s, misses + 1)
            if lower >= target:
                m = misses
            else:
                break
        if m < 0:
            return -np.inf, np.inf
    else:
        m = int(np.floor((1 - target) * n_pos))
    # reject everything strictly below the (m+1)-th lowest positive score: at most m misses
    return float(np.nextafter(pos[m], -np.inf)), np.inf


def _upper(errors: np.ndarray, n: np.ndarray, level: float) -> np.ndarray:
    """One-sided Clopper-Pearson upper bound on error rates (1 where n = 0 or all are errors)."""
    errors, n = np.asarray(errors, float), np.asarray(n, float)
    out = np.ones_like(errors)
    ok = (n > 0) & (errors < n)
    out[ok] = beta.ppf(level, errors[ok] + 1, n[ok] - errors[ok])
    return out


def choose_thresholds(
    task: Task, lab, p_lab, prices: Prices, rule: str = "empirical", level: float = 0.9
) -> tuple[float, float]:
    """(t_lo, t_hi) minimizing estimated cost on the labeled items, from cross-fitted scores
    ``p_lab``. ``rule='ucb'`` replaces each automated action's observed error count by its
    ``level`` upper confidence bound, so a threshold is only trusted where the few labels
    support it (small-sample thresholds are otherwise optimistic).

    Items sorted by score: the lowest j act negative, the highest n - i act positive, the rest
    are deferred; j and i fall only between distinct scores. Cost separates into a negative
    part (depends on j), a positive part (on i) and the deferred middle (prefix sums), so the
    best pair is a prefix minimum: linear in k.
    """
    order = np.argsort(p_lab, kind="stable")
    ps = np.asarray(p_lab, float)[order]
    lab = np.asarray(lab)[order]
    y, hc, auto = task.y[lab], task.human_correct[lab], task.auto_cost[lab]
    n = len(ps)
    wrong_cost = np.where(y == 1, prices.c_fn, prices.c_fp)
    cum = lambda a: np.concatenate([[0.0], np.cumsum(a)])
    d_cum = cum(task.review_cost[lab] + (1 - hc) * wrong_cost)
    auto_cum, pos_cum, neg_cum = cum(auto), cum(y == 1), cum(y == 0)
    bounds = np.array([b for b in range(n + 1) if b in (0, n) or ps[b - 1] != ps[b]])

    # Negative part for j = number acting negative.
    fn = pos_cum[bounds]
    if rule == "ucb":
        fn = _upper(fn, bounds, level) * bounds
    negc = auto_cum[bounds] + fn * prices.c_fn
    if not task.auto_negative:
        negc = np.where(bounds == 0, 0.0, np.inf)
    # Positive part for i = first index acting positive.
    tail = n - bounds
    fp = neg_cum[n] - neg_cum[bounds]
    if rule == "ucb":
        fp = _upper(fp, tail, level) * tail
    posc = auto_cum[n] - auto_cum[bounds] + fp * prices.c_fp

    # total(j, i) = negc[j] - d_cum[j] + posc[i] + d_cum[i] for j <= i.
    left = negc - d_cum[bounds]
    best_left = np.minimum.accumulate(left)
    arg_left = np.zeros(len(bounds), dtype=int)
    for m in range(1, len(bounds)):
        arg_left[m] = m if left[m] < left[arg_left[m - 1]] else arg_left[m - 1]
    total = best_left + posc + d_cum[bounds]
    m = int(np.argmin(total))
    j, i = bounds[arg_left[m]], bounds[m]
    t_lo = float(ps[j - 1]) if j > 0 else -np.inf
    t_hi = float(ps[i]) if i < n else np.inf
    return t_lo, t_hi
