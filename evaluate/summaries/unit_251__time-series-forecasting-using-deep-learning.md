---
title: "Time Series Forecasting using Deep Learning"
unit_id: 251
course_id: 0
level: "Expert"
slug: time-series-forecasting-using-deep-learning
is_course: 0
objectives:
  - "Learning this module enables users to preprocess raw data and do the time series forecasting with Deep Learning libraries"
---

# Time Series Forecasting using Deep Learning

Advanced time series forecasting using deep learning techniques in HPC environments. Follow-up to Time Series Forecasting 101 (linear regression, AR/ARIMA/SARIMA, smoothing methods). Prerequisites: familiarity with machine learning, deep learning, Python programming.

Dataset example: Walmart store sales across states, categories, departments, items over 6 years; 48,000 time series aggregated by food-wise (not item-wise due to noise/inconsistent patterns).

AutoARIMA: Automated ARIMA with computer-selected (p,d,q) and (P,D,Q) parameters; helpful with multiple significant lags; Test MAPE ~30.37% (mediocre but captures seasonality).

Deep Learning models:

Artificial (Deep) Neural Network (ANN/DNN): Complicated function fitter; multiple linear functions combined, passed through non-linear activation functions. Hyperparameters: number of hidden layers, neurons per layer, activation function. Approach: feed y(t-1)...y(t-n) lags, select optimal n, use exogenous features (day, month).

Recurrent Neural Networks (RNN): Modified ANN architecture with "memory" of previous iterations; time-steps hyperparameter; applications: video, speech, time-series.

Long Short-Term Memory (LSTM): Improved RNN addressing vanishing/exploding gradients. Forget gate (determines prior relevant info), Input gate (adds current relevant info), Output gate (finalizes hidden state). Decides "how much" network remembers at each step.

Univariate LSTM: Feed only y(t-1)...y(t-n) without exogenous variables. Architectures: (1) y(t-1) to y(t-5) with 50 LSTM units; (2) y(t-1) to y(t-30) with 50 LSTM units.

Multivariate LSTM: Include exogenous variables (day-of-week, holidays). Intuition: If yesterday was Christmas and Christmas sales continue, model should account for multi-day effects, not just immediate past.

Model comparison:
- ANN: Non-linear ARIMA version; direct input-output relationships
- RNN: Permanent memory; entire information passed to next unit
- LSTM: Selective memory; gates determine what passes to next unit

Performance: Multivariate LSTM achieves best MAPE on test set (improvement over SARIMA ~30%).

Resources: Jupyter Notebook (GitHub: https://github.com/junghawoo/TimeSeriesForecastingDeepLearning101.git), Spring 2023 lecture video, RCAC training (https://www.rcac.purdue.edu/training/time-series-forecasting-101) with presentation slides and exercise files.

Related: Time Series Forecasting 101 Presentation Slides (2.18 MB), Time Series Forecasting 201 Presentation Slides (1.98 MB), Exercise Files (32.22 MB).

## Summarized attachments
- **Time_Series_201** (Time_Series_201.pdf, file): Advanced PDF tutorial on time series forecasting using deep learning. Covers AutoARIMA (automated parameter selection), Artificial Neural Networks (ANN) for non-linear trend fitting, Recurrent Neural Networks (RNN) with memory architecture, and Long Short-Term Memory (LSTM) networks addressing vanishing/exploding gradients with forget/input/output gates. Presents univariate LSTM (y(t-1)...y(t-n) only) and multivariate LSTM (with exogenous variables like day-of-week, holidays). Uses Walmart sales dataset (48,000 time series aggregated by food category) with performance comparison showing multivariate LSTM outperforming SARIMA (~30% improvement).
- **Jupyter Notebook for Time Series forecasting with Deep Learning** (github.com/junghawoo/TimeSeriesForecastingDeepLearning101, notebook): Jupyter Notebook implementation of deep learning time series forecasting with ANN, RNN, and LSTM models. No machine-readable content extracted from GitHub repository.
- **Lecture Video for Time Series forecasting with Deep Learning 101** (cdnapisec.kaltura.com, link): Spring 2023 video lecture on time series forecasting using deep learning techniques. No content extracted.
- **More resources on Time series forecasting with Deep Learning** (rcac.purdue.edu/training/time-series-forecasting-101, link): RCAC training page on Time Series Forecasting 101. Provides schedule, prerequisites (machine learning, deep learning, Python familiarity), lecture recordings, presentation slides (101 and 201 versions), and exercise files (32.22 MB) for learning deep learning approaches to time series forecasting in HPC environments.
