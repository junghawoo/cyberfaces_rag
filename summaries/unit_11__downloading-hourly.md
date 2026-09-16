---
title: "Downloading hourly gauge precipitation from National Climate Data Center (NCDC)"
unit_id: 11
course_id: 4
level: "Developer"
slug: downloading-hourly
is_course: 0
---

# Downloading hourly gauge precipitation from National Climate Data Center (NCDC)

FAIR Science Data Access Module #3. Automatically download hourly precipitation datasets from National Climate Data Center (NCDC). Prepared by Pin-Ching Li, Sayan Dey, Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University, vmerwade@purdue.edu).

Objective: Learn to access NCDC weather database and download precipitation datasets using cdo-api-py Python module. Covers both single-station and multi-station downloads within study area boundaries. Method applies to other NCDC datasets (temperature, soil temperature, snowfall).

Requirements: Web browser, mygeohub.org account, Jupyter Notebook (Download_NCDC_Rainfall.ipynb provided).

Data sources: NOAA (National Oceanic and Atmospheric Administration), NCDC (National Climate Data Center). Two download methods: (1) by station ID, (2) by study area latitude-longitude boundary.

Access token: Required to access NCDC Climate Data Online (CDO) web services (https://www.ncdc.noaa.gov/cdo-web/token). Generate by email; limits: 5 requests/second, 10,000 requests/day. Do not share token publicly.

Python libraries: cdo_api_py (Client class for NCDC database access), pandas (dataframe storage), datetime (datetime object conversion).

Single-station download workflow: Create Client instance with token; set startdate/enddate (datetime objects, format yyyy-mm-dd hh:mm:ss); set datasetid ("PRECIP_HLY" for hourly precipitation); input gauge_id (e.g., "COOP:180700"); call get_data_by_station function; store result in pandas dataframe; export to CSV file (filename format: datasetid + gauge_id + ".csv").

Multi-station download workflow: Define extent as dictionary (north, south, east, west latitude/longitude); call find_stations function with datasetid, extent, startdate, enddate; returns dataframe containing station info (ID, datacoverage, elevation, elevationUnit, latitude, longitude, maxdate, mindate, name); loop through stations, extract ID, call get_data_by_station for each station to download data.

Example coordinates: north 39.14, south 38.68, east -74.65, west -77.35 (study area boundary window).

Data format: HPCP unit: 1/100 inch (standard); output: CSV files with precipitation values.

Jupyter Notebook: https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA2/Coursepage_DA2_Download_NCDC_Rainfall.ipynb.

Homework: Plot monthly and daily streamflow depths (USGS gage 03335500 Wabash at Lafayette, IN); overlay monthly and daily precipitation depths for watershed (HU 05120108 outlet at 03335500); FAIR data principles image included.

## Summarized attachments
- **Accessing and Downloading Precipitation Data from NCDC database** (Accessing_and_Downloading_Precipitation_Data_from_NCDC_database.pdf, file): Tutorial by Pin-Ching Li, Sayan Dey, and Venkatesh Merwade on downloading hourly precipitation data from NOAA's National Climate Data Center. Covers NCDC Climate Data Online (CDO) web services access token generation, single-station and multi-station downloads using cdo-api-py Python module. Details single-station workflow (get_data_by_station function with station ID "COOP:180700" example) and multi-station workflow (find_stations function with latitude-longitude boundary extents). Specifies hourly precipitation dataset type ("PRECIP_HLY"), data format (HPCP in 1/100 inch units), and CSV output files.
- **FAIR Data Principles** (FAIR_data_principles.jpg, image): Image illustrating FAIR data principles.
- **Jupyter Notebook Exercise** (github.com/PurdueCyberTraining/fairclimatewater, notebook): Jupyter Notebook (DA2 module) implementing NCDC precipitation data download using cdo-api-py Client class with user token, pandas dataframe storage, and datetime formatting; includes examples for single and multi-station downloads within study area boundaries.
