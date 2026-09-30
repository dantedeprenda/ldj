# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.670 | 0.330 | 0.000 / 0.421 / 0.589 | 0.010 [0.000, 0.054] | 0.015 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.910 | 0.529 | 0.243 / 0.585 / 0.691 | 0.090 [0.042, 0.164] | 0.099 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.970 | 0.648 | 0.590 / 0.677 / 0.767 | 0.180 [0.110, 0.269] | 0.186 | False |
| gemma_features | certified | 0.50 | 200 | 100 | 0.250 | 0.160 | 0.000 / 0.000 / 0.635 | 0.030 [0.006, 0.085] | 0.120 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.840 | 0.489 | 0.000 / 0.569 / 0.699 | 0.060 [0.022, 0.126] | 0.071 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.930 | 0.622 | 0.496 / 0.682 / 0.775 | 0.150 [0.086, 0.235] | 0.161 | False |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.781 | 0.667 / 0.790 / 0.865 | 0.710 [0.611, 0.796] | 0.710 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.798 | 0.729 / 0.802 / 0.861 | 0.750 [0.653, 0.831] | 0.750 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.817 | 0.766 / 0.819 / 0.864 | 0.850 [0.765, 0.914] | 0.850 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.820 | 0.433 | 0.000 / 0.482 / 0.654 | 0.040 [0.011, 0.099] | 0.049 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.980 | 0.615 | 0.499 / 0.629 / 0.730 | 0.090 [0.042, 0.164] | 0.092 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 1.000 | 0.712 | 0.644 / 0.712 / 0.779 | 0.120 [0.064, 0.200] | 0.120 | False |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.330 | 0.208 | 0.000 / 0.000 / 0.650 | 0.010 [0.000, 0.054] | 0.030 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.970 | 0.591 | 0.462 / 0.612 / 0.729 | 0.060 [0.022, 0.126] | 0.062 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.980 | 0.695 | 0.601 / 0.716 / 0.796 | 0.170 [0.102, 0.258] | 0.173 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.804 | 0.695 / 0.800 / 0.911 | 0.710 [0.611, 0.796] | 0.710 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.814 | 0.746 / 0.810 / 0.881 | 0.740 [0.643, 0.823] | 0.740 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.832 | 0.788 / 0.833 / 0.875 | 0.810 [0.719, 0.882] | 0.810 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.240 | 0.101 | 0.000 / 0.000 / 0.399 | 0.010 [0.000, 0.054] | 0.042 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.410 | 0.187 | 0.000 / 0.000 / 0.519 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.870 | 0.424 | 0.000 / 0.519 / 0.519 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.960 | 0.529 | 0.519 / 0.519 / 0.620 | 0.360 [0.266, 0.462] | 0.375 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 1.000 | 0.544 | 0.519 / 0.519 / 0.620 | 0.260 [0.177, 0.357] | 0.260 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.531 | 0.519 / 0.519 / 0.602 | 0.120 [0.064, 0.200] | 0.120 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.433
- B = 400: gemma_features_judge at f = 0.25, 0.615
- B = 800: gemma_judge_0shot at f = 0.00, 0.424

B* (smallest B where the best arm fits, f > 0): 200
