# Audit report

**Verdict: insufficient evidence.** Target: error rate among automated items <= 0.1, with probability >= 0.95 over the draw of the audit sample (policy: accept).

- Audit sample: 121 labeled items; deploy items: 1036.
- Certifying risk <= 0.1 needs at least 29 audit items in the automated region with no errors (more if any are wrong); the first threshold tested holds 53 audit items.

## Assumptions (not checked by this tool)

- The audit rows are a random sample of the items the policy will face.
- The decision system (model, prompt, head) was frozen before the audit rows were labeled, and not changed after seeing them.
- Deploy items come from the same distribution as audited items; a changed source needs a new audit.
- Audit labels are the reference the target is stated against (e.g. one reviewer vs a consensus changes what is certified).

The guarantee is about the rate over repeated audit samples. It says nothing about any single automated item, and nothing after the data source changes.
