# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.670 | 0.354 | 0.000 / 0.454 / 0.625 | 0.050 [0.016, 0.113] | 0.075 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.960 | 0.605 | 0.505 / 0.622 / 0.748 | 0.140 [0.079, 0.224] | 0.146 | False |
| gemma_features | certified | 0.25 | 800 | 100 | 0.890 | 0.600 | 0.000 / 0.699 / 0.775 | 0.170 [0.102, 0.258] | 0.191 | False |
| gemma_features | certified | 0.50 | 200 | 100 | 0.230 | 0.158 | 0.000 / 0.000 / 0.689 | 0.060 [0.022, 0.126] | 0.261 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.770 | 0.479 | 0.000 / 0.585 / 0.773 | 0.100 [0.049, 0.176] | 0.130 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.870 | 0.608 | 0.000 / 0.702 / 0.812 | 0.230 [0.152, 0.325] | 0.264 | False |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.819 | 0.699 / 0.813 / 0.923 | 0.800 [0.708, 0.873] | 0.800 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.839 | 0.758 / 0.842 / 0.903 | 0.860 [0.776, 0.921] | 0.860 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.841 | 0.792 / 0.839 / 0.892 | 0.930 [0.861, 0.971] | 0.930 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.830 | 0.445 | 0.000 / 0.491 / 0.651 | 0.040 [0.011, 0.099] | 0.048 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.990 | 0.647 | 0.547 / 0.649 / 0.766 | 0.100 [0.049, 0.176] | 0.101 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.960 | 0.679 | 0.609 / 0.725 / 0.799 | 0.220 [0.143, 0.314] | 0.229 | False |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.300 | 0.207 | 0.000 / 0.000 / 0.714 | 0.080 [0.035, 0.152] | 0.267 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.910 | 0.575 | 0.396 / 0.615 / 0.776 | 0.090 [0.042, 0.164] | 0.099 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.970 | 0.704 | 0.626 / 0.723 / 0.814 | 0.210 [0.135, 0.303] | 0.216 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.830 | 0.725 / 0.836 / 0.932 | 0.760 [0.664, 0.840] | 0.760 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.850 | 0.781 / 0.854 / 0.916 | 0.830 [0.742, 0.898] | 0.830 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.847 | 0.801 / 0.844 / 0.900 | 0.900 [0.824, 0.951] | 0.900 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.160 | 0.074 | 0.000 / 0.000 / 0.410 | 0.010 [0.000, 0.054] | 0.062 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.430 | 0.215 | 0.000 / 0.000 / 0.530 | 0.010 [0.000, 0.054] | 0.023 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.670 | 0.338 | 0.000 / 0.530 / 0.530 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.940 | 0.530 | 0.410 / 0.530 / 0.633 | 0.400 [0.303, 0.503] | 0.426 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.990 | 0.559 | 0.530 / 0.530 / 0.633 | 0.360 [0.266, 0.462] | 0.364 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.549 | 0.530 / 0.530 / 0.633 | 0.220 [0.143, 0.314] | 0.220 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.445
- B = 400: gemma_features_judge at f = 0.25, 0.647
- B = 800: gemma_judge_0shot at f = 0.00, 0.338

B* (smallest B where the best arm fits, f > 0): 200
