# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.600 | 0.321 | 0.000 / 0.442 / 0.617 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.870 | 0.470 | 0.000 / 0.530 / 0.675 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.940 | 0.599 | 0.144 / 0.662 / 0.736 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.250 | 0.164 | 0.000 / 0.000 / 0.659 | 0.030 [0.006, 0.085] | 0.120 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.740 | 0.405 | 0.000 / 0.504 / 0.685 | 0.010 [0.000, 0.054] | 0.014 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.880 | 0.563 | 0.000 / 0.651 / 0.753 | 0.020 [0.002, 0.070] | 0.023 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.766 | 0.627 / 0.782 / 0.895 | 0.490 [0.389, 0.592] | 0.490 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.786 | 0.711 / 0.786 / 0.863 | 0.380 [0.285, 0.483] | 0.380 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.808 | 0.769 / 0.811 / 0.846 | 0.350 [0.257, 0.452] | 0.350 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.730 | 0.396 | 0.000 / 0.477 / 0.650 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.960 | 0.582 | 0.490 / 0.610 / 0.722 | 0.030 [0.006, 0.085] | 0.031 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.960 | 0.658 | 0.598 / 0.700 / 0.754 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.310 | 0.205 | 0.000 / 0.000 / 0.673 | 0.010 [0.000, 0.054] | 0.032 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.900 | 0.520 | 0.257 / 0.571 / 0.736 | 0.020 [0.002, 0.070] | 0.022 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.678 | 0.583 / 0.704 / 0.769 | 0.020 [0.002, 0.070] | 0.020 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.794 | 0.646 / 0.799 / 0.921 | 0.480 [0.379, 0.582] | 0.480 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.808 | 0.736 / 0.806 / 0.887 | 0.410 [0.313, 0.513] | 0.410 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.824 | 0.779 / 0.824 / 0.872 | 0.390 [0.294, 0.493] | 0.390 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.240 | 0.112 | 0.000 / 0.000 / 0.543 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.440 | 0.221 | 0.000 / 0.000 / 0.543 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.850 | 0.448 | 0.000 / 0.543 / 0.543 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.970 | 0.555 | 0.531 / 0.543 / 0.639 | 0.410 [0.313, 0.513] | 0.423 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 1.000 | 0.551 | 0.543 / 0.543 / 0.621 | 0.130 [0.071, 0.212] | 0.130 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.547 | 0.543 / 0.543 / 0.543 | 0.040 [0.011, 0.099] | 0.040 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.396
- B = 400: gemma_features_judge at f = 0.25, 0.582
- B = 800: gemma_features_judge at f = 0.50, 0.678

B* (smallest B where the best arm fits, f > 0): 200
