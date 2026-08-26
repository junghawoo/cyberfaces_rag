---
title: "Downloading hourly gauge precipitation from National Climate Data Center (NCDC)"
unit_id: 11
course_id: 4
level: "Developer"
slug: downloading-hourly
is_course: 0
---

# Downloading hourly gauge precipitation from National Climate Data Center (NCDC)

## Extracted resources (local files)

### Accessing and Downloading Precipitation Data from NCDC database
*Source file:* `Accessing_and_Downloading_Precipitation_Data_from_NCDC_database.pdf`  ·  *type:* file

FAIR SCIENCE – Data Access Module #3 
Accessing and Downloading Precipitation Data from NCDC database 
Prepared by Pin-Ching Li, Sayan Dey and Venkatesh Merwade  
Lyles School of Civil Engineering, Purdue University 
vmerwade@purdue.edu 
1. INTRODUCTION 
Precipitation data is one of the most important datasets for hydrologic modeling. Traditionally, 
precipitation is measured by rain gauges. In the Unites States, rainfall data is collected by National 
Oceanic and Atmospheric Administration (NOAA) and is available to be downloaded on National 
Climate Data Center (NCDC).  
This tutorial aims to automatically download hourly precipitation datasets from. Students will learn 
how to access NCDC weather database and download relevant weather datasets by cdo-api-py 
python module. The procedure of downloading precipitation dataset for individual station is 
introduced. The further instruction will guide students to download precipitation datasets of 
stations within a study area. Although this tutorial focuses on precipitation datasets, other weather 
datasets in NCDC database, such as, temperature, soil temperature, and snowfall, can also be 
downloaded by going through the same procedure.  
2. COMPUTER REQUIREMENTS 
A web browser is required for this tutorial with good internet connection and login credentials for 
an account on www.mygeohub.org.  
3. DATA REQUIREMENTS 
There are two ways to download precipitation data from NCDC: (i) by providing station ID, or (ii) 
by applying the extents of study area. Precipitation dataset of specific gage can be downloaded by 
its station id. To download precipitation datasets of multiple rain gages within a study area, the 
latitude-longitude boundary of your study area is needed. 
Student needs a login token for accessing NCDC database (described in section 4.1). A jupyter 
notebook file, Download_NCDC_Rainfall.ipynb, is provided to you for this exercise.

4. GETTING STARTED 
Two methods of downloading precipitation data are demonstrated in this tutorial. First, a method 
of downloading precipitation data of a specific station is introduced. Then, precipitation data for 
all gauges within a boundary are downloaded.  
The major steps of downloading precipitation dataset are as follows: 
1. Generate access token for access to NCDC database 
2. Import the modules for downloading and storing dataset 
3. Download precipitation data by inputting a specific station number 
4. Download precipitation data for multiple stations in a study area 
4.1 Generate access token for access to NCDC database 
NCDC’s Climate Data Online (CDO) web services requires the user (python client) to provide an 
access token before using their API. Each token is limited to five requests per second and 10,000 
requests per day. First, get your token by entering your email address on the website: 
https://www.ncdc.noaa.gov/cdo-web/token. Your token will then be sent to your email address. 
Because your token is associated with your email address, it is recommended that you do not share 
your token publicly.

4.2 Import the modules for downloading and storing dataset 
Import the following modules: Client in cdo_api_py module for access to NCDC database, pandas 
module for storing dataset in a dataframe and datetime for working with datetime objects. Once 
you get the token, you can access the NCDC database by Client instance. 
 
4.3. Download precipitation data by inputting a specific station number 
The get_data_by_station function in Client is used to download NCDC data. It requires the 
following inputs: start date, end date, dataset type, and gauge ID. The datetime function is applied 
to convert the start date and end date from integers to the standard datetime format: yyyy-mm-dd 
hh:mm:ss. To download hourly precipitation dataset, the dataset type is set to be “PRECIP-HLY”. 
We are using gauge with ID “COOP:180700” as an example. 
The precipitation data returned by the function: get_data_by_station is stored in a pandas 
dataframe (Rainfall_data). This dataframe is written as a .csv file in our current folder (the folder 
where the jupyter notebook file is saved).

In a separate tab in your browser, navigate to your current folder. You will find a csv file named 
“PRECIP_HLY_COOP:180700.csv”. Click on the .csv file to view its content. It should look like 
the following figure: 
 
4.4. Download precipitation data for multiple stations in a study area 
To download precipitation data for multiple stations in a study area, you have to create a square-
shaped window with the latitude - longitude coordinates of the study area’s boundary. This window 
is fed into the find_stations function in Client to get the gauge ID of all stations located within that 
window. The process of downloading data for individual stations is similar to what we did in 
section 4.3. You need to call the get_data_by_station function for each station found by the 
find_stations function.

Function find_stations returns a dataframe containing the following information: ID, datacoverage, 
elevation, elevationUnit, latitude, longitude, maxdate, mindate, and name as figure shown below: 
 
The “id” of each gage is fed to function get_data_by_station to download precipitation dataset. 
 
Exercise: Download precipitation datasets from all gauges within the given extent in 4.4. Save 
these datasets as .csv files. 
Hint: Create a for loop to get gage’s “id” from stations created in last step. 
 
Homework: 
Plot the depth of monthly and daily streamflow of the USGS gage 03335500 Wabash at Lafayette, 
IN. At the same graph, plot the depth of monthly and daily precipitation of the watershed 
(Hydrologic Unit 05120108) which has an outlet point at USGS 03335500.

## Image text (OCR)

### `FAIR_data_principles.jpg`
Bee J \ccessible —

R
oy
%

e

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA2/Coursepage_DA2_Download_NCDC_Rainfall.ipynb

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
