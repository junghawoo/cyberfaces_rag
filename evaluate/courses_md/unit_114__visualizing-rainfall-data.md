---
title: "Visualizing rainfall data"
unit_id: 114
course_id: 4
level: "Foundation"
slug: visualizing-rainfall-data
is_course: 0
---

# Visualizing rainfall data

## Extracted resources (local files)

### NCDC Visualization
*Source file:* `NCDC_Visualization.pdf`  ·  *type:* file

FAIR SCIENCE – Data Visualization Module 
Visualizing Spatial Distributed Precipitation Data 
Prepared by Pin-Ching Li, Sayan Dey and Venkatesh Merwade  
Lyles School of Civil Engineering, Purdue University 
vmerwade@purdue.edu 
1. INTRODUCTION 
Precipitation observation varies in a large study area due to climatological and meteorological 
phenomena. In addition, precipitation measured by gage stations nearby can be significantly 
different. Visualization of precipitation data gives us a better understanding of spatial pattern of 
rainfall. Data mapping of precipitation shows the spatial pattern of rainfall and possible 
inconsistency between data points. 
This tutorial aims to visualize maximum daily precipitation in Indiana in 2019. Precipitation 
datasets are downloaded from National Climate Data Center (NCDC). The procedure for 
downloading precipitation dataset was introduced in previous tutorial: Accessing and 
Downloading Precipitation Data from NCDC database. Students will learn how to visualize the 
spatial distributed dataset with color mapping and changing marker size by statistics values of 
precipitation.  
2. COMPUTER REQUIREMENTS 
A web browser is required for this tutorial with good internet connection and login credentials for 
an account on www.mygeohub.org.  
3. DATA REQUIREMENTS 
Student needs a login token for accessing NCDC database (described in previous tutorial: 
Accessing and Downloading Precipitation Data from NCDC database). A jupyter notebook file, 
NCDC_Visualization.ipynb, is provided to you for this exercise.

4. GETTING STARTED 
Until now you have learned how to write code to download NCDC precipitation data. In this 
tutorial, we download daily precipitation data for the entire Indiana state in 2019. After the 
dataframe of precipitation dataset is obtained, visualize them on the map with lat, long. 
The major steps of visualizing precipitation dataset are as follows: 
1. Get station numbers of multiple stations with enough data coverage 
2. Download precipitation data for multiple stations in a study area 
3. Visualize precipitation statistics with color mapping and marker size changing 
4.1 Get station numbers of multiple stations with enough data coverage 
NCDC’s Climate Data Online (CDO) web services require an access token before users use their 
API. The detail steps to get your token are recorded in the previous tutorial: Accessing and 
Downloading Precipitation Data from NCDC database. Once you get the token, you can access 
the NCDC database by Client instance. Import the following modules: Client in cdo_api_py for 
access to NCDC database, pandas for storing dataset in a dataframe and datetime for working with 
datetime objects.  
 
The get_data_by_station() function in Client is applied to download NCDC data. It requires the 
following inputs: start date, end date, dataset type, and gauge ID. The datetime function in datetime 
module creates the datetime object of the start date and end date. The datasetid is set to be 
“GHCND” for accessing daily weather datasets. To download precipitation data for multiple 
stations in a study area, we create a square-shaped window called extent which has the latitude - 
longitude coordinates of the study area’s boundary. Students need to accomplish this part 
themselves to generate a dataframe containing information of stations within the extent by 
find_stations() function in Client. The extent of region is "north": 41.76, "south": 37.8, "east": -
84.81, and "west": -88.03. The first 10 rows of dataframe are shown as below.

find_stations() will generate all the stations with observations within the given max and min date. 
Therefore, there are some stations without enough length of observation period. For example, the 
station in 8th row of the station dataframe has maximum date 07/13/2019, which is lower than the 
given maximum date 12/31/2019. Stations without enough length of observation period are 
eliminated from the list of stations to be downloaded.  
A for-loop is created to collect the indexes of stations without enough length of observation. The 
data type of maximum date and minimum date are string. In order to change the date from string 
to datetime, the datetime.strptime() function is applied to transfer them into datetime object. If the 
station has minimum date larger than 01/01/2019 or maximum date smaller than 12/31/2019, it 
would be eliminated from downloading list. Subtract the maximum and minimum date of stations 
from the given maximum and minimum date to determine if the stations can stay in the 
downloading list or not.

It is necessary to drop stations with low datacoverage (less than 0.95). After cleaning up the list of 
stations, stations in other states need to be purged. Finally, we get the list of stations in Indiana 
with enough quality of precipitation data for get_data_by_station() function in Client for 
downloading. 
 
The first 15 rows of stations_IN are shown below.

4.2 Download precipitation data for multiple stations in the study area 
get_data_by_station() function download precipitation dataset from each NCDC weather station 
in a pandas dataframe. There are 153 NCDC weather stations with sufficient precipitation data in 
Indiana. The dataframes of all stations are merged into a dataframe for visualization. 
 
4.3 Visualize maximum precipitation with color mapping and marker size changing 
In this step, color mapping and marker size according to maximum precipitation are added to the 
scatter plots of NCDC stations across the Indiana. The maximum precipitation of each gage station 
is obtained by applying describe function of pandas. Spatial information of stations is appended to 
Describe_IN for mapping. The geographic coordinate system (lat, long) is used to locate the 
weather stations.

A scatter plot with color mapping is applied to present the spatial distribution of maximum 
precipitation.  
 
There is an outlier which has significantly high value with respect to nearby station. It is hard to 
get the spatial pattern of maximum precipitation in Indiana. Therefore, we have to eliminate this 
point for visualization purpose. 
Get rid of the outlier and draw the scatter plot again with cmap =’jet’. Then, you will get the scatter 
plot shown below. This plot gives us a better understanding of distribution of maximum 
precipitation.

Changing marker size with values is a different way to visualize maximum precipitation. Five to 
the power of maximum precipitation normalized with mean precipitation is set to decide the size 
of data point (the formula of marker size can be adjusted for a better presentation of different 
variable). 
 
Homework: 
Create a scatter plot of NCDC stations in Indiana with color mapping and marker size of mean and 
standard deviation of precipitation datasets in 2018.

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DV1/Visualization_NCDC.ipynb

## NCDC Spatial Distribution

In previous tutorial, students can access NCDC weather data by cdo_api_py module. We learned how to download precipitation data within a given extent boundary. 


In this tutorial, the statistics of NCDC daily precipitation data is presented by color mapping and changing marker size across the whole Indiana.  


```python
from cdo_api_py import Client
import pandas as pd
import datetime
# token for accessing the NCDC server
token = "<Your Token>"# be sure not to share your token publicly
# Client helps you access the NCDC database with your token
my_client = Client(token, default_units="None", default_limit=1000)
```

## Get raw dataframe of Stations in Indiana

Use the function learned in previous tutorial to download multiple stations in the give extent

```python
# write your code to get stations in the given extent in tutorial
```

## Clean Precipitation Dataset
There are hundreds NCDC weather stations in Indiana. However, many stations have low datacoverage. 

Our task in this part is to keep the dataset with sufficient observation (>95% datacoverage). Our list of stations contains stations in other state. Therefore, we have to get rid of those stations as well.

```python
dropind = []
# Drop station without enough date of observation
for i in range(len(stations.maxdate)):
    # get max and min date of each station
    date_str = stations.maxdate[i]
    date_str_min= stations.mindate[i]
    # transfer string to datetime
    datelast = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    datefirst= datetime.datetime.strptime(date_str_min, '%Y-%m-%d')
    # get the position of stations with insufficient daily data
    if datelast-enddate < datetime.timedelta(days=0):
        dropind.append(i)
    elif datefirst-startdate > datetime.timedelta(days=0):
        dropind.append(i)        
# delete stations without enough time length
stations = stations.drop(stations.index[dropind])
stations_raw= stations

# Get names of indexes for which datacoverage less than 0.95
indexNames = stations[ stations['datacoverage'] < 0.95 ].index
# Delete these row indexes from dataFrame
stations.drop(indexNames , inplace=True)

# other gages with available data less than 0.95
# this list can be obtained after downloading all the datasets  
Insuff_gage = ['GHCND:US1INBN0010', 'GHCND:US1INBW0010',
                 'GHCND:US1INCW0003', 'GHCND:US1INLK0046',
                 'GHCND:US1INMN0007', 'GHCND:US1INMT0001',
                 'GHCND:US1INPS0001', 'GHCND:US1KYBT0001',
                 'GHCND:USC00116558', 'GHCND:USC00121873',
                 'GHCND:USC00122041', 'GHCND:USC00124244',
                 'GHCND:USC00126801']
# get rid of the stations in list above
# Get the final station list for downloading
stations_IN = stations[~stations['id'].isin(Insuff_gage)]
# get rid of the stations in other states
other_state = []
for i in stations_IN.index:
    if stations_IN['name'][i][-5:] != 'IN US':
        other_state.append(i)
stations_IN.drop(other_state , inplace=True)
# list first 20 stations to see if there is something wrong in the dataframe
stations_IN.head(20)
```

```python
# Get data from the NCDC client
i = 0
for rowid, station in stations_IN.iterrows(): 
    # try downloading due to some unaccessible sites of database
    try:
        station_data = my_client.get_data_by_station(
                        datasetid=datasetid,
                        stationid=station['id'],
                        startdate=startdate,
                        enddate=enddate,
                        return_dataframe=True,
                        include_station_meta=True)
        # set datetime to index
        station_data.set_index(pd.to_datetime(station_data['date']), inplace =True)
        # Drop all rows except for rainfall
        Rainfall_day = station_data.filter(['PRCP'])
        Rainfall_day = Rainfall_day.rename(columns={"PRCP": station['id']})
        # Merge the dataframe of rainfall from each station
        if i ==0:
            merged= Rainfall_day
        else:
            merged =pd.merge(merged,Rainfall_day ,how='outer', left_index=True, right_index=True)
        i +=1
    # print the id of broken dataset
    except:
        print(station['id'])
# The unit of rainfall is tenth of mm
# Get the final rainfall dataset
GHCN_IN  = merged
```

## Visualization of maximum precipitation

Use describe function to generate statistics of precipiation dataset. 

Drop the nan value of Describe_IN after append lat, long of stations to get a clean dataframe.

```python
import matplotlib.pyplot as plt
%matplotlib inline
# There is a simple way to get statistics of dataframe 
Describe_IN = GHCN_IN.describe()
Describe_IN
# get lat, long values from stations dataframe
stations_lat = stations.pivot(columns='id', index = 'elevationUnit', values='latitude')
stations_long= stations.pivot(columns='id', index = 'elevationUnit', values='longitude')
# rename the index from meter to latitude and longitude
lat_IN  = stations_lat.rename(index={'METERS': 'latitude'})
long_IN = stations_long.rename(index={'METERS': 'longitude'})
# append lat, long dataframe to the statistics of all stations
Describe_IN = Describe_IN.append(lat_IN)
Describe_IN = Describe_IN.append(long_IN)
# show the statistics of stations in Indiana
Describe_IN = Describe_IN.T
Describe_IN = Describe_IN.dropna()
```

## Color Mapping
Color mapping maximum precipitation can have different color bar. In this script, 'jet' is the main cmap label and is the classic color bar from matlab.

```python
# set up the font size
plt.rcParams.update({'font.size': 15})
# create scatter plot of precipitation with color mapping of maximum values
fig, ax = plt.subplots()
Describe_IN.plot(kind="scatter", x="longitude", y="latitude", c='max', cmap="viridis",title='Max Precipitation in Indiana 2019', ax=ax)
plt.show()
```

```python
# write your code to get rid of the outlier and draw the scatter plot with color mapping of maximum precipitation
```

## Marker Size
Apply marker size to the maximum precipitation values. 

The formula of marker size can be changed to linear or exponential. It all depends on how you want to present your data.

```python
plt.rcParams.update({'font.size': 15})
Max_less = Describe_IN[Describe_IN['max']<2000]
# set up the size of maximum precipitation value
# we choose power of 5 to show a more obvious difference between data points
# remove the outlier
s = [5**(Max_less['max'][i]/Max_less['max'].mean()*2) for i in range(Max_less.shape[0])]
Max_less.plot(kind="scatter", x="longitude", y="latitude", s=s,title='Max Precipitation in Indiana 2019')
plt.show()
```

```python
# check the stations shows much larger maximum among others
Describe_IN[Describe_IN['max']>2000]
```
