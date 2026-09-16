---
title: "Jupyter NoteBook - Data Access Activities"
unit_id: 135
course_id: 0
slug: jupyter-notebook-data-access-activities
is_course: 0
---

# Jupyter NoteBook - Data Access Activities

## Fetched resources (external URLs)

### Activity 1 Student (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity1_Student.ipynb

# Activity
Choose one variable among : Mean temperature 'TAVG' , Precipitation 'PRCP' and Direction of fastest 5-second wind (degrees) 'WDF5' and use any of the following stations:
1. Station_id = GHCND:USW00023174 , LOS ANGELES INTERNATIONAL AIRPORT, CA US
2. Station_id: GHCND:USW00013874 , ATLANTA HARTSFIELD JACKSON INTERNATIONAL AIRPORT, GA US
3. Station_id : GHCND:USW00013904 , AUSTIN BERGSTROM INTERNATIONAL AIRPORT, TX US

    Note: Some stations may not have all the parameters e.g. TMIN, TMAX etc

```python
# Import libraries
import requests
import pandas as pd
#convert the response as a strcuctured json
import json
#mathematical operations on lists
import numpy as np
#parse the datetimes we get from NOAA
from datetime import datetime
```

```python
#add the access token you got from NOAA
Token = 'QEBZgOivFWhcZcxssuQKncnLcilnGFlQ'
```

```python
##You can enter any station ID 
station_id = 'GHCND:USW00023174' 
```

```python
# Creating empty lists
dates_temp = []
temp = []
```

```python
# enter year
year = str(2014)
```

```python
# enter data type
datatype= 'WDF5'
```

```python
#make the api call
r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid='+datatype+'&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
```

```python
#load the api response as a json
d = json.loads(r.text)
d
```

```python
#get all items in the response which are temperature readings
temps = [item for item in d['results'] if item['datatype']=='WDF5'] # here we can replace datatype with other available data e.g TAVG to get average temperature
temps
```

```python
#get the date field from all temperature readings
dates_temp += [item['date'] for item in temps]
dates_temp
```

```python
#get the temp value and store in the empty list
temp += [item['value'] for item in temps]
temp # these values are in tenths of celsius
```

```python
# Create an empty dataframe
df_temp = pd.DataFrame()
df_temp
```

```python
#populate date and temperature fields in the empty dataframe(cast string date to datetime and convert temperature to farenheit from tenths of celsius
df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
df_temp['Wind'] = [float(v) for v in temp] # here for each variable we will see if conversion is required or not
df_temp
```

```python
df_temp
```

### Activity 1A (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity1A.ipynb

# Downloading data(Precipitation) from NOAA using API

```python
# Import libraries
import requests
# for data manipulation and analysis
import pandas as pd
#convert the response as a strcuctured json
import json
#mathematical operations on lists
#import numpy as np
#parse the datetimes we get from NOAA
from datetime import datetime
```

```python
#add the access token you got from NOAA
Token = 'QEBZgOivFWhcZcxssuQKncnLcilnGFlQ'
```

```python
##You can enter any station ID 
station_id = 'GHCND:USW00003927' #Dallas Fort Worth Airport station
```

```python
# Creating empty lists
dates_prcp = []
prcps = []
```

```python
type(dates_prcp)
```

```python
# enter year
year = str(2014)
```

```python
# enter data type
datatype= 'PRCP' # precipitation 
```

```python
#make the api call
r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid='+datatype+'&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
```

```python
#load the api response as a json
d = json.loads(r.text)
d
```

```python
#get all items in the response which are precipitation readings
prcp = [item for item in d['results'] if item['datatype']=='PRCP'] # here we can replace datatype with other available data e.g TAVG to get average temperature
prcp
```

```python
#get the date field from all precipitation readings
dates_prcp = [item['date'] for item in prcp] 
dates_prcp
```

```python
#get the actual precipitation from all precipitation readings
prcps = [item['value'] for item in prcp]
prcps
```

```python
# Create an empty dataframe
df_prcp = pd.DataFrame()
df_prcp
```

```python
#populate date and precipitation fields in the empty dataframe(cast string date to datetime and convert precipitation to mm)
df_prcp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_prcp]
df_prcp['Precipitation(mm)'] = [(float(v)/254)*25.4 for v in prcps] #prcp is convereted to mm
```

```python
df_prcp
```

```python
#Saving dataframe as a csv file
df_prcp.to_csv('PRECIPITATION.csv', index=False)
```

# Downloading data for multiple years

```python
# Creating empty lists
dates_prcp = []
prcps = []
Token = 'QEBZgOivFWhcZcxssuQKncnLcilnGFlQ'
datatype= 'PRCP'
station_id = 'GHCND:USW00003927'
# enter year range
for year in range(2018, 2020):
    year = str(year)
    
    
    #make the api call
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid='+datatype+'&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
    #load the api response as a json
    d = json.loads(r.text)
    #get all items in the response which are precipitation readings
    prcp = [item for item in d['results'] if item['datatype']=='PRCP'] # here we can replace datatype with other available data e.g TAVG to get average temperature
    #get the date field from all precipitation readings
    dates_prcp += [item['date'] for item in prcp]
    #get the actual precipitation from all precipitation readings
    prcps += [item['value'] for item in prcp]
```

```python
# Create an empty dataframe
df_prcp = pd.DataFrame()
df_prcp
```

```python
#populate date and precipitation fields in the empty dataframe(cast string date to datetime and convert precipitation to mm)
df_prcp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_prcp]
df_prcp['Precipitation(mm)'] = [(float(v)/254)*25.4 for v in prcps] #prcp is convereted to mm
```

```python
df_prcp
```

# Different station

```python
station_id = 'GHCND:US1TXTN0030' # station in Fort Worth near Dallas
```

```python
# Creating empty lists
dates_prcp = []
prcps = []
```

```python
year = str(2014)
```

```python
datatype= 'PRCP'
```

```python
#make the api call
r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid='+datatype+'&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
```

```python
#load the api response as a json
d = json.loads(r.text)
d
```

```python
#get all items in the response which are precipitation readings
prcp = [item for item in d['results'] if item['datatype']=='PRCP'] # here we can replace datatype with other available data e.g TAVG to get average temperature
prcp
```

```python
#get the date field from all precipitation readings
dates_prcp += [item['date'] for item in prcp]
dates_prcp
```

```python
#get the actual precipitation from all precipitation readings
prcps += [item['value'] for item in prcp]
prcps
```

```python
# Create an empty dataframe
df_prcp = pd.DataFrame()
df_prcp
```

```python
#populate date and precipitation fields in the empty dataframe(cast string date to datetime)
df_prcp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_prcp]
df_prcp['Precipitation(mm)'] = [(float(v)/254)*25.4 for v in prcps] 
```

```python
df_prcp
```

```python
#Saving dataframe as a csv file
df_prcp.to_csv('PRECIPITATION_FW.csv', index=False)
```

### Activity 1B (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity1B.ipynb

# Downloading data(Temperature) from NOAA using API

```python
# Import libraries
import requests
import pandas as pd
#convert the response as a strcuctured json
import json
#mathematical operations on lists
import numpy as np
#parse the datetimes we get from NOAA
from datetime import datetime
```

```python
#add the access token you got from NOAA 
Token = 'QEBZgOivFWhcZcxssuQKncnLcilnGFlQ'
```

```python
##You can enter any station ID 
station_id = 'GHCND:USW00003927' #Dallas Fort Worth Airport station
```

```python
# Creating empty lists
dates_temp = []
temp = []
```

```python
type(dates_temp)
```

```python
# enter year
year = str(2014)
```

```python
# enter data type
datatype= 'TAVG'
```

```python
#make the api call
r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid='+datatype+'&limit=1000&stationid='+station_id+'&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
```

```python
#load the api response as a json
d = json.loads(r.text)
d
```

```python
#get all items in the response which are temperature readings
temps = [item for item in d['results'] if item['datatype']=='TAVG'] # here we can replace datatype with other available data e.g TAVG to get average temperature
temps
```

```python
#get the date field from all temperature readings
dates_temp = [item['date'] for item in temps]
dates_temp
```

```python
#get the temp value and store in the empty list
temp = [item['value'] for item in temps]
temp # these values are in tenths of celsius
```

```python
# Create an empty dataframe
df_temp = pd.DataFrame()
df_temp
```

```python
#populate date and temperature fields in the empty dataframe(cast string date to datetime and convert temperature to farenheit from tenths of celsius
df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in temp] # here for each variable we will see if conversion is required or not
df_temp
```

```python
df_temp
```

```python
#Saving dataframe as a csv file
df_temp.to_csv('Temperature.csv', index=False)
```

# Activity
Choose one variable among : Mean temperature 'TAVG' , Precipitation 'PRCP' and Direction of fastest 5-second wind (degrees) 'WDF5' and use any of the following stations:
1. Station_id = GHCND:USW00023174 , LOS ANGELES INTERNATIONAL AIRPORT, CA US
2. Station_id: GHCND:USW00013874 , ATLANTA HARTSFIELD JACKSON INTERNATIONAL AIRPORT, GA US
3. Station_id : GHCND:USW00013904 , AUSTIN BERGSTROM INTERNATIONAL AIRPORT, TX US

    Note: Some stations may not have all the parameters e.g. TMIN, TMAX etc

### Activity 2 (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity2.ipynb

# Installing dataretrieval library 
To run this script make sure to install dataretrieval using pip. Pip is a Python package manager.
When the library is installed, you may be asked to restart kernel. You can do so by clicking on 'kernel' tab and selecting 'Restart'.

```python
pip install -U dataretrieval
```

```python
# import required library 
import dataretrieval.nwis as nwis
```

# Services available from NWIS:

1. Instantaneous values (iv)
2. Daily values (dv)
3. Site info (site)
4. Discharge peaks (peaks)
5. Discharge measurements (measurements)
6. Water quality samples (qwdata)

# Parameter codes (parameterCd) :
1. Water temperature, degrees Celsius = 00010
2. Discharge, cubic feet per second = 00060
3. Gage height, feet                =00065

```python
site = '08057000' # Trinity River at Dallas, TX , url : https://waterdata.usgs.gov/tx/nwis/inventory/?site_no=08057000
# get basic info about the site (Another station_id="08075770")
df_I = nwis.get_record(sites=site, service='site')
df_I
```

# Getting daily values for the three parameters : Water temperature, Discharge and Gage height. 

```python
# get daily values (dv) , parameterCd='00010' , water temperature
site = '08057000'
df = nwis.get_record(sites=site, service='dv', start='2014-12-31', end='2016-01-01', parameterCd='00010')
df
```

```python
# get daily values (dv) , parameterCd='00060' , Discharge , radar based: https://www.usgs.gov/data/radar-based-field-measurements-surface-velocity-and-discharge-10-us-geological-survey
site = '08057000'
df1 = nwis.get_record(sites=site, service='dv', start='2014-12-31', end='2016-01-01', parameterCd='00060')
df1
```

```python
# get daily values (dv) , parameterCd='00065' , Gage height
site = '08057000'
df2 = nwis.get_record(sites=site, service='dv', start='2014-12-31', end='2016-01-01', parameterCd='00065')
df2
```

# Getting instantaneous values for the three parameters : Water temperature, Discharge and Gage height. 

```python
# get instantaneous values (iv) , parameterCd='00065' , Gage height
site = '08057000'
df3 = nwis.get_record(sites=site, service='iv', start='2014-12-31', end='2016-01-01', parameterCd='00065')
df3
```

```python
# get instantaneous values (iv) , parameterCd='00060' , Discharge
site = '08057000'
df4 = nwis.get_record(sites=site, service='iv', start='2014-12-31', end='2016-01-01', parameterCd='00060')
df4
```

```python
# get instantaneous values (iv) , parameterCd='00010' , water temperature
site = '08057000'
df5 = nwis.get_record(sites=site, service='iv', start='2014-12-31', end='2016-01-01', parameterCd='00010')
df5
```

# Getting discharge peaks. 

```python
# get discharge peaks (peaks) , these are some severe storm events 
site = '08057000'
df6 = nwis.get_record(sites=site, service='peaks', start='2012-12-31', end='2016-01-01') # no need of parameterCd
df6
```

# Getting discharge measurements. 

```python
# get discharge measurments (measurements) These are field measurements 
site = '08057000'
df7 = nwis.get_record(sites=site, service='measurements', start='2012-12-31', end='2016-01-01') # no need of parameterCd
df7
```

```python
df7.to_csv('Measurements'+'.csv')
```

# Getting water quality

```python
# get water quality (qwdata) 
site = '08057000'
df8 = nwis.get_record(sites=site, service='qwdata', start='2012-12-31', end='2016-01-01') # no need of parameterCd
df8
```

```python
# save dataframe to an excel file

FileName = site + ".csv"

df8.to_csv(FileName)
```

# Getting daily value discharge data from two different stations 

```python
# get daily values (dv) , parameterCd='00060' , Discharge
site_1 = '08057000' # Trinity_Dallas
site_2 = '08075770' #Hunting_Houston
dfn1 = nwis.get_record(sites=site_1, service='dv', start='2014-12-31', end='2016-01-01', parameterCd='00060')
dfn2 = nwis.get_record(sites=site_2, service='dv', start='2014-12-31', end='2016-01-01', parameterCd='00060')
dfn1
```

```python
dfn2
```

```python
# Making a new dataframe by joining both dataframes 
import pandas as pd
df_A= pd.concat([dfn1, dfn2], axis=1) 
```

```python
df_A
```

```python
Place1 =df_A ['00060_radar_Mean'] # Trinity_Dallas
Place2 = df_A ['00060_Mean'] #Hunting_Houston
```

```python
# Making a new column for dates by creating a new dataframe
import datetime

# Define the start and end dates
start_date = datetime.date(2014, 12, 31)
end_date = datetime.date(2016, 1, 1)

# Generate the date range
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Create a DataFrame with the date range
df_D = pd.DataFrame({'Date': date_range})

# Display the DataFrame
print(df_D)
Date = df_D['Date']
```

```python
# Plotting line graphs 
import matplotlib.pyplot as plt
plt.plot(Date, df_A ['00060_radar_Mean'] , label='Trinity_Dallas') # You can replace df_A ['00060_radar_Mean'] with Place1
plt.plot(Date, Place2, label='Hunting_Houston')
plt.legend(loc='upper left')
plt.xlabel('Time')
plt.ylabel('Discharge (cfs)')
plt.show()
```

# Activity 
Use any of the following stations and find 'peak', 'dv' and 'iv'. You will need to change service in nwis.get.record syntax to find these parameters. 
1. Station ID: 02336000 , Chattahoochee River at Atlanta, GA
2. Station ID: 07191160 , Spavinaw Creek near Maysville, AR


    Note: All the services may not be available at some stations. 

```python
# get daily values (dv) , parameterCd='00060' , Discharge
#site_1 = '02336000' # Chattahoochee River at Atlanta, GA
#dfn1 = nwis.get_record(sites=site_1, service='qwdata', start='2014-12-31', end='2016-01-01', parameterCd='00060')
#dfn1
```

```python
#site_2 = '07191160' #Spavinaw Creek near Maysville, AR
#dfn2 = nwis.get_record(sites=site_2, service='peaks', start='2014-12-31', end='2016-01-01', parameterCd='00060')
#dfn2
```

### Activity 2 students (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity_2_students.ipynb

# Activity 
Use any of the following stations and find 'peak', 'dv' and 'iv'. You will need to change service in nwis.get.record syntax to find these parameters. 
1. Station ID: 02336000 , Chattahoochee River at Atlanta, GA
2. Station ID: 07191160 , Spavinaw Creek near Maysville, AR


    Note: All the services may not be available at some stations. 

```python
# import required library 
import dataretrieval.nwis as nwis
```

```python
site = '02336000'  
# get basic info about the site (Another station_id="08075770")
df_I = nwis.get_record(sites=site, service='site')
df_I
```

```python
# get daily values (dv) , parameterCd='00060' , Discharge
site_1 = '02336000' # Chattahoochee River at Atlanta, GA
dfn1 = nwis.get_record(sites=site_1, service='qwdata', start='2014-12-31', end='2016-01-01', parameterCd='00060')
dfn1
```

```python
site_2 = '07191160' #Spavinaw Creek near Maysville, AR
dfn2 = nwis.get_record(sites=site_2, service='peaks', start='2014-12-31', end='2016-01-01', parameterCd='00060')
dfn2
```

### Activity 3 (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity3.ipynb

# Bulk download nc files (Aphrodite) Part I

# Instructions
For the sake of executing this script, username and password of the instructor has been used. You will need to create an account on https://www.chikyu.ac.jp/precip/english/ for getting authorization to access files.

```python
# Import libraries
import requests 
import numpy as np #NumPy support large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import os
```

```python
# Enter username and password
username = 'engrjunaid07@gmail.com'
password = 'XNeY9qvk'

#Username and password
#ID: engrjunaid07@gmail.com
#PW: XNeY9qvk
```

```python
# chech current working directory 
os.getcwd()
```

```python
#Script will execute and download files for all years except the last year in bracket
years = np.arange(2008,2010)
for year in years:
    url = 'http://aphrodite.st.hirosaki-u.ac.jp/product/APHRO_V1808_TEMP/APHRO_MA/025deg_nc/APHRO_MA_TAVE_025deg_V1808.'+ str(year)+ '.nc.gz'
    r = requests.get(url, auth=(username,password), allow_redirects = True)
    open(str(year)+'.gz', 'wb').write(r.content)
```

# Unzip netCDF files Part II

# Instructions:
1. You may need to install gzip library to execute this part of the script.

```python
import gzip
import os

# Path to the directory containing .gz files
directory = os.getcwd() #os.path.expanduser("~") as this function retrieves home directory

# Extension for the uncompressed files
uncompressed_extension = ".nc"  # Modify this to your desired extension

# Loop over all files in the directory
for filename in os.listdir():
    if filename.endswith(".gz"):
        file_path = os.path.join(directory, filename)
        output_path = os.path.splitext(file_path)[0] + uncompressed_extension

        # Open .gz file and create output file
        with gzip.open(file_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            f_out.write(f_in.read())

        print(f"File {filename} unzipped successfully.")

```

# Reading netCDF files Part III

# Instructions
You might need to install netCDF4 using 'pip install netCDF4' 

```python
# Import libraries
from netCDF4 import Dataset
import numpy as np
import pandas as pd 
import os
```

```python
# loading netCDF file using Dataset function of netCDF library 
data = Dataset('2008.nc')
```

```python
# Reading in the netCDF file
print(data.variables.keys())
```

```python
# Reading data
data
```

```python
# Reading data variable lat
data.variables['lat']
```

```python
# Reading data variable lon
data.variables['lon']
```

```python
# Reading data variable time
data.variables['time']
```

```python
# Reading data variable tave
data.variables['tave']
```

```python
# Storing the lat and lon data into the variables 
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
```

```python
lat
```

```python
lon
```

# Finding time series of Temperature at a point of interest Part IV

```python
# Storing the lat and lon of a place in Asia into variables 
lat_A =  33.70
lon_A =  73.10
```

```python
# Calculating squared difference of lat and lon 
diff_lat = (lat - lat_A)**2
diff_lon = (lon - lon_A)**2
```

```python
diff_lat
```

```python
# Identifying the index of the value for lat and lon 
min_index_lat = diff_lat.argmin()
min_index_lon = diff_lon.argmin()
```

```python
min_index_lat
```

```python
min_index_lon
```

```python
temp = data.variables['tave']
temp
```

```python
# Creating an empty pandas dataframe
starting_date = data.variables['time'].units[14:24]
ending_date = data.variables['time'].units[14:18] + '-12-31'
date_range = pd.date_range(start = starting_date, end = ending_date)
df = pd.DataFrame(0, columns = ['Temparature'], index = date_range)

dt = np.arange(0, data.variables['time'].size)
```

```python
data.variables['time']
```

```python
# indexing the starting data from data variable 'time'
starting_date = data.variables['time'].units[14:24]
starting_date
```

![Index.JPG](attachment:Index.JPG)

```python
# indexing the ending data from data variable 'time'
ending_date = data.variables['time'].units[14:18] + '-12-31'
ending_date
```

```python
date_range = pd.date_range(start = starting_date, end = ending_date)
date_range
```

```python
df = pd.DataFrame(0, columns = ['Temparature'], index = date_range)
df
```

```python
dt = np.arange(0, data.variables['time'].size)
dt
```

```python
time_index = 0
df.iloc[time_index] = temp[time_index,min_index_lat ,min_index_lon]
df.iloc[time_index]
```

```python
time_index = 1
df.iloc[time_index] = temp[time_index,min_index_lat ,min_index_lon]
df.iloc[time_index]
```

```python
time_index = 2
df.iloc[time_index] = temp[time_index,min_index_lat ,min_index_lon]
df.iloc[time_index]
```

```python
for time_index in dt:          #for time_index in range(365): we could use range function but leap years have 366 days
    df.iloc[time_index] = temp[time_index,min_index_lat ,min_index_lon]
```

```python
df
```

```python
# Saving the time series into a csv , temperature values are in °C
df.to_csv('temparature_2008Isb.csv')
```

### Activity 4 (notebook)
*URL:* https://github.com/PurdueCyberTraining/justiceindata/blob/main/Tuesday/DataAccess/Activity4.ipynb

# Data Access - Energy
### This Example showcases a method to add a large data set from a github repository

```python
import requests 

csv_url = "https://raw.githubusercontent.com/buds-lab/the-building-data-genome-project/master/data/raw/temp_open_utc.csv" 

response = requests.get(csv_url) 

if response.status_code == 200: 

    with open('filename.csv', 'wb') as f: 
        f.write(response.content) 
        print("File downloaded successfully.") 
else: 
    print('Failed to download file.') 

```

_output:_
```
File downloaded successfully.
```

### Data File hyperlink is needed as the csv_url.
### Github files will have a //raw. superceding the link for the actual file location. Other sites may be different.

```python
import pandas as pd
```

```python
df = pd.read_csv('filename.csv')
```

```python
df.head()
```

_result:_
```
timestamp  PrimClass_Jolie  PrimClass_Jaylin  Office_Jesus  \
0  2010-01-01 08:00:00+00:00              NaN               NaN           NaN   
1  2010-01-01 09:00:00+00:00              NaN               NaN           NaN   
2  2010-01-01 10:00:00+00:00              NaN               NaN           NaN   
3  2010-01-01 11:00:00+00:00              NaN               NaN           NaN   
4  2010-01-01 12:00:00+00:00              NaN               NaN           NaN   

   PrimClass_Jayla  PrimClass_Janiya  PrimClass_Janice  Office_Jett  \
0              NaN               NaN               NaN          NaN   
1              NaN               NaN               NaN          NaN   
2              NaN               NaN               NaN          NaN   
3              NaN               NaN               NaN          NaN   
4              NaN               NaN               NaN          NaN   

   Office_Jerry  PrimClass_Jaden  ...  UnivLab_Aine  UnivLab_Anita  \
0           NaN              NaN  ...           NaN            NaN   
1           NaN              NaN  ...           NaN            NaN   
2           NaN              NaN  ...           NaN            NaN   
3           NaN              NaN  ...           NaN            NaN   
4           NaN              NaN  ...           NaN            NaN   

   UnivLab_Alisa  UnivDorm_Adriana  UnivLab_Aoife  PrimClass_Uma  \
0            NaN               NaN            NaN            NaN   
1            NaN               NaN            NaN            NaN   
2            NaN               NaN            NaN            NaN   
3            NaN               NaN            NaN            NaN   
4            NaN               NaN            NaN            NaN   

   PrimClass_Umar  UnivDorm_Una  PrimClass_Uriah  PrimClass_Ulysses  
0             NaN           NaN              NaN                NaN  
1             NaN           NaN              NaN                NaN  
2             NaN           NaN              NaN                NaN  
3             NaN           NaN              NaN                NaN  
4             NaN           NaN              NaN                NaN  

[5 rows x 508 columns]
```

```python
df.PrimClass_Jolie.plot()
```

_result:_
```
<matplotlib.axes._subplots.AxesSubplot at 0x7f1e100ac050>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```
