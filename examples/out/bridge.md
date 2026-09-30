# Escalation report: examples/out/bridge_input.csv

121 items. Default right 0.653 at 0.5 per item; fallback right 0.893 at 4.

| both right | only default right (escalating breaks) | only fallback right (escalating repairs) | both wrong | escalation value |
|---|---|---|---|---|
| 69 | 10 | 39 | 3 | +0.240 |

| rate | score | accuracy | cost | repaired | broken | net | 95% CI |
|---|---|---|---|---|---|---|---|
| 10% | random | 0.669 | 0.8471 | 4 | 2 | +0.0165 | [-0.0248, +0.0579] |
| 10% | oracle | 0.752 | 0.8471 | 12 | 0 | +0.0992 | [+0.0496, +0.1570] |
| 10% | risk | 0.686 | 0.8471 | 4 | 0 | +0.0331 | [+0.0083, +0.0661] |
| 20% | random | 0.702 | 1.194 | 8 | 2 | +0.0496 | [+0.0000, +0.1074] |
| 20% | oracle | 0.851 | 1.194 | 24 | 0 | +0.1983 | [+0.1240, +0.2727] |
| 20% | risk | 0.744 | 1.194 | 11 | 0 | +0.0909 | [+0.0413, +0.1405] |
| 30% | random | 0.727 | 1.541 | 11 | 2 | +0.0744 | [+0.0165, +0.1322] |
| 30% | oracle | 0.950 | 1.541 | 36 | 0 | +0.2975 | [+0.2149, +0.3802] |
| 30% | risk | 0.752 | 1.541 | 14 | 2 | +0.0992 | [+0.0413, +0.1653] |
| 50% | random | 0.785 | 2.236 | 20 | 4 | +0.1322 | [+0.0579, +0.2066] |
| 50% | oracle | 0.975 | 2.236 | 39 | 0 | +0.3223 | [+0.2397, +0.4050] |
| 50% | risk | 0.843 | 2.236 | 26 | 3 | +0.1901 | [+0.1074, +0.2727] |

Net = (repaired − broken) / items. The oracle is an upper bound, not a policy. A score earns its place only by beating random and the best fixed action at equal cost on new items.
