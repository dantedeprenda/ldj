# Pilot protocol template: historical test → shadow pilot → report

A fill-in template for evaluating one operational decision with `ldj`. Fields marked
**[WAREHOUSE]** must be filled in by the operating team; **[AGREE]** fields are agreed between the
team and the evaluator **before any outcome of the evaluation period is looked at**. Nothing here
describes a real site.

Version / date: ____  Frozen (commit id or signed copy): ____

## 1. The decision

| Field | Value |
|---|---|
| Decision unit (one row = one ...) | **[WAREHOUSE]** e.g. one exception / one discrepancy line |
| Decision owner (role) | **[WAREHOUSE]** |
| Who approves integration / budget | **[WAREHOUSE]** |
| Current SOP (document and version) | **[WAREHOUSE]** |
| Volume per week; share handled by exception path | **[WAREHOUSE]** |
| Current handling time and rework cost (source) | **[WAREHOUSE]** |
| Inputs available **at decision time** (fields, systems) | **[WAREHOUSE]** |
| Information that arrives later and must be excluded | **[WAREHOUSE]** (checked with `ldj split --decision-time/--available-at`) |
| Outcome records (where "was this right" is recorded, and when) | **[WAREHOUSE]** |
| Default action | **[AGREE]** e.g. auto-resolution suggestion |
| Fallback path | **[AGREE]** e.g. senior operator / SOP lookup / document check (not assumed to be always right) |
| Physical inspection or sensor evidence needed? | **[WAREHOUSE]** (if yes, a text-only system may not be suitable) |

## 2. Reference labels and grading

| Field | Value |
|---|---|
| Rubric: what counts as correct, and severity levels | **[AGREE]**, written with operators |
| Graders (roles, independence from the system and from each other) | **[WAREHOUSE]** |
| Disagreement handling (second grader, adjudicator) | **[AGREE]** |
| Reference definition used for certificates | **[AGREE]** (a certificate holds only for the label definition it was computed on; see `docs/input-contract.md`) |
| Correctness graded separately from wording/polish | yes / no **[AGREE]** |
| Historical operator decision used as | a comparison action, not automatically the correct answer |

## 3. Historical test

| Field | Value |
|---|---|
| Export (dates, fields, who authorized it) | **[WAREHOUSE]** |
| Grouping key (order, shipment) | **[WAREHOUSE]** |
| Split | `ldj split --time ____ --group ____ --dev-until ____ --cohort-share ____ --seed ____` **[AGREE]** |
| Random cohort size and how it is labeled (blind to scores) | **[AGREE]** |
| Enriched sample of rare errors (optional) | diagnostic only; never used for rates **[AGREE]** |
| Baselines compared | current process; always-default; always-fallback; simple business rules **[WAREHOUSE]**; confidence threshold; benefit-targeting policy |
| Information budget per policy (labels, paired examples) | **[AGREE]** (a paired example costs two executions plus grading) |
| Risk target(s) and confidence | **[AGREE]** e.g. error ≤ ____ at 95%; critical-error limits by type **[WAREHOUSE]** |

Everything that is chosen (prompt, threshold, policy) is chosen on the **dev** period only, then
frozen (commit id: ____) before the eval period is scored once.

## 4. Go / no-go criteria for the shadow pilot (fixed before viewing outcomes)

| Criterion | Threshold |
|---|---|
| Minimum reduction in total handling effort (incl. review, verification, rework, waiting) | **[AGREE]** (a discussion target, not a promise) |
| Acceptable error rate by severity type | **[WAREHOUSE]** |
| Outcome ascertainment (share of cases whose outcome is known) | **[AGREE]** |
| Integration and maintenance effort acceptable | **[WAREHOUSE]** |
| If evidence is insufficient (too few cases for rare failures) | report "insufficient evidence"; do not borrow thresholds from other tasks |

## 5. Shadow pilot

| Field | Value |
|---|---|
| Frozen workflow (commit id) | ____ |
| Period and case volume | **[AGREE]** |
| Who keeps control (the operating team does) | **[WAREHOUSE]** |
| Logged per case | suggestion, escalation reason, operator outcome, handling time, corrections, API cost, failures |
| Review sample | random cases from **both** accepted and escalated suggestions, so silent misses are visible |

What shadow can claim: quality of suggestions and **potential** savings on new cases. What it
cannot claim: **realized** time savings; that needs a later, approved assisted-workflow comparison
with randomized or credibly matched assignment.

## 6. Report outline

1. Recommendation: proceed / narrow / stop, with the reason.
2. Task, SOP version, data dates; dev/eval boundary; cohort size.
3. Baselines (current process, simple rules) vs the evaluated policies.
4. Rubric, grader agreement, disputed cases.
5. Results by task subtype; harmful errors and missed exceptions; escalation frequency and
   fallback benefit (`ldj bridge`); certified automation or "insufficient evidence" (`ldj audit`).
6. Processing and review time; costs.
7. Historical-to-shadow change in performance.
8. Potential vs realized savings, reported separately.
9. What was not checked; deviations from this protocol.

Private delivery, a public case study and any data release are separate decisions; only what the
warehouse authorizes is published.
