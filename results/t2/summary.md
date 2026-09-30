# t2

Task t2_screening: 15,121 items, train 7,560, test 7,561 (6.3% positive).

## Within-category AUROC (mean over seeds)

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 |
| tfidf_logreg | 0.686 | 0.704 | 0.758 | 0.788 | 0.806 | 0.894 |
| tfidf_knn10 | 0.500 | 0.500 | 0.676 | 0.733 | 0.750 | 0.827 |
| bge_logreg | 0.723 | 0.760 | 0.788 | 0.821 | 0.839 | 0.895 |
| bge_knn | 0.500 | 0.500 | 0.677 | 0.758 | 0.786 | 0.838 |
| bgeL_logreg | 0.738 | 0.773 | 0.804 | 0.828 | 0.852 | 0.903 |
| bgeL_knn | 0.500 | 0.500 | 0.681 | 0.765 | 0.790 | 0.841 |
| gemma_features | 0.840 | 0.851 | 0.862 | 0.890 | 0.892 | 0.896 |
| gemma_judge_0shot | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 |

## Cost per item with thresholds set from the k labels (mean over seeds)

### c_fp=$1.83, c_fn=$20.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.5156 (20% deferred) | $1.3162 (15% deferred) | $1.2644 (10% deferred) | $1.4187 (0% deferred) |
| tfidf_logreg | $2.2208 (82% deferred) | $2.0230 (70% deferred) | $1.4628 (22% deferred) | $1.1354 (16% deferred) | $0.9752 (11% deferred) | $0.9332 (0% deferred) |
| tfidf_knn10 | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.5734 (25% deferred) | $1.1727 (16% deferred) | $1.0248 (10% deferred) | $1.0271 (0% deferred) |
| bge_logreg | $2.2208 (82% deferred) | $1.9484 (67% deferred) | $1.3222 (23% deferred) | $1.0921 (17% deferred) | $0.9147 (11% deferred) | $0.9254 (0% deferred) |
| bge_knn | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.5366 (27% deferred) | $1.1635 (17% deferred) | $0.9604 (11% deferred) | $0.9864 (0% deferred) |
| bgeL_logreg | $2.2223 (82% deferred) | $2.0861 (69% deferred) | $1.5564 (21% deferred) | $1.1343 (15% deferred) | $1.1119 (11% deferred) | $0.9372 (0% deferred) |
| bgeL_knn | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.5178 (28% deferred) | $1.1561 (17% deferred) | $0.9507 (11% deferred) | $1.0021 (0% deferred) |
| gemma_features | $2.1786 (87% deferred) | $1.8323 (68% deferred) | $1.0361 (23% deferred) | $0.8107 (17% deferred) | $0.7486 (11% deferred) | $0.8944 (1% deferred) |
| gemma_judge_0shot | $2.1471 (85% deferred) | $1.8695 (67% deferred) | $1.0892 (22% deferred) | $0.9340 (16% deferred) | $0.8420 (11% deferred) | $0.9831 (0% deferred) |

### c_fp=$1.83, c_fn=$20.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.8325 (20% deferred) | $1.8269 (15% deferred) | $1.3517 (10% deferred) | $1.4383 (0% deferred) |
| tfidf_logreg | $2.2208 (82% deferred) | $2.1174 (70% deferred) | $1.8398 (22% deferred) | $1.3454 (16% deferred) | $1.1712 (11% deferred) | $0.9313 (0% deferred) |
| tfidf_knn10 | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.8408 (22% deferred) | $1.5577 (15% deferred) | $1.1677 (10% deferred) | $1.0209 (0% deferred) |
| bge_logreg | $2.2208 (82% deferred) | $2.1271 (73% deferred) | $1.8534 (26% deferred) | $1.2272 (17% deferred) | $0.9586 (11% deferred) | $0.9309 (0% deferred) |
| bge_knn | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.8409 (22% deferred) | $1.5207 (15% deferred) | $1.0408 (11% deferred) | $0.9996 (0% deferred) |
| bgeL_logreg | $2.2223 (82% deferred) | $2.0868 (65% deferred) | $1.9045 (34% deferred) | $1.3364 (17% deferred) | $1.1118 (11% deferred) | $0.9337 (0% deferred) |
| bgeL_knn | $2.2208 (82% deferred) | $2.0841 (65% deferred) | $1.8390 (22% deferred) | $1.5475 (15% deferred) | $1.0293 (11% deferred) | $0.9880 (0% deferred) |
| gemma_features | $2.2586 (89% deferred) | $2.1175 (73% deferred) | $1.8716 (30% deferred) | $0.9906 (16% deferred) | $0.7888 (11% deferred) | $0.9069 (1% deferred) |
| gemma_judge_0shot | $2.2217 (82% deferred) | $2.0842 (65% deferred) | $1.8326 (20% deferred) | $1.1046 (16% deferred) | $0.8987 (10% deferred) | $0.9814 (0% deferred) |

### c_fp=$1.83, c_fn=$20.0, rule=recall95_empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.8212 (100% deferred) |
| tfidf_logreg | $2.3639 (100% deferred) | $2.1281 (80% deferred) | $1.8959 (72% deferred) | $1.7001 (65% deferred) | $1.6966 (64% deferred) | $1.7734 (50% deferred) |
| tfidf_knn10 | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.1189 (85% deferred) | $1.8684 (72% deferred) | $2.0032 (78% deferred) | $2.6854 (93% deferred) |
| bge_logreg | $2.3639 (100% deferred) | $2.0998 (81% deferred) | $1.7168 (65% deferred) | $1.4650 (52% deferred) | $1.4712 (53% deferred) | $1.6524 (44% deferred) |
| bge_knn | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.0514 (83% deferred) | $1.7043 (64% deferred) | $1.8368 (71% deferred) | $2.4333 (80% deferred) |
| bgeL_logreg | $2.3600 (100% deferred) | $2.2225 (81% deferred) | $1.9876 (75% deferred) | $1.7962 (65% deferred) | $1.7411 (64% deferred) | $1.9423 (57% deferred) |
| bgeL_knn | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.0510 (83% deferred) | $1.7273 (65% deferred) | $1.7990 (68% deferred) | $2.6054 (89% deferred) |
| gemma_features | $2.1782 (89% deferred) | $1.9682 (78% deferred) | $1.4966 (54% deferred) | $1.2670 (43% deferred) | $1.2885 (44% deferred) | $1.5592 (41% deferred) |
| gemma_judge_0shot | $2.1976 (90% deferred) | $2.0462 (81% deferred) | $1.5538 (56% deferred) | $1.5846 (60% deferred) | $1.6348 (62% deferred) | $2.2884 (75% deferred) |

### c_fp=$1.83, c_fn=$20.0, rule=recall95_ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.8212 (100% deferred) |
| tfidf_logreg | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.5958 (89% deferred) |
| tfidf_knn10 | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.8110 (99% deferred) |
| bge_logreg | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.6116 (89% deferred) |
| bge_knn | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.7126 (94% deferred) |
| bgeL_logreg | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.6286 (91% deferred) |
| bgeL_knn | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3822 (100% deferred) | $2.4043 (100% deferred) | $2.4470 (100% deferred) | $2.7108 (95% deferred) |
| gemma_features | $2.3640 (100% deferred) | $2.3686 (100% deferred) | $2.3823 (100% deferred) | $2.4044 (100% deferred) | $2.4471 (100% deferred) | $2.5473 (87% deferred) |
| gemma_judge_0shot | $2.3639 (100% deferred) | $2.3685 (100% deferred) | $2.3823 (100% deferred) | $2.4043 (100% deferred) | $2.4471 (100% deferred) | $2.7501 (96% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $1.8765 (20% deferred) | $1.8524 (15% deferred) | $1.8661 (10% deferred) | $2.0765 (0% deferred) |
| tfidf_logreg | $2.7106 (82% deferred) | $2.9841 (70% deferred) | $2.1004 (24% deferred) | $1.6140 (16% deferred) | $1.4910 (11% deferred) | $1.3523 (0% deferred) |
| tfidf_knn10 | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $2.0032 (22% deferred) | $1.7879 (15% deferred) | $1.6810 (10% deferred) | $1.4941 (0% deferred) |
| bge_logreg | $2.7106 (82% deferred) | $2.8207 (67% deferred) | $1.8221 (24% deferred) | $1.6233 (17% deferred) | $1.3428 (11% deferred) | $1.4022 (0% deferred) |
| bge_knn | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $1.8894 (21% deferred) | $1.7446 (15% deferred) | $1.5370 (10% deferred) | $1.4657 (0% deferred) |
| bgeL_logreg | $2.7131 (82% deferred) | $3.3033 (69% deferred) | $2.2829 (21% deferred) | $2.1718 (15% deferred) | $1.7047 (11% deferred) | $1.4494 (0% deferred) |
| bgeL_knn | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $1.8778 (22% deferred) | $1.7564 (15% deferred) | $1.5697 (10% deferred) | $1.4832 (0% deferred) |
| gemma_features | $2.8099 (87% deferred) | $2.3763 (68% deferred) | $1.7401 (23% deferred) | $1.4194 (17% deferred) | $1.2468 (11% deferred) | $1.2757 (0% deferred) |
| gemma_judge_0shot | $2.7929 (85% deferred) | $2.5144 (67% deferred) | $1.8474 (22% deferred) | $1.4666 (15% deferred) | $1.3226 (10% deferred) | $1.4135 (0% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $1.8765 (20% deferred) | $1.8524 (15% deferred) | $1.8661 (10% deferred) | $2.1760 (0% deferred) |
| tfidf_logreg | $2.7106 (82% deferred) | $2.4396 (70% deferred) | $1.8860 (22% deferred) | $1.8650 (18% deferred) | $1.8760 (13% deferred) | $1.4694 (0% deferred) |
| tfidf_knn10 | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $1.8904 (22% deferred) | $1.8526 (15% deferred) | $1.8661 (10% deferred) | $1.6045 (0% deferred) |
| bge_logreg | $2.7106 (82% deferred) | $2.4467 (73% deferred) | $1.9013 (26% deferred) | $1.8748 (21% deferred) | $1.8782 (13% deferred) | $1.4794 (1% deferred) |
| bge_knn | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $1.8872 (22% deferred) | $1.8527 (15% deferred) | $1.8661 (10% deferred) | $1.6492 (0% deferred) |
| bgeL_logreg | $2.7131 (82% deferred) | $2.3837 (65% deferred) | $1.9977 (34% deferred) | $1.9098 (23% deferred) | $1.9126 (20% deferred) | $1.5052 (0% deferred) |
| bgeL_knn | $2.7106 (82% deferred) | $2.3779 (65% deferred) | $1.8835 (22% deferred) | $1.8526 (15% deferred) | $1.8661 (10% deferred) | $1.6744 (0% deferred) |
| gemma_features | $2.7712 (89% deferred) | $2.4172 (73% deferred) | $1.9176 (30% deferred) | $1.8829 (23% deferred) | $1.8847 (15% deferred) | $1.2541 (0% deferred) |
| gemma_judge_0shot | $2.7125 (82% deferred) | $2.3779 (65% deferred) | $1.8765 (20% deferred) | $1.8524 (15% deferred) | $1.8661 (10% deferred) | $1.5051 (0% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=recall95_empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.5004 (100% deferred) |
| tfidf_logreg | $3.0430 (100% deferred) | $3.5788 (80% deferred) | $3.0771 (72% deferred) | $2.6541 (65% deferred) | $2.5865 (64% deferred) | $2.6816 (50% deferred) |
| tfidf_knn10 | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0839 (85% deferred) | $2.8480 (72% deferred) | $2.8363 (78% deferred) | $3.4195 (93% deferred) |
| bge_logreg | $3.0430 (100% deferred) | $3.4148 (81% deferred) | $2.8229 (65% deferred) | $2.5968 (52% deferred) | $2.3995 (53% deferred) | $2.6065 (44% deferred) |
| bge_knn | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $2.9486 (83% deferred) | $2.7573 (64% deferred) | $2.6717 (71% deferred) | $3.2865 (80% deferred) |
| bgeL_logreg | $3.0464 (100% deferred) | $3.9901 (81% deferred) | $3.2586 (75% deferred) | $3.1387 (65% deferred) | $2.8050 (64% deferred) | $2.9055 (57% deferred) |
| bgeL_knn | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $2.9317 (83% deferred) | $2.7748 (65% deferred) | $2.6925 (68% deferred) | $3.3762 (89% deferred) |
| gemma_features | $3.0735 (89% deferred) | $2.9973 (78% deferred) | $2.7071 (54% deferred) | $2.4244 (43% deferred) | $2.2609 (44% deferred) | $2.4032 (41% deferred) |
| gemma_judge_0shot | $3.0801 (90% deferred) | $3.1468 (81% deferred) | $2.7863 (56% deferred) | $2.4983 (60% deferred) | $2.4697 (62% deferred) | $3.0409 (75% deferred) |

### c_fp=$1.83, c_fn=$100.0, rule=recall95_ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| base_rate | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.5004 (100% deferred) |
| tfidf_logreg | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.3390 (89% deferred) |
| tfidf_knn10 | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.5084 (99% deferred) |
| bge_logreg | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.4190 (89% deferred) |
| bge_knn | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.4559 (94% deferred) |
| bgeL_logreg | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.3260 (91% deferred) |
| bgeL_knn | $3.0430 (100% deferred) | $3.0476 (100% deferred) | $3.0613 (100% deferred) | $3.0834 (100% deferred) | $3.1262 (100% deferred) | $3.4266 (95% deferred) |
| gemma_features | $3.0431 (100% deferred) | $3.0477 (100% deferred) | $3.0614 (100% deferred) | $3.0835 (100% deferred) | $3.1263 (100% deferred) | $3.2631 (87% deferred) |
| gemma_judge_0shot | $3.0431 (100% deferred) | $3.0476 (100% deferred) | $3.0614 (100% deferred) | $3.0835 (100% deferred) | $3.1262 (100% deferred) | $3.4659 (96% deferred) |

