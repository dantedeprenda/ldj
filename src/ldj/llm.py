"""OpenAI-compatible chat backend (OpenRouter by default), cached, rate-limited, priced.

Ported from the routing paper. Every request is cached before it is scored, and a failed call
is never cached, so a rerun retries it instead of scoring an error.
"""

from __future__ import annotations

import json
import logging
import os
import threading
import time
from typing import Any

import httpx

from ldj.cache import CallCache

_log = logging.getLogger(__name__)


class ChatBackend:
    def __init__(
        self,
        model: str,
        base_url: str = "https://openrouter.ai/api/v1",
        api_key_env: str = "OPENROUTER_API_KEY",
        price_in: float = 0.0,  # USD per 1M prompt tokens
        price_out: float = 0.0,  # USD per 1M completion tokens
        timeout_s: float = 60.0,
        max_retries: int = 8,
        rpm: float | None = None,
        cache: CallCache | None = None,
        offline: bool = False,
        max_usd: float | None = None,
    ):
        self.model, self.base_url, self.api_key_env = model, base_url.rstrip("/"), api_key_env
        self.price_in, self.price_out, self.max_retries = price_in, price_out, max_retries
        self.cache = cache or CallCache()
        self.offline = offline  # True: only cached replies; an uncached request raises
        self.max_usd = max_usd  # hard cap on new spend in this process
        self._client = httpx.Client(timeout=timeout_s)
        self._interval = 60.0 / rpm if rpm else 0.0
        self._next_slot = 0.0
        self._slot_lock = threading.Lock()
        self.new_spend = 0.0

    @property
    def backend_id(self) -> str:
        return f"chat:{self.model}"

    def complete(
        self,
        system: str,
        user: str,
        response_format: dict | None = None,
        temperature: float = 0.0,
        seed: int | None = None,
    ) -> tuple[str, float, float]:
        """Return (text, latency_s, cost_usd). The cost is the call's price from its token usage,
        cached or not, so a method's inference cost does not depend on the cache; ``new_spend``
        counts only money actually spent in this process. ``temperature`` and ``seed`` (for
        repeated samples) enter the request, and so the cache key, only when set: the default
        request is unchanged, so existing cache entries still match."""
        request: dict[str, Any] = {
            "model": self.model,
            "temperature": temperature if temperature else 0,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        }
        if seed is not None:
            request["seed"] = seed
        if response_format is not None:
            request["response_format"] = response_format
        cached = self.cache.get(self.backend_id, request)
        if cached is not None:
            response, latency = cached
        elif self.offline:
            raise RuntimeError(f"{self.model}: not cached and backend is offline")
        elif self.max_usd is not None and self.new_spend >= self.max_usd:
            raise BudgetExceeded(f"{self.model}: spent ${self.new_spend:.2f} of ${self.max_usd}")
        else:
            response, latency = self._post(request)
            self.cache.put(self.backend_id, request, response, latency)
        usage = response.get("usage", {})
        cost = (
            usage.get("prompt_tokens", 0) * self.price_in
            + usage.get("completion_tokens", 0) * self.price_out
        ) / 1e6
        if cached is None:
            with self._slot_lock:
                self.new_spend += cost
        return response["choices"][0]["message"]["content"], latency, cost

    def _wait_turn(self) -> None:
        if not self._interval:
            return
        with self._slot_lock:
            now = time.monotonic()
            start = max(now, self._next_slot)
            self._next_slot = start + self._interval
        time.sleep(start - now)

    def _post(self, request: dict) -> tuple[dict, float]:
        key = os.environ.get(self.api_key_env)
        if not key:
            raise RuntimeError(f"{self.api_key_env} is not set")
        headers = {"Authorization": f"Bearer {key}"}
        for attempt in range(self.max_retries + 1):
            self._wait_turn()
            start = time.perf_counter()
            resp = self._client.post(
                f"{self.base_url}/chat/completions", json=request, headers=headers
            )
            latency = time.perf_counter() - start
            if (resp.status_code == 429 or resp.status_code >= 500) and attempt < self.max_retries:
                wait = max(_retry_after(resp), min(2**attempt, 60))
                _log.warning(
                    "%s: HTTP %s, retry %d in %.0fs",
                    self.model,
                    resp.status_code,
                    attempt + 1,
                    wait,
                )
                time.sleep(wait)
                continue
            resp.raise_for_status()
            body = resp.json()
            if "choices" not in body:  # OpenRouter can return 200 with an error body
                raise RuntimeError(f"{self.model}: no choices in reply: {str(body)[:200]}")
            return body, latency
        raise RuntimeError("unreachable")


class BudgetExceeded(RuntimeError):
    pass


def _retry_after(resp: httpx.Response) -> float:
    try:
        return max(float(resp.headers.get("retry-after", 0)), 0.0)
    except ValueError:
        return 0.0


class StubChat:
    """Deterministic fake for tests: every probability asked for is 0.9 if the text contains
    the word 'positive', else 0.1. Never touches the network."""

    backend_id = "chat:stub"

    def __init__(self, **_: Any):
        self.calls = 0
        self.new_spend = 0.0

    def complete(self, system: str, user: str, response_format: dict | None = None):
        self.calls += 1
        p = 0.9 if "positive" in user.split("### Item")[-1].lower() else 0.1
        keys = (
            list(response_format["json_schema"]["schema"]["properties"]) if response_format else []
        )
        return json.dumps({k: p for k in keys}), 0.0, 0.0


def json_schema(name: str, properties: dict[str, dict]) -> dict:
    """OpenAI-style strict structured-output format."""
    return {
        "type": "json_schema",
        "json_schema": {
            "name": name,
            "strict": True,
            "schema": {
                "type": "object",
                "properties": properties,
                "required": list(properties),
                "additionalProperties": False,
            },
        },
    }
