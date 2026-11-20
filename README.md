# FL-SCAP reproducible figure package

Source: 5_Results_and_Graphs.zip supplied with the user's PhD project. The CSV files are **reported outputs**, not independently reproduced simulations.

## Rebuild

Install `numpy`, `pandas`, `matplotlib`, then run:

`python generate_figures.py`

This produces high-resolution PNG and vector SVG figures under `figures/`.

Figures 1 and 2 are Python-drawn schematic interpretations of the documented architecture, not screenshots or measured iFogSim2 output. Figures 3 to 12 are computed solely from the included supplied CSVs. The script excludes OA-DQN from all comparison figures as requested.

The reported numbers are preserved; no new iFogSim2 or FedAvg experiments are executed by this script. Errors are reported seed-level SD, not confidence intervals; statistical significance must be assessed separately. Some baseline algorithms optimize different decision objectives and their comparisons should be interpreted carefully. Not all figure results favor FL-SCAP.
