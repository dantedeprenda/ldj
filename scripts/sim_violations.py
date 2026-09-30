"""Known-truth simulations of the anomalous violation rates (results/sim_violations/).

    uv run python scripts/sim_violations.py [--quick]

Synthetic populations with known risk curves, through the real certification code path
(ldj.allocate.certified_threshold -> ldj.certify). Factors: fixed vs fresh pool, violations judged
on the true risk vs a fixed / fresh finite test set, and a pool-size control. Writes
results/sim_violations/{summary.csv,summary.md,per_pool.csv}.
"""

from __future__ import annotations

import sys
import zlib
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from ldj import certify
from ldj.allocate import Policy, certified_threshold

DELTA = 0.05


@dataclass(frozen=True)
class Case:
    name: str
    c: float  # g(s) = c (1 - s)^k
    k: int
    alpha: float
    pool: int
    n_cert: int
    n_fit: int  # labels spent fitting (removed from the pool, unused here)
    test: int
    ties: int = 0  # > 0: scores rounded to this many levels (tied scores, as coarse routers give)

    def g(self, s):
        return self.c * (1 - s) ** self.k

    def scores(self, s):
        return np.floor(s * self.ties) / self.ties if self.ties else s

    def true_risk(self, lam: float) -> float:
        # E[g(s) | s >= lam] for s ~ U(0, 1): c (1 - lam)^k / (k + 1)
        if not np.isfinite(lam):
            return 0.0
        lam = min(max(lam, 0.0), 1.0)
        if self.ties:  # rounded score >= lam  <=>  s >= ceil(lam * ties) / ties
            lam = np.ceil(lam * self.ties - 1e-12) / self.ties
        return self.c * (1 - lam) ** self.k / (self.k + 1)


CASES = [
    Case("a_twinrouter", 0.87, 2, 0.145, 500, 300, 100, 470),
    Case("a_twinrouter_ties10", 0.87, 2, 0.145, 500, 300, 100, 470, ties=10),
    Case("a_twinrouter_pool5000", 0.87, 2, 0.145, 5000, 300, 100, 470),
    Case("b_w5_b800", 0.533, 2, 0.10, 3000, 400, 400, 2000),
    Case("c_t1_alpha021", 0.545, 1, 0.21, 3000, 720, 80, 2000),
]


def draw(case: Case, n: int, rng) -> tuple[np.ndarray, np.ndarray]:
    s = rng.random(n)
    wrong = rng.random(n) < case.g(s)
    # accept policy: y = 1 when the cheap action is right; the policy sees the (maybe tied) score
    return case.scores(s), (~wrong).astype(float)


def case_cov(case: Case, t: float) -> float:
    """1 - true coverage of automating score >= t (tie-aware)."""
    lam = min(max(t, 0.0), 1.0)
    if case.ties:
        lam = np.ceil(lam * case.ties - 1e-12) / case.ties
    return lam


def one(case: Case, pol: Policy, pool_s, pool_y, rng, test_fixed, big_test: bool):
    """One resample: permute the pool, take fit + cert, grid from the rest, certify, judge."""
    perm = rng.permutation(len(pool_s))
    b = case.n_fit + case.n_cert
    cert, rest = perm[case.n_fit : b], perm[b:]
    t = certified_threshold(pol, pool_s[rest], pool_s[cert], pool_y[cert])
    certified = bool(np.isfinite(t))
    out = {"certified": certified, "true_viol": certified and case.true_risk(t) > case.alpha}
    for label, (ts, ty) in (("fixed_test", test_fixed), ("fresh_test", draw(case, case.test, rng))):
        auto = ts >= t if certified else np.zeros(len(ts), bool)
        risk = (1 - ty[auto]).mean() if auto.any() else 0.0
        out[f"{label}_viol"] = bool(auto.any() and risk > case.alpha)
    out["coverage_true"] = (1 - case_cov(case, t)) if certified else 0.0
    return out


def rate(k: int, n: int) -> tuple[float, float, float]:
    return k / n, float(certify.cp_lower(k, n, 0.025)), float(certify.cp_upper(k, n, 0.025))


def run(quick: bool) -> None:
    fresh_reps = 800 if quick else 20000
    n_pools, per_pool = (10, 60) if quick else (400, 50)
    rows, per_pool_rows = [], []
    for case in CASES:
        pol = Policy("accept", alpha=case.alpha, delta=DELTA)
        rng = np.random.default_rng(zlib.crc32(case.name.encode()))
        # fresh pool per resample
        res = []
        for _ in range(fresh_reps):
            ps, py = draw(case, case.pool, rng)
            res.append(one(case, pol, ps, py, rng, draw(case, case.test, rng), False))
        f = pd.DataFrame(res)
        for judge in ("true", "fixed_test", "fresh_test"):
            k = int(f[f"{judge}_viol"].sum())
            rows.append(
                {
                    "case": case.name,
                    "pool": "fresh",
                    "judged_on": judge,
                    "n": len(f),
                    "viol": k,
                    "useful": f.certified.mean(),
                    "coverage": f.coverage_true.mean(),
                }
            )
        # fixed pool (X4-like): many pool realizations, each with its own fixed test set
        allf = []
        for p in range(n_pools):
            ps, py = draw(case, case.pool, rng)
            test_fixed = draw(case, case.test, rng)
            r = pd.DataFrame(
                [one(case, pol, ps, py, rng, test_fixed, False) for _ in range(per_pool)]
            )
            r["pool_id"] = p
            allf.append(r)
            per_pool_rows.append(
                {
                    "case": case.name,
                    "pool_id": p,
                    "true_viol_rate": r.true_viol.mean(),
                    "fixed_test_viol_rate": r.fixed_test_viol.mean(),
                }
            )
        a = pd.concat(allf)
        for judge in ("true", "fixed_test", "fresh_test"):
            k = int(a[f"{judge}_viol"].sum())
            rows.append(
                {
                    "case": case.name,
                    "pool": f"fixed ({n_pools}x{per_pool})",
                    "judged_on": judge,
                    "n": len(a),
                    "viol": k,
                    "useful": a.certified.mean(),
                    "coverage": a.coverage_true.mean(),
                }
            )
        print(f"done {case.name}", flush=True)
    out = Path("results/sim_violations")
    out.mkdir(parents=True, exist_ok=True)
    t = pd.DataFrame(rows)
    t[["rate", "lo", "hi"]] = [rate(int(v), int(n)) for v, n in zip(t.viol, t.n)]
    t.to_csv(out / "summary.csv", index=False)
    pp = pd.DataFrame(per_pool_rows)
    pp.to_csv(out / "per_pool.csv", index=False)
    lines = [
        "| case | pool | judged on | n | violation [95% CI] | useful | mean true coverage |",
        "|---|---|---|---|---|---|---|",
    ]
    for _, r in t.iterrows():
        lines.append(
            f"| {r.case} | {r['pool']} | {r.judged_on} | {r.n} | "
            f"{r.rate:.3f} [{r.lo:.3f}, {r.hi:.3f}] | {r.useful:.2f} | {r.coverage:.3f} |"
        )
    lines += ["", "Per-pool violation rates (fixed pool; share of pools above 5%, range):", ""]
    for case, g in pp.groupby("case"):
        for col in ("true_viol_rate", "fixed_test_viol_rate"):
            v = g[col].to_numpy()
            lines.append(
                f"- {case}, {col}: mean {v.mean():.3f}, pools above 0.05: "
                f"{(v > 0.05).mean():.0%}, range {v.min():.3f}–{v.max():.3f}"
            )
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    run("--quick" in sys.argv)
