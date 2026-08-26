---
title: "Ecology: Stream Metabolism"
unit_id: 226
course_id: 0
level: "Expert"
slug: ecology-stream-metabolism
is_course: 0
---

# Ecology: Stream Metabolism

Expert-level ecology tutorial on modeling ecosystem metabolism (productivity, respiration, carbon cycling) in streams/rivers. The main resource is the Jupyter notebook `Stream Metabolism.ipynb` from the GitHub repo `jakehosen/cybertraining_ecology` (Level 2). Workflow: download data from StreamPULSE, compute gas exchange different ways, run the model with old-school K estimates, run the model with Bayesian estimation, and plot results.

The work uses R (despite `python` code fences) with libraries: dataRetrieval, stringr, parallel, lubridate, streamMetabolizer, zoo, chron, dplyr, doBy, oce, and later rstan (rstan 2.32.5 / Stan 2.32.2, requiring StanHeaders). streamMetabolizer is a USGS-developed R package (documentation at usgs-r.github.io/streamMetabolizer via web.archive.org). Method uses dissolved oxygen (DO) time series to infer gross primary production (GPP) and aerobic ecosystem respiration (ER), comparing daytime vs. nighttime oxygen change while accounting for air-water gas exchange. The governing equation models modeled DO (mO_i,d) using GPP_d, ER_d, cross-sectional depth Z_i,d, standardized gas exchange K600_d (scaled to Schmidt number 600), DO saturation O_sat, PPFD (photosynthetic photon flux density), and timestep Δt (60 minutes). Units: g-O2 m^-2 d^-1.

Custom functions defined: `radi` (degrees to radians); `lightest` (models light insolation from time and location via solar position, computing solar declination, hour angle, equation of time, returns GI); `bpcalc` (barometric pressure correction to altitude, returns mm Hg); `get_usgs_q_data` (downloads USGS discharge data via constructNWISURL/importWaterML1 for parameter codes 00060 discharge and 00065 gage height, statCd 00011). Study site: Farmington River at USGS gage 01184000, Unionville, Connecticut (lat 41.7555472, lon -72.8870417, elevation 66). Datasets: barometric pressure `files/bdl_pressure_2014_2020_15.rds` and sonde data `files/unio.csv` (temperature, dissolved oxygen HDO_mg_l, specific conductance SpCond, pH). Analysis subset July 2017.

Processing: converts discharge cfs to cms (×0.0283168), converts conductance to salinity via oce::swSCTp, computes DO saturation via calc_DO_sat with the garcia-benson model, derives DO percent saturation. Channel geometry obtained from USGS NWIS measurements (importRDB1) to estimate mean depth, width, and velocity via linear regressions (log mean_depth ~ log discharge; velocity and width ~ gage height). Gaps ≤2 hours interpolated per day using na.approx (zoo); solar time computed with streamMetabolizer::calc_solar_time.

The `metab` function (author Alison Appling) fits metabolism models; documentation details required input columns (solar.time, DO.obs, DO.sat, depth, temp.water, light; discharge optional) and model types mle, night, bayes, Kmodel, sim with their data_daily formats (K600.daily, GPP.daily, ER.daily, etc.). Two gas-exchange approaches: (1) manual empirical K estimation from flow rate; (2) Bayesian estimation pooling K across days via discharge–K relationship. Bayesian model name `b_Kb_oipi_tr_plrckm.stan` (pool_K600='binned', err_obs_iid, err_proc_iid, ode_method trapezoid). Log-discharge binned via calc_bins (width 0.2) producing K600_lnQ_nodes_centers (brks). Specs set burnin_steps=10, saved_steps=20, GPP_daily_mu=3.1, ER_daily_mu=-7.1, 4 chains on 4 cores; MCMC via Stan (rstan), model fit in ~24 sec. Final step plots comparison of GPP and ER estimates between the two K-estimation methods.

## Summarized attachments

- **Stream Metabolism Jupyter Notebook** (https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Stream%20Metabolism.ipynb, notebook): Interactive R-based tutorial on ecosystem metabolism modeling in streams using dissolved oxygen time series, streamMetabolizer package, and Bayesian parameter estimation methods including gas exchange rate (K600) estimation, gross primary production (GPP), and ecosystem respiration (ER) calculations.
