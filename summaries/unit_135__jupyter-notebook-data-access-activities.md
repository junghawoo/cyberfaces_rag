---
title: "Jupyter NoteBook - Data Access Activities"
unit_id: 135
course_id: 0
slug: jupyter-notebook-data-access-activities
is_course: 0
---

# Jupyter NoteBook - Data Access Activities

This module contains four hands-on activities demonstrating data access and retrieval using Jupyter notebooks from the PurdueCyberTraining/justiceindata repository.

**Activity 1 (Activity1_Student.ipynb, Activity1A.ipynb, Activity1B.ipynb)**: NOAA Weather Data Access via API. Students learn to download climate variables—Mean temperature (TAVG), Precipitation (PRCP), and Wind direction (WDF5)—from NOAA GHCND (Global Historical Climatology Network) stations using API authentication tokens. Examples use multiple airport stations: Los Angeles International Airport (GHCND:USW00023174), Atlanta Hartsfield Jackson (GHCND:USW00013874), Austin Bergstrom (GHCND:USW00013904), and Dallas Fort Worth (GHCND:USW00003927). The activities use Python libraries: requests (HTTP requests), pandas (data manipulation), json (API response parsing), numpy (array operations), and datetime (timestamp parsing). Code demonstrates API call construction, JSON response parsing, filtering data by datatype, populating DataFrames, unit conversion (tenths of Celsius to Fahrenheit, tenths of inches to millimeters), and exporting to CSV files (Temperature.csv, PRECIPITATION.csv, PRECIPITATION_FW.csv). Activities include multi-year data retrieval loops (2018-2020 range).

**Activity 2 (Activity2.ipynb, Activity_2_students.ipynb)**: USGS NWIS Data Retrieval using dataretrieval library. This section covers the dataretrieval.nwis Python package for accessing USGS water data. Available NWIS services include: instantaneous values (iv), daily values (dv), site information, discharge peaks, discharge measurements, and water quality samples (qwdata). Key parameter codes: water temperature (00010), discharge cubic feet per second (00060), gage height feet (00065). Examples use Trinity River at Dallas (site 08057000), Hunting River near Houston (08075770), Chattahoochee River at Atlanta (02336000), and Spavinaw Creek near Maysville (07191160). Code retrieves daily/instantaneous values, peak discharge events, field measurements, and water quality data for date ranges (2014-2016). Includes data concatenation with pandas.concat(), matplotlib line plot visualization, and CSV export. Multi-site comparison demonstrates discharge pattern analysis.

**Activity 3 (Activity3.ipynb)**: NetCDF Data Processing Pipeline. Four-part activity covering authenticated bulk download of Aphrodite precipitation/temperature netCDF files from https://www.chikyu.ac.jp/precip/english/ using requests and username/password credentials. Files downloaded as gzip archives (APHRO_V1808_TEMP format, 2008-2010 year range). Unzipping uses gzip library. Reading uses netCDF4.Dataset to load .nc files and extract variables: lat, lon, time, tave (temperature average). Extracts coordinate arrays and identifies nearest grid point to a location of interest (example: 33.70°N, 73.10°E in Asia) using squared-difference indexing with numpy.argmin(). Creates pandas DataFrame with daily date_range and loops through time dimension to populate temperature time series (stored as temparature_2008Isb.csv).

**Activity 4 (Activity4.ipynb)**: CSV Data Access from GitHub. Demonstrates downloading CSV datasets from GitHub repositories using requests library. Example: temp_open_utc.csv from buds-lab/the-building-data-genome-project. Highlights raw GitHub URL format (https://raw.githubusercontent.com/...). Uses pandas.read_csv() to load downloaded files and matplotlib.plot() for visualization of building temperature data with multiple columns (PrimClass_*, Office_*, UnivLab_*, UnivDorm_* sensors).

Key libraries used across activities: requests, pandas, numpy, json, datetime, gzip, netCDF4, matplotlib. Topics include API authentication, JSON parsing, unit conversion, CSV I/O, dataframe operations, temporal data handling, geospatial indexing, and visualization.

## Summarized attachments

- **Activity 1 Student (notebook)** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity1_Student.ipynb, Jupyter notebook): Teaches downloading climate variables (Mean temperature TAVG, Precipitation PRCP, Wind direction WDF5) from NOAA GHCND weather stations using API authentication tokens, with examples using airport stations (Los Angeles, Atlanta, Austin) and Python libraries for API calls, JSON parsing, DataFrame population, and unit conversions.

- **Activity 1A (notebook)** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity1A.ipynb, Jupyter notebook): Demonstrates downloading precipitation data from NOAA via the GHCND API, including single-year and multi-year retrieval loops for Dallas Fort Worth and other stations, with data transformation to millimeters and CSV export.

- **Activity 1B (notebook)** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity1B.ipynb, Jupyter notebook): Covers downloading temperature (TAVG) data from NOAA GHCND for specific stations, with conversion from tenths of Celsius to Fahrenheit and example export to CSV files.

- **Activity 2 (notebook)** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity2.ipynb, Jupyter notebook): Teaches USGS water data retrieval using the dataretrieval library with example parameter codes for water temperature, discharge, and gage height from Trinity River and other USGS sites, demonstrating daily/instantaneous values, peak discharge, field measurements, and water quality data retrieval with visualization and CSV export.

- **Activity 2 students (notebook)** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity_2_students.ipynb, Jupyter notebook): Student exercise notebook covering USGS NWIS data retrieval for water quality and discharge measurements using dataretrieval library with guided activities for Chattahoochee River and Spavinaw Creek stations.

- **Activity 3 (notebook)** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity3.ipynb, Jupyter notebook): Four-part tutorial on downloading, unzipping, and processing netCDF files from Aphrodite precipitation/temperature database including authenticated downloads, gzip decompression, variable extraction (lat, lon, time, temperature), geospatial nearest-neighbor indexing, and time series DataFrame creation and export.

- **Activity 4 (notebook)** (https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity4.ipynb, Jupyter notebook): Demonstrates downloading CSV datasets from GitHub repositories using raw URLs and requests library, with example of building temperature data from the buds-lab/the-building-data-genome-project and pandas/matplotlib visualization techniques.
