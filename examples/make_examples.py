"""SYNTHETIC example: exception / discrepancy triage, run end to end through split -> audit -> bridge.

    uv run python examples/make_examples.py

Nothing here is real warehouse data. It shows the shape of the files a pilot would produce:

1. ``examples/out/events.csv``: one row per exception (time, order id, the model's confidence that
   auto-resolving it is right). The true outcomes are hidden until the cohort is "labeled".
2. ``ldj split``: earlier weeks = dev, later weeks = eval; a random 20% of eval ORDERS is the
   cohort, and ``--one-per-group`` picks one random exception per cohort order as the audit item
   (exceptions of one order are correlated; the audit assumes independent items).
3. "Labeling" the audit items: for those rows only, both actions' outcomes are recorded (was the
   auto-resolution right; was the senior operator's resolution right) with their handling costs.
4. ``ldj audit``: may we auto-resolve, and for what share, with error <= 0.10 (95% confidence)?
5. ``ldj bridge``: where does sending an exception to the senior operator repair vs break things?
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(os.path.relpath(Path(__file__).parent / "out"))  # relative: no home paths in reports
BANNER = "SYNTHETIC DATA - illustration of the file formats only; no real warehouse."


def make_events(n_orders: int = 1500, seed: int = 0) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    rows = []
    for o in range(n_orders):
        start = pd.Timestamp("2026-01-05") + pd.Timedelta(hours=int(rng.integers(0, 16 * 7 * 24)))
        for _ in range(int(rng.integers(1, 4))):
            difficulty = rng.random()
            rows.append(
                {
                    "exception_id": f"e{len(rows)}",
                    "order_id": f"ord{o}",
                    "created_at": (
                        start + pd.Timedelta(hours=int(rng.integers(0, 48)))
                    ).isoformat(),
                    "score": float(np.clip(1 - difficulty + rng.normal(0, 0.15), 0, 1)),
                    # hidden truth
                    "default_ok": int(rng.random() < 0.97 - 0.55 * difficulty),
                    "fallback_ok": int(rng.random() < 0.97 - 0.20 * difficulty),
                }
            )
    df = pd.DataFrame(rows)
    df["default_cost"] = 0.50  # auto-resolution: ~1 min of a clerk confirming, USD
    df["fallback_cost"] = 4.00  # senior operator: ~8 min, USD
    truth = df[["exception_id", "default_ok", "fallback_ok", "default_cost", "fallback_cost"]]
    events = df[["exception_id", "order_id", "created_at", "score"]]
    return events, truth


def ldj(*args: str) -> None:
    subprocess.run([sys.executable, "-m", "ldj.cli", *args], check=True)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "README.txt").write_text(BANNER + "\n")
    events, truth = make_events()
    events.to_csv(OUT / "events.csv", index=False)
    ldj(
        "split",
        str(OUT / "events.csv"),
        "--time",
        "created_at",
        "--group",
        "order_id",
        "--dev-share",
        "0.6",
        "--cohort-share",
        "0.2",
        "--one-per-group",
        "--seed",
        "0",
        "--out",
        str(OUT / "split.csv"),
    )
    sp = pd.read_csv(OUT / "split.csv").merge(truth, on="exception_id")
    ev = sp[sp["period"] == "eval"].copy()
    # "label" the audit items only (one per cohort order): was auto-resolution right?
    ev["label"] = np.where(ev["audit_item"] == 1, ev["default_ok"], np.nan)
    ev["role"] = ev["audit_role"]
    ev[["exception_id", "score", "role", "label"]].to_csv(OUT / "audit_input.csv", index=False)
    ldj(
        "audit",
        str(OUT / "audit_input.csv"),
        "--kind",
        "accept",
        "--alpha",
        "0.10",
        "--md",
        str(OUT / "audit.md"),
        "--html",
        str(OUT / "audit.html"),
        "--json",
        str(OUT / "audit.json"),
    )
    co = ev[ev["audit_item"] == 1].copy()  # independent items: one per sampled order
    co["risk"] = 1 - co["score"]  # escalate the exceptions the model is least sure about
    co[
        ["exception_id", "default_ok", "fallback_ok", "default_cost", "fallback_cost", "risk"]
    ].to_csv(OUT / "bridge_input.csv", index=False)
    ldj(
        "bridge",
        str(OUT / "bridge_input.csv"),
        "--score",
        "risk",
        "--md",
        str(OUT / "bridge.md"),
        "--html",
        str(OUT / "bridge.html"),
    )
    print(BANNER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
