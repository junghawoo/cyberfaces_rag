---
title: "Time Series forecasting 101"
unit_id: 250
course_id: 0
level: "Expert"
slug: time-series-forecasting-101-
is_course: 0
objectives:
  - "Learning this module enables users to preprocess raw data and do the time series forecasting"
---

# Time Series forecasting 101

Machine learning approach to analyze and forecast time series data in high-performance computing environments. Explores both machine learning and deep learning techniques. Prerequisites: familiarity with machine learning, deep learning, python programming.

Time series definition: series of data points indexed in time order; typically equally spaced points in time. Examples: monthly sales, hourly stock prices, quarterly unemployment rates, annual GDP, daily airline filled seats.

Dataset example: number of miles traveled by air, rail, road since January 1990 (monthly data type).

Preprocessing: time series data must have index with equal increments; must be datetime type in Python; pandas.date_range function for redefining time series indexes.

Time series components: Level (mean of points), Trend, Seasonality, Residual error.

Forecasting methods:

Simple Linear Regression: Y(t) = β₀ + β₁*t; target y(t), predictor indexed t(1,2,3...t); does not capture seasonality.

Multiple Linear Regression: includes seasonal dummies (0/1 binary for seasons 2-12); includes exogenous variables (independent predictors e.g., t-1 observations).

ACF/PACF analysis: Lag = n times removed (e.g., lag 1 is y(t-1)); ACF (autocorrelation function) = correlation between lags; PACF (partial autocorrelation) = "true correlation" removing relationships with other lags.

Stationarity: time series with constant mean, variance, autocorrelation; ADF (Augmented Dickey-Fuller) test for statistical significance (p-value hypothesis testing).

Auto-Regressive (AR) Model: regression with significant lags as predictors; conditions: stationary series, significant lag variables identified via PACF.

ARIMA (AutoRegressive Integrated Moving Average): combination of AR and MA (moving average) models; hyperparameters (p,d,q) where p=significant AR lags (PACF), d=differencing order, q=significant MA lags (ACF).

SARIMA (Seasonal ARIMA): adds seasonal component (P,D,Q,S) to capture seasonality; Y(t) = ay(t-1)+by(t-2)+...+s1*y(t-12)+error.

Smoothing Methods: Simple Exponential Smoothing (weighted average, recent obs highest weights, alpha learning rate); Double Exponential Smoothing (accounts for trend, flat forecast issue resolved); Triple/Holt-Winter's Smoothing (level, trend, seasonality); Additive vs Multiplicative (additive=linear, multiplicative=percentage changes).

Resources: Jupyter Notebook (GitHub: https://github.com/junghawoo/TimeSeriesForecasting101.git); Lecture Recording; Time Series Forecasting 101 Presentation Slides; Time Series Forecasting 201 Presentation Slides; Exercise Files (RCAC/Purdue: https://www.rcac.purdue.edu/training/time-series-forecasting-101); Anvil HPC environment.

Next topics: AutoARIMA, Complex time-series data, Deep Learning models for time-series.

## Summarized attachments
- **Time_Series_101** (Time_Series_101.pdf, file): PDF tutorial on time series forecasting fundamentals covering time series definition, preprocessing with pandas.date_range, time series components (level, trend, seasonality, residual), and forecasting methods including simple linear regression, multiple linear regression with seasonal dummies, ACF/PACF analysis, stationarity testing, autoregressive models, ARIMA/SARIMA, and smoothing methods (simple, double, and triple exponential smoothing).
- **Jupyter Notebook for Time Series forecasting** (github.com/junghawoo/TimeSeriesForecasting101, notebook): Jupyter Notebook implementation of time series forecasting techniques with code examples. No machine-readable content extracted from GitHub repository.
- **Lecture Video for Time Series forecasting 101** (cdnapisec.kaltura.com, link): Video lecture on time series forecasting 101 techniques. No content extracted.
- **More resources on Time series forecasting** (rcac.purdue.edu/training/time-series-forecasting-101, link): RCAC (Rosen Center for Advanced Computing) training page on Time Series Forecasting 101. Provides course schedule, prerequisites (familiarity with machine learning, deep learning, Python), lecture recordings, and materials including Time Series Forecasting 101 and 201 presentation slides, and exercise files (32.22 MB).
