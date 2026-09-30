# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.520 | 0.263 | 0.000 / 0.404 / 0.584 | 0.010 [0.000, 0.054] | 0.019 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.880 | 0.474 | 0.000 / 0.542 / 0.666 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.25 | 800 | 100 | 0.900 | 0.580 | 0.095 / 0.654 / 0.754 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 200 | 100 | 0.100 | 0.063 | 0.000 / 0.000 / 0.060 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.790 | 0.437 | 0.000 / 0.511 / 0.693 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.900 | 0.592 | 0.143 / 0.652 / 0.752 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.755 | 0.645 / 0.770 / 0.851 | 0.220 [0.143, 0.314] | 0.220 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.777 | 0.686 / 0.790 / 0.844 | 0.130 [0.071, 0.212] | 0.130 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.803 | 0.752 / 0.814 / 0.855 | 0.130 [0.071, 0.212] | 0.130 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.690 | 0.362 | 0.000 / 0.455 / 0.627 | 0.010 [0.000, 0.054] | 0.014 | True |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.940 | 0.562 | 0.437 / 0.586 / 0.693 | 0.010 [0.000, 0.054] | 0.011 | True |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.970 | 0.669 | 0.618 / 0.681 / 0.752 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.200 | 0.126 | 0.000 / 0.000 / 0.613 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.920 | 0.523 | 0.322 / 0.573 / 0.704 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 0.990 | 0.669 | 0.581 / 0.680 / 0.747 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.772 | 0.661 / 0.771 / 0.866 | 0.270 [0.186, 0.368] | 0.270 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.778 | 0.697 / 0.774 / 0.856 | 0.130 [0.071, 0.212] | 0.130 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.804 | 0.748 / 0.803 / 0.864 | 0.110 [0.056, 0.188] | 0.110 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.120 | 0.056 | 0.000 / 0.000 / 0.368 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.250 | 0.113 | 0.000 / 0.000 / 0.526 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.380 | 0.183 | 0.000 / 0.000 / 0.526 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.880 | 0.482 | 0.000 / 0.526 / 0.624 | 0.230 [0.152, 0.325] | 0.261 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.960 | 0.512 | 0.526 / 0.526 / 0.535 | 0.100 [0.049, 0.176] | 0.104 | True |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 1.000 | 0.528 | 0.526 / 0.526 / 0.526 | 0.020 [0.002, 0.070] | 0.020 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features_judge at f = 0.25, 0.362
- B = 400: gemma_features_judge at f = 0.25, 0.562
- B = 800: gemma_features_judge at f = 0.25, 0.669

B* (smallest B where the best arm fits, f > 0): 200
