# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features_judge | certified | 0.10 | 67 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.10 | 134 | 500 | 0.440 | 0.251 | 0.000 / 0.000 / 0.634 | 0.134 [0.105, 0.167] | 0.305 | False |
| gemma_features_judge | certified | 0.10 | 267 | 500 | 0.880 | 0.521 | 0.000 / 0.579 / 0.736 | 0.310 [0.270, 0.353] | 0.352 | False |
| gemma_features_judge | certified | 0.25 | 67 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| gemma_features_judge | certified | 0.25 | 134 | 500 | 0.294 | 0.199 | 0.000 / 0.000 / 0.698 | 0.154 [0.123, 0.189] | 0.524 | False |
| gemma_features_judge | certified | 0.25 | 267 | 500 | 0.944 | 0.578 | 0.389 / 0.609 / 0.762 | 0.286 [0.247, 0.328] | 0.303 | False |
| gemma_features_judge | certified | 0.50 | 67 | 500 | 0.004 | 0.004 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| gemma_features_judge | certified | 0.50 | 134 | 500 | 0.012 | 0.011 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 1.000 | True |
| gemma_features_judge | certified | 0.50 | 267 | 500 | 0.836 | 0.510 | 0.000 / 0.573 / 0.763 | 0.202 [0.168, 0.240] | 0.242 | False |
| gemma_features_judge | certified | 0.75 | 67 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 134 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| gemma_features_judge | certified | 0.75 | 267 | 500 | 0.022 | 0.021 | 0.000 / 0.000 / 0.000 | 0.022 [0.011, 0.039] | 1.000 | True |
| gemma_features_judge | heuristic | 1.00 | 67 | 500 | 0.434 | 0.412 | 0.000 / 0.000 / 1.000 | 0.434 [0.390, 0.479] | 1.000 | False |
| gemma_features_judge | heuristic | 1.00 | 134 | 500 | 1.000 | 0.850 | 0.708 / 0.864 / 0.990 | 0.892 [0.861, 0.918] | 0.892 | False |
| gemma_features_judge | heuristic | 1.00 | 267 | 500 | 1.000 | 0.859 | 0.760 / 0.864 / 0.953 | 0.934 [0.909, 0.954] | 0.934 | False |
| gemma_judge_0shot | certified | 0.00 | 67 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_judge_0shot | certified | 0.00 | 134 | 500 | 0.082 | 0.041 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.073 | True |
| gemma_judge_0shot | certified | 0.00 | 267 | 500 | 0.238 | 0.088 | 0.000 / 0.000 / 0.333 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 67 | 500 | 0.012 | 0.011 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 1.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 134 | 500 | 0.742 | 0.381 | 0.000 / 0.490 / 0.606 | 0.156 [0.125, 0.191] | 0.210 | False |
| gemma_judge_0shot | heuristic | 1.00 | 267 | 500 | 0.940 | 0.448 | 0.333 / 0.490 / 0.490 | 0.054 [0.036, 0.078] | 0.057 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 67: gemma_features_judge at f = 0.50, 0.004
- B = 134: gemma_judge_0shot at f = 0.00, 0.041
- B = 267: gemma_judge_0shot at f = 0.00, 0.088

B* (smallest B where the best arm fits, f > 0): 67
