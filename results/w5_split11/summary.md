# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma_features | certified | 0.25 | 200 | 100 | 0.760 | 0.399 | 0.000 / 0.463 / 0.653 | 0.080 [0.035, 0.152] | 0.105 | True |
| gemma_features | certified | 0.25 | 400 | 100 | 0.960 | 0.598 | 0.489 / 0.622 / 0.742 | 0.140 [0.079, 0.224] | 0.146 | False |
| gemma_features | certified | 0.25 | 800 | 100 | 0.930 | 0.625 | 0.087 / 0.704 / 0.779 | 0.270 [0.186, 0.368] | 0.290 | False |
| gemma_features | certified | 0.50 | 200 | 100 | 0.250 | 0.165 | 0.000 / 0.000 / 0.685 | 0.060 [0.022, 0.126] | 0.240 | True |
| gemma_features | certified | 0.50 | 400 | 100 | 0.940 | 0.555 | 0.329 / 0.584 / 0.752 | 0.100 [0.049, 0.176] | 0.106 | True |
| gemma_features | certified | 0.50 | 800 | 100 | 0.900 | 0.627 | 0.439 / 0.696 / 0.785 | 0.180 [0.110, 0.269] | 0.200 | False |
| gemma_features | heuristic | 1.00 | 200 | 100 | 1.000 | 0.803 | 0.708 / 0.802 / 0.908 | 0.820 [0.731, 0.890] | 0.820 | False |
| gemma_features | heuristic | 1.00 | 400 | 100 | 1.000 | 0.827 | 0.762 / 0.825 / 0.885 | 0.910 [0.836, 0.958] | 0.910 | False |
| gemma_features | heuristic | 1.00 | 800 | 100 | 1.000 | 0.836 | 0.794 / 0.842 / 0.875 | 0.940 [0.874, 0.978] | 0.940 | False |
| gemma_features_judge | certified | 0.25 | 200 | 100 | 0.840 | 0.474 | 0.000 / 0.529 / 0.684 | 0.110 [0.056, 0.188] | 0.131 | False |
| gemma_features_judge | certified | 0.25 | 400 | 100 | 0.980 | 0.643 | 0.548 / 0.656 / 0.757 | 0.140 [0.079, 0.224] | 0.143 | False |
| gemma_features_judge | certified | 0.25 | 800 | 100 | 0.960 | 0.693 | 0.644 / 0.724 / 0.788 | 0.170 [0.102, 0.258] | 0.177 | False |
| gemma_features_judge | certified | 0.50 | 200 | 100 | 0.380 | 0.254 | 0.000 / 0.000 / 0.699 | 0.080 [0.035, 0.152] | 0.211 | True |
| gemma_features_judge | certified | 0.50 | 400 | 100 | 0.970 | 0.624 | 0.498 / 0.638 / 0.783 | 0.110 [0.056, 0.188] | 0.113 | False |
| gemma_features_judge | certified | 0.50 | 800 | 100 | 1.000 | 0.726 | 0.653 / 0.726 / 0.800 | 0.170 [0.102, 0.258] | 0.170 | False |
| gemma_features_judge | heuristic | 1.00 | 200 | 100 | 1.000 | 0.821 | 0.727 / 0.823 / 0.924 | 0.740 [0.643, 0.823] | 0.740 | False |
| gemma_features_judge | heuristic | 1.00 | 400 | 100 | 1.000 | 0.837 | 0.765 / 0.835 / 0.904 | 0.760 [0.664, 0.840] | 0.760 | False |
| gemma_features_judge | heuristic | 1.00 | 800 | 100 | 1.000 | 0.842 | 0.802 / 0.846 / 0.875 | 0.950 [0.887, 0.984] | 0.950 | False |
| gemma_judge_0shot | certified | 0.00 | 200 | 100 | 0.180 | 0.075 | 0.000 / 0.000 / 0.346 | 0.010 [0.000, 0.054] | 0.056 | True |
| gemma_judge_0shot | certified | 0.00 | 400 | 100 | 0.380 | 0.172 | 0.000 / 0.000 / 0.520 | 0.020 [0.002, 0.070] | 0.053 | True |
| gemma_judge_0shot | certified | 0.00 | 800 | 100 | 0.590 | 0.280 | 0.000 / 0.394 / 0.520 | 0.000 [0.000, 0.036] | 0.000 | True |
| gemma_judge_0shot | heuristic | 1.00 | 200 | 100 | 0.960 | 0.514 | 0.394 / 0.520 / 0.621 | 0.300 [0.212, 0.400] | 0.312 | False |
| gemma_judge_0shot | heuristic | 1.00 | 400 | 100 | 0.980 | 0.530 | 0.520 / 0.520 / 0.621 | 0.290 [0.204, 0.389] | 0.296 | False |
| gemma_judge_0shot | heuristic | 1.00 | 800 | 100 | 0.990 | 0.518 | 0.520 / 0.520 / 0.520 | 0.050 [0.016, 0.113] | 0.051 | True |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 200: gemma_features at f = 0.25, 0.399
- B = 400: gemma_features at f = 0.50, 0.555
- B = 800: gemma_judge_0shot at f = 0.00, 0.280

B* (smallest B where the best arm fits, f > 0): 200
