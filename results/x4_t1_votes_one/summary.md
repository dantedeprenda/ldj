# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features_judge | certified | 0.10 | 200 | 500 | 0.338 | 0.154 | 0.000 / 0.000 / 0.509 | 0.024 [0.012, 0.042] | 0.071 | True |
| gemma_features_judge | certified | 0.10 | 400 | 500 | 0.640 | 0.277 | 0.000 / 0.283 / 0.577 | 0.030 [0.017, 0.049] | 0.047 | True |
| gemma_features_judge | certified | 0.10 | 800 | 500 | 0.736 | 0.362 | 0.000 / 0.510 / 0.608 | 0.036 [0.021, 0.056] | 0.049 | True |
| gemma_features_judge | certified | 0.25 | 200 | 500 | 0.374 | 0.181 | 0.000 / 0.000 / 0.523 | 0.028 [0.015, 0.047] | 0.075 | True |
| gemma_features_judge | certified | 0.25 | 400 | 500 | 0.628 | 0.284 | 0.000 / 0.292 / 0.573 | 0.020 [0.010, 0.036] | 0.032 | True |
| gemma_features_judge | certified | 0.25 | 800 | 500 | 0.798 | 0.404 | 0.000 / 0.520 / 0.634 | 0.028 [0.015, 0.047] | 0.035 | True |
| gemma_features_judge | certified | 0.50 | 200 | 500 | 0.088 | 0.056 | 0.000 / 0.000 / 0.000 | 0.016 [0.007, 0.031] | 0.182 | True |
| gemma_features_judge | certified | 0.50 | 400 | 500 | 0.568 | 0.255 | 0.000 / 0.311 / 0.568 | 0.010 [0.003, 0.023] | 0.018 | True |
| gemma_features_judge | certified | 0.50 | 800 | 500 | 0.792 | 0.418 | 0.000 / 0.510 / 0.642 | 0.018 [0.008, 0.034] | 0.023 | True |
| gemma_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 400 | 500 | 0.086 | 0.054 | 0.000 / 0.000 / 0.000 | 0.014 [0.006, 0.029] | 0.163 | True |
| gemma_features_judge | certified | 0.75 | 800 | 500 | 0.624 | 0.307 | 0.000 / 0.391 / 0.612 | 0.026 [0.014, 0.044] | 0.042 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 500 | 0.996 | 0.670 | 0.514 / 0.677 / 0.815 | 0.432 [0.388, 0.477] | 0.434 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.684 | 0.581 / 0.688 / 0.786 | 0.406 [0.363, 0.450] | 0.406 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.701 | 0.642 / 0.701 / 0.758 | 0.342 [0.300, 0.385] | 0.342 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 500 | 0.026 | 0.009 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 500 | 0.058 | 0.019 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 500 | 0.062 | 0.020 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 500 | 0.698 | 0.291 | 0.000 / 0.333 / 0.490 | 0.016 [0.007, 0.031] | 0.023 | True |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 500 | 0.688 | 0.268 | 0.000 / 0.333 / 0.490 | 0.002 [0.000, 0.011] | 0.003 | True |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 500 | 0.738 | 0.268 | 0.000 / 0.333 / 0.490 | 0.000 [0.000, 0.007] | 0.000 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.181
- B = 400: gemma_features_judge at f = 0.25, 0.284
- B = 800: gemma_features_judge at f = 0.50, 0.418

B* (smallest B where the best arm fits, f > 0): 200
