---
title: "Visualizing rainfall data"
unit_id: 114
course_id: 4
level: "Foundation"
slug: visualizing-rainfall-data
is_course: 0
---

# Visualizing rainfall data

This module teaches spatial visualization of precipitation data to identify geographic rainfall patterns and inconsistencies between gauge stations. It focuses on creating scatter plots with color mapping and variable marker sizes to visualize maximum daily precipitation in Indiana for 2019 using National Climate Data Center (NCDC) data.

**Source materials:** PDF document `NCDC_Visualization.pdf` prepared by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade (vmerwade@purdue.edu) from Lyles School of Civil Engineering, Purdue University. Jupyter Notebook exercise `NCDC_Visualization.ipynb` (GitHub: https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DV1/Visualization_NCDC.ipynb). Prerequisite: tutorial "Accessing and Downloading Precipitation Data from NCDC database."

**Environment:** Web browser with mygeohub.org account; Jupyter Notebook platform.

**Data source and access:** NCDC's Climate Data Online (CDO) web services via Python cdo_api_py module requiring user access token. Precipitation dataset type: GHCND (Global Historical Climatology Network - Daily) with PRCP column measured in tenths of millimeters. Date range: 01/01/2019 to 12/31/2019 across Indiana.

**Station discovery and filtering:** Use Client class from cdo_api_py with token authentication. Define geographic extent for Indiana: north latitude 41.76, south latitude 37.8, east longitude -84.81, west longitude -88.03. Apply find_stations() function to retrieve all stations within extent and date range. Filter results by data coverage quality: eliminate stations with maxdate prior to 12/31/2019 or mindate later than 01/01/2019; remove stations with datacoverage < 0.95 using datetime.strptime() to convert date strings to datetime objects; manually exclude list of insufficient gages (GHCND:US1INBN0010, GHCND:US1INBW0010, etc.); purge stations from other states by checking name suffix ("IN US"). Final cleaned list contains 153 NCDC weather stations with sufficient precipitation data quality.

**Data download and merge:** Iterate through cleaned station list; download precipitation data for each station using get_data_by_station() with datasetid, stationid, startdate, enddate parameters; set date column as index using pd.to_datetime(); filter for PRCP column only; rename columns to station IDs; merge all station dataframes using pd.merge() with outer join to create unified GHCN_IN dataframe.

**Visualization methods:** Generate statistics using pandas describe() function. Append latitude-longitude coordinates by pivoting stations dataframe and renaming indices. Create scatter plots with geographic coordinates (longitude on x-axis, latitude on y-axis) using matplotlib.pyplot. Apply color mapping via cmap parameter (options: 'jet', 'viridis') to represent maximum precipitation values. Normalize marker size using formula 5^(max_precip / mean_precip * 2) to show proportional differences. Identify and remove outliers (values > 2000 tenth-mm) for clearer spatial pattern visualization.

**Assignment:** Create scatter plot of NCDC stations in Indiana with color mapping and variable marker sizes representing mean and standard deviation of precipitation datasets for 2018.

## Summarized attachments
- **NCDC Visualization** (NCDC_Visualization.pdf, file): Tutorial by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade on visualizing spatial distributed precipitation data from National Climate Data Center (NCDC) to identify geographic rainfall patterns, covering NCDC's Climate Data Online (CDO) web services API access via cdo_api_py, station discovery within geographic extent using find_stations() function, data quality filtering by coverage percentage and date completeness, download of GHCND daily precipitation data via get_data_by_station(), merging multiple station dataframes, and scatter plot visualization with color mapping and variable marker sizes representing maximum precipitation values across Indiana weather stations.
