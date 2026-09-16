---
title: "Unit 366"
unit_id: 366
---

# Unit 366

## Extracted resources (local files)

### Coursepage_DP6_DEM_Process_v3.ipynb
*Source file:* `Coursepage_DP6_DEM_Process_v3.ipynb`  ·  *type:* ipynb

## <span style="color:green"><h1><center>DEM Processing and Topographic Wetness Index (TWI)</center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil and Construction Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'> The objective of this tutorial is to learn how to merge, project, clip the DEM raster and generate Topographic Wetness Index (TWI) files. We will use the downloaded DEM raster files from USGS National Elevation Dataset from previous DEM Downloading module.</p> 

## <span style="color:green"> Data Source and Availibility </span>

<p style='text-align: justify;'>USGS-DEM, available in 1 or 1/3 or 1/9 arc-second</p>

<img src="img_DEM_DataAvailibility_202504.png" alt="Data Availibility" style="max-width: 100%; height: auto;">

## <span style="color:green">Overview of steps </span>
<ol type="1">
    <span style="color:red"><li>Read and plot original files</li></span>
    <span style="color:red"><li>Merge or Mosaick the the original files (not needed if only one raster sile is downloaded)</li></span>
     <span style="color:red"><li>Reproject or Transform coordinate system from Goegraphic to Projected Coordinate System</li></span>
    <span style="color:red"><li>Clipping or Masking the reprojected raster file</li></span>
    <span style="color:red"><li>Generate TWI raster file</li></span>



## <span style="color:green">Import the packages/modules required for this exercise</span>

We need different packages as shown below. It can be either installed using pip method or conda method.


```python
## Import the modules/packages/libraries required
import math
import matplotlib.pyplot as plt
import os

from pynhd import NLDI
from pygeohydro import NWIS
import rasterio
import rasterio.plot

import geopandas as gpd# for reading the shapefile

## Merging/ Mosaicking
from rasterio.merge import merge

## Reprojecting
from rasterio.warp import calculate_default_transform, reproject, Resampling
import pyproj

## Clipping
from rasterio.mask import mask
from shapely.geometry import mapping
from shapely.geometry import Polygon

from os.path import expanduser

import tempfile
from pathlib import Path
import pywbt
import numpy as np
```

```python
## Print the version number
import pynhd
print("PyNHD version: ",pynhd.__version__)
del pynhd

print("Rasterio version: ",rasterio.__version__)
print("Geopandas version: ",gpd.__version__)
print("PyProj version: ",pyproj.__version__)

import shapely
print("Shapely version: ",shapely.__version__)
del shapely

print("PyWBT version: ",pywbt.__version__)

```

## <span style="color:green">Step 1: Define the variables and plot unmerged raster files</span> 
<ul>
<li>Variables: <span style="color:red">USGS Site, resolution, directories, extents</span></li>
<li>Plot Unmerged files: <span style="color:red">using rasterio plot</span></li>

```python
## Few variables from previous DEM Access Modules
site_id='03335500'
resolution='1'


folder_main=f"{expanduser('~')}/scratch/DEM_Access"
folder_input=f'{folder_main}/data_{site_id}'
dem_files_store=f'{folder_input}/raw_{site_id}'
##Read the shapefile using geopandas
watershed =gpd.read_file(f'{folder_input}/shape_{site_id}.shp')
## Get site identifiers
site_info = NWIS().get_info({"site": site_id}, expanded=True)
## Get the extents and number of tiles downloaded
extents_basin=watershed.total_bounds
extent_left=abs(math.floor(extents_basin[0]))
extent_right=abs(math.floor(extents_basin[2]))
extent_bottom=abs(math.ceil(extents_basin[1]))
extent_top=abs(math.ceil(extents_basin[3]))
num_tiles_download=(((extent_left+1)-extent_right)*((extent_top+1)-extent_bottom))
## Define a empty list to hold lon and lat pair
overlap_lonlat=[]

## Create a for loop to create a rectangular boundary and see if overlaps with watershed
for lon in (range(extent_right,extent_left+1,1)):
    for lat in (range(extent_bottom,extent_top+1,1)):
        ## Defining in anticlockwise direction
        corner_left_bottom=(-lon,lat-1)
        corner_right_bottom=(-lon+1,lat-1)
        corner_right_top=(-lon+1,lat)
        corner_left_top=(-lon,lat)
        
        # Create a polygon from the coordinates
        rectangular_boundary = Polygon([corner_left_bottom,corner_right_bottom,corner_right_top,corner_left_top])

        # Create a GeoDataFrame
        rectangular_gdf = gpd.GeoDataFrame(geometry=[rectangular_boundary])
        
        # Set the coordinate reference system (CRS) if needed
        # Example: gdf.crs = {'init': 'epsg:4326'}  # WGS84

        rectangular_gdf.crs = watershed.crs

        # Perform the overlay operation to find the intersection
        intersection = gpd.overlay(watershed, rectangular_gdf, how='intersection')

        # Check if there's any intersection
        if not intersection.empty:
            #print("The rectangular polygon overlaps with the shapefile.")
            overlap_lonlat.append((lon,lat))
        #else:
        #    print("The rectangular polygon does not overlap with the shapefile.")       

print("The required lon and lat pairs are: \n",overlap_lonlat)

## Calulate the number of tiles to be downloaded from USGS
num_tiles_download=(((extent_left+1)-extent_right)*((extent_top+1)-extent_bottom))
print(f"\nNumber of tiles required to cover the entire region: {num_tiles_download}")
print(f"Left: {extent_left}, Right: {extent_right}, Bottom: {extent_bottom}, Top: {extent_top}")

print(f"\nNumber of tiles within watershed boundary: {len(overlap_lonlat)}")

## Creating the dictionary
arc_seconds = {
    "1": "1 arc-second",
    "13": "1/3 arc-second",
    "19": "1/9 arc-second"
}

if (len(overlap_lonlat)>1):
    title=f"Unmerged Raster DEMs with a spatial resolution of {arc_seconds[resolution]}\n (for USGS {site_id}: {site_info['station_nm'].iloc[0]})"
else:
    title=f"Single Raster DEMwith a spatial resolution of {arc_seconds[resolution]}\n (for USGS {site_id}: {site_info['station_nm'].iloc[0]})"


## Plotting
fig, ax = plt.subplots(figsize=(8, 8))
for location in overlap_lonlat:
        usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
        ## WRITE THE CODE BELOW
        local_raster_filename=fr'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif'
        raster = rasterio.open(local_raster_filename)
        rasterio.plot.show(raster,
                           ax=ax,
                           cmap='viridis')
        #print(f'lat: {lat},lon: {lon},file:{local_fileloc_filename}')
watershed.plot(ax=ax, 
           facecolor='none',
               edgecolor='white',
               linewidth=5)
plt.title(title)
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Free up memory
del raster,fig,ax
```

## <span style="color:green">Step 2: Merging the raster</span> 

<ul>
<li>Input: <span style="color:red">Downloaded raster tiles</span></li>
<li>Output: <span style="color:red">Merged raster tile</span></li>

## <span style="color:green">Step 2a: Create folders for saving the intermediate and results files</span>
    
<li>Code: <span style="color:red"></span></li>
folder_intermediate=f'{folder_process}/intermediate_{site_id}'<br>
check_create_path_func(folder_intermediate)<br>
folder_results=f'./results_{site_id}'<br>
check_create_path_func(folder_results)<br>

```python
def check_create_path_func(path):
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print(f"The new directory \033[1m'{path}'\033[0m is created!")
    else:
        print(f"The new directory \033[1m'{path}'\033[0m is not created as it already exists!")
        
folder_process=f"{expanduser('~')}/scratch/DEM_Process"
check_create_path_func(folder_process)

## Create the a folder for intermediate raster files 
## WRITE THE CODE BELOW




```

## <span style="color:green">Step 2b: Merging the rasters (if required)</span>

<ul>
<li> Define a function for merging the raster files using the merge function in rasterio package </li>
<li> Create a filename for saving the merged raster files </li>
<li> Call the defined function merging the rasters</li>
    Code: mosaic_new_raster,mosaic_transform=merge(datasets,
                                             resampling=Resampling.nearest,
                                             method='first',
                                             target_aligned_pixels=False)

```python
def merge_dem_raster_func(input_foldername, output_filename):
    ## Get a list of all DEM files in the input folder
    dem_files = [f for f in os.listdir(input_foldername) if f.startswith(f"USGS_{resolution}_")]
    ## Create a list to store the raster datasets
    datasets = []
    ## Open each DEM file and append it to the datasets list
    for dem_file in dem_files:
        file_path = os.path.join(input_foldername, dem_file)
        src = rasterio.open(file_path)
        datasets.append(src)
    ## Merge the raster datasets into a single mosaic and return ndarray and information on mapping the pixel coordinates
    ## WRITE THE CODE BELOW
        
    
    
    
    ## Copy the metadata from one of the datasets (assuming they all have the same metadata)
    out_meta = datasets[0].meta.copy()

    out_meta.update({
        'height': mosaic_new_raster.shape[1],
        'width': mosaic_new_raster.shape[2],
        'transform': mosaic_transform ## copy the transform parameter from merge
    })
    with rasterio.open(output_filename, 'w', **out_meta) as dest:
        dest.write(mosaic_new_raster)
    ## Close all the opened datasets
    for dataset in datasets:
        dataset.close()
    print(f"Merging completed for {len(overlap_lonlat)} DEM raster files")

if num_tiles_download==1:
    merged_raster_filename=f'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif'
    print("No need to merge as only one tiff file")
    title_4_plot=f"Original DEM Raster (Merging not required) in {watershed.crs} Geographic CRS\n(for USGS {site_id} and {arc_seconds[resolution]} resolution)"
else:
    merged_raster_filename=f'{folder_intermediate}/merged_{resolution}_{site_id}.tif'
    ## WRITE THE CODE BELOW
    merge_dem_raster_func(dem_files_store,merged_raster_filename)
    title_4_plot=f"Merged DEM Raster in {watershed.crs} Geographic CRS\n(for USGS {site_id} and {arc_seconds[resolution]} resolution)"
```

```python
with rasterio.open(merged_raster_filename) as src:
    print(src)
    fig, ax = plt.subplots(figsize = (8,8))
    mapped=rasterio.plot.show(src,
                              ax=ax, 
                              cmap='viridis')
    im = mapped.get_images()[0]
    fig.colorbar(im,
                 ax=ax,
                 shrink=0.5,
                 label='Elevation (in meters)',
                 location='right',
                 orientation='vertical')
    ax.set_xlabel("Longitude (DD)")
    ax.set_ylabel("Latitude (DD)")
    ax.set_title(title_4_plot)
    
watershed.plot(ax=ax,
               facecolor='none',
               edgecolor='white',
               linewidth=5)
src.close()
del mapped,im
del fig,ax
```

## <span style="color:green">Step 3: Reproject both the shapefile and raster to PCS from GCS</span>

<ul>
<li> Find the UTM Zone for Projected Coordinate System using the centroid point </li>
<li> Project the merged dem </li>

```python
## Find if basin has a projection
print(watershed.crs)
```

## <span style="color:green">Step 3a: Finding the UTM Zone</span>

<ul>
<li> Find the approximate centroid </li>    
<li> Find whether the centroid is in N or S </li>
<li> Calculate the zone value (below calculations applciable to conterminous US) </li>


```python
## Find the approximate centroid
df=watershed
df['geometry'].centroid
## Find the center point
df['Center_point'] = df['geometry'].centroid
## Extract lat and lon from the centerpoint
df["lon"] = df.Center_point.map(lambda p: p.x)
df["lat"] = df.Center_point.map(lambda p: p.y)
df
```

```python
## Calculate N or S
if 0 < df['lat'][0] < 84:
    lat_zone='N'
elif -84 < df['lat'][0] < 0:
    lat_zone='S'

## Calculate zone 
## Applicable for US only

if -138 < df['lon'][0] < -132:
    zone_value='08'
elif -132 < df['lon'][0] < -126:
    zone_value='09'
elif -126 < df['lon'][0] < -120:
    zone_value='10'
elif -120 < df['lon'][0] < -114:
    zone_value='11'
elif -114 < df['lon'][0] < -108:
    zone_value='12'
elif -108 < df['lon'][0] < -102:
    zone_value='13'
elif -102 < df['lon'][0] < -96:
    zone_value='14'
elif -96 < df['lon'][0] < -90:
    zone_value='15'
elif -90 < df['lon'][0] < -84:
    zone_value='16'
elif -84 < df['lon'][0] < -78:
    zone_value='17'
elif -78 < df['lon'][0] < -72:
    zone_value='18'
elif -72 and df['lon'][0] < -66:
    zone_value='19'
elif -66 < df['lon'][0] < -60:
    zone_value='20'    
elif -60 < df['lon'][0] < -54:
    zone_value='21'
elif -54 < df['lon'][0] < -48:
    zone_value='22'      
else:
    print("not in conterminous US")
    
crs_string=f'EPSG:326{zone_value}'
crs_string
```

```python
## Alternative Method to estimate the CRS
crs_string2=watershed.estimate_utm_crs(datum_name='WGS 84')
crs_string2
```

## <span style="color:green">Step 3b: Reprojecting watershed shapefile to UTM using calculated zone</span>

<ul>
<li> Using the string created for EPSG (by calculated zone value), reproject it to PCS  </li>
<li> Calculate the zone value (below calculations applciable to conterminous US) </li>

```python
shapefile_fileloc_filename=f'{folder_input}/shape_{site_id}.shp'
watershed_file=gpd.read_file(shapefile_fileloc_filename)
watershed_proj=watershed_file.to_crs(crs_string)
```

```python
print(watershed_file.crs)
print(watershed_proj.crs)
```

```python
proj_shapefile_filename=f'{folder_results}/proj_shp_{site_id}.shp'
print("Projected Watershed shapefile is stored at:", proj_shapefile_filename)
watershed_proj.to_file(proj_shapefile_filename, driver='ESRI Shapefile',mode='w')
```

## <span style="color:green">Step 3c: Reprojecting merged raster to UTM using calculated zone</span>

<ul>
<li> Using the string created for EPSG (by calculated zone value), reproject it to PCS  </li>
<li> Calculate the zone value (below calculations applciable to conterminous US) </li>
    
    Code: reproject(source=rasterio.band(src,i),
                          destination=rasterio.band(dst,i),
                          src_transform=src.transform,
                          src_crs=src.crs,
                          dst_transform=transform,
                          dst_crs=target_crs_proj,
                          resampling=Resampling.nearest) <br>
    Code: reproject_raster_func(merged_raster_filename,reprojected_raster_filename,crs_string)

```python
def reproject_raster_func(input_raster, output_raster, target_crs):
    # Load the input DEM
    with rasterio.open(input_raster) as src:
        # Define the target CRS
        target_crs_proj = pyproj.CRS.from_string(target_crs)
        # Calculate the transformation and new dimensions
        transform, width, height = calculate_default_transform(src.crs, target_crs_proj, src.width, src.height, *src.bounds)
        # Update metadata for the new dataset
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': target_crs_proj,
            'transform': transform,
            'width': width,
            'height': height
        })
        # Create the output dataset and perform the reprojection
        with rasterio.open(output_raster, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                ## WRITE CODE BELOW
                
                
                
                
                
                
                
        print(f"Reprojection of raster complete to {target_crs} projected CRS.")
reprojected_raster_filename=f'{folder_intermediate}/reprojected_{resolution}_{site_id}.tif'
## WRITE CODE BELOW

```

```python
reprojected_raster_filename=f'{folder_intermediate}/reprojected_{resolution}_{site_id}.tif'
with rasterio.open(reprojected_raster_filename) as src:
    fig, ax = plt.subplots(figsize = (8,8))
    mapped=rasterio.plot.show(src,
                              ax=ax, 
                              cmap='viridis')
    im = mapped.get_images()[0]
    fig.colorbar(im,
                 ax=ax,
                 shrink=0.5,
                 label='Elevation (in meters)',
                 location='right',
                 orientation='vertical')
    ax.set_xlabel("Easting (meters)")
    ax.set_ylabel("Northing (meters)")
    ax.set_title(f"Reprojected Raster DEM in {watershed_proj.crs} Projected CRS\n(for USGS {site_id} and {arc_seconds[resolution]} resolution)")
## Uee the reprojected watershed shapefile
watershed_proj.plot(ax=ax,
                    facecolor='none',
                    edgecolor='white',
                    linewidth=5)
src.close()
del mapped,im,fig,ax,src
```

## <span style="color:green">Step 4: Clipping the reprojected raster file using watershed shapefile</span>

<ul>
<li> Using the buffer, clip/ mask the watershed  </li>
    
    Code: clipped,out_transform=mask(src,geoms,crop=True)
    Code: buffer_value_in_meters=1500
clip_raster_with_shapefile_func(reprojected_raster_filename,
                                clipped_raster_filename,
                                proj_shapefile_filename,
                                buffer_value_in_meters)


```python
proj_shapefile_filename=f'{folder_results}/proj_shp_{site_id}.shp'

def clip_raster_with_shapefile_func(input_raster, output_raster, shapefile,buffer_value):
    ## Open the shapefile using geopandas
    shapefile_gdf = gpd.read_file(shapefile).buffer(buffer_value)
    ## Open the input raster
    with rasterio.open(input_raster) as src:
        ## Convert the shapefile geometry to the same CRS as the raster
        shapefile_gdf = shapefile_gdf.to_crs(src.crs)
        ## Convert the shapefile geometry to GeoJSON-like format
        geoms = [mapping(geom) for geom in shapefile_gdf.geometry]
        ## Clip the raster using the shapefile geometry
        ## WRITE THE CODE BELOW

        
        ## Update metadata for the new dataset
        out_meta = src.meta.copy()
        out_meta.update({
            'height': clipped.shape[1],
            'width': clipped.shape[2],
            'transform': out_transform
        })
        ## Save the clipped raster to the output file
        with rasterio.open(output_raster, 'w', **out_meta) as dst:
            dst.write(clipped)
    print(f"Raster clipping complete with a buffer value of {buffer_value} m.")

clipped_raster_filename=f'{folder_results}/clipped_{resolution}_{site_id}.tif'
## WRITE THE CODE BELOW    





```

```python
with rasterio.open(clipped_raster_filename) as src1:
    fig, ax = plt.subplots(figsize = (8,8))
    mapped=rasterio.plot.show(src1,
                              ax=ax, 
                              cmap='viridis')
    im = mapped.get_images()[0]
    fig.colorbar(im,
                 ax=ax,
                 shrink=0.5,
                 label='Elevation (in meters)',
                 location='right',
                 orientation='vertical')
    ax.set_xlabel("Easting (meters)")
    ax.set_ylabel("Northing (meters)")
    ax.set_title(f"Clipped Raster DEM with a buffer of {buffer_value_in_meters} m and with {watershed_proj.crs} Projected CRS\n(for USGS {site_id} and {arc_seconds[resolution]} resolution)")

## Uee the reprojected watershed shapefile
watershed_proj.plot(ax=ax,
                    facecolor='none',
                    edgecolor='white',
                    linewidth=5)
del src1,fig,ax
```

## <span style="color:green">Step 5: Creating TWI raster</span>

<ul>
<li> Intermediate steps: Fill Sinks (Breach Depressions), Flow Direction, Flow Accumulation, Slope and TWI,   </li>
    Code: <br> with tempfile.TemporaryDirectory(dir=str(folder_results)) as temp_dir:<br>
    pywbt.whitebox_tools(input_dir,
                         wbt_args,
                         save_dir=input_dir,
                         max_procs=-1,
                        )


```python
fname = Path(clipped_raster_filename)
fname.parent.mkdir(parents=True, exist_ok=True)

wbt_args = {
    "BreachDepressions": [f"-i={fname.name}", "--fill_pits", f"-o=dem_corr_{resolution}_{site_id}.tif"],
    "D8Pointer": [f"-i=dem_corr_{resolution}_{site_id}.tif", f"-o=fdir_{resolution}_{site_id}.tif"],
    "DownslopeFlowpathLength": [f"--d8_pntr=fdir_{resolution}_{site_id}.tif", f"-o=downslope_fp_length_{resolution}_{site_id}.tif"],
    "D8FlowAccumulation": [f"-i=fdir_{resolution}_{site_id}.tif", "--pntr", "--out_type='specific contributing area'", f"-o=sca_{resolution}_{site_id}.tif"],
    "Slope": [f"-i=dem_corr_{resolution}_{site_id}.tif", "--units=degrees", f"-o=slope_{resolution}_{site_id}.tif"],
    "WetnessIndex": [f"--sca=sca_{resolution}_{site_id}.tif", f"--slope=slope_{resolution}_{site_id}.tif", f"-o=twi_{resolution}_{site_id}.tif"],
}
```

```python
input_dir=folder_results

## WRITE THE CODE BELOW

```

```python
with rasterio.open(f"{folder_results}/twi_{resolution}_{site_id}.tif") as src1:
    fig, ax = plt.subplots(figsize = (8,8))
    mapped=rasterio.plot.show(src1,
                              ax=ax, 
                              cmap='plasma')
    im = mapped.get_images()[0]
    fig.colorbar(im,
                 ax=ax,
                 shrink=0.5,
                 label='Topographic Wetness Index\n(Dimensionless)',
                 location='right',
                 orientation='vertical')
    ax.set_xlabel("Easting (meters)")
    ax.set_ylabel("Northing (meters)")
    ax.set_title(f"Topographic Wetness Index (TWI) in {watershed_proj.crs} Projected CRS\n(for USGS {site_id} and {arc_seconds[resolution]} resolution)")

## Uee the reprojected watershed shapefile
watershed_proj.plot(ax=ax,
                    facecolor='none',
                    edgecolor='white',
                    linewidth=5)
del src1,fig,ax
```

```python
## Define the file paths for the different rasters

raster_files = {
    "Clipped DEM Raster": [f"{folder_results}/clipped_{resolution}_{site_id}.tif",'Elevation (in meters)'],
    "Breach Depressions Filled Raster": [f"{folder_results}/dem_corr_{resolution}_{site_id}.tif",'Elevation (in meters)'],
    "D8 Flow Direction Raster": [f"{folder_results}/fdir_{resolution}_{site_id}.tif",'Index from 1 to 128'],
    "Slope Raster": [f"{folder_results}/slope_{resolution}_{site_id}.tif",'Slope (Degrees)'],
    "Flow Accumulation Raster (Specific Contributing Area)": [f"{folder_results}/sca_{resolution}_{site_id}.tif",'Count of Cells/ meter'],
    "Topographic Wetness Index (TWI) Raster": [f"{folder_results}/twi_{resolution}_{site_id}.tif",'TWI (Dimensionless)'],}

# Create a figure with a 3x2 layout
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Loop through the raster files and plot them
for ax, (title, (file,units)) in zip(axes, raster_files.items()):
    with rasterio.open(file) as src:
        # Read the first band
        data = src.read(1)
        vmin, vmax = np.percentile(data[data != src.nodata], [2, 98])
        #im = ax.imshow(data, cmap='plasma', vmin=vmin, vmax=vmax)
        
        mapped=rasterio.plot.show(src, ax=ax, cmap='plasma', vmin=vmin, vmax=vmax)
        im = mapped.get_images()[0]
       
    
        # Plot the raster data
        #img = ax.imshow(data, cmap='viridis')
        ax.set_title(title)
        ax.axis('off')  # Hide the axis
        
        ## Uee the reprojected watershed shapefile
        watershed_proj.plot(ax=ax,
                            facecolor='none',
                            edgecolor='white',
                            linewidth=5)
        
        # Add a colorbar specific to this subplot
        cbar = plt.colorbar(im, ax=ax, shrink=0.5)
        cbar.set_label(units)  # Label for the colorbar

# Adjust layout
plt.tight_layout()
plt.show()
```

### Instructions_DP6_DEM_Process_TWI_v06b.pdf
*Source file:* `Instructions_DP6_DEM_Process_TWI_v06b.pdf`  ·  *type:* pdf

Processing Digital Elevation Model (DEM) to generate 
Topographic Wetness Index (TWI) 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
Digital Elevation Model (DEM) raster data are often acquired in tiles or strips based on 
the data collection method. These data tiles must be pre-processed before using in any 
hydrologic applications.  First, these tiles need to be merged (or mosaicked) to create a 
single raster. Second, it must be re-projected from its source geographic coordinate 
system to a projected coordinate system. Typically, DEM data from sources such as the 
National Map Viewer are available in a Geographic Coordinate System, necessitating 
reprojection to a coordinate system suitable for the specific geographic location. This 
ensures minimal distortions and preserves data accuracy. Nextly,  the mosaicked DEM 
needs to be clipped to match the region of interest defined by a shapefile. This step is 
crucial as it trims unnecessary data outside the study region, reducing processing time 
for subsequent analyses and visualization. Finally, Topographic Wetness Index is created 
from the clipped DEM file involving few intermediate raster cacluation like filling the 
sinks, flow direction, flow accumulation, and slope index. This tutorial provides an 
automated way of performing these steps in a cyber environment.  
 
Pre-requisites 
 
You must have a login (CI login will also work with institutional credentials or with 
Google Account) for the CyberFaces platform. If you do not have a login, please visit 
www.cyberfaces.org and click on Register.  
 
Computer Requirements 
 
The tutorial can be completed by using a Python-based Jupyter Notebook with a proper 
conda environment with the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “ct-fair” kernel in the CyberFaCES

platform. The user does not have to install any modules to complete this tutorial in the 
CyberFaCES platform. However, if a user wants to use this in another platform, the 
following packages are needed: (1) rasterio for plotting, merging, reprojecting, and other 
operations on raster data (2) geopandas for working with shapefile, (3) pyproj for the 
coordinate system, (4) shapely for clipping operation, and (5) pywbt for TWI creation.  
  
Overview of steps 
1. Define the variables and plot the unmerged downloaded raster files 
2. Merging or mosaicking the unmerged raster tiles. 
3. Reprojecting the merged raster file. 
4. Clipping the raster file for the watershed with a buffer region 
5. Generate the Toip 
 
Instructions 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with institutional credentials or 
ORCID or use Google Account (there are a number of login options in the 
dropdown and if nothing works 
you may need to register as a new 
user as you are accessing 
CyberFaCES for the first time). 
Also, select the “Remember this 
selection” option for future easy 
access to CyberFaCES. 
 
3. Navigate to “Learn” on the top 
ribbon and select “Take Course”.

4. Select “I-GUIDE Forum 2025 Hands-on Tutorial: CyberTraining on Geospatial 
Data Processing using Python for Hydrology” course from the list of courses as 
shown below.  
5. Click on “Start now” or “Resume” and you will be able to see the material for 
completing this workshop. If you have not completed the earlier module 
(DEM_Access), please complete the Jupyter Notebook before proceeding. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here.  Now, we will complete the Geospatial & 
Hydrological Science: DEM Processing. Select “JN-DEM Processing and TWI” 
Jupyter Notebook and it will redirect to the Interactive Jupyter Notebook Hub.  
7. Be patient until the Notebook opens, and it has the correct Kernel (ct-fair) as shown 
below. This kernel has all 
modules preinstalled for 
completing this tutorial. 
8. Run the first code cell to im
port the essential modules i
n the current kernel. Also, e
xecute the next cell to get th
e version number of the pac
kages that we will be using 
in this module. 
 
Step 1: Define the variables and plot unmerged raster files 
9. At this point, we need to specify the USGS site number and the desired resolution 
before plotting the individual, unmerged raster tiles alongside the watershed 
shapefile. To proceed, simply execute the cell without the need to input any code. 
The resulting plot will display the unmerged raster tiles alongside the shapefile,

as depicted in the figure below. It’s worth noting that the displayed x and y 
coordinates represent longitudes and latitudes, indicating that the raster files are 
not yet in a projected coordinate system. Consequently, when calculating areas 
and distances, it’s important to be aware that accuracy may be compromised due 
to the absence of projection. Just run the cell in Step 1 to see the following outputs. 
You do not have to write any code for this cell. If you get an error, check for the 
correctness of USGS number, resolution, and see if you downloaded the DEM tiles 
in folder – “~/scratch/DEM_Access/data_<site_id>/raw_<site_id>/”. 
 
Step 2: Merging the raster 
10. As observed in the previous plot, there are 
multiple 
tiles 
(three 
in 
this 
case)  
overlapping the watershed boundary, and 
the boundary of each is easily noticeable. 
To create a single raster, the first task is to 
merge or mosaic the various raster files 
into a unified and continuous raster 
dataset.  
Step 
2a: 
Create 
folders 
for 
saving 
the 
intermediate and results files 
11. To begin, we will establish two folders: one for intermediate files, where we will 
store files generated during intermediary steps like merging and reprojection, and 
another for the final results, specifically for the clipping step. To create these 
folders, simply execute the cell provided. There is no need to write any code within 
the cell. 
 
Step 2b: Merging the rasters (if required) 
12. Now, we will develop a function that will handle the merging operation using the 
merge function in rasterio package. This function will utilize the metadata from 
the original file and apply it to the newly created raster file. Additionally, we will 
incorporate a condition to bypass the merging process if a single raster tile covers

the entire extent of the watershed file. To proceed, please complete the cell within 
the Jupyter Notebook file following the example provided in the figure below. You 
will need to write the code and save it with a specific name inside the folder 
created in the previous step. When this code is executed, it will result in merged 
raster files being added to the intermediate directory, and you can review the 
folder structure as outlined in the figure. 
 
   
13. The next cell shows the plot of the merged raster file along with the watershed 
shapefile. If you correctly wrote the code in the previous step, you should get a 
seamless raster file covering the Cedar Creek watershed as shown below. Just run 
the cell. You don’t have to write any code in the cell to plot the merged raster data.

Step 3: Reproject both the shapefile and raster to PCS from GCS 
14. We will now find the proper coordinate system depending on the location of this 
watershed. If you run the next code cell, you will see that the watershed shapefile 
has EPSG:4326 projection (also known as 
WGS84 projection) as shown below. This 
is a geographic coordinate system and we 
need to transform this to a projected 
coordinate system.  
 
15. First, we will find the centroid of the watershed and then estimate the appropriate 
UTM zone for the projected coordinate system. Just run the next two cells. You do 
not have to write any code for this cell. Next, we will find the appropriate UTM 
zone based on the centroid of the 
watershed. It becomes tricky when the 
watershed has a huge area and spans 
across two or more UTM zones. But, let 
us keep it simple for now i.e. to find the 
UTM zone based on the centroid. We 
have also provided an in-built function 
to estimate the UTM Zone for 
reprojection based on the watershed 
shapefile. For the current watershed, 
the projected CRS is estimated as 
EPSG:32616 or WGS 84 / UTM zone 
16N as shown below. 
 
Step 3b: Reprojecting watershed shapefile to UTM using calculated zone

16. Now we will project the watershed to the appropriate UTM zone as this will be 
used for clipping the projected raster file in the next step. Just run the next two 
cells. You do not have to write any code for this cell. Execution of this cell will add 
the shapefiles to the results directory as shown below. 
 
 
 
Step 3c: Reprojecting merged raster to UTM using calculated zone 
17. To complete the reprojection process, we will use a function for raster projection, 
which will transform the default coordinate system into the desired projected 
coordinate system. You will need to write the code to perform this raster 
reprojection task. Once the code is executed, the reprojected raster file will be 
included in the intermediate directory, as indicated below.

18. After reprojecting the raster data to the suitable UTM zone, our next step will 
involve creating a plot to visualize the changes in the output file. Additionally, we 
will generate plots for all the downloaded raster files and overlay them with the 
shapefile to assess 
the success of the 
entire process. To 
accomplish 
this, 
please proceed by 
executing the cell 
in 
the 
Jupyter 
Notebook file, as 
illustrated in the 
figure below. You 
do not have to 
write any code for 
plotting the reprojected raster file. If you look carefully, you may notice a slight 
tilt or inclination in the image (see right top and right bottom of the plotted 
image), which is a result of the raster data reprojection. 
 
Step 4: Clipping the reprojected raster file using watershed shapefile 
19. The final step in preprocessing DEM data involves the process of clipping the 
raster data to match the study area. To achieve this, we will create a function that 
will clip the reprojected raster file based on a specific region defined by a 
reprojected shapefile. It is important to emphasize that the original watershed file 
cannot be used for this task, as it is in a geographic coordinate system. To execute 
this task, we will need to write code for the clipping operation as shown below. 
Upon successful execution of the code, the clipped raster file will be added to the 
result directory as shown below. This clipping process serves the purpose of 
reducing unnecessary data stored on the hard disk outside of the study region.

20. Next, we will create a plot 
specifically for the clipped 
raster that corresponds to the 
study area. While observing 
this plot, you may observe that 
there are no elevation values 
present for areas outside the 
defined shapefile, effectively 
reducing storage space. To 
generate plots for the final raster files, simply execute the next cell. There's no need 
to write any code for plotting the reprojected raster file. 
Step 5: Creating the TWI from Clipped DEM 
21. Next, we will use White Box Tools (WBT) to generate the Topographic Wetness 
Index (TWI) raster. The process begins by creating a Digital Elevation Model 
(DEM) with depressions removed, then calculates the flow direction using the D8 
algorithm. Next, it generates a specific contributing area raster and creates a slope 
raster, which serve as intermediate files for calculating the TWI raster. To execute 
this task, we will need to write code for the clipping operation as shown below 
 
 
22. We will now plot the TWI raster. Just run the next cell. You do not have to write 
any code for this cell.

23. Finally, run the next code and we will plot all the rasters we have created in this 
tutorial to see the comparison. 
 
 
 
24. If you are curious, you can try the Yellowstone River at Yellowstone Lk Outlet 
YNP, WY (06186500). You should obtain the plots of rasters as shown below.

Ok, you have now completed the tutorial successfully. Congratulations! 
 
References 
1. Hawker, L., Bates, P., Neal, J., & Rougier, J. (2018). Perspectives on digital elevation 
model (DEM) simulation for flood modeling in the absence of a high-accuracy 
open access global DEM. Frontiers in Earth Science, 6, 233. 
2. Saksena, S., & Merwade, V. (2015). Incorporating the effect of DEM resolution and 
accuracy for improved flood inundation mapping. Journal of Hydrology, 530, 180-
194. 
3. Chegini, T., Li, H. Y., & Leung, L. R. (2021). HyRiver: Hydroclimate Data Retriever. 
Journal of Open Source Software, 6(66), 3175. 
4. https://docs.python.org/3/library/urllib.request.html. 
5. Gillies, S. (2019). Rasterio documentation. MapBox: San Francisco, CA, USA, 23. 
6. https://pywbt.readthedocs.io/latest/ 
7. Lindsay, JB. 2014. The Whitebox Geospatial Analysis Tools project and open-
access GIS. Proceedings of the GIS Research UK 22nd Annual Conference, The 
University of Glasgow, 16-18 April, DOI: 10.13140/RG.2.1.1010.8962.
