---
title: "Timeseries Analysis - Forecasting Daily Streamflow"
unit_id: 106
course_id: 4
level: "Foundation"
slug: timeseries-analysis-forecasting
is_course: 0
---

# Timeseries Analysis - Forecasting Daily Streamflow

Tutorial on daily streamflow forecasting using first order exponential smoothing method. Part of FAIR Climate and Water Science, Module 2: Data Processing (DP) for Water Science. Prepared by Pin-Ching Li, Sayan Dey, Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University, vmerwade@purdue.edu).

Objective: Develop exponential smoothing model for streamflow forecasting using historical time series. Approaches: exponential smoothing, ARIMA (Auto Regressive Integrated Moving Average), machine learning tools.

Requirements: Web browser, mygeohub.org account, Jupyter Notebook (streamflow_forecasting_exercise.ipynb provided).

Data: USGS 03335500 Wabash River at Lafayette, IN; instantaneous observation ('iv') data from January 1 to June 30, 2019; resampled to daily mean discharge. Python libraries: numpy, pandas, hydrofunctions, matplotlib, sklearn.

Workflow: Use hydrofunctions library to download data via NWIS object (gage number, observation type, dates); apply get_data() function; resample instantaneous data into daily mean streamflow series; store as dataframe; save to CSV.

First order exponential smoothing formula: ŷₜ = α*yₜ₋₁ + (1-α)*ŷₜ₋₁ (α=smoothing parameter, yₜ₋₁=observation, ŷₜ₋₁=previous forecast).

Python class implementation (OOP style): Exp_Smoothing class with __init__(series, alpha) constructor; exponential_smoothing() method calculates smoothing (i=0: initial condition equals observation; i>0: apply forecasting formula).

Prediction class: Exp_Smoothing_Prediction class extends model with n_preds parameter for forecasting beyond dataset length; generates predictions for extra days when i≥len(series).

Model evaluation: Split dataset into training and validation sets; calculate mean squared error (MSE) using sklearn.metrics.mean_squared_error(); optimize alpha parameter manually to minimize MSE; Train_Score function returns error metric.

Visualization: Plot daily streamflow time series ("2019 USGS 03335500 WABASH RIVER AT LAFAYETTE, IN"); x-axis: date (yyyy/mm), y-axis: discharge (cfs); overlay model output with observations; generate prediction plots for 10+ additional days.

Jupyter Notebook: https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP3/Coursepage_DP3_streamflow_forecasting_exercise.ipynb. Flowchart (flow chart1.pptx) shows optimization workflow steps.

Homework: Report prediction error; find optimal alpha value minimizing MSE; submit alpha and MSE values.

## Summarized attachments
- **Daily Streamflow Forecasting by First Order Exponential Smoothing Method** (Daily_Streamflow_Forecasting_by_First_Order_Exponential_Smoothing_Method.pdf, file): PDF tutorial by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade on exponential smoothing for streamflow forecasting. Covers forecasting formula ŷₜ = α*yₜ₋₁ + (1-α)*ŷₜ₋₁, OOP implementation using Exp_Smoothing class with alpha parameter optimization, model evaluation using mean squared error (MSE), and prediction generation for extended forecasting horizons.
- **Flowchart** (flow chart1.pptx, file): PowerPoint flowchart showing the streamflow forecasting model optimization workflow steps.
- **Jupyter Notebook Exercise** (github.com/PurdueCyberTraining/fairclimatewater, notebook): Jupyter Notebook for FAIR Climate and Water Science (DP3 module) demonstrating exponential smoothing implementation using hydrofunctions to download USGS streamflow data, daily resampling, model training with alpha parameter tuning, and MSE-based validation for streamflow forecasting.
