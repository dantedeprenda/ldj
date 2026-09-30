# Platform-shift stress test (T1, exploratory)

Platforms: 0: 2016 comments, 31.2% positive, direct-judge error 20.4%; 2: 1818 comments, 24.0% positive, direct-judge error 23.0%; 3: 1149 comments, 30.5% positive, direct-judge error 25.5%

Failures (cache-only): {'questions': 2, 'judge': 0}

Certified cells, α = 0.10, δ = 0.05. Violation = realized target test-half risk > α.

| source→target | method | f | B | grid | useful | automated | violation [95% CI] | consistent |
|---|---|---|---|---|---|---|---|---|
| 0→0 | gemma_features_judge | 0.25 | 200 | source | 0.67 | 0.347 | 0.020 [0.010, 0.036] | yes |
| 0→0 | gemma_features_judge | 0.25 | 200 | target | 0.66 | 0.345 | 0.020 [0.010, 0.036] | yes |
| 0→0 | gemma_features_judge | 0.25 | 400 | source | 0.91 | 0.530 | 0.024 [0.012, 0.042] | yes |
| 0→0 | gemma_features_judge | 0.25 | 400 | target | 0.91 | 0.530 | 0.024 [0.012, 0.042] | yes |
| 0→0 | gemma_features_judge | 0.25 | 800 | source | 0.95 | 0.630 | 0.022 [0.011, 0.039] | yes |
| 0→0 | gemma_features_judge | 0.25 | 800 | target | 0.93 | 0.616 | 0.020 [0.010, 0.036] | yes |
| 0→0 | gemma_features_judge | 0.50 | 200 | source | 0.27 | 0.173 | 0.016 [0.007, 0.031] | yes |
| 0→0 | gemma_features_judge | 0.50 | 200 | target | 0.26 | 0.167 | 0.016 [0.007, 0.031] | yes |
| 0→0 | gemma_features_judge | 0.50 | 400 | source | 0.84 | 0.487 | 0.028 [0.015, 0.047] | yes |
| 0→0 | gemma_features_judge | 0.50 | 400 | target | 0.85 | 0.489 | 0.026 [0.014, 0.044] | yes |
| 0→0 | gemma_features_judge | 0.50 | 800 | source | 0.92 | 0.634 | 0.022 [0.011, 0.039] | yes |
| 0→0 | gemma_features_judge | 0.50 | 800 | target | 0.95 | 0.653 | 0.022 [0.011, 0.039] | yes |
| 0→0 | gemma_judge_0shot | 0.00 | 200 | source | 0.02 | 0.012 | 0.006 [0.001, 0.017] | yes |
| 0→0 | gemma_judge_0shot | 0.00 | 200 | target | 0.02 | 0.012 | 0.006 [0.001, 0.017] | yes |
| 0→0 | gemma_judge_0shot | 0.00 | 400 | source | 0.02 | 0.008 | 0.000 [0.000, 0.007] | yes |
| 0→0 | gemma_judge_0shot | 0.00 | 400 | target | 0.02 | 0.008 | 0.000 [0.000, 0.007] | yes |
| 0→0 | gemma_judge_0shot | 0.00 | 800 | source | 0.00 | 0.000 | 0.000 [0.000, 0.007] | yes |
| 0→0 | gemma_judge_0shot | 0.00 | 800 | target | 0.00 | 0.000 | 0.000 [0.000, 0.007] | yes |
| 2→2 | gemma_features_judge | 0.25 | 200 | source | 0.85 | 0.473 | 0.016 [0.007, 0.031] | yes |
| 2→2 | gemma_features_judge | 0.25 | 200 | target | 0.85 | 0.475 | 0.018 [0.008, 0.034] | yes |
| 2→2 | gemma_features_judge | 0.25 | 400 | source | 0.98 | 0.633 | 0.010 [0.003, 0.023] | yes |
| 2→2 | gemma_features_judge | 0.25 | 400 | target | 0.99 | 0.640 | 0.012 [0.004, 0.026] | yes |
| 2→2 | gemma_features_judge | 0.25 | 800 | source | 0.92 | 0.653 | 0.002 [0.000, 0.011] | yes |
| 2→2 | gemma_features_judge | 0.25 | 800 | target | 1.00 | 0.711 | 0.002 [0.000, 0.011] | yes |
| 2→2 | gemma_features_judge | 0.50 | 200 | source | 0.39 | 0.245 | 0.008 [0.002, 0.020] | yes |
| 2→2 | gemma_features_judge | 0.50 | 200 | target | 0.39 | 0.243 | 0.008 [0.002, 0.020] | yes |
| 2→2 | gemma_features_judge | 0.50 | 400 | source | 0.96 | 0.614 | 0.018 [0.008, 0.034] | yes |
| 2→2 | gemma_features_judge | 0.50 | 400 | target | 0.96 | 0.618 | 0.014 [0.006, 0.029] | yes |
| 2→2 | gemma_features_judge | 0.50 | 800 | source | 0.93 | 0.662 | 0.004 [0.000, 0.014] | yes |
| 2→2 | gemma_features_judge | 0.50 | 800 | target | 1.00 | 0.712 | 0.006 [0.001, 0.017] | yes |
| 2→2 | gemma_judge_0shot | 0.00 | 200 | source | 0.10 | 0.040 | 0.002 [0.000, 0.011] | yes |
| 2→2 | gemma_judge_0shot | 0.00 | 200 | target | 0.10 | 0.040 | 0.002 [0.000, 0.011] | yes |
| 2→2 | gemma_judge_0shot | 0.00 | 400 | source | 0.16 | 0.072 | 0.000 [0.000, 0.007] | yes |
| 2→2 | gemma_judge_0shot | 0.00 | 400 | target | 0.16 | 0.072 | 0.000 [0.000, 0.007] | yes |
| 2→2 | gemma_judge_0shot | 0.00 | 800 | source | 0.28 | 0.132 | 0.000 [0.000, 0.007] | yes |
| 2→2 | gemma_judge_0shot | 0.00 | 800 | target | 0.28 | 0.132 | 0.000 [0.000, 0.007] | yes |
| 3→3 | gemma_features_judge | 0.25 | 200 | source | 0.59 | 0.305 | 0.012 [0.004, 0.026] | yes |
| 3→3 | gemma_features_judge | 0.25 | 200 | target | 0.59 | 0.303 | 0.010 [0.003, 0.023] | yes |
| 3→3 | gemma_features_judge | 0.25 | 400 | source | 0.97 | 0.557 | 0.026 [0.014, 0.044] | yes |
| 3→3 | gemma_features_judge | 0.25 | 400 | target | 0.98 | 0.563 | 0.024 [0.012, 0.042] | yes |
| 3→3 | gemma_features_judge | 0.50 | 200 | source | 0.11 | 0.070 | 0.012 [0.004, 0.026] | yes |
| 3→3 | gemma_features_judge | 0.50 | 200 | target | 0.10 | 0.068 | 0.012 [0.004, 0.026] | yes |
| 3→3 | gemma_features_judge | 0.50 | 400 | source | 0.97 | 0.547 | 0.008 [0.002, 0.020] | yes |
| 3→3 | gemma_features_judge | 0.50 | 400 | target | 0.96 | 0.545 | 0.010 [0.003, 0.023] | yes |
| 3→3 | gemma_judge_0shot | 0.00 | 200 | source | 0.16 | 0.060 | 0.000 [0.000, 0.007] | yes |
| 3→3 | gemma_judge_0shot | 0.00 | 200 | target | 0.16 | 0.060 | 0.000 [0.000, 0.007] | yes |
| 3→3 | gemma_judge_0shot | 0.00 | 400 | source | 0.66 | 0.144 | 0.000 [0.000, 0.007] | yes |
| 3→3 | gemma_judge_0shot | 0.00 | 400 | target | 0.74 | 0.160 | 0.000 [0.000, 0.007] | yes |
| 0→2 | gemma_features_judge | 0.25 | 200 | source | 0.67 | 0.342 | 0.008 [0.002, 0.020] | yes |
| 0→2 | gemma_features_judge | 0.25 | 200 | target | 0.64 | 0.331 | 0.010 [0.003, 0.023] | yes |
| 0→2 | gemma_features_judge | 0.25 | 400 | source | 0.91 | 0.511 | 0.004 [0.000, 0.014] | yes |
| 0→2 | gemma_features_judge | 0.25 | 400 | target | 0.92 | 0.524 | 0.002 [0.000, 0.011] | yes |
| 0→2 | gemma_features_judge | 0.25 | 800 | source | 0.95 | 0.600 | 0.000 [0.000, 0.007] | yes |
| 0→2 | gemma_features_judge | 0.25 | 800 | target | 0.96 | 0.596 | 0.000 [0.000, 0.007] | yes |
| 0→2 | gemma_features_judge | 0.50 | 200 | source | 0.27 | 0.167 | 0.004 [0.000, 0.014] | yes |
| 0→2 | gemma_features_judge | 0.50 | 200 | target | 0.22 | 0.140 | 0.004 [0.000, 0.014] | yes |
| 0→2 | gemma_features_judge | 0.50 | 400 | source | 0.84 | 0.472 | 0.004 [0.000, 0.014] | yes |
| 0→2 | gemma_features_judge | 0.50 | 400 | target | 0.87 | 0.485 | 0.004 [0.000, 0.014] | yes |
| 0→2 | gemma_features_judge | 0.50 | 800 | source | 0.92 | 0.607 | 0.006 [0.001, 0.017] | yes |
| 0→2 | gemma_features_judge | 0.50 | 800 | target | 0.92 | 0.609 | 0.008 [0.002, 0.020] | yes |
| 0→2 | gemma_judge_0shot | 0.00 | 200 | source | 0.02 | 0.011 | 0.006 [0.001, 0.017] | yes |
| 0→2 | gemma_judge_0shot | 0.00 | 200 | target | 0.02 | 0.011 | 0.006 [0.001, 0.017] | yes |
| 0→2 | gemma_judge_0shot | 0.00 | 400 | source | 0.02 | 0.007 | 0.000 [0.000, 0.007] | yes |
| 0→2 | gemma_judge_0shot | 0.00 | 400 | target | 0.02 | 0.007 | 0.000 [0.000, 0.007] | yes |
| 0→2 | gemma_judge_0shot | 0.00 | 800 | source | 0.00 | 0.000 | 0.000 [0.000, 0.007] | yes |
| 0→2 | gemma_judge_0shot | 0.00 | 800 | target | 0.00 | 0.000 | 0.000 [0.000, 0.007] | yes |
| 0→3 | gemma_features_judge | 0.25 | 200 | source | 0.67 | 0.343 | 0.034 [0.020, 0.054] | yes |
| 0→3 | gemma_features_judge | 0.25 | 200 | target | 0.58 | 0.320 | 0.036 [0.021, 0.056] | yes |
| 0→3 | gemma_features_judge | 0.25 | 400 | source | 0.91 | 0.519 | 0.030 [0.017, 0.049] | yes |
| 0→3 | gemma_features_judge | 0.25 | 400 | target | 0.96 | 0.564 | 0.034 [0.020, 0.054] | yes |
| 0→3 | gemma_features_judge | 0.25 | 800 | source | 0.95 | 0.618 | 0.022 [0.011, 0.039] | yes |
| 0→3 | gemma_features_judge | 0.25 | 800 | target | 0.99 | 0.678 | 0.020 [0.010, 0.036] | yes |
| 0→3 | gemma_features_judge | 0.50 | 200 | source | 0.27 | 0.172 | 0.014 [0.006, 0.029] | yes |
| 0→3 | gemma_features_judge | 0.50 | 200 | target | 0.14 | 0.097 | 0.016 [0.007, 0.031] | yes |
| 0→3 | gemma_features_judge | 0.50 | 400 | source | 0.84 | 0.478 | 0.016 [0.007, 0.031] | yes |
| 0→3 | gemma_features_judge | 0.50 | 400 | target | 0.90 | 0.515 | 0.018 [0.008, 0.034] | yes |
| 0→3 | gemma_features_judge | 0.50 | 800 | source | 0.92 | 0.624 | 0.008 [0.002, 0.020] | yes |
| 0→3 | gemma_features_judge | 0.50 | 800 | target | 1.00 | 0.680 | 0.006 [0.001, 0.017] | yes |
| 0→3 | gemma_judge_0shot | 0.00 | 200 | source | 0.02 | 0.008 | 0.006 [0.001, 0.017] | yes |
| 0→3 | gemma_judge_0shot | 0.00 | 200 | target | 0.04 | 0.017 | 0.008 [0.002, 0.020] | yes |
| 0→3 | gemma_judge_0shot | 0.00 | 400 | source | 0.02 | 0.005 | 0.000 [0.000, 0.007] | yes |
| 0→3 | gemma_judge_0shot | 0.00 | 400 | target | 0.02 | 0.005 | 0.000 [0.000, 0.007] | yes |
| 0→3 | gemma_judge_0shot | 0.00 | 800 | source | 0.00 | 0.000 | 0.000 [0.000, 0.007] | yes |
| 0→3 | gemma_judge_0shot | 0.00 | 800 | target | 0.00 | 0.000 | 0.000 [0.000, 0.007] | yes |
| 2→0 | gemma_features_judge | 0.25 | 200 | source | 0.85 | 0.473 | 0.092 [0.068, 0.121] | **no** |
| 2→0 | gemma_features_judge | 0.25 | 200 | target | 0.85 | 0.474 | 0.096 [0.072, 0.125] | **no** |
| 2→0 | gemma_features_judge | 0.25 | 400 | source | 0.98 | 0.641 | 0.168 [0.136, 0.204] | **no** |
| 2→0 | gemma_features_judge | 0.25 | 400 | target | 0.99 | 0.644 | 0.174 [0.142, 0.210] | **no** |
| 2→0 | gemma_features_judge | 0.25 | 800 | source | 0.92 | 0.667 | 0.308 [0.268, 0.351] | **no** |
| 2→0 | gemma_features_judge | 0.25 | 800 | target | 1.00 | 0.726 | 0.366 [0.324, 0.410] | **no** |
| 2→0 | gemma_features_judge | 0.50 | 200 | source | 0.39 | 0.248 | 0.052 [0.034, 0.075] | yes |
| 2→0 | gemma_features_judge | 0.50 | 200 | target | 0.41 | 0.257 | 0.050 [0.033, 0.073] | yes |
| 2→0 | gemma_features_judge | 0.50 | 400 | source | 0.96 | 0.623 | 0.124 [0.096, 0.156] | **no** |
| 2→0 | gemma_features_judge | 0.50 | 400 | target | 0.96 | 0.622 | 0.122 [0.095, 0.154] | **no** |
| 2→0 | gemma_features_judge | 0.50 | 800 | source | 0.93 | 0.678 | 0.218 [0.183, 0.257] | **no** |
| 2→0 | gemma_features_judge | 0.50 | 800 | target | 1.00 | 0.731 | 0.256 [0.218, 0.297] | **no** |
| 2→0 | gemma_judge_0shot | 0.00 | 200 | source | 0.10 | 0.047 | 0.002 [0.000, 0.011] | yes |
| 2→0 | gemma_judge_0shot | 0.00 | 200 | target | 0.10 | 0.047 | 0.002 [0.000, 0.011] | yes |
| 2→0 | gemma_judge_0shot | 0.00 | 400 | source | 0.16 | 0.081 | 0.000 [0.000, 0.007] | yes |
| 2→0 | gemma_judge_0shot | 0.00 | 400 | target | 0.16 | 0.081 | 0.000 [0.000, 0.007] | yes |
| 2→0 | gemma_judge_0shot | 0.00 | 800 | source | 0.28 | 0.149 | 0.000 [0.000, 0.007] | yes |
| 2→0 | gemma_judge_0shot | 0.00 | 800 | target | 0.28 | 0.149 | 0.000 [0.000, 0.007] | yes |
| 2→3 | gemma_features_judge | 0.25 | 200 | source | 0.85 | 0.470 | 0.108 [0.082, 0.139] | **no** |
| 2→3 | gemma_features_judge | 0.25 | 200 | target | 0.82 | 0.469 | 0.106 [0.080, 0.136] | **no** |
| 2→3 | gemma_features_judge | 0.25 | 400 | source | 0.98 | 0.641 | 0.178 [0.145, 0.214] | **no** |
| 2→3 | gemma_features_judge | 0.25 | 400 | target | 1.00 | 0.657 | 0.184 [0.151, 0.221] | **no** |
| 2→3 | gemma_features_judge | 0.25 | 800 | source | 0.92 | 0.672 | 0.300 [0.260, 0.342] | **no** |
| 2→3 | gemma_features_judge | 0.25 | 800 | target | 1.00 | 0.733 | 0.340 [0.299, 0.383] | **no** |
| 2→3 | gemma_features_judge | 0.50 | 200 | source | 0.39 | 0.248 | 0.058 [0.039, 0.082] | yes |
| 2→3 | gemma_features_judge | 0.50 | 200 | target | 0.25 | 0.172 | 0.066 [0.046, 0.091] | yes |
| 2→3 | gemma_features_judge | 0.50 | 400 | source | 0.96 | 0.627 | 0.122 [0.095, 0.154] | **no** |
| 2→3 | gemma_features_judge | 0.50 | 400 | target | 0.98 | 0.645 | 0.122 [0.095, 0.154] | **no** |
| 2→3 | gemma_features_judge | 0.50 | 800 | source | 0.93 | 0.688 | 0.204 [0.170, 0.242] | **no** |
| 2→3 | gemma_features_judge | 0.50 | 800 | target | 1.00 | 0.744 | 0.236 [0.199, 0.276] | **no** |
| 2→3 | gemma_judge_0shot | 0.00 | 200 | source | 0.10 | 0.029 | 0.002 [0.000, 0.011] | yes |
| 2→3 | gemma_judge_0shot | 0.00 | 200 | target | 0.09 | 0.036 | 0.002 [0.000, 0.011] | yes |
| 2→3 | gemma_judge_0shot | 0.00 | 400 | source | 0.16 | 0.053 | 0.000 [0.000, 0.007] | yes |
| 2→3 | gemma_judge_0shot | 0.00 | 400 | target | 0.16 | 0.053 | 0.000 [0.000, 0.007] | yes |
| 2→3 | gemma_judge_0shot | 0.00 | 800 | source | 0.28 | 0.098 | 0.000 [0.000, 0.007] | yes |
| 2→3 | gemma_judge_0shot | 0.00 | 800 | target | 0.28 | 0.098 | 0.000 [0.000, 0.007] | yes |
| 3→0 | gemma_features_judge | 0.25 | 200 | source | 0.59 | 0.319 | 0.028 [0.015, 0.047] | yes |
| 3→0 | gemma_features_judge | 0.25 | 200 | target | 0.62 | 0.320 | 0.026 [0.014, 0.044] | yes |
| 3→0 | gemma_features_judge | 0.25 | 400 | source | 0.97 | 0.583 | 0.068 [0.048, 0.094] | yes |
| 3→0 | gemma_features_judge | 0.25 | 400 | target | 0.85 | 0.500 | 0.064 [0.044, 0.089] | yes |
| 3→0 | gemma_features_judge | 0.50 | 200 | source | 0.11 | 0.073 | 0.026 [0.014, 0.044] | yes |
| 3→0 | gemma_features_judge | 0.50 | 200 | target | 0.29 | 0.178 | 0.026 [0.014, 0.044] | yes |
| 3→0 | gemma_features_judge | 0.50 | 400 | source | 0.97 | 0.571 | 0.044 [0.028, 0.066] | yes |
| 3→0 | gemma_features_judge | 0.50 | 400 | target | 0.84 | 0.495 | 0.042 [0.026, 0.063] | yes |
| 3→0 | gemma_judge_0shot | 0.00 | 200 | source | 0.16 | 0.088 | 0.000 [0.000, 0.007] | yes |
| 3→0 | gemma_judge_0shot | 0.00 | 200 | target | 0.22 | 0.093 | 0.000 [0.000, 0.007] | yes |
| 3→0 | gemma_judge_0shot | 0.00 | 400 | source | 0.66 | 0.274 | 0.000 [0.000, 0.007] | yes |
| 3→0 | gemma_judge_0shot | 0.00 | 400 | target | 0.74 | 0.300 | 0.000 [0.000, 0.007] | yes |
| 3→2 | gemma_features_judge | 0.25 | 200 | source | 0.59 | 0.317 | 0.004 [0.000, 0.014] | yes |
| 3→2 | gemma_features_judge | 0.25 | 200 | target | 0.65 | 0.334 | 0.004 [0.000, 0.014] | yes |
| 3→2 | gemma_features_judge | 0.25 | 400 | source | 0.97 | 0.573 | 0.018 [0.008, 0.034] | yes |
| 3→2 | gemma_features_judge | 0.25 | 400 | target | 0.89 | 0.522 | 0.016 [0.007, 0.031] | yes |
| 3→2 | gemma_features_judge | 0.50 | 200 | source | 0.11 | 0.072 | 0.008 [0.002, 0.020] | yes |
| 3→2 | gemma_features_judge | 0.50 | 200 | target | 0.25 | 0.156 | 0.012 [0.004, 0.026] | yes |
| 3→2 | gemma_features_judge | 0.50 | 400 | source | 0.97 | 0.562 | 0.010 [0.003, 0.023] | yes |
| 3→2 | gemma_features_judge | 0.50 | 400 | target | 0.89 | 0.519 | 0.010 [0.003, 0.023] | yes |
| 3→2 | gemma_judge_0shot | 0.00 | 200 | source | 0.16 | 0.080 | 0.000 [0.000, 0.007] | yes |
| 3→2 | gemma_judge_0shot | 0.00 | 200 | target | 0.22 | 0.078 | 0.000 [0.000, 0.007] | yes |
| 3→2 | gemma_judge_0shot | 0.00 | 400 | source | 0.66 | 0.223 | 0.000 [0.000, 0.007] | yes |
| 3→2 | gemma_judge_0shot | 0.00 | 400 | target | 0.74 | 0.250 | 0.000 [0.000, 0.007] | yes |

## Headline

| setting | grid | cells | inconsistent | max violation | mean automation |
|---|---|---|---|---|---|
| control | source | 24 | 0 | 0.028 | 0.335 |
| control | target | 24 | 0 | 0.026 | 0.340 |
| shift | source | 48 | 10 | 0.308 | 0.341 |
| shift | target | 48 | 10 | 0.366 | 0.347 |
