#!/usr/bin/env bash
# Quick check (2-4 min): re-runs 5 controllers on one test trace in iFogSim2 and compares with the logged results
cd "$(dirname "$0")" && python3 run_demo.py "$@"
