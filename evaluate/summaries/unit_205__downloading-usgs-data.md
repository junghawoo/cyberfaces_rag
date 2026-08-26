---
title: "Downloading USGS Data"
unit_id: 205
course_id: 0
level: "Foundation"
slug: downloading-usgs-data
is_course: 0
---

# Downloading USGS Data

This Foundation-level module teaches downloading hydrology and water quality data from the USGS National Water Information System (NWIS) using the R package **dataRetrieval**. (Content is identical to unit 207; the fetched resource here is titled "DownloadData (notebook)" — Downloading USGS Data.ipynb from GitHub repo jakehosen/cybertraining_ecology, Level 1.) Cites the CRAN "Introduction to the dataRetrieval package" vignette. Data types covered: site data; hydrology time series (stream/river stage and discharge, groundwater level); rating curve data; and surface water chemistry/quality. NWIS holds time series (typically 15-minute intervals), individual observations, and water quality samples.

**Packages loaded:** dataRetrieval, stringr, gridExtra, ggplot2, reshape2, tidyverse (2.0.0: dplyr, readr, forcats, tibble, lubridate, tidyr, purrr); Jupyter display options repr.matrix.max.cols/max.rows and repr.plot.res.

**Site Data:** 8-digit site identifiers; readNWISsite(c("01491000","01645000")). Key columns: station_nm, lat_va, long_va, huc_cd (Hydrological Unit Code / watershed address), contrib_drain_area_va (drainage area), well_depth_va. Links to USGS national map (maps.waterdata.usgs.gov/mapper) and Wikipedia Hydrological code.

**Codes:** Parameter codes (pCode, 6-digit) — 00060 Discharge (ft^3/s), 00065 Gage height (ft), 00010 Temperature (C), 00300 Dissolved oxygen, 00400 pH, 00602 Nitrate filtered (mg-N/L). Statistics codes (statCd, 5-digit) — 00001 Maximum, 00002 Minimum, 00003 Mean, 00008 Median. Service codes — dv, uv, qw, sv, pk, gw, ad. Links to USGS parameter/stat code lists and USGS Water Services.

**Site information:** whatNWISdata(siteNumber, service, statCd) — example USGS Super Gage Wabash River at New Harmony, Indiana (ID 03378500), dv + statCd 00003 returns 12 variables (parm_cd column). whatWQPsamples(siteid="USGS-03378500") returns water quality grab samples; ActivityIdentifier column's last five digits are the parameter code, extracted with regular expression \d{5}$ via str_extract (stringr), stored as character in pCode. The qw service is slated for deactivation.

**Hydrology Time Series:** readNWISdata for Wabash (03378500), service iv and dv, parameterCd 00065/00060, tz CST/CST6CDT; POSIX dateTime converted to R date; ggplot geom_line plots of discharge (X_00065_00000) and stage arranged via grid.arrange (gridExtra).

**Field Hydrology Measurements:** service "measurements" (gage_height_va, discharge_va) for rating curves; explains floodplain effect on stage-discharge relationship. Four fits compared by RMSE: log-transformed linear regression, quadratic, third-order polynomial, LOESS (using lm, poly, loess, predict).

**Water Quality Sensor Data:** whatNWISsites(stateCd="IN", parameterCd="99133") finds 20 in-situ nitrate sensor sites; site_tp_cd codes ST/LK/GW. readNWISdata for Wabash (03378500) and White River at Hazelton (03374100), parameters 00060/00010/99133; melt (reshape2) reshapes wide-to-long; facet_wrap plotting.

**Groundwater Well Data:** whatNWISsites(stateCd="IN") subset to GW; groundwater pCodes 30210 (Depth to water level below LSD), 30211 (Elevation above NGVD 1929, meters), 62611 (Groundwater level above NAVD 1988, feet). readNWISgwl("393423086161001") for Morgan County, Indiana; plots lev_va / sl_lev_va since 1983.

**Water Quality Data:** whatNWISdata(parameterCd c("00602","00660"), stateCd "IN", service "qw") for total dissolved nitrogen / orthophosphate sites; readNWISqw for Whitewater River near Economy, IN (03274650); count_nu indicates sample availability.

**Exercises ("Now it's your turn!"):** plot discharge over a year for a chosen site (example 01646500); fit and select best rating-curve equation by RMSE (log-transformed linear, quadratic, third-order polynomial, LOESS). Sample outputs show field measurement records 1930–2024 and regression coefficients.

## Summarized attachments

- **DownloadData (notebook)** (GitHub jakehosen/cybertraining_ecology/Level 1/Downloading USGS Data.ipynb, Jupyter notebook): Interactive R notebook teaching USGS National Water Information System (NWIS) data access and analysis using the dataRetrieval package. Content identical to unit 207: site data retrieval (8-digit site identifiers, station name, coordinates, hydrological unit code, drainage area), hydrologic time series (stream stage and discharge via services iv instantaneous/dv daily via readNWISdata), rating curve data (gage height vs discharge field measurements fit by multiple regression models: log-transformed linear, quadratic, third-order polynomial, LOESS to compare by RMSE), water quality sensor data (Wabash River 03378500, White River 03374100, parameters discharge/temperature/nitrate with NEON data product codes), groundwater well levels (depth to water level, elevation above sea level via readNWISgwl), and water quality grab samples (filtered nitrogen, orthophosphate). Visualized with ggplot2, facet_wrap, grid.arrange. Cites CRAN dataRetrieval vignette and USGS parameter/statistics/service code documentation.
