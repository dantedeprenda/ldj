"""X4: split a label budget between fitting and certifying (exploratory on seen data).

    uv run python scripts/allocate.py configs/x4_t1.yaml [--reps N]

Offline: LLM backends in the X4 configs set ``offline: true``, so an uncached call raises
instead of billing. Writes results/<name>/:

    rows.parquet   one row per (group, method, arm, f, B, resample): tables recompute offline
    summary.csv    per (method, arm, f, B): certified share, automation, violation rate + SE
    summary.md     the same, plus the best certified arm per B and B*
"""

from __future__ import annotations

import argparse
import json
import logging
import platform
import time
from pathlib import Path

import pandas as pd
import yaml

from ldj import allocate
from ldj.cache import CallCache
from ldj.methods import build_methods
from ldj.tasks import load_task


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--reps", type=int, help="override reps (e.g. a quick pilot)")
    ap.add_argument("--out", default="results")
    ap.add_argument(
        "--resummarize", action="store_true", help="rebuild summaries from rows.parquet only"
    )
    ap.add_argument("--workers", type=int, default=1, help="local processes (1 = sequential)")
    ap.add_argument("--chunk", type=int, default=50, help="resamples per unit of work")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    cfg = yaml.safe_load(Path(args.config).read_text())
    delta = cfg["policy"].get("delta", 0.05)
    out = Path(args.out) / cfg["name"]
    if args.resummarize:
        summary = allocate.summarize(pd.read_parquet(out / "rows.parquet"), delta)
        best, bstar = allocate.b_star(summary)
        summary.to_csv(out / "summary.csv", index=False)
        (out / "summary.md").write_text(allocate.markdown(summary, best, bstar))
        print(f"re-summarized {out}; B* = {bstar}")
        return 0
    if args.reps:
        cfg["reps"] = args.reps
    t0 = time.perf_counter()
    if args.workers > 1:
        from ldj.parallel import run_parallel

        rows = run_parallel(cfg, args.workers, args.chunk)
        methods = []
    else:
        task = load_task(cfg["task"])
        if cfg.get("train_labels") == "single_annotator":
            task = allocate.single_annotator_labels(task)
        elif cfg.get("train_labels") in ("one_vote", "majority3"):
            from ldj.labels import vote_labels

            task = vote_labels(task, cfg["train_labels"], int(cfg.get("label_seed", 0)))
        methods = build_methods(cfg["methods"], CallCache(cfg.get("cache", ".cache/calls.sqlite")))
        rows = allocate.run(task, methods, cfg)
    summary = allocate.summarize(rows, delta)
    best, bstar = allocate.b_star(summary)
    out.mkdir(parents=True, exist_ok=True)
    rows.to_parquet(out / "rows.parquet")
    summary.to_csv(out / "summary.csv", index=False)
    (out / "summary.md").write_text(allocate.markdown(summary, best, bstar))
    cfg["platform"] = f"local ({platform.system()} {platform.machine()})"
    (out / "config.json").write_text(json.dumps(cfg, indent=1))
    failed = {m.name: len(getattr(getattr(m, "answerer", m), "failed", ())) for m in methods}
    print(f"{len(rows)} rows in {time.perf_counter() - t0:.0f}s; B* = {bstar}; failed {failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
