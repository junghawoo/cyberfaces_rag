---
title: "Accessing NOAA precipitation data using shapefile"
unit_id: 273
course_id: 0
level: "Foundation"
slug: accessing-noaa-precipitation-data-using-shapefile
is_course: 0
---

# Accessing NOAA precipitation data using shapefile

## Fetched resources (external URLs)

### Precipitation Access (notebook)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/main/prec_data/Coursepage_DA6_Precipitation_Access.ipynb

## <span style="color:green"><h1><center>Downloading NOAA Precipitation for a Watershed </center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


```python
from pynhd import NLDI
import os
#from pygeohydro import NWIS
import requests
import pandas as pd
import time
import re
```

```python
## USGS Site Number
site_id='03335000'

# Date range for the precipitation data
start_date = '2024-01-01'
end_date = '2024-12-31'

watershed=NLDI().get_basins(site_id,fsource='nwissite')
extents_basin=watershed.total_bounds
print(extents_basin)
## Adding site_id to geodataframe
watershed["site_id"]=site_id

## Adding other details
#nwis = NWIS()
#site_info = nwis.get_info({"site": site_id}, expanded=True)


#watershed["site_nm"] = site_info["station_nm"].iloc[0]
#watershed["site_lon"] = site_info["dec_long_va"].iloc[0]  
#watershed["site_lat"] = site_info["dec_lat_va"].iloc[0]
#watershed["dr_ar_sqmi"]=site_info["drain_area_va"].iloc[0]
#watershed["hcdn_2009"]=site_info["hcdn_2009"].iloc[0]

print(watershed.head())
print(watershed.columns)

watershed.plot()

# Output folder for CSVs
folder_output = f'data_{site_id}'
os.makedirs(folder_output, exist_ok=True)
shapefile_fileloc_filename=f"./{folder_output}/shape_{site_id}.shp"
watershed.to_file(filename=shapefile_fileloc_filename,
                 driver="ESRI Shapefile",
                 mode="w")
```

```python
# Calculate centroids for each geometry
watershed['centroid'] = watershed.geometry.centroid

# Show result
print(watershed[['geometry', 'centroid']])

```

```python
# NOAA API token (get yours here: https://www.ncdc.noaa.gov/cdo-web/token)
API_TOKEN = 'BzJUVDNQCXcethBKDLveceOBxuaTHfxq'

# Define bounding box (minlon, minlat, maxlon, maxlat)
#bbox = [-125, 30, -65, 50]  # Example: USA lower 48 states
bbox = extents_basin

# Define request headers
headers = {'token': API_TOKEN}

# Base URL for NOAA NCEI API stations endpoint
base_url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/stations'

# Parameters for the request
params = {
    'datasetid': 'GHCND',         # Global Historical Climatology Network - Daily
    'extent': f'{bbox[1]},{bbox[0]},{bbox[3]},{bbox[2]}',  # lat1, lon1, lat2, lon2
    'limit': 1000,                # Max records per request
    'offset': 1,                  # Start offset
}

all_stations = []
page = 1

while True:
    print(f'Fetching page {page} with offset {params["offset"]}...')

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print(f'Error: {response.status_code} - {response.text}')
        break

    data = response.json()

    # Check if there are results
    if 'results' not in data or not data['results']:
        print('No more stations to fetch.')
        break

    all_stations.extend(data['results'])

    # Pagination: increase offset by limit
    params['offset'] += params['limit']
    page += 1

    # NOAA rate limits: be kind
    time.sleep(1)

# Convert results to pandas DataFrame
df = pd.DataFrame(all_stations)

# Select desired columns (if they exist)
selected_columns = ['id', 'name', 'latitude', 'longitude', 'elevation', 'mindate', 'maxdate']
df_selected = df[selected_columns].copy()

# Rename columns if you want
df_selected.rename(columns={
    'id': 'Station ID',
    'latitude': 'Station_Lat',
    'longitude': 'Station_Lon',
    'mindate': 'Start Date',
    'maxdate': 'End Date',
    'elevation': 'Elevation'
}, inplace=True)

# Display and save
print(df_selected.head())

df_selected.to_csv(f"./{folder_output}/noaa_all_stations.csv", index=False)

print(f'Download complete: {len(df_selected)} stations saved to noaa_all_stations.csv in {folder_output} folder')

```

```python
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
# Convert to pandas DataFrame first
#df = pd.DataFrame(all_stations)

# Create a geometry column from Station_Lon and Station_Lat
geometry = [Point(xy) for xy in zip(df_selected['Station_Lon'], df_selected['Station_Lat'])]

# Create GeoDataFrame
gdf_all = gpd.GeoDataFrame(df_selected, geometry=geometry)

# Set a CRS (Coordinate Reference System), assuming WGS84 (EPSG:4326)
gdf_all.set_crs(epsg=4326, inplace=True)

# Show the GeoDataFrame
print(len(gdf_all))
print(gdf_all.head())



df_active=df_selected[df_selected['End Date']>=end_date]
df_active.to_csv(f"./{folder_output}/noaa_active_stations.csv", index=False)
# Create a geometry column from Station_Lon and Station_Lat
geometry = [Point(xy) for xy in zip(df_active['Station_Lon'], df_active['Station_Lat'])]

# Create GeoDataFrame
gdf_active = gpd.GeoDataFrame(df_active, geometry=geometry)

# Set a CRS (Coordinate Reference System), assuming WGS84 (EPSG:4326)
gdf_active.set_crs(epsg=4326, inplace=True)

# Show the GeoDataFrame
print(len(gdf_active))
print(gdf_active.head())
```

```python
import matplotlib.pyplot as plt
# Check CRS consistency
print("Watershed CRS:", watershed.crs)
print("Stations CRS:", gdf_all.crs)
```

```python
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the watershed polygons
watershed.plot(ax=ax, color='lightblue', edgecolor='blue', alpha=0.5, linewidth=1)

# Plot the stations as points
gdf_all.plot(ax=ax, color='red', markersize=50, marker='o', label=f'NOAA All {len(gdf_all)} Sites ',alpha=0.25)
gdf_active.plot(ax=ax, color='green', markersize=40, marker='x', label=f'NOAA Active {len(gdf_active)} Sites',alpha=1)

# Add titles and legend
ax.set_title(f"Watershed and NOAA Precipitation Sites\n(USGS {site_id})")#: {site_info['station_nm'].iloc[0]}\nDrainage Area: {round(site_info['drain_area_va'].iloc[0],2)} sq. mi.)")
ax.legend()
# Save the figure as a PNG file
plt.savefig(f"./{folder_output}/{site_id}_plot_image.png")
```

```python
# Request headers
headers = {'token': API_TOKEN}
# Base URL for data endpoint
base_url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data'

# Dataset and datatype
datasetid = 'GHCND'  # Global Historical Climatology Network - Daily
datatypeid = 'PRCP'  # Precipitation

print(len(df_selected))
#print((stations_df.head()))

print(len(df_active))
print((df_active.head()))
```

```python
# Output folder for CSVs
output_folder = 'station_precip_data'
os.makedirs(output_folder, exist_ok=True)

# Function to sanitize filename
def sanitize_filename(name):
    return re.sub(r'[^\w\-_\. ]', '_', name)

# Loop through each station
for index, row in df_active.iterrows():
    station_id = row['Station ID']
    print(f"\nDownloading PRCP data for station {station_id} ({index + 1}/{len(df_active)})")

    # Prepare parameters for each station
    params = {
        'datasetid': datasetid,
        'datatypeid': datatypeid,
        'stationid': station_id,
        'startdate': start_date,
        'enddate': end_date,
        'limit': 1000,
        'offset': 1,
        'units': 'standard'  # or 'metric'
    }

    station_data = []
    page = 1

    while True:
        print(f"Fetching page {page} for {station_id} with offset {params['offset']}...")

        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error for station {station_id}: {response.status_code} - {response.text}")
            break

        data = response.json()

        if 'results' not in data or not data['results']:
            print(f"No more data for station {station_id}.")
            break

        station_data.extend(data['results'])

        # Pagination: increase offset by limit
        params['offset'] += params['limit']
        page += 1

        # Respect NOAA rate limits
        time.sleep(2)

    if station_data:
        # Convert to DataFrame
        station_df = pd.DataFrame(station_data)
        station_df['Station ID'] = station_id  # Add station ID to each row

        # Clean station ID for filename (remove colons, slashes, etc.)
        clean_station_id = sanitize_filename(station_id)

        # Build file path
        output_file = f"./{folder_output}/{clean_station_id}.csv"

        # Save to CSV
        station_df.to_csv(output_file, index=False)
        print(f"Saved {len(station_df)} records to {output_file}")
    else:
        print(f"No precipitation data found for station {station_id}.")

print("\nDownload complete for all stations.")
```

```python
annual_total=[]

for index, row in df_active.iterrows():
    station_id = row['Station ID']
    # Clean station ID for filename (remove colons, slashes, etc.)
    clean_station_id = sanitize_filename(station_id)

    try:
        df = pd.read_csv(f"/glade/u/home/jjoseph/prec_noaa_dataaccess/{folder_output}/{clean_station_id}.csv")

    
        # Convert 'date' to datetime
        df['date'] = pd.to_datetime(df['date'])
    
        # Extract the year
        df['year'] = df['date'].dt.year
    
        # Inspect data
        #print(df.head())

        # Group by station and year, sum the precipitation values
        annual_precip = df.groupby(['Station ID', 'year'])['value'].sum().reset_index()
        
        # Rename columns for clarity
        annual_precip.columns = ['Station ID', 'Year', 'Annual_Total_Precip']
        
        # Display result
        print(annual_precip)

    except Exception as e:
            #print(f"Error processing {station_id}: {e}")
            continue

```

```python
!pwd
```

```python
!zip -r data_03335000.zip data_03335000
```
