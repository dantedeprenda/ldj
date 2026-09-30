# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.640 | 0.326 | 0.000 / 0.430 / 0.598 | 0.010 [0.000, 0.054] | 0.016 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.960 | 0.573 | 0.454 / 0.612 / 0.705 | 0.060 [0.022, 0.126] | 0.062 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.950 | 0.575 | 0.104 / 0.663 / 0.748 | 0.060 [0.022, 0.126] | 0.063 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.300 | 0.197 | 0.000 / 0.000 / 0.691 | 0.040 [0.011, 0.099] | 0.133 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.940 | 0.551 | 0.350 / 0.571 / 0.712 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.940 | 0.590 | 0.223 / 0.653 / 0.771 | 0.070 [0.029, 0.139] | 0.074 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.807 | 0.718 / 0.809 / 0.905 | 0.660 [0.558, 0.752] | 0.660 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.812 | 0.731 / 0.810 / 0.875 | 0.690 [0.590, 0.779] | 0.690 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.825 | 0.786 / 0.822 / 0.872 | 0.790 [0.697, 0.865] | 0.790 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.750 | 0.399 | 0.000 / 0.489 / 0.631 | 0.020 [0.002, 0.070] | 0.027 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.980 | 0.629 | 0.526 / 0.639 / 0.725 | 0.060 [0.022, 0.126] | 0.061 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.950 | 0.652 | 0.585 / 0.695 / 0.774 | 0.050 [0.016, 0.113] | 0.053 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.320 | 0.216 | 0.000 / 0.000 / 0.691 | 0.050 [0.016, 0.113] | 0.156 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.970 | 0.618 | 0.488 / 0.632 / 0.758 | 0.050 [0.016, 0.113] | 0.052 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 1.000 | 0.707 | 0.605 / 0.714 / 0.793 | 0.060 [0.022, 0.126] | 0.060 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.818 | 0.714 / 0.811 / 0.927 | 0.650 [0.548, 0.743] | 0.650 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.829 | 0.758 / 0.829 / 0.896 | 0.660 [0.558, 0.752] | 0.660 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.839 | 0.786 / 0.840 / 0.878 | 0.780 [0.686, 0.857] | 0.780 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.290 | 0.140 | 0.000 / 0.000 / 0.525 | 0.020 [0.002, 0.070] | 0.069 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.480 | 0.228 | 0.000 / 0.000 / 0.525 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.750 | 0.367 | 0.000 / 0.525 / 0.525 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.980 | 0.549 | 0.525 / 0.525 / 0.624 | 0.370 [0.276, 0.472] | 0.378 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 1.000 | 0.532 | 0.525 / 0.525 / 0.624 | 0.200 [0.127, 0.292] | 0.200 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.530 | 0.525 / 0.525 / 0.525 | 0.050 [0.016, 0.113] | 0.050 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.399
- B = 400: gemma_features_judge at f = 0.25, 0.629
- B = 800: gemma_features_judge at f = 0.50, 0.707

B* (smallest B where the best arm fits, f > 0): 200
