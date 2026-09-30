"""Run X4 allocation jobs on Modal (cloud CPUs), so the laptop can be off.

One-time setup (from the repo root):

    uv sync --extra cloud
    uv run modal token new                      # log in (opens a browser)
    uv run python scripts/modal_upload.py       # data and caches -> private volume "ldj-data"

Run a config (results land in results/<name>/ locally and in the volume's results/):

    uv run modal run scripts/modal_app.py --config configs/x4_t2.yaml [--reps 20] [--chunk 25]
    uv run modal run --detach scripts/modal_app.py --config ...   # keeps running if the laptop
                                                                    # disconnects; fetch later

Rows match the local runner's in every decision (certified, violated) and to ~1e-4 in thresholds
and automation: x86 Linux and Apple ARM round floating point differently, even with the locked
package versions (checked on a 20-resample T1 pilot: summaries differ by at most 5e-5 in mean
automation, 0 elsewhere). Compare runs exactly within one platform, to ~1e-4 across platforms. The image has no GPU and
no PyTorch: embeddings come from the uploaded cache, and LLM backends are offline (cache only).
"""

import json
import os
import shutil
from pathlib import Path

import modal

VOL = modal.Volume.from_name("ldj-data", create_if_missing=True)
ROOT = "/vol"
APP = modal.App("ldj")
image = (
    modal.Image.debian_slim(python_version="3.13")
    .uv_sync(frozen=True)  # the exact versions in uv.lock
    .add_local_python_source("ldj")
    .add_local_dir("configs", "/app/configs")
)
CPU = 1.0  # cores per container: each unit is single-threaded, so more cores per container only add cost
# Starter plan: 100 containers at once across the workspace; beyond that work queues (no extra cost).


def _setup() -> None:
    """Work from /app (configs live in the image) with the volume's data and caches linked in."""
    for name in ("data", ".cache"):
        link = Path("/app") / name
        if not link.exists():
            link.symlink_to(Path(ROOT) / name)
    os.chdir("/app")


def _local_cfg(cfg: dict) -> dict:
    """Point the config at the container's local copy of the call cache (SQLite on a shared
    volume is not safe with many concurrent containers)."""
    cfg = dict(cfg)
    src = Path(ROOT) / cfg.get("cache", ".cache/calls.sqlite")
    dst = Path("/tmp/calls.sqlite")
    if not dst.exists():
        shutil.copy(src, dst)
    cfg["cache"] = str(dst)
    return cfg


@APP.function(image=image, volumes={ROOT: VOL}, cpu=CPU, timeout=600)
def plan(cfg_json: str, chunk: int) -> list:
    from ldj import parallel

    _setup()
    cfg = _local_cfg(json.loads(cfg_json))
    _, groups, _ = parallel.load_for(cfg)
    return parallel.units(cfg, groups, chunk)


@APP.cls(image=image, volumes={ROOT: VOL}, cpu=CPU, timeout=3600, max_containers=100)
class Runner:
    cfg_json: str = modal.parameter()

    @modal.enter()
    def load(self) -> None:
        from ldj import parallel

        _setup()
        self.cfg = _local_cfg(json.loads(self.cfg_json))
        _, self.groups, self.methods = parallel.load_for(self.cfg)
        self.cache: dict = {}

    @modal.method()
    def run(self, unit) -> list[dict]:
        from ldj import parallel

        return parallel.run_unit(self.groups, self.methods, self.cfg, tuple(unit), self.cache)


@APP.function(image=image, volumes={ROOT: VOL}, timeout=600)
def save(name: str, rows_parquet: bytes, files: dict[str, str]) -> None:
    out = Path(ROOT) / "results" / name
    out.mkdir(parents=True, exist_ok=True)
    (out / "rows.parquet").write_bytes(rows_parquet)
    for fname, text in files.items():
        (out / fname).write_text(text)
    VOL.commit()


@APP.local_entrypoint()
def main(config: str, reps: int = 0, chunk: int = 50, out: str = "results") -> None:
    import io
    import time

    import yaml

    from ldj import allocate, parallel

    cfg = yaml.safe_load(Path(config).read_text())
    if reps:
        cfg["reps"] = reps
    cfg_json = json.dumps(cfg)
    cfg["platform"] = "modal (linux x86_64)"  # recorded in config.json; not sent to workers
    t0 = time.perf_counter()
    todo = plan.remote(cfg_json, chunk)
    print(f"{cfg['name']}: {len(todo)} units")
    rows: list[dict] = []
    for i, part in enumerate(Runner(cfg_json=cfg_json).run.map(todo, order_outputs=False), 1):
        rows += part
        if i % max(1, len(todo) // 10) == 0 or i == len(todo):
            print(f"  {i}/{len(todo)} units, {time.perf_counter() - t0:.0f}s")
    df = parallel.canonical(rows)
    delta = cfg["policy"].get("delta", 0.05)
    summary = allocate.summarize(df, delta)
    best, bstar = allocate.b_star(summary)
    dest = Path(out) / cfg["name"]
    dest.mkdir(parents=True, exist_ok=True)
    df.to_parquet(dest / "rows.parquet")
    files = {
        "summary.csv": summary.to_csv(index=False),
        "summary.md": allocate.markdown(summary, best, bstar),
        "config.json": json.dumps(cfg, indent=1),
    }
    for fname, text in files.items():
        (dest / fname).write_text(text)
    buf = io.BytesIO()
    df.to_parquet(buf)
    save.remote(cfg["name"], buf.getvalue(), files)
    print(f"{len(df)} rows in {time.perf_counter() - t0:.0f}s; B* = {bstar}; saved to {dest}")
