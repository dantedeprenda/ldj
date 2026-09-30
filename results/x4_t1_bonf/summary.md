# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 400 | 500 | 0.200 | 0.055 | 0.000 / 0.000 / 0.268 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.10 | 800 | 500 | 0.862 | 0.278 | 0.000 / 0.312 / 0.417 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 400 | 500 | 0.216 | 0.068 | 0.000 / 0.000 / 0.318 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.25 | 800 | 500 | 0.952 | 0.345 | 0.233 / 0.360 / 0.457 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 400 | 500 | 0.072 | 0.027 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.50 | 800 | 500 | 0.874 | 0.300 | 0.000 / 0.329 / 0.448 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 400 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 800 | 500 | 0.142 | 0.058 | 0.000 / 0.000 / 0.361 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | heuristic | 1.00 | 25 | 500 | 0.012 | 0.012 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 50 | 500 | 0.012 | 0.012 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 100 | 500 | 0.270 | 0.194 | 0.000 / 0.000 / 0.744 | 0.254 [0.216, 0.295] | 0.941 | False |
| bgeL_logreg | heuristic | 1.00 | 200 | 500 | 0.862 | 0.496 | 0.000 / 0.544 / 0.727 | 0.320 [0.279, 0.363] | 0.371 | False |
| bgeL_logreg | heuristic | 1.00 | 400 | 500 | 0.998 | 0.610 | 0.507 / 0.606 / 0.726 | 0.348 [0.306, 0.392] | 0.349 | False |
| bgeL_logreg | heuristic | 1.00 | 800 | 500 | 1.000 | 0.641 | 0.551 / 0.640 / 0.743 | 0.282 [0.243, 0.324] | 0.282 | False |
| gemma_features_judge | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 200 | 500 | 0.202 | 0.088 | 0.000 / 0.000 / 0.424 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.10 | 400 | 500 | 0.840 | 0.394 | 0.000 / 0.455 / 0.564 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.10 | 800 | 500 | 0.998 | 0.577 | 0.496 / 0.586 / 0.655 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.25 | 200 | 500 | 0.122 | 0.060 | 0.000 / 0.000 / 0.428 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 400 | 500 | 0.850 | 0.423 | 0.000 / 0.483 / 0.601 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 800 | 500 | 1.000 | 0.607 | 0.538 / 0.608 / 0.678 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.50 | 200 | 500 | 0.012 | 0.008 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 400 | 500 | 0.544 | 0.270 | 0.000 / 0.372 / 0.580 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 800 | 500 | 0.990 | 0.575 | 0.489 / 0.583 / 0.674 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 400 | 500 | 0.018 | 0.012 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.75 | 800 | 500 | 0.622 | 0.329 | 0.000 / 0.467 / 0.613 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | heuristic | 1.00 | 25 | 500 | 0.064 | 0.064 | 0.000 / 0.000 / 0.000 | 0.064 [0.044, 0.089] | 1.000 | True |
| gemma_features_judge | heuristic | 1.00 | 50 | 500 | 0.066 | 0.066 | 0.000 / 0.000 / 0.000 | 0.066 [0.046, 0.091] | 1.000 | True |
| gemma_features_judge | heuristic | 1.00 | 100 | 500 | 0.930 | 0.713 | 0.596 / 0.754 / 0.894 | 0.462 [0.418, 0.507] | 0.497 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.771 | 0.668 / 0.777 / 0.869 | 0.424 [0.380, 0.469] | 0.424 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.793 | 0.721 / 0.795 / 0.867 | 0.366 [0.324, 0.410] | 0.366 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.808 | 0.766 / 0.808 / 0.851 | 0.334 [0.293, 0.377] | 0.334 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.10, 0.088
- B = 400: gemma_features_judge at f = 0.25, 0.423
- B = 800: gemma_features_judge at f = 0.25, 0.607

B* (smallest B where the best arm fits, f > 0): 200
