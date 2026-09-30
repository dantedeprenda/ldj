# X4 allocation frontier (exploratory)

`useful`: share of resamples whose certificate automates something. `violation`: the unconditional rate the guarantee is about, with a Clopper-Pearson interval; `violation if useful` is a diagnostic. `consistent`: the interval's lower end is <= delta (the data do not show the guarantee failing; not a proof).

| method | arm | f | B | n | useful | automated (mean) | p10 / p50 / p90 | violation [95% CI] | violation if useful | consistent |
|---|---|---|---|---|---|---|---|---|---|---|
| llama_features | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.10 | 100 | 500 | 0.018 | 0.012 | 0.000 / 0.000 / 0.000 | 0.016 [0.007, 0.031] | 0.889 | True |
| llama_features | certified | 0.10 | 200 | 500 | 0.568 | 0.258 | 0.000 / 0.341 / 0.544 | 0.016 [0.007, 0.031] | 0.028 | True |
| llama_features | certified | 0.10 | 400 | 500 | 0.888 | 0.453 | 0.000 / 0.518 / 0.621 | 0.012 [0.004, 0.026] | 0.014 | True |
| llama_features | certified | 0.10 | 800 | 500 | 0.966 | 0.589 | 0.514 / 0.616 / 0.689 | 0.012 [0.004, 0.026] | 0.012 | True |
| llama_features | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.25 | 100 | 500 | 0.008 | 0.006 | 0.000 / 0.000 / 0.000 | 0.008 [0.002, 0.020] | 1.000 | True |
| llama_features | certified | 0.25 | 200 | 500 | 0.698 | 0.349 | 0.000 / 0.432 / 0.601 | 0.016 [0.007, 0.031] | 0.023 | True |
| llama_features | certified | 0.25 | 400 | 500 | 0.946 | 0.531 | 0.390 / 0.567 / 0.674 | 0.016 [0.007, 0.031] | 0.017 | True |
| llama_features | certified | 0.25 | 800 | 500 | 0.986 | 0.639 | 0.579 / 0.648 / 0.711 | 0.008 [0.002, 0.020] | 0.008 | True |
| llama_features | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.50 | 200 | 500 | 0.158 | 0.102 | 0.000 / 0.000 / 0.614 | 0.012 [0.004, 0.026] | 0.076 | True |
| llama_features | certified | 0.50 | 400 | 500 | 0.936 | 0.537 | 0.385 / 0.570 / 0.681 | 0.010 [0.003, 0.023] | 0.011 | True |
| llama_features | certified | 0.50 | 800 | 500 | 0.960 | 0.621 | 0.558 / 0.642 / 0.720 | 0.006 [0.001, 0.017] | 0.006 | True |
| llama_features | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features | certified | 0.75 | 400 | 500 | 0.286 | 0.187 | 0.000 / 0.000 / 0.665 | 0.014 [0.006, 0.029] | 0.049 | True |
| llama_features | certified | 0.75 | 800 | 500 | 0.964 | 0.579 | 0.485 / 0.597 / 0.713 | 0.006 [0.001, 0.017] | 0.006 | True |
| llama_features | heuristic | 1.00 | 25 | 500 | 0.056 | 0.056 | 0.000 / 0.000 / 0.000 | 0.056 [0.038, 0.080] | 1.000 | True |
| llama_features | heuristic | 1.00 | 50 | 500 | 0.050 | 0.050 | 0.000 / 0.000 / 0.000 | 0.050 [0.033, 0.073] | 1.000 | True |
| llama_features | heuristic | 1.00 | 100 | 500 | 0.882 | 0.666 | 0.000 / 0.730 / 0.886 | 0.488 [0.443, 0.533] | 0.553 | False |
| llama_features | heuristic | 1.00 | 200 | 500 | 1.000 | 0.746 | 0.634 / 0.745 / 0.858 | 0.420 [0.376, 0.465] | 0.420 | False |
| llama_features | heuristic | 1.00 | 400 | 500 | 1.000 | 0.762 | 0.686 / 0.761 / 0.835 | 0.344 [0.302, 0.387] | 0.344 | False |
| llama_features | heuristic | 1.00 | 800 | 500 | 1.000 | 0.774 | 0.724 / 0.776 / 0.821 | 0.346 [0.304, 0.390] | 0.346 | False |
| llama_features_judge | certified | 0.10 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.10 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.10 | 100 | 500 | 0.014 | 0.010 | 0.000 / 0.000 / 0.000 | 0.010 [0.003, 0.023] | 0.714 | True |
| llama_features_judge | certified | 0.10 | 200 | 500 | 0.804 | 0.373 | 0.000 / 0.432 / 0.579 | 0.014 [0.006, 0.029] | 0.017 | True |
| llama_features_judge | certified | 0.10 | 400 | 500 | 0.978 | 0.537 | 0.439 / 0.548 / 0.648 | 0.016 [0.007, 0.031] | 0.016 | True |
| llama_features_judge | certified | 0.10 | 800 | 500 | 0.994 | 0.630 | 0.555 / 0.634 / 0.707 | 0.016 [0.007, 0.031] | 0.016 | True |
| llama_features_judge | certified | 0.25 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.25 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.25 | 100 | 500 | 0.006 | 0.005 | 0.000 / 0.000 / 0.000 | 0.006 [0.001, 0.017] | 1.000 | True |
| llama_features_judge | certified | 0.25 | 200 | 500 | 0.824 | 0.417 | 0.000 / 0.463 / 0.615 | 0.012 [0.004, 0.026] | 0.015 | True |
| llama_features_judge | certified | 0.25 | 400 | 500 | 0.996 | 0.592 | 0.497 / 0.594 / 0.697 | 0.014 [0.006, 0.029] | 0.014 | True |
| llama_features_judge | certified | 0.25 | 800 | 500 | 1.000 | 0.670 | 0.610 / 0.670 / 0.729 | 0.006 [0.001, 0.017] | 0.006 | True |
| llama_features_judge | certified | 0.50 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.50 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.50 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.50 | 200 | 500 | 0.204 | 0.130 | 0.000 / 0.000 / 0.622 | 0.008 [0.002, 0.020] | 0.039 | True |
| llama_features_judge | certified | 0.50 | 400 | 500 | 0.968 | 0.578 | 0.452 / 0.600 / 0.705 | 0.010 [0.003, 0.023] | 0.010 | True |
| llama_features_judge | certified | 0.50 | 800 | 500 | 0.998 | 0.668 | 0.599 / 0.673 / 0.741 | 0.008 [0.002, 0.020] | 0.008 | True |
| llama_features_judge | certified | 0.75 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.75 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.75 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.75 | 200 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_features_judge | certified | 0.75 | 400 | 500 | 0.366 | 0.239 | 0.000 / 0.000 / 0.684 | 0.014 [0.006, 0.029] | 0.038 | True |
| llama_features_judge | certified | 0.75 | 800 | 500 | 0.992 | 0.614 | 0.493 / 0.621 / 0.730 | 0.012 [0.004, 0.026] | 0.012 | True |
| llama_features_judge | heuristic | 1.00 | 25 | 500 | 0.058 | 0.058 | 0.000 / 0.000 / 0.000 | 0.058 [0.039, 0.082] | 1.000 | True |
| llama_features_judge | heuristic | 1.00 | 50 | 500 | 0.066 | 0.066 | 0.000 / 0.000 / 0.000 | 0.066 [0.046, 0.091] | 1.000 | True |
| llama_features_judge | heuristic | 1.00 | 100 | 500 | 0.920 | 0.699 | 0.598 / 0.739 / 0.893 | 0.472 [0.428, 0.517] | 0.513 | False |
| llama_features_judge | heuristic | 1.00 | 200 | 500 | 1.000 | 0.757 | 0.648 / 0.759 / 0.868 | 0.414 [0.370, 0.459] | 0.414 | False |
| llama_features_judge | heuristic | 1.00 | 400 | 500 | 1.000 | 0.777 | 0.695 / 0.779 / 0.849 | 0.350 [0.308, 0.394] | 0.350 | False |
| llama_features_judge | heuristic | 1.00 | 800 | 500 | 1.000 | 0.790 | 0.742 / 0.789 / 0.840 | 0.280 [0.241, 0.322] | 0.280 | False |
| llama_judge_0shot | certified | 0.00 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_judge_0shot | certified | 0.00 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_judge_0shot | certified | 0.00 | 100 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_judge_0shot | certified | 0.00 | 200 | 500 | 0.492 | 0.165 | 0.000 / 0.000 / 0.328 | 0.022 [0.011, 0.039] | 0.045 | True |
| llama_judge_0shot | certified | 0.00 | 400 | 500 | 0.848 | 0.281 | 0.000 / 0.328 / 0.328 | 0.022 [0.011, 0.039] | 0.026 | True |
| llama_judge_0shot | certified | 0.00 | 800 | 500 | 0.996 | 0.327 | 0.328 / 0.328 / 0.328 | 0.000 [0.000, 0.007] | 0.000 | True |
| llama_judge_0shot | heuristic | 1.00 | 25 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_judge_0shot | heuristic | 1.00 | 50 | 500 | 0.000 | 0.000 | 0.000 / 0.000 / 0.000 | 0.000 [0.000, 0.007] | - | True |
| llama_judge_0shot | heuristic | 1.00 | 100 | 500 | 0.004 | 0.002 | 0.000 / 0.000 / 0.000 | 0.004 [0.000, 0.014] | 1.000 | True |
| llama_judge_0shot | heuristic | 1.00 | 200 | 500 | 0.992 | 0.404 | 0.328 / 0.328 / 0.478 | 0.492 [0.447, 0.537] | 0.496 | False |
| llama_judge_0shot | heuristic | 1.00 | 400 | 500 | 1.000 | 0.395 | 0.328 / 0.328 / 0.478 | 0.440 [0.396, 0.485] | 0.440 | False |
| llama_judge_0shot | heuristic | 1.00 | 800 | 500 | 1.000 | 0.380 | 0.328 / 0.328 / 0.478 | 0.346 [0.304, 0.390] | 0.346 | False |

## Best certified arm per B (descriptive: picked after seeing test results)

- B = 100: llama_features at f = 0.10, 0.012
- B = 200: llama_features_judge at f = 0.25, 0.417
- B = 400: llama_features_judge at f = 0.25, 0.592
- B = 800: llama_features_judge at f = 0.25, 0.670

B* (smallest B where the best arm fits, f > 0): 100
