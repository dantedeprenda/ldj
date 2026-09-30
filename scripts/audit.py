"""Blind hand audit of test labels (pre-registered: 200 test items per task, seed 7).

    uv run python scripts/audit.py make t1     # writes data/audit/t1_audit.csv
    (fill the your_label column: 1 = positive, 0 = negative, blank = can't tell)
    uv run python scripts/audit.py score t1    # agreement, and the ids you disagree with
    uv run python scripts/audit.py score t1 claude   # scores data/audit/t1_audit_claude.csv

The sheet shows only the text (and, for T2, the review's criteria); never the dataset's label
or any method's score. The sheet lives in data/ (gitignored): SYNERGY abstracts must not be
republished and T1 comments are offensive. ``score`` writes results/audit_<task>.json with the
ids you marked differently, for the pre-registered sensitivity analysis.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np
import yaml

from ldj.tasks import load_task

QUESTION = {
    "t1": "Is this comment hate speech? (attacks or demeans a group, or a person because they "
    "belong to a group, defined by race, ethnicity, religion, gender, sexual orientation, "
    "gender identity, disability or national origin) 1 = yes, 0 = no",
    "t2": "Should this record go on to full-text review for this systematic review, given its "
    "research question and eligibility criteria? 1 = yes, 0 = no",
}


def task_for(name: str):
    return load_task(yaml.safe_load(Path(f"configs/{name}.yaml").read_text())["task"])


def make(name: str, n: int = 200) -> None:
    t = task_for(name)
    pick = np.sort(np.random.default_rng(7).choice(t.test, n, replace=False))
    out = Path("data/audit") / f"{name}_audit.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    ctx = t.meta.get("category_context", {})
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "context", "text", "your_label", "notes"])
        for i in pick:
            w.writerow([t.ids[i], ctx.get(str(t.categories[i]), ""), t.texts[i], "", ""])
    print(f"wrote {out} ({n} items). Question: {QUESTION[name]}")


def score(name: str, labeler: str | None = None) -> None:
    """``labeler`` scores a separate copy of the sheet (e.g. labels proposed by Claude, kept
    apart from the author's own) and writes results/audit_<task>_<labeler>.json."""
    t = task_for(name)
    y = dict(zip(t.ids, t.y, strict=True))
    suffix = f"_{labeler}" if labeler else ""
    rows = list(csv.DictReader((Path("data/audit") / f"{name}_audit{suffix}.csv").open()))
    done = [r for r in rows if r["your_label"].strip() in ("0", "1")]
    disagree = [r["id"] for r in done if float(r["your_label"]) != y[r["id"]]]
    res = {
        "labeled": len(done),
        "of": len(rows),
        "agreement": 1 - len(disagree) / len(done) if done else None,
        "disagree_ids": disagree,
    }
    Path("results").mkdir(exist_ok=True)
    Path(f"results/audit_{name}{suffix}.json").write_text(json.dumps(res, indent=1))
    print(
        json.dumps({k: v for k, v in res.items() if k != "disagree_ids"}),
        f"{len(disagree)} disagreements",
    )


if __name__ == "__main__":
    {"make": make, "score": score}[sys.argv[1]](*sys.argv[2:])
