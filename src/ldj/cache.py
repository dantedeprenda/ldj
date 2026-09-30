"""SQLite cache for every external call, keyed by a hash of (backend id, request).

Re-running an experiment, sweeping thresholds or recomputing metrics never re-bills an
API. Cached rows keep the latency measured on the original call.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
from pathlib import Path
from typing import Any


class CallCache:
    def __init__(self, path: str | Path = ".cache/calls.sqlite"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._db = sqlite3.connect(self.path, check_same_thread=False, timeout=60)
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS calls (key TEXT PRIMARY KEY, backend TEXT, "
            "request TEXT, response TEXT, latency_s REAL, created TEXT DEFAULT CURRENT_TIMESTAMP)"
        )
        self._db.commit()

    @staticmethod
    def key(backend_id: str, request: Any) -> str:
        blob = json.dumps({"backend": backend_id, "request": request}, sort_keys=True)
        return hashlib.sha256(blob.encode()).hexdigest()

    def get(self, backend_id: str, request: Any) -> tuple[dict, float] | None:
        with self._lock:
            row = self._db.execute(
                "SELECT response, latency_s FROM calls WHERE key = ?",
                (self.key(backend_id, request),),
            ).fetchone()
        return (json.loads(row[0]), row[1]) if row else None

    def put(self, backend_id: str, request: Any, response: dict, latency_s: float) -> None:
        with self._lock:
            self._db.execute(
                "INSERT OR REPLACE INTO calls (key, backend, request, response, latency_s) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    self.key(backend_id, request),
                    backend_id,
                    json.dumps(request),
                    json.dumps(response),
                    latency_s,
                ),
            )
            self._db.commit()
