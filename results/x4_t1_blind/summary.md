# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| blind_features | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.10 | 100 | 500 | 0.016 | 0.011 | 0.000 / 0.000 / 0.000 | 0.010 [0.003, 0.023] | 0.625 | True |
| blind_features | certified | 0.10 | 200 | 500 | 0.718 | 0.318 | 0.000 / 0.388 / 0.535 | 0.026 [0.014, 0.044] | 0.036 | True |
| blind_features | certified | 0.10 | 400 | 500 | 0.940 | 0.484 | 0.300 / 0.523 / 0.619 | 0.016 [0.007, 0.031] | 0.017 | True |
| blind_features | certified | 0.10 | 800 | 500 | 0.992 | 0.595 | 0.524 / 0.604 / 0.667 | 0.022 [0.011, 0.039] | 0.022 | True |
| blind_features | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.25 | 100 | 500 | 0.004 | 0.003 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| blind_features | certified | 0.25 | 200 | 500 | 0.658 | 0.325 | 0.000 / 0.423 / 0.588 | 0.024 [0.012, 0.042] | 0.036 | True |
| blind_features | certified | 0.25 | 400 | 500 | 0.964 | 0.529 | 0.401 / 0.549 / 0.662 | 0.024 [0.012, 0.042] | 0.025 | True |
| blind_features | certified | 0.25 | 800 | 500 | 0.996 | 0.633 | 0.564 / 0.635 / 0.707 | 0.020 [0.010, 0.036] | 0.020 | True |
| blind_features | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.50 | 200 | 500 | 0.160 | 0.102 | 0.000 / 0.000 / 0.610 | 0.018 [0.008, 0.034] | 0.113 | True |
| blind_features | certified | 0.50 | 400 | 500 | 0.932 | 0.493 | 0.312 / 0.536 / 0.662 | 0.014 [0.006, 0.029] | 0.015 | True |
| blind_features | certified | 0.50 | 800 | 500 | 0.962 | 0.613 | 0.542 / 0.639 / 0.716 | 0.022 [0.011, 0.039] | 0.023 | True |
| blind_features | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features | certified | 0.75 | 400 | 500 | 0.220 | 0.141 | 0.000 / 0.000 / 0.630 | 0.010 [0.003, 0.023] | 0.045 | True |
| blind_features | certified | 0.75 | 800 | 500 | 0.946 | 0.530 | 0.331 / 0.576 / 0.689 | 0.018 [0.008, 0.034] | 0.019 | True |
| blind_features | heuristic | 1.00 | 25 | 500 | 0.046 | 0.046 | 0.000 / 0.000 / 0.000 | 0.046 [0.029, 0.068] | 1.000 | True |
| blind_features | heuristic | 1.00 | 50 | 500 | 0.056 | 0.056 | 0.000 / 0.000 / 0.000 | 0.056 [0.038, 0.080] | 1.000 | True |
| blind_features | heuristic | 1.00 | 100 | 500 | 0.846 | 0.624 | 0.000 / 0.700 / 0.872 | 0.474 [0.429, 0.519] | 0.560 | False |
| blind_features | heuristic | 1.00 | 200 | 500 | 1.000 | 0.722 | 0.605 / 0.727 / 0.834 | 0.454 [0.410, 0.499] | 0.454 | False |
| blind_features | heuristic | 1.00 | 400 | 500 | 1.000 | 0.741 | 0.669 / 0.745 / 0.808 | 0.414 [0.370, 0.459] | 0.414 | False |
| blind_features | heuristic | 1.00 | 800 | 500 | 1.000 | 0.751 | 0.705 / 0.749 / 0.801 | 0.310 [0.270, 0.353] | 0.310 | False |
| blind_features_judge | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.10 | 100 | 500 | 0.016 | 0.011 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 0.750 | True |
| blind_features_judge | certified | 0.10 | 200 | 500 | 0.778 | 0.358 | 0.000 / 0.420 / 0.556 | 0.022 [0.011, 0.039] | 0.028 | True |
| blind_features_judge | certified | 0.10 | 400 | 500 | 0.948 | 0.521 | 0.391 / 0.554 / 0.651 | 0.028 [0.015, 0.047] | 0.030 | True |
| blind_features_judge | certified | 0.10 | 800 | 500 | 0.996 | 0.627 | 0.558 / 0.634 / 0.696 | 0.028 [0.015, 0.047] | 0.028 | True |
| blind_features_judge | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.25 | 100 | 500 | 0.006 | 0.005 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 1.000 | True |
| blind_features_judge | certified | 0.25 | 200 | 500 | 0.752 | 0.382 | 0.000 / 0.450 / 0.607 | 0.022 [0.011, 0.039] | 0.029 | True |
| blind_features_judge | certified | 0.25 | 400 | 500 | 0.964 | 0.565 | 0.444 / 0.587 / 0.691 | 0.020 [0.010, 0.036] | 0.021 | True |
| blind_features_judge | certified | 0.25 | 800 | 500 | 0.996 | 0.658 | 0.593 / 0.664 / 0.720 | 0.020 [0.010, 0.036] | 0.020 | True |
| blind_features_judge | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.50 | 200 | 500 | 0.254 | 0.163 | 0.000 / 0.000 / 0.647 | 0.018 [0.008, 0.034] | 0.071 | True |
| blind_features_judge | certified | 0.50 | 400 | 500 | 0.962 | 0.542 | 0.357 / 0.572 / 0.698 | 0.020 [0.010, 0.036] | 0.021 | True |
| blind_features_judge | certified | 0.50 | 800 | 500 | 0.962 | 0.637 | 0.574 / 0.663 / 0.731 | 0.014 [0.006, 0.029] | 0.015 | True |
| blind_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| blind_features_judge | certified | 0.75 | 400 | 500 | 0.300 | 0.193 | 0.000 / 0.000 / 0.663 | 0.014 [0.006, 0.029] | 0.047 | True |
| blind_features_judge | certified | 0.75 | 800 | 500 | 0.968 | 0.579 | 0.410 / 0.611 / 0.733 | 0.018 [0.008, 0.034] | 0.019 | True |
| blind_features_judge | heuristic | 1.00 | 25 | 500 | 0.062 | 0.062 | 0.000 / 0.000 / 0.000 | 0.062 [0.043, 0.087] | 1.000 | True |
| blind_features_judge | heuristic | 1.00 | 50 | 500 | 0.062 | 0.062 | 0.000 / 0.000 / 0.000 | 0.062 [0.043, 0.087] | 1.000 | True |
| blind_features_judge | heuristic | 1.00 | 100 | 500 | 0.896 | 0.675 | 0.000 / 0.732 / 0.889 | 0.456 [0.412, 0.501] | 0.509 | False |
| blind_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.744 | 0.640 / 0.750 / 0.846 | 0.402 [0.359, 0.446] | 0.402 | False |
| blind_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.764 | 0.692 / 0.761 / 0.842 | 0.322 [0.281, 0.365] | 0.322 | False |
| blind_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.772 | 0.722 / 0.772 / 0.820 | 0.142 [0.113, 0.176] | 0.142 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 100: blind_features_judge at f = 0.10, 0.011
- B = 200: blind_features_judge at f = 0.25, 0.382
- B = 400: blind_features_judge at f = 0.25, 0.565
- B = 800: blind_features_judge at f = 0.25, 0.658

B* (smallest B where the best arm fits, f > 0): 100
