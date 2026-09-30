| case | pool | judged on | n | violation [95% CI] | useful | mean true coverage |
|---|---|---|---|---|---|---|
| a_twinrouter | fresh | true | 20000 | 0.027 [0.024, 0.029] | 0.97 | 0.545 |
| a_twinrouter | fresh | fixed_test | 20000 | 0.061 [0.058, 0.065] | 0.97 | 0.545 |
| a_twinrouter | fresh | fresh_test | 20000 | 0.062 [0.059, 0.066] | 0.97 | 0.545 |
| a_twinrouter | fixed (400x50) | true | 20000 | 0.035 [0.033, 0.038] | 0.97 | 0.550 |
| a_twinrouter | fixed (400x50) | fixed_test | 20000 | 0.054 [0.051, 0.057] | 0.97 | 0.550 |
| a_twinrouter | fixed (400x50) | fresh_test | 20000 | 0.070 [0.067, 0.074] | 0.97 | 0.550 |
| a_twinrouter_ties10 | fresh | true | 20000 | 0.000 [0.000, 0.001] | 0.99 | 0.528 |
| a_twinrouter_ties10 | fresh | fixed_test | 20000 | 0.026 [0.024, 0.029] | 0.99 | 0.528 |
| a_twinrouter_ties10 | fresh | fresh_test | 20000 | 0.028 [0.026, 0.030] | 0.99 | 0.528 |
| a_twinrouter_ties10 | fixed (400x50) | true | 20000 | 0.000 [0.000, 0.000] | 0.99 | 0.528 |
| a_twinrouter_ties10 | fixed (400x50) | fixed_test | 20000 | 0.032 [0.029, 0.034] | 0.99 | 0.528 |
| a_twinrouter_ties10 | fixed (400x50) | fresh_test | 20000 | 0.030 [0.027, 0.032] | 0.99 | 0.528 |
| a_twinrouter_pool5000 | fresh | true | 20000 | 0.031 [0.028, 0.033] | 0.98 | 0.559 |
| a_twinrouter_pool5000 | fresh | fixed_test | 20000 | 0.066 [0.063, 0.070] | 0.98 | 0.559 |
| a_twinrouter_pool5000 | fresh | fresh_test | 20000 | 0.067 [0.063, 0.070] | 0.98 | 0.559 |
| a_twinrouter_pool5000 | fixed (400x50) | true | 20000 | 0.033 [0.031, 0.036] | 0.98 | 0.558 |
| a_twinrouter_pool5000 | fixed (400x50) | fixed_test | 20000 | 0.068 [0.064, 0.071] | 0.98 | 0.558 |
| a_twinrouter_pool5000 | fixed (400x50) | fresh_test | 20000 | 0.067 [0.063, 0.070] | 0.98 | 0.558 |
| b_w5_b800 | fresh | true | 20000 | 0.031 [0.029, 0.034] | 0.98 | 0.585 |
| b_w5_b800 | fresh | fixed_test | 20000 | 0.042 [0.039, 0.045] | 0.98 | 0.585 |
| b_w5_b800 | fresh | fresh_test | 20000 | 0.042 [0.039, 0.044] | 0.98 | 0.585 |
| b_w5_b800 | fixed (400x50) | true | 20000 | 0.030 [0.028, 0.033] | 0.98 | 0.586 |
| b_w5_b800 | fixed (400x50) | fixed_test | 20000 | 0.044 [0.042, 0.047] | 0.98 | 0.586 |
| b_w5_b800 | fixed (400x50) | fresh_test | 20000 | 0.042 [0.039, 0.045] | 0.98 | 0.586 |
| c_t1_alpha021 | fresh | true | 20000 | 0.037 [0.034, 0.039] | 0.96 | 0.617 |
| c_t1_alpha021 | fresh | fixed_test | 20000 | 0.060 [0.057, 0.063] | 0.96 | 0.617 |
| c_t1_alpha021 | fresh | fresh_test | 20000 | 0.062 [0.059, 0.066] | 0.96 | 0.617 |
| c_t1_alpha021 | fixed (400x50) | true | 20000 | 0.032 [0.030, 0.035] | 0.96 | 0.617 |
| c_t1_alpha021 | fixed (400x50) | fixed_test | 20000 | 0.052 [0.049, 0.056] | 0.96 | 0.617 |
| c_t1_alpha021 | fixed (400x50) | fresh_test | 20000 | 0.056 [0.053, 0.060] | 0.96 | 0.617 |

Per-pool violation rates (fixed pool; share of pools above 5%, range):

- a_twinrouter, true_viol_rate: mean 0.035, pools above 0.05: 17%, range 0.000–0.880
- a_twinrouter, fixed_test_viol_rate: mean 0.054, pools above 0.05: 21%, range 0.000–0.940
- a_twinrouter_pool5000, true_viol_rate: mean 0.033, pools above 0.05: 26%, range 0.000–0.160
- a_twinrouter_pool5000, fixed_test_viol_rate: mean 0.068, pools above 0.05: 35%, range 0.000–0.700
- a_twinrouter_ties10, true_viol_rate: mean 0.000, pools above 0.05: 0%, range 0.000–0.020
- a_twinrouter_ties10, fixed_test_viol_rate: mean 0.032, pools above 0.05: 13%, range 0.000–0.880
- b_w5_b800, true_viol_rate: mean 0.030, pools above 0.05: 21%, range 0.000–0.300
- b_w5_b800, fixed_test_viol_rate: mean 0.044, pools above 0.05: 28%, range 0.000–0.700
- c_t1_alpha021, true_viol_rate: mean 0.032, pools above 0.05: 22%, range 0.000–0.260
- c_t1_alpha021, fixed_test_viol_rate: mean 0.052, pools above 0.05: 27%, range 0.000–0.680
