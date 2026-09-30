# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_judge_0shot_s5 | certified | 0.00 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_judge_0shot_s5 | certified | 0.00 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_judge_0shot_s5 | certified | 0.00 | 100 | 500 | 0.016 | 0.010 | 0.000 / 0.000 / 0.000 | 0.016 [0.007, 0.031] | 1.000 | True |
| gemma_judge_0shot_s5 | certified | 0.00 | 200 | 500 | 0.276 | 0.098 | 0.000 / 0.000 / 0.363 | 0.010 [0.003, 0.023] | 0.036 | True |
| gemma_judge_0shot_s5 | certified | 0.00 | 400 | 500 | 0.698 | 0.229 | 0.000 / 0.271 / 0.440 | 0.004 [0.000, 0.014] | 0.006 | True |
| gemma_judge_0shot_s5 | certified | 0.00 | 800 | 500 | 0.968 | 0.354 | 0.271 / 0.353 / 0.440 | 0.006 [0.001, 0.017] | 0.006 | True |
| gemma_judge_0shot_s5 | heuristic | 1.00 | 25 | 500 | 0.042 | 0.042 | 0.000 / 0.000 / 0.000 | 0.042 [0.026, 0.063] | 1.000 | True |
| gemma_judge_0shot_s5 | heuristic | 1.00 | 50 | 500 | 0.012 | 0.012 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 1.000 | True |
| gemma_judge_0shot_s5 | heuristic | 1.00 | 100 | 500 | 0.510 | 0.334 | 0.000 / 0.582 / 0.680 | 0.510 [0.465, 0.555] | 1.000 | False |
| gemma_judge_0shot_s5 | heuristic | 1.00 | 200 | 500 | 0.970 | 0.508 | 0.363 / 0.505 / 0.663 | 0.476 [0.431, 0.521] | 0.491 | False |
| gemma_judge_0shot_s5 | heuristic | 1.00 | 400 | 500 | 1.000 | 0.501 | 0.400 / 0.474 / 0.624 | 0.402 [0.359, 0.446] | 0.402 | False |
| gemma_judge_0shot_s5 | heuristic | 1.00 | 800 | 500 | 1.000 | 0.488 | 0.440 / 0.466 / 0.583 | 0.288 [0.249, 0.330] | 0.288 | False |
| gemma_s5_features_judge | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.10 | 100 | 500 | 0.018 | 0.012 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 0.444 | True |
| gemma_s5_features_judge | certified | 0.10 | 200 | 500 | 0.676 | 0.326 | 0.000 / 0.412 / 0.586 | 0.016 [0.007, 0.031] | 0.024 | True |
| gemma_s5_features_judge | certified | 0.10 | 400 | 500 | 0.894 | 0.503 | 0.000 / 0.569 / 0.670 | 0.020 [0.010, 0.036] | 0.022 | True |
| gemma_s5_features_judge | certified | 0.10 | 800 | 500 | 0.976 | 0.630 | 0.562 / 0.662 / 0.732 | 0.014 [0.006, 0.029] | 0.014 | True |
| gemma_s5_features_judge | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.25 | 100 | 500 | 0.004 | 0.003 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| gemma_s5_features_judge | certified | 0.25 | 200 | 500 | 0.760 | 0.397 | 0.000 / 0.467 / 0.645 | 0.022 [0.011, 0.039] | 0.029 | True |
| gemma_s5_features_judge | certified | 0.25 | 400 | 500 | 0.930 | 0.569 | 0.349 / 0.613 / 0.732 | 0.034 [0.020, 0.054] | 0.037 | True |
| gemma_s5_features_judge | certified | 0.25 | 800 | 500 | 0.940 | 0.644 | 0.601 / 0.691 / 0.753 | 0.008 [0.002, 0.020] | 0.009 | True |
| gemma_s5_features_judge | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.50 | 200 | 500 | 0.270 | 0.177 | 0.000 / 0.000 / 0.667 | 0.026 [0.014, 0.044] | 0.096 | True |
| gemma_s5_features_judge | certified | 0.50 | 400 | 500 | 0.878 | 0.534 | 0.000 / 0.602 / 0.726 | 0.014 [0.006, 0.029] | 0.016 | True |
| gemma_s5_features_judge | certified | 0.50 | 800 | 500 | 0.968 | 0.674 | 0.613 / 0.698 / 0.770 | 0.010 [0.003, 0.023] | 0.010 | True |
| gemma_s5_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_s5_features_judge | certified | 0.75 | 400 | 500 | 0.400 | 0.263 | 0.000 / 0.000 / 0.693 | 0.016 [0.007, 0.031] | 0.040 | True |
| gemma_s5_features_judge | certified | 0.75 | 800 | 500 | 0.920 | 0.599 | 0.305 / 0.657 / 0.755 | 0.018 [0.008, 0.034] | 0.020 | True |
| gemma_s5_features_judge | heuristic | 1.00 | 25 | 500 | 0.064 | 0.064 | 0.000 / 0.000 / 0.000 | 0.064 [0.044, 0.089] | 1.000 | True |
| gemma_s5_features_judge | heuristic | 1.00 | 50 | 500 | 0.074 | 0.074 | 0.000 / 0.000 / 0.000 | 0.074 [0.053, 0.101] | 1.000 | False |
| gemma_s5_features_judge | heuristic | 1.00 | 100 | 500 | 0.930 | 0.714 | 0.599 / 0.750 / 0.895 | 0.470 [0.426, 0.515] | 0.505 | False |
| gemma_s5_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.774 | 0.675 / 0.775 / 0.870 | 0.396 [0.353, 0.440] | 0.396 | False |
| gemma_s5_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.796 | 0.729 / 0.797 / 0.860 | 0.338 [0.297, 0.381] | 0.338 | False |
| gemma_s5_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.808 | 0.771 / 0.807 / 0.851 | 0.282 [0.243, 0.324] | 0.282 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 100: gemma_s5_features_judge at f = 0.10, 0.012
- B = 200: gemma_s5_features_judge at f = 0.25, 0.397
- B = 400: gemma_s5_features_judge at f = 0.25, 0.569
- B = 800: gemma_s5_features_judge at f = 0.50, 0.674

B* (smallest B where the best arm fits, f > 0): 100
