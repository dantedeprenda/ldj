"""Self-contained HTML (and JSON-ready dicts) for ``ldj audit``, ``ldj bridge`` and ``ldj reproduce``.

One file per report: inline CSS, no scripts, no external assets or URLs, light and dark themes from
the viewer's system setting. Every text value is escaped. The wording follows the tool's rules: a
guarantee is over repeated audit samples, not about any single automated item; "insufficient
evidence" is shown as prominently as "supported"; unchecked assumptions are always listed.
"""

from __future__ import annotations

import html
import math

import numpy as np

from ldj import bridge

CSS = """
:root { --bg:#ffffff; --fg:#1d1d1f; --muted:#5f6368; --line:#d9dce1; --card:#f6f7f9;
  --ok:#0b6b3a; --ok-bg:#e3f4ea; --no:#8a4b00; --no-bg:#fdf0dc; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#16181c; --fg:#e8eaed; --muted:#a3a8b0; --line:#34383f; --card:#1f2228;
    --ok:#7fd8a4; --ok-bg:#16301f; --no:#f3c07a; --no-bg:#3a2a12; }
}
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--fg);
  font:15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
main { max-width:860px; margin:0 auto; padding:24px 16px 48px; }
h1 { font-size:22px; margin:0 0 4px; } h2 { font-size:17px; margin:28px 0 8px; }
.sub { color:var(--muted); margin:0 0 20px; }
.verdict { border-radius:10px; padding:16px 18px; margin:16px 0; font-size:18px; font-weight:600; }
.verdict.ok { background:var(--ok-bg); color:var(--ok); }
.verdict.no { background:var(--no-bg); color:var(--no); }
.verdict small { display:block; font-size:14px; font-weight:400; margin-top:6px; color:var(--fg); }
table { border-collapse:collapse; width:100%; margin:8px 0; font-variant-numeric:tabular-nums; }
th, td { text-align:left; padding:6px 8px; border-bottom:1px solid var(--line); }
th { color:var(--muted); font-weight:500; font-size:13px; }
.wrap { overflow-x:auto; }
.card { background:var(--card); border-radius:10px; padding:12px 16px; margin:8px 0; }
ul { padding-left:20px; } li { margin:4px 0; }
.note { color:var(--muted); font-size:13px; }
"""


def _e(x) -> str:
    return html.escape(str(x), quote=True)


def _num(x, fmt: str = "{:.4g}") -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    return fmt.format(x)


def _page(title: str, body: str) -> str:
    return (
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f"<title>{_e(title)}</title><style>{CSS}</style></head>"
        f"<body><main>{body}</main></body></html>\n"
    )


def audit_html(r: dict) -> str:
    """HTML for a result dict from ``ldj.audit.audit``."""
    p = r["policy"]
    if p["kind"] == "recall":
        target = f"recall ≥ {p['target']}"
    else:
        target = f"error rate among automated items ≤ {p['alpha']}"
    conf = 1 - p["delta"]
    ok = r["verdict"] == "supported"
    if ok:
        what = (
            f"Automate {'items scored below' if p['kind'] == 'recall' else 'items at threshold'} "
            f"{_num(r['threshold'])}: about {_num(r['automated_share'], '{:.1%}')} of deploy items."
        )
    else:
        what = r.get("what_would_help") or "No threshold could be certified."
    rows = [
        ("Target", target),
        ("Confidence", f"{conf:.2f} over repeated audit samples"),
        ("Policy", p["kind"]),
        ("Audit sample (labeled)", r["n_audit"]),
        ("Deploy items (unlabeled)", r["n_deploy"]),
        ("Threshold", _num(r.get("threshold"))),
        ("Share of deploy items automated", _num(r.get("automated_share"), "{:.1%}")),
        ("Certified bound", _num(r.get("bound"))),
    ]
    if "audit_positives" in r:
        rows.append(("Positives in the audit sample", r["audit_positives"]))
    if "audit_items_in_automated_region" in r:
        rows.append(("Audit items in the automated region", r["audit_items_in_automated_region"]))
        rows.append(("Errors among them", r["audit_errors_in_automated_region"]))
    table = "".join(f"<tr><th>{_e(k)}</th><td>{_e(v)}</td></tr>" for k, v in rows)
    assumptions = "".join(f"<li>{_e(a)}</li>" for a in r.get("assumptions", []))
    body = (
        "<h1>Audit report</h1>"
        f'<p class="sub">{_e(target)}, with probability ≥ {conf:.2f}</p>'
        f'<div class="verdict {"ok" if ok else "no"}">'
        f"{'Evidence supports this policy' if ok else 'Insufficient evidence'}"
        f"<small>{_e(what)}</small></div>"
        f'<div class="wrap"><table>{table}</table></div>'
        "<h2>What the guarantee means</h2>"
        '<div class="card">Over many independent random audit samples, the chance that this '
        f"procedure issues an unsafe certificate (one whose true error misses the target) is at "
        f"most {1 - conf:.0%}. Audits that issue nothing count as safe, so this is not a promise "
        "about the share of issued certificates: when certificates are rare, a larger share of the "
        "issued ones can be unsafe. It says nothing about any single automated item, and it stops "
        "applying when the data source changes.</div>"
        "<h2>Assumptions this tool cannot check</h2>"
        f"<ul>{assumptions}</ul>"
    )
    return _page("Audit report", body)


def bridge_result(path: str, scores: list[str], rates: list[float]) -> dict:
    """The data behind ``ldj bridge`` as a dict (same computation as ``bridge.report_csv``)."""
    import pandas as pd

    df = pd.read_csv(path)
    missing = [c for c in (*bridge.REQUIRED, *scores) if c not in df.columns]
    if missing:
        raise ValueError(f"{path}: missing columns {missing}")
    if df[list(bridge.REQUIRED)].isna().any().any():
        raise ValueError(f"{path}: every row needs both outcomes and both costs")
    p = bridge.Paired(*(df[c].to_numpy(float if "cost" in c else int) for c in bridge.REQUIRED))
    rows = []
    for rate in rates:
        cands = [("random", np.zeros(p.n)), ("oracle", None)]
        cands += [(s, df[s].to_numpy(float)) for s in scores]
        for name, s in cands:
            mask = bridge.oracle_mask(p, rate) if s is None else bridge.escalate_top(s, rate)
            o = bridge.outcome(p, mask)
            m, lo, hi = bridge.net_ci(p, [mask])
            rows.append({"rate": rate, "score": name, **o, "net": m, "ci": [lo, hi]})
    return {"path": path, "table": bridge.table(p), "rows": rows}


def bridge_html(res: dict) -> str:
    t = res["table"]
    cells = (
        f"<tr><td>{t['both_right']}</td><td>{t['only_default_right']}</td>"
        f"<td>{t['only_fallback_right']}</td><td>{t['both_wrong']}</td>"
        f"<td>{t['escalation_value']:+.3f}</td></tr>"
    )
    rows = "".join(
        f"<tr><td>{r['rate']:.0%}</td><td>{_e(r['score'])}</td><td>{r['accuracy']:.3f}</td>"
        f"<td>{_num(r['cost'])}</td><td>{r['repaired']}</td><td>{r['broken']}</td>"
        f"<td>{r['net']:+.4f}</td><td>[{r['ci'][0]:+.4f}, {r['ci'][1]:+.4f}]</td></tr>"
        for r in res["rows"]
    )
    body = (
        "<h1>Escalation report</h1>"
        f'<p class="sub">{_e(res["path"])}: {t["n"]} items. Default right '
        f"{t['default_accuracy']:.3f} at {_num(t['default_cost'])} per item; fallback right "
        f"{t['fallback_accuracy']:.3f} at {_num(t['fallback_cost'])}.</p>"
        '<h2>Where escalation can matter</h2><div class="wrap"><table>'
        "<tr><th>Both right</th><th>Only default right (escalating breaks)</th>"
        "<th>Only fallback right (escalating repairs)</th><th>Both wrong</th>"
        f"<th>Escalation value</th></tr>{cells}</table></div>"
        '<p class="note">Escalation value = P(repair) − P(break): what escalating every item '
        "is worth. Both outcomes must be observed on every evaluated item.</p>"
        '<h2>Escalating the top-scored share</h2><div class="wrap"><table>'
        "<tr><th>Rate</th><th>Score</th><th>Accuracy</th><th>Cost</th><th>Repaired</th>"
        f"<th>Broken</th><th>Net</th><th>95% CI</th></tr>{rows}</table></div>"
        '<div class="card">Net = (repaired − broken) / items. The oracle is an upper bound, not '
        "a policy. A score earns its place only by beating random and the best fixed action at "
        "equal cost on new items; predicting that the default will fail is not enough.</div>"
    )
    return _page("Escalation report", body)


def replay_html(name: str, ok_analysis: bool, ok_audit: bool, secs: float, demo: list) -> str:
    items = []
    for r in demo:
        ok = r["verdict"] == "supported"
        extra = (
            f"automate about {r['automated_share']:.1%} of deploy items"
            if ok
            else (r.get("what_would_help") or "")
        )
        items.append(
            f"<tr><td>{_e(r['alpha'])}</td><td>{_e(r['audit_size'])}</td>"
            f"<td>{'Supported' if ok else 'Insufficient evidence'}</td><td>{_e(extra)}</td></tr>"
        )
    good = ok_analysis and ok_audit
    body = (
        f"<h1>Replay of {_e(name)}</h1>"
        f'<div class="verdict {"ok" if good else "no"}">'
        f"{'Every number matches the packaged result' if good else 'MISMATCH'}"
        f"<small>Pre-registered analysis: {'match' if ok_analysis else 'mismatch'}. "
        f"Audit demo: {'match' if ok_audit else 'mismatch'}. Time {secs:.0f} s.</small></div>"
        '<h2>Audit demo</h2><div class="wrap"><table><tr><th>Error target</th>'
        f"<th>Audit labels</th><th>Verdict</th><th>Detail</th></tr>{''.join(items)}</table></div>"
        '<p class="note">Target 0.10 is T1\'s primary; 0.21 (no worse than one human reviewer) '
        "is its secondary target, added to the demo after 0.10 was insufficient at both sizes. "
        "Analysis tables: analysis.md in this folder.</p>"
    )
    return _page(f"Replay of {name}", body)
