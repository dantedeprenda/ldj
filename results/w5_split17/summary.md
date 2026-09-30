# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.710 | 0.393 | 0.000 / 0.490 / 0.673 | 0.040 [0.011, 0.099] | 0.056 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.940 | 0.561 | 0.423 / 0.596 / 0.711 | 0.030 [0.006, 0.085] | 0.032 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.930 | 0.613 | 0.108 / 0.697 / 0.768 | 0.040 [0.011, 0.099] | 0.043 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.210 | 0.140 | 0.000 / 0.000 / 0.654 | 0.050 [0.016, 0.113] | 0.238 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.830 | 0.479 | 0.000 / 0.567 / 0.699 | 0.020 [0.002, 0.070] | 0.024 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.880 | 0.608 | 0.000 / 0.685 / 0.775 | 0.070 [0.029, 0.139] | 0.080 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.783 | 0.699 / 0.790 / 0.872 | 0.540 [0.437, 0.640] | 0.540 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.803 | 0.717 / 0.811 / 0.868 | 0.640 [0.538, 0.734] | 0.640 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.822 | 0.772 / 0.825 / 0.865 | 0.720 [0.621, 0.805] | 0.720 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.800 | 0.444 | 0.000 / 0.521 / 0.668 | 0.030 [0.006, 0.085] | 0.037 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.980 | 0.609 | 0.478 / 0.636 / 0.745 | 0.040 [0.011, 0.099] | 0.041 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.990 | 0.713 | 0.654 / 0.728 / 0.789 | 0.080 [0.035, 0.152] | 0.081 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.230 | 0.155 | 0.000 / 0.000 / 0.659 | 0.040 [0.011, 0.099] | 0.174 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.940 | 0.562 | 0.356 / 0.614 / 0.725 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.722 | 0.641 / 0.740 / 0.800 | 0.050 [0.016, 0.113] | 0.051 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.808 | 0.731 / 0.809 / 0.915 | 0.600 [0.497, 0.697] | 0.600 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.828 | 0.758 / 0.835 / 0.894 | 0.680 [0.579, 0.770] | 0.680 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.838 | 0.785 / 0.844 / 0.878 | 0.710 [0.611, 0.796] | 0.710 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.180 | 0.084 | 0.000 / 0.000 / 0.529 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.450 | 0.219 | 0.000 / 0.000 / 0.529 | 0.030 [0.006, 0.085] | 0.067 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.770 | 0.368 | 0.000 / 0.529 / 0.529 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.950 | 0.524 | 0.529 / 0.529 / 0.625 | 0.300 [0.212, 0.400] | 0.316 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.529 | 0.529 / 0.529 / 0.625 | 0.150 [0.086, 0.235] | 0.153 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.534 | 0.529 / 0.529 / 0.529 | 0.060 [0.022, 0.126] | 0.060 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.444
- B = 400: gemma_features_judge at f = 0.25, 0.609
- B = 800: gemma_features_judge at f = 0.50, 0.722

B* (smallest B where the best arm fits, f > 0): 200
