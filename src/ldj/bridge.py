"""E-bridge: when does sending an item to a fallback action actually help?

Predicting that the default action will fail is not the same as knowing the fallback will do
better (the routing paper's finding). Given, for the same items, whether the default action and the
fallback were each right, and what each cost, this module reports:

- the four cells: both right, only default right (escalating *breaks* it), only fallback right
  (escalating *repairs* it), both wrong (escalating cannot help);
- the escalation value, P(repair) − P(break): what escalating everything is worth;
- for any score, the outcome of escalating the top share of items at escalation rates fixed in
  advance, so no threshold is tuned on the evaluation items.

Both outcomes must be observed on every evaluated item, whether or not a policy would escalate it.
Otherwise the fallback is seen only where a policy chose it and policies cannot be compared without
bias. Neither action is assumed to be an oracle.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Paired:
    default_ok: np.ndarray  # (n,) 1 if the default action was right
    fallback_ok: np.ndarray  # (n,) 1 if the fallback was right
    default_cost: np.ndarray  # (n,) cost of the default action
    fallback_cost: (
        np.ndarray
    )  # (n,) cost of the fallback (paid instead of, not on top of, the default)

    def __post_init__(self) -> None:
        n = len(self.default_ok)
        for name in ("fallback_ok", "default_cost", "fallback_cost"):
            if len(getattr(self, name)) != n:
                raise ValueError(f"{name} has {len(getattr(self, name))} items, expected {n}")
        for name in ("default_ok", "fallback_ok"):
            if not np.isin(getattr(self, name), (0, 1)).all():
                raise ValueError(f"{name} must be 0/1")

    @property
    def n(self) -> int:
        return len(self.default_ok)

    @property
    def repair(self) -> np.ndarray:
        return (self.default_ok == 0) & (self.fallback_ok == 1)

    @property
    def breaks(self) -> np.ndarray:
        return (self.default_ok == 1) & (self.fallback_ok == 0)


def table(p: Paired) -> dict:
    """The four cells, and what escalating everything is worth."""
    both = int(((p.default_ok == 1) & (p.fallback_ok == 1)).sum())
    neither = int(((p.default_ok == 0) & (p.fallback_ok == 0)).sum())
    rep, brk = int(p.repair.sum()), int(p.breaks.sum())
    return {
        "n": p.n,
        "both_right": both,
        "only_default_right": brk,
        "only_fallback_right": rep,
        "both_wrong": neither,
        "discordant_share": (rep + brk) / p.n,
        "escalation_value": (rep - brk) / p.n,
        "default_accuracy": float(p.default_ok.mean()),
        "fallback_accuracy": float(p.fallback_ok.mean()),
        "default_cost": float(p.default_cost.mean()),
        "fallback_cost": float(p.fallback_cost.mean()),
    }


def escalate_top(score: np.ndarray, rate: float, seed: int = 0) -> np.ndarray:
    """Mask escalating the round(rate * n) highest-scored items; ties broken at random (seeded),
    so a coarse score is not credited with an arbitrary order."""
    score = np.asarray(score, float)
    m = round(rate * len(score))
    tiebreak = np.random.default_rng(seed).random(len(score))
    order = np.lexsort((tiebreak, -score))
    mask = np.zeros(len(score), bool)
    mask[order[:m]] = True
    return mask


def outcome(p: Paired, mask: np.ndarray) -> dict:
    """Result of escalating the items in ``mask`` and keeping the default elsewhere."""
    mask = np.asarray(mask, bool)
    final = np.where(mask, p.fallback_ok, p.default_ok)
    rep, brk = int((mask & p.repair).sum()), int((mask & p.breaks).sum())
    return {
        "escalated": float(mask.mean()),
        "accuracy": float(final.mean()),
        "cost": float(np.where(mask, p.fallback_cost, p.default_cost).mean()),
        "repaired": rep,
        "broken": brk,
        "net_per_item": (rep - brk) / p.n,
        # among escalated items: how often escalation helped vs hurt
        "repair_rate_escalated": rep / mask.sum() if mask.any() else float("nan"),
        "break_rate_escalated": brk / mask.sum() if mask.any() else float("nan"),
    }


def oracle_mask(p: Paired, rate: float) -> np.ndarray:
    """Best possible escalation at ``rate``: repairs first, then items where it changes nothing."""
    score = p.repair * 2.0 + (~p.breaks) * 1.0
    return escalate_top(score, rate)


def net_ci(p: Paired, masks: list[np.ndarray], b: int = 2000, seed: int = 0) -> tuple:
    """(mean, 2.5%, 97.5%) of the net repair per item, averaged over ``masks`` (e.g. one per label
    seed), with items resampled as the unit."""
    delta = np.mean(
        [np.asarray(m, bool) * (p.repair.astype(int) - p.breaks.astype(int)) for m in masks], 0
    )
    idx = np.random.default_rng(seed).integers(0, p.n, size=(b, p.n))
    boots = delta[idx].mean(axis=1)
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return float(delta.mean()), float(lo), float(hi)


def frontier(p: Paired, score: np.ndarray, seed: int = 0, w: np.ndarray | None = None) -> tuple:
    """(cost, accuracy) of escalating the top m items by ``score``, for m = 0..n, with ties
    broken at random as in ``escalate_top``. ``w`` are item weights (bootstrap counts)."""
    n = p.n
    w = np.ones(n) if w is None else np.asarray(w, float)
    tiebreak = np.random.default_rng(seed).random(n)
    order = np.lexsort((tiebreak, -np.asarray(score, float)))
    total = w.sum()
    d_acc = (w * (p.fallback_ok - p.default_ok))[order]
    d_cost = (w * (p.fallback_cost - p.default_cost))[order]
    acc = ((w * p.default_ok).sum() + np.concatenate([[0.0], np.cumsum(d_acc)])) / total
    cost = ((w * p.default_cost).sum() + np.concatenate([[0.0], np.cumsum(d_cost)])) / total
    return cost, acc


def at_cost(cost: np.ndarray, acc: np.ndarray, target: float) -> float:
    """Accuracy where the escalation path first reaches ``target`` cost, interpolated between
    the neighbouring steps; nan if escalating everything stays below the target."""
    hit = np.flatnonzero(cost >= target)
    if not len(hit):
        return float("nan")
    m = int(hit[0])
    if m == 0 or cost[m] == cost[m - 1]:
        return float(acc[m])
    t = (target - cost[m - 1]) / (cost[m] - cost[m - 1])
    return float(acc[m - 1] + t * (acc[m] - acc[m - 1]))


REQUIRED = ("default_ok", "fallback_ok", "default_cost", "fallback_cost")


def report_csv(path: str, scores: list[str], rates: list[float]) -> str:
    """Markdown report for a CSV with one row per evaluated item: ``default_ok``, ``fallback_ok``
    (0/1, both observed on every row), ``default_cost``, ``fallback_cost``, and optional score
    columns (higher = escalate first). The rows must be an evaluation sample chosen without
    looking at the scores; the report cannot check that."""
    import pandas as pd

    df = pd.read_csv(path)
    missing = [c for c in (*REQUIRED, *scores) if c not in df.columns]
    if missing:
        raise ValueError(f"{path}: missing columns {missing}")
    if df[list(REQUIRED)].isna().any().any():
        raise ValueError(f"{path}: every row needs both outcomes and both costs")
    p = Paired(*(df[c].to_numpy(float if "cost" in c else int) for c in REQUIRED))
    t = table(p)
    lines = [
        f"# Escalation report: {path}",
        "",
        (
            f"{t['n']} items. Default right {t['default_accuracy']:.3f} at {t['default_cost']:.4g} "
            f"per item; fallback right {t['fallback_accuracy']:.3f} at {t['fallback_cost']:.4g}."
        ),
        "",
        (
            "| both right | only default right (escalating breaks) | only fallback right "
            "(escalating repairs) | both wrong | escalation value |"
        ),
        "|---|---|---|---|---|",
        (
            f"| {t['both_right']} | {t['only_default_right']} | {t['only_fallback_right']} | "
            f"{t['both_wrong']} | {t['escalation_value']:+.3f} |"
        ),
        "",
        "| rate | score | accuracy | cost | repaired | broken | net | 95% CI |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for rate in rates:
        cands = [("random", np.zeros(p.n)), ("oracle", None)] + [
            (s, df[s].to_numpy(float)) for s in scores
        ]
        for name, s in cands:
            mask = oracle_mask(p, rate) if s is None else escalate_top(s, rate)
            o = outcome(p, mask)
            m, lo, hi = net_ci(p, [mask])
            lines.append(
                f"| {rate:.0%} | {name} | {o['accuracy']:.3f} | {o['cost']:.4g} | {o['repaired']} | "
                f"{o['broken']} | {m:+.4f} | [{lo:+.4f}, {hi:+.4f}] |"
            )
    lines += [
        "",
        (
            "Net = (repaired − broken) / items. The oracle is an upper bound, not a policy. A score "
            "earns its place only by beating random and the best fixed action at equal cost on new items."
        ),
    ]
    return "\n".join(lines) + "\n"
