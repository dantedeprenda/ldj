"""Discrimination, selective risk and the hierarchical paired bootstrap.

Ported from the routing paper (``dmroute.metrics.stats`` and ``scripts/evidence.py``) so its
numbers reproduce exactly.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import rankdata

MIN_CLASS = 10  # fewer positives or negatives than this and a per-category AUROC is noise


def auroc_rows(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Row-wise AUROC via the Mann-Whitney rank formula (ties get average ranks)."""
    ranks = rankdata(p, axis=1)
    pos = y.sum(axis=1)
    neg = y.shape[1] - pos
    with np.errstate(invalid="ignore", divide="ignore"):
        return ((ranks * y).sum(axis=1) - pos * (pos + 1) / 2) / (pos * neg)


def auroc(p: np.ndarray, y: np.ndarray) -> float:
    return float(auroc_rows(np.asarray(p, float)[None], np.asarray(y, float)[None])[0])


def stratified_draws(cats: np.ndarray, rng: np.random.Generator, b: int) -> np.ndarray:
    """B x n test positions, resampled with replacement within each category; row 0 = identity."""
    n = len(cats)
    out = np.empty((b, n), dtype=int)
    out[0] = np.arange(n)
    for c in np.unique(cats):
        members = np.flatnonzero(cats == c)
        out[1:, members] = rng.choice(members, size=(b - 1, len(members)))
    return out


def within_rows(p: np.ndarray, y: np.ndarray, cats: np.ndarray, idx: np.ndarray) -> np.ndarray:
    """Within-category AUROC (n-weighted over categories with >= MIN_CLASS of each outcome) for
    each bootstrap row of test positions ``idx`` (shape B x n). With a single category this is
    plain AUROC (when both outcomes reach MIN_CLASS)."""
    num = np.zeros(len(idx))
    den = np.zeros(len(idx))
    for c in np.unique(cats):
        cols = cats[idx] == c
        n_c = int(cols[0].sum())
        if n_c == 0:
            continue
        pos = idx[cols].reshape(len(idx), n_c)
        yy, pp = y[pos], p[pos]
        ok = (yy.sum(1) >= MIN_CLASS) & ((n_c - yy.sum(1)) >= MIN_CLASS)
        a = auroc_rows(pp, yy)
        num += np.where(ok, a * n_c, 0.0)
        den += np.where(ok, n_c, 0.0)
    with np.errstate(invalid="ignore"):
        return num / den


def seed_boot(diff: np.ndarray, seed_draws: np.ndarray) -> np.ndarray:
    """(seeds x B) paired differences -> B bootstrap means over resampled seeds (column 0 =
    point estimate)."""
    return np.nanmean(np.take_along_axis(diff, seed_draws.T, axis=0), axis=0)


def seed_draws(n_seeds: int, b: int, rng: np.random.Generator) -> np.ndarray:
    out = rng.integers(0, n_seeds, size=(b, n_seeds))
    out[0] = np.arange(n_seeds)
    return out


def ci(boot: np.ndarray) -> tuple[float, float, float]:
    """(point, 2.5%, 97.5%) from bootstrap replicates whose first entry is the point estimate."""
    lo, hi = np.nanpercentile(boot[1:], [2.5, 97.5])
    return float(boot[0]), float(lo), float(hi)


def risk_coverage(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Selective risk (share of y = 0 among accepted) after accepting the i highest-scored
    items, i = 1..n. Tied scores have no order, so each tie block gets its expected risk."""
    order = np.argsort(-p, kind="stable")
    fails = 1.0 - y[order]
    cum = np.cumsum(fails)
    ps = p[order]
    start = 0
    for i in range(1, len(ps) + 1):
        if i == len(ps) or ps[i] != ps[start]:
            if i - start > 1:
                before = cum[start - 1] if start else 0.0
                cum[start:i] = before + fails[start:i].mean() * np.arange(1, i - start + 1)
            start = i
    return cum / np.arange(1, len(y) + 1)


def aurc(p: np.ndarray, y: np.ndarray) -> float:
    """Area under the risk-coverage curve (lower is better)."""
    return float(risk_coverage(p, y).mean())


def risk_at(p: np.ndarray, y: np.ndarray, coverage: float) -> float:
    return float(risk_coverage(p, y)[max(round(coverage * len(y)) - 1, 0)])


def wss(p: np.ndarray, y: np.ndarray, recall: float = 0.95, tie_draws: int = 50) -> float:
    """Work saved over sampling at ``recall`` (Cohen et al. 2006): screening in score order,
    the share of items never screened once ``recall`` of the positives are found, minus
    (1 - recall). Tied scores are screened in random order, averaged over ``tie_draws``."""
    y = np.asarray(y, float)
    n, n_pos = len(y), y.sum()
    if n_pos == 0:
        return float("nan")
    need = np.ceil(recall * n_pos)
    rng = np.random.default_rng(0)
    out = []
    for _ in range(tie_draws):
        order = np.lexsort((rng.random(n), -np.asarray(p, float)))
        screened = int(np.argmax(np.cumsum(y[order]) >= need)) + 1
        out.append((n - screened) / n - (1 - recall))
    return float(np.mean(out))
