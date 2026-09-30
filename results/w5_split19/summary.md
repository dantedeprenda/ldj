# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.530 | 0.278 | 0.000 / 0.400 / 0.613 | 0.030 [0.006, 0.085] | 0.057 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.810 | 0.456 | 0.000 / 0.560 / 0.703 | 0.050 [0.016, 0.113] | 0.062 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.850 | 0.534 | 0.000 / 0.649 / 0.740 | 0.020 [0.002, 0.070] | 0.024 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.200 | 0.134 | 0.000 / 0.000 / 0.632 | 0.030 [0.006, 0.085] | 0.150 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.750 | 0.414 | 0.000 / 0.486 / 0.711 | 0.010 [0.000, 0.054] | 0.013 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.780 | 0.511 | 0.000 / 0.642 / 0.765 | 0.030 [0.006, 0.085] | 0.038 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.764 | 0.664 / 0.756 / 0.871 | 0.390 [0.294, 0.493] | 0.390 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.805 | 0.713 / 0.806 / 0.889 | 0.500 [0.398, 0.602] | 0.500 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.814 | 0.758 / 0.815 / 0.864 | 0.550 [0.447, 0.650] | 0.550 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.660 | 0.356 | 0.000 / 0.441 / 0.665 | 0.040 [0.011, 0.099] | 0.061 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.920 | 0.556 | 0.262 / 0.599 / 0.736 | 0.070 [0.029, 0.139] | 0.076 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.960 | 0.656 | 0.594 / 0.692 / 0.769 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.190 | 0.126 | 0.000 / 0.000 / 0.637 | 0.030 [0.006, 0.085] | 0.158 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.910 | 0.530 | 0.308 / 0.573 / 0.741 | 0.030 [0.006, 0.085] | 0.033 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.681 | 0.594 / 0.697 / 0.771 | 0.020 [0.002, 0.070] | 0.020 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.781 | 0.654 / 0.790 / 0.875 | 0.450 [0.350, 0.553] | 0.450 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.810 | 0.715 / 0.810 / 0.904 | 0.450 [0.350, 0.553] | 0.450 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.824 | 0.774 / 0.824 / 0.870 | 0.430 [0.331, 0.533] | 0.430 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.230 | 0.102 | 0.000 / 0.000 / 0.528 | 0.010 [0.000, 0.054] | 0.043 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.460 | 0.215 | 0.000 / 0.000 / 0.528 | 0.010 [0.000, 0.054] | 0.022 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.770 | 0.364 | 0.000 / 0.528 / 0.528 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.970 | 0.525 | 0.528 / 0.528 / 0.623 | 0.230 [0.152, 0.325] | 0.237 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.990 | 0.527 | 0.528 / 0.528 / 0.604 | 0.160 [0.094, 0.247] | 0.162 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.529 | 0.528 / 0.528 / 0.528 | 0.030 [0.006, 0.085] | 0.030 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.356
- B = 400: gemma_features_judge at f = 0.25, 0.556
- B = 800: gemma_features_judge at f = 0.50, 0.681

B* (smallest B where the best arm fits, f > 0): 200
