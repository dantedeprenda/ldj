# T2 by review (review = unit of inference)

Best (method, f) per target and B by mean automation over eligible reviews (descriptive).
`reviews certifying` = reviews where most resamples give a useful certificate.

| target | B | method | f | eligible reviews | reviews certifying | mean automation [95% CI over reviews] | worst per-review violation |
|---|---|---|---|---|---|---|---|
| recall 0.90 | 25 | bge_logreg | 0.10 | 14 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.90 | 50 | bge_logreg | 0.10 | 13 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.90 | 100 | bge_logreg | 0.10 | 11 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.90 | 200 | gemma_judge_0shot | 0.00 | 8 | 0 | 0.001 [0.000, 0.002] | 0.000 |
| recall 0.90 | 400 | gemma_features | 0.10 | 6 | 1 | 0.098 [0.000, 0.253] | 0.074 |
| recall 0.90 | 800 | gemma_features | 0.25 | 3 | 1 | 0.195 [0.000, 0.584] | 0.058 |
| recall 0.95 | 25 | bgeL_logreg | 0.10 | 14 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.95 | 50 | bgeL_logreg | 0.10 | 13 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.95 | 100 | bgeL_logreg | 0.10 | 11 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.95 | 200 | bgeL_logreg | 0.10 | 8 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.95 | 400 | bgeL_logreg | 0.10 | 6 | 0 | 0.000 [0.000, 0.000] | 0.000 |
| recall 0.95 | 800 | gemma_features | 0.10 | 3 | 1 | 0.161 [0.000, 0.484] | 0.076 |
