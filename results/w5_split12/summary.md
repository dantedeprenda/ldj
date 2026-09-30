# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.660 | 0.331 | 0.000 / 0.436 / 0.596 | 0.020 [0.002, 0.070] | 0.030 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.910 | 0.495 | 0.203 / 0.553 / 0.639 | 0.020 [0.002, 0.070] | 0.022 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.930 | 0.573 | 0.096 / 0.635 / 0.707 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.180 | 0.111 | 0.000 / 0.000 / 0.598 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.900 | 0.480 | 0.245 / 0.536 / 0.654 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.920 | 0.583 | 0.490 / 0.635 / 0.736 | 0.020 [0.002, 0.070] | 0.022 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.750 | 0.651 / 0.747 / 0.849 | 0.420 [0.322, 0.523] | 0.420 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.765 | 0.673 / 0.772 / 0.848 | 0.280 [0.195, 0.379] | 0.280 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.783 | 0.734 / 0.782 / 0.834 | 0.220 [0.143, 0.314] | 0.220 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.760 | 0.406 | 0.000 / 0.482 / 0.652 | 0.010 [0.000, 0.054] | 0.013 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.920 | 0.571 | 0.478 / 0.617 / 0.711 | 0.030 [0.006, 0.085] | 0.033 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.960 | 0.645 | 0.600 / 0.681 / 0.738 | 0.030 [0.006, 0.085] | 0.031 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.290 | 0.184 | 0.000 / 0.000 / 0.643 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.960 | 0.562 | 0.383 / 0.601 / 0.698 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.667 | 0.567 / 0.682 / 0.759 | 0.020 [0.002, 0.070] | 0.020 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.784 | 0.678 / 0.782 / 0.891 | 0.470 [0.369, 0.572] | 0.470 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.794 | 0.723 / 0.795 / 0.860 | 0.430 [0.331, 0.533] | 0.430 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.799 | 0.760 / 0.795 / 0.850 | 0.230 [0.152, 0.325] | 0.230 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.250 | 0.111 | 0.000 / 0.000 / 0.521 | 0.020 [0.002, 0.070] | 0.080 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.380 | 0.170 | 0.000 / 0.000 / 0.521 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.730 | 0.351 | 0.000 / 0.521 / 0.521 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 1.000 | 0.544 | 0.521 / 0.521 / 0.627 | 0.320 [0.230, 0.421] | 0.320 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.531 | 0.521 / 0.521 / 0.627 | 0.250 [0.169, 0.347] | 0.255 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.530 | 0.521 / 0.521 / 0.605 | 0.110 [0.056, 0.188] | 0.110 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.406
- B = 400: gemma_features_judge at f = 0.25, 0.571
- B = 800: gemma_features_judge at f = 0.50, 0.667

B* (smallest B where the best arm fits, f > 0): 200
