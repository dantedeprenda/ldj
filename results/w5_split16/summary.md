# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.650 | 0.334 | 0.000 / 0.429 / 0.628 | 0.020 [0.002, 0.070] | 0.031 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.910 | 0.538 | 0.197 / 0.588 / 0.731 | 0.100 [0.049, 0.176] | 0.110 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.920 | 0.590 | 0.108 / 0.688 / 0.765 | 0.070 [0.029, 0.139] | 0.076 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.220 | 0.141 | 0.000 / 0.000 / 0.619 | 0.010 [0.000, 0.054] | 0.045 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.860 | 0.490 | 0.000 / 0.536 / 0.729 | 0.050 [0.016, 0.113] | 0.058 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.900 | 0.616 | 0.237 / 0.697 / 0.783 | 0.110 [0.056, 0.188] | 0.122 | False |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.805 | 0.702 / 0.806 / 0.894 | 0.710 [0.611, 0.796] | 0.710 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.813 | 0.757 / 0.818 / 0.881 | 0.710 [0.611, 0.796] | 0.710 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.835 | 0.789 / 0.841 / 0.880 | 0.870 [0.788, 0.929] | 0.870 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.790 | 0.416 | 0.000 / 0.469 / 0.640 | 0.040 [0.011, 0.099] | 0.051 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.930 | 0.596 | 0.479 / 0.634 / 0.760 | 0.060 [0.022, 0.126] | 0.065 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.970 | 0.705 | 0.647 / 0.724 / 0.804 | 0.170 [0.102, 0.258] | 0.175 | False |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.270 | 0.177 | 0.000 / 0.000 / 0.641 | 0.030 [0.006, 0.085] | 0.111 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.960 | 0.586 | 0.422 / 0.617 / 0.764 | 0.060 [0.022, 0.126] | 0.062 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.720 | 0.620 / 0.742 / 0.814 | 0.160 [0.094, 0.247] | 0.162 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.830 | 0.723 / 0.837 / 0.917 | 0.750 [0.653, 0.831] | 0.750 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.838 | 0.762 / 0.838 / 0.912 | 0.790 [0.697, 0.865] | 0.790 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.858 | 0.813 / 0.858 / 0.909 | 0.890 [0.812, 0.944] | 0.890 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.250 | 0.109 | 0.000 / 0.000 / 0.411 | 0.010 [0.000, 0.054] | 0.040 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.440 | 0.197 | 0.000 / 0.000 / 0.527 | 0.020 [0.002, 0.070] | 0.045 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.780 | 0.367 | 0.000 / 0.463 / 0.527 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.960 | 0.532 | 0.399 / 0.527 / 0.628 | 0.370 [0.276, 0.472] | 0.385 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 1.000 | 0.535 | 0.527 / 0.527 / 0.628 | 0.180 [0.110, 0.269] | 0.180 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 0.990 | 0.531 | 0.527 / 0.527 / 0.535 | 0.100 [0.049, 0.176] | 0.101 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.416
- B = 400: gemma_features_judge at f = 0.25, 0.596
- B = 800: gemma_features at f = 0.25, 0.590

B* (smallest B where the best arm fits, f > 0): 200
