---
title: "Timeseries Analysis - Cross Validation"
unit_id: 108
course_id: 4
level: "Expert"
slug: timeseries-analysis-cross-validation
is_course: 0
---

# Timeseries Analysis - Cross Validation

This module covers cross-validation techniques for optimizing time series forecasting models while preserving temporal dependencies. It addresses the challenge of generating multiple training and validation sets from time series data without disrupting time ordering, using Holt-Winters Exponential Model (HWEM) for streamflow prediction.

**Source materials:** PDF document `Cross_Validation.pdf` and flowchart `flow chart3.pptx` prepared by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade (vmerwade@purdue.edu) from Lyles School of Civil Engineering, Purdue University. Jupyter Notebook exercise `cross_validation_exercise.ipynb` (GitHub: https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP5/Coursepage_DP5_cross_validation_exercise.ipynb) adapted from Sergeev (2018). References include Hyndman and Athanasopoulos (2018) "Forecasting: principles and practice."

**Environment:** Web browser with mygeohub.org account; Jupyter Notebook platform.

**Cross-validation methodology:** Unlike traditional random resampling that disrupts time ordering, cross-validation preserves time structure by splitting dataset into multiple folds along the time axis. Each fold step generates one training and one validation set. Following diagram conventions from Hyndman and Athanasopoulos (2018), blue dots represent training data and red dots represent validation data, with n days per unit. Initial step uses training set of length 6*n days with validation set of n days. Subsequent steps expand training set incrementally (7*n, 8*n, etc.) while validation set slides forward n days along time axis. Process continues until final observations are reached. Errors from all folds are averaged into final validation score.

**Setup and splitting:** Obtain daily streamflow data for USGS station 03335500 (Wabash River at Lafayette) from 01/01/2019 to 06/30/2019 using hydrofunctions library; plot hydrograph. Use sklearn.model_selection.TimeSeriesSplit to split dataset into n_splits folds with prediction horizon of 5 days. Set initial training set to 122 days (6 folds of 5-day prediction horizon). Configure TimeSeriesSplit(n_splits) to generate training-validation pairs while maintaining temporal order.

**HoltWinters class:** Implements triple exponential smoothing with __init__ constructor accepting series, seasonal length (slen), parameters (alpha, beta, gamma), and prediction horizon (n_preds). Methods include initial_trend() computing average trend across season, initial_seasonal_components() calculating season averages and seasonal variations, and triple_exponential_smoothing() performing forward smoothing with component initialization at step 0, then iterative updates for each observation and subsequent predictions.

**Cross-validation error function:** Timeseries_CVscore() returns average MSE across all folds. Iterates through train-test pairs from TimeSeriesSplit, trains HoltWinters model on each training fold, forecasts validation fold, computes MSE loss using sklearn.metrics.mean_squared_error, and returns mean of error array.

**Optimization:** scipy.optimize.minimize() with Truncated Newton conjugate gradient (TNC) algorithm minimizes Timeseries_CVscore across parameters constrained to [0,1] range. Initial parameter guess: alpha=0.7, beta=0.1, gamma=0.3. Optimal parameters extracted from optimization result. Test MSE evaluated on holdout test set separate from cross-validation training-validation splits.

**Deliverables:** Plot predictions against observations over time. Compare results with traditional optimization method (Unit 107). For station 08158000 using six months of 2018 data: optimize both HWEM and first-order exponential smoothing via cross-validation, report final parameters and MSE values, forecast next month, plot predicted hydrograph, compare outcomes between cross-validation and non-cross-validation approaches.

## Summarized attachments
- **Cross Validation** (Cross_Validation.pdf, file): Tutorial by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade on cross-validation for optimizing Holt-Winters Exponential Model (HWEM) for streamflow forecasting while preserving time dependencies, covering time series cross-validation methodology following Hyndman and Athanasopoulos convention, TimeSeriesSplit implementation in sklearn with expanding training windows and sliding validation folds, Timeseries_CVscore function computing average mean squared error across all folds, scipy.optimize.minimize with TNC algorithm for parameter optimization in [0,1] range, HWEM parameter optimization (alpha, beta, gamma), test set evaluation, and comparison with traditional (non-cross-validated) optimization methods.
