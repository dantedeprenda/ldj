# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.610 | 0.315 | 0.000 / 0.426 / 0.609 | 0.010 [0.000, 0.054] | 0.016 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.890 | 0.500 | 0.000 / 0.549 / 0.673 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.960 | 0.601 | 0.150 / 0.663 / 0.761 | 0.030 [0.006, 0.085] | 0.031 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.170 | 0.110 | 0.000 / 0.000 / 0.628 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.800 | 0.448 | 0.000 / 0.510 / 0.712 | 0.010 [0.000, 0.054] | 0.013 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.900 | 0.551 | 0.139 / 0.622 / 0.744 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.762 | 0.654 / 0.774 / 0.881 | 0.280 [0.195, 0.379] | 0.280 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.798 | 0.721 / 0.799 / 0.871 | 0.310 [0.221, 0.410] | 0.310 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.814 | 0.762 / 0.814 / 0.867 | 0.340 [0.248, 0.442] | 0.340 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.760 | 0.406 | 0.000 / 0.479 / 0.670 | 0.010 [0.000, 0.054] | 0.013 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.940 | 0.566 | 0.447 / 0.604 / 0.711 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.980 | 0.653 | 0.579 / 0.699 / 0.779 | 0.020 [0.002, 0.070] | 0.020 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.260 | 0.172 | 0.000 / 0.000 / 0.652 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.920 | 0.555 | 0.305 / 0.601 / 0.731 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.970 | 0.662 | 0.580 / 0.679 / 0.784 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.782 | 0.673 / 0.779 / 0.874 | 0.340 [0.248, 0.442] | 0.340 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.813 | 0.742 / 0.811 / 0.885 | 0.330 [0.239, 0.431] | 0.330 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.822 | 0.782 / 0.824 / 0.864 | 0.210 [0.135, 0.303] | 0.210 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.120 | 0.052 | 0.000 / 0.000 / 0.338 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.190 | 0.077 | 0.000 / 0.000 / 0.339 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.370 | 0.163 | 0.000 / 0.000 / 0.515 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.920 | 0.474 | 0.347 / 0.515 / 0.615 | 0.200 [0.127, 0.292] | 0.217 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.506 | 0.515 / 0.515 / 0.595 | 0.110 [0.056, 0.188] | 0.112 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.512 | 0.515 / 0.515 / 0.515 | 0.060 [0.022, 0.126] | 0.060 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.406
- B = 400: gemma_features_judge at f = 0.25, 0.566
- B = 800: gemma_features_judge at f = 0.50, 0.662

B* (smallest B where the best arm fits, f > 0): 200
