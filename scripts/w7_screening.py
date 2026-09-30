"""Prioritized screening with heuristic and certified stopping on T2 (results/w7_t2/).

    uv run python scripts/w7_screening.py configs/w7_t2.yaml --smoke      # 2 reviews, 2 runs
    uv run python scripts/w7_screening.py configs/w7_t2.yaml --workers 6  # full, local
    uv run modal run scripts/modal_w7.py --config configs/w7_t2.yaml      # full, on Modal

Writes results/<name>/{rows.parquet, summary.md, per_review.md}.
"""

from __future__ import annotations

import argparse
import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from ldj import screening_al as sa
from ldj.cache import CallCache
from ldj.methods import build_methods
from ldj.tasks import load_task

ARMS = ["a_judge_static", "b_features_static", "c_active", "d_active_llm"]


def load_reviews(cfg: dict[str, Any]) -> list[dict]:
    """Per review: texts, labels, cached judge probabilities and question answers (whole pool)."""
    task = load_task(cfg["task"])
    cache = CallCache(cfg.get("cache", ".cache/calls.sqlite"))
    judge, questions = build_methods([cfg["judge"], cfg["questions"]], cache)
    out = []
    for c in np.unique(task.categories):
        sub = task.subset(c)
        idx = np.arange(sub.n)
        p = judge.fit(sub, idx[:0]).predict(sub, idx)
        x, _ = questions.answerer.matrix(sub, idx)
        out.append(
            {
                "review": str(c),
                "texts": sub.texts,
                "y": sub.y.astype(int),
                "judge": np.asarray(p, float),
                "x": np.asarray(x, float),
            }
        )
    return out


def run_unit(rev: dict, run: int, cfg: dict[str, Any], tfidf=None) -> list[dict]:
    y = rev["y"]
    rng = np.random.default_rng([run, len(y), int(y.sum())])
    seeds = sa.seed_pair(y, rng)
    tf = tfidf if tfidf is not None else sa.tfidf_matrix(rev["texts"])
    orders = {
        "a_judge_static": sa.static_order(rev["judge"], seeds, rng),
        "b_features_static": sa.features_order(rev["x"], y, seeds, rng),
        "c_active": sa.active_order(tf, y, seeds, rng, batch=cfg.get("batch", 10)),
        "d_active_llm": sa.active_order(
            tf, y, seeds, rng, batch=cfg.get("batch", 10), prior=rev["judge"]
        ),
    }
    rows = []
    for arm, order in orders.items():
        yo = y[order]
        stops = {
            "heuristic_50": sa.heuristic_stop(yo),
            "certified_95": sa.certified_stop(yo, every=cfg.get("check_every", 5)),
        }
        for rule, t in stops.items():
            rows.append(
                {
                    "review": rev["review"],
                    "run": run,
                    "arm": arm,
                    "rule": rule,
                    "pool": len(y),
                    "relevant": int(y.sum()),
                    **sa.outcome(yo, t),
                }
            )
    return rows


def summarize(df: pd.DataFrame) -> tuple[str, str]:
    per = (
        df.groupby(["review", "arm", "rule"])
        .agg(
            pool=("pool", "first"),
            relevant=("relevant", "first"),
            work_saved=("work_saved", "mean"),
            recall=("recall", "mean"),
            met=("met", "mean"),
            screened=("screened", "mean"),
        )
        .reset_index()
    )
    macro = (
        per.groupby(["arm", "rule"])
        .agg(
            work_saved=("work_saved", "mean"),
            recall=("recall", "mean"),
            runs_meeting_95=("met", "mean"),
            reviews_meeting_95_in_95pct=("met", lambda m: (m >= 0.95).mean()),
            screened=("screened", "mean"),
        )
        .reset_index()
    )
    s = [
        "# W7 summary (macro over reviews; exploratory)",
        "",
        (
            "| arm | stopping | work saved | mean recall | runs with recall >= 0.95 | "
            "reviews meeting it in >= 95% of runs | screened |"
        ),
        "|---|---|---|---|---|---|---|",
    ]
    for r in macro.itertuples():
        s.append(
            f"| {r.arm} | {r.rule} | {r.work_saved:.3f} | {r.recall:.3f} | "
            f"{r.runs_meeting_95:.2f} | {r.reviews_meeting_95_in_95pct:.2f} | "
            f"{r.screened:.0f} |"
        )
    p = [
        "# W7 per review",
        "",
        "| review | pool | relevant | arm | stopping | work saved | recall | runs >= 0.95 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in per.itertuples():
        p.append(
            f"| {r.review} | {r.pool} | {r.relevant} | {r.arm} | {r.rule} | "
            f"{r.work_saved:.3f} | {r.recall:.3f} | {r.met:.2f} |"
        )
    return "\n".join(s) + "\n", "\n".join(p) + "\n"


def write(df: pd.DataFrame, cfg: dict[str, Any], out_root: str = "results") -> Path:
    dest = Path(out_root) / cfg["name"]
    dest.mkdir(parents=True, exist_ok=True)
    df.to_parquet(dest / "rows.parquet")
    s, p = summarize(df)
    (dest / "summary.md").write_text(s)
    (dest / "per_review.md").write_text(p)
    return dest


_W: dict[str, Any] = {}


def _init(cfg):
    logging.basicConfig(level=logging.WARNING)
    _W["cfg"], _W["revs"] = cfg, load_reviews(cfg)
    _W["tf"] = {}


def _work(unit):
    ri, run = unit
    rev = _W["revs"][ri]
    if ri not in _W["tf"]:
        _W["tf"][ri] = sa.tfidf_matrix(rev["texts"])
    return run_unit(rev, run, _W["cfg"], _W["tf"][ri])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--workers", type=int, default=1)
    args = ap.parse_args()
    logging.basicConfig(level=logging.WARNING)
    cfg = yaml.safe_load(Path(args.config).read_text())
    t0 = time.perf_counter()
    revs = load_reviews(cfg)
    n_rev = 2 if args.smoke else len(revs)
    runs = 2 if args.smoke else int(cfg["runs"])
    units = [(ri, r) for ri in range(n_rev) for r in range(runs)]
    rows: list[dict] = []
    if args.workers > 1:
        import multiprocessing as mp

        with ProcessPoolExecutor(
            args.workers, mp_context=mp.get_context("spawn"), initializer=_init, initargs=(cfg,)
        ) as ex:
            for f in as_completed([ex.submit(_work, u) for u in units]):
                rows += f.result()
    else:
        _W.update(cfg=cfg, revs=revs, tf={})
        for u in units:
            rows += _work(u)
    if args.smoke:
        cfg = {**cfg, "name": cfg["name"] + "_smoke"}
    dest = write(pd.DataFrame(rows), cfg)
    print(f"{len(rows)} rows, {len(units)} units in {time.perf_counter() - t0:.0f}s -> {dest}")
    print((dest / "summary.md").read_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
