### Table 2 - Objective-1 reproduction (Static placement, 10 rounds, full FedAvg)

| Metric                                         | Objective1_reported   | Reproduced   |   Relative_error_pct | Note                                                  |
|:-----------------------------------------------|:----------------------|:-------------|---------------------:|:------------------------------------------------------|
| Baseline mean RCT (s)                          | 4.81                  | 3.745        |                -22.1 | sd over 3 trace seeds = 0.037                         |
| High-latency mean RCT (s)                      | 7.46                  | 5.163        |                -30.8 | sd over 3 trace seeds = 0.086                         |
| Low-fog-capacity mean RCT (s)                  | 6.66                  | 4.268        |                -35.9 | sd over 3 trace seeds = 0.053                         |
| Straggler ratio range                          | (0.08, 0.38)          | (0.00, 0.36) |                nan   | min/max over all rounds                               |
| Training stability range                       | (0.63, 0.92)          | (0.70, 0.99) |                nan   | rounds >= 3 (TSI needs 3-round window)                |
| Baseline COS                                   | 0.28                  | 0.2          |                -28.6 | stress score; Obj-1 weights unpublished -> trend only |
| High-latency COS                               | 0.63                  | 0.212        |                -66.3 | stress score; Obj-1 weights unpublished -> trend only |
| Low-fog-capacity COS                           | 0.57                  | 0.255        |                -55.3 | stress score; Obj-1 weights unpublished -> trend only |
| Combined-stress COS                            | 0.79                  | 0.273        |                -65.4 | stress score; Obj-1 weights unpublished -> trend only |
| R-base: RCT by Obj-1 formula max(t+u+d) (s)    | n/a                   | 3.573        |                nan   | excludes fog aggregation/queueing                     |
| R-highlat: RCT by Obj-1 formula max(t+u+d) (s) | n/a                   | 4.992        |                nan   | excludes fog aggregation/queueing                     |
| R-lowcap: RCT by Obj-1 formula max(t+u+d) (s)  | n/a                   | 3.665        |                nan   | excludes fog aggregation/queueing                     |
| Final accuracy, baseline (10 rounds)           | n/a                   | 0.8164       |                nan   |                                                       |
