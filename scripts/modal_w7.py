"""Run W7 (scripts/w7_screening.py) on Modal: one unit per (review, run).

    uv run modal run scripts/modal_w7.py --config configs/w7_t2.yaml [--runs 30]

Same image/volume pattern as scripts/modal_app.py (private volume "ldj-data" with data/t2 and the
call cache; LLM backends offline). Results land in results/<name>/ locally.
"""

import json
import os
import shutil
import sys
from pathlib import Path

import modal

VOL = modal.Volume.from_name("ldj-data")
ROOT = "/vol"
APP = modal.App("ldj-w7")
image = (
    modal.Image.debian_slim(python_version="3.13")
    .uv_sync(frozen=True)
    .add_local_python_source("ldj")
    .add_local_dir("configs", "/app/configs")
    .add_local_file("scripts/w7_screening.py", "/app/w7_screening.py")
)


def _setup(cfg: dict) -> dict:
    for name in ("data", ".cache"):
        link = Path("/app") / name
        if not link.exists():
            link.symlink_to(Path(ROOT) / name)
    os.chdir("/app")
    sys.path.insert(0, "/app")
    dst = Path("/tmp/calls.sqlite")
    if not dst.exists():
        shutil.copy(Path(ROOT) / ".cache/calls.sqlite", dst)
    return {**cfg, "cache": str(dst)}


@APP.function(image=image, volumes={ROOT: VOL}, cpu=1.0, timeout=900)
def sizes(cfg_json: str) -> int:
    cfg = _setup(json.loads(cfg_json))
    import w7_screening

    return len(w7_screening.load_reviews(cfg))


@APP.cls(image=image, volumes={ROOT: VOL}, cpu=1.0, timeout=3600, max_containers=100)
class W7:
    cfg_json: str = modal.parameter()

    @modal.enter()
    def load(self) -> None:
        self.cfg = _setup(json.loads(self.cfg_json))
        import w7_screening

        self.mod = w7_screening
        self.revs = w7_screening.load_reviews(self.cfg)
        self.tf: dict = {}

    @modal.method()
    def run(self, unit) -> list[dict]:
        from ldj import screening_al as sa

        ri, run = unit
        if ri not in self.tf:
            self.tf[ri] = sa.tfidf_matrix(self.revs[ri]["texts"])
        return self.mod.run_unit(self.revs[ri], run, self.cfg, self.tf[ri])


@APP.local_entrypoint()
def main(config: str, runs: int = 0) -> None:
    import time

    import pandas as pd
    import yaml

    sys.path.insert(0, "scripts")
    import w7_screening

    cfg = yaml.safe_load(Path(config).read_text())
    if runs:
        cfg["runs"] = runs
    cfg_json = json.dumps(cfg)
    t0 = time.perf_counter()
    n_rev = sizes.remote(cfg_json)
    units = [(ri, r) for ri in range(n_rev) for r in range(int(cfg["runs"]))]
    print(f"{n_rev} reviews, {len(units)} units")
    rows: list[dict] = []
    for i, part in enumerate(W7(cfg_json=cfg_json).run.map(units, order_outputs=False), 1):
        rows += part
        if i % max(1, len(units) // 10) == 0 or i == len(units):
            print(f"  {i}/{len(units)} units, {time.perf_counter() - t0:.0f}s")
    cfg["platform"] = "modal (linux x86_64)"
    dest = w7_screening.write(pd.DataFrame(rows), cfg)
    print(f"{len(rows)} rows in {time.perf_counter() - t0:.0f}s -> {dest}")
    print((dest / "summary.md").read_text())
