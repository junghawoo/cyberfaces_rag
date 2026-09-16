---
title: "Geospatial analysis"
unit_id: 170
course_id: 6
level: "Foundation"
slug: geospatial-analysis
is_course: 0
---

# Geospatial analysis

Reservoir simulation assignment (Homework 7) for ENVR 890-001: Python for Environmental Research, Fall 2020 (Purdue University). By Andrew Hamilton with material adapted from Greg Characklis, David Gorelick, H.B. Zeff.

Jupyter Notebook: https://github.com/PurdueCyberTraining/python4env/blob/main/Lec7-HW7/HW7_ReservoirSimulation.ipynb (Due November 23, 2020).

Objective: Build on reservoir simulation example from Lectures 9 & 10; perform Monte Carlo analysis using time series techniques to test different operating rules.

Dataset: Synthetic streamflow dataset with 10,000 synthetic time series; 20 years each (240 months). Python libraries: numpy, pandas, matplotlib, seaborn.

Parameters: storage_max = 4.5M AF (acre-feet), storage_0 = 3M AF (initial), demand = 50,000 AF/month, 4 variables tracked (inflow, demand, release, storage).

Part 1 - Baseline operations: Simulate reservoir operations under 10,000 inflow scenarios using get_release_storage function; store results in 10000x240x4 array; calculate metrics: supply reliability (fraction months releases=demands), flood risk (99.9th percentile releases), end storage (average last 12 months as fraction of max).

Part 2 - Flood control operations: Alternative rules preemptively release water when reservoir nears full. Rule 1: storage_flood=3M AF threshold, fraction_flood=0.1 (fraction above threshold to release); if storage>storage_flood, flood_release=(storage-storage_flood)*fraction_flood. Rule 2: Seasonal drawdown using monthly_mean, monthly_std of synthetic inflows; storage_flood_monthly varies by month (3.75M AF peak months, 3M AF low months); allows preemptive releases before winter/spring floods.

Part 3 - Demand scenarios: Generate 10,000 random demand growth rates between -0.2% and +0.2% per month (0.998 to 1.002 multiplier using numpy.random.uniform); rerun Monte Carlo with both inflow and demand uncertainties matched (scenario 1 inflow with scenario 1 demand growth, etc.); compare performance metrics across operational scenarios.

Analysis outputs: 3 figures per scenario (inflow, release, storage) showing first 10 simulations over 240 months; comparison of supply reliability, flood risk, end storage metrics across baseline and flood control rules.

## Summarized attachments
- **Homework 7: Reservoir Simulation** (github.com/PurdueCyberTraining/python4env, notebook): Jupyter Notebook for ENVR 890-001: Python for Environmental Research (Fall 2020, Purdue University) by Andrew Hamilton. Monte Carlo reservoir simulation with 10,000 synthetic 20-year streamflow time series (240 months each). Compares baseline operations with flood control rules using metrics: supply reliability (demand satisfaction fraction), flood risk (99.9th percentile releases), end storage. Includes seasonal demand growth scenarios (-0.2% to +0.2% monthly growth rates) and code examples using numpy, pandas, matplotlib, and seaborn for simulating and visualizing water resource management outcomes.
