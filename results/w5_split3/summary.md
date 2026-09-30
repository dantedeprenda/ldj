# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.650 | 0.350 | 0.000 / 0.453 / 0.631 | 0.030 [0.006, 0.085] | 0.046 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.990 | 0.611 | 0.482 / 0.628 / 0.739 | 0.070 [0.029, 0.139] | 0.071 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 1.000 | 0.679 | 0.605 / 0.703 / 0.776 | 0.140 [0.079, 0.224] | 0.140 | False |
| gemma_features | certified | 0.50 | 200 | 100 | 0.220 | 0.152 | 0.000 / 0.000 / 0.684 | 0.040 [0.011, 0.099] | 0.182 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.930 | 0.559 | 0.394 / 0.599 / 0.741 | 0.050 [0.016, 0.113] | 0.054 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.920 | 0.649 | 0.585 / 0.701 / 0.791 | 0.120 [0.064, 0.200] | 0.130 | False |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.797 | 0.687 / 0.812 / 0.891 | 0.710 [0.611, 0.796] | 0.710 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.817 | 0.754 / 0.812 / 0.889 | 0.750 [0.653, 0.831] | 0.750 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.841 | 0.803 / 0.843 / 0.883 | 0.920 [0.848, 0.965] | 0.920 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.740 | 0.414 | 0.000 / 0.494 / 0.696 | 0.030 [0.006, 0.085] | 0.041 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.980 | 0.627 | 0.515 / 0.651 / 0.749 | 0.080 [0.035, 0.152] | 0.082 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 1.000 | 0.732 | 0.654 / 0.742 / 0.798 | 0.260 [0.177, 0.357] | 0.260 | False |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.320 | 0.218 | 0.000 / 0.000 / 0.705 | 0.030 [0.006, 0.085] | 0.094 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.960 | 0.603 | 0.482 / 0.639 / 0.747 | 0.020 [0.002, 0.070] | 0.021 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 1.000 | 0.732 | 0.657 / 0.741 / 0.802 | 0.100 [0.049, 0.176] | 0.100 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.821 | 0.733 / 0.826 / 0.902 | 0.730 [0.632, 0.814] | 0.730 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.837 | 0.772 / 0.833 / 0.901 | 0.790 [0.697, 0.865] | 0.790 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.860 | 0.822 / 0.860 / 0.896 | 0.930 [0.861, 0.971] | 0.930 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.140 | 0.068 | 0.000 / 0.000 / 0.368 | 0.020 [0.002, 0.070] | 0.143 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.330 | 0.158 | 0.000 / 0.000 / 0.533 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.800 | 0.399 | 0.000 / 0.533 / 0.533 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.940 | 0.512 | 0.520 / 0.533 / 0.617 | 0.210 [0.135, 0.303] | 0.223 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.528 | 0.533 / 0.533 / 0.540 | 0.100 [0.049, 0.176] | 0.102 | True |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.538 | 0.533 / 0.533 / 0.533 | 0.070 [0.029, 0.139] | 0.070 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.414
- B = 400: gemma_features_judge at f = 0.25, 0.627
- B = 800: gemma_features_judge at f = 0.50, 0.732

B* (smallest B where the best arm fits, f > 0): 200
