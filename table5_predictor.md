### Table 5 - Prediction accuracy on held-out trajectories (next-round outcome)

| Model                               |   RCT_MAE |   RCT_RMSE |   RCT_R2 |   FRU_MAE |   FRU_RMSE |   FRU_R2 |   SR_MAE |   SR_RMSE |   SR_R2 |   RCT_MAE_on_action_rounds |
|:------------------------------------|----------:|-----------:|---------:|----------:|-----------:|---------:|---------:|----------:|--------:|---------------------------:|
| Persistence                         |    1.6631 |     3.0751 |   0.4825 |    0.0547 |     0.0928 |   0.3181 |   0.1014 |    0.1343 | -0.6593 |                     1.938  |
| Linear (ridge)                      |    1.5264 |     2.4196 |   0.6796 |    0.0193 |     0.0247 |   0.9515 |   0.0768 |    0.0957 |  0.1569 |                     1.7951 |
| GRU (action-independent)            |    1.8652 |     2.6882 |   0.6045 |    0.0346 |     0.0456 |   0.8354 |   0.086  |    0.1076 | -0.0657 |                     2.0588 |
| GRU + action conditioning (FL-SCAP) |    1.6414 |     2.6854 |   0.6053 |    0.0365 |     0.0458 |   0.8338 |   0.0754 |    0.0955 |  0.1603 |                     1.9776 |

Uncertainty quality: {
 "spearman_unc_vs_abs_err": 0.5114216153203842,
 "p_value": 1.1987609683715487e-38,
 "mae_by_uncertainty_tercile": [
  0.652250407059112,
  1.3832545560973497,
  2.8871762140427304
 ],
 "n_test": 560,
 "n_train": 1400,
 "rare_action_rounds": 1,
 "mae_rare": 1.860475040890213,
 "mae_common": 1.6409618077625425,
 "unc_rare": 0.44660801429352437,
 "unc_common": 0.07284202355118803
}
