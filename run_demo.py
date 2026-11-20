"""Quick check that the package runs and reproduces the reported results.

Re-runs 5 controllers (Static, Greedy, GA, OA-DQN, FL-SCAP) with the supplied trained models on one
held-out test trace (scenario S6, seed 0) in iFogSim2 with full FedAvg, then compares each round's
measured RCT with the logged result in results/eval_main.csv. Takes about 2-4 minutes.

    python run_demo.py              # default S6, seed 0
    python run_demo.py S7 2         # any scenario S1-S7 and seed 0-4
"""
import os, sys, time, json
import numpy as np, pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import flscap.runner as R
from flscap.simbridge import IFogSim2
from flscap.env import FogFLEnv
from flscap.scenarios import SCENARIOS

sc = sys.argv[1] if len(sys.argv) > 1 else "S6"
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
agents = ["Static", "Greedy", "GA", "OA-DQN", "FL-SCAP"]
sel = json.load(open(os.path.join(ROOT, "results", "tables", "lambda_selected.json")))

print(f"Starting iFogSim2 ... scenario {sc}, test seed {seed}")
sim = IFogSim2()
env = FogFLEnv(sim, 20, 4, fl_mode="full", fl_cache={})
env.reset("S1", 0)
ep_seed = R.TEST_SEED_BASE + seed * 100 + SCENARIOS.index(sc)
logged = pd.read_csv(os.path.join(ROOT, "results", "eval_main.csv"))
rows = []
for name in agents:
    agent, _ = R.load_agent(name, seed, env)
    if name == "FL-SCAP":
        agent.lam_p, agent.lam_u = sel["lam_p"], sel["lam_u"]
    out = []
    t0 = time.time()
    R.run_episode(env, agent, sc, ep_seed, False, out)
    rct = np.array([o["RCT"] for o in out])
    ref = logged[(logged.agent == name) & (logged.seed == seed) & (logged.scenario == sc)].sort_values("round").RCT.values
    match = len(ref) == len(rct) and np.allclose(ref, rct, atol=1e-6)
    rows.append(dict(algorithm=name, mean_RCT_s=rct.mean().round(3), SLA_rate=np.mean(rct > 7.5).round(3),
                     final_accuracy=round(out[-1]["ACC"], 4), actions=sum(o["action"] != "noop" for o in out),
                     matches_logged_result="yes" if match else "no", seconds=round(time.time() - t0)))
    print(f"  {name:8s} mean RCT {rct.mean():.3f} s   matches logged result: {'yes' if match else 'no'}")
sim.close()
print()
print(pd.DataFrame(rows).to_string(index=False))
