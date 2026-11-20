#!/usr/bin/env bash
# Full experiment from scratch (about 4 hours on 2 cores). Retrains every model (overwrites results/models).
set -e
cd "$(dirname "$0")"
python3 scripts/run_jobs.py jobs/train_main.txt 2
python3 scripts/pipeline_after_training.py
python3 scripts/obj1_reproduction.py
python3 scripts/predictor_eval.py
python3 scripts/dynamic_adaptation.py
python3 scripts/run_jobs.py jobs/train_scal.txt 2
python3 scripts/run_jobs.py jobs/eval_scal.txt 2
python3 scripts/scalability.py
python3 scripts/static_artifacts.py
python3 scripts/analyze.py
python3 scripts/build_report.py
