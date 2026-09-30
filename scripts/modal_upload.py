"""Upload the data and caches Modal jobs need to the private volume "ldj-data".

    uv run python scripts/modal_upload.py [--t0] [ITEM ...]   # e.g. .cache/calls.sqlite only

Uploads T1 and T2 inputs, the LLM call cache and the embedding cache (~0.8 GB). The volume is
private to the Modal account; nothing is published. T0 (raw Jev answers, kept private) is included with --t0, with its embeddings from the
routing repo's cache via the .cache/embeddings_t0 link.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

VOLUME = "ldj-data"
ITEMS = [
    "data/t1/measuring-hate-speech.parquet",
    "data/t2/synergy",
    ".cache/calls.sqlite",
    ".cache/embeddings",
]
T0_ITEMS = [
    "data/t0/llmrouterbench.npz",
    "data/t0/llmrouterbench_pool.npz",
    ".cache/embeddings_t0",
]  # a link to the routing repo's embedding cache


def snapshot(src: str) -> str:
    """A consistent copy of a SQLite file via its backup API. Copying the live file while fetch
    processes write to it gave Modal an incomplete cache (2026-09-30: W5 found answers missing)."""
    import sqlite3
    import tempfile

    dst = Path(tempfile.mkdtemp()) / Path(src).name
    with sqlite3.connect(f"file:{src}?mode=ro", uri=True) as a, sqlite3.connect(dst) as b:
        a.backup(b)
    return str(dst)


def main() -> int:
    items = ITEMS + (T0_ITEMS if "--t0" in sys.argv else [])
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    if only:
        items = [i for i in items if i in only]
    subprocess.run(["modal", "volume", "create", VOLUME], check=False, capture_output=True)
    for item in items:
        if not Path(item).exists():
            print(f"missing locally, skipped: {item}")
            continue
        src = snapshot(item) if item.endswith(".sqlite") else item
        print(f"uploading {item} ...", flush=True)
        subprocess.run(["modal", "volume", "put", "--force", VOLUME, src, item], check=True)
    subprocess.run(["modal", "volume", "ls", VOLUME, "data"], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
