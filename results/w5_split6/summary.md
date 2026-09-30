# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.660 | 0.337 | 0.000 / 0.443 / 0.619 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.870 | 0.498 | 0.000 / 0.568 / 0.667 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.900 | 0.576 | 0.099 / 0.649 / 0.735 | 0.030 [0.006, 0.085] | 0.033 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.180 | 0.119 | 0.000 / 0.000 / 0.658 | 0.020 [0.002, 0.070] | 0.111 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.850 | 0.479 | 0.000 / 0.548 / 0.699 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.850 | 0.537 | 0.000 / 0.637 / 0.743 | 0.010 [0.000, 0.054] | 0.012 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.769 | 0.638 / 0.784 / 0.886 | 0.470 [0.369, 0.572] | 0.470 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.805 | 0.747 / 0.812 / 0.869 | 0.600 [0.497, 0.697] | 0.600 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.815 | 0.759 / 0.819 / 0.865 | 0.530 [0.428, 0.631] | 0.530 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.790 | 0.424 | 0.000 / 0.493 / 0.646 | 0.010 [0.000, 0.054] | 0.013 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.970 | 0.608 | 0.492 / 0.641 / 0.713 | 0.010 [0.000, 0.054] | 0.010 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.960 | 0.678 | 0.622 / 0.711 / 0.776 | 0.070 [0.029, 0.139] | 0.073 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.260 | 0.169 | 0.000 / 0.000 / 0.643 | 0.010 [0.000, 0.054] | 0.038 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.960 | 0.574 | 0.374 / 0.605 / 0.719 | 0.010 [0.000, 0.054] | 0.010 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.980 | 0.686 | 0.587 / 0.704 / 0.777 | 0.030 [0.006, 0.085] | 0.031 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.797 | 0.673 / 0.807 / 0.900 | 0.530 [0.428, 0.631] | 0.530 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.824 | 0.759 / 0.831 / 0.890 | 0.640 [0.538, 0.734] | 0.640 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.835 | 0.791 / 0.835 / 0.883 | 0.540 [0.437, 0.640] | 0.540 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.230 | 0.101 | 0.000 / 0.000 / 0.417 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.450 | 0.215 | 0.000 / 0.000 / 0.534 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.790 | 0.400 | 0.000 / 0.534 / 0.534 | 0.010 [0.000, 0.054] | 0.013 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.980 | 0.544 | 0.417 / 0.534 / 0.638 | 0.360 [0.266, 0.462] | 0.367 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.546 | 0.534 / 0.534 / 0.638 | 0.220 [0.143, 0.314] | 0.224 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.556 | 0.534 / 0.534 / 0.621 | 0.250 [0.169, 0.347] | 0.250 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.424
- B = 400: gemma_features_judge at f = 0.25, 0.608
- B = 800: gemma_features_judge at f = 0.50, 0.686

B* (smallest B where the best arm fits, f > 0): 200
