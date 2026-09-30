# Pre-registered analysis: x1_t1

Primary method: **gemma_features_judge**. Best text baseline at k = 25 (pre-registered rule): **gemma_features** (0.869; others: bgeL_logreg 0.782).

## A. Within-category AUROC, primary minus comparator (95% CI, hierarchical bootstrap)

| k | comparator | primary | comparator | diff | 95% CI | seeds won |
|---|---|---|---|---|---|---|
| 5 | gemma_features (best) | 0.860 | 0.831 | +0.029 | [+0.012, +0.056] | 5/5 |
| 5 | bgeL_logreg | 0.860 | 0.699 | +0.161 | [+0.090, +0.243] | 5/5 |
| 5 | gemma_judge_0shot | 0.860 | 0.845 | +0.015 | [-0.052, +0.061] | 4/5 |
| 5 | gemma_judge_0shot_platt | 0.860 | 0.845 | +0.015 | [-0.052, +0.061] | 4/5 |
| 10 | gemma_features (best) | 0.877 | 0.855 | +0.022 | [+0.011, +0.036] | 5/5 |
| 10 | bgeL_logreg | 0.877 | 0.779 | +0.098 | [+0.057, +0.135] | 5/5 |
| 10 | gemma_judge_0shot | 0.877 | 0.845 | +0.032 | [-0.009, +0.066] | 4/5 |
| 10 | gemma_judge_0shot_platt | 0.877 | 0.845 | +0.032 | [-0.009, +0.066] | 4/5 |
| 25 | gemma_features (best) | 0.881 | 0.869 | +0.012 | [+0.006, +0.019] | 5/5 |
| 25 | bgeL_logreg | 0.881 | 0.782 | +0.099 | [+0.059, +0.146] | 5/5 |
| 25 | gemma_judge_0shot | 0.881 | 0.845 | +0.036 | [+0.016, +0.058] | 5/5 |
| 25 | gemma_judge_0shot_platt | 0.881 | 0.845 | +0.036 | [+0.016, +0.058] | 5/5 |
| 50 | gemma_features (best) | 0.908 | 0.897 | +0.012 | [+0.006, +0.018] | 5/5 |
| 50 | bgeL_logreg | 0.908 | 0.835 | +0.074 | [+0.056, +0.093] | 5/5 |
| 50 | gemma_judge_0shot | 0.908 | 0.845 | +0.063 | [+0.048, +0.079] | 5/5 |
| 50 | gemma_judge_0shot_platt | 0.908 | 0.845 | +0.063 | [+0.048, +0.079] | 5/5 |
| 100 | gemma_features (best) | 0.907 | 0.898 | +0.009 | [+0.003, +0.015] | 5/5 |
| 100 | bgeL_logreg | 0.907 | 0.837 | +0.071 | [+0.045, +0.099] | 5/5 |
| 100 | gemma_judge_0shot | 0.907 | 0.845 | +0.062 | [+0.046, +0.079] | 5/5 |
| 100 | gemma_judge_0shot_platt | 0.907 | 0.845 | +0.062 | [+0.046, +0.079] | 5/5 |
| all | gemma_features (best) | 0.920 | 0.913 | +0.007 | [+0.001, +0.012] | 5/5 |
| all | bgeL_logreg | 0.920 | 0.897 | +0.023 | [+0.011, +0.037] | 5/5 |
| all | gemma_judge_0shot | 0.920 | 0.845 | +0.075 | [+0.060, +0.091] | 5/5 |
| all | gemma_judge_0shot_platt | 0.920 | 0.845 | +0.075 | [+0.060, +0.091] | 5/5 |

## B. Cost per item (c_fp=$1.0, c_fn=$1.0, rule=ucb), primary minus comparator; negative = primary cheaper

| k | comparator | primary $ | comparator $ | diff $ | 95% CI |
|---|---|---|---|---|---|
| 5 | gemma_features | 0.4552 | 0.4552 | +0.0000 | [+0.0000, +0.0000] |
| 5 | bgeL_logreg | 0.4552 | 0.4551 | +0.0001 | [+0.0001, +0.0001] |
| 5 | gemma_judge_0shot | 0.4552 | 0.4481 | +0.0071 | [+0.0001, +0.0216] |
| 5 | gemma_judge_0shot_platt | 0.4552 | 0.4438 | +0.0114 | [+0.0001, +0.0343] |
| 10 | gemma_features | 0.3610 | 0.3656 | -0.0046 | [-0.0227, +0.0127] |
| 10 | bgeL_logreg | 0.3610 | 0.4552 | -0.0943 | [-0.1763, -0.0194] |
| 10 | gemma_judge_0shot | 0.3610 | 0.3263 | +0.0347 | [-0.0317, +0.1157] |
| 10 | gemma_judge_0shot_platt | 0.3610 | 0.3436 | +0.0174 | [-0.0360, +0.0922] |
| 25 | gemma_features | 0.2472 | 0.2376 | +0.0096 | [-0.0094, +0.0385] |
| 25 | bgeL_logreg | 0.2472 | 0.3611 | -0.1139 | [-0.1860, -0.0426] |
| 25 | gemma_judge_0shot | 0.2472 | 0.2399 | +0.0073 | [-0.0289, +0.0439] |
| 25 | gemma_judge_0shot_platt | 0.2472 | 0.2523 | -0.0051 | [-0.0351, +0.0283] |
| 50 | gemma_features | 0.2241 | 0.2220 | +0.0022 | [-0.0296, +0.0505] |
| 50 | bgeL_logreg | 0.2241 | 0.3375 | -0.1133 | [-0.2053, -0.0328] |
| 50 | gemma_judge_0shot | 0.2241 | 0.2340 | -0.0098 | [-0.0509, +0.0349] |
| 50 | gemma_judge_0shot_platt | 0.2241 | 0.2415 | -0.0173 | [-0.0578, +0.0291] |
| 100 | gemma_features | 0.2001 | 0.2096 | -0.0095 | [-0.0431, +0.0188] |
| 100 | bgeL_logreg | 0.2001 | 0.2646 | -0.0645 | [-0.0927, -0.0417] |
| 100 | gemma_judge_0shot | 0.2001 | 0.2005 | -0.0004 | [-0.0402, +0.0391] |
| 100 | gemma_judge_0shot_platt | 0.2001 | 0.2031 | -0.0030 | [-0.0408, +0.0354] |
| all | gemma_features | 0.2282 | 0.2442 | -0.0160 | [-0.0249, -0.0070] |
| all | bgeL_logreg | 0.2282 | 0.2545 | -0.0263 | [-0.0444, -0.0088] |
| all | gemma_judge_0shot | 0.2282 | 0.2595 | -0.0313 | [-0.0472, -0.0157] |
| all | gemma_judge_0shot_platt | 0.2282 | 0.2595 | -0.0313 | [-0.0472, -0.0157] |
