# ldj: methods and limitations

A two-page note for anyone using the tool's reports. Facts and numbers come from the evidence
tables in `results/` (map: `results/README.md`) and the technical report, `docs/report.md`.

## What the tool answers

> Given your model's predictions and a limited set of human checks, what fraction of work can you
> justify automating, what does the whole workflow cost, and when is the evidence insufficient?

- `ldj audit`: certify one fixed decision system from a random audit sample.
- `ldj bridge`: measure when escalating to a fallback action helps, from paired outcomes.
- `ldj reproduce`: replay a packaged result offline and check every number.

## What `ldj audit` certifies

**Selective risk** (accept or classify policies): among the items the policy automates (score, or
distance from the decision cut, at or above a threshold λ), the share it gets wrong is ≤ α.
**Recall** (screening): auto-rejecting items scored below t keeps ≥ the target share of positives.

Both hold **with probability ≥ 1 − δ over the draw of the audit sample** (δ = 0.05 by default).

How:
1. **Thresholds come from unlabeled deploy items only.** The grid is quantiles of the deploy scores,
   never of the audit sample's scores or labels. This keeps each test valid.
2. **One-sided Clopper–Pearson bounds** on the error rate (or a lower bound on recall) at each grid
   threshold, exact conditional on how many audit items fall in the automated region (or how many
   are positive).
3. **Fixed-sequence testing** (Learn-then-Test) from strict to loose thresholds, at level δ,
   stopping at the first failure. The loosest passing threshold is certified.
4. **The grid starts where the audit sample is expected to hold 2× the zero-error minimum** of
   items (29 items for α = 0.10, δ = 0.05, so 58). Starting at 1× made power level off near 50%
   at any sample size in simulation; 2× reached 87% at n = 1,000 and 99% at n = 3,000.

Validity is checked by brute force against exact binomial tails and by simulation with known risk
curves (violation rate ≤ δ; the naive "observed risk ≤ α" rule violates far more often).

## What the guarantee means, and what it doesn't

- It is about **the procedure over repeated independent audit samples**: the probability that it
  issues an unsafe certificate (true risk above α, or recall below target) is at most δ, where an
  audit that issues nothing counts as safe. It is **not** a promise that 1 − δ of *issued*
  certificates are safe (next bullet but one). It says nothing about any single automated item.
  *(Corrected 2026-09-30; an earlier version stated the issued-certificate reading.)*
- It **stops applying when the data source changes.** A new source needs a new audit.
- **Among issued certificates, the violation rate can exceed δ** when certificates are rare. On
  T2 at B = 800, 2.5% of all draws violated (within δ) but 7.6% of issued certificates did; on T0,
  6–100% of rare certificates violated while the unconditional rate stayed within δ. Reports show
  both, plus how often a useful certificate is issued and the spread of automation across draws.
- An average hides variance: on T1 at 200 labels (features, 25% for fitting), mean certified
  automation was 29.5%, but only 59% of draws certified anything useful; the median was 40%.

## Assumptions the tool cannot check

1. The audit rows are a random sample of the items the policy will face.
2. The system (model, prompt, head) was frozen before the audit rows were labeled.
3. Deploy items come from the same distribution as audited items.
4. The audit labels are the reference the target is stated against.

## The label reference matters

Certifying T1 with **one annotator's labels** instead of a consensus of ≥ 3 kept every certificate
valid when scored against the consensus, but **automated about half as much** (e.g. 18.9% vs 49.2%
at 400 labels). This annotator disagrees with the consensus ~21% of the time, so measured errors
look worse. The direction is not guaranteed: noise correlated with the model's errors could make
certificates optimistic. Consensus labels were better even per annotation action.

## Escalation value (`ldj bridge`)

With both actions observed on every evaluated item, four cells: both right; only default right
(escalating **breaks** it); only fallback right (escalating **repairs** it); both wrong.
**Escalation value = P(repair) − P(break)**, what escalating every item is worth. A score earns its
place only by beating random and the best fixed action **at equal cost** on new items. On routing
(T0), escalating the prompts that look hardest barely beat random, because hard prompts are often
hard for both models; no policy reliably beat always using the mid-priced model at equal cost,
though a perfect policy would have gained 6.6 points.

## Whole-workflow cost

On T1 (moderation; $0.25 per review; a consensus label counted as 3 annotations), nothing paid off
at 1,000 items: label costs dominate. At 10,000 items, question features plus the judge's score
with 400 labels saved ~45% of human checks in 94% of draws; break-even ~2,100 items. The direct
zero-shot judge rarely paid at these volumes. These are scenarios, not measured volumes.

## Numeric reproducibility

Runs on Apple ARM and x86 Linux (Modal) agree on every decision (certified, violated) and to
~1e-4 in thresholds and automation, even with identical package versions: the chips round
floating point differently. Compare runs exactly within one platform, to ~1e-4 across platforms.
Each run records its platform. The packaged replay matches exactly on the platform that built it.

## Limits of the evidence so far

- **Most numbers are on data already seen** (T0 routing, T1 moderation, T2 screening). The default
  rule (`preregistration/default-rule.md`) was frozen from them and then tested once on 5,000
  untouched comments (`results/w5_t1_fresh/w5.md`). Its automation advantage replicated; its
  guarantee check failed on the pre-registered split and held at 200–400 labels over 20 re-drawn
  splits, slightly exceeded at 800 (report §6).
- **A pre-declared success criterion** (≥ 10% certified automation at ≤ 800 labels on ≥ 2 tasks)
  failed with text methods: T1 passed from 200 labels; T2 and T0 failed. With Jev question features
  T0 also passes, but Jev was added after that verdict.
- **Screening:** certifying 95% recall at 95% confidence needs ≥ 59 positives in the audit sample
  with none missed. Most systematic reviews' pools cannot supply that from a random sample; only
  1 of 15 did at 800 labels. Active learning with a statistical stopping rule met 95% recall in
  every tested run, but that is empirical, not a proven guarantee.
- **Certificates hold only for their label definition and source:** majority-of-3 labels and a
  platform shift both broke them (report §5).
- The audit labels were proposed by an LLM and checked by the author, not independently
  adjudicated.
