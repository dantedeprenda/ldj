# E-bridge on T0 at equal cost vs always-mid (exploratory)

Always-X on test: deepseek-v3.1-terminus acc 0.742 at $0.00112; deepseek-r1-0528 acc 0.785 at $0.01449; gpt-5 acc 0.807 at $0.02508

Accuracy of each policy at always-mid's cost, minus always-mid's accuracy (positive = beats the best fixed model at equal cost).

| policy | k | difference | 95% CI |
|---|---|---|---|
| oracle (cheap -> strong) | - | +0.0663 | [+0.0482, +0.0825] |
| random (cheap -> strong) | - | -0.0008 | [-0.0162, +0.0136] |
| jev_features: difficulty -> strong | 25 | -0.0077 | [-0.0263, +0.0111] |
| jev_features: benefit -> strong | 25 | -0.0005 | [-0.0176, +0.0148] |
| jev_features: difficulty -> strong | all | -0.0101 | [-0.0311, +0.0105] |
| jev_features: benefit -> strong | all | +0.0080 | [-0.0109, +0.0233] |
| tfidf_logreg: difficulty -> strong | 25 | -0.0043 | [-0.0192, +0.0099] |
| tfidf_logreg: benefit -> strong | 25 | -0.0003 | [-0.0161, +0.0143] |
| tfidf_logreg: difficulty -> strong | all | -0.0083 | [-0.0294, +0.0125] |
| tfidf_logreg: benefit -> strong | all | +0.0128 | [-0.0038, +0.0316] |
| bgeL_logreg: difficulty -> strong | 25 | -0.0098 | [-0.0243, +0.0068] |
| bgeL_logreg: benefit -> strong | 25 | -0.0099 | [-0.0230, +0.0060] |
| bgeL_logreg: difficulty -> strong | all | -0.0113 | [-0.0333, +0.0064] |
| bgeL_logreg: benefit -> strong | all | +0.0166 | [-0.0015, +0.0336] |
| bge_logreg: difficulty -> strong | 25 | -0.0076 | [-0.0235, +0.0080] |
| bge_logreg: benefit -> strong | 25 | +0.0009 | [-0.0137, +0.0164] |
| bge_logreg: difficulty -> strong | all | -0.0090 | [-0.0295, +0.0085] |
| bge_logreg: benefit -> strong | all | +0.0196 | [+0.0021, +0.0382] |
