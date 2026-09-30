# T0 ledger: routing cost vs quality (exploratory)

Always-cheap: $0.00112/prompt, accuracy 0.742. Always-strong: $0.02508/prompt, accuracy 0.807. A label = one cheap-model run ($0.00117), graded automatically. Policy accuracy approximates deferred prompts at the strong model's overall accuracy. **A cost-quality trade, not a free saving.** Best certified cell per (method, B) by savings at 10k prompts; picked after seeing results.

| method | f | B | automated | $/prompt | accuracy (approx., optimistic) | saved vs always-strong @10k | @100k | P(saves) @10k |
|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | 0.10 | 100 | 0.000 | 0.02508 | 0.807 | $-0.12 | $-0.12 | 0% |
| bgeL_logreg | 0.25 | 200 | 0.004 | 0.02499 | 0.807 | $+0.71 | $+9.21 | 1% |
| bgeL_logreg | 0.50 | 400 | 0.005 | 0.02495 | 0.807 | $+0.80 | $+12.20 | 2% |
| bgeL_logreg | 0.75 | 800 | 0.010 | 0.02484 | 0.808 | $+1.44 | $+22.80 | 3% |
| bge_logreg | 0.10 | 100 | 0.000 | 0.02508 | 0.807 | $-0.12 | $-0.12 | 0% |
| bge_logreg | 0.25 | 200 | 0.005 | 0.02495 | 0.807 | $+1.08 | $+12.90 | 1% |
| bge_logreg | 0.50 | 400 | 0.008 | 0.02489 | 0.808 | $+1.44 | $+18.58 | 3% |
| bge_logreg | 0.75 | 800 | 0.010 | 0.02484 | 0.808 | $+1.45 | $+22.92 | 3% |
| category_prior | 0.10 | 100 | 0.004 | 0.02498 | 0.807 | $+0.87 | $+9.79 | 1% |
| category_prior | 0.50 | 200 | 0.004 | 0.02498 | 0.807 | $+0.75 | $+9.63 | 1% |
| category_prior | 0.75 | 400 | 0.008 | 0.02488 | 0.808 | $+1.51 | $+19.30 | 1% |
| category_prior | 0.10 | 800 | 0.000 | 0.02508 | 0.807 | $-0.94 | $-0.94 | 0% |
| jev_features | 0.25 | 100 | 0.013 | 0.02481 | 0.808 | $+2.58 | $+26.81 | 2% |
| jev_features | 0.50 | 200 | 0.071 | 0.02343 | 0.813 | $+16.28 | $+164.89 | 13% |
| jev_features | 0.25 | 400 | 0.158 | 0.02134 | 0.824 | $+36.94 | $+373.59 | 42% |
| jev_features | 0.25 | 800 | 0.273 | 0.01860 | 0.834 | $+63.92 | $+647.63 | 66% |
| tfidf_logreg | 0.10 | 100 | 0.001 | 0.02506 | 0.807 | $+0.14 | $+2.46 | 0% |
| tfidf_logreg | 0.25 | 200 | 0.003 | 0.02501 | 0.807 | $+0.53 | $+7.39 | 1% |
| tfidf_logreg | 0.75 | 400 | 0.006 | 0.02494 | 0.807 | $+0.92 | $+13.45 | 1% |
| tfidf_logreg | 0.75 | 800 | 0.013 | 0.02477 | 0.808 | $+2.21 | $+30.48 | 4% |
