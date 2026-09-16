---
title: "Data Preprocessing"
unit_id: 252
course_id: 0
level: "Foundation"
slug: data-preprocessing-
is_course: 0
---

# Data Preprocessing

## Fetched resources (external URLs)

### AI/ML Data Preprocessing (notebook)
*URL:* https://github.com/VMerwadeGroup/CyberFaCES/blob/main/AI_DataPrep/Data_prep.ipynb

```python
## required packages
import numpy as np
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import hydrofunctions as hf
import pygridmet as gridmet
from pygridmet import GridMET
from pynhd import NLDI
import requests
from io import StringIO
# used to help transform data
from sklearn import preprocessing
```

### Retrieving Site shapefile

```python
## Let's see the redults for cedar creek
site_number  = '04180000'
geometry = NLDI().get_basins(site_number).geometry.iloc[0]
```

### Get Discharge Data USGS (15 mins)

```python
## Get discharge data

START_DATE = "1988-01-01"
END_DATE = "2023-01-01"
discharge = hf.NWIS(site_number, 'iv', START_DATE,END_DATE)

discharge.get_data()

```

_output:_
```
Requested data from https://nwis.waterservices.usgs.gov/nwis/iv/?format=json%2C1.1&sites=04180000&startDT=1988-01-01&endDT=2023-01-01
```

_output:_
```
One or more datasets in this request is going to be 'upsampled' to 0 days 00:15:00 because the data were collected at a lower frequency of 0 days 01:00:00
c:\temp\envs\Hydro\Lib\site-packages\hydrofunctions\hydrofunctions.py:596: HydroUserWarning: One or more datasets in this request is going to be 'upsampled' to 0 days 00:15:00 because the data were collected at a lower frequency of 0 days 01:00:00
  warnings.warn(
c:\temp\envs\Hydro\Lib\site-packages\hydrofunctions\station.py:317: FutureWarning: It is no longer necessary to call .get_data() to request data.
  warnings.warn(
```

_result:_
```
USGS:04180000: CEDAR CREEK NEAR CEDARVILLE, IN
    00060: <Hour>  Discharge, cubic feet per second 
    00065: <15 * Minutes>  Gage height, feet 
Start: 1988-01-19 05:00:00+00:00
End:   2023-01-02 04:45:00+00:00
```

```python
# save the data as TXT and CSV and store them in the "Raw_Data" folder

raw_data = pd.DataFrame({'discharge_cfs':discharge.df().iloc[:,0],
                          'qualifiers':discharge.df().iloc[:,1]})

# raw_data.to_csv(Folder1 + "Raw_Discharge_" + site_no + ".txt")
# raw_data.to_csv(Folder1 + "Raw_Discharge_" + site_no + ".csv")

flow = pd.DataFrame(raw_data['discharge_cfs'])
```

```python
%matplotlib inline


flow.plot(figsize=(12,6))
plt.title("Discharge Hydrograph of " + site_number)
plt.legend(["Discharge"], loc='best', edgecolor='k')
plt.xlabel("Date")
plt.ylabel("Discharge (cfs)")
plt.show()
```

```python
flow
```

_result:_
```
discharge_cfs
datetimeUTC                             
1988-01-19 05:00:00+00:00          735.0
1988-01-19 05:15:00+00:00            NaN
1988-01-19 05:30:00+00:00            NaN
1988-01-19 05:45:00+00:00            NaN
1988-01-19 06:00:00+00:00          722.0
...                                  ...
2023-01-02 03:45:00+00:00            NaN
2023-01-02 04:00:00+00:00          470.0
2023-01-02 04:15:00+00:00            NaN
2023-01-02 04:30:00+00:00            NaN
2023-01-02 04:45:00+00:00            NaN

[1225632 rows x 1 columns]
```

### Daily Discharge

```python
# check the number of days between the START_DATE and END_DATE
from datetime import datetime
a = datetime.strptime(START_DATE, "%Y-%m-%d")
b = datetime.strptime(END_DATE, "%Y-%m-%d")

delta = b - a

print(delta.days + 1) # includes END_DATE
```

_output:_
```
12785
```

```python
# change to the site number of interest

siteNumber = site_number

usgs_water_data_url = "https://waterdata.usgs.gov/nwis/dv"
params = {
    "site_no": siteNumber,
    "begin_date": START_DATE,
    "end_date": END_DATE,
    "format": "rdb", # default parameter, do not change
    # 00060 - Discharge, cubic feet per second (Mean)
    "parameter_cd": "00060", # Learn more https://waterdata.usgs.gov/nwis/?tab_delimited_format_info
}

# send request
response = requests.get(usgs_water_data_url, params=params)

if response.status_code == 200:
    print("Successful Data Request! ")
else:
    print(response.status_code)
    print(response.reason)
    print("Uh-oh...something went wrong.")
```

_output:_
```
Successful Data Request!
```

```python
# split the response text into the header information and table data
header, table = response.text.split("# \n")
```

```python
print(header)
```

_output:_
```
# ---------------------------------- WARNING ----------------------------------------
# Some of the data that you have obtained from this U.S. Geological Survey database
# may not have received Director's approval. Any such data values are qualified
# as provisional and are subject to revision. Provisional data are released on the
# condition that neither the USGS nor the United States Government may be held liable
# for any damages resulting from its use.
#
# Additional info: https://waterdata.usgs.gov/provisional-data-statement/
#
# Contact:   gs-w_waterdata_support@usgs.gov
# retrieved: 2024-07-18 14:33:45 EDT       (vaww01)
#
# Data for the following 1 site(s) are contained in this file
#    USGS 04180000 CEDAR CREEK NEAR CEDARVILLE, IN
# -----------------------------------------------------------------------------------
#
# Data provided for site 04180000
#            TS   parameter     statistic     Description
#         52097       00060     00003     Discharge, cubic feet per second (Mean)
#
# Data-value qualification codes included in this output:
#     A  Approved for publication -- Processing and review completed.
#     e  Value has been estimated.
```

```python
# Read the data into a DataFrame, skipping the first two lines
df = pd.read_csv(StringIO(table), sep="\t", skiprows=2, header=None)

# Drop any completely empty columns that might have been incorrectly parsed
df.dropna(how='all', axis=1, inplace=True)

# Define the column names
df.columns = ["agency", "site", "datetime", "discharge", "quality"]

# Print the dimensions and the first few rows of the DataFrame
print(f"Table dimensions: {df.shape}")
print(df.head())
```

_output:_
```
Table dimensions: (12785, 5)
  agency     site    datetime  discharge quality
0   USGS  4180000  1988-01-01      210.0       A
1   USGS  4180000  1988-01-02      200.0       A
2   USGS  4180000  1988-01-03      180.0       A
3   USGS  4180000  1988-01-04      160.0       A
4   USGS  4180000  1988-01-05      120.0       A
```

```python
## Filtering and final discharge

df = df.filter(["datetime", "discharge"], axis=1)
df["discharge"] = df["discharge"].astype(float) * 0.0283168 # convert to m^3/s
df.index = pd.to_datetime(df["datetime"])
df.drop("datetime", axis=1, inplace=True)
df
```

_result:_
```
discharge
datetime             
1988-01-01   5.946528
1988-01-02   5.663360
1988-01-03   5.097024
1988-01-04   4.530688
1988-01-05   3.398016
...               ...
2022-12-28   1.769800
2022-12-29   1.891562
2022-12-30   3.058214
2022-12-31  21.605718
2023-01-01  18.207702

[12785 rows x 1 columns]
```

### Gridmet Data

```python
GridMET().gridmet_table
```

_result:_
```
variable    abbr  \
0                            Precipitation      pr   
1                Maximum Relative Humidity    rmax   
2                Minimum Relative Humidity    rmin   
3                        Specific Humidity     sph   
4                        Surface Radiation    srad   
5                           Wind Direction      th   
6                  Minimum Air Temperature    tmmn   
7                  Maximum Air Temperature    tmmx   
8                               Wind Speed      vs   
9                            Burning Index      bi   
10                  Fuel Moisture (100-hr)   fm100   
11                 Fuel Moisture (1000-hr)  fm1000   
12                Energy Release Component     erc   
13  Reference Evapotranspiration (Alfalfa)     etr   
14    Reference Evapotranspiration (Grass)     pet   
15                  Vapor Pressure Deficit     vpd   

                                          long_name  \
0                              precipitation_amount   
1                   daily_maximum_relative_humidity   
2                   daily_minimum_relative_humidity   
3                      daily_mean_specific_humidity   
4         daily_mean_shortwave_radiation_at_surface   
5                         daily_mean_wind_direction   
6                         daily_minimum_temperature   
7                         daily_maximum_temperature   
8                             daily_mean_wind_speed   
9                        daily_mean_burning_index_g   
10                         dead_fuel_moisture_100hr   
11                        dead_fuel_moisture_1000hr   
12            daily_mean_energy_release_component-g   
13  daily_mean_reference_evapotranspiration_alfalfa   
14    daily_mean_reference_evapotranspiration_grass   
15                daily_mean_vapor_pressure_deficit   

                           units  
0                             mm  
1                              %  
2                              %  
3                          kg/kg  
4                           W/m2  
5   Degrees clockwise from north  
6                              K  
7                              K  
8                            m/s  
9                              -  
10                             %  
11                             %  
12                             -  
13                            mm  
14                            mm  
15                           kPa
```

```python
### get the data
dates = (START_DATE, END_DATE)
daily = gridmet.get_bygeom(geometry, dates, variables=["pr", "rmax","rmin","tmmn","tmmx","vs","pet"])
```

```python
# Visualization
ax = daily.where(daily.pr > 0).pet.plot(x="lon", y="lat", row="time", col_wrap=3)
#ax.fig.savefig(Path("_static", "gridmet_grid.png"), facecolor="w", bbox_inches="tight")
```

```python
daily
```

_result:_
```
<xarray.Dataset> Size: 39MB
Dimensions:      (time: 12776, lat: 10, lon: 11)
Coordinates:
  * time         (time) datetime64[ns] 102kB 1988-01-01 ... 2023-01-01
  * lat          (lat) float64 80B 41.61 41.57 41.53 41.48 ... 41.32 41.28 41.23
  * lon          (lon) float64 88B -85.31 -85.27 -85.22 ... -84.97 -84.93 -84.89
    spatial_ref  int32 4B 0
Data variables:
    pr           (time, lat, lon) float32 6MB nan nan nan nan ... nan nan nan
    rmax         (time, lat, lon) float32 6MB nan nan nan nan ... nan nan nan
    rmin         (time, lat, lon) float32 6MB nan nan nan nan ... nan nan nan
    tmmn         (time, lat, lon) float32 6MB nan nan nan nan ... nan nan nan
    tmmx         (time, lat, lon) float32 6MB nan nan nan nan ... nan nan nan
    vs           (time, lat, lon) float32 6MB nan nan nan nan ... nan nan nan
    pet          (time, lat, lon) float32 6MB nan nan nan nan ... nan nan nan
Attributes: (12/20)
    geospatial_bounds_crs:      EPSG:4326
    Conventions:                CF-1.0
    geospatial_bounds:          POLYGON((-124.7666666333333 49.40000000000000...
    geospatial_lat_min:         41.19166666666667
    geospatial_lat_max:         41.60833333333334
    geospatial_lon_min:         -85.34999996666667
    ...                         ...
    note1:                      The projection information for this file is: ...
    note2:                      Citation: Abatzoglou, J.T., 2013, Development...
    note3:                      Data in slices after last_permanent_slice (1-...
    note4:                      Data in slices after last_provisional_slice (...
    note5:                      Days correspond approximately to calendar day...
    History:                    Translated to CF-1.0 Conventions by Netcdf-Ja...
```

```python
# Convert the dataset to a DataFrame
daily_df = daily.to_dataframe().reset_index()

# Display the resulting DataFrame
daily_df.head()
```

_result:_
```
time        lat        lon  pr  rmax  rmin  tmmn  tmmx  vs  pet  \
0 1988-01-01  41.608333 -85.308333 NaN   NaN   NaN   NaN   NaN NaN  NaN   
1 1988-01-01  41.608333 -85.266667 NaN   NaN   NaN   NaN   NaN NaN  NaN   
2 1988-01-01  41.608333 -85.225000 NaN   NaN   NaN   NaN   NaN NaN  NaN   
3 1988-01-01  41.608333 -85.183333 NaN   NaN   NaN   NaN   NaN NaN  NaN   
4 1988-01-01  41.608333 -85.141667 NaN   NaN   NaN   NaN   NaN NaN  NaN   

   spatial_ref  
0            0  
1            0  
2            0  
3            0  
4            0
```

```python
# Group by the 'time' column and calculate the mean for each group
aggregated_df = daily_df.groupby(by="time").agg({
    "pr": "mean",
    "rmax": "mean",
    "rmin": "mean",
    "tmmn": "mean",
    "tmmx": "mean",
    "vs": "mean",
    "pet": "mean"
}).reset_index()

# Convert the 'time' column to datetime and set it as the index
aggregated_df['time'] = pd.to_datetime(aggregated_df['time'])
aggregated_df.set_index('time', inplace=True)
aggregated_df.index.name = "datetime"

# Display the shape and head of the DataFrame
print(aggregated_df.shape)
aggregated_df.head()
```

_output:_
```
(12776, 7)
```

_result:_
```
pr       rmax       rmin        tmmn        tmmx        vs  \
datetime                                                                  
1988-01-01  0.0  80.104080  38.022449  259.765320  268.838776  6.828571   
1988-01-02  0.0  71.246941  30.116325  257.908173  269.997955  4.795918   
1988-01-03  0.0  70.048981  25.981632  263.012238  274.977570  4.383674   
1988-01-04  0.0  78.636734  26.330612  255.655090  271.171448  8.838776   
1988-01-05  0.0  70.534691  35.285713  253.540817  259.259186  7.338776   

                 pet  
datetime              
1988-01-01  1.036735  
1988-01-02  0.989796  
1988-01-03  1.253061  
1988-01-04  1.253061  
1988-01-05  0.504082
```

```python
## Concatenate all of the data

model_df = pd.concat([df, aggregated_df], axis=1)
#model_df.dropna(inplace=True)

print(model_df.shape)

model_df.head()
```

_output:_
```
(12785, 8)
```

_result:_
```
discharge   pr       rmax       rmin        tmmn        tmmx  \
datetime                                                                   
1988-01-01   5.946528  0.0  80.104080  38.022449  259.765320  268.838776   
1988-01-02   5.663360  0.0  71.246941  30.116325  257.908173  269.997955   
1988-01-03   5.097024  0.0  70.048981  25.981632  263.012238  274.977570   
1988-01-04   4.530688  0.0  78.636734  26.330612  255.655090  271.171448   
1988-01-05   3.398016  0.0  70.534691  35.285713  253.540817  259.259186   

                  vs       pet  
datetime                        
1988-01-01  6.828571  1.036735  
1988-01-02  4.795918  0.989796  
1988-01-03  4.383674  1.253061  
1988-01-04  8.838776  1.253061  
1988-01-05  7.338776  0.504082
```

```python
# Export the DataFrame to a CSV file
model_df.to_csv('model_df.csv')


```
