# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.10 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.10 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.10 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.10 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.10 | 800 | 1500 | 0.329 | 0.063 | 0.000 / 0.000 / 0.248 | 0.054 [0.043, 0.067] | 0.164 | True |
| bgeL_logreg | certified | 0.25 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.25 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.25 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.25 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.25 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.25 | 800 | 1500 | 0.161 | 0.039 | 0.000 / 0.000 / 0.197 | 0.029 [0.021, 0.039] | 0.183 | True |
| bgeL_logreg | certified | 0.50 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.50 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.50 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.50 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.50 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.50 | 800 | 1500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.002] | - | True |
| bgeL_logreg | certified | 0.75 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.75 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.75 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.75 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.75 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| bgeL_logreg | certified | 0.75 | 800 | 1500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.002] | - | True |
| bgeL_logreg | heuristic | 1.00 | 25 | 7000 | 0.227 | 0.165 | 0.000 / 0.000 / 0.806 | 0.196 [0.187, 0.206] | 0.864 | False |
| bgeL_logreg | heuristic | 1.00 | 50 | 6500 | 0.407 | 0.277 | 0.000 / 0.000 / 0.900 | 0.320 [0.309, 0.331] | 0.785 | False |
| bgeL_logreg | heuristic | 1.00 | 100 | 5500 | 0.551 | 0.321 | 0.000 / 0.088 / 0.885 | 0.359 [0.346, 0.372] | 0.651 | False |
| bgeL_logreg | heuristic | 1.00 | 200 | 4000 | 0.667 | 0.397 | 0.000 / 0.361 / 0.969 | 0.458 [0.442, 0.474] | 0.686 | False |
| bgeL_logreg | heuristic | 1.00 | 400 | 3000 | 0.797 | 0.493 | 0.000 / 0.569 / 0.914 | 0.528 [0.510, 0.546] | 0.663 | False |
| bgeL_logreg | heuristic | 1.00 | 800 | 1500 | 0.723 | 0.328 | 0.000 / 0.355 / 0.677 | 0.397 [0.372, 0.423] | 0.549 | False |
| gemma_features_judge | certified | 0.10 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.10 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.10 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.10 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.10 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.10 | 800 | 1500 | 0.332 | 0.161 | 0.000 / 0.000 / 0.524 | 0.025 [0.017, 0.034] | 0.074 | True |
| gemma_features_judge | certified | 0.25 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.25 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.25 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.25 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.25 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.25 | 800 | 1500 | 0.161 | 0.082 | 0.000 / 0.000 / 0.498 | 0.009 [0.005, 0.015] | 0.054 | True |
| gemma_features_judge | certified | 0.50 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.50 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.50 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.50 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.50 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.50 | 800 | 1500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.002] | - | True |
| gemma_features_judge | certified | 0.75 | 25 | 7000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.75 | 50 | 6500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.75 | 100 | 5500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.75 | 200 | 4000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.75 | 400 | 3000 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.001] | - | True |
| gemma_features_judge | certified | 0.75 | 800 | 1500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.002] | - | True |
| gemma_features_judge | heuristic | 1.00 | 25 | 7000 | 0.543 | 0.364 | 0.000 / 0.312 / 0.830 | 0.351 [0.340, 0.362] | 0.646 | False |
| gemma_features_judge | heuristic | 1.00 | 50 | 6500 | 0.706 | 0.465 | 0.000 / 0.574 / 0.873 | 0.385 [0.373, 0.397] | 0.545 | False |
| gemma_features_judge | heuristic | 1.00 | 100 | 5500 | 0.786 | 0.512 | 0.000 / 0.596 / 0.897 | 0.438 [0.425, 0.452] | 0.558 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 4000 | 0.837 | 0.571 | 0.000 / 0.677 / 0.927 | 0.576 [0.561, 0.592] | 0.689 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 3000 | 0.963 | 0.673 | 0.051 / 0.828 / 0.918 | 0.580 [0.562, 0.598] | 0.602 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 1500 | 0.945 | 0.528 | 0.001 / 0.648 / 0.854 | 0.339 [0.315, 0.363] | 0.359 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 800: gemma_features_judge at f = 0.10, 0.161

B* (smallest B where the best arm fits, f > 0): 800
