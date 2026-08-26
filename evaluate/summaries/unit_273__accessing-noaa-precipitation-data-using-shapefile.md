---
title: "Accessing NOAA precipitation data using shapefile"
unit_id: 273
course_id: 0
level: "Foundation"
slug: accessing-noaa-precipitation-data-using-shapefile
is_course: 0
---

# Accessing NOAA precipitation data using shapefile

Jupyter notebook tutorial for downloading NOAA Global Historical Climatology Network Daily (GHCND) precipitation data for a watershed using USGS site number and NOAA NCEI API.

**Authors:** Jibin Joseph and Venkatesh Merwade, Lyles School of Civil Engineering, Purdue University (joseph57@purdue.edu, vmerwade@purdue.edu). **Topic:** FAIR Science in Water Resources. **Source:** Coursepage_DA6_Precipitation_Access.ipynb (GitHub: I-GUIDE/hydroewd/blob/main/prec_data/).

## Workflow Overview

**Step 1: Watershed Definition**
- Input: USGS site number (e.g., '03335000')
- Retrieve watershed boundary via pynhd.NLDI().get_basins()
- Extract extent bounds (minlon, minlat, maxlon, maxlat)
- Save watershed as ESRI shapefile
- Calculate polygon centroids for analysis

**Step 2: NOAA Station Discovery**
- NOAA NCEI API token: https://www.ncdc.noaa.gov/cdo-web/token
- Query endpoint: https://www.ncei.noaa.gov/cdo-web/api/v2/stations
- Dataset: GHCND (Global Historical Climatology Network - Daily)
- Bbox parameter format: "lat1,lon1,lat2,lon2" (from watershed bounds)
- Pagination: limit=1000 records/request, offset iteration
- Rate limiting: sleep(1) between requests
- Output: Station ID, name, latitude, longitude, elevation, date range

**Step 3: Data Filtering**
- Filter stations with End Date >= end_date (currently active)
- Convert to GeoDataFrame with Point geometry
- CRS: EPSG:4326 (WGS84)
- Visualization: Plot watershed (light blue polygon), all stations (red circles), active stations (green X marks)

## Data Retrieval and Processing

**Step 4: Precipitation Download**
- Endpoint: https://www.ncei.noaa.gov/cdo-web/api/v2/data
- DataType ID: PRCP (precipitation), datasetid: GHCND
- Date range: start_date/end_date (e.g., '2024-01-01' to '2024-12-31')
- Units: 'standard' (inches) or 'metric' (mm)
- Save per-station CSV files with sanitized filenames (remove special characters)
- Rate limiting: sleep(2) between station requests

**Step 5: Annual Aggregation**
- Read each station CSV
- Convert date to datetime, extract year
- Group by station and year, sum precipitation values
- Output: Annual_Total_Precip (summed daily values per year per station)

## Libraries and Tools

**Python packages:** pynhd (NLDI watershed retrieval), requests (API calls), pandas (data manipulation), geopandas (geospatial operations), shapely.geometry (Point), matplotlib (visualization), re (filename sanitization). **API:** NOAA NCEI CDO Web API v2. **Data source:** GHCND (daily precipitation, temperature, snow, etc.).

**Output products:** Watershed shapefile, station CSV files (metadata and precipitation data), PNG map visualization, annual precipitation summaries, compressed data archive (zip).

**Example parameters:** Site ID='03335000', Date range='2024-01-01' to '2024-12-31', Output folder='data_03335000', Rate limits respected with 1-2 second delays.

## Summarized attachments
- **Precipitation Access** (https://github.com/I-GUIDE/hydroewd/blob/main/prec_data/Coursepage_DA6_Precipitation_Access.ipynb, notebook): Interactive Jupyter notebook by Jibin Joseph and Venkatesh Merwade for downloading NOAA Global Historical Climatology Network Daily (GHCND) precipitation data for a watershed using USGS site number via pynhd NLDI, NOAA NCEI CDO Web API, watershed boundary retrieval and shapefile export, station discovery via API with pagination and rate limiting, filtering of active stations, precipitation data retrieval and per-station CSV export with sanitization, annual aggregation of daily precipitation values, geospatial visualization with geopandas, and handling of standard/metric unit conversions.
