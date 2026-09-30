# Pre-registered analysis: x1_t2

Primary method: **gemma_features_judge**. Best text baseline at k = 25 (pre-registered rule): **gemma_features** (0.862; others: bgeL_logreg 0.804).

## A. Within-category AUROC, primary minus comparator (95% CI, hierarchical bootstrap)

| k | comparator | primary | comparator | diff | 95% CI | seeds won |
|---|---|---|---|---|---|---|
| 5 | gemma_features (best) | 0.858 | 0.840 | +0.018 | [+0.011, +0.026] | 5/5 |
| 5 | bgeL_logreg | 0.858 | 0.738 | +0.119 | [+0.081, +0.168] | 5/5 |
| 5 | gemma_judge_0shot | 0.858 | 0.845 | +0.013 | [-0.040, +0.057] | 3/5 |
| 5 | gemma_judge_0shot_platt | 0.858 | 0.779 | +0.078 | [+0.042, +0.112] | 5/5 |
| 10 | gemma_features (best) | 0.865 | 0.851 | +0.015 | [-0.000, +0.031] | 4/5 |
| 10 | bgeL_logreg | 0.865 | 0.773 | +0.092 | [+0.063, +0.126] | 5/5 |
| 10 | gemma_judge_0shot | 0.865 | 0.845 | +0.020 | [-0.022, +0.057] | 4/5 |
| 10 | gemma_judge_0shot_platt | 0.865 | 0.799 | +0.066 | [+0.026, +0.102] | 5/5 |
| 25 | gemma_features (best) | 0.883 | 0.862 | +0.021 | [+0.011, +0.039] | 5/5 |
| 25 | bgeL_logreg | 0.883 | 0.804 | +0.079 | [+0.021, +0.135] | 4/5 |
| 25 | gemma_judge_0shot | 0.883 | 0.845 | +0.038 | [-0.004, +0.074] | 4/5 |
| 25 | gemma_judge_0shot_platt | 0.883 | 0.817 | +0.066 | [+0.026, +0.100] | 5/5 |
| 50 | gemma_features (best) | 0.907 | 0.890 | +0.016 | [+0.007, +0.025] | 5/5 |
| 50 | bgeL_logreg | 0.907 | 0.828 | +0.079 | [+0.053, +0.108] | 5/5 |
| 50 | gemma_judge_0shot | 0.907 | 0.845 | +0.061 | [+0.034, +0.091] | 5/5 |
| 50 | gemma_judge_0shot_platt | 0.907 | 0.834 | +0.072 | [+0.035, +0.103] | 5/5 |
| 100 | gemma_features (best) | 0.909 | 0.892 | +0.017 | [+0.012, +0.023] | 5/5 |
| 100 | bgeL_logreg | 0.909 | 0.852 | +0.057 | [+0.031, +0.088] | 5/5 |
| 100 | gemma_judge_0shot | 0.909 | 0.845 | +0.064 | [+0.037, +0.093] | 5/5 |
| 100 | gemma_judge_0shot_platt | 0.909 | 0.845 | +0.064 | [+0.037, +0.093] | 5/5 |
| all | gemma_features (best) | 0.916 | 0.896 | +0.020 | [+0.012, +0.028] | 5/5 |
| all | bgeL_logreg | 0.916 | 0.903 | +0.013 | [-0.011, +0.035] | 5/5 |
| all | gemma_judge_0shot | 0.916 | 0.845 | +0.071 | [+0.044, +0.100] | 5/5 |
| all | gemma_judge_0shot_platt | 0.916 | 0.845 | +0.071 | [+0.044, +0.100] | 5/5 |
