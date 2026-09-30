# Deviations from the pre-registrations

## 1. T2 restarted after an embedding memory leak (2026-09-28, 14:25 CEST)

**What happened.** The first T2 run loaded a fresh copy of bge-large for every review (15 copies)
and did not free the old ones from GPU memory. After about 50 minutes the machine (16 GB) had
filled its 10 GB swap, and embedding had slowed to about 4 reviews per hour.

**What we changed.** The embedding store now reuses one encoder (`ldj/methods/text.py`) and T2
was restarted from the start. The first attempt's log is `logs/t2_attempt1.log`.

**Effect on results.** None expected. The method, settings, data, seeds and questions are
unchanged, and the embeddings the first attempt had already written were reused from the cache.
The restarted run reproduced all 130 cells the first attempt had finished, identically (checked with a diff of the two logs).

**T1 is unaffected.** It embeds a single task, so it loads each encoder once.

## 2. Blind audits labeled by Claude, pending the author's check (2026-09-29)

**What happened.** The pre-registrations say the author hand-audits 200 test items per task. At
the author's request, Claude (Opus 5.5) labeled both sheets instead, and the author will check the
labels. Claude saw only the sheet: the text and, for T2, the review's question and criteria. It saw
no gold label and no method score before all 400 rows were labeled and saved. The labels are kept
apart from the author's column, in `data/audit/<task>_audit_claude.csv`, with a note on every
borderline call. They are scored with `scripts/audit.py score <task> claude`.

**Why it matters.** The audit is meant to be an independent human check on label noise. An LLM
auditor is not independent of the LLM methods under test (Gemma judge, question features), so its
disagreements with the gold may be correlated with the methods' errors. The labels become
human-verified only once the author has checked them. Until then, the sensitivity rerun that
removes disagreements is reported as provisional, or not at all.

**Checked 2026-09-29.** The author checked every label, filled the two T1 rows Claude could not
call (both 0), and found no others to change. The labels were then copied into the pre-registered
sheets (`data/audit/<task>_audit.csv`, notes marked "Claude, checked by author"). The sensitivity
rerun is in `notes/results.md`; all six hypotheses still hold.

**Result (before the check; T1 is 78.5% after the two fills).**
- T1: 198 labeled (2 can't tell), 78.3% agreement, 43 disagreements. 31 of the 43 are Claude
  "hate speech" where the gold is not, mostly gendered slurs aimed at one person. 20 of the 43 are
  among the 40 rows Claude flagged as borderline. This is close to the 79% agreement of a single
  MHS annotator with the consensus (`notes/plan.md`, Phase 2).
- T2: 200 labeled, 92.0% agreement, 16 disagreements. 11 are Claude "include" where the gold
  excludes. That is expected at title/abstract stage, since, for 4 of the 15 reviews, the labels are final inclusions (the other 11 use abstract-stage labels; corrected 2026-09-30).
  5 are gold includes that Claude excluded: those are the misses that matter for recall.

## 3. Blind question set generated before its prompt was committed (2026-09-30)

**What happened.** The plan was to commit and push `scripts/blind_questions.py` (which holds the
generation prompt verbatim) before running it. The commit was chained after a lint check that
failed, so nothing was committed, and the generation was run in a separate call about a minute
later. The prompt text is exactly as written before the run; the lint fixes that followed changed
only an unused import, a regex flag alias and a variable name.

**Effect.** The generator saw only the task description (no data), so no information could leak
into the questions. What is lost is the independent timestamp showing the prompt predates the
questions. The set is used for W4 as exploratory work, labeled with this deviation.

**Also.** The script reported $0.0000 because the backend was created without Claude's prices;
the real cost of the single call was about one cent.
