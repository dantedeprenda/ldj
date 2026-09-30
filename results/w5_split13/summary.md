# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.790 | 0.407 | 0.000 / 0.473 / 0.625 | 0.010 [0.000, 0.054] | 0.013 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.940 | 0.532 | 0.258 / 0.577 / 0.690 | 0.040 [0.011, 0.099] | 0.043 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.920 | 0.581 | 0.113 / 0.645 / 0.728 | 0.030 [0.006, 0.085] | 0.033 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.190 | 0.125 | 0.000 / 0.000 / 0.630 | 0.030 [0.006, 0.085] | 0.158 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.850 | 0.472 | 0.000 / 0.526 / 0.687 | 0.010 [0.000, 0.054] | 0.012 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.980 | 0.621 | 0.539 / 0.626 / 0.734 | 0.010 [0.000, 0.054] | 0.010 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.768 | 0.637 / 0.776 / 0.886 | 0.470 [0.369, 0.572] | 0.470 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.776 | 0.702 / 0.774 / 0.845 | 0.380 [0.285, 0.483] | 0.380 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.793 | 0.735 / 0.798 / 0.844 | 0.350 [0.257, 0.452] | 0.350 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.840 | 0.448 | 0.000 / 0.504 / 0.630 | 0.010 [0.000, 0.054] | 0.012 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.980 | 0.578 | 0.450 / 0.601 / 0.701 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.970 | 0.655 | 0.599 / 0.684 / 0.748 | 0.030 [0.006, 0.085] | 0.031 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.250 | 0.161 | 0.000 / 0.000 / 0.631 | 0.020 [0.002, 0.070] | 0.080 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.960 | 0.556 | 0.381 / 0.589 / 0.708 | 0.040 [0.011, 0.099] | 0.042 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.657 | 0.577 / 0.660 / 0.746 | 0.020 [0.002, 0.070] | 0.020 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.786 | 0.657 / 0.794 / 0.893 | 0.570 [0.467, 0.669] | 0.570 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.799 | 0.728 / 0.805 / 0.872 | 0.480 [0.379, 0.582] | 0.480 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.813 | 0.749 / 0.820 / 0.866 | 0.400 [0.303, 0.503] | 0.400 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.170 | 0.072 | 0.000 / 0.000 / 0.365 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.390 | 0.178 | 0.000 / 0.000 / 0.517 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.510 | 0.236 | 0.000 / 0.353 / 0.517 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.920 | 0.485 | 0.359 / 0.517 / 0.613 | 0.240 [0.160, 0.336] | 0.261 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 1.000 | 0.531 | 0.517 / 0.517 / 0.613 | 0.210 [0.135, 0.303] | 0.210 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 0.990 | 0.514 | 0.517 / 0.517 / 0.517 | 0.050 [0.016, 0.113] | 0.051 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.448
- B = 400: gemma_features_judge at f = 0.25, 0.578
- B = 800: gemma_features_judge at f = 0.50, 0.657

B* (smallest B where the best arm fits, f > 0): 200
