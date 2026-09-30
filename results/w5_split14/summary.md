# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.660 | 0.364 | 0.000 / 0.466 / 0.651 | 0.090 [0.042, 0.164] | 0.136 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.920 | 0.551 | 0.272 / 0.603 / 0.724 | 0.070 [0.029, 0.139] | 0.076 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.870 | 0.558 | 0.000 / 0.669 / 0.763 | 0.080 [0.035, 0.152] | 0.092 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.230 | 0.162 | 0.000 / 0.000 / 0.699 | 0.080 [0.035, 0.152] | 0.348 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.840 | 0.474 | 0.000 / 0.529 / 0.721 | 0.060 [0.022, 0.126] | 0.071 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.910 | 0.598 | 0.152 / 0.677 / 0.772 | 0.070 [0.029, 0.139] | 0.077 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.793 | 0.684 / 0.800 / 0.894 | 0.700 [0.600, 0.788] | 0.700 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.817 | 0.756 / 0.818 / 0.874 | 0.800 [0.708, 0.873] | 0.800 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.823 | 0.776 / 0.824 / 0.865 | 0.770 [0.675, 0.848] | 0.770 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.850 | 0.463 | 0.000 / 0.485 / 0.680 | 0.080 [0.035, 0.152] | 0.094 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.950 | 0.598 | 0.479 / 0.639 / 0.736 | 0.050 [0.016, 0.113] | 0.053 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.890 | 0.632 | 0.000 / 0.708 / 0.783 | 0.040 [0.011, 0.099] | 0.045 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.290 | 0.197 | 0.000 / 0.000 / 0.690 | 0.050 [0.016, 0.113] | 0.172 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.940 | 0.563 | 0.324 / 0.606 / 0.735 | 0.050 [0.016, 0.113] | 0.053 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.980 | 0.692 | 0.600 / 0.726 / 0.804 | 0.090 [0.042, 0.164] | 0.092 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.801 | 0.690 / 0.804 / 0.890 | 0.650 [0.548, 0.743] | 0.650 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.832 | 0.759 / 0.831 / 0.892 | 0.730 [0.632, 0.814] | 0.730 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.829 | 0.783 / 0.832 / 0.872 | 0.650 [0.548, 0.743] | 0.650 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.190 | 0.082 | 0.000 / 0.000 / 0.368 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.480 | 0.219 | 0.000 / 0.000 / 0.524 | 0.010 [0.000, 0.054] | 0.021 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.800 | 0.392 | 0.000 / 0.524 / 0.524 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.960 | 0.524 | 0.419 / 0.524 / 0.624 | 0.340 [0.248, 0.442] | 0.354 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.990 | 0.542 | 0.524 / 0.524 / 0.624 | 0.290 [0.204, 0.389] | 0.293 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.542 | 0.524 / 0.524 / 0.614 | 0.190 [0.118, 0.281] | 0.190 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.463
- B = 400: gemma_features_judge at f = 0.25, 0.598
- B = 800: gemma_features_judge at f = 0.50, 0.692

B* (smallest B where the best arm fits, f > 0): 200
