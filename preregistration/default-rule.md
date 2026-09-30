# Frozen default rule (plan v3, W3 → tested in W5)

Frozen 2026-09-30, before any W5 data exists. Written from **development evidence only**: the
X4 runs on T0, T1, T2 (`notes/results.md`), which have been seen. It is therefore a hypothesis to
test, not a result. W5 tests it unchanged on untouched data under a pre-registration; any later
change is a new rule, logged as a deviation.

## The rule

For a binary decision (accept / classify) with a selective-risk target α and δ = 0.05:

1. **Method:** question features plus the zero-shot judge's probability, under one logistic head
   (`questions_judge`). Fixed questions and prompt, frozen before any label is seen.
2. **Label budget:** do not attempt certification below **B = 200** labels. Below it, report
   "insufficient evidence expected" and state the number needed.
3. **Split:** fit on **25%** of B when B ≤ 400; on **50%** when B ≥ 800 (linear share in between is
   not used: take the nearer of the two). The rest is a random certification sample, never used for
   fitting or for choosing anything.
4. **Labels:** prefer consensus labels (≥ 3 annotations) for the certification sample. One
   annotator's labels keep the guarantee but automate about half as much (T1).
5. **Certificate:** Clopper–Pearson with fixed-sequence testing over a grid built from unlabeled
   deploy scores (`ldj.certify`, grid start 2× the zero-error minimum). Report the unconditional
   guarantee, the share of draws expected to give a useful certificate, and the automation spread.

For screening with a recall target: use a random certification sample only if its **expected
number of positives is ≥ 70** (prevalence × certification-sample size); otherwise recommend a
certified-stopping workflow (W7) instead. When used: fit on 10% of B.

## Development evidence behind each choice (seen data)

| Choice | Evidence |
|---|---|
| Features + judge | T1: best certified arm at every B ≥ 200 (B = 400, f = 0.25: 57.4% automated, useful in 94% of draws, vs features 49.2% / 86%). T2: ties features. |
| B ≥ 200 | T1: nothing useful below 200 for any arm (B = 100 best 1.1%); ledger break-even ~1,500–2,100 items at B = 200–400. |
| f = 0.25 / 0.50 | T1: best share 0.25 at B = 200–400, 0.50 at B = 800 (features + judge and features alike). |
| Consensus labels | T1 single-annotator run: same draws, about half the automation, still valid; better per annotation action too (consensus B = 200, 600 actions, saved 23.5% of checks at 10k items vs 14.9% for one annotator at B = 400). |
| ≥ 70 positives (screening) | T2: the only review that certified had ~70 positives in its certification sample; reviews with 4–14 never did. 59 is the zero-miss minimum at 95% / 95%. |

## What it does not claim

- Nothing about T0-like tasks: on routing, no arm certified meaningful automation (text methods
  only; Jev features not tested).
- Nothing about domains beyond comment moderation for the numbers above; W5 tests the same source.
- The best-arm choices above were read off test-scored frontiers; that is why they must be tested
  on untouched data before being recommended.

## Erratum (2026-09-30, after freezing; the rule itself is unchanged)

The evidence row for **"Consensus labels"** was wrong: it counted a consensus label as 3
annotation actions, but it is built from 5.66 on average. Per label, consensus still certifies
about twice as much as one annotator; **per annotation action, one annotator is slightly cheaper**
at these budgets (20.5% vs 18.1% of checks saved at 10k items). Item 4 is therefore supported per
label but not per unit of annotation cost. W5 uses consensus labels as pre-registered, so it is
unaffected; the rule text is not edited after freezing.
