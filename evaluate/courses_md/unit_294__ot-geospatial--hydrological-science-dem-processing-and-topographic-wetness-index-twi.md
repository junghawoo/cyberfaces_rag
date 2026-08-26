---
title: "[OT] Geospatial & Hydrological Science: DEM Processing and Topographic Wetness Index (TWI)"
unit_id: 294
course_id: 0
level: "Expert"
slug: ot-geospatial--hydrological-science-dem-processing-and-topographic-wetness-index-twi
is_course: 0
---

# [OT] Geospatial & Hydrological Science: DEM Processing and Topographic Wetness Index (TWI)

## Fetched resources (external URLs)

### Jupyter Notebook (OT DEM Process) (notebook)
*URL:* https://github.com/jibcar/Miniworkshop_2025May/blob/main/Coursepage_DEMProcess_OT.ipynb

## <span style="color:green"><h1><center>Accessing and Processing Global DEM</center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'>This tutorial walks you through the end-to-end workflow for extracting a Topographic Wetness Index (TWI) raster anywhere on Earth. </p>


* You’ll start by defining a custom bounding box that encloses your area of interest.
* The script then pulls the corresponding DEM tiles on-the-fly from OpenTopography and reprojects to proper projected coordinate system.
* Next, we preprocess the reprojected DEM (breach depressions, compute flow direction, slope, and specific contributing area) using WhiteboxTools via its PyWBT wrapper.
* Finally, we calculate and visualize the TWI, giving you a ready-to-use layer for hydrologic or ecological analyses.

## <span style="color:green">Topographic Wetness Index (TWI)</span>

**Topographic Wetness Index (also called “compound topographic index” or simply *wetness index*)** quantifies how likely a point on the landscape is to accumulate and retain water given the local contributing area and slope:

$$
\text{TWI} \;=\; \ln\!\biggl(\frac{\alpha}{\tan\beta}\biggr)
$$

| Symbol | Meaning | Units |
| :----: | ------- | ----- |
| $\alpha$  | *Specific upslope contributing area* &nbsp;– the drainage area per unit contour length flowing into the cell (often derived from a DEM flow-accumulation grid) | m² m⁻¹ |
| $\beta$ | *Local slope angle* (in radians), usually calculated from the same DEM | – |

<span style="color:green">**Interpretation**</span>

* Large ($\alpha$) (many upstream cells) **increases** TWI → wetter, more saturated ground.  
* Steep slopes ($\tan(\beta$) large) **decrease** TWI → faster drainage, drier ground.  
* Flat valley bottoms with large contributing areas therefore have the **highest** TWI values.

<span style="color:green">**Applications**</span>

* Predicting zones of soil saturation and runoff generation  
* Estimating spatial patterns of soil moisture for eco-hydrological models  
* Delineating riparian buffers and wetland boundaries  
* As an explanatory variable in species-distribution or erosion studies

<span style="color:green">**Important notes**</span>

* TWI is **dimensionless** and relative; thresholds vary by terrain and resolution.  
* Calculations are sensitive to DEM quality, flow-routing algorithm, and the method used to
  estimate slope.  
* Variations exist (e.g. log-transforms with different bases, or adding a small constant to avoid
  ($\tan\beta = 0$) at perfectly flat cells).


## <span style="color:green"> Available Different Global Dataset from Open Topography</span>
<ol type="1">
    <span style="color:red"><li>AW3D30 (ALOS World 3D 30m)</li></span>
    <span style="color:red"><li>AW3D30_E (ALOS World 3D Ellipsoidal, 30m)</li></span>
    <span style="color:red"><li>COP30 (Copernicus Global DSM 30m)</li></span>
     <span style="color:red"><li>COP90 (Copernicus Global DSM 90m)</li></span> 
    <span style="color:red"><li>GEBCOIceTopo (Global Bathymetry and Topography that includes ice sheet topography, 500m)</li></span>  
      <span style="color:red"><li>GEBCOSubIceTopo (Global Bathymetry and Topography Including Basal Ice Surface that includes under-ice sheet topography, 500m)</li></span> 
    <span style="color:red"><li>GEDI_L3 (DTM 1000m)</li></span>
         <span style="color:red"><li>NASADEM (NASADEM Global DEM)</li></span>
    <span style="color:red"><li>SRTMGL3 (SRTM GL3 90m)</li></span>
    <span style="color:red"><li>SRTMGL1 (SRTM GL1 30m)</li></span>
     <span style="color:red"><li>SRTMGL1_E (SRTM GL1 Ellipsoidal 30m)</li></span>  
     <span style="color:red"><li>SRTM15Plus (Global Bathymetry SRTM15+ V2.1 500m)</li></span>  
    
     

## <span style="color:green">Step 0: Import the packages/modules required for this exercise</span>

We need different packages as shown below. It can be either installed using pip method or conda method.


```python
import requests
import os
import geopandas as gpd
from pynhd import NLDI
import matplotlib.pyplot as plt
import rasterio
import rasterio.plot
import ipywidgets as widgets
from IPython.display import display
import urllib.request
import progressbar
import math
from shapely.geometry import box
import sys
sys.path.append("/srv/shared/data_dem_access/")
from USGS_sites_map import display_bounding_box, display_data_avail


import geopandas as gpd
import requests, io, json

## Reprojecting
from rasterio.warp import calculate_default_transform, reproject, Resampling
import pyproj

## TWI
import tempfile
from pathlib import Path
import pywbt
import numpy as np
```

## <span style="color:green">Step 1a: Pick a suitable global DEM</span>

```python
# Raster data dictionary
raster_data_dict = {
    "AW3D30": "ALOS World 3D 30m",
    "AW3D30_E": "ALOS World 3D Ellipsoidal, 30m",
    "COP30": "Copernicus Global DSM 30m",
    "COP90": "Copernicus Global DSM 90m",
    "GEBCOIceTopo": "Global Bathymetry and Topography that includes ice sheet topography, 500m",
    "GEBCOSubIceTopo": "Global Bathymetry and Topography Including Basal Ice Surface that includes under-ice sheet topography, 500m",
    "GEDI_L3": "DTM 1000m",
    "NASADEM": "NASADEM Global DEM",
    "SRTMGL3": "SRTM GL3 90m",
    "SRTMGL1": "SRTM GL1 30m",
    "SRTMGL1_E": "SRTM GL1 Ellipsoidal 30m",
    "SRTM15Plus": "Global Bathymetry SRTM15+ V2.1 500m",
}

options = [('— select a raster —', None)] + [
    (f"{code} — {name}", code) for code, name in raster_data_dict.items()
]

raster_dropdown = widgets.Dropdown(
    options=options,
    value=None,
    description='Raster:',
    layout=widgets.Layout(width='600px')
)

display(raster_dropdown)
```

```python
selected_raster_code = raster_dropdown.value          
if selected_raster_code is None:
    print("No raster selected yet.")
else:
    selected_raster_name = raster_data_dict[selected_raster_code]     
    print(f"Selected DEM Raster code : {selected_raster_code}\nSelected DEM Raster name : {selected_raster_name}")

```

## <span style="color:green">Step 1b: Define a bounding box and check if system can handle it</span>

```python
#bounding_box = (-88.27914124959916, 37.65387909441565, -84.65774514744832, 39) #large area and requires higher RAM or HPC
#bounding_box = (-87.20779996, 40.12094423, -84.40668323, 41.35449477) #west, south, east, north
#bounding_box = (76.20028223013529,9.899460286791733,78, 11)
## Create filename unique to bounding box
west, south, east, north = bounding_box

## Build a Shapely polygon and create a geodataframe
geom = box(west, south, east, north)
bb_gdf = gpd.GeoDataFrame({'geometry': [geom]}, crs='EPSG:4326')
## Method to estimate the CRS and convert to string object
crs_string_full=bb_gdf.estimate_utm_crs(datum_name='WGS 84')
crs_string=str(crs_string_full.to_epsg())

## Calculate the area in sq. m. and sq. km.
bb_gdf['area_m2'] = bb_gdf.to_crs(crs_string).geometry.area
#print(bb_gdf['area_m2'].iloc[0], "sq. m.")
bb_gdf['area_km2'] = bb_gdf['area_m2'] / 1000000
#print(bb_gdf['area_km2'].iloc[0], "sq. km.")
if bb_gdf['area_km2'].iloc[0] > 35000:
    print("Please use smaller bounding box, otherwise kernel will die soon...\nUse Higher RAM or HPC for this larger bounding box")
else:
    print("Please proceed!\nThe area of bounding box within the safe limits...")
```

## <span style="color:green">Step 1c: Display the bounding box and data availibility</span>

```python
display_data_avail(selected_raster_code, bounding_box)
```

## <span style="color:green">Step 1d: Create a unique filename based on bounding box extents</span>

```python
expanded_bb = (
    math.floor(west  * 100) / 100,   # left  (west), use floor
    math.floor(south * 100) / 100,   # bottom(south), use floor
    math.ceil(east   * 100) / 100,   # right (east), use ceil
    math.ceil(north  * 100) / 100    # top   (north), use ceil
)
def bbox_to_filename(bb):
    w, s, e, n = [round(x, 2) for x in bb]

    def tag(value, pos_char, neg_char):
        hemis = pos_char if value >= 0 else neg_char
        #return f"{hemis}{abs(value):.2f}"
        return f"{hemis}{abs(value)}"
    

    parts = [
        tag(w, 'E', 'W'),   # longitude west edge
        tag(s, 'N', 'S'),   # latitude  south edge
        tag(e, 'E', 'W'),   # longitude east edge
        tag(n, 'N', 'S')    # latitude  north edge
    ]
    
    return("".join(parts))

unique_name=bbox_to_filename(expanded_bb)

## Create DEM file name
file_name = f"dem_{unique_name}_{selected_raster_code}.tif"
print("Filename for current bounding box:", file_name)
```

## <span style="color:green">Step 2a: Download the data from OpenTopography using your API key</span>

```python
## OpenTopography API base URL
BASE_URL = "https://portal.opentopography.org/API/globaldem"
api_key = "<use your API Key from OpenTopography>"  # Replace with your actual OpenTopography API key
## Create the API request URL
url = (
    f"{BASE_URL}?demtype={selected_raster_code}"
    f"&south={expanded_bb[1]}&north={expanded_bb[3]}"
    f"&west={expanded_bb[0]}&east={expanded_bb[2]}"
    f"&outputFormat=GTiff&API_Key={api_key}"
)
print("Please wait! Download will take time to complete...")

## Send GET request to OpenTopography API
response = requests.get(url, 
                        stream=True)
print(response)
#print(response.content)
```

## <span style="color:green">Step 2b: Create folder paths to save raw and final data</span>

```python
## Define a function for making a directory depending on whether is exists or not.
## We are creating a function so that it can be used later for creating three folders in the later modules
def check_create_path_func(path):
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print(f"The new directory \033[1m'{path}'\033[0m is created!")
    else:
        print(f"The new directory \033[1m'{path}'\033[0m is not created as it already exists!")
        
## Create the a folder for storing DEMs using the earlier defined function
folder_main=f"{os.path.expanduser('~')}/scratch/DEM_Access"
check_create_path_func(folder_main)
folder_input=f"{folder_main}/data"
check_create_path_func(folder_input)
folder_results=f'./results'
check_create_path_func(folder_results)
```

## <span style="color:green">Step 2c: Save the DEM data to input folder</span>

```python
## Check if the request was successful
dem_filepath = f'{folder_input}/{file_name}' 
if response.status_code == 200:
      
    ## Save the response content as a tif file
    with open(dem_filepath, 'wb') as f:
        f.write(response.content)

    print(f"Data downloaded at f'{dem_filepath}'")
    
elif response.status_code == 204:
    print(f"Error: No Data: {response.status_code}")
elif response.status_code == 400:
    print(f"Error: Bad request: {response.status_code}")
elif response.status_code == 401:
    print(f"Error: Unauthorized: {response.status_code}")
elif response.status_code == 403:
    print(f"Error: Forbidden: {response.status_code}")
elif response.status_code == 404:
    print(f"Error: Not Found: {response.status_code}")
elif response.status_code == 408:
    print(f"Error: Request Timeout: {response.status_code}")
elif response.status_code == 500:
    print(f"Error: Internal Error: {response.status_code}")
else:
    print(f"Error: Unexpected status code: {response.status_code}")

## Clear space removing redundant variables
del response
```

## <span style="color:green">Step 2d: Plot the downlaoded DEM</span>

```python
## Open the DEM data
with rasterio.open(dem_filepath) as src:
    # Read the DEM data (this is a numpy array)
    dem_data = src.read(1)
    dem_transform = src.transform
    print(f"DEM CRS: {src.crs}")
    print(f"DEM Transform: {src.transform}")
    print("CRS object :", src.crs)          # full CRS object
    print("EPSG code  :", src.crs.to_epsg()) 

    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))

    ## Plot the DEM data using imshow from matplotlib and add the extent
    im = ax.imshow(dem_data, cmap='viridis', origin='upper', extent=[dem_transform[2], dem_transform[2] + dem_transform[0] * dem_data.shape[1],
                                                                   dem_transform[5] + dem_transform[4] * dem_data.shape[0], dem_transform[5]])

    ## Plot the watershed on top of the DEM
    bb_gdf.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=2)

    ## Create a colorbar associated with the imshow object
    plt.colorbar(im, ax=ax, label='Elevation (m)', shrink=0.5)

    ## Set title
    plt.title(f'DEM Data from OpenTopography\n({selected_raster_name})')

    ## Show the plot
    plt.show()
```

## <span style="color:green">Step 3a: Reprojecting merged raster to UTM using calculated zone</span>


Reprojecting a raster ensures its grid aligns with the map projection used by other spatial layers, preventing spatial offsets. Tt converts cell sizes and coordinates into the desired CRS so distance, area, and slope calculations are numerically correct. Consistent projection is essential for overlay analyses, mosaicking, and accurate map visualization across datasets.

<ul>
<li> Using the string created for EPSG (by calculated zone value), reproject it to PCS  </li>
<li> Calculate the zone value (below calculations applciable to conterminous US) </li>

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
                reproject(source=rasterio.band(src,i),
                          destination=rasterio.band(dst,i),
                          src_transform=src.transform,
                          src_crs=src.crs,
                          dst_transform=transform,
                          dst_crs=target_crs_proj,
                          resampling=Resampling.nearest)
        print(f"Reprojection of raster complete to {target_crs} projected CRS.")
reprojected_raster_filename=f'{folder_results}/reprojected_{unique_name}_{selected_raster_code}.tif'
## WRITE CODE BELOW
reproject_raster_func(dem_filepath,reprojected_raster_filename,crs_string)
```

## <span style="color:green">Step 3b: Plot the reprojected raster</span>

```python
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
    ax.set_title(f"Reprojected Raster DEM in EPSG: {crs_string} Projected CRS\n(for {selected_raster_name})")
## Uee the reprojected watershed shapefile
bb_gdf.to_crs(crs_string).plot(ax=ax,
                    facecolor='none',
                    edgecolor='red',
                    linewidth=5)
src.close()
del mapped,im,fig,ax,src
```

## <span style="color:green">Step 4a: Creating Topographic Wetness Index(TWI) raster</span>

We will use PyWBT, a Python wrapper around the WhiteboxTools (WBT) geospatial analysis library. First, let us create a dictionary whose keys are WhiteboxTools command names and whose values are the exact command-line arguments you would pass to each tool. Then, PyWBT then runs the tools in the order they appear in that dictionary, piping the outputs from one step into the next.
<ul>
<li> Breach Depressions (Alternative to Fill Sinks) : Removes all sinks and flats by cutting through barriers instead of filling them, so every cell has a downhill path.</li>
<li> D8Pointer: Creates a flow-direction grid (D8), assigning each cell the code of the downslope neighbour it drains to.</li>
<li> DownslopeFlowpathLength: Computes, for every cell, the total length of its downslope flow path to an outlet. Useful for hydrologic indices and erosion models.</li>
<li> D8Flow Accumulation: Calculates specific contributing area (SCA) using the D8 directions—i.e. the upslope area per unit contour length contributing to each pixel.</li>
<li> Slope: Derives slope from the corrected DEM.   </li>
<li> TWI: Combines SCA and slope to produce the Topographic Wetness Index (TWI): TWI = ln(SCA / tan β).</li>

```python
src_dir = Path(reprojected_raster_filename)
print(src_dir)

src_dir.parent.mkdir(parents=True, exist_ok=True)

wbt_args = {
    "BreachDepressions": [f"-i={src_dir.name}", "--fill_pits", f"-o=dem_corr_{unique_name}_{selected_raster_code}.tif"],
    "D8Pointer": [f"-i=dem_corr_{unique_name}_{selected_raster_code}.tif", f"-o=fdir_{unique_name}_{selected_raster_code}.tif"],
    "DownslopeFlowpathLength": [f"--d8_pntr=fdir_{unique_name}_{selected_raster_code}.tif", f"-o=downslope_fp_length_{unique_name}_{selected_raster_code}.tif"],
    "D8FlowAccumulation": [f"-i=fdir_{unique_name}_{selected_raster_code}.tif", "--pntr", "--out_type='specific contributing area'", f"-o=sca_{unique_name}_{selected_raster_code}.tif"],
    "Slope": [f"-i=dem_corr_{unique_name}_{selected_raster_code}.tif", "--units=radians", f"-o=slope_{unique_name}_{selected_raster_code}.tif"],
    "WetnessIndex": [f"--sca=sca_{unique_name}_{selected_raster_code}.tif", f"--slope=slope_{unique_name}_{selected_raster_code}.tif", f"-o=twi_{unique_name}_{selected_raster_code}.tif"],
}
```

## <span style="color:green">Step 4b: Run each tool in order </span>


```python
input_dir=folder_results
#print(input_dir)

## WRITE THE CODE BELOW
with tempfile.TemporaryDirectory(dir=str(folder_results)) as temp_dir:
    pywbt.whitebox_tools(input_dir,
                         wbt_args,
                         save_dir=input_dir,
                         max_procs=1)
```

## <span style="color:green">Step 4c: Plot the TWI and intermediate outputs </span>


```python
with rasterio.open(f"{folder_results}/twi_{unique_name}_{selected_raster_code}.tif") as src1:
    twi2 = src1.read(1)
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
    ax.set_title(f"Topographic Wetness Index (TWI) in EPSG: {crs_string} Projected CRS\n(for {selected_raster_name})")

## Uee the reprojected watershed shapefile
bb_gdf.to_crs(crs_string).plot(ax=ax,
                    facecolor='none',
                    edgecolor='red',
                    linewidth=5)
del src1,fig,ax
```

```python
## Define the file paths for the different rasters

raster_files = {
    "Reprojected DEM Raster": [f"{folder_results}/reprojected_{unique_name}_{selected_raster_code}.tif",'Elevation (in meters)'],
    "Breach Depressions Filled Raster": [f"{folder_results}/dem_corr_{unique_name}_{selected_raster_code}.tif",'Elevation (in meters)'],
    "D8 Flow Direction Raster": [f"{folder_results}/fdir_{unique_name}_{selected_raster_code}.tif",'Index from 1 to 128'],
    "Flow Accumulation Raster (Specific Contributing Area)": [f"{folder_results}/sca_{unique_name}_{selected_raster_code}.tif",'Count of Cells/ meter'],
    "Slope Raster": [f"{folder_results}/slope_{unique_name}_{selected_raster_code}.tif",'Slope (Radians)'],
    "Topographic Wetness Index (TWI) Raster": [f"{folder_results}/twi_{unique_name}_{selected_raster_code}.tif",'TWI (Dimensionless)'],}

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
        bb_gdf.to_crs(crs_string).plot(ax=ax,
                            facecolor='none',
                            edgecolor='red',
                            linewidth=5)
        
        # Add a colorbar specific to this subplot
        cbar = plt.colorbar(im, ax=ax, shrink=0.5)
        cbar.set_label(units)  # Label for the colorbar

# Adjust layout
plt.tight_layout()
plt.show()
```
