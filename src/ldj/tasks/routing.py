"""T0: is the cheap LLM's answer good enough? (the routing paper's tasks)

Built from ``scripts/export_t0.py``. Acting = serving the cheap model's answer (its cost is
``auto_cost``); deferring = asking the strongest pool model instead (its cost, and it may also be
wrong). A predicted failure cannot be "acted on" alone, so ``auto_negative`` is False. One label
= running the cheap model on a prompt and grading it (mean cheap-model cost).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ldj.task import Task


def load(name: str = "llmrouterbench", root: str = "data/t0") -> Task:
    d = np.load(Path(root) / f"{name}.npz", allow_pickle=True)
    return Task(
        name=f"t0_{name}",
        ids=d["ids"].tolist(),
        texts=d["texts"].tolist(),
        y=d["y"],
        categories=d["categories"],
        train=d["train"],
        test=d["test"],
        review_cost=d["strong_cost"],
        human_correct=d["strong_correct"],
        auto_cost=d["cheap_cost"],
        label_cost=float(d["cheap_cost"].mean()),
        auto_negative=False,
        features={"jev": d["jev"]},
        meta={"pool": d["pool"].tolist(), "domains": d["domains"].tolist()},
    )
