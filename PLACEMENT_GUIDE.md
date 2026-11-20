# Figures, captions, text citations and placement

All graphics are author-generated: no third-party visual is reproduced. Figures 1–2 are explanatory schematics and should be cited as original author diagrams; Figures 3–12 reproduce numbers from the reported experiment CSVs, not a fresh iFogSim2 run. No additional external bibliographic citations are required for authors’ original experimental plots. Cite Fig. X within the manuscript.

## Fig. 1 — Proposed federated fog-IoT system architecture

**Insert:** After opening text in 3.1 System Architecture.

**In-text citation:** Figure 1 illustrates the FL clients, fog microservices, global coordinator and the telemetry feedback loop used for orchestration.

**Caption source:** Author-drawn Python schematic based on the system design described in Section 3.1.

**PNG:** `01_system_architecture_schematic.png`

## Fig. 2 — Processing pipeline of the proposed FL-SCAP controller

**Insert:** After opening text in 3.5 Proposed FL-SCAP Algorithm.

**In-text citation:** The complete sequence of observation, stress estimation, prediction, uncertainty assessment and masked action selection is summarized in Fig. 2.

**Caption source:** Author-drawn Python schematic based on the implemented algorithm described in Section 3.5.

**PNG:** `02_flscap_decision_pipeline.png`

## Fig. 3 — Mean round completion time under seven evaluation scenarios

**Insert:** Immediately before 4.3 Federated Learning Performance Comparison.

**In-text citation:** Figure 3 compares the algorithms across the seven supplied stress scenarios, showing that the ranking changes with operating conditions.

**Caption source:** Authors’ Python plot of the reported experiment outputs (per-scenario CSV); RCT in seconds.

**PNG:** `08_scenario_RCT_heatmap.png`

## Fig. 4 — Mean round completion time of FL-SCAP and comparison algorithms

**Insert:** Immediately before 4.4 Fog Infrastructure Performance.

**In-text citation:** Figure 4 visualizes the mean RCT values from Table IV and their reported seed-level standard deviations.

**Caption source:** Authors’ Python plot based on the reported data in Table IV; error bars represent seed-level SD.

**PNG:** `03_mean_round_completion_time.png`

## Fig. 5 — Straggler ratio across orchestration algorithms

**Insert:** Immediately before 4.4 Fog Infrastructure Performance.

**In-text citation:** Figure 5 illustrates the straggler-ratio comparison from Table IV, including the lowest reported mean for FL-SCAP.

**Caption source:** Authors’ Python plot based on reported Table IV metrics; error bars where supplied.

**PNG:** `04_straggler_ratio.png`

## Fig. 6 — Peak fog CPU utilization across algorithms

**Insert:** Immediately before 4.5 Orchestration Overhead.

**In-text citation:** Figure 6 compares peak CPU utilization, highlighting the relatively high peak load recorded by FL-SCAP.

**Caption source:** Authors’ Python plot based on reported Table V metrics.

**PNG:** `05_peak_cpu.png`

## Fig. 7 — Unnecessary orchestration actions per evaluation episode

**Insert:** Immediately before 4.6 Prediction Model Evaluation.

**In-text citation:** Figure 7 shows the fewer unnecessary actions recorded by FL-SCAP compared with DQN, PPO and COS-DQN.

**Caption source:** Authors’ Python plot based on reported Table VI metrics.

**PNG:** `06_unnecessary_actions.png`

## Fig. 8 — Migration-cost comparison among placement algorithms

**Insert:** Immediately before 4.6 Prediction Model Evaluation.

**In-text citation:** Figure 8 presents migration costs and reveals the greater migration overhead incurred by FL-SCAP.

**Caption source:** Authors’ Python plot based on reported Table VI metrics; cost units follow the simulation report.

**PNG:** `07_migration_cost.png`

## Fig. 9 — Migration cost and SLA violation trade-off

**Insert:** Immediately before 4.6 Prediction Model Evaluation.

**In-text citation:** Figure 9 jointly illustrates the reported migration-cost and SLA-violation values, revealing differences between action overhead and timing compliance.

**Caption source:** Authors’ Python plot of reported orchestration and SLA measurements; descriptive association only.

**PNG:** `12_migration_SLA_tradeoff.png`

## Fig. 10 — Prediction errors for next-round completion time

**Insert:** Immediately before 4.7 Ablation Experiments.

**In-text citation:** Figure 10 compares RCT forecasting errors and shows that ridge regression outperformed the GRU predictors on RCT MAE and RMSE.

**Caption source:** Authors’ Python plot based on the held-out prediction results in Table VII.

**PNG:** `09_predictor_errors.png`

## Fig. 11 — Ablation of stress, uncertainty and stability components

**Insert:** Immediately before 4.8 Statistical Analysis.

**In-text citation:** Figure 11 compares the reported mean RCT across FL-SCAP ablation variants; the uncertainty-free variant has the largest RCT.

**Caption source:** Authors’ Python plot based on the reported values in Table VIII.

**PNG:** `10_flscap_ablation.png`

## Fig. 12 — Round completion time under increasing system sizes

**Insert:** Immediately before 5. DISCUSSION.

**In-text citation:** Figure 12 compares mean RCT across increasing client/fog-node configurations. FL-SCAP remains below DQN but above GA at all tested scales.

**Caption source:** Authors’ Python plot based on the scalability results in Table IX.

**PNG:** `11_scalability_RCT.png`

