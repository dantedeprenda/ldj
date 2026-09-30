# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| bgeL_logreg | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.10 | 400 | 500 | 0.004 | 0.001 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| bgeL_logreg | certified | 0.10 | 800 | 500 | 0.004 | 0.001 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| bgeL_logreg | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.25 | 400 | 500 | 0.002 | 0.000 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| bgeL_logreg | certified | 0.25 | 800 | 500 | 0.002 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.50 | 400 | 500 | 0.002 | 0.001 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| bgeL_logreg | certified | 0.50 | 800 | 500 | 0.004 | 0.001 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | 0.000 | True |
| bgeL_logreg | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 400 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| bgeL_logreg | certified | 0.75 | 800 | 500 | 0.002 | 0.001 | 0.000 / 0.000 / 0.000 | 0.002 [0.000, 0.011] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 25 | 500 | 0.014 | 0.014 | 0.000 / 0.000 / 0.000 | 0.014 [0.006, 0.029] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 50 | 500 | 0.008 | 0.008 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 1.000 | True |
| bgeL_logreg | heuristic | 1.00 | 100 | 500 | 0.080 | 0.055 | 0.000 / 0.000 / 0.000 | 0.080 [0.058, 0.107] | 1.000 | False |
| bgeL_logreg | heuristic | 1.00 | 200 | 500 | 0.112 | 0.052 | 0.000 / 0.000 / 0.330 | 0.112 [0.086, 0.143] | 1.000 | False |
| bgeL_logreg | heuristic | 1.00 | 400 | 500 | 0.194 | 0.065 | 0.000 / 0.000 / 0.326 | 0.188 [0.155, 0.225] | 0.969 | False |
| bgeL_logreg | heuristic | 1.00 | 800 | 500 | 0.310 | 0.068 | 0.000 / 0.000 / 0.251 | 0.254 [0.216, 0.295] | 0.819 | False |
| jev_features | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.10 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.10 | 200 | 500 | 0.024 | 0.010 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 0.250 | True |
| jev_features | certified | 0.10 | 400 | 500 | 0.178 | 0.047 | 0.000 / 0.000 / 0.213 | 0.008 [0.002, 0.020] | 0.045 | True |
| jev_features | certified | 0.10 | 800 | 500 | 0.412 | 0.096 | 0.000 / 0.000 / 0.306 | 0.010 [0.003, 0.023] | 0.024 | True |
| jev_features | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.25 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.25 | 200 | 500 | 0.028 | 0.013 | 0.000 / 0.000 / 0.000 | 0.012 [0.004, 0.026] | 0.429 | True |
| jev_features | certified | 0.25 | 400 | 500 | 0.176 | 0.057 | 0.000 / 0.000 / 0.273 | 0.008 [0.002, 0.020] | 0.045 | True |
| jev_features | certified | 0.25 | 800 | 500 | 0.422 | 0.105 | 0.000 / 0.000 / 0.345 | 0.012 [0.004, 0.026] | 0.028 | True |
| jev_features | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.50 | 200 | 500 | 0.006 | 0.004 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 1.000 | True |
| jev_features | certified | 0.50 | 400 | 500 | 0.118 | 0.050 | 0.000 / 0.000 / 0.335 | 0.022 [0.011, 0.039] | 0.186 | True |
| jev_features | certified | 0.50 | 800 | 500 | 0.296 | 0.090 | 0.000 / 0.000 / 0.325 | 0.012 [0.004, 0.026] | 0.041 | True |
| jev_features | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| jev_features | certified | 0.75 | 400 | 500 | 0.004 | 0.003 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| jev_features | certified | 0.75 | 800 | 500 | 0.146 | 0.061 | 0.000 / 0.000 / 0.348 | 0.010 [0.003, 0.023] | 0.068 | True |
| jev_features | heuristic | 1.00 | 25 | 500 | 0.008 | 0.008 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 1.000 | True |
| jev_features | heuristic | 1.00 | 50 | 500 | 0.004 | 0.004 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| jev_features | heuristic | 1.00 | 100 | 500 | 0.324 | 0.229 | 0.000 / 0.000 / 0.739 | 0.324 [0.283, 0.367] | 1.000 | False |
| jev_features | heuristic | 1.00 | 200 | 500 | 0.842 | 0.477 | 0.000 / 0.548 / 0.693 | 0.496 [0.451, 0.541] | 0.589 | False |
| jev_features | heuristic | 1.00 | 400 | 500 | 0.986 | 0.533 | 0.373 / 0.561 / 0.661 | 0.464 [0.420, 0.509] | 0.471 | False |
| jev_features | heuristic | 1.00 | 800 | 500 | 1.000 | 0.565 | 0.486 / 0.576 / 0.642 | 0.454 [0.410, 0.499] | 0.454 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: jev_features at f = 0.25, 0.013
- B = 400: jev_features at f = 0.25, 0.057
- B = 800: jev_features at f = 0.25, 0.105

B* (smallest B where the best arm fits, f > 0): 200
