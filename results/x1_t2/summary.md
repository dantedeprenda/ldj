# x1_t2

Task t2_screening: 15,121 items, train 7,560, test 7,561 (6.3% positive).

## Within-category AUROC (mean over seeds)

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | 0.738 | 0.773 | 0.804 | 0.828 | 0.852 | 0.903 |
| gemma_features | 0.840 | 0.851 | 0.862 | 0.890 | 0.892 | 0.896 |
| gemma_judge_0shot | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 |
| gemma_judge_0shot_platt | 0.779 | 0.799 | 0.817 | 0.834 | 0.845 | 0.845 |
| gemma_features_judge | 0.858 | 0.865 | 0.883 | 0.907 | 0.909 | 0.916 |

## Cost per item with thresholds set from the k labels (mean over seeds)

### c_fp=$1.83, c_fn=$20.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $2.2223 (82% deferred) | $2.0861 (69% deferred) | $1.5564 (21% deferred) | $1.1343 (15% deferred) | $1.1119 (11% deferred) | $0.9372 (0% deferred) |
| gemma_features | $2.1786 (87% deferred) | $1.8323 (68% deferred) | $1.0361 (23% deferred) | $0.8107 (17% deferred) | $0.7486 (11% deferred) | $0.8944 (1% deferred) |
| gemma_judge_0shot | $2.1471 (85% deferred) | $1.8695 (67% deferred) | $1.0892 (22% deferred) | $0.9340 (16% deferred) | $0.8420 (11% deferred) | $0.9831 (0% deferred) |
| gemma_judge_0shot_platt | $2.1876 (87% deferred) | $1.8801 (66% deferred) | $1.1504 (23% deferred) | $0.9437 (17% deferred) | $0.8345 (11% deferred) | $0.9808 (0% deferred) |
| gemma_features_judge | $2.1514 (86% deferred) | $1.8232 (68% deferred) | $1.0433 (24% deferred) | $0.8043 (17% deferred) | $0.7250 (11% deferred) | $0.8743 (0% deferred) |

### c_fp=$1.83, c_fn=$20.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $2.2223 (82% deferred) | $2.0868 (65% deferred) | $1.9045 (34% deferred) | $1.3364 (17% deferred) | $1.1118 (11% deferred) | $0.9337 (0% deferred) |
| gemma_features | $2.2586 (89% deferred) | $2.1175 (73% deferred) | $1.8716 (30% deferred) | $0.9906 (16% deferred) | $0.7888 (11% deferred) | $0.9069 (1% deferred) |
| gemma_judge_0shot | $2.2217 (82% deferred) | $2.0842 (65% deferred) | $1.8326 (20% deferred) | $1.1046 (16% deferred) | $0.8987 (10% deferred) | $0.9814 (0% deferred) |
| gemma_judge_0shot_platt | $2.2545 (88% deferred) | $2.1242 (74% deferred) | $1.8612 (27% deferred) | $1.1488 (16% deferred) | $0.9315 (11% deferred) | $0.9768 (0% deferred) |
| gemma_features_judge | $2.2551 (89% deferred) | $2.1204 (73% deferred) | $1.8738 (31% deferred) | $0.9871 (16% deferred) | $0.7651 (11% deferred) | $0.8860 (0% deferred) |

### c_fp=$1.83, c_fn=$20.0, rule=recall95_empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $2.3600 (100% deferred) | $2.2225 (81% deferred) | $1.9876 (75% deferred) | $1.7962 (65% deferred) | $1.7411 (64% deferred) | $1.9423 (57% deferred) |
| gemma_features | $2.1782 (89% deferred) | $1.9682 (78% deferred) | $1.4966 (54% deferred) | $1.2670 (43% deferred) | $1.2885 (44% deferred) | $1.5592 (41% deferred) |
| gemma_judge_0shot | $2.1976 (90% deferred) | $2.0462 (81% deferred) | $1.5538 (56% deferred) | $1.5846 (60% deferred) | $1.6348 (62% deferred) | $2.2884 (75% deferred) |
| gemma_judge_0shot_platt | $2.2062 (90% deferred) | $2.0527 (81% deferred) | $1.7002 (63% deferred) | $1.6509 (63% deferred) | $1.7217 (66% deferred) | $2.2770 (74% deferred) |
| gemma_features_judge | $2.1773 (89% deferred) | $1.9626 (77% deferred) | $1.4844 (53% deferred) | $1.2597 (43% deferred) | $1.2842 (44% deferred) | $1.5223 (39% deferred) |

### c_fp=$1.83, c_fn=$20.0, rule=recall95_ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.6286 (91% deferred) |
| gemma_features | $2.3640 (100% deferred) | $2.3686 (100% deferred) | $2.3823 (100% deferred) | $2.4044 (100% deferred) | $2.4471 (100% deferred) | $2.5473 (87% deferred) |
| gemma_judge_0shot | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3823 (100% deferred) | $2.4043 (100% deferred) | $2.4471 (100% deferred) | $2.7501 (96% deferred) |
| gemma_judge_0shot_platt | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3823 (100% deferred) | $2.4043 (100% deferred) | $2.4471 (100% deferred) | $2.7501 (96% deferred) |
| gemma_features_judge | $2.3640 (100% deferred) | $2.3686 (100% deferred) | $2.3824 (100% deferred) | $2.4044 (100% deferred) | $2.4472 (100% deferred) | $2.5473 (87% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $2.7131 (82% deferred) | $3.3033 (69% deferred) | $2.2829 (21% deferred) | $2.1718 (15% deferred) | $1.7047 (11% deferred) | $1.4494 (0% deferred) |
| gemma_features | $2.8099 (87% deferred) | $2.3763 (68% deferred) | $1.7401 (23% deferred) | $1.4194 (17% deferred) | $1.2468 (11% deferred) | $1.2757 (0% deferred) |
| gemma_judge_0shot | $2.7929 (85% deferred) | $2.5144 (67% deferred) | $1.8474 (22% deferred) | $1.4666 (15% deferred) | $1.3226 (10% deferred) | $1.4135 (0% deferred) |
| gemma_judge_0shot_platt | $2.8150 (87% deferred) | $2.5486 (66% deferred) | $1.9246 (22% deferred) | $1.5394 (18% deferred) | $1.4237 (11% deferred) | $1.4628 (0% deferred) |
| gemma_features_judge | $2.7375 (86% deferred) | $2.3756 (68% deferred) | $1.6388 (23% deferred) | $1.4098 (17% deferred) | $1.3167 (11% deferred) | $1.2276 (0% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $2.7131 (82% deferred) | $2.3837 (65% deferred) | $1.9977 (34% deferred) | $1.9098 (23% deferred) | $1.9126 (20% deferred) | $1.5052 (0% deferred) |
| gemma_features | $2.7712 (89% deferred) | $2.4172 (73% deferred) | $1.9176 (30% deferred) | $1.8829 (23% deferred) | $1.8847 (15% deferred) | $1.2541 (0% deferred) |
| gemma_judge_0shot | $2.7125 (82% deferred) | $2.3779 (65% deferred) | $1.8765 (20% deferred) | $1.8524 (15% deferred) | $1.8661 (10% deferred) | $1.5051 (0% deferred) |
| gemma_judge_0shot_platt | $2.7706 (88% deferred) | $2.4322 (74% deferred) | $1.9126 (27% deferred) | $1.8915 (25% deferred) | $1.8893 (16% deferred) | $1.5357 (0% deferred) |
| gemma_features_judge | $2.7589 (89% deferred) | $2.4218 (73% deferred) | $1.9197 (31% deferred) | $1.8844 (23% deferred) | $1.8845 (15% deferred) | $1.2112 (0% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=recall95_empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $3.0464 (100% deferred) | $3.9901 (81% deferred) | $3.2586 (75% deferred) | $3.1387 (65% deferred) | $2.8050 (64% deferred) | $2.9055 (57% deferred) |
| gemma_features | $3.0735 (89% deferred) | $2.9973 (78% deferred) | $2.7071 (54% deferred) | $2.4244 (43% deferred) | $2.2609 (44% deferred) | $2.4032 (41% deferred) |
| gemma_judge_0shot | $3.0801 (90% deferred) | $3.1468 (81% deferred) | $2.7863 (56% deferred) | $2.4983 (60% deferred) | $2.4697 (62% deferred) | $3.0409 (75% deferred) |
| gemma_judge_0shot_platt | $3.1235 (90% deferred) | $3.1515 (81% deferred) | $2.9090 (63% deferred) | $2.5665 (63% deferred) | $2.5346 (66% deferred) | $3.0386 (74% deferred) |
| gemma_features_judge | $3.0763 (89% deferred) | $3.0100 (77% deferred) | $2.6931 (53% deferred) | $2.4079 (43% deferred) | $2.2565 (44% deferred) | $2.3664 (39% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=recall95_ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| bgeL_logreg | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.3260 (91% deferred) |
| gemma_features | $3.0431 (100% deferred) | $3.0477 (100% deferred) | $3.0614 (100% deferred) | $3.0835 (100% deferred) | $3.1263 (100% deferred) | $3.2631 (87% deferred) |
| gemma_judge_0shot | $3.0431 (100% deferred) | $3.0476 (100% deferred) | $3.0614 (100% deferred) | $3.0835 (100% deferred) | $3.1262 (100% deferred) | $3.4659 (96% deferred) |
| gemma_judge_0shot_platt | $3.0431 (100% deferred) | $3.0476 (100% deferred) | $3.0614 (100% deferred) | $3.0835 (100% deferred) | $3.1262 (100% deferred) | $3.4659 (96% deferred) |
| gemma_features_judge | $3.0432 (100% deferred) | $3.0477 (100% deferred) | $3.0615 (100% deferred) | $3.0835 (100% deferred) | $3.1263 (100% deferred) | $3.2539 (87% deferred) |

