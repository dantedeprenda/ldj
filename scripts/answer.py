"""Fetch (and cache) every LLM answer a config's methods need, for all items of its task.

    uv run python scripts/answer.py configs/w5_t1_fresh.yaml [--rpm 600] [--workers 32]

Turns the config's backends online, keeps the ``max_usd`` cap, answers question sets and zero-shot
judges for every item once, and reports spend and failures. Allocation runs then read the cache
offline. Keys come from .env (never printed).
"""

from __future__ import annotations

import copy
import logging
import sys
from pathlib import Path

import numpy as np
import yaml

from ldj.cache import CallCache
from ldj.cli import load_dotenv
from ldj.methods import build_methods
from ldj.tasks import load_task


def _online(spec, rpm=None):
    """Backends online; ``rpm`` overrides the self-imposed request rate (operational only: it
    does not change any request, so cache keys and answers are unaffected)."""
    if isinstance(spec, dict):
        out = {k: (False if k == "offline" else _online(v, rpm)) for k, v in spec.items()}
        if rpm and "rpm" in out:
            out["rpm"] = rpm
        return out
    if isinstance(spec, list):
        return [_online(v, rpm) for v in spec]
    return spec


def main(config: str, rpm: int | None = None, workers: int | None = None) -> int:
    load_dotenv()
    logging.basicConfig(level=logging.WARNING)
    cfg = yaml.safe_load(Path(config).read_text())
    task = load_task(cfg["task"])
    everything = np.arange(task.n)
    # questions and judges only: questions_judge reuses the same cached calls
    specs = [
        _online(copy.deepcopy(s), rpm)
        for s in cfg["methods"]
        if s["type"] in ("questions", "judge")
    ]
    methods = build_methods(
        specs, CallCache(cfg.get("cache", ".cache/calls.sqlite")), max_usd=cfg.get("max_usd")
    )
    spent = 0.0
    for m in methods:  # workers: calls in flight per method (operational; answers unchanged)
        if workers:
            if hasattr(m, "answerer"):
                m.answerer.workers = workers
            else:
                m.workers = workers
        if hasattr(m, "answerer"):
            x, _ = m.answerer.matrix(task, everything)
            failed = int(np.isnan(x).any(axis=1).sum())
            backend = m.answerer.backend
        else:
            m.fit(task, everything[:0]).predict(task, everything)
            failed = len(m.failed)
            backend = m.backend
        spent = max(spent, backend.new_spend)  # methods may share one backend
        print(
            f"{m.name}: {task.n} items, {failed} failed, backend spend so far ${backend.new_spend:.4f}",
            flush=True,
        )
    print(f"total new spend ${spent:.4f} (cap ${cfg.get('max_usd')})")
    return 0


if __name__ == "__main__":
    rpm = int(sys.argv[sys.argv.index("--rpm") + 1]) if "--rpm" in sys.argv else None
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else None
    raise SystemExit(main(sys.argv[1], rpm, workers))
