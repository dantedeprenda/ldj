"""Build methods from config entries (see configs/*.yaml)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ldj.cache import CallCache
from ldj.llm import ChatBackend, StubChat
from ldj.methods.base import BaseRate, CategoryPrior, Method
from ldj.methods.llm import (
    JudgePlatt,
    LLMAnswerer,
    LLMJudge,
    Precomputed,
    QuestionFeatures,
    QuestionsPlusJudge,
)
from ldj.methods.text import Embedding, EmbeddingStore, Tfidf


def make_backend(spec: dict[str, Any], cache: CallCache, max_usd: float | None):
    spec = dict(spec)
    kind = spec.pop("kind", "http")
    if kind == "stub":
        return StubChat()
    if kind == "typesafe":  # Jev (TypeSafe decision model)
        from ldj.jev import JevBackend

        return JevBackend(cache=cache, max_usd=max_usd, **spec)
    return ChatBackend(cache=cache, max_usd=max_usd, **spec)


def build_methods(
    specs: list[dict[str, Any]], cache: CallCache, max_usd: float | None = None
) -> list[Method]:
    out: list[Method] = []
    backends: dict[str, Any] = {}

    def backend(spec):
        key = yaml.safe_dump(spec, sort_keys=True)
        if key not in backends:
            backends[key] = make_backend(spec, cache, max_usd)
        return backends[key]

    for spec in specs:
        spec = dict(spec)
        kind = spec.pop("type")
        only_ks = spec.pop("ks", None)  # restrict this method to some label budgets
        policies = spec.pop("policies", True)  # False: skip cross-fitted cost policies
        first = len(out)
        if kind == "base_rate":
            out.append(BaseRate())
        elif kind == "category_prior":
            out.append(CategoryPrior())
        elif kind == "tfidf":
            for head in spec.get("heads", ["logreg", "knn"]):
                out.append(Tfidf(head=head))
        elif kind == "embedding":
            store = EmbeddingStore(
                model=spec["model"],
                max_chars=spec.get("max_chars", 2000),
                cache_dir=spec.get("cache_dir", ".cache/embeddings"),
                device=spec.get("device"),
            )
            for head in spec.get("heads", ["logreg", "knn"]):
                out.append(Embedding(store, spec["label"], head=head, tune=spec.get("tune", False)))
        elif kind == "questions":
            ans = spec["answerer"]
            if "precomputed" in ans:
                answerer = Precomputed(ans["precomputed"], ans.get("cost_per_item", 0.0))
            else:
                q = yaml.safe_load(Path(ans["questions"]).read_text())
                answerer = LLMAnswerer(
                    backend(ans["backend"]),
                    q["questions"],
                    q["context"],
                    max_chars=ans.get("max_chars", 2000),
                )
            out.append(QuestionFeatures(answerer, spec["label"], tune=spec.get("tune", False)))
        elif kind == "judge":
            for shots in spec.get("shots", [0]):
                out.append(
                    LLMJudge(
                        backend(spec["backend"]),
                        spec["instruction"],
                        label=spec["label"],
                        shots=shots,
                        max_chars=spec.get("max_chars", 2000),
                        samples=spec.get("samples", 1),
                        temperature=spec.get("temperature", 0.0),
                    )
                )
        elif kind in ("judge_platt", "questions_judge"):
            j = spec["judge"]
            judge = LLMJudge(
                backend(j["backend"]),
                j["instruction"],
                label=j["label"],
                max_chars=j.get("max_chars", 2000),
                samples=j.get("samples", 1),
                temperature=j.get("temperature", 0.0),
            )
            if kind == "judge_platt":
                out.append(JudgePlatt(judge))
            else:
                ans = spec["answerer"]
                q = yaml.safe_load(Path(ans["questions"]).read_text())
                answerer = LLMAnswerer(
                    backend(ans["backend"]),
                    q["questions"],
                    q["context"],
                    max_chars=ans.get("max_chars", 2000),
                )
                out.append(QuestionsPlusJudge(answerer, judge, spec["label"]))
        elif kind == "setfit":
            from ldj.methods.setfit import SetFit

            out.append(SetFit(**spec))
        else:
            raise ValueError(f"unknown method type {kind!r}")
        for m in out[first:]:
            m.only_ks = None if only_ks is None else {str(k) for k in only_ks}
            m.policies = policies
    return out
