"""Build the offline replay fixture release/fixtures/moderation-v1/ from the T1 results.

    uv run python scripts/make_fixture.py

Needs the local T1 data and results (data/, results/t1/). Writes test labels, categories and costs
(no comment texts), the saved predictions and records, the config, the expected outputs and
SHA256SUMS. The fixture is committed so a fresh clone can replay without any of those.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
import yaml

from ldj.reproduce import audit_demo, load_fixture_task
from ldj.tasks import load_task

NAME = "moderation-v1"
README = """# Fixture moderation-v1

The T1 (content moderation) pre-registered result, packaged for `ldj reproduce --fixture
moderation-v1`. It rebuilds `results/t1/analysis.md` (H1–H3) and an audit demo offline.

- `task.npz`: for the 2,000 test comments: ids, the consensus label (hate speech score > 0.5),
  platform category, one real annotator's correctness, review and automation costs. No texts.
- `preds.npz`, `records.json`: every method's saved test predictions and run records.
- `config.yaml`: the pre-registered T1 config. `expected.json`: the outputs to match.

Data: Measuring Hate Speech corpus (Kennedy et al. 2020, CC-BY-4.0), ucberkeley-dlab. Gemma judge
probabilities are model outputs; Google claims no rights in Gemma outputs (Gemma Terms of Use).
Code: Apache-2.0.
"""


def main() -> int:
    cfg_path = Path("configs/t1.yaml")
    cfg = yaml.safe_load(cfg_path.read_text())
    task = load_task(cfg["task"])
    src = Path("results/t1")
    out = Path("release/fixtures") / NAME
    out.mkdir(parents=True, exist_ok=True)
    te = np.asarray(task.test)
    np.savez_compressed(
        out / "task.npz",
        name=np.array(task.name),
        ids=np.array([task.ids[i] for i in te]),
        y=task.y[te],
        categories=task.categories[te],
        human_correct=task.human_correct[te],
        review_cost=task.review_cost[te],
        auto_cost=task.auto_cost[te],
        label_cost=np.array(task.label_cost),
        auto_negative=np.array(task.auto_negative),
    )
    shutil.copy(src / "preds.npz", out / "preds.npz")
    shutil.copy(src / "records.json", out / "records.json")
    shutil.copy(cfg_path, out / "config.yaml")
    (out / "README.md").write_text(README)
    ft = load_fixture_task(out)
    expected = {
        "analysis": json.loads((src / "analysis.json").read_text()),
        "audit_demo": json.loads(
            json.dumps(audit_demo(ft, np.load(out / "preds.npz")), default=float)
        ),
    }
    (out / "expected.json").write_text(json.dumps(expected, indent=1))
    sums = [
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}"
        for p in sorted(out.iterdir())
        if p.name != "SHA256SUMS"
    ]
    (out / "SHA256SUMS").write_text("\n".join(sums) + "\n")
    size = sum(p.stat().st_size for p in out.iterdir())
    print(f"wrote {out} ({size / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
