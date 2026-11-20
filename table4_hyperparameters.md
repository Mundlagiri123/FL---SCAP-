### Table 4 - RL, FL-SCAP and baseline hyperparameters

| Component | Setting |
|---|---|
| Double DQN (DQN, COS-DQN, OA-DQN, FL-SCAP core) | MLP 128-128, Adam 5e-4, gamma 0.9, replay 20k, batch 64, Huber, target sync 250, warm-up 300, eps 1->0.05 over 60% of episodes |
| PPO | actor/critic MLP 128-128, lr 3e-4 (critic 9e-4), gamma 0.9, GAE 0.95, clip 0.2, entropy 0.01, 4 epochs, minibatch 40, update every 4 episodes |
| Predictor | GRU hidden 48 over k=4 rounds, action embedding 8 + 19 action descriptors, 5 bootstrap heads (MLP 64), Adam 1e-3, online 1 minibatch/step, active after 400 samples |
| Uncertainty | std_heads(RCT)/7.5 + 0.5 std_heads(P_SLA) + 0.3/sqrt(1+n(kind,service)) |
| Stress encoder | rule-based, window k=3, 6 components (comm, resource, straggler, participation, drift, mixed) |
| Decision weights (training) | lambda_p = 1.0, lambda_u = 0.5 |
| Decision weights (test, validation-selected) | lambda_p = 0.0, lambda_u = 0.5 |
| Safeguards | migration cooldown 3 rounds, <= 1 scale action / 2 rounds, min benefit delta = 0.05 |
| GA | pop 30, 25 generations, tournament, uniform crossover, mutation 0.15, elitism 2 |
| PSO | 20 particles, 25 iterations, w 0.7, c1 = c2 = 1.5 |
| Greedy | relieve fogs above 0.75 utilisation |
