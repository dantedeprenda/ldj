# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.560 | 0.293 | 0.000 / 0.413 / 0.618 | 0.040 [0.011, 0.099] | 0.071 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.860 | 0.479 | 0.000 / 0.544 / 0.700 | 0.020 [0.002, 0.070] | 0.023 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.960 | 0.593 | 0.136 / 0.656 / 0.756 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.210 | 0.139 | 0.000 / 0.000 / 0.632 | 0.040 [0.011, 0.099] | 0.190 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.740 | 0.404 | 0.000 / 0.485 / 0.705 | 0.020 [0.002, 0.070] | 0.027 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.950 | 0.599 | 0.496 / 0.634 / 0.756 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.771 | 0.632 / 0.778 / 0.891 | 0.470 [0.369, 0.572] | 0.470 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.785 | 0.703 / 0.786 / 0.874 | 0.310 [0.221, 0.410] | 0.310 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.808 | 0.760 / 0.814 / 0.858 | 0.390 [0.294, 0.493] | 0.390 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.760 | 0.408 | 0.000 / 0.480 / 0.669 | 0.040 [0.011, 0.099] | 0.053 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.970 | 0.588 | 0.468 / 0.599 / 0.728 | 0.030 [0.006, 0.085] | 0.031 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.970 | 0.663 | 0.593 / 0.691 / 0.756 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.340 | 0.224 | 0.000 / 0.000 / 0.696 | 0.040 [0.011, 0.099] | 0.118 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.900 | 0.522 | 0.257 / 0.566 / 0.720 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 1.000 | 0.684 | 0.608 / 0.679 / 0.776 | 0.010 [0.000, 0.054] | 0.010 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.796 | 0.682 / 0.798 / 0.902 | 0.520 [0.418, 0.621] | 0.520 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.801 | 0.720 / 0.803 / 0.882 | 0.380 [0.285, 0.483] | 0.380 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.821 | 0.768 / 0.821 / 0.879 | 0.390 [0.294, 0.493] | 0.390 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.220 | 0.101 | 0.000 / 0.000 / 0.525 | 0.020 [0.002, 0.070] | 0.091 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.270 | 0.120 | 0.000 / 0.000 / 0.525 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.760 | 0.371 | 0.000 / 0.525 / 0.525 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.970 | 0.549 | 0.525 / 0.525 / 0.628 | 0.470 [0.369, 0.572] | 0.485 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.970 | 0.529 | 0.513 / 0.525 / 0.628 | 0.300 [0.212, 0.400] | 0.309 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.546 | 0.525 / 0.525 / 0.628 | 0.230 [0.152, 0.325] | 0.230 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.408
- B = 400: gemma_features_judge at f = 0.25, 0.588
- B = 800: gemma_features_judge at f = 0.50, 0.684

B* (smallest B where the best arm fits, f > 0): 200
