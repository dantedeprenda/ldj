"""Certifying when it is safe to automate, from a random sample of human labels.

Two guarantees, both distribution-free and holding with probability >= 1 - delta over the
draw of the certification sample:

- **Selective risk** (T0, T1): among the items the policy automates (confidence >= lambda),
  the share it gets wrong is <= alpha.
- **Recall** (T2): auto-rejecting items scored below t keeps >= target of the positives.

Both invert a one-sided Clopper-Pearson bound at every threshold of a grid and pick one with
Learn-then-Test fixed-sequence testing (Angelopoulos et al. 2021), or with a Bonferroni
correction over the grid (as in Geifman & El-Yaniv 2017's SGR).

Validity needs the grid to be fixed before the certification labels are seen. The grid may
depend on scores of *other* unlabeled items (``pool_thresholds``), but not on the
certification sample's own scores or labels. Each bound is exact conditional on how many
certification items fall above the threshold (or how many are positive), so it is valid
marginally too.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.stats import beta


def cp_upper(errors, n, delta: float) -> np.ndarray:
    """One-sided (1 - delta) Clopper-Pearson upper bound on an error rate: 1 where n = 0 or
    every trial is an error. ``cp_upper(e, n, delta) <= alpha`` exactly when the binomial
    p-value P(X <= e | n, alpha) is <= delta."""
    errors, n = np.asarray(errors, float), np.asarray(n, float)
    out = np.ones(np.broadcast(errors, n).shape)
    errors, n = np.broadcast_to(errors, out.shape), np.broadcast_to(n, out.shape)
    ok = (n > 0) & (errors < n)
    out[ok] = beta.ppf(1 - delta, errors[ok] + 1, n[ok] - errors[ok])
    return out


def cp_lower(successes, n, delta: float) -> np.ndarray:
    """One-sided (1 - delta) Clopper-Pearson lower bound on a success rate (0 where n = 0 or
    there are no successes)."""
    return 1.0 - cp_upper(np.asarray(n, float) - np.asarray(successes, float), n, delta)


def min_accepted(alpha: float, delta: float) -> int:
    """Fewest certification items with zero errors that certify risk <= alpha: the smallest
    n with (1 - alpha)^n <= delta (29 for alpha = 0.10, delta = 0.05)."""
    n = int(np.ceil(np.log(delta) / np.log1p(-alpha)))
    while n > 1 and (1 - alpha) ** (n - 1) <= delta:  # guard against rounding up past it
        n -= 1
    return n


def pool_thresholds(pool_conf, coverages) -> np.ndarray:
    """Thresholds under which each of ``coverages`` of the unlabeled pool has confidence >=
    threshold (approximately, with ties). The pool must be disjoint from the certification
    sample."""
    pool_conf = np.sort(np.asarray(pool_conf, float))[::-1]
    idx = np.clip(np.ceil(np.asarray(coverages, float) * len(pool_conf)).astype(int) - 1, 0, None)
    return pool_conf[idx]


def coverage_grid(
    n_cal: int, alpha: float, delta: float, step: float = 0.01, slack: float = 2.0
) -> np.ndarray:
    """Pre-specified coverages for fixed-sequence testing, from strict to loose.

    Fixed-sequence stops at the first failure, so the start matters. It is where the
    certification sample is expected to hold ``slack * min_accepted`` items. With slack 1,
    half the draws hold fewer than ``min_accepted`` there and fail at once: in simulation
    power levelled off near 50% however large the sample. Slack 2 lifted it to 87% at
    n = 1,000 and 99% at n = 3,000 (``tests/test_certify.py`` has the setup)."""
    start = min(max(slack * min_accepted(alpha, delta) / max(n_cal, 1), step), 1.0)
    grid = np.arange(np.ceil(start / step) * step, 1.0 + step / 2, step)
    return np.unique(np.clip(np.concatenate([[start], grid]), 0, 1))


@dataclass(frozen=True)
class Certificate:
    threshold: float  # automate where the score passes this; nan when nothing is certified
    index: int  # position in the grid, -1 when nothing is certified
    bounds: np.ndarray  # the bound at every grid threshold (upper risk or lower recall)
    counts: np.ndarray  # certification items the bound rests on, per threshold

    @property
    def certified(self) -> bool:
        return self.index >= 0


def _select(passed: np.ndarray, method: str) -> int:
    if method == "fixed_sequence":
        fails = np.flatnonzero(~passed)
        return (fails[0] if len(fails) else len(passed)) - 1
    if method == "bonferroni":
        hits = np.flatnonzero(passed)
        return int(hits[-1]) if len(hits) else -1
    raise ValueError(f"unknown method {method!r}")


def certify_risk(
    conf, loss, thresholds, alpha: float, delta: float = 0.05, method: str = "fixed_sequence"
) -> Certificate:
    """Automate items with confidence >= lambda, choosing the loosest lambda in ``thresholds``
    (ordered strict to loose, i.e. decreasing) whose selective risk is certified <= alpha.

    ``conf``: confidence of each certification item; ``loss``: 1 when automating that item
    would be wrong. ``fixed_sequence`` tests in grid order at level delta and stops at the first
    failure; ``bonferroni`` tests every threshold at delta / len(grid) and keeps the loosest
    that passes.
    """
    conf, loss = np.asarray(conf, float), np.asarray(loss, float)
    thresholds = np.asarray(thresholds, float)
    if np.any(np.diff(thresholds) > 0):
        raise ValueError("thresholds must run strict to loose (non-increasing)")
    order = np.argsort(-conf, kind="stable")
    cs, cum = conf[order], np.concatenate([[0.0], np.cumsum(loss[order])])
    n = np.searchsorted(-cs, -thresholds, side="right")  # items with conf >= threshold
    level = delta if method == "fixed_sequence" else delta / len(thresholds)
    bounds = cp_upper(cum[n], n, level)
    i = _select(bounds <= alpha, method)
    return Certificate(float(thresholds[i]) if i >= 0 else float("nan"), i, bounds, n)


def certify_recall(
    score,
    y,
    thresholds,
    target: float = 0.95,
    delta: float = 0.05,
    method: str = "fixed_sequence",
) -> Certificate:
    """Auto-reject items scored below t, choosing the highest t in ``thresholds`` (ordered
    from rejecting least to most, i.e. increasing) whose recall is certified >= ``target``.

    The bound rests on the positives in the certification sample: with none missed, 95%
    recall at 95% confidence needs 59 of them.
    """
    score, y = np.asarray(score, float), np.asarray(y, float)
    thresholds = np.asarray(thresholds, float)
    if np.any(np.diff(thresholds) < 0):
        raise ValueError("thresholds must run from rejecting least to most (non-decreasing)")
    pos = np.sort(score[y == 1])
    misses = np.searchsorted(pos, thresholds, side="left")  # positives scored below t
    n_pos = np.full(len(thresholds), len(pos))
    level = delta if method == "fixed_sequence" else delta / len(thresholds)
    bounds = cp_lower(n_pos - misses, n_pos, level)
    i = _select(bounds >= target, method)
    return Certificate(float(thresholds[i]) if i >= 0 else float("nan"), i, bounds, n_pos)


def risk_outcome(conf, loss, threshold: float, alpha: float) -> dict:
    """Coverage and selective risk of automating ``conf >= threshold`` on held-out items.
    Nothing certified means nothing automated, which cannot violate the target."""
    conf, loss = np.asarray(conf, float), np.asarray(loss, float)
    auto = conf >= threshold  # False everywhere when threshold is nan
    risk = float(loss[auto].mean()) if auto.any() else 0.0
    return {"coverage": float(auto.mean()), "risk": risk, "violated": bool(risk > alpha)}


def recall_outcome(score, y, threshold: float, target: float) -> dict:
    """Work saved (share auto-rejected) and recall of rejecting ``score < threshold`` on
    held-out items."""
    score, y = np.asarray(score, float), np.asarray(y, float)
    reject = score < threshold  # False everywhere when threshold is nan
    recall = float((~reject)[y == 1].mean()) if (y == 1).any() else 1.0
    return {"work_saved": float(reject.mean()), "recall": recall, "violated": bool(recall < target)}
