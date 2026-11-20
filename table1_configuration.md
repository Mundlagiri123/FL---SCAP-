### Table 1 - Experimental configuration

| Parameter | Value |
|---|---|
| Simulator | iFogSim2 (CloudSim 7) + FLFogDevice routing/readiness extension; 1 JVM per worker |
| FL | Synchronous FedAvg, NumPy (TensorFlow not installable here); MNIST 60k/10k |
| Data partition | Non-IID shards: 40 shards x 1500, 2 per client (seed 42) |
| Model / optimiser | 784-128-10 MLP, Adam lr 1e-3, batch 32, 2 local epochs |
| Topology | 1 coordinator, 4 fog nodes, 20 clients (5 per fog); scalability 50/8, 100/12 |
| Client compute / RAM | 600-1500 MIPS, 1024 MB |
| Fog compute / RAM | 8000 MIPS, 8192 MB |
| Links | client 10/20 Mbps up/down, fog-coordinator 100 Mbps; throughput capped by 64 KB TCP window / RTT |
| Latency | client-fog 10-30 ms (high-latency 80-150 ms); fog-coordinator 5-10 ms |
| Participation | 14-19 of 20 clients per round (S5: 8-19) |
| Local training workload | 0.3 MI per sample-epoch (3000 samples x 2 epochs) |
| Model update size | 407080 bytes (101,770 float32 parameters) |
| Round timeout / SLA | 12.0 s / 7.5 s |
| Episode | 20 FL rounds (one full FL training run); one action per round |
| Initial placement (all methods) | {'M1': [0], 'M2': [1], 'M3': [2], 'M4': [0]} |
| Training | 150 episodes x 5 seeds per learner (scenario sampled from S1-S7); proxy FL during training |
| Validation | lambda grid on validation trace seeds (S2,S3,S4,S6,S7), proxy FL |
| Test | S1-S7 x 5 seeds on unseen trace seeds, full FL, paired across all 13 methods |

| Service | CPU reserve (MIPS) | RAM (MB) | BW (Mbps) | max replicas | state (MB) | startup (ms) |
|---|---|---|---|---|---|---|
| M1 | 2000 | 2048 | 20 | 2 | 8 | 800 |
| M2 | 500 | 512 | 4 | 4 | 2 | 200 |
| M3 | 1500 | 1536 | 4 | 2 | 6 | 500 |
| M4 | 1000 | 1024 | 20 | 4 | 4 | 400 |

Per-tuple work (MI): {'cpu_agg': 400, 'cpu_tel': 50, 'cpu_ana': 600, 'cpu_dist': 150, 'cpu_load': 50}
