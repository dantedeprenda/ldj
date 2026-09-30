# Errata

Corrections made after results were first reported. Each was verified against the code before
being applied; the affected documents were corrected in place.

## 1. Consensus labels cost 5.66 annotations, not 3 (2026-09-30)

Found by a read-only correctness review. The moderation ledger counted a consensus label as 3
annotation actions (the task's minimum and median), but the consensus label is the Rasch score over
every annotation of the comment: 5.66 on average in the training pool, and the mean sets total
cost. `scripts/ledger.py` now uses 5.66, with 3 kept as a labeled sensitivity.

Corrected, features + judge:

| Budget | Break-even (items) | Human checks saved at 10k |
|---|---|---|
| B = 200 | 1,528 → **2,884** | 33.3% → **27.9%** |
| B = 400 | 2,092 → **3,948** | 45.4% → **34.7%** |
| B = 800 | 3,541 → **6,681** | 43.8% → **22.5%** |

The claim "consensus labels beat one annotator per annotation action" is withdrawn. Certificates,
violation rates and every non-ledger number are unaffected.

The same review found three issues with no effect on reported numbers:
- `ldj audit` gave a silent wrong verdict on NaN scores; they are now refused.
- An offline cache miss is scored 0.5 instead of raising. The confirmatory run was checked for
  completeness before it ran.
- The pool-threshold grid can be one item off because of float rounding. Validity is unaffected;
  it was left as is so the confirmatory test stays comparable with development runs.

## 2. Wording corrected after an external review (2026-09-30)

An external review checked the claims against the code. All points below were verified.

1. **What the guarantee says.** The HTML audit report and the methods note said "at least 1 − δ of
   *issued* certificates meet the target". The procedure guarantees that the probability of issuing
   an unsafe certificate, over audit draws including those that issue nothing, is at most δ. These
   differ when certificates are rare (screening, B = 800: 2.5% of all draws vs 7.6% of issued
   certificates violate). Both texts are corrected (`src/ldj/report.py`, `docs/methods.md`).
2. **The confirmatory guarantee criterion (H3) is weak.** "Clopper–Pearson lower end ≤ δ" only
   shows that excess violations were not detected. The pre-registered calculation is kept, but a
   pass is now labeled "not contradicted by this test", never "guarantee supported". H3 failed that
   criterion, so its verdict is unchanged (now worded "not supported: excess violations detected").
3. **Screening stopping.** "Certified stopping holds under active learning" overstated it: the
   stopping test is applied repeatedly over many windows, a multiple-testing issue its source paper
   leaves open. Supported: every tested active-learning run met 95% recall.
4. **Screening labels.** The loader uses abstract-stage inclusion for 11 of 15 reviews (including
   Moran_2020, the one that certifies) and final inclusion for 4. Statements that all screening
   labels were final inclusions are corrected.
5. **TwinRouterBench outcomes are simulated from tiers.** The dataset gives each prompt only its
   cheapest sufficient tier; a tier "succeeds" if and only if it is at or above it. So the top tier
   is right on every prompt by construction, and the escalation cells (0 "only cheap right", 0
   "both wrong") are artifacts. The TwinRouterBench results are kept but are not paired-execution
   evidence like LLMRouterBench's. Its 7 inconsistent cells were then examined with known-truth
   simulations (`results/sim_violations/summary.md`).
