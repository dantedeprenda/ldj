# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 200 | 500 | 0.002 | 0.001 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| bgeL_logreg | certified | 0.10 | 400 | 500 | 0.014 | 0.002 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 0.857 | True |
| bgeL_logreg | certified | 0.10 | 800 | 500 | 0.010 | 0.001 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 0.400 | True |
| bgeL_logreg | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 200 | 500 | 0.012 | 0.004 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 0.667 | True |
| bgeL_logreg | certified | 0.25 | 400 | 500 | 0.018 | 0.003 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.333 | True |
| bgeL_logreg | certified | 0.25 | 800 | 500 | 0.014 | 0.002 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.429 | True |
| bgeL_logreg | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 200 | 500 | 0.002 | 0.001 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| bgeL_logreg | certified | 0.50 | 400 | 500 | 0.016 | 0.005 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 0.750 | True |
| bgeL_logreg | certified | 0.50 | 800 | 500 | 0.022 | 0.004 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.273 | True |
| bgeL_logreg | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 400 | 500 | 0.008 | 0.005 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 1.000 | True |
| bgeL_logreg | certified | 0.75 | 800 | 500 | 0.034 | 0.010 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.176 | True |
| bgeL_logreg | heuristic | 1.00 | 25 | 500 | 0.076 | 0.076 | 0.000 / 0.000 / 0.000 | 0.076 [0.054, 0.103] | 1.000 | False |
| bgeL_logreg | heuristic | 1.00 | 50 | 500 | 0.036 | 0.035 | 0.000 / 0.000 / 0.000 | 0.036 [0.021, 0.056] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 100 | 500 | 0.250 | 0.159 | 0.000 / 0.000 / 0.643 | 0.250 [0.213, 0.290] | 1.000 | False |
| bgeL_logreg | heuristic | 1.00 | 200 | 500 | 0.338 | 0.176 | 0.000 / 0.000 / 0.600 | 0.322 [0.281, 0.365] | 0.953 | False |
| bgeL_logreg | heuristic | 1.00 | 400 | 500 | 0.456 | 0.194 | 0.000 / 0.000 / 0.567 | 0.334 [0.293, 0.377] | 0.732 | False |
| bgeL_logreg | heuristic | 1.00 | 800 | 500 | 0.642 | 0.241 | 0.000 / 0.248 / 0.546 | 0.336 [0.295, 0.379] | 0.523 | False |
| jev_features | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.10 | 100 | 500 | 0.018 | 0.010 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.333 | True |
| jev_features | certified | 0.10 | 200 | 500 | 0.116 | 0.044 | 0.000 / 0.000 / 0.270 | 0.006 [0.001, 0.017] | 0.052 | True |
| jev_features | certified | 0.10 | 400 | 500 | 0.386 | 0.124 | 0.000 / 0.000 / 0.437 | 0.016 [0.007, 0.031] | 0.041 | True |
| jev_features | certified | 0.10 | 800 | 500 | 0.602 | 0.242 | 0.000 / 0.113 / 0.605 | 0.012 [0.004, 0.026] | 0.020 | True |
| jev_features | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.25 | 100 | 500 | 0.020 | 0.013 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 0.600 | True |
| jev_features | certified | 0.25 | 200 | 500 | 0.158 | 0.069 | 0.000 / 0.000 / 0.359 | 0.012 [0.004, 0.026] | 0.076 | True |
| jev_features | certified | 0.25 | 400 | 500 | 0.424 | 0.158 | 0.000 / 0.000 / 0.539 | 0.012 [0.004, 0.026] | 0.028 | True |
| jev_features | certified | 0.25 | 800 | 500 | 0.660 | 0.273 | 0.000 / 0.179 / 0.626 | 0.016 [0.007, 0.031] | 0.024 | True |
| jev_features | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 200 | 500 | 0.126 | 0.071 | 0.000 / 0.000 / 0.484 | 0.020 [0.010, 0.036] | 0.159 | True |
| jev_features | certified | 0.50 | 400 | 500 | 0.350 | 0.141 | 0.000 / 0.000 / 0.468 | 0.010 [0.003, 0.023] | 0.029 | True |
| jev_features | certified | 0.50 | 800 | 500 | 0.560 | 0.223 | 0.000 / 0.146 / 0.606 | 0.014 [0.006, 0.029] | 0.025 | True |
| jev_features | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 400 | 500 | 0.124 | 0.070 | 0.000 / 0.000 / 0.492 | 0.008 [0.002, 0.020] | 0.065 | True |
| jev_features | certified | 0.75 | 800 | 500 | 0.398 | 0.170 | 0.000 / 0.000 / 0.580 | 0.018 [0.008, 0.034] | 0.045 | True |
| jev_features | heuristic | 1.00 | 25 | 500 | 0.054 | 0.054 | 0.000 / 0.000 / 0.000 | 0.054 [0.036, 0.078] | 1.000 | True |
| jev_features | heuristic | 1.00 | 50 | 500 | 0.078 | 0.071 | 0.000 / 0.000 / 0.000 | 0.078 [0.056, 0.105] | 1.000 | False |
| jev_features | heuristic | 1.00 | 100 | 500 | 0.832 | 0.571 | 0.000 / 0.658 / 0.813 | 0.440 [0.396, 0.485] | 0.529 | False |
| jev_features | heuristic | 1.00 | 200 | 500 | 0.988 | 0.654 | 0.492 / 0.673 / 0.789 | 0.400 [0.357, 0.444] | 0.405 | False |
| jev_features | heuristic | 1.00 | 400 | 500 | 1.000 | 0.683 | 0.589 / 0.692 / 0.766 | 0.394 [0.351, 0.438] | 0.394 | False |
| jev_features | heuristic | 1.00 | 800 | 500 | 1.000 | 0.698 | 0.639 / 0.699 / 0.758 | 0.366 [0.324, 0.410] | 0.366 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 100: jev_features at f = 0.25, 0.013
- B = 200: jev_features at f = 0.50, 0.071
- B = 400: jev_features at f = 0.25, 0.158
- B = 800: jev_features at f = 0.25, 0.273

B* (smallest B where the best arm fits, f > 0): 100
