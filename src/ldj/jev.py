"""Jev (TypeSafe's decision model) as an ldj backend.

Jev answers typed questions about a state: ``POST {base_url}/v1/systemone`` with
``{state, model, questions: {qid: {type: "noul", instructions}}}`` returns
``{model, answers: {qid: {type: "noul", noul: P(yes)}}, usage: {input_tokens}}`` (the routing
paper's client, ``dmroute.backends.systemone``). Price: $0.042 per million input tokens.

``JevBackend.complete`` speaks the same interface as ``ldj.llm.ChatBackend``, so the existing
question answerer (``LLMAnswerer``), judge (``LLMJudge``) and features + judge methods run on
Jev unchanged: it reads the question ids and texts from the prompt ldj builds and the structured-
output schema, asks Jev one noul question per id (the whole question set in one call), and returns
the JSON reply those methods parse. The state is the item text (without ldj's "### Item" header).

Calls are cached like ChatBackend (key = backend id + Jev request; failed calls are never
cached), with a spend cap, an rpm throttle and an offline mode. Returned model versions are
recorded. The API key is read from TYPESAFE_API_KEY (this repo's .env, else the routing repo's)
and is never printed.
"""

from __future__ import annotations

import json
import os
import re
import threading
import time
from pathlib import Path
from typing import Any

import httpx

from ldj.cache import CallCache
from ldj.llm import BudgetExceeded

KEY_ENV = "TYPESAFE_API_KEY"
_QLINE = re.compile(r"^- (\w+): (.+)$", re.MULTILINE)


def load_key(env: str = KEY_ENV) -> str | None:
    """The API key from the environment, this repo's .env, or ../routing-success-prediction/.env."""
    if os.environ.get(env):
        return os.environ[env]
    for f in (Path(".env"), Path("../routing-success-prediction/.env")):
        if f.exists():
            for line in f.read_text().splitlines():
                if line.strip().startswith(f"{env}="):
                    value = line.split("=", 1)[1].strip().strip("\"'")
                    if value:
                        os.environ[env] = value
                        return value
    return None


def item_state(user: str) -> str:
    """The item text from ldj's user message (drops the '### Item' header and any context)."""
    return user.split("### Item\n", 1)[1] if "### Item\n" in user else user


def jev_questions(system: str, response_format: dict | None) -> tuple[dict, str]:
    """(Jev question map, reply kind) recovered from an ldj prompt and its output schema."""
    schema = (response_format or {}).get("json_schema", {})
    name = schema.get("name")
    props = list(schema.get("schema", {}).get("properties", {}))
    if name == "judgment":
        instruction = system.split("\n\nReturn JSON only", 1)[0].strip()
        return {"decision": {"type": "noul", "instructions": instruction}}, "judgment"
    if name == "question_probabilities":
        texts = dict(_QLINE.findall(system))
        missing = [q for q in props if q not in texts]
        if missing:
            raise ValueError(f"question text not found in prompt for {missing}")
        return {q: {"type": "noul", "instructions": texts[q]} for q in props}, "questions"
    raise ValueError(f"unsupported response format {name!r}")


class JevBackend:
    def __init__(
        self,
        model: str = "jev-1.13.0",
        base_url: str = "https://api.typesafe.ai",
        price_per_m_input: float = 0.042,
        timeout_s: float = 30.0,
        max_retries: int = 4,
        rpm: float | None = None,
        cache: CallCache | None = None,
        offline: bool = False,
        max_usd: float | None = None,
        name: str = "jev",
    ):
        self.model, self.base_url, self.name = model, base_url.rstrip("/"), name
        self.price_per_m_input, self.max_retries = price_per_m_input, max_retries
        self.cache = cache or CallCache()
        self.offline, self.max_usd = offline, max_usd
        self._client = httpx.Client(timeout=timeout_s)
        self._interval = 60.0 / rpm if rpm else 0.0
        self._next = 0.0
        self._lock = threading.Lock()
        self.new_spend = 0.0
        self.models_seen: set[str] = set()

    @property
    def backend_id(self) -> str:
        return f"systemone:{self.name}:{self.model}"

    def request(self, state: str, questions: dict) -> dict:
        return {"state": state, "model": self.model, "questions": questions}

    def ask(self, state: str, questions: dict, use_cache: bool = True) -> tuple[dict, float, float]:
        """(response, latency_s, cost_usd); ``use_cache=False`` always calls the API and does
        not store the reply (for repeat-call variance)."""
        req = self.request(state, questions)
        cached = self.cache.get(self.backend_id, req) if use_cache else None
        if cached is not None:
            response, latency = cached
            fresh = False
        elif self.offline:
            raise RuntimeError(f"{self.model}: not cached and backend is offline")
        elif self.max_usd is not None and self.new_spend >= self.max_usd:
            raise BudgetExceeded(f"{self.model}: spent ${self.new_spend:.2f} of ${self.max_usd}")
        else:
            response, latency = self._post(req)
            if use_cache:
                self.cache.put(self.backend_id, req, response, latency)
            fresh = True
        cost = response.get("usage", {}).get("input_tokens", 0) * self.price_per_m_input / 1e6
        with self._lock:
            if fresh:
                self.new_spend += cost
            if response.get("model"):
                self.models_seen.add(str(response["model"]))
        return response, latency, cost

    def complete(self, system: str, user: str, response_format: dict | None = None, **_: Any):
        """ChatBackend-compatible call: returns (json_text, latency_s, cost_usd)."""
        questions, kind = jev_questions(system, response_format)
        response, latency, cost = self.ask(item_state(user), questions)
        answers = response["answers"]
        p = {q: float(answers[q]["noul"]) for q in questions}
        text = json.dumps({"probability": p["decision"]} if kind == "judgment" else p)
        return text, latency, cost

    def _wait_turn(self) -> None:
        if not self._interval:
            return
        with self._lock:
            now = time.monotonic()
            slot = max(self._next, now)
            self._next = slot + self._interval
        if slot > now:
            time.sleep(slot - now)

    def _post(self, req: dict) -> tuple[dict, float]:
        key = load_key()
        if not key:
            raise RuntimeError(f"{KEY_ENV} is not set")
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
        url = f"{self.base_url}/v1/systemone"
        for attempt in range(self.max_retries + 1):
            self._wait_turn()
            start = time.perf_counter()
            resp = self._client.post(url, json=req, headers=headers)
            latency = time.perf_counter() - start
            if (resp.status_code in (429, 529) or resp.status_code >= 500) and (
                attempt < self.max_retries
            ):
                time.sleep(2**attempt)
                continue
            resp.raise_for_status()
            return resp.json(), latency
        raise RuntimeError("unreachable")
