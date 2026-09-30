# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 200 | 500 | 0.108 | 0.041 | 0.000 / 0.000 / 0.317 | 0.020 [0.010, 0.036] | 0.185 | True |
| bgeL_logreg | certified | 0.10 | 400 | 500 | 0.674 | 0.208 | 0.000 / 0.223 / 0.426 | 0.006 [0.001, 0.017] | 0.009 | True |
| bgeL_logreg | certified | 0.10 | 800 | 500 | 0.936 | 0.388 | 0.201 / 0.426 / 0.510 | 0.016 [0.007, 0.031] | 0.017 | True |
| bgeL_logreg | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 200 | 500 | 0.100 | 0.045 | 0.000 / 0.000 / 0.037 | 0.018 [0.008, 0.034] | 0.180 | True |
| bgeL_logreg | certified | 0.25 | 400 | 500 | 0.800 | 0.285 | 0.000 / 0.322 / 0.475 | 0.016 [0.007, 0.031] | 0.020 | True |
| bgeL_logreg | certified | 0.25 | 800 | 500 | 0.982 | 0.462 | 0.377 / 0.476 / 0.555 | 0.012 [0.004, 0.026] | 0.012 | True |
| bgeL_logreg | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 200 | 500 | 0.018 | 0.011 | 0.000 / 0.000 / 0.000 | 0.016 [0.007, 0.031] | 0.889 | True |
| bgeL_logreg | certified | 0.50 | 400 | 500 | 0.636 | 0.257 | 0.000 / 0.327 / 0.499 | 0.012 [0.004, 0.026] | 0.019 | True |
| bgeL_logreg | certified | 0.50 | 800 | 500 | 0.984 | 0.468 | 0.358 / 0.481 / 0.576 | 0.020 [0.010, 0.036] | 0.020 | True |
| bgeL_logreg | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 400 | 500 | 0.042 | 0.026 | 0.000 / 0.000 / 0.000 | 0.010 [0.003, 0.023] | 0.238 | True |
| bgeL_logreg | certified | 0.75 | 800 | 500 | 0.814 | 0.344 | 0.000 / 0.381 / 0.540 | 0.014 [0.006, 0.029] | 0.017 | True |
| bgeL_logreg | heuristic | 1.00 | 25 | 500 | 0.012 | 0.012 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 50 | 500 | 0.012 | 0.012 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 100 | 500 | 0.270 | 0.194 | 0.000 / 0.000 / 0.744 | 0.254 [0.216, 0.295] | 0.941 | False |
| bgeL_logreg | heuristic | 1.00 | 200 | 500 | 0.862 | 0.496 | 0.000 / 0.544 / 0.727 | 0.320 [0.279, 0.363] | 0.371 | False |
| bgeL_logreg | heuristic | 1.00 | 400 | 500 | 0.998 | 0.610 | 0.507 / 0.606 / 0.726 | 0.348 [0.306, 0.392] | 0.349 | False |
| bgeL_logreg | heuristic | 1.00 | 800 | 500 | 1.000 | 0.641 | 0.551 / 0.640 / 0.743 | 0.282 [0.243, 0.324] | 0.282 | False |
| gemma_features_judge | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 100 | 500 | 0.016 | 0.011 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 0.500 | True |
| gemma_features_judge | certified | 0.10 | 200 | 500 | 0.666 | 0.325 | 0.000 / 0.420 / 0.596 | 0.016 [0.007, 0.031] | 0.024 | True |
| gemma_features_judge | certified | 0.10 | 400 | 500 | 0.912 | 0.509 | 0.188 / 0.570 / 0.663 | 0.024 [0.012, 0.042] | 0.026 | True |
| gemma_features_judge | certified | 0.10 | 800 | 500 | 0.970 | 0.616 | 0.543 / 0.654 / 0.724 | 0.016 [0.007, 0.031] | 0.016 | True |
| gemma_features_judge | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 100 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| gemma_features_judge | certified | 0.25 | 200 | 500 | 0.748 | 0.393 | 0.000 / 0.470 / 0.632 | 0.024 [0.012, 0.042] | 0.032 | True |
| gemma_features_judge | certified | 0.25 | 400 | 500 | 0.938 | 0.574 | 0.438 / 0.609 / 0.723 | 0.028 [0.015, 0.047] | 0.030 | True |
| gemma_features_judge | certified | 0.25 | 800 | 500 | 0.926 | 0.630 | 0.581 / 0.685 / 0.750 | 0.010 [0.003, 0.023] | 0.011 | True |
| gemma_features_judge | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 200 | 500 | 0.276 | 0.181 | 0.000 / 0.000 / 0.660 | 0.018 [0.008, 0.034] | 0.065 | True |
| gemma_features_judge | certified | 0.50 | 400 | 500 | 0.884 | 0.536 | 0.000 / 0.599 / 0.719 | 0.016 [0.007, 0.031] | 0.018 | True |
| gemma_features_judge | certified | 0.50 | 800 | 500 | 0.984 | 0.678 | 0.610 / 0.698 / 0.765 | 0.014 [0.006, 0.029] | 0.014 | True |
| gemma_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 400 | 500 | 0.380 | 0.252 | 0.000 / 0.000 / 0.698 | 0.016 [0.007, 0.031] | 0.042 | True |
| gemma_features_judge | certified | 0.75 | 800 | 500 | 0.900 | 0.583 | 0.244 / 0.645 / 0.754 | 0.026 [0.014, 0.044] | 0.029 | True |
| gemma_features_judge | heuristic | 1.00 | 25 | 500 | 0.064 | 0.064 | 0.000 / 0.000 / 0.000 | 0.064 [0.044, 0.089] | 1.000 | True |
| gemma_features_judge | heuristic | 1.00 | 50 | 500 | 0.066 | 0.066 | 0.000 / 0.000 / 0.000 | 0.066 [0.046, 0.091] | 1.000 | True |
| gemma_features_judge | heuristic | 1.00 | 100 | 500 | 0.930 | 0.713 | 0.596 / 0.754 / 0.894 | 0.462 [0.418, 0.507] | 0.497 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.771 | 0.668 / 0.777 / 0.869 | 0.424 [0.380, 0.469] | 0.424 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.793 | 0.721 / 0.795 / 0.867 | 0.366 [0.324, 0.410] | 0.366 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.808 | 0.766 / 0.808 / 0.851 | 0.334 [0.293, 0.377] | 0.334 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 100: gemma_features_judge at f = 0.10, 0.011
- B = 200: gemma_features_judge at f = 0.25, 0.393
- B = 400: gemma_features_judge at f = 0.25, 0.574
- B = 800: gemma_features_judge at f = 0.50, 0.678

B* (smallest B where the best arm fits, f > 0): 100
