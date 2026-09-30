# x1_t1

Task t1_moderation: 5,000 items, train 3,000, test 2,000 (29.6% positive).

## Within-category AUROC (mean over seeds)

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | 0.831 | 0.855 | 0.869 | 0.897 | 0.898 | 0.913 |
| gemma_judge_0shot | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 |
| gemma_judge_0shot_platt | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 |
| gemma_features_judge | 0.860 | 0.877 | 0.881 | 0.908 | 0.907 | 0.920 |
| bgeL_logreg | 0.699 | 0.779 | 0.782 | 0.835 | 0.837 | 0.897 |

## Cost per item with thresholds set from the k labels (mean over seeds)

### c_fp=$1.0, c_fn=$1.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.3994 (75% deferred) | $0.2635 (11% deferred) | $0.2319 (10% deferred) | $0.1999 (10% deferred) | $0.1997 (2% deferred) | $0.2442 (0% deferred) |
| gemma_judge_0shot | $0.4098 (84% deferred) | $0.2612 (9% deferred) | $0.2289 (8% deferred) | $0.2190 (12% deferred) | $0.2005 (1% deferred) | $0.2595 (0% deferred) |
| gemma_judge_0shot_platt | $0.4001 (74% deferred) | $0.2750 (14% deferred) | $0.2533 (15% deferred) | $0.2267 (17% deferred) | $0.2027 (4% deferred) | $0.2595 (0% deferred) |
| gemma_features_judge | $0.3921 (74% deferred) | $0.2605 (17% deferred) | $0.2235 (8% deferred) | $0.1931 (6% deferred) | $0.1899 (1% deferred) | $0.2286 (0% deferred) |
| bgeL_logreg | $0.5048 (80% deferred) | $0.3918 (60% deferred) | $0.3377 (20% deferred) | $0.2538 (6% deferred) | $0.2478 (6% deferred) | $0.2545 (0% deferred) |

### c_fp=$1.0, c_fn=$1.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.4552 (100% deferred) | $0.3656 (55% deferred) | $0.2376 (12% deferred) | $0.2220 (15% deferred) | $0.2096 (2% deferred) | $0.2442 (0% deferred) |
| gemma_judge_0shot | $0.4481 (98% deferred) | $0.3263 (47% deferred) | $0.2399 (8% deferred) | $0.2340 (19% deferred) | $0.2005 (1% deferred) | $0.2595 (0% deferred) |
| gemma_judge_0shot_platt | $0.4438 (91% deferred) | $0.3436 (59% deferred) | $0.2523 (12% deferred) | $0.2415 (19% deferred) | $0.2031 (4% deferred) | $0.2595 (0% deferred) |
| gemma_features_judge | $0.4552 (100% deferred) | $0.3610 (61% deferred) | $0.2472 (18% deferred) | $0.2241 (19% deferred) | $0.2001 (5% deferred) | $0.2282 (0% deferred) |
| bgeL_logreg | $0.4551 (100% deferred) | $0.4553 (100% deferred) | $0.3611 (40% deferred) | $0.3375 (47% deferred) | $0.2646 (14% deferred) | $0.2545 (0% deferred) |

### c_fp=$1.0, c_fn=$5.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.7550 (75% deferred) | $0.7226 (47% deferred) | $0.5508 (21% deferred) | $0.4302 (5% deferred) | $0.3664 (9% deferred) | $0.3783 (0% deferred) |
| gemma_judge_0shot | $0.8606 (84% deferred) | $0.5970 (23% deferred) | $0.6024 (10% deferred) | $0.4950 (17% deferred) | $0.4922 (10% deferred) | $0.5478 (2% deferred) |
| gemma_judge_0shot_platt | $0.8229 (74% deferred) | $0.5190 (19% deferred) | $0.6326 (15% deferred) | $0.5164 (22% deferred) | $0.4945 (13% deferred) | $0.5430 (17% deferred) |
| gemma_features_judge | $0.7537 (74% deferred) | $0.6277 (36% deferred) | $0.5057 (12% deferred) | $0.3841 (13% deferred) | $0.3427 (12% deferred) | $0.3694 (1% deferred) |
| bgeL_logreg | $0.8552 (80% deferred) | $0.7796 (40% deferred) | $0.6612 (23% deferred) | $0.7682 (10% deferred) | $0.5572 (22% deferred) | $0.4065 (2% deferred) |

### c_fp=$1.0, c_fn=$5.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.8030 (90% deferred) | $0.7078 (78% deferred) | $0.6027 (37% deferred) | $0.5080 (58% deferred) | $0.4268 (39% deferred) | $0.3783 (0% deferred) |
| gemma_judge_0shot | $0.8745 (98% deferred) | $0.7264 (84% deferred) | $0.5435 (53% deferred) | $0.5270 (52% deferred) | $0.5125 (53% deferred) | $0.5478 (2% deferred) |
| gemma_judge_0shot_platt | $0.8138 (91% deferred) | $0.7264 (84% deferred) | $0.5907 (50% deferred) | $0.5396 (57% deferred) | $0.5145 (56% deferred) | $0.5430 (17% deferred) |
| gemma_features_judge | $0.8006 (91% deferred) | $0.6585 (76% deferred) | $0.6071 (38% deferred) | $0.4976 (54% deferred) | $0.3713 (27% deferred) | $0.3694 (1% deferred) |
| bgeL_logreg | $0.8552 (80% deferred) | $0.7796 (40% deferred) | $0.7198 (54% deferred) | $0.6569 (58% deferred) | $0.5939 (50% deferred) | $0.4079 (3% deferred) |

### c_fp=$5.0, c_fn=$1.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.7882 (82% deferred) | $0.5535 (11% deferred) | $0.3541 (12% deferred) | $0.3367 (13% deferred) | $0.2843 (3% deferred) | $0.3432 (0% deferred) |
| gemma_judge_0shot | $0.7578 (84% deferred) | $0.7554 (15% deferred) | $0.3639 (5% deferred) | $0.3163 (5% deferred) | $0.2985 (2% deferred) | $0.3715 (0% deferred) |
| gemma_judge_0shot_platt | $0.8349 (74% deferred) | $0.8010 (21% deferred) | $0.4670 (14% deferred) | $0.3339 (7% deferred) | $0.3137 (6% deferred) | $0.3715 (0% deferred) |
| gemma_features_judge | $0.7720 (80% deferred) | $0.5733 (17% deferred) | $0.3340 (11% deferred) | $0.3144 (9% deferred) | $0.2865 (6% deferred) | $0.3257 (0% deferred) |
| bgeL_logreg | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.4074 (20% deferred) | $0.3633 (9% deferred) | $0.3216 (5% deferred) | $0.3526 (6% deferred) |

### c_fp=$5.0, c_fn=$1.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.8372 (100% deferred) | $0.5273 (46% deferred) | $0.3392 (14% deferred) | $0.3354 (20% deferred) | $0.2825 (11% deferred) | $0.3432 (0% deferred) |
| gemma_judge_0shot | $0.8371 (100% deferred) | $0.5752 (55% deferred) | $0.3750 (18% deferred) | $0.3233 (10% deferred) | $0.2950 (4% deferred) | $0.3715 (0% deferred) |
| gemma_judge_0shot_platt | $0.8371 (100% deferred) | $0.5688 (55% deferred) | $0.3935 (21% deferred) | $0.3284 (12% deferred) | $0.3098 (4% deferred) | $0.3715 (0% deferred) |
| gemma_features_judge | $0.8372 (100% deferred) | $0.5447 (48% deferred) | $0.3231 (12% deferred) | $0.3387 (21% deferred) | $0.2884 (11% deferred) | $0.3328 (0% deferred) |
| bgeL_logreg | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.4074 (20% deferred) | $0.4447 (35% deferred) | $0.3146 (10% deferred) | $0.3563 (8% deferred) |

