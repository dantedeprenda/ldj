# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.570 | 0.284 | 0.000 / 0.419 / 0.585 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.830 | 0.469 | 0.000 / 0.557 / 0.703 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.830 | 0.523 | 0.000 / 0.645 / 0.730 | 0.020 [0.002, 0.070] | 0.024 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.110 | 0.072 | 0.000 / 0.000 / 0.594 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.800 | 0.437 | 0.000 / 0.499 / 0.715 | 0.020 [0.002, 0.070] | 0.025 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.890 | 0.571 | 0.000 / 0.644 / 0.752 | 0.030 [0.006, 0.085] | 0.034 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.746 | 0.633 / 0.753 / 0.846 | 0.330 [0.239, 0.431] | 0.330 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.787 | 0.703 / 0.784 / 0.863 | 0.350 [0.257, 0.452] | 0.350 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.802 | 0.752 / 0.804 / 0.847 | 0.300 [0.212, 0.400] | 0.300 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.740 | 0.382 | 0.000 / 0.470 / 0.618 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.900 | 0.526 | 0.181 / 0.597 / 0.703 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.940 | 0.622 | 0.578 / 0.675 / 0.747 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.240 | 0.150 | 0.000 / 0.000 / 0.632 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.870 | 0.496 | 0.000 / 0.568 / 0.710 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.970 | 0.652 | 0.568 / 0.677 / 0.760 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.769 | 0.653 / 0.772 / 0.889 | 0.430 [0.331, 0.533] | 0.430 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.795 | 0.717 / 0.792 / 0.868 | 0.290 [0.204, 0.389] | 0.290 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.807 | 0.760 / 0.809 / 0.851 | 0.160 [0.094, 0.247] | 0.160 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.200 | 0.079 | 0.000 / 0.000 / 0.345 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.430 | 0.194 | 0.000 / 0.000 / 0.516 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.660 | 0.299 | 0.000 / 0.345 / 0.516 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.950 | 0.499 | 0.345 / 0.516 / 0.616 | 0.280 [0.195, 0.379] | 0.295 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.970 | 0.514 | 0.516 / 0.516 / 0.616 | 0.190 [0.118, 0.281] | 0.196 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.519 | 0.516 / 0.516 / 0.516 | 0.040 [0.011, 0.099] | 0.040 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.382
- B = 400: gemma_features_judge at f = 0.25, 0.526
- B = 800: gemma_features_judge at f = 0.50, 0.652

B* (smallest B where the best arm fits, f > 0): 200
