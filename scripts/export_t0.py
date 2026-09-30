"""Export the routing paper's tasks (T0) into this harness's format. Offline; no API calls.

Run from the paper repo, in its environment (it needs its data, call cache and code):

    cd ../routing-success-prediction
    uv run python ../ldj/scripts/export_t0.py ../ldj/data/t0

Writes one ``<name>.npz`` per benchmark with texts, the same train/test split, the cached
decision-model answers to the 13 frozen questions (v1), and per-item costs. The decision-model
answers stay local: raw outputs are not redistributed, and data/ is
gitignored.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, "scripts")
from extensions import Setup  # the paper's re-implementation, verified 35/35 against it

BENCH = {
    "llmrouterbench": ("configs/llmrouterbench_test.yaml", "jev"),
    "twinrouterbench": ("configs/twinrouterbench_test.yaml", "jev-4k"),
}


def main(out: str) -> int:
    out_dir = Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, (config, jev) in BENCH.items():
        s = Setup(config, jev, offline=True)
        q, c = s.ds.quality_matrix(), s.ds.cost_matrix()
        np.savez_compressed(
            out_dir / f"{name}.npz",
            ids=np.array([ex.id for ex in s.ds.examples]),
            texts=np.array(s.texts, dtype=object),
            categories=s.cats,
            domains=s.domains,
            y=(q[:, 0] >= 0.5).astype(float),
            train=s.train,
            test=s.test,
            jev=s.jev,
            cheap_cost=c[:, 0],
            strong_cost=c[:, -1],
            strong_correct=(q[:, -1] >= 0.5).astype(float),
            pool=np.array(s.ds.model_names),
        )
        print(
            f"{name}: {len(s.texts)} items, train {len(s.train)}, test {len(s.test)}, "
            f"pool {s.ds.model_names}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
