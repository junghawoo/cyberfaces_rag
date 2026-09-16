---
title: "Ecology: Lake Metabolism"
unit_id: 215
course_id: 0
level: "Expert"
slug: lake-metabolism
is_course: 0
---

# Ecology: Lake Metabolism

## Summary

Expert-level ecology module modeling ecosystem metabolism in lakes using R, delivered via notebook `Lake Metabolism.ipynb` (GitHub jakehosen/cybertraining_ecology, Level 2).

Loads a revised gas-exchange function `k.read.fixed` (a fixed version of the Read/Jordan Read USGS K600 model using wind speed, Kd light attenuation, latitude, lake area, atmospheric pressure, water/air temperature, relative humidity, shortwave/longwave radiation; internally calls calc.zeng, water.density, thermal expansion and kinematic viscosity helpers, Schmidt number 600 scaling). R libraries: tidyr, dplyr, rLakeAnalyzer, lubridate, LakeMetabolizer (developed by USGS and collaborators), curl, ggplot2, readr, zoo, reshape2.

Explains ecosystem metabolism (productivity, respiration, carbon cycling) inferred from dissolved-oxygen (DO) time series to estimate gross primary production (GPP) and aerobic respiration (ER), presenting the modeled DO change equation with terms GPP_d, ER_d, K600_d gas exchange, PPFD photosynthetic photon flux density, Osat DO saturation, and mixing depth z. Contrasts lake gas exchange (wind turbulence, solar convection, water color, lake size) versus stream turbulence.

Data loading: Sparkling Lake 2014 hourly wide water-temperature CSV (`Sparkling2014wtemp_hourly_wide.csv`, 2532 rows × 29 columns), meteorological metData.rds (air_temp, rel_hum, wind_speed_2m, par, opt_wtemp, opt_do_raw), and RDS temperature files for BASS, CITZ (Citizens Reservoir), CROK (Crooked Lake), FAIL (Failing Lake) buoys. Computes DO saturation with `o2.at.sat.base` (altitude 300). Explains lake stratification layers (epilimnion, metalimnion, hypolimnion), uses `wtr.heat.map` and `wtr.plot.temp` for depth-vs-time heatmaps, `ts.thermo.depth` for thermocline/mixing depth, plotted with ggplot2. Corrects wind with `wind.scale.base` (U10), converts PAR to shortwave via `par.to.sw.base`, computes net longwave via `calc.lw.net.base`, and `is.day` day/night irradiance flag.

Metabolism calculation: computes K600 via `k.cole.base` (Cole simple temperature method) and `k.read.fixed` (Read method), converts to O2 gas exchange with `k600.2.kGAS.base`, then estimates metabolism per day using `metab.mle` (Maximum Likelihood Estimation), `metab.ols`, `metab.kalman`, and `metab.bookkeep`, producing NEP/ER/GPP outputs combined and compared with faceted ggplot geom_smooth (loess). Includes an Indiana Lakes comparison table (Indiana_Lakes.jpg) with sites ACRE (Intermittent Drainage Wetland, agricultural tile drainage), BASS Lake, Citizens Reservoir (CITZ, urban industrial), Crooked Lake (CROOK, forested/residential), Failing Lake (FAIL, forested prairie preserve), Geist Reservoir (GEIST, urban residential), and PWA wetlands (PWAP1, PWAP2), listing latitude, longitude, max depth, surface area, Secchi depth, watershed area, dominant land use, sampling period. Loads per-site metabolism RDS files (dated 20241007) and plots photosynthesis (GPP > 0.05) for each. Suggests extending analysis to Lake Taihu data.

## Summarized attachments

- **JN - Lake Metabolism** (https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Lake%20Metabolism.ipynb, Jupyter notebook): Expert-level R notebook for modeling ecosystem metabolism in lakes using dissolved oxygen time series analysis with functions for gas exchange calculations, thermal stratification detection, and metabolism estimation via multiple methods (maximum likelihood, OLS, Kalman filter, bookkeeping), applied to Indiana lake datasets with visualization and comparison of gross primary production and respiration across sites with different land use characteristics.
