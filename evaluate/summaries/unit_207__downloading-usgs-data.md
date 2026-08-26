---
title: "Ecology: Downloading USGS Data"
unit_id: 207
course_id: 0
level: "Foundation"
slug: downloading-usgs-data
is_course: 0
---

# Ecology: Downloading USGS Data

This Foundation-level ecology module teaches how to download hydrology and water quality data from the USGS National Water Information System (NWIS) using the R package **dataRetrieval**. The lesson resource is the Jupyter notebook "Ecology - Download USGS Data" (Downloading USGS Data.ipynb) from the GitHub repo jakehosen/cybertraining_ecology (Level 1). It references the CRAN "Introduction to the dataRetrieval package" vignette. Data types covered: site data; hydrology time series (stream/river stage and discharge, groundwater level); rating curve data (converting stage to discharge); and surface water chemistry/quality data. NWIS collects time series (typically 15-minute intervals), individual observations, and water quality samples.

**Getting R packages loaded:** libraries dataRetrieval, stringr, gridExtra, ggplot2, reshape2, tidyverse (tidyverse 2.0.0: dplyr, readr, forcats, tibble, lubridate, tidyr, purrr). Uses options(repr.matrix.max.cols/max.rows) and repr.plot.res for Jupyter display.

**Site Data:** USGS sites use 8-digit site identifiers; readNWISsite(siteNumbers) retrieves site metadata (columns station_nm, lat_va, long_va, huc_cd = Hydrological Unit Code / watershed address, contrib_drain_area_va = drainage area, well_depth_va). Example site numbers "01491000","01645000". Links to the USGS national map (maps.waterdata.usgs.gov/mapper) and the Wikipedia Hydrological code article.

**Codes:** Parameter codes (pCode, 6 digits) — 00060 Discharge (ft^3/s), 00065 Gage height (ft), 00010 Temperature (C), 00300 Dissolved oxygen, 00400 pH, 00602 Nitrate filtered (mg-N/L). Statistics codes (statCd, 5 digits) — 00001 Maximum, 00002 Minimum, 00003 Mean, 00008 Median. Service codes — dv daily values, uv unit values, qw water quality, sv site visits, pk peak measurements, gw groundwater levels, ad annual data report sites. Links to USGS parameter code list, stat_code list, and USGS Water Services.

**Site information:** whatNWISdata(siteNumber, service, statCd) lists available variables; example USGS Super Gage site Wabash River at New Harmony, Indiana (ID 03378500), querying dv/statCd 00003, yielding 12 variables (parm_cd column). whatWQPsamples(siteid="USGS-03378500") lists water quality grab samples; the ActivityIdentifier column holds the parameter code in its last five digits, extracted via a regular expression \d{5}$ using str_extract from stringr, stored as character in pCode (preserving leading zeros). Notes the qw service is being deactivated.

**Hydrology Time Series:** readNWISdata for Wabash River (03378500), service "iv" (instantaneous) and "dv" (daily), parameterCd 00065/00060, startDate/endDate, tz CST/CST6CDT; converts dateTime to R date; plots discharge (X_00065_00000) and stage with ggplot geom_line, arranged via grid.arrange (gridExtra). POSIX timestamps.

**Field Hydrology Measurements:** service "measurements" retrieves field measurements (gage_height_va, discharge_va) for rating curves; discusses floodplain effect on stage-discharge slope. Four fitting approaches compared by RMSE: log-transformed linear regression, quadratic, third-order polynomial, and LOESS (locally weighted scatterplot smoothing), using lm, poly, loess, and predict.

**Water Quality Sensor Data:** whatNWISsites(stateCd="IN", parameterCd="99133") finds in-situ nitrate sensor sites (20 found); site_tp_cd codes ST (stream), LK (lake), GW (groundwater). readNWISdata for Wabash River (03378500) and White River at Hazelton (03374100), parameters discharge 00060, temperature 00010, nitrate 99133; uses melt (reshape2) to reshape wide-to-long and facet_wrap plotting.

**Groundwater Well Data:** whatNWISsites(stateCd="IN") subset to GW sites; three groundwater pCodes — 30210 (Depth to water level below land surface datum LSD), 30211 (Elevation above NGVD 1929, meters), 62611 (Groundwater level above NAVD 1988, feet). readNWISgwl("393423086161001") downloads Morgan County, Indiana data; plots lev_va / sl_lev_va (level above sea level) since 1983.

**Water Quality Data:** whatNWISdata(parameterCd c("00602","00660"), stateCd "IN", service "qw") finds total dissolved nitrogen / orthophosphate sites; readNWISqw for Whitewater River near Economy, IN (03274650); count_nu indicates sample availability.

**Exercises ("Now it's your turn!"):** plot discharge over a year for a chosen site (example 01646500) and fit rating curves selecting the best equation by RMSE (log-transformed linear, quadratic, third-order polynomial, LOESS). Sample output shows measurement records from 1930–2024 and regression coefficients.

## Summarized attachments

- **Ecology - Download USGS Data (notebook)** (GitHub jakehosen/cybertraining_ecology/Level 1/Downloading USGS Data.ipynb, Jupyter notebook): Interactive R notebook teaching USGS National Water Information System (NWIS) data access and analysis via the dataRetrieval package. Covers site data (8-digit site identifiers, metadata), hydrologic time series (stream stage/discharge via readNWISdata services iv/dv/measurements), rating curves (gage height vs discharge relationships fit by log-transformed linear regression, quadratic, third-order polynomial, LOESS), water quality sensor data (in-situ nitrate, temperature), groundwater well data (depth to water level, elevation), and water quality grab samples. Visualizes data with ggplot2 and grid.arrange. References the dataRetrieval CRAN vignette and USGS parameter/statistic/service code documentation.
