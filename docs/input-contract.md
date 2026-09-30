# Input contract: the CSV files `ldj` reads

Three commands take your own data. Each reads one CSV with a header row. Extra columns are
ignored (keep ids and anything you need to trace a row back). A synthetic end-to-end example of all
three is in `examples/` (`uv run python examples/make_examples.py`).

## `ldj split`: dev / eval periods and the audit cohort

Run this first, on the log of decisions you want to evaluate.

| Column | Required | Type | Meaning |
|---|---|---|---|
| time column (`--time`) | yes | date/time | When the decision was made. No missing or unparseable values (the command refuses them). |
| group column (`--group`) | recommended | string | Rows that belong together (an order, a shipment). A group never straddles the dev/eval boundary. |
| decision time + available-at (`--decision-time`, `--available-at`) | optional | date/time | If given, rows whose information became available after the decision are flagged `leak = 1`. Such information must not be a model input. |

Options: `--dev-until DATE` or `--dev-share 0.6` (share of groups, by start time, in dev);
`--cohort-share 0.2`; `--cohort-unit group|row` (default `group`); `--one-per-group`; `--seed`;
`--spanning later|drop`.

Output: the input plus
- `period`: `dev` (earlier; choose prompts, thresholds and policies here, as often as you like) or
  `eval` (later; used once, after everything is frozen).
- `cohort`: 1 for the rows of a seeded random share of eval **groups** (every row of a drawn group
  is in the cohort; with `--cohort-unit row`, a random share of eval rows instead). The cohort
  gives unbiased rates for the eval period.
- `audit_item`: 1 for the rows to label for the audit. Without `--one-per-group` it equals
  `cohort`; with it, exactly one random row per cohort group.
- `audit_role`: `audit` (`audit_item = 1`) or `deploy` (other eval rows, including the unpicked rows
  of cohort groups); empty for dev rows. Label the `audit` rows, and only these, without looking at
  the model's scores.

**Why the group is the sampling unit.** Rows of one order or shipment are correlated: they share a
customer, a carrier, a day, often the same root cause. The audit's certificate (Clopper–Pearson)
assumes independent audit items; feeding it several correlated rows per group makes the evidence
look stronger than it is and the guarantee can fail. So `ldj split` draws whole groups, and
`--one-per-group` passes one random row per drawn group to `ldj audit`, which makes the audit items
independent and the guarantee a statement about groups as sampled. The unpicked rows of a cohort
group go back to `deploy` (they are items the policy runs on, not audit evidence). The report
warns when the audit would have many more rows than independent groups, and whenever
`--cohort-unit row` is used while eval groups have more than one row. Without `--group`, every row
is its own group.

A group whose events span the boundary goes to eval by default (so nothing in dev saw part of it);
`--spanning drop` removes it instead. The printed report gives rows and groups per period, cohort
groups and rows, rows per cohort group (max, mean), audit rows and independent audit groups,
the number of spanning groups, the boundary, and any warnings.

## `ldj audit`: may we automate, and how much?

Use the eval rows.

| Column | Required | Type | Meaning |
|---|---|---|---|
| `score` | yes | number | The frozen system's score; higher = more confident the automatic action is right (`--kind accept`) or the positive class (`classify`, cut at `--cut`), or more likely relevant (`recall`). |
| `role` | yes | `audit` / `deploy` | `audit` = the random audit items, labeled (one per sampled group with `ldj split --one-per-group`); `deploy` = the unlabeled items the policy will run on. Take it from `split`'s `audit_role`. |
| `label` | audit rows | 0/1 | The human reference for audit rows: `accept`: 1 if the automatic action was right; `classify`/`recall`: the true class. |

Options: `--kind accept|classify|recall`, `--alpha` (risk target) or `--target` (recall target),
`--delta` (default 0.05), `--md/--html/--json` outputs. The verdict is "supported" (a threshold, the
share of deploy items it automates, the certified bound) or "insufficient evidence" (with what
more evidence would take). The audit treats every `audit` row as an independent draw: if several
audit rows come from one group, the certificate overstates the evidence. Use `ldj split
--one-per-group` (or otherwise keep one row per group) so that each audit row is independent.

## `ldj bridge`: does sending items to the fallback help?

Use the cohort rows, with **both** actions' outcomes recorded on every row: whatever a policy
would do, the evaluation needs to know what each action would have produced.

| Column | Required | Type | Meaning |
|---|---|---|---|
| `default_ok` | yes | 0/1 | Was the default action (e.g. auto-resolution) right? |
| `fallback_ok` | yes | 0/1 | Was the fallback (e.g. a senior operator, an SOP lookup) right? |
| `default_cost` | yes | number | Cost of the default action (money or minutes; be consistent). |
| `fallback_cost` | yes | number | Cost of the fallback, paid instead of the default. |
| score columns (`--score COL`, repeatable) | optional | number | Candidate escalation scores; higher = escalate first. |

The report gives the four cells (both right; only default right: escalating breaks it; only
fallback right: escalating repairs it; both wrong), the escalation value (repair − break per item),
and each score's result at fixed escalation rates against random and the oracle.

## What the tool cannot check

These are recorded as assumptions in every audit report; the tool has no way to verify them:

- **Random sampling:** the audit cohort is a random sample of the items the policy will face.
  `ldj split` draws it at random; a hand-picked or enriched sample breaks the guarantee.
- **Frozen system:** the model, prompt and head were fixed before the cohort was labeled, and not
  changed after seeing it.
- **Same distribution:** deploy items come from the same process as audited ones. A new source,
  season or SOP needs a new audit.
- **Label reference:** the certificate holds for the label definition it was computed on, and only
  that one. In this project's moderation data, certificates computed on the majority vote of 3
  annotators failed against the consensus reference (up to 29% violations where 5% was allowed),
  while single-annotator labels stayed valid (`results/x4_t1_votes_maj3/summary.md`). Decide the
  reference (who grades, with which rubric) before labeling.

Details of the certificate and its limits: [`docs/methods.md`](methods.md).
