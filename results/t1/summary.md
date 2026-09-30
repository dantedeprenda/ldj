# t1

Task t1_moderation: 5,000 items, train 3,000, test 2,000 (29.6% positive).

## Within-category AUROC (mean over seeds)

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | 0.831 | 0.855 | 0.869 | 0.897 | 0.898 | 0.913 |
| gemma_judge_0shot | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 | 0.845 |
| gemma_judge_25shot | 0.853 |  | 0.861 |  |  |  |
| base_rate | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 |
| category_prior | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 |
| tfidf_logreg | 0.568 | 0.611 | 0.603 | 0.683 | 0.715 | 0.846 |
| tfidf_knn10 | 0.500 | 0.500 | 0.563 | 0.652 | 0.681 | 0.759 |
| bge_logreg | 0.672 | 0.752 | 0.768 | 0.823 | 0.848 | 0.886 |
| bge_knn | 0.500 | 0.500 | 0.713 | 0.747 | 0.770 | 0.833 |
| bgeL_logreg | 0.699 | 0.779 | 0.782 | 0.835 | 0.837 | 0.897 |
| bgeL_knn | 0.500 | 0.500 | 0.722 | 0.767 | 0.781 | 0.842 |
| setfit | 0.658 | 0.700 | 0.685 | 0.805 | 0.813 | 0.881 |

## Cost per item with thresholds set from the k labels (mean over seeds)

### c_fp=$1.0, c_fn=$1.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.3994 (75% deferred) | $0.2635 (11% deferred) | $0.2319 (10% deferred) | $0.1999 (10% deferred) | $0.1997 (2% deferred) | $0.2442 (0% deferred) |
| gemma_judge_0shot | $0.4098 (84% deferred) | $0.2612 (9% deferred) | $0.2289 (8% deferred) | $0.2190 (12% deferred) | $0.2005 (1% deferred) | $0.2595 (0% deferred) |
| gemma_judge_25shot | $0.4136 (86% deferred) |  | $0.2199 (1% deferred) |  |  |  |
| base_rate | $0.5048 (80% deferred) | $0.3918 (60% deferred) | $0.2971 (0% deferred) | $0.2977 (0% deferred) | $0.2990 (0% deferred) | $0.3715 (0% deferred) |
| category_prior | $0.5048 (80% deferred) | $0.3771 (12% deferred) | $0.3181 (4% deferred) | $0.3506 (12% deferred) | $0.2990 (0% deferred) | $0.3710 (0% deferred) |
| tfidf_logreg | $0.5048 (80% deferred) | $0.3534 (40% deferred) | $0.3310 (26% deferred) | $0.2975 (13% deferred) | $0.2732 (7% deferred) | $0.2726 (0% deferred) |
| tfidf_knn10 | $0.5048 (80% deferred) | $0.3918 (60% deferred) | $0.3011 (4% deferred) | $0.3034 (15% deferred) | $0.3021 (16% deferred) | $0.3265 (0% deferred) |
| bge_logreg | $0.5048 (80% deferred) | $0.3386 (38% deferred) | $0.3226 (16% deferred) | $0.2636 (14% deferred) | $0.2222 (4% deferred) | $0.2531 (0% deferred) |
| bge_knn | $0.5048 (80% deferred) | $0.3918 (60% deferred) | $0.2991 (13% deferred) | $0.2761 (11% deferred) | $0.2680 (1% deferred) | $0.2900 (0% deferred) |
| bgeL_logreg | $0.5048 (80% deferred) | $0.3918 (60% deferred) | $0.3377 (20% deferred) | $0.2538 (6% deferred) | $0.2478 (6% deferred) | $0.2545 (0% deferred) |
| bgeL_knn | $0.5048 (80% deferred) | $0.3918 (60% deferred) | $0.3164 (8% deferred) | $0.2637 (6% deferred) | $0.2561 (4% deferred) | $0.2820 (0% deferred) |
| setfit |  |  |  |  |  |  |

### c_fp=$1.0, c_fn=$1.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.4552 (100% deferred) | $0.3656 (55% deferred) | $0.2376 (12% deferred) | $0.2220 (15% deferred) | $0.2096 (2% deferred) | $0.2442 (0% deferred) |
| gemma_judge_0shot | $0.4481 (98% deferred) | $0.3263 (47% deferred) | $0.2399 (8% deferred) | $0.2340 (19% deferred) | $0.2005 (1% deferred) | $0.2595 (0% deferred) |
| gemma_judge_25shot | $0.4496 (98% deferred) |  | $0.2211 (5% deferred) |  |  |  |
| base_rate | $0.4551 (100% deferred) | $0.4553 (100% deferred) | $0.3922 (60% deferred) | $0.3294 (20% deferred) | $0.2990 (0% deferred) | $0.3715 (0% deferred) |
| category_prior | $0.4551 (100% deferred) | $0.4337 (88% deferred) | $0.3388 (29% deferred) | $0.3663 (44% deferred) | $0.2990 (0% deferred) | $0.3706 (0% deferred) |
| tfidf_logreg | $0.4551 (100% deferred) | $0.4128 (75% deferred) | $0.3634 (47% deferred) | $0.2929 (16% deferred) | $0.2775 (11% deferred) | $0.2726 (0% deferred) |
| tfidf_knn10 | $0.4551 (100% deferred) | $0.4553 (100% deferred) | $0.3592 (40% deferred) | $0.3430 (41% deferred) | $0.3117 (23% deferred) | $0.3265 (0% deferred) |
| bge_logreg | $0.4551 (100% deferred) | $0.4119 (80% deferred) | $0.3378 (40% deferred) | $0.2974 (39% deferred) | $0.2342 (10% deferred) | $0.2531 (0% deferred) |
| bge_knn | $0.4551 (100% deferred) | $0.4553 (100% deferred) | $0.3018 (19% deferred) | $0.3408 (51% deferred) | $0.2930 (20% deferred) | $0.2900 (0% deferred) |
| bgeL_logreg | $0.4551 (100% deferred) | $0.4553 (100% deferred) | $0.3611 (40% deferred) | $0.3375 (47% deferred) | $0.2646 (14% deferred) | $0.2545 (0% deferred) |
| bgeL_knn | $0.4551 (100% deferred) | $0.4553 (100% deferred) | $0.3021 (24% deferred) | $0.2864 (27% deferred) | $0.2764 (10% deferred) | $0.2820 (0% deferred) |
| setfit |  |  |  |  |  |  |

### c_fp=$1.0, c_fn=$5.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.7550 (75% deferred) | $0.7226 (47% deferred) | $0.5508 (21% deferred) | $0.4302 (5% deferred) | $0.3664 (9% deferred) | $0.3783 (0% deferred) |
| gemma_judge_0shot | $0.8606 (84% deferred) | $0.5970 (23% deferred) | $0.6024 (10% deferred) | $0.4950 (17% deferred) | $0.4922 (10% deferred) | $0.5478 (2% deferred) |
| gemma_judge_25shot | $0.8504 (86% deferred) |  | $0.4712 (13% deferred) |  |  |  |
| base_rate | $0.8552 (80% deferred) | $0.8175 (60% deferred) | $0.7420 (20% deferred) | $0.7805 (40% deferred) | $0.7439 (20% deferred) | $0.7785 (0% deferred) |
| category_prior | $0.8552 (80% deferred) | $0.9622 (32% deferred) | $0.7742 (12% deferred) | $0.8346 (36% deferred) | $0.7642 (36% deferred) | $0.7785 (0% deferred) |
| tfidf_logreg | $0.8552 (80% deferred) | $0.7519 (32% deferred) | $0.8324 (2% deferred) | $0.7876 (43% deferred) | $0.6703 (32% deferred) | $0.5184 (8% deferred) |
| tfidf_knn10 | $0.8552 (80% deferred) | $0.8175 (60% deferred) | $0.7837 (10% deferred) | $0.8035 (38% deferred) | $0.7306 (18% deferred) | $0.6775 (0% deferred) |
| bge_logreg | $0.8552 (80% deferred) | $0.7555 (54% deferred) | $0.6965 (12% deferred) | $0.5395 (9% deferred) | $0.4476 (17% deferred) | $0.4378 (2% deferred) |
| bge_knn | $0.8552 (80% deferred) | $0.8175 (60% deferred) | $0.6049 (1% deferred) | $0.6285 (12% deferred) | $0.5505 (14% deferred) | $0.5267 (13% deferred) |
| bgeL_logreg | $0.8552 (80% deferred) | $0.7796 (40% deferred) | $0.6612 (23% deferred) | $0.7682 (10% deferred) | $0.5572 (22% deferred) | $0.4065 (2% deferred) |
| bgeL_knn | $0.8552 (80% deferred) | $0.8175 (60% deferred) | $0.6418 (15% deferred) | $0.5646 (13% deferred) | $0.5484 (11% deferred) | $0.4925 (0% deferred) |
| setfit |  |  |  |  |  |  |

### c_fp=$1.0, c_fn=$5.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.8030 (90% deferred) | $0.7078 (78% deferred) | $0.6027 (37% deferred) | $0.5080 (58% deferred) | $0.4268 (39% deferred) | $0.3783 (0% deferred) |
| gemma_judge_0shot | $0.8745 (98% deferred) | $0.7264 (84% deferred) | $0.5435 (53% deferred) | $0.5270 (52% deferred) | $0.5125 (53% deferred) | $0.5478 (2% deferred) |
| gemma_judge_25shot | $0.8776 (98% deferred) |  | $0.5169 (50% deferred) |  |  |  |
| base_rate | $0.8552 (80% deferred) | $0.8553 (80% deferred) | $0.7420 (20% deferred) | $0.7805 (40% deferred) | $0.7439 (20% deferred) | $0.7785 (0% deferred) |
| category_prior | $0.8552 (80% deferred) | $0.8452 (72% deferred) | $0.7819 (43% deferred) | $0.7792 (44% deferred) | $0.7642 (36% deferred) | $0.7785 (0% deferred) |
| tfidf_logreg | $0.8552 (80% deferred) | $0.8242 (62% deferred) | $0.7405 (21% deferred) | $0.7506 (64% deferred) | $0.6663 (49% deferred) | $0.5184 (8% deferred) |
| tfidf_knn10 | $0.8552 (80% deferred) | $0.8553 (80% deferred) | $0.7405 (22% deferred) | $0.7603 (72% deferred) | $0.7019 (39% deferred) | $0.6775 (0% deferred) |
| bge_logreg | $0.8552 (80% deferred) | $0.7799 (64% deferred) | $0.6354 (48% deferred) | $0.5630 (53% deferred) | $0.5216 (48% deferred) | $0.4373 (5% deferred) |
| bge_knn | $0.8552 (80% deferred) | $0.8553 (80% deferred) | $0.6787 (33% deferred) | $0.6156 (50% deferred) | $0.5689 (38% deferred) | $0.5267 (13% deferred) |
| bgeL_logreg | $0.8552 (80% deferred) | $0.7796 (40% deferred) | $0.7198 (54% deferred) | $0.6569 (58% deferred) | $0.5939 (50% deferred) | $0.4079 (3% deferred) |
| bgeL_knn | $0.8552 (80% deferred) | $0.8553 (80% deferred) | $0.6310 (39% deferred) | $0.5889 (55% deferred) | $0.5639 (42% deferred) | $0.4925 (0% deferred) |
| setfit |  |  |  |  |  |  |

### c_fp=$5.0, c_fn=$1.0, rule=empirical

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.7882 (82% deferred) | $0.5535 (11% deferred) | $0.3541 (12% deferred) | $0.3367 (13% deferred) | $0.2843 (3% deferred) | $0.3432 (0% deferred) |
| gemma_judge_0shot | $0.7578 (84% deferred) | $0.7554 (15% deferred) | $0.3639 (5% deferred) | $0.3163 (5% deferred) | $0.2985 (2% deferred) | $0.3715 (0% deferred) |
| gemma_judge_25shot | $0.7736 (86% deferred) |  | $0.4068 (10% deferred) |  |  |  |
| base_rate | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.2971 (0% deferred) | $0.2977 (0% deferred) | $0.2990 (0% deferred) | $0.3715 (0% deferred) |
| category_prior | $0.8371 (100% deferred) | $0.4421 (28% deferred) | $0.3303 (9% deferred) | $0.3519 (8% deferred) | $0.2990 (0% deferred) | $0.3706 (0% deferred) |
| tfidf_logreg | $0.8371 (100% deferred) | $0.5050 (40% deferred) | $0.4494 (26% deferred) | $0.3677 (15% deferred) | $0.3194 (5% deferred) | $0.3619 (1% deferred) |
| tfidf_knn10 | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.3287 (4% deferred) | $0.3345 (10% deferred) | $0.3186 (5% deferred) | $0.3715 (0% deferred) |
| bge_logreg | $0.8371 (100% deferred) | $0.5846 (38% deferred) | $0.4040 (23% deferred) | $0.4000 (17% deferred) | $0.3063 (7% deferred) | $0.3715 (3% deferred) |
| bge_knn | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.4736 (15% deferred) | $0.3411 (13% deferred) | $0.3283 (4% deferred) | $0.3679 (1% deferred) |
| bgeL_logreg | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.4074 (20% deferred) | $0.3633 (9% deferred) | $0.3216 (5% deferred) | $0.3526 (6% deferred) |
| bgeL_knn | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.3671 (14% deferred) | $0.3422 (10% deferred) | $0.3130 (1% deferred) | $0.3638 (3% deferred) |
| setfit |  |  |  |  |  |  |

### c_fp=$5.0, c_fn=$1.0, rule=ucb

| method | k=5 | k=10 | k=25 | k=50 | k=100 | k=all |
|---|---|---|---|---|---|---|
| gemma_features | $0.8372 (100% deferred) | $0.5273 (46% deferred) | $0.3392 (14% deferred) | $0.3354 (20% deferred) | $0.2825 (11% deferred) | $0.3432 (0% deferred) |
| gemma_judge_0shot | $0.8371 (100% deferred) | $0.5752 (55% deferred) | $0.3750 (18% deferred) | $0.3233 (10% deferred) | $0.2950 (4% deferred) | $0.3715 (0% deferred) |
| gemma_judge_25shot | $0.8372 (100% deferred) |  | $0.3768 (19% deferred) |  |  |  |
| base_rate | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.5133 (40% deferred) | $0.2977 (0% deferred) | $0.2990 (0% deferred) | $0.3715 (0% deferred) |
| category_prior | $0.8371 (100% deferred) | $0.6042 (60% deferred) | $0.4384 (29% deferred) | $0.3519 (8% deferred) | $0.2990 (0% deferred) | $0.3706 (0% deferred) |
| tfidf_logreg | $0.8371 (100% deferred) | $0.5909 (56% deferred) | $0.4411 (27% deferred) | $0.3583 (17% deferred) | $0.3165 (6% deferred) | $0.3686 (2% deferred) |
| tfidf_knn10 | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.4134 (22% deferred) | $0.3318 (10% deferred) | $0.3121 (6% deferred) | $0.3728 (0% deferred) |
| bge_logreg | $0.8371 (100% deferred) | $0.6321 (61% deferred) | $0.4010 (23% deferred) | $0.3969 (26% deferred) | $0.3048 (8% deferred) | $0.3704 (4% deferred) |
| bge_knn | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.3890 (22% deferred) | $0.3411 (13% deferred) | $0.3181 (6% deferred) | $0.3679 (1% deferred) |
| bgeL_logreg | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.4074 (20% deferred) | $0.4447 (35% deferred) | $0.3146 (10% deferred) | $0.3563 (8% deferred) |
| bgeL_knn | $0.8371 (100% deferred) | $0.6210 (60% deferred) | $0.3517 (16% deferred) | $0.3500 (19% deferred) | $0.3013 (1% deferred) | $0.3683 (4% deferred) |
| setfit |  |  |  |  |  |  |

