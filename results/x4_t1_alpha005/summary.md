# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 400 | 500 | 0.024 | 0.008 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 0.083 | True |
| bgeL_logreg | certified | 0.10 | 800 | 500 | 0.624 | 0.155 | 0.000 / 0.181 / 0.308 | 0.012 [0.004, 0.026] | 0.019 | True |
| bgeL_logreg | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 400 | 500 | 0.012 | 0.005 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 0.167 | True |
| bgeL_logreg | certified | 0.25 | 800 | 500 | 0.742 | 0.211 | 0.000 / 0.243 / 0.357 | 0.002 [0.000, 0.011] | 0.003 | True |
| bgeL_logreg | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 400 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 800 | 500 | 0.392 | 0.132 | 0.000 / 0.000 / 0.359 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 400 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 800 | 500 | 0.002 | 0.001 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 25 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | heuristic | 1.00 | 100 | 500 | 0.006 | 0.006 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 200 | 500 | 0.086 | 0.055 | 0.000 / 0.000 / 0.000 | 0.086 [0.063, 0.114] | 1.000 | False |
| bgeL_logreg | heuristic | 1.00 | 400 | 500 | 0.840 | 0.370 | 0.000 / 0.416 / 0.546 | 0.298 [0.258, 0.340] | 0.355 | False |
| bgeL_logreg | heuristic | 1.00 | 800 | 500 | 0.996 | 0.431 | 0.298 / 0.446 / 0.541 | 0.242 [0.205, 0.282] | 0.243 | False |
| gemma_features_judge | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 400 | 500 | 0.568 | 0.237 | 0.000 / 0.341 / 0.477 | 0.016 [0.007, 0.031] | 0.028 | True |
| gemma_features_judge | certified | 0.10 | 800 | 500 | 0.850 | 0.387 | 0.000 / 0.467 / 0.549 | 0.020 [0.010, 0.036] | 0.024 | True |
| gemma_features_judge | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 400 | 500 | 0.532 | 0.247 | 0.000 / 0.385 / 0.515 | 0.024 [0.012, 0.042] | 0.045 | True |
| gemma_features_judge | certified | 0.25 | 800 | 500 | 0.810 | 0.381 | 0.000 / 0.486 / 0.568 | 0.030 [0.017, 0.049] | 0.037 | True |
| gemma_features_judge | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 400 | 500 | 0.040 | 0.025 | 0.000 / 0.000 / 0.000 | 0.014 [0.006, 0.029] | 0.350 | True |
| gemma_features_judge | certified | 0.50 | 800 | 500 | 0.680 | 0.332 | 0.000 / 0.448 / 0.566 | 0.030 [0.017, 0.049] | 0.044 | True |
| gemma_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 400 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 800 | 500 | 0.074 | 0.046 | 0.000 / 0.000 / 0.000 | 0.026 [0.014, 0.044] | 0.351 | True |
| gemma_features_judge | heuristic | 1.00 | 25 | 500 | 0.010 | 0.010 | 0.000 / 0.000 / 0.000 | 0.010 [0.003, 0.023] | 1.000 | True |
| gemma_features_judge | heuristic | 1.00 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | heuristic | 1.00 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 500 | 0.568 | 0.373 | 0.000 / 0.604 / 0.696 | 0.434 [0.390, 0.479] | 0.764 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.618 | 0.544 / 0.617 / 0.697 | 0.494 [0.449, 0.539] | 0.494 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.632 | 0.575 / 0.635 / 0.682 | 0.504 [0.459, 0.549] | 0.504 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 400: gemma_features_judge at f = 0.25, 0.247
- B = 800: gemma_features_judge at f = 0.10, 0.387

B* (smallest B where the best arm fits, f > 0): 400
