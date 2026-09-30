"""Build replay fixture release/fixtures/moderation-v2/: the frozen rule's method (features + judge).

    uv run python scripts/make_fixture_v2.py

Like moderation-v1 (``scripts/make_fixture.py``), but packaged from the X1 run on T1
(``configs/x1_t1.yaml``: same task, splits, seeds and label draws as the pre-registered T1 run),
whose saved predictions include features + judge (``gemma_features_judge``), the method of the
frozen default rule (preregistration/default-rule.md). The analysis part is the x1_t1 analysis (primary:
features + judge; exploratory, not pre-registered). The audit demo audits the features + judge
head fit on 25 labels (seed 42) with the same targets, sizes and seed as v1. v1 is untouched.
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

NAME = "moderation-v2"
DEMO = {
    "method": "gemma_features_judge|25|42",
    "sizes": [50, 1000],
    "seed": 0,
    "alphas": [0.10, 0.21],
    "analysis_label": "Exploratory X1 analysis",
    "note": (
        "The frozen rule's method (features + judge), fit on 25 labels. Error-rate target 0.10 is "
        "T1's primary; 0.21 (no worse than one human reviewer) its secondary. Same sizes and seed "
        "as moderation-v1."
    ),
}
README = """# Fixture moderation-v2

The T1 (content moderation) X1 run, packaged for `ldj reproduce --fixture moderation-v2`. It
rebuilds `results/x1_t1/analysis.md` (features + judge vs question features, bge-large and the
zero-shot judge; exploratory) and an audit demo of the frozen default rule's method
(features + judge, preregistration/default-rule.md) offline.

- `task.npz`: for the 2,000 test comments: ids, consensus label, platform, one annotator's
  correctness, costs. No texts.
- `preds.npz`, `records.json`: the X1 run's saved test predictions and records.
- `config.yaml`: configs/x1_t1.yaml. `demo.json`: the audit demo. `expected.json`: outputs to match.

Data: Measuring Hate Speech corpus (Kennedy et al. 2020, CC-BY-4.0). Gemma outputs: Google claims
no rights in Gemma outputs (Gemma Terms of Use). Code: Apache-2.0.
"""


def main() -> int:
    cfg_path = Path("configs/x1_t1.yaml")
    cfg = yaml.safe_load(cfg_path.read_text())
    task = load_task(cfg["task"])
    src = Path("results/x1_t1")
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
    (out / "demo.json").write_text(json.dumps(DEMO, indent=1))
    (out / "README.md").write_text(README)
    ft = load_fixture_task(out)
    expected = {
        "analysis": json.loads((src / "analysis.json").read_text()),
        "audit_demo": json.loads(
            json.dumps(audit_demo(ft, np.load(out / "preds.npz"), DEMO), default=float)
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
    for r in expected["audit_demo"]:
        print(r["alpha"], r["audit_size"], r["verdict"], round(r["automated_share"], 3))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
