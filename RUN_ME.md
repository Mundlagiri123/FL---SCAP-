# How to run FL-SCAP (iFogSim2) — executable package

Everything needed is in this folder: source code, the compiled iFogSim2 simulator and its extension (`java/lib/ifogsim2.jar`, `java/lib/flscap-sim.jar`), the dataset (`data/mnist.npz`), the 63 trained models used in the paper (`results/models/`), and all logged results.

## 1. Install (once)

1. Java JDK 17 or newer — check with `java -version`.
2. Python 3.10 or newer — check with `python --version` (Windows) or `python3 --version` (Linux/macOS).
3. Python libraries:

```
pip install numpy scipy pandas matplotlib tabulate
```

No compilation is needed: the Java part is already compiled into `java/lib/flscap-sim.jar`.

## 2. Quick check (2–4 minutes)

Windows: double-click `run_demo.bat`  ·  Linux/macOS: `./run_demo.sh`

It re-runs Static, Greedy, GA, OA-DQN and FL-SCAP with the trained models on one unseen test trace (scenario S6, seed 0) in iFogSim2 with full FedAvg, and checks every round against the logged results. Expected output ends with:

```
algorithm  mean_RCT_s  SLA_rate  final_accuracy  actions matches_logged_result
   Static       6.133      0.00          0.8078        0                   yes
   Greedy       6.366      0.05          0.8078        3                   yes
       GA       6.345      0.05          0.8078        2                   yes
   OA-DQN       7.156      0.20          0.8078       20                   yes
  FL-SCAP       6.460      0.05          0.8078        2                   yes
```

Any other scenario and seed: `python run_demo.py S7 2` (scenarios S1–S7, seeds 0–4).

## 3. What each executable does

| Command | What it does | Time |
|---|---|---|
| `run_demo.bat` / `run_demo.sh` | Quick reproduction check with the trained models | 2–4 min |
| `python flscap/runner.py eval --agent Static Greedy GA PSO DQN PPO COS-DQN OA-DQN FL-SCAP --seeds 0 1 2 3 4 --scenarios S1 S2 S3 S4 S5 S6 S7 --out results/my_eval.csv` | Full test evaluation of all algorithms with the trained models | ~1 h |
| `python flscap/runner.py train --agent FL-SCAP --seeds 0 --episodes 150` | Train one controller (any of the 13 names) for one seed | ~4 min |
| `python scripts/analyze.py results/my_eval.csv` | Tables (results/tables) and figures (results/figures) from an evaluation file | <1 min |
| `python scripts/obj1_reproduction.py` | Objective-1 reproduction (Static, 4 conditions) | ~3 min |
| `python scripts/predictor_eval.py` | Predictor accuracy and uncertainty study | ~10 min |
| `python scripts/dynamic_adaptation.py` | S7 adaptation metrics from results/eval_main.csv | seconds |
| `python scripts/tune_lambda.py` | FL-SCAP λ validation grid | ~15 min |
| `python tests/test_nn_gradcheck.py` | Checks the GRU/MLP gradients | seconds |
| `run_full_experiment.bat` / `.sh` | Everything from scratch: retrains all 63 models and regenerates every table and figure | ~4 h |

Algorithm names accepted by `--agent`: Static, Greedy, GA, PSO, DQN, PPO, COS-DQN, OA-DQN, OA-DQN+Pred, FL-SCAP, FL-SCAP-noStress, FL-SCAP-noUnc, FL-SCAP-noSafe.

## 4. Notes

- The supplied models are evaluation copies: replay buffers and optimiser state were removed to cut the size from 2.5 GB to 84 MB. They give identical decisions; to continue training, retrain with `runner.py train` (this overwrites the model file).
- Training a model writes `results/models/<name>_s<seed>.pkl`; back up the folder first if you want to keep the paper's models.
- Rebuild the Java part only if you change it: `cd java` then `javac -d classes -cp "lib/*" src/org/flscap/*.java` (use `"lib/*"` on Windows too) and `jar cf lib/flscap-sim.jar -C classes .`
