"""Split an X4 allocation run into independent units and run them in parallel.

A unit is (group, budget B, a chunk of resample ids). Every resample is seeded by
(seed, group, B, rep), so any split of the work yields exactly the rows the single-process runner
(``allocate.run``) yields; rows are returned in a canonical order. Workers build their own task and
methods once (LLM backends hold open cache connections and cannot be shared between processes).
The same ``load_for`` / ``units`` / ``run_unit`` functions serve local processes and Modal.
"""

from __future__ import annotations

import logging
import multiprocessing as mp
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Any

import numpy as np
import pandas as pd

from ldj import allocate
from ldj.cache import CallCache
from ldj.methods import build_methods
from ldj.task import Task
from ldj.tasks import load_task

_log = logging.getLogger(__name__)
ORDER = ["group", "B", "rep", "method", "arm", "f"]


def load_for(cfg: dict[str, Any]) -> tuple[Task, list[Task], list]:
    """The task (with any label swap the config asks for), its groups, and fresh methods."""
    task = load_task(cfg["task"])
    if cfg.get("train_labels") == "single_annotator":
        task = allocate.single_annotator_labels(task)
    elif cfg.get("train_labels") in ("one_vote", "majority3"):
        from ldj.labels import vote_labels

        task = vote_labels(task, cfg["train_labels"], int(cfg.get("label_seed", 0)))
    groups = (
        [task.subset(c) for c in np.unique(task.categories)] if cfg.get("per_category") else [task]
    )
    methods = build_methods(cfg["methods"], CallCache(cfg.get("cache", ".cache/calls.sqlite")))
    return task, groups, methods


def units(cfg: dict[str, Any], groups: list[Task], chunk: int = 50) -> list[tuple]:
    """(group index, B, resample ids) for every budget a group can afford."""
    reps, min_rest = int(cfg["reps"]), int(cfg.get("min_rest", 100))
    out = []
    for gi, sub in enumerate(groups):
        for b in cfg["budgets"]:
            if b + min_rest > len(sub.train):
                continue
            for start in range(0, reps, chunk):
                out.append((gi, int(b), list(range(start, min(start + chunk, reps)))))
    return out


def run_unit(groups, methods, cfg, unit, cache: dict | None = None) -> list[dict]:
    gi, b, rep_ids = unit
    return allocate.run_group(
        groups[gi],
        methods,
        allocate.Policy(**cfg["policy"]),
        budgets=[b],
        fit_shares=list(cfg["fit_shares"]),
        reps=int(cfg["reps"]),
        seed=int(cfg.get("seed", 0)),
        group=gi,
        min_rest=int(cfg.get("min_rest", 100)),
        heuristic=bool(cfg.get("heuristic", True)),
        volume=cfg.get("volume"),
        rep_ids=rep_ids,
        cache=cache,
    )


def canonical(rows: list[dict] | pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    return df.sort_values(ORDER, kind="stable").reset_index(drop=True)


_W: dict[str, Any] = {}


def _init(cfg: dict[str, Any]) -> None:
    logging.basicConfig(level=logging.WARNING)
    _, groups, methods = load_for(cfg)
    _W.update(cfg=cfg, groups=groups, methods=methods, cache={})


def _work(unit) -> list[dict]:
    return run_unit(_W["groups"], _W["methods"], _W["cfg"], unit, _W["cache"])


def run_parallel(cfg: dict[str, Any], workers: int, chunk: int = 50) -> pd.DataFrame:
    """Run all units on ``workers`` local processes; logs progress as units finish."""
    _, groups, _ = load_for(cfg)
    todo = units(cfg, groups, chunk)
    t0 = time.perf_counter()
    rows: list[dict] = []
    ctx = mp.get_context("spawn")  # a clean interpreter per worker (no forked sqlite handles)
    with ProcessPoolExecutor(workers, mp_context=ctx, initializer=_init, initargs=(cfg,)) as ex:
        futures = [ex.submit(_work, u) for u in todo]
        for i, f in enumerate(as_completed(futures), 1):
            rows += f.result()
            if i % max(1, len(todo) // 20) == 0 or i == len(todo):
                el = time.perf_counter() - t0
                _log.warning(
                    "%d/%d units, %.0fs elapsed, ~%.0fs left",
                    i,
                    len(todo),
                    el,
                    el / i * (len(todo) - i),
                )
    return canonical(rows)
