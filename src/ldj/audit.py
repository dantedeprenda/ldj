"""Audit one fixed decision system from a random sample of human checks.

Input: a score for every item. Items with role ``audit`` also carry a human label and must be a
random sample of the items the policy will face, labeled after the system was frozen. Items with
role ``deploy`` are the unlabeled items the policy will run on; the threshold grid is built from
their scores only, never from the audit sample.

Output: either "supported" (a threshold whose risk, or recall, is certified at the stated target
with probability >= 1 - delta, and the share of deploy items it would automate) or "insufficient
evidence", with what more evidence would be needed. It cannot check that the audit sample really
is random, that the system was frozen before labeling, or that deploy items resemble the audited
ones; those are recorded as assumptions in every report.
"""

from __future__ import annotations

from dataclasses import asdict

import numpy as np

from ldj import certify
from ldj.allocate import Policy, _grid

ASSUMPTIONS = [
    "The audit rows are a random sample of the items the policy will face.",
    (
        "The decision system (model, prompt, head) was frozen before the audit rows were labeled, "
        "and not changed after seeing them."
    ),
    (
        "Deploy items come from the same distribution as audited items; a changed source needs a "
        "new audit."
    ),
    (
        "Audit labels are the reference the target is stated against (e.g. one reviewer vs a "
        "consensus changes what is certified)."
    ),
]


def audit(scores_audit, labels_audit, scores_deploy, policy: Policy) -> dict:
    s_a = np.asarray(scores_audit, float)
    y_a = np.asarray(labels_audit, float)
    s_d = np.asarray(scores_deploy, float)
    if not np.isin(y_a, (0, 1)).all():
        raise ValueError("audit labels must be 0/1")
    if np.isnan(s_a).any() or np.isnan(s_d).any():
        raise ValueError(
            "scores contain NaN: score every row (a missing score would silently "
            "become the strictest threshold and block certification)"
        )
    if len(s_d) == 0:
        raise ValueError("need deploy rows: the threshold grid is built from their scores")
    grid = _grid(policy, s_d, len(s_a))
    out = {
        "policy": asdict(policy),
        "n_audit": len(s_a),
        "n_deploy": len(s_d),
        "assumptions": ASSUMPTIONS,
    }
    if policy.kind == "recall":
        cert = certify.certify_recall(s_a, y_a, grid, policy.target, policy.delta, policy.selection)
        t = cert.threshold
        automated = float((s_d < t).mean()) if cert.certified else 0.0
        n_pos = int(y_a.sum())
        need = certify.min_accepted(1 - policy.target, policy.delta)
        out.update(
            audit_positives=n_pos,
            threshold=t,
            automated_share=automated,
            bound=float(cert.bounds[cert.index]) if cert.certified else None,
            verdict="supported" if automated > 0 else "insufficient evidence",
            what_would_help=(
                None
                if automated > 0
                else f"Certifying recall >= {policy.target} needs at least {need} positives in the "
                f"audit sample with none missed; it has {n_pos}."
            ),
        )
        return out
    conf_a, loss_a = policy.conf_loss(s_a, y_a)
    cert = certify.certify_risk(conf_a, loss_a, grid, policy.alpha, policy.delta, policy.selection)
    conf_d, _ = policy.conf_loss(s_d, np.zeros(len(s_d)))
    t = cert.threshold
    automated = float((conf_d >= t).mean()) if cert.certified else 0.0
    need = certify.min_accepted(policy.alpha, policy.delta)
    auto_a = conf_a >= t if cert.certified else np.zeros(len(s_a), bool)
    out.update(
        threshold=t,
        automated_share=automated,
        audit_items_in_automated_region=int(auto_a.sum()),
        audit_errors_in_automated_region=int(loss_a[auto_a].sum()),
        bound=float(cert.bounds[cert.index]) if cert.certified else None,
        verdict="supported" if automated > 0 else "insufficient evidence",
        what_would_help=(
            None
            if automated > 0
            else f"Certifying risk <= {policy.alpha} needs at least {need} audit items in the "
            f"automated region with no errors (more if any are wrong); the first threshold "
            f"tested holds {int(cert.counts[0]) if len(cert.counts) else 0} audit items."
        ),
    )
    return out


def markdown(r: dict) -> str:
    p = r["policy"]
    target = (
        f"recall >= {p['target']}"
        if p["kind"] == "recall"
        else f"error rate among automated items <= {p['alpha']}"
    )
    lines = [
        "# Audit report",
        "",
        (
            f"**Verdict: {r['verdict']}.** Target: {target}, with probability >= {1 - p['delta']:.2f} "
            f"over the draw of the audit sample (policy: {p['kind']})."
        ),
        "",
        f"- Audit sample: {r['n_audit']} labeled items; deploy items: {r['n_deploy']}.",
    ]
    if r["verdict"] == "supported":
        lines.append(
            f"- Automate {'items scored below' if p['kind'] == 'recall' else 'at threshold'} "
            f"{r['threshold']:.4g}: about {r['automated_share']:.1%} of deploy items."
        )
        lines.append(f"- Certified bound: {r['bound']:.4f}.")
    else:
        lines.append(f"- {r['what_would_help']}")
    lines += ["", "## Assumptions (not checked by this tool)", ""]
    lines += [f"- {a}" for a in r["assumptions"]]
    lines += [
        "",
        (
            "The guarantee is about the rate over repeated audit samples. It says nothing about any "
            "single automated item, and nothing after the data source changes."
        ),
    ]
    return "\n".join(lines) + "\n"
