"""Platform-shift stress test: certify on one platform, deploy on another.

    uv run python scripts/shift_analyze.py run [--reps 500] [--workers 4]
    uv run python scripts/shift_analyze.py analyze

``run`` reads cached Gemma answers (offline) for T1's 5,000 comments, then for every
(source, target) pair, budget and resample draws B labels from the source platform's pool half,
fits the features + judge head on a share f (or uses the direct judge, f = 0), certifies on the rest
with a grid built either from the source pool's unlabeled rest (S) or from the target's unlabeled
pool half (T), and scores the certified threshold on the target's test half. Label draws are seeded
by (seed, source, B, rep): every pair with the same source, including its control, shares draws,
and both grid variants use the same fitted scores. Writes results/shift_t1/rows.parquet.
``analyze`` writes results/shift_t1/summary.{md,csv}.
"""

from __future__ import annotations

import copy
import logging
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from ldj import allocate, certify
from ldj.cache import CallCache
from ldj.methods import build_methods
from ldj.methods.base import LogisticHead
from ldj.tasks import load_task
from ldj.tasks.moderation_shift import halves

OUT = Path("results/shift_t1")
PLATFORMS = ["0", "2", "3"]
PAIRS = [
    ("0", "2"),
    ("2", "0"),
    ("0", "3"),
    ("3", "0"),
    ("2", "3"),
    ("3", "2"),
    ("0", "0"),
    ("2", "2"),
    ("3", "3"),
]
BUDGETS = [200, 400, 800]
SHARES = [0.25, 0.50]
MIN_REST = 100
POLICY = allocate.Policy("classify", alpha=0.10, delta=0.05, cut=0.5)
SEED = 0


def features() -> tuple:
    """(task, question answers X, judge scores j, failures) from the cache only."""
    logging.disable(logging.WARNING)
    cfg = yaml.safe_load(Path("configs/x4_t1_arms2.yaml").read_text())
    task = load_task(cfg["task"])
    spec = copy.deepcopy(next(m for m in cfg["methods"] if m["type"] == "questions_judge"))
    [m] = build_methods([spec], CallCache(".cache/calls.sqlite"))
    everything = np.arange(task.n)
    x, _ = m.answerer.matrix(task, everything)
    j = np.asarray(m.judge.fit(task, everything[:0]).predict(task, everything), float)
    failures = {"questions": int(np.isnan(x).any(axis=1).sum()), "judge": len(m.judge.failed)}
    return task, x, j, failures


_S: dict = {}


def _init(y, cats, z, j):
    _S.update(y=y, cats=cats, z=z, j=j)


def _certify(p, cert, grid_scores, y):
    grid = allocate._grid(POLICY, grid_scores, len(cert))
    conf, loss = POLICY.conf_loss(p[cert], y[cert])
    return certify.certify_risk(conf, loss, grid, POLICY.alpha, POLICY.delta).threshold


def run_pair(pair, reps):
    y, cats, z, j = _S["y"], _S["cats"], _S["z"], _S["j"]
    s, t = pair
    src_pool, _ = halves(cats, s, SEED)
    tgt_pool, tgt_test = halves(cats, t, SEED)
    rows = []
    for b in BUDGETS:
        if b + MIN_REST > len(src_pool):
            continue
        for r in range(reps):
            perm = np.random.default_rng([SEED, int(s), b, r]).permutation(src_pool)
            lab, rest = perm[:b], perm[b:]
            arms = [("gemma_judge_0shot", 0.0, j, lab)]
            for f in SHARES:
                n_fit = round(f * b)
                fit = lab[:n_fit]
                ok = ~np.isnan(z[fit]).any(axis=1)
                head = LogisticHead().fit(z[fit][ok], y[fit][ok])
                p = head.predict(np.where(np.isnan(z), 0.5, z))
                arms.append(("gemma_features_judge", f, p, lab[n_fit:]))
            for method, f, p, cert in arms:
                for grid_name, grid_items in (("source", rest), ("target", tgt_pool)):
                    thr = _certify(p, cert, p[grid_items], y)
                    o = allocate._outcome(POLICY, p[tgt_test], y[tgt_test], thr)
                    rows.append(
                        {
                            "source": s,
                            "target": t,
                            "method": method,
                            "f": f,
                            "B": b,
                            "rep": r,
                            "grid": grid_name,
                            "certified": bool(np.isfinite(thr)),
                            **o,
                        }
                    )
    return rows


def run(reps: int = 500, workers: int = 4) -> None:
    task, x, j, failures = features()
    print(f"cache-only features; failures: {failures}")
    z = np.column_stack([x, j])
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with ProcessPoolExecutor(
        workers, initializer=_init, initargs=(task.y, task.categories, z, j)
    ) as ex:
        for part in ex.map(run_pair, PAIRS, [reps] * len(PAIRS)):
            rows += part
    df = pd.DataFrame(rows)
    df.to_parquet(OUT / "rows.parquet")
    context = []
    for pl in PLATFORMS:
        m = task.categories == pl
        context.append(
            {
                "platform": pl,
                "comments": int(m.sum()),
                "positive": task.y[m].mean(),
                "judge_error": float(((j[m] >= 0.5) != (task.y[m] == 1)).mean()),
            }
        )
    pd.DataFrame(context).to_csv(OUT / "platforms.csv", index=False)
    (OUT / "failures.txt").write_text(str(failures) + "\n")
    print(f"{len(df)} rows -> {OUT / 'rows.parquet'}")


def analyze() -> None:
    df = pd.read_parquet(OUT / "rows.parquet")
    df["useful"] = df["certified"] & (df["automated"] > 0)
    df["auto"] = np.where(df["useful"], df["automated"], 0.0)
    g = df.groupby(["source", "target", "method", "f", "B", "grid"])
    s = g.agg(
        n=("rep", "size"),
        useful=("useful", "mean"),
        automated=("auto", "mean"),
        violations=("violated", "sum"),
    ).reset_index()
    k, n = s["violations"].to_numpy(float), s["n"].to_numpy(float)
    s["violation"] = k / n
    s["lo"] = certify.cp_lower(k, n, 0.025)
    s["hi"] = certify.cp_upper(k, n, 0.025)
    s["consistent"] = s["lo"] <= POLICY.delta
    s["shift"] = np.where(s["source"] == s["target"], "control", "shift")
    s.to_csv(OUT / "summary.csv", index=False)
    ctx = pd.read_csv(OUT / "platforms.csv")
    lines = [
        "# Platform-shift stress test (T1, exploratory)",
        "",
        "Platforms: "
        + "; ".join(
            f"{int(r.platform)}: {r.comments} comments, {r.positive:.1%} positive, direct-judge "
            f"error {r.judge_error:.1%}"
            for r in ctx.itertuples()
        ),
        "",
        f"Failures (cache-only): {(OUT / 'failures.txt').read_text().strip()}",
        "",
        "Certified cells, α = 0.10, δ = 0.05. Violation = realized target test-half risk > α.",
        "",
        (
            "| source→target | method | f | B | grid | useful | automated | violation [95% CI] | "
            "consistent |"
        ),
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in s.sort_values(["shift", "source", "target", "method", "f", "B", "grid"]).itertuples():
        lines.append(
            f"| {r.source}→{r.target} | {r.method} | {r.f:.2f} | {r.B} | {r.grid} | "
            f"{r.useful:.2f} | {r.automated:.3f} | {r.violation:.3f} [{r.lo:.3f}, {r.hi:.3f}] | "
            f"{'yes' if r.consistent else '**no**'} |"
        )
    agg = (
        s.groupby(["shift", "grid"])
        .agg(
            cells=("n", "size"),
            inconsistent=("consistent", lambda c: int((~c).sum())),
            max_violation=("violation", "max"),
            mean_auto=("automated", "mean"),
        )
        .reset_index()
    )
    lines += [
        "",
        "## Headline",
        "",
        "| setting | grid | cells | inconsistent | max violation | mean automation |",
        "|---|---|---|---|---|---|",
    ]
    for r in agg.itertuples():
        lines.append(
            f"| {r.shift} | {r.grid} | {r.cells} | {r.inconsistent} | "
            f"{r.max_violation:.3f} | {r.mean_auto:.3f} |"
        )
    (OUT / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[-(len(agg) + 4) :]))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "run":
        reps = int(sys.argv[sys.argv.index("--reps") + 1]) if "--reps" in sys.argv else 500
        workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
        run(reps, workers)
    else:
        analyze()
