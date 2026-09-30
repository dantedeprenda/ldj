# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| jev_direct_0shot | certified | 0.00 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_direct_0shot | certified | 0.00 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_direct_0shot | certified | 0.00 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_direct_0shot | certified | 0.00 | 200 | 500 | 0.016 | 0.005 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 0.500 | True |
| jev_direct_0shot | certified | 0.00 | 400 | 500 | 0.162 | 0.032 | 0.000 / 0.000 / 0.167 | 0.004 [0.000, 0.014] | 0.025 | True |
| jev_direct_0shot | certified | 0.00 | 800 | 500 | 0.552 | 0.086 | 0.000 / 0.114 / 0.212 | 0.000 [0.000, 0.007] | 0.000 | True |
| jev_direct_0shot | heuristic | 1.00 | 25 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| jev_direct_0shot | heuristic | 1.00 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_direct_0shot | heuristic | 1.00 | 100 | 500 | 0.008 | 0.005 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 1.000 | True |
| jev_direct_0shot | heuristic | 1.00 | 200 | 500 | 0.488 | 0.176 | 0.000 / 0.000 / 0.403 | 0.384 [0.341, 0.428] | 0.787 | False |
| jev_direct_0shot | heuristic | 1.00 | 400 | 500 | 0.970 | 0.267 | 0.167 / 0.274 / 0.354 | 0.248 [0.211, 0.288] | 0.256 | False |
| jev_direct_0shot | heuristic | 1.00 | 800 | 500 | 1.000 | 0.266 | 0.212 / 0.274 / 0.330 | 0.124 [0.096, 0.156] | 0.124 | False |
| jev_features | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.10 | 100 | 500 | 0.050 | 0.034 | 0.000 / 0.000 / 0.000 | 0.014 [0.006, 0.029] | 0.280 | True |
| jev_features | certified | 0.10 | 200 | 500 | 0.824 | 0.409 | 0.000 / 0.466 / 0.623 | 0.008 [0.002, 0.020] | 0.010 | True |
| jev_features | certified | 0.10 | 400 | 500 | 0.990 | 0.601 | 0.492 / 0.611 / 0.711 | 0.010 [0.003, 0.023] | 0.010 | True |
| jev_features | certified | 0.10 | 800 | 500 | 0.992 | 0.683 | 0.618 / 0.691 / 0.752 | 0.006 [0.001, 0.017] | 0.006 | True |
| jev_features | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.25 | 100 | 500 | 0.008 | 0.006 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.750 | True |
| jev_features | certified | 0.25 | 200 | 500 | 0.816 | 0.450 | 0.000 / 0.514 / 0.665 | 0.010 [0.003, 0.023] | 0.012 | True |
| jev_features | certified | 0.25 | 400 | 500 | 0.996 | 0.647 | 0.544 / 0.647 / 0.748 | 0.020 [0.010, 0.036] | 0.020 | True |
| jev_features | certified | 0.25 | 800 | 500 | 0.998 | 0.720 | 0.660 / 0.722 / 0.784 | 0.014 [0.006, 0.029] | 0.014 | True |
| jev_features | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 100 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| jev_features | certified | 0.50 | 200 | 500 | 0.358 | 0.235 | 0.000 / 0.000 / 0.685 | 0.010 [0.003, 0.023] | 0.028 | True |
| jev_features | certified | 0.50 | 400 | 500 | 0.986 | 0.622 | 0.492 / 0.642 / 0.749 | 0.008 [0.002, 0.020] | 0.008 | True |
| jev_features | certified | 0.50 | 800 | 500 | 0.992 | 0.714 | 0.643 / 0.721 / 0.793 | 0.012 [0.004, 0.026] | 0.012 | True |
| jev_features | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 400 | 500 | 0.460 | 0.309 | 0.000 / 0.000 / 0.736 | 0.014 [0.006, 0.029] | 0.030 | True |
| jev_features | certified | 0.75 | 800 | 500 | 0.988 | 0.658 | 0.545 / 0.669 / 0.780 | 0.008 [0.002, 0.020] | 0.008 | True |
| jev_features | heuristic | 1.00 | 25 | 500 | 0.048 | 0.048 | 0.000 / 0.000 / 0.000 | 0.048 [0.031, 0.071] | 1.000 | True |
| jev_features | heuristic | 1.00 | 50 | 500 | 0.094 | 0.094 | 0.000 / 0.000 / 0.000 | 0.094 [0.070, 0.123] | 1.000 | False |
| jev_features | heuristic | 1.00 | 100 | 500 | 0.984 | 0.790 | 0.654 / 0.800 / 0.941 | 0.456 [0.412, 0.501] | 0.463 | False |
| jev_features | heuristic | 1.00 | 200 | 500 | 1.000 | 0.814 | 0.720 / 0.822 / 0.902 | 0.392 [0.349, 0.436] | 0.392 | False |
| jev_features | heuristic | 1.00 | 400 | 500 | 1.000 | 0.830 | 0.758 / 0.828 / 0.904 | 0.318 [0.277, 0.361] | 0.318 | False |
| jev_features | heuristic | 1.00 | 800 | 500 | 1.000 | 0.839 | 0.796 / 0.838 / 0.884 | 0.298 [0.258, 0.340] | 0.298 | False |
| jev_features_judge | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.10 | 100 | 500 | 0.060 | 0.041 | 0.000 / 0.000 / 0.000 | 0.022 [0.011, 0.039] | 0.367 | True |
| jev_features_judge | certified | 0.10 | 200 | 500 | 0.876 | 0.439 | 0.000 / 0.488 / 0.632 | 0.010 [0.003, 0.023] | 0.011 | True |
| jev_features_judge | certified | 0.10 | 400 | 500 | 0.996 | 0.616 | 0.511 / 0.622 / 0.721 | 0.012 [0.004, 0.026] | 0.012 | True |
| jev_features_judge | certified | 0.10 | 800 | 500 | 0.994 | 0.694 | 0.623 / 0.706 / 0.763 | 0.008 [0.002, 0.020] | 0.008 | True |
| jev_features_judge | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.25 | 100 | 500 | 0.006 | 0.005 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 0.667 | True |
| jev_features_judge | certified | 0.25 | 200 | 500 | 0.850 | 0.472 | 0.000 / 0.525 / 0.672 | 0.012 [0.004, 0.026] | 0.014 | True |
| jev_features_judge | certified | 0.25 | 400 | 500 | 0.998 | 0.658 | 0.552 / 0.657 / 0.762 | 0.016 [0.007, 0.031] | 0.016 | True |
| jev_features_judge | certified | 0.25 | 800 | 500 | 0.998 | 0.730 | 0.669 / 0.735 / 0.792 | 0.014 [0.006, 0.029] | 0.014 | True |
| jev_features_judge | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.50 | 100 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| jev_features_judge | certified | 0.50 | 200 | 500 | 0.408 | 0.267 | 0.000 / 0.000 / 0.688 | 0.008 [0.002, 0.020] | 0.020 | True |
| jev_features_judge | certified | 0.50 | 400 | 500 | 0.994 | 0.638 | 0.511 / 0.650 / 0.766 | 0.010 [0.003, 0.023] | 0.010 | True |
| jev_features_judge | certified | 0.50 | 800 | 500 | 0.994 | 0.729 | 0.658 / 0.732 / 0.805 | 0.018 [0.008, 0.034] | 0.018 | True |
| jev_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features_judge | certified | 0.75 | 400 | 500 | 0.484 | 0.328 | 0.000 / 0.000 / 0.740 | 0.008 [0.002, 0.020] | 0.017 | True |
| jev_features_judge | certified | 0.75 | 800 | 500 | 0.988 | 0.672 | 0.552 / 0.688 / 0.794 | 0.010 [0.003, 0.023] | 0.010 | True |
| jev_features_judge | heuristic | 1.00 | 25 | 500 | 0.060 | 0.060 | 0.000 / 0.000 / 0.000 | 0.060 [0.041, 0.085] | 1.000 | True |
| jev_features_judge | heuristic | 1.00 | 50 | 500 | 0.096 | 0.096 | 0.000 / 0.000 / 0.000 | 0.096 [0.072, 0.125] | 1.000 | False |
| jev_features_judge | heuristic | 1.00 | 100 | 500 | 0.996 | 0.804 | 0.676 / 0.808 / 0.951 | 0.444 [0.400, 0.489] | 0.446 | False |
| jev_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.821 | 0.724 / 0.827 / 0.909 | 0.368 [0.326, 0.412] | 0.368 | False |
| jev_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.837 | 0.766 / 0.836 / 0.906 | 0.304 [0.264, 0.346] | 0.304 | False |
| jev_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.846 | 0.807 / 0.847 / 0.887 | 0.200 [0.166, 0.238] | 0.200 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 100: jev_features_judge at f = 0.10, 0.041
- B = 200: jev_features_judge at f = 0.25, 0.472
- B = 400: jev_features_judge at f = 0.25, 0.658
- B = 800: jev_features_judge at f = 0.25, 0.730

B* (smallest B where the best arm fits, f > 0): 100
