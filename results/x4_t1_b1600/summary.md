# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 1600 | 500 | 0.986 | 0.489 | 0.431 / 0.502 / 0.556 | 0.010 [0.003, 0.023] | 0.010 | True |
| bgeL_logreg | certified | 0.25 | 1600 | 500 | 0.992 | 0.538 | 0.492 / 0.548 / 0.594 | 0.006 [0.001, 0.017] | 0.006 | True |
| bgeL_logreg | certified | 0.50 | 1600 | 500 | 0.998 | 0.556 | 0.493 / 0.559 / 0.620 | 0.006 [0.001, 0.017] | 0.006 | True |
| bgeL_logreg | certified | 0.75 | 1600 | 500 | 0.996 | 0.519 | 0.407 / 0.527 / 0.617 | 0.008 [0.002, 0.020] | 0.008 | True |
| bgeL_logreg | heuristic | 1.00 | 1600 | 500 | 1.000 | 0.671 | 0.613 / 0.669 / 0.727 | 0.096 [0.072, 0.125] | 0.096 | False |
| gemma_features_judge | certified | 0.10 | 1600 | 500 | 0.992 | 0.703 | 0.659 / 0.711 / 0.754 | 0.006 [0.001, 0.017] | 0.006 | True |
| gemma_features_judge | certified | 0.25 | 1600 | 500 | 1.000 | 0.737 | 0.697 / 0.738 / 0.778 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 1600 | 500 | 0.994 | 0.735 | 0.694 / 0.739 / 0.785 | 0.012 [0.004, 0.026] | 0.012 | True |
| gemma_features_judge | certified | 0.75 | 1600 | 500 | 0.994 | 0.706 | 0.641 / 0.712 / 0.778 | 0.018 [0.008, 0.034] | 0.018 | True |
| gemma_features_judge | heuristic | 1.00 | 1600 | 500 | 1.000 | 0.814 | 0.785 / 0.815 / 0.840 | 0.264 [0.226, 0.305] | 0.264 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 1600: gemma_features_judge at f = 0.25, 0.737

B* (smallest B where the best arm fits, f > 0): 1600
