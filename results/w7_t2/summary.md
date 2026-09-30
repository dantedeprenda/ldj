# W7 summary (macro over reviews; exploratory)

| arm | stopping | work saved | mean recall | runs with recall >= 0.95 | reviews meeting it in >= 95% of runs | screened |
|---|---|---|---|---|---|---|
| a_judge_static | certified_95 | 0.117 | 0.987 | 0.94 | 0.53 | 879 |
| a_judge_static | heuristic_50 | 0.588 | 0.860 | 0.36 | 0.20 | 260 |
| b_features_static | certified_95 | 0.146 | 0.990 | 0.94 | 0.47 | 837 |
| b_features_static | heuristic_50 | 0.584 | 0.814 | 0.57 | 0.13 | 268 |
| c_active | certified_95 | 0.150 | 0.998 | 1.00 | 1.00 | 833 |
| c_active | heuristic_50 | 0.541 | 0.894 | 0.61 | 0.40 | 310 |
| d_active_llm | certified_95 | 0.131 | 0.997 | 1.00 | 1.00 | 850 |
| d_active_llm | heuristic_50 | 0.552 | 0.894 | 0.46 | 0.40 | 297 |
