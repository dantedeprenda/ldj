# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.800 | 0.421 | 0.000 / 0.481 / 0.673 | 0.040 [0.011, 0.099] | 0.050 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.880 | 0.513 | 0.000 / 0.591 / 0.699 | 0.030 [0.006, 0.085] | 0.034 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.930 | 0.583 | 0.089 / 0.674 / 0.766 | 0.080 [0.035, 0.152] | 0.086 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.170 | 0.115 | 0.000 / 0.000 / 0.639 | 0.020 [0.002, 0.070] | 0.118 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.820 | 0.476 | 0.000 / 0.564 / 0.705 | 0.040 [0.011, 0.099] | 0.049 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.860 | 0.576 | 0.000 / 0.687 / 0.790 | 0.140 [0.079, 0.224] | 0.163 | False |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.806 | 0.742 / 0.809 / 0.887 | 0.730 [0.632, 0.814] | 0.730 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.817 | 0.753 / 0.824 / 0.880 | 0.790 [0.697, 0.865] | 0.790 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.843 | 0.800 / 0.842 / 0.886 | 0.900 [0.824, 0.951] | 0.900 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.850 | 0.477 | 0.000 / 0.530 / 0.684 | 0.060 [0.022, 0.126] | 0.071 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.970 | 0.593 | 0.469 / 0.610 / 0.726 | 0.010 [0.000, 0.054] | 0.010 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.950 | 0.665 | 0.591 / 0.712 / 0.772 | 0.070 [0.029, 0.139] | 0.074 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.290 | 0.187 | 0.000 / 0.000 / 0.638 | 0.020 [0.002, 0.070] | 0.069 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.930 | 0.553 | 0.372 / 0.590 / 0.732 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.692 | 0.584 / 0.715 / 0.794 | 0.090 [0.042, 0.164] | 0.091 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.815 | 0.705 / 0.820 / 0.906 | 0.730 [0.632, 0.814] | 0.730 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.822 | 0.755 / 0.827 / 0.889 | 0.640 [0.538, 0.734] | 0.640 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.842 | 0.791 / 0.844 / 0.891 | 0.780 [0.686, 0.857] | 0.780 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.160 | 0.074 | 0.000 / 0.000 / 0.398 | 0.030 [0.006, 0.085] | 0.188 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.280 | 0.134 | 0.000 / 0.000 / 0.521 | 0.010 [0.000, 0.054] | 0.036 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.520 | 0.256 | 0.000 / 0.349 / 0.521 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.930 | 0.509 | 0.393 / 0.521 / 0.630 | 0.360 [0.266, 0.462] | 0.387 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.532 | 0.521 / 0.521 / 0.630 | 0.290 [0.204, 0.389] | 0.296 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 0.990 | 0.529 | 0.521 / 0.521 / 0.611 | 0.160 [0.094, 0.247] | 0.162 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.477
- B = 400: gemma_features_judge at f = 0.25, 0.593
- B = 800: gemma_features_judge at f = 0.50, 0.692

B* (smallest B where the best arm fits, f > 0): 200
