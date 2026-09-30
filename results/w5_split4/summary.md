# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.610 | 0.329 | 0.000 / 0.451 / 0.653 | 0.030 [0.006, 0.085] | 0.049 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.930 | 0.531 | 0.264 / 0.555 / 0.722 | 0.060 [0.022, 0.126] | 0.065 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.930 | 0.596 | 0.110 / 0.675 / 0.769 | 0.070 [0.029, 0.139] | 0.075 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.240 | 0.163 | 0.000 / 0.000 / 0.673 | 0.040 [0.011, 0.099] | 0.167 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.830 | 0.473 | 0.000 / 0.542 / 0.688 | 0.040 [0.011, 0.099] | 0.048 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.950 | 0.633 | 0.500 / 0.676 / 0.772 | 0.070 [0.029, 0.139] | 0.074 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.793 | 0.658 / 0.806 / 0.920 | 0.650 [0.548, 0.743] | 0.650 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.811 | 0.746 / 0.808 / 0.881 | 0.720 [0.621, 0.805] | 0.720 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.814 | 0.756 / 0.816 / 0.869 | 0.710 [0.611, 0.796] | 0.710 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.810 | 0.443 | 0.000 / 0.511 / 0.678 | 0.020 [0.002, 0.070] | 0.025 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.980 | 0.603 | 0.493 / 0.610 / 0.721 | 0.060 [0.022, 0.126] | 0.061 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.960 | 0.675 | 0.614 / 0.713 / 0.791 | 0.080 [0.035, 0.152] | 0.083 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.300 | 0.206 | 0.000 / 0.000 / 0.721 | 0.050 [0.016, 0.113] | 0.167 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.930 | 0.553 | 0.331 / 0.598 / 0.707 | 0.020 [0.002, 0.070] | 0.022 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.694 | 0.604 / 0.718 / 0.785 | 0.050 [0.016, 0.113] | 0.051 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.811 | 0.680 / 0.815 / 0.928 | 0.570 [0.467, 0.669] | 0.570 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.827 | 0.750 / 0.829 / 0.901 | 0.670 [0.569, 0.761] | 0.670 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.833 | 0.778 / 0.835 / 0.881 | 0.720 [0.621, 0.805] | 0.720 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.120 | 0.052 | 0.000 / 0.000 / 0.364 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.190 | 0.087 | 0.000 / 0.000 / 0.409 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.260 | 0.127 | 0.000 / 0.000 / 0.531 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.970 | 0.532 | 0.531 / 0.531 / 0.627 | 0.270 [0.186, 0.368] | 0.278 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.525 | 0.531 / 0.531 / 0.531 | 0.080 [0.035, 0.152] | 0.082 | True |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 0.980 | 0.522 | 0.531 / 0.531 / 0.531 | 0.010 [0.000, 0.054] | 0.010 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.443
- B = 400: gemma_features_judge at f = 0.25, 0.603
- B = 800: gemma_features_judge at f = 0.50, 0.694

B* (smallest B where the best arm fits, f > 0): 200
