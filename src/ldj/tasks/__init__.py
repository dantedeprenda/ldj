"""Task loaders by name: ``load_task({"name": "t0", "benchmark": "llmrouterbench"})``."""

from __future__ import annotations

from typing import Any

from ldj.task import Task


def load_task(spec: dict[str, Any]) -> Task:
    spec = dict(spec)
    name = spec.pop("name")
    if name == "t0":
        from ldj.tasks import routing

        return routing.load(spec.pop("benchmark", "llmrouterbench"), **spec)
    if name == "t1":
        from ldj.tasks import moderation

        return moderation.load(**spec)
    if name == "t1_fresh":
        from ldj.tasks import moderation_fresh

        return moderation_fresh.load(**spec)
    if name == "t1_shift":
        from ldj.tasks import moderation_shift

        return moderation_shift.load(**spec)
    if name == "t2":
        from ldj.tasks import screening

        return screening.load(**spec)
    if name == "synthetic":
        from ldj.tasks import synthetic

        return synthetic.load(**spec)
    raise ValueError(f"unknown task {name!r}")
