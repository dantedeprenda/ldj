# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 500 | 0.710 | 0.365 | 0.000 / 0.432 / 0.624 | 0.066 [0.046, 0.091] | 0.093 | True |
| gemma_features | certified | 0.25 | 400 | 500 | 0.902 | 0.535 | 0.176 / 0.592 / 0.713 | 0.110 [0.084, 0.141] | 0.122 | False |
| gemma_features | certified | 0.25 | 800 | 500 | 0.916 | 0.606 | 0.086 / 0.678 / 0.768 | 0.202 [0.168, 0.240] | 0.221 | False |
| gemma_features | certified | 0.50 | 200 | 500 | 0.248 | 0.158 | 0.000 / 0.000 / 0.642 | 0.038 [0.023, 0.059] | 0.153 | True |
| gemma_features | certified | 0.50 | 400 | 500 | 0.818 | 0.470 | 0.000 / 0.539 / 0.733 | 0.098 [0.073, 0.127] | 0.120 | False |
| gemma_features | certified | 0.50 | 800 | 500 | 0.894 | 0.603 | 0.000 / 0.671 / 0.781 | 0.156 [0.125, 0.191] | 0.174 | False |
| gemma_features | heuristic | 1.00 | 200 | 500 | 1.000 | 0.789 | 0.660 / 0.800 / 0.904 | 0.734 [0.693, 0.772] | 0.734 | False |
| gemma_features | heuristic | 1.00 | 400 | 500 | 1.000 | 0.812 | 0.727 / 0.815 / 0.890 | 0.812 [0.775, 0.845] | 0.812 | False |
| gemma_features | heuristic | 1.00 | 800 | 500 | 1.000 | 0.828 | 0.782 / 0.830 / 0.873 | 0.928 [0.902, 0.949] | 0.928 | False |
| gemma_features_judge | certified | 0.25 | 200 | 500 | 0.794 | 0.426 | 0.000 / 0.491 / 0.660 | 0.072 [0.051, 0.098] | 0.091 | False |
| gemma_features_judge | certified | 0.25 | 400 | 500 | 0.968 | 0.615 | 0.505 / 0.635 / 0.745 | 0.166 [0.134, 0.202] | 0.171 | False |
| gemma_features_judge | certified | 0.25 | 800 | 500 | 0.986 | 0.690 | 0.630 / 0.718 / 0.792 | 0.268 [0.230, 0.309] | 0.272 | False |
| gemma_features_judge | certified | 0.50 | 200 | 500 | 0.344 | 0.223 | 0.000 / 0.000 / 0.680 | 0.056 [0.038, 0.080] | 0.163 | True |
| gemma_features_judge | certified | 0.50 | 400 | 500 | 0.924 | 0.554 | 0.278 / 0.601 / 0.755 | 0.094 [0.070, 0.123] | 0.102 | False |
| gemma_features_judge | certified | 0.50 | 800 | 500 | 0.986 | 0.705 | 0.625 / 0.716 / 0.796 | 0.194 [0.160, 0.231] | 0.197 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.813 | 0.690 / 0.818 / 0.927 | 0.762 [0.722, 0.799] | 0.762 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.833 | 0.760 / 0.832 / 0.905 | 0.852 [0.818, 0.882] | 0.852 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.847 | 0.791 / 0.848 / 0.901 | 0.914 [0.886, 0.937] | 0.914 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 500 | 0.180 | 0.076 | 0.000 / 0.000 / 0.342 | 0.004 [0.000, 0.014] | 0.022 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 500 | 0.450 | 0.198 | 0.000 / 0.000 / 0.507 | 0.004 [0.000, 0.014] | 0.009 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 500 | 0.766 | 0.357 | 0.000 / 0.507 / 0.507 | 0.000 [0.000, 0.007] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 500 | 0.946 | 0.501 | 0.388 / 0.507 / 0.609 | 0.342 [0.300, 0.385] | 0.362 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 500 | 0.986 | 0.522 | 0.507 / 0.507 / 0.609 | 0.274 [0.235, 0.315] | 0.278 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 500 | 0.998 | 0.520 | 0.507 / 0.507 / 0.588 | 0.164 [0.133, 0.199] | 0.164 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features at f = 0.25, 0.365
- B = 400: gemma_judge_0shot at f = 0.00, 0.198
- B = 800: gemma_judge_0shot at f = 0.00, 0.357

B* (smallest B where the best arm fits, f > 0): 200
