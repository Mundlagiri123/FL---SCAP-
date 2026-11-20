@echo off
REM Quick check (2-4 min): re-runs 5 controllers on one test trace in iFogSim2 and compares with the logged results
python run_demo.py %*
pause
