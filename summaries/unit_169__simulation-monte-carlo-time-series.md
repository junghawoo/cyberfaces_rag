---
title: "Simulation, Monte Carlo, & time series"
unit_id: 169
course_id: 6
level: "Foundation"
slug: simulation-monte-carlo-time-series
is_course: 0
---

# Simulation, Monte Carlo, & time series

Two-lecture module covering Monte Carlo uncertainty quantification and synthetic time series generation for hydrological modeling. Instructor: Andrew Hamilton (Purdue); adapted material from Greg Characklis, David Gorelick, H.B. Zeff. Course: ENVR 890-001: Python for Environmental Research (Fall 2020).

## Lecture 9: Reservoir Simulation & Monte Carlo Methods (Oct 23, 2020)

Notebook: Lec9_ResevoirMonteCarlo.ipynb (PurdueCyberTraining/python4env GitHub)

Covers Monte Carlo (MC) methods for propagating uncertainty through computational models. Introduces MC sampling with PM10 air quality concentrations (normal distribution, μ=90 μg/m3, σ=20 μg/m3) to estimate violation probability and percentiles. Implements MC sampling using numpy.random.normal to generate 1,000,000 samples and compute statistics (mean, std, skew, kurtosis). Calculates probability of violating 150 μg/m3 standard and 95th percentile.

Applies MC to nonlinear health impact model: cardiovascular deaths = 15 / (1 + exp(-(PM10 - 80) / 35)). Propagates PM10 uncertainty through the function to obtain distribution of expected deaths and probability exceedances.

Reservoir model: Water balance equation (inflow + precipitation) - (release + evaporation) = change in storage. Implements deterministic model with constraints: negative storage handled via deficit release; maximum storage (2 MAF) via spillage. Exercises progressively build skills: (1) function for release/storage given inflow/demand, (2) while loop to find failure years under constant inflow scenarios, (3) 20-year simulation with NumPy arrays and plotting, (4) Monte Carlo sampling of inflows from lognormal distribution, (5) 1000 Monte Carlo simulations of 20-year reservoir runs to assess probabilistic outcomes: final storage statistics, water deficit fractions, 95th percentile.

Tools: numpy, pandas, matplotlib, seaborn, scipy.stats (normal, lognormal distributions, skew, kurtosis functions).

## Lecture 10: Reservoir Simulation & Time Series Analysis (Oct 30, 2020)

Notebook: Lec10_ReservoirTimeSeries.ipynb (PurdueCyberTraining/python4env GitHub)

Extends reservoir simulation with synthetic streamflow generation from historical data. Uses Shasta Reservoir (northern California) monthly inflow data (shasta_inflow.csv): 480 months from Oct 1980 to Sep 2020. Demonstrates full time series workflow: data loading (pandas.read_csv, datetime conversion), exploratory analysis (plotting, histograms), distribution fitting.

Fits lognormal distribution to historical inflows: lognorm.fit returns shape=1.17, loc=11488.67, scale=17421.08. Compares fit statistics (mean, std) to data. Generates synthetic inflows (synthetic1) by sampling fitted lognormal distribution.

Addresses seasonality: log-transforms inflows and examines monthly means/stds using pandas.groupby. Removes trend via linear regression (statsmodels.formula.api.ols) on log-inflows vs time. Deseasonalizes by converting to monthly z-scores: (inflow - monthly_mean) / monthly_std.

Tests autocorrelation using scatter plots and ACF plots (statsmodels.graphics.tsaplots.plot_acf). Fits autoregressive (AR) models with lag variables (lag-1, lag-2, lag-3, lag-12) using OLS regression to deseasoned data. Final model uses AR(1,12): deseas ~ deseas_l1 + deseas_l12, R²=0.471. Examines residuals to confirm white noise properties.

Generates synthetic time series (synthetic2) by reversing deseasonalization: (1) samples normally distributed noise, (2) applies AR prediction + noise, (3) reseasonalizes via inverse z-score transform, (4) exponentiates back to original scale. Visualizes synthetic vs historical inflows, monthly statistics comparison.

Implements reservoir simulation with synthetic inflows and handles demand growth (0.1%/month exponential increase). Demonstrates 10,000 Monte Carlo scenarios: generates 10000 x 240 (20 years x 12 months) synthetic inflow array using NumPy for computational efficiency. Uses lag initialization from last 12 months of historical data.

Advanced topics mentioned: ARMA (correlated errors), ARIMA (integrated trends), ARIMAX (exogenous variables), Fourier analysis, Wavelet analysis, Multivariate synthetic time series with Copulas and Vector Auto-Regression, Semiparametric sampling, Hidden Markov Models.

Libraries: numpy, pandas, matplotlib, seaborn, scipy.stats (lognorm, gamma, norm), statsmodels.formula.api (OLS), statsmodels.graphics.tsaplots (plot_acf).

Dataset: shasta_inflow.csv (480 monthly records, AF units, 1980-2020).

Key learning outcomes: Monte Carlo uncertainty quantification, deterministic vs stochastic reservoir modeling, time series deseasonalization and detrending, autoregressive model fitting, synthetic streamflow generation preserving seasonality and autocorrelation.

## Summarized attachments

- **Notes: Simulation & Monte Carlo** (https://github.com/PurdueCyberTraining/python4env/blob/main/Lec7-0-MonteCarlo/Lec9_ResevoirMonteCarlo.ipynb, Jupyter notebook): Lecture 9 on Monte Carlo methods for uncertainty quantification in environmental models. Demonstrates MC sampling with PM10 air quality (normal distribution), probability violation calculations, and propagation of uncertainty through nonlinear health impact models. Implements deterministic reservoir model with water balance constraints (negative storage handling, maximum storage via spillage). Progresses to stochastic models with lognormal inflow sampling and 1000 MC simulations to assess probabilistic outcomes (final storage statistics, water deficit fractions, percentile exceedances).
- **Notes: Simulation, Monte Carlo, & time series** (https://github.com/PurdueCyberTraining/python4env/blob/main/Lec7-1-Timeseries/Lec10_ReservoirTimeSeries.ipynb, Jupyter notebook): Lecture 10 on time series analysis and synthetic streamflow generation. Uses 480 months of Shasta Reservoir historical inflow data (1980-2020). Covers distribution fitting (lognormal), deseasonalization via monthly z-scores, autocorrelation testing (ACF plots), autoregressive (AR) model fitting with lag variables (lag-1, lag-12; R²=0.471), synthetic time series generation by reversing deseasonalization process. Demonstrates 10,000 MC scenarios with synthetic inflows preserving seasonality and autocorrelation for reservoir simulation with demand growth.
