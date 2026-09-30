"""Export every pool model's per-prompt correctness and cost for T0 (E-bridge, three actions).

Run from the paper repo, in its environment (offline; no API calls):

    cd ../routing-success-prediction
    uv run python ../ldj/scripts/export_t0_pool.py ../ldj/data/t0

Writes ``<name>_pool.npz`` next to the main export, with ids, the pool's model names, a 0/1
correctness matrix (items x models) and a cost matrix, from the same code path as
``export_t0.py``. The main export is left untouched.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, "scripts")
from extensions import Setup  # the paper's re-implementation, verified 35/35 against it

BENCH = {"llmrouterbench": ("configs/llmrouterbench_test.yaml", "jev")}


def main(out: str) -> int:
    out_dir = Path(out)
    for name, (config, jev) in BENCH.items():
        s = Setup(config, jev, offline=True)
        q, c = s.ds.quality_matrix(), s.ds.cost_matrix()
        np.savez_compressed(
            out_dir / f"{name}_pool.npz",
            ids=np.array([ex.id for ex in s.ds.examples]),
            pool=np.array(s.ds.model_names),
            correct=(q >= 0.5).astype(np.int8),
            cost=c,
        )
        print(f"{name}: {q.shape[0]} items, pool {s.ds.model_names}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
