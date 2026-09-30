"""Offline replay of a packaged result: ``ldj reproduce --fixture moderation-v1``.

A fixture (release/fixtures/<name>/) holds only what the analysis reads: test labels, categories
and costs (no item texts), the saved predictions and records, the config, and the expected outputs.
Replaying needs no API key, no dataset download, no cache and no sibling repository.

It (1) reruns the pre-registered analysis and compares every number with the packaged one, and
(2) runs ``ldj audit`` on the saved predictions with a small and a large random audit sample, so
the report shows both an "insufficient evidence" and a "supported" case.
"""

from __future__ import annotations

import json
import shutil
import time
from pathlib import Path

import numpy as np

from ldj.allocate import Policy
from ldj.analysis import analyze
from ldj.audit import audit
from ldj.task import Task

# alpha 0.10 is T1's primary target; 0.21 (no worse than one human reviewer) is its secondary
# target, added to the demo after 0.10 gave "insufficient" at both sizes.
AUDIT_DEMO = {
    "method": "gemma_features|25|42",
    "sizes": [50, 1000],
    "seed": 0,
    "alphas": [0.10, 0.21],
}


def load_fixture_task(d: Path) -> Task:
    t = np.load(d / "task.npz", allow_pickle=False)
    n = len(t["ids"])
    return Task(
        name=str(t["name"]),
        ids=[str(x) for x in t["ids"]],
        texts=[""] * n,  # texts are not shipped; the analysis does not read them
        y=t["y"],
        categories=t["categories"],
        train=np.array([], dtype=int),
        test=np.arange(n),
        review_cost=t["review_cost"],
        human_correct=t["human_correct"],
        auto_cost=t["auto_cost"],
        label_cost=float(t["label_cost"]),
        auto_negative=bool(t["auto_negative"]),
    )


def demo_spec(d: Path) -> dict:
    """The fixture's audit-demo spec (``demo.json``, e.g. moderation-v2), else the v1 default."""
    f = d / "demo.json"
    return json.loads(f.read_text()) if f.exists() else AUDIT_DEMO


def audit_demo(task: Task, preds, spec: dict | None = None) -> list[dict]:
    """Audit one fixed system (a saved head) on random test samples; the rest are deploy items."""
    spec = spec or AUDIT_DEMO
    p = preds[spec["method"]]
    rng = np.random.default_rng(spec["seed"])
    order = rng.permutation(len(p))
    out = []
    for alpha in spec["alphas"]:
        for size in spec["sizes"]:
            a, d = order[:size], order[size:]
            r = audit(p[a], task.y[a], p[d], Policy("classify", alpha=alpha))
            out.append(
                {
                    "alpha": alpha,
                    "audit_size": size,
                    "verdict": r["verdict"],
                    "automated_share": r["automated_share"],
                    "threshold": r["threshold"],
                    "bound": r["bound"],
                    "what_would_help": r["what_would_help"],
                }
            )
    return out


def _close(a, b, tol: float = 1e-9) -> bool:
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_close(a[k], b[k], tol) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(_close(x, y, tol) for x, y in zip(a, b))
    if isinstance(a, float) or isinstance(b, float):
        if a is None or b is None:
            return a is b
        return (np.isnan(a) and np.isnan(b)) or abs(a - b) <= tol
    return a == b


def reproduce(fixture: str, out_dir: str | None = None) -> bool:
    d = Path(fixture)
    if not d.exists():
        d = Path("release/fixtures") / fixture
    out = Path(out_dir or f"results/reproduce/{d.name}")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    t0 = time.perf_counter()
    task = load_fixture_task(d)
    analyze(str(d / "config.yaml"), task=task, preds_dir=str(d), out_dir=str(out))
    expected = json.loads((d / "expected.json").read_text())
    got = json.loads((out / "analysis.json").read_text())
    ok_analysis = _close(got, expected["analysis"])
    spec = demo_spec(d)
    demo = audit_demo(task, np.load(d / "preds.npz"), spec)
    ok_audit = _close(json.loads(json.dumps(demo, default=float)), expected["audit_demo"])
    secs = time.perf_counter() - t0
    lines = [
        f"# Replay of {d.name}",
        "",
        (
            f"- {spec.get('analysis_label', 'Pre-registered analysis')} matches the packaged numbers: "
            f"**{'yes' if ok_analysis else 'NO'}**"
        ),
        f"- Audit demo matches: **{'yes' if ok_audit else 'NO'}**",
        f"- Time: {secs:.0f} s",
        "",
        f"## Audit demo ({spec['method']}; random audit samples from the test split)",
        "",
        spec.get(
            "note",
            "Error-rate target 0.10 is T1's primary; 0.21 (no worse than one human reviewer) is its "
            "secondary target, added to the demo after 0.10 was insufficient at both sizes.",
        ),
        "",
    ]
    for r in demo:
        extra = (
            f"automate about {r['automated_share']:.1%} of deploy items"
            if r["verdict"] == "supported"
            else r["what_would_help"]
        )
        lines.append(
            f"- target {r['alpha']}, {r['audit_size']} audit labels: **{r['verdict']}**; {extra}"
        )
    lines += ["", "Analysis tables: `analysis.md` in this folder."]
    (out / "replay.md").write_text("\n".join(lines) + "\n")
    from ldj.report import replay_html

    (out / "replay.html").write_text(replay_html(d.name, ok_analysis, ok_audit, secs, demo))
    print("\n".join(lines))
    return ok_analysis and ok_audit
