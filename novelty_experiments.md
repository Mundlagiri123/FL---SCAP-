### Experiments 1-4 - paired treatment vs. control

| experiment          | treatment   | baseline         | metric   |   n_pairs |   treatment_mean |   baseline_mean |   improvement_pct |   ci95_lo |   ci95_hi |   wilcoxon_p |   rank_biserial |
|:--------------------|:------------|:-----------------|:---------|----------:|-----------------:|----------------:|------------------:|----------:|----------:|-------------:|----------------:|
| Exp1 observability  | OA-DQN      | DQN              | RCT_mean |        35 |            5.545 |           5.773 |             3.962 |    -1.163 |     0.436 |     0.31     |           0.2   |
| Exp1 observability  | OA-DQN      | DQN              | sla_rate |        35 |            0.094 |           0.094 |            -0     |    -0.076 |     0.066 |     0.465    |           0.186 |
| Exp1 observability  | OA-DQN      | DQN              | reward   |        35 |          -28.313 |         -30.134 |             6.043 |    -2.3   |     7.68  |     0.79     |          -0.054 |
| Exp1 observability  | OA-DQN      | DQN              | actions  |        35 |           17.629 |          15.286 |            15.327 |     0.171 |     4.457 |     0.0501   |           0.439 |
| Exp2 prediction     | OA-DQN+Pred | OA-DQN           | RCT_mean |        35 |            5.598 |           5.545 |            -0.967 |    -0.303 |     0.425 |     0.981    |           0.006 |
| Exp2 prediction     | OA-DQN+Pred | OA-DQN           | sla_rate |        35 |            0.103 |           0.094 |            -9.091 |    -0.049 |     0.066 |     0.696    |           0.095 |
| Exp2 prediction     | OA-DQN+Pred | OA-DQN           | reward   |        35 |          -28.896 |         -28.313 |            -2.058 |    -3.012 |     1.777 |     0.471    |          -0.143 |
| Exp2 prediction     | OA-DQN+Pred | OA-DQN           | actions  |        35 |           18.714 |          17.629 |             6.159 |    -0.743 |     3     |     0.423    |           0.199 |
| Exp3 stress context | FL-SCAP     | FL-SCAP-noStress | RCT_mean |        35 |            5.456 |           5.481 |             0.458 |    -0.261 |     0.203 |     0.716    |          -0.073 |
| Exp3 stress context | FL-SCAP     | FL-SCAP-noStress | sla_rate |        35 |            0.066 |           0.063 |            -4.545 |    -0.017 |     0.023 |     0.893    |          -0.033 |
| Exp3 stress context | FL-SCAP     | FL-SCAP-noStress | reward   |        35 |          -28.072 |         -28.321 |             0.882 |    -1.223 |     1.706 |     0.656    |           0.089 |
| Exp3 stress context | FL-SCAP     | FL-SCAP-noStress | actions  |        35 |            9.771 |          10.714 |            -8.8   |    -2.086 |     0.143 |     0.173    |          -0.275 |
| Exp4 uncertainty    | FL-SCAP     | FL-SCAP-noUnc    | RCT_mean |        35 |            5.456 |           5.632 |             3.118 |    -0.554 |     0.148 |     0.852    |           0.038 |
| Exp4 uncertainty    | FL-SCAP     | FL-SCAP-noUnc    | sla_rate |        35 |            0.066 |           0.089 |            25.806 |    -0.059 |     0.011 |     0.295    |          -0.26  |
| Exp4 uncertainty    | FL-SCAP     | FL-SCAP-noUnc    | reward   |        35 |          -28.072 |         -29.127 |             3.622 |    -1.073 |     3.411 |     0.74     |          -0.067 |
| Exp4 uncertainty    | FL-SCAP     | FL-SCAP-noUnc    | actions  |        35 |            9.771 |           9.371 |             4.268 |    -1.571 |     2.286 |     0.399    |           0.17  |
| Safeguards          | FL-SCAP     | FL-SCAP-noSafe   | RCT_mean |        35 |            5.456 |           5.465 |             0.172 |    -0.294 |     0.256 |     0.565    |           0.114 |
| Safeguards          | FL-SCAP     | FL-SCAP-noSafe   | sla_rate |        35 |            0.066 |           0.081 |            19.298 |    -0.06  |     0.023 |     0.847    |          -0.048 |
| Safeguards          | FL-SCAP     | FL-SCAP-noSafe   | reward   |        35 |          -28.072 |         -28.82  |             2.596 |    -1.182 |     2.787 |     0.61     |           0.102 |
| Safeguards          | FL-SCAP     | FL-SCAP-noSafe   | actions  |        35 |            9.771 |          17.829 |           -45.192 |    -9.858 |    -6.057 |     1.69e-06 |          -0.927 |
