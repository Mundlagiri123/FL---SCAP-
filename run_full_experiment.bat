@echo off
REM Full experiment from scratch (about 4 hours on 2 cores). Retrains every model (overwrites results\models).
python scripts\run_jobs.py jobs\train_main.txt 2 || goto :err
python scripts\pipeline_after_training.py || goto :err
python scripts\obj1_reproduction.py || goto :err
python scripts\predictor_eval.py || goto :err
python scripts\dynamic_adaptation.py || goto :err
python scripts\run_jobs.py jobs\train_scal.txt 2 || goto :err
python scripts\run_jobs.py jobs\eval_scal.txt 2 || goto :err
python scripts\scalability.py || goto :err
python scripts\static_artifacts.py || goto :err
python scripts\analyze.py || goto :err
python scripts\build_report.py || goto :err
echo Done.
pause
exit /b 0
:err
echo A step failed - see the message above.
pause
exit /b 1
