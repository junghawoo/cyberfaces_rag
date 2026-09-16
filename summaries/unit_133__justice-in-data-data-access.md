---
title: "Justice in Data: Data Access"
unit_id: 133
course_id: 10
level: "Foundation"
slug: justice-in-data-data-access
is_course: 0
---

# Justice in Data: Data Access

This module covers data access fundamentals for water and energy domain applications. Presenters: Steven Tanner McCullough and Junaid Ahmad.

**Data Access Fundamentals**: Data access is defined as the on-demand, authorized ability to retrieve, modify, copy, or move data from IT systems in an authenticated manner. Three main categories of data sources are covered: local files, databases (organized structured information managed via Database Management Systems/DBMS), and Application Programming Interfaces (APIs). Python is used throughout with its flexible open-source libraries for accessing and processing data.

**Major Data Sources**: Earth Explorer (USGS), National Oceanic and Atmospheric Administration (NOAA), National Weather Service, and NASA POWER provide water and environmental data. Building Energy Domain sources include eiapy and nrel-dev-api (PyPI libraries) for accessing U.S. Energy Information Administration (EIA) and National Renewable Energy Laboratory (NREL) data, plus the Building Data Genome Project (GitHub repository, National University of Singapore). CSV (Comma-Separated Value) files are explained as data storage methods where entries are saved as text with commas/spaces/semicolons to organize data for program interpretation.

**Four Hands-On Python Activities**:

1. **Accessing Temperature/Precipitation Data from NOAA**: Uses NOAA's Climate Data Online (CDO) API with datatype codes (e.g., PRCP for precipitation, TAVG for temperature). API parameters include datasetid (GHCND—Global Historical Climatology Network Daily), limit (max 1000), stationid, startdate, and enddate. Activities implemented in Jupyter Notebooks (Activity1A, Activity1B) via MyGeoHub platform.

2. **Downloading Streamflow Data from USGS**: Uses dataretrieval Python package to retrieve hydrologic data from the National Water Information System (NWIS) and Water Quality Portal (WQP—EPA, USDA, USGS data). Services include instantaneous values (iv), daily values (dv), site info, discharge peaks, discharge measurements, and water quality samples (qwdata). Site type codes and parameter codes documented for surface water, groundwater, atmospheric, and spring sites. Jupyter Notebook: Activity2.

3. **Downloading netCDF Files from APHRODITE**: NetCDF (network Common Data Form) stores multidimensional scientific data (temperature, humidity, pressure, wind speed/direction). APHRODITE (Asian Precipitation - Highly-Resolved Observational Data Integration Towards Evaluation) develops daily precipitation/temperature datasets at 0.5° and 0.25° spatial resolution. Manual download steps and bulk downloading via Python; data viewer: Panoply. Jupyter Notebook: Activity3.

4. **Downloading CSV from Building Genome Project via GitHub**: Building Genome Projects I & II contain time-series hourly energy usage data for residential, commercial, education, and industrial buildings—serving as test bench for modeling/analysis techniques. Data stored as singular CSV on GitHub repository (buds-lab/the-building-data-genome-project) because it is static (not frequently updated). Method 1: manual download via browser; Method 2: Python Requests library to download raw CSV (temp_open_utc.csv) for reproducible analysis. Jupyter Notebook: Activity4.

**Key Tools & Libraries**: Python, Pandas, Jupyter Notebook (MyGeoHub), NOAA Climate Data Online (CDO) API, dataretrieval-python, USGS NWIS, APHRODITE, netCDF format, Panoply viewer, Requests library, GitHub.

**References**: Hodson et al. 2023 (dataretrieval Python package DOI), GeoDelta Labs (YouTube), "Getting Weather Data in 3 Easy Steps" (Towards Data Science).

**External Resources**: Data Access Pre-Survey (QuestionPro link) and YouTube recording of presentation.

## Summarized attachments
- **Data Access Slides** (`Data_Access_Final.pdf`, file): Presented by Steven Tanner McCullough and Junaid Ahmad, covers data access fundamentals (definition, authorization, authentication), three main data source categories (local files, databases, APIs), and water/energy domain data sources (USGS Earth Explorer, NOAA, NASA POWER, EIA, NREL).
- **Activity 1A: NOAA Temperature/Precipitation Data Access** (Jupyter notebook, MyGeohub): Hands-on exercise accessing NOAA's Climate Data Online (CDO) API for precipitation (PRCP) and temperature (TAVG) data using GHCND dataset and station/date parameters.
- **Activity 1B: NOAA Temperature/Precipitation Data Access (continuation)** (Jupyter notebook, MyGeohub): Continuation of Activity 1A for NOAA data retrieval.
- **Activity 2: USGS Streamflow Data Download** (Jupyter notebook, MyGeohub): Hands-on exercise downloading daily streamflow values (ft3/sec) from USGS NWIS using the dataretrieval Python package, covering instantaneous values, daily values, site info, discharge peaks/measurements, and water quality data (qwdata).
- **Activity 3: APHRODITE netCDF Files Download** (Jupyter notebook, MyGeohub): Hands-on exercise downloading and converting netCDF files from the APHRODITE project (Asian Precipitation - Highly-Resolved Observational Data Integration Towards Evaluation) for temperature data at 0.5° and 0.25° spatial resolution, including use of Panoply netCDF viewer.
- **Activity 4: Building Genome Project CSV Download** (Jupyter notebook, MyGeohub): Hands-on exercise downloading time-series hourly energy usage CSV data from the Building Data Genome Project GitHub repository using Python Requests library for residential, commercial, education, and industrial building types.
- **Building Data Genome Project** (GitHub repository, https://github.com/buds-lab/the-building-data-genome-project): Time-series hourly energy usage data for various building types serving as test bench for energy modeling and analysis techniques; data organized as single CSV files for easy distribution and updating.
- **Data Access Pre-Survey** (https://utaedu.questionpro.com/a/TakeSurvey?tt=/g5acu9ejKwECHrPeIW9eQ%3D%3D, survey): QuestionPro-hosted pre-assessment survey for evaluating prior knowledge.
- **Data Access Recording** (https://www.youtube.com/watch?v=fRkHPIZ2DPY, video): YouTube recording of the presentation covering data access fundamentals, Python flexibility for data processing, three main data access categories (local files, databases, APIs), and overview of hands-on activities.
