# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.600 | 0.307 | 0.000 / 0.424 / 0.582 | 0.020 [0.002, 0.070] | 0.033 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.930 | 0.522 | 0.322 / 0.557 / 0.674 | 0.020 [0.002, 0.070] | 0.022 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.970 | 0.589 | 0.109 / 0.650 / 0.740 | 0.040 [0.011, 0.099] | 0.041 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.190 | 0.125 | 0.000 / 0.000 / 0.645 | 0.010 [0.000, 0.054] | 0.053 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.840 | 0.446 | 0.000 / 0.510 / 0.667 | 0.030 [0.006, 0.085] | 0.036 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.890 | 0.582 | 0.000 / 0.641 / 0.748 | 0.050 [0.016, 0.113] | 0.056 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.767 | 0.637 / 0.773 / 0.862 | 0.480 [0.379, 0.582] | 0.480 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.778 | 0.691 / 0.776 / 0.855 | 0.420 [0.322, 0.523] | 0.420 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.801 | 0.741 / 0.801 / 0.863 | 0.460 [0.360, 0.563] | 0.460 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.850 | 0.446 | 0.000 / 0.490 / 0.657 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.970 | 0.577 | 0.437 / 0.595 / 0.716 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.990 | 0.691 | 0.636 / 0.704 / 0.758 | 0.020 [0.002, 0.070] | 0.020 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.270 | 0.179 | 0.000 / 0.000 / 0.661 | 0.010 [0.000, 0.054] | 0.037 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.960 | 0.547 | 0.366 / 0.571 / 0.720 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.686 | 0.599 / 0.693 / 0.774 | 0.030 [0.006, 0.085] | 0.030 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.791 | 0.688 / 0.801 / 0.881 | 0.490 [0.389, 0.592] | 0.490 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.798 | 0.721 / 0.797 / 0.879 | 0.350 [0.257, 0.452] | 0.350 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.818 | 0.766 / 0.817 / 0.863 | 0.380 [0.285, 0.483] | 0.380 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.140 | 0.062 | 0.000 / 0.000 / 0.357 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.250 | 0.110 | 0.000 / 0.000 / 0.532 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.640 | 0.292 | 0.000 / 0.357 / 0.532 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.960 | 0.511 | 0.403 / 0.532 / 0.623 | 0.150 [0.086, 0.235] | 0.156 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.960 | 0.507 | 0.519 / 0.532 / 0.532 | 0.060 [0.022, 0.126] | 0.062 | True |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.533 | 0.532 / 0.532 / 0.532 | 0.030 [0.006, 0.085] | 0.030 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.446
- B = 400: gemma_features_judge at f = 0.25, 0.577
- B = 800: gemma_features_judge at f = 0.25, 0.691

B* (smallest B where the best arm fits, f > 0): 200
