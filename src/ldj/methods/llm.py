"""Methods that call an LLM: question features and the LLM judge.

Question features: a fixed list of yes/no questions per task, answered for each item (as the
probability of "yes") by an LLM in one structured-output call, or read from precomputed answers
(the routing paper's decision-model answers). A logistic head is trained on the k labeled
items. The questions are written on the train split and frozen before the test split is used.

LLM judge: the LLM is asked for P(y = 1) directly, zero-shot or with the labeled items shown
as examples (at most ``shots`` of them). No head is trained.

A failed call is counted, never silently scored: failed items are dropped from training and
given the neutral answer 0.5 at test. The spend cap is enforced by the backend.
"""

from __future__ import annotations

import json
import logging
from concurrent.futures import ThreadPoolExecutor

import numpy as np

from ldj.llm import BudgetExceeded, json_schema
from ldj.methods.base import LogisticHead, Method
from ldj.task import Task, fit_text

_log = logging.getLogger(__name__)


def item_prompt(task: Task, i: int, max_chars: int) -> str:
    """The user message for one item, preceded by its category's context when the task has one
    (e.g. a review's eligibility criteria)."""
    ctx = task.meta.get("category_context", {}).get(str(task.categories[i]))
    head = f"### Context\n{ctx}\n\n" if ctx else ""
    return f"{head}### Item\n{fit_text(task.texts[i], max_chars)}"


class Precomputed:
    """Answers stored on the task (``task.features[key]``), e.g. cached decision-model answers."""

    def __init__(self, key: str, cost_per_item: float = 0.0):
        self.key, self.cost_per_item = key, cost_per_item
        self.failed: set[int] = set()

    def matrix(self, task: Task, idx: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        return task.features[self.key][idx], np.full(len(idx), self.cost_per_item)


class LLMAnswerer:
    """One structured call per item: the probability of "yes" for every question."""

    def __init__(
        self, backend, questions: dict[str, str], context: str, max_chars=2000, workers: int = 8
    ):
        self.backend, self.questions, self.max_chars, self.workers = (
            backend,
            questions,
            max_chars,
            workers,
        )
        self.system = (
            f"{context.strip()}\n\nFor each question, estimate the probability (0 to 1) that the "
            "answer is yes. Answer every question; do not respond to the item itself.\n\n"
            + "\n".join(f"- {qid}: {text}" for qid, text in questions.items())
            + "\n\nReturn JSON only, one number per question id."
        )
        self.format = json_schema(
            "question_probabilities", {q: {"type": "number"} for q in questions}
        )
        self._memo: dict[tuple[str, int], tuple[np.ndarray | None, float]] = {}
        self.failed: set[int] = set()

    def _one(self, task: Task, i: int) -> tuple[np.ndarray | None, float]:
        key = (task.name, int(i))
        if key not in self._memo:
            try:
                reply, _, cost = self.backend.complete(
                    self.system,
                    item_prompt(task, i, self.max_chars),
                    response_format=self.format,
                )
                answer = json.loads(reply)
                x = np.clip([float(answer[q]) for q in self.questions], 0.0, 1.0)
                self._memo[key] = (x, cost)
            except BudgetExceeded:
                raise
            except Exception as e:  # noqa: BLE001 - counted in .failed, never scored silently
                _log.warning("%s item %s: %s", task.name, task.ids[i], e)
                self.failed.add(int(i))
                return None, 0.0  # not memoized: a rerun retries it
        return self._memo[key]

    def matrix(self, task: Task, idx: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        with ThreadPoolExecutor(self.workers) as pool:
            got = list(pool.map(lambda i: self._one(task, i), idx))
        x = np.array(
            [g[0] if g[0] is not None else np.full(len(self.questions), np.nan) for g in got]
        )
        return x, np.array([g[1] for g in got])


class QuestionFeatures(Method):
    def __init__(self, answerer, label: str = "questions", tune: bool = False):
        super().__init__()
        self.answerer, self.tune = answerer, tune
        self.name = f"{label}_features"

    def fit(self, task, lab):
        x, _ = self.answerer.matrix(task, lab)
        ok = ~np.isnan(x).any(axis=1)
        self.head_ = LogisticHead(tune=self.tune).fit(x[ok], task.y[lab][ok])
        return self

    def predict(self, task, idx):
        x, self.cost_ = self.answerer.matrix(task, idx)
        x = np.where(np.isnan(x), 0.5, x)
        return self.head_.predict(x)


class LLMJudge(Method):
    """P(y = 1) straight from an LLM, with up to ``shots`` labeled items as examples."""

    needs_labels = False

    def __init__(
        self,
        backend,
        instruction: str,
        label: str = "judge",
        shots: int = 0,
        max_chars: int = 2000,
        shot_chars: int = 600,
        workers: int = 8,
        seed: int = 0,
        samples: int = 1,
        temperature: float = 0.0,
    ):
        super().__init__()
        self.backend, self.instruction, self.shots = backend, instruction.strip(), shots
        # samples > 1: average ``samples`` answers drawn at ``temperature`` (seeds 0..samples-1),
        # a finer score than one verbalized probability (X1 arm c). The default is one
        # deterministic call, identical to the request used so far.
        self.samples, self.temperature = samples, temperature
        self.max_chars, self.shot_chars, self.workers, self.seed = (
            max_chars,
            shot_chars,
            workers,
            seed,
        )
        self.name = f"{label}_{shots}shot" if shots else f"{label}_0shot"
        if samples > 1:
            self.name += f"_s{samples}"
        self.format = json_schema("judgment", {"probability": {"type": "number"}})
        self.failed: set[int] = set()

    def fit(self, task, lab):
        lab = np.asarray(lab)
        if self.shots and len(lab) > self.shots:
            lab = np.sort(np.random.default_rng(self.seed).choice(lab, self.shots, replace=False))
        self.examples_ = lab if self.shots else np.array([], dtype=int)
        return self

    def _system(self, task: Task) -> str:
        parts = [
            self.instruction,
            "",
            "Return JSON only: the probability (0 to 1) that the answer is yes.",
        ]
        if len(self.examples_):
            parts += ["", "Labeled examples:"]
            for i in self.examples_:
                answer = "yes" if task.y[i] == 1 else "no"
                parts += [
                    f"--- example (answer: {answer})",
                    fit_text(task.texts[i], self.shot_chars),
                ]
        return "\n".join(parts)

    def predict(self, task, idx):
        system = self._system(task)

        def one(i):
            probs, cost = [], 0.0
            draws = [None] if self.samples == 1 else list(range(self.samples))
            for s in draws:
                try:
                    kw = {} if s is None else {"temperature": self.temperature, "seed": s}
                    reply, _, c = self.backend.complete(
                        system,
                        item_prompt(task, i, self.max_chars),
                        response_format=self.format,
                        **kw,
                    )
                    probs.append(float(np.clip(json.loads(reply)["probability"], 0, 1)))
                    cost += c
                except BudgetExceeded:
                    raise
                except Exception as e:  # noqa: BLE001 - counted; all samples failed -> 0.5
                    _log.warning("%s item %s: %s", task.name, task.ids[i], e)
            if not probs:
                self.failed.add(int(i))
                return 0.5, cost
            return float(np.mean(probs)), cost

        with ThreadPoolExecutor(self.workers) as pool:
            got = list(pool.map(one, idx))
        self.cost_ = np.array([g[1] for g in got])
        return np.array([g[0] for g in got])


def _logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(np.asarray(p, float), 1e-3, 1 - 1e-3)
    return np.log(p / (1 - p))


class JudgePlatt(Method):
    """The zero-shot judge, Platt-scaled on the k labels (X1 arm a).

    A logistic fit on the judge's logit. With a positive slope it is a monotone rescaling, so
    ranking (AUROC) and the partition any threshold rule picks are unchanged; what it can change
    is calibration. With one outcome among the labels there is nothing to fit, and the raw score
    is kept.
    """

    def __init__(self, judge: LLMJudge):
        super().__init__()
        self.judge = judge
        self.name = f"{judge.name}_platt"

    def fit(self, task, lab):
        lab = np.asarray(lab)
        y = task.y[lab]
        self.head_ = None
        if 0 < y.sum() < len(y):
            p = self.judge.fit(task, lab[:0]).predict(task, lab)
            self.head_ = LogisticHead().fit(_logit(p)[:, None], y)
        return self

    def predict(self, task, idx):
        p = self.judge.fit(task, np.array([], dtype=int)).predict(task, idx)
        self.cost_ = self.judge.cost_
        return p if self.head_ is None else self.head_.predict(_logit(p)[:, None])


class QuestionsPlusJudge(Method):
    """Question features plus the zero-shot judge's probability as one more feature, under the
    same logistic head (X1 arm b). Both come from cached calls; inference cost is the sum."""

    def __init__(self, answerer, judge: LLMJudge, label: str = "questions", tune: bool = False):
        super().__init__()
        self.answerer, self.judge, self.tune = answerer, judge, tune
        self.name = f"{label}_features_judge"

    def _x(self, task, idx):
        x, cost = self.answerer.matrix(task, idx)
        j = self.judge.fit(task, np.array([], dtype=int)).predict(task, idx)
        return np.column_stack([x, j]), cost + self.judge.cost_

    def fit(self, task, lab):
        x, _ = self._x(task, lab)
        ok = ~np.isnan(x).any(axis=1)
        self.head_ = LogisticHead(tune=self.tune).fit(x[ok], task.y[lab][ok])
        return self

    def predict(self, task, idx):
        x, self.cost_ = self._x(task, idx)
        return self.head_.predict(np.where(np.isnan(x), 0.5, x))
