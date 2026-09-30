# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 50 | 500 | 0.038 | 0.029 | 0.000 / 0.000 / 0.000 | 0.018 [0.008, 0.034] | 0.474 | True |
| bgeL_logreg | certified | 0.10 | 100 | 500 | 0.278 | 0.128 | 0.000 / 0.000 / 0.481 | 0.034 [0.020, 0.054] | 0.122 | True |
| bgeL_logreg | certified | 0.10 | 200 | 500 | 0.696 | 0.350 | 0.000 / 0.363 / 0.743 | 0.042 [0.026, 0.063] | 0.060 | True |
| bgeL_logreg | certified | 0.10 | 400 | 500 | 0.942 | 0.635 | 0.462 / 0.681 / 0.804 | 0.060 [0.041, 0.085] | 0.064 | True |
| bgeL_logreg | certified | 0.10 | 800 | 500 | 0.990 | 0.770 | 0.691 / 0.778 / 0.856 | 0.080 [0.058, 0.107] | 0.081 | False |
| bgeL_logreg | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 50 | 500 | 0.042 | 0.033 | 0.000 / 0.000 / 0.000 | 0.026 [0.014, 0.044] | 0.619 | True |
| bgeL_logreg | certified | 0.25 | 100 | 500 | 0.486 | 0.247 | 0.000 / 0.000 / 0.628 | 0.030 [0.017, 0.049] | 0.062 | True |
| bgeL_logreg | certified | 0.25 | 200 | 500 | 0.868 | 0.489 | 0.000 / 0.553 / 0.766 | 0.046 [0.029, 0.068] | 0.053 | True |
| bgeL_logreg | certified | 0.25 | 400 | 500 | 0.978 | 0.717 | 0.591 / 0.738 / 0.854 | 0.054 [0.036, 0.078] | 0.055 | True |
| bgeL_logreg | certified | 0.25 | 800 | 500 | 0.990 | 0.825 | 0.736 / 0.827 / 0.937 | 0.062 [0.043, 0.087] | 0.063 | True |
| bgeL_logreg | certified | 0.50 | 25 | 500 | 0.006 | 0.006 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 1.000 | True |
| bgeL_logreg | certified | 0.50 | 50 | 500 | 0.006 | 0.006 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 1.000 | True |
| bgeL_logreg | certified | 0.50 | 100 | 500 | 0.266 | 0.170 | 0.000 / 0.000 / 0.635 | 0.026 [0.014, 0.044] | 0.098 | True |
| bgeL_logreg | certified | 0.50 | 200 | 500 | 0.892 | 0.498 | 0.000 / 0.538 / 0.760 | 0.028 [0.015, 0.047] | 0.031 | True |
| bgeL_logreg | certified | 0.50 | 400 | 500 | 0.984 | 0.731 | 0.586 / 0.740 / 0.897 | 0.054 [0.036, 0.078] | 0.055 | True |
| bgeL_logreg | certified | 0.50 | 800 | 500 | 0.998 | 0.852 | 0.752 / 0.851 / 0.960 | 0.028 [0.015, 0.047] | 0.028 | True |
| bgeL_logreg | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 100 | 500 | 0.006 | 0.006 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 1.000 | True |
| bgeL_logreg | certified | 0.75 | 200 | 500 | 0.392 | 0.260 | 0.000 / 0.000 / 0.743 | 0.034 [0.020, 0.054] | 0.087 | True |
| bgeL_logreg | certified | 0.75 | 400 | 500 | 0.942 | 0.605 | 0.298 / 0.642 / 0.879 | 0.016 [0.007, 0.031] | 0.017 | True |
| bgeL_logreg | certified | 0.75 | 800 | 500 | 0.992 | 0.816 | 0.665 / 0.827 / 0.972 | 0.012 [0.004, 0.026] | 0.012 | True |
| bgeL_logreg | heuristic | 1.00 | 25 | 500 | 0.302 | 0.302 | 0.000 / 0.000 / 1.000 | 0.302 [0.262, 0.344] | 1.000 | False |
| bgeL_logreg | heuristic | 1.00 | 50 | 500 | 0.658 | 0.561 | 0.000 / 0.718 / 1.000 | 0.368 [0.326, 0.412] | 0.559 | False |
| bgeL_logreg | heuristic | 1.00 | 100 | 500 | 0.932 | 0.753 | 0.407 / 0.823 / 1.000 | 0.418 [0.374, 0.463] | 0.448 | False |
| bgeL_logreg | heuristic | 1.00 | 200 | 500 | 1.000 | 0.841 | 0.604 / 0.871 / 1.000 | 0.332 [0.291, 0.375] | 0.332 | False |
| bgeL_logreg | heuristic | 1.00 | 400 | 500 | 1.000 | 0.933 | 0.837 / 0.952 / 1.000 | 0.250 [0.213, 0.290] | 0.250 | False |
| bgeL_logreg | heuristic | 1.00 | 800 | 500 | 1.000 | 0.989 | 0.954 / 1.000 / 1.000 | 0.168 [0.136, 0.204] | 0.168 | False |
| gemma_features_judge | certified | 0.10 | 25 | 500 | 0.008 | 0.008 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 0.250 | True |
| gemma_features_judge | certified | 0.10 | 50 | 500 | 0.194 | 0.141 | 0.000 / 0.000 / 0.696 | 0.012 [0.004, 0.026] | 0.062 | True |
| gemma_features_judge | certified | 0.10 | 100 | 500 | 0.654 | 0.423 | 0.000 / 0.536 / 0.820 | 0.014 [0.006, 0.029] | 0.021 | True |
| gemma_features_judge | certified | 0.10 | 200 | 500 | 0.868 | 0.669 | 0.000 / 0.762 / 0.937 | 0.014 [0.006, 0.029] | 0.016 | True |
| gemma_features_judge | certified | 0.10 | 400 | 500 | 0.970 | 0.870 | 0.769 / 0.906 / 1.000 | 0.016 [0.007, 0.031] | 0.016 | True |
| gemma_features_judge | certified | 0.10 | 800 | 500 | 0.974 | 0.943 | 0.889 / 0.990 / 1.000 | 0.006 [0.001, 0.017] | 0.006 | True |
| gemma_features_judge | certified | 0.25 | 25 | 500 | 0.002 | 0.002 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| gemma_features_judge | certified | 0.25 | 50 | 500 | 0.182 | 0.142 | 0.000 / 0.000 / 0.735 | 0.014 [0.006, 0.029] | 0.077 | True |
| gemma_features_judge | certified | 0.25 | 100 | 500 | 0.870 | 0.583 | 0.000 / 0.641 / 0.885 | 0.018 [0.008, 0.034] | 0.021 | True |
| gemma_features_judge | certified | 0.25 | 200 | 500 | 0.976 | 0.809 | 0.644 / 0.834 / 0.993 | 0.008 [0.002, 0.020] | 0.008 | True |
| gemma_features_judge | certified | 0.25 | 400 | 500 | 0.970 | 0.904 | 0.844 / 0.949 / 1.000 | 0.002 [0.000, 0.011] | 0.002 | True |
| gemma_features_judge | certified | 0.25 | 800 | 500 | 0.998 | 0.987 | 0.958 / 1.000 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 25 | 500 | 0.022 | 0.022 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 0.182 | True |
| gemma_features_judge | certified | 0.50 | 50 | 500 | 0.020 | 0.020 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 0.200 | True |
| gemma_features_judge | certified | 0.50 | 100 | 500 | 0.728 | 0.512 | 0.000 / 0.611 / 0.881 | 0.006 [0.001, 0.017] | 0.008 | True |
| gemma_features_judge | certified | 0.50 | 200 | 500 | 0.962 | 0.799 | 0.603 / 0.845 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 400 | 500 | 0.990 | 0.926 | 0.833 / 0.951 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 800 | 500 | 0.994 | 0.979 | 0.942 / 1.000 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| gemma_features_judge | certified | 0.75 | 100 | 500 | 0.016 | 0.016 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 0.125 | True |
| gemma_features_judge | certified | 0.75 | 200 | 500 | 0.834 | 0.633 | 0.000 / 0.703 / 0.968 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.75 | 400 | 500 | 0.962 | 0.831 | 0.667 / 0.875 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | certified | 0.75 | 800 | 500 | 0.998 | 0.957 | 0.885 / 0.981 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | heuristic | 1.00 | 25 | 500 | 0.606 | 0.606 | 0.000 / 1.000 / 1.000 | 0.284 [0.245, 0.326] | 0.469 | False |
| gemma_features_judge | heuristic | 1.00 | 50 | 500 | 0.994 | 0.954 | 0.850 / 1.000 / 1.000 | 0.106 [0.080, 0.136] | 0.107 | False |
| gemma_features_judge | heuristic | 1.00 | 100 | 500 | 1.000 | 0.983 | 0.932 / 1.000 / 1.000 | 0.012 [0.004, 0.026] | 0.012 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.995 | 0.998 / 1.000 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.999 | 0.999 / 1.000 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 1.000 | 0.999 / 1.000 / 1.000 | 0.000 [0.000, 0.007] | 0.000 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 25: gemma_features_judge at f = 0.50, 0.022
- B = 50: gemma_features_judge at f = 0.25, 0.142
- B = 100: gemma_features_judge at f = 0.25, 0.583
- B = 200: gemma_features_judge at f = 0.25, 0.809
- B = 400: gemma_features_judge at f = 0.50, 0.926
- B = 800: gemma_features_judge at f = 0.25, 0.987

B* (smallest B where the best arm fits, f > 0): 25
