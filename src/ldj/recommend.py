"""``ldj recommend``: the frozen default rule (preregistration/default-rule.md) as a command.

The rule was frozen from development evidence (seen data) and tested on untouched data
(preregistration/W5.md; docs/report.md §6). This module only restates it; it does not learn anything.
"""

from __future__ import annotations

from ldj import certify

RULE_NOTE = (
    "This rule was frozen from development data (T0-T2, already seen) and tested once on 5,000 "
    "fresh comments (preregistration/W5.md): its automation advantage replicated; its guarantee "
    "check failed on the pre-registered split and held at 200-400 labels over 20 re-drawn "
    "splits (docs/report.md, section 6). Evidence: preregistration/default-rule.md, results/."
)
MIN_B = 200  # below this nothing useful certified on T1 (preregistration/default-rule.md)
MIN_POSITIVES = 70  # screening: expected positives in the certification sample
RECALL_FIT_SHARE = 0.10


def fit_share(budget: int) -> float:
    """0.25 for B <= 400, 0.50 for B >= 800; in between, the nearer of the two (ties go to 0.25)."""
    if budget <= 400:
        return 0.25
    if budget >= 800:
        return 0.50
    return 0.25 if budget - 400 <= 800 - budget else 0.50


def recommend(
    task: str,
    budget: int,
    alpha: float = 0.10,
    delta: float = 0.05,
    prevalence: float | None = None,
    label_source: str = "consensus",
    target: float = 0.95,
) -> dict:
    if task not in ("classify", "accept", "recall"):
        raise ValueError("task must be classify, accept or recall")
    if label_source not in ("consensus", "single", "majority"):
        raise ValueError("label_source must be consensus, single or majority")
    warnings = []
    if label_source == "majority":
        warnings.append(
            "Certificates hold only for the label definition they are computed on. On T1, "
            "certificates computed on majority-of-3 votes failed against the consensus (up to 29% "
            "violations at a 5% target; results/x4_t1_votes_maj3/). Certify on the reference you "
            "will be judged against."
        )
    elif label_source == "single":
        warnings.append(
            "One annotator's labels keep the guarantee on T1 but automated about half as much as "
            "consensus labels (results/x4_t1_single/); consensus labels are preferred."
        )
    out = {
        "task": task,
        "budget": budget,
        "delta": delta,
        "label_source": label_source,
        "warnings": warnings,
        "note": RULE_NOTE,
    }
    if task == "recall":
        need = certify.min_accepted(1 - target, delta)
        out.update(target_recall=target, zero_miss_positives=need)
        if prevalence is None:
            out.update(
                action="need prevalence",
                advice="Give --prevalence: random-sample recall certification depends on "
                "how many relevant items the certification sample will hold.",
            )
            return out
        expected = prevalence * (1 - RECALL_FIT_SHARE) * budget
        out["expected_positives"] = expected
        if expected >= MIN_POSITIVES:
            out.update(
                action="certify from a random sample",
                method="features + judge",
                fit_share=RECALL_FIT_SHARE,
                advice=f"Fit on {RECALL_FIT_SHARE:.0%} of the labels; certify recall on "
                f"the rest (~{expected:.0f} expected positives, >= {MIN_POSITIVES}).",
            )
        else:
            out.update(
                action="use certified stopping with active learning",
                advice=f"Only ~{expected:.0f} positives expected in a random "
                f"certification sample (< {MIN_POSITIVES}; {need} with no misses "
                f"are needed for {target:.0%} recall at {1 - delta:.0%}). Screen "
                "with active learning and a certified stopping rule instead (W7: "
                "held 95% recall in every run, saving ~15%).",
            )
        return out
    need = certify.min_accepted(alpha, delta)
    out.update(alpha=alpha, zero_error_min_audit=need, method="features + judge")
    if budget < MIN_B:
        out.update(
            action="insufficient evidence expected",
            advice=f"Collect >= {MIN_B} labels; below that nothing useful was certified "
            f"on T1. Any certificate needs >= {need} audited items in the automated "
            f"region with no errors.",
        )
        return out
    f = fit_share(budget)
    n_fit = round(f * budget)
    out.update(
        action="fit then certify",
        fit_share=f,
        n_fit=n_fit,
        n_certify=budget - n_fit,
        advice=f"Fit features + judge on {n_fit} labels; certify on the other "
        f"{budget - n_fit}, a random sample never used for fitting or choices.",
    )
    return out


def text(r: dict) -> str:
    lines = [f"Recommendation ({r['task']}, B = {r['budget']}): **{r['action']}**", ""]
    if "method" in r:
        lines.append(f"- Method: {r['method']}")
    lines.append(f"- {r['advice']}")
    if "zero_error_min_audit" in r:
        lines.append(
            f"- Zero-error minimum audit size for alpha = {r['alpha']}, delta = "
            f"{r['delta']}: {r['zero_error_min_audit']} items in the automated region."
        )
    if "zero_miss_positives" in r:
        lines.append(
            f"- Zero-miss minimum for recall {r['target_recall']}: "
            f"{r['zero_miss_positives']} positives."
        )
    lines += [f"- Warning: {w}" for w in r["warnings"]]
    lines += ["", r["note"]]
    return "\n".join(lines) + "\n"
