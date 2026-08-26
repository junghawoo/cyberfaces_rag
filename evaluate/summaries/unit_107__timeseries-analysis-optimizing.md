---
title: "Timeseries Analysis - Optimizing Model Parameters"
unit_id: 107
course_id: 4
level: "Expert"
slug: timeseries-analysis-optimizing
is_course: 0
---

# Timeseries Analysis - Optimizing Model Parameters

This module covers optimization of streamflow forecasting models using Holt-Winters exponential smoothing. It teaches parameter optimization and model evaluation techniques for time series forecasting in hydrology, addressing the real-world challenge of accurate streamflow prediction.

**Source materials:** PDF document `Optimization_of_Daily_Streamflow_Forecasting_Model.pdf` and flowchart presentation `flow chart.pptx`, prepared by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade (vmerwade@purdue.edu) from Lyles School of Civil Engineering, Purdue University. Jupyter Notebook exercise `optimization_forecasting_exercise.ipynb` (GitHub: https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP4/Coursepage_DP4_optimization_forecasting_exercise.ipynb) with code adapted from Sergeev (2018) and includes hydrofunctions library for USGS data retrieval.

**Environment:** Web browser with mygeohub.org account and internet connection; Jupyter Notebook execution platform.

**Core model:** Holt-Winters Exponential Model (HWEM), also known as triple exponential smoothing, combines three components: level (lt), trend (bt), and seasonal (st) components with corresponding parameters alpha (α), beta (β), and gamma (γ). The model prediction equation is ŷ(t+m) = lt + m*bt + st−L+1+(m−1) mod L, where L is seasonal index and m is trend index. Initial values for trend (b0) and seasonal components (s0-L to s0) are calculated from the series data.

**Data workflow:** (1) Obtain daily streamflow data for USGS station 03335500 (Wabash River at Lafayette) from 01/01/2019 to 06/30/2019 using hydrofunctions library and plot hydrograph; (2) Implement HoltWinters Python class with __init__ constructor initializing series, seasonal length (slen), parameters (alpha, beta, gamma), and prediction horizon (n_preds); (3) Compute initial_trend() averaging trend values across season; (4) Calculate initial_seasonal_components() computing season averages and seasonal variations; (5) Execute triple_exponential_smoothing() method performing forward smoothing process where first step uses observation values, subsequent steps update level, trend, and seasonality based on equations (2)-(4).

**Optimization process:** Dataset partitioned into training, validation, and test sets. Training process constructs model with training set, compares predictions against validation set, updates parameters, and repeats until error converges. Define Train_Score() function computing Mean Squared Error (MSE) loss function for model evaluation. Use scipy.optimize.minimize() with Truncated Newton conjugate gradient (TNC) algorithm to minimize MSE across parameters constrained to range [0,1]. Optimal parameters (alpha_final, beta_final, gamma_final) are extracted from optimization results (opt.x).

**Evaluation and prediction:** After optimization, report training MSE and test MSE using sklearn.metrics.mean_squared_error(). Forecast streamflow for next m days using optimized parameters; plot results showing predicted hydrograph against observed discharge values over time. Prediction uncertainty increases with each forecast step as model relies on previous predictions rather than observations.

**Assignment:** Optimize Holt-Winters model and first-order exponential smoothing model for USGS station 08158000 using six months of 2018 data. Report final parameters and errors from both training and test processes. Generate forecast for next one month with optimized parameters and plot predicted hydrograph.

## Summarized attachments
- **Flowchart** (flow chart.pptx, file): Visual flowchart presentation illustrating the streamflow forecasting model optimization process and workflow.
- **Optimization of Daily Streamflow Forecasting Model** (Optimization_of_Daily_Streamflow_Forecasting_Model.pdf, file): Comprehensive tutorial by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade on optimizing Holt-Winters exponential smoothing (triple exponential smoothing) for daily streamflow forecasting, covering HWEM equations with level, trend, and seasonal components, dataset partitioning into training/validation/test sets, Mean Squared Error (MSE) loss function computation, scipy.optimize.minimize with TNC algorithm for parameter optimization, and evaluation of forecasting accuracy for USGS streamflow stations using six months of data with visualization of predicted vs observed discharge.
