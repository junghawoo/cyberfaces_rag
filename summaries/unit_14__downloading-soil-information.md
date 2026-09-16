---
title: "Downloading soil information from Gridded Soil Survey Geographic Database (gSSURGO)"
unit_id: 14
course_id: 4
level: "Foundation"
slug: downloading-soil-information
is_course: 0
---

# Downloading soil information from Gridded Soil Survey Geographic Database (gSSURGO)

## Image text (OCR)

### `FAIR_data_principles.jpg`
Bee J \ccessible —

R
oy
%

e

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA3-NCDC_Rainfall/Coursepage_DA3_Download_NCDC_Rainfall.ipynb

Import the Libraries: cdo_api_py, pandas, datetime.

Get token from NOAA website before running the code (https://www.ncdc.noaa.gov/cdo-web/token)

```python
from cdo_api_py import Client
import pandas as pd
from datetime import datetime
token = "<Your Token>"# be sure not to share your token publicly
# Client helps you access the NCDC database with your token
my_client = Client(token, default_units="None", default_limit=1000)
```

```python
# input of start date, end date, type of dataset, and name of gauge
# get start and end date (YYYY/MM/DD) by function datetime(YYYY,MM,DD)
startdate = datetime(2012, 1, 1)
enddate   = datetime(2012, 6, 30)
# type of download dataset: hourly precipitation
# Use pprint(my_client.list_datasets()) to check what kind of datasetid you want to use
datasetid = "PRECIP_HLY" 
gauge_id  = "COOP:180700" 
```

Download Precipitation of a specific station

```python
"""
The get_data_by_station function returns the dataframe containing the precipitation dataset you request.
"""
Rainfall_data = my_client.get_data_by_station(datasetid=datasetid, stationid=gauge_id,
                startdate=startdate, enddate=enddate, return_dataframe=True,
                include_station_meta=True) 

# show the first 10 rows of DataFrame
# HPCP unit:1/100 inch (standard)
print(Rainfall_data.head(10)) 

# write the dataframe into the .csv file by to_csv function with the filename
filename = datasetid +"_"+ gauge_id +".csv"
Rainfall_data.to_csv(filename)
```

The extend is the lat, long of the target region. The gauge stations in that region would be read.
The data type is demanded and different datatype could be found in the category of NOAA data.

```python
#The extend is the lat, long of the target region.
extent = {"north": 39.14, "south": 38.68,
          "east": -74.65, "west": -77.35}

# input of start date, end date, type of dataset, and name of gauge
startdate = datetime(2012, 1, 1)
enddate = datetime(2012, 6, 30)
datasetid="PRECIP_HLY" 
```

Find the stations in the target region.

```python
"""
The find_stations function returns the dataframe containing stations' info within the input extent.
"""
stations = my_client.find_stations(
            datasetid=datasetid,
            extent=extent,
            startdate=startdate,
            enddate=enddate,
            return_dataframe=True)
print(stations)
```

Write a loop to download precipitation data from stations in the target region

## Summarized attachments

- **FAIR_data_principles.jpg** (`FAIR_data_principles.jpg`, image): Image file with OCR-extracted text that appears garbled or incomplete. No meaningful machine-readable content extracted.
- **Jupyter Notebook Exercise** (`https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA3-NCDC_Rainfall/Coursepage_DA3_Download_NCDC_Rainfall.ipynb`, notebook): Jupyter notebook demonstrating NOAA climate data download workflow using cdo_api_py, pandas, and datetime libraries. Covers accessing NCDC database with authentication token, specifying date ranges and precipitation dataset types (PRECIP_HLY), downloading precipitation data from specific gauge stations with metadata, and finding stations within geographic extent (latitude/longitude bounds) and exporting to CSV format.
