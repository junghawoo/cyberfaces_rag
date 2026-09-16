---
title: "Test - Geospatial Analysis (LULC Change)"
unit_id: 202
course_id: 0
level: "Developer"
slug: test-geospatial-analysis-lulc-change
is_course: 0
---

# Test - Geospatial Analysis (LULC Change)

## Extracted resources (local files)

### BlankPage
*Source file:* `BlankPage.pdf`  ·  *type:* file

_[no extractable text]_

### Solution_DA3_DEM_Access_v2
*Source file:* `Solution_DA3_DEM_Access_v2.ipynb`  ·  *type:* file

## <span style="color:green"><h1><center>DEM Accessing using a Shapefile</center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'>We will download DEM raster files from USGS National Elevation Dataset using the extents of watershed shapefile accessed using USGS site number. Later, the DEM raster files will be plotted along with watershed boundary.</p> 

## <span style="color:green"> Data Source </span>

<p style='text-align: justify;'>USGS 1/3 arc second DEM</p>

## <span style="color:green">Overview of steps </span>
<ol type="1">
    <span style="color:red"><li>Using USGS Station Number, get the shapefile for a  basin (watershed) and it extents</li></span>
    <span style="color:red"><li>Download the DEM from USGS-Amazon Web Service</li></span>
     <span style="color:red"><li>Plotting the Unmerged Raster Tiles</li></span>



## <span style="color:green">Import the packages/modules required for this exercise</span>

We need different packages as shown below. It can be either installed using pip method or conda method.


```python
## Import the modules/packages/libraries required
import math
import numpy as np
import os
import matplotlib.pyplot as plt

from pynhd import NLDI
import urllib.request
import progressbar
import rasterio
import rasterio.plot
```

## <span style="color:green">Step 1a: Input USGS Site, DEM resolution, and create a directory</span> 
<ul>
<li>Input: <span style="color:red">USGS Site</span></li>
<li>Input: <span style="color:red">Desired resolution</span></li>
<li>Create: <span style="color:red">Folder for storing input raster files from USGS AWS</span></li>

```python
## Input the USGS site number to get the shapefile
## E.g. "04180000" has a drainage area of 270 sq mi and can downloaded within 2-3 minutes
## But "03335500" has a drainage area of 7267 sq mi and needs for time and space
## WRITE CODE BELOW
site_id ='09241000'
#"09037500" #WILLIAMS FORK NEAR PARSHALL, CO
#07103700	FOUNTAIN CREEK NEAR COLORADO SPRINGS, CO.
#09064500	HOMESTAKE CREEK NEAR RED CLIFF, CO.
#09241000 ELK RIVER AT CLARK, CO.	CO

## Resolution of required DEM
## USGS-AWS has different options like 1/3 arc second (code = 13), 1/9 arc second (code = 19; currently unavailable)
## WRITE CODE BELOW
resolution='13'  

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
## WRITE CODE BELOW
folder_input=f'./input_{site_id}'
check_create_path_func(folder_input)
```

_output:_
```
The new directory [1m'./input_09241000'[0m is not created as it already exists!
```

## <span style="color:green">Step 1b: Input USGS Site and get the basin</span> 

<ul>
<li>Input: <span style="color:red">Get a input station</span></li>
<li>Output: <span style="color:red">Find out the basin</span></li>
<li>Output: <span style="color:red">Save the basin file as shapefile</span></li>
    

```python
## Get the watershed using USGS station number using pynhd module
## WRITE THE CODE BELOW
watershed = NLDI().get_basins(site_id)

## Plot the watershed
## DD indicates latitude/ longitude degrees is followed by immediately followed by decimal
ax = watershed.plot(facecolor="b", 
                    edgecolor="k", 
                    figsize=(8, 8))
plt.title(f"Shapefile corresponding to {site_id} site")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Saving the watershed file as a shapefile at desired location
## WRITE THE CODE BELOW
shapefile_fileloc_filename=f'{folder_input}/shape_{site_id}.shp'
watershed.to_file(filename=shapefile_fileloc_filename,
                  driver= 'ESRI Shapefile',
                  mode='w')
```

_result:_
```
<Figure size 800x800 with 1 Axes>
```

## <span style="color:green">Step 2: Get the extents for downloading DEM</span>

<ul>
<li> Extents of the basin (watershed) is obtained using .total_bounds </li>
<li> Then we will find the bounding extents using math floor and ceil function </li>
    

```python
## Get the min and max of latitude and longitude (or easting and northing)
extents_basin=watershed.total_bounds

## N or S and W or E may become a problem
print(f'Left Bounding Longtitude is {extents_basin[0]:.3f}\u00b0 or {abs(extents_basin[0]):.3f}\u00b0 W')
print(f'Right Bounding Longtitude is {extents_basin[2]:.3f}\u00b0 or {abs(extents_basin[2]):.3f}\u00b0 W')
print(f'Bottom Bounding Latitude is {extents_basin[1]:.3f}\u00b0 or {abs(extents_basin[1]):.3f}\u00b0 N')
print(f'Top Bounding Latitude is {extents_basin[3]:.3f}\u00b0 or {abs(extents_basin[3]):.3f}\u00b0 N')
```

_output:_
```
Left Bounding Longtitude is -107.076° or 107.076° W
Right Bounding Longtitude is -106.635° or 106.635° W
Bottom Bounding Latitude is 40.678° or 40.678° N
Top Bounding Latitude is 40.907° or 40.907° N
```

```python
## DEMs are numbered using integer
## Calculate largest integer that equals or not greater than left and bottom bounds
## WRITE THE CODE BELOW
extent_left=abs(math.floor(extents_basin[0]))
extent_right=abs(math.floor(extents_basin[2]))
## You may be tempted to calculate the ceil of right extent
## But, number scheme is such that 84W indicates data from -84 to -83 deg W

## Calculate smallest integer that equals or not less than right and upper bounds
## WRITE THE CODE BELOW
extent_bottom=abs(math.ceil(extents_basin[1]))
extent_top=abs(math.ceil(extents_basin[3]))
## Similarly, you may be tempted to calculate the floor of bottom extent
## But, number scheme is again such that 40N includes data from +39 to +40 deg N 

## Calulate the number of tiles to be downloaded from USGS
num_tiles_download=(((extent_left+1)-extent_right)*((extent_top+1)-extent_bottom))
print(f"Number of tiles to be downloaded: {num_tiles_download}")
print(f"Left: {extent_left}, Right: {extent_right}, Bottom: {extent_bottom}, Top: {extent_top}")
```

_output:_
```
Number of tiles to be downloaded: 2
Left: 108, Right: 107, Bottom: 41, Top: 41
```

```python
## Create a progress bar for monitoring the download process
class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()
```

## <span style="color:green">Step 3a: Downloading the DEM from USGS-Amazon Web Service</span>

<ul>
<li> Create a for loop anf download the DEM covering the shapefile </li>
<li> Save it in a folder </li>

```python
current_filenum=1

for lon in (range(extent_right,extent_left+1,1)):
    for lat in (range(extent_bottom,extent_top+1,1)):
        usgs_filename=f'n{lat:02d}w{lon:03d}'
        
        print(f'Beginning file {current_filenum} download with urllib2  out of {num_tiles_download}...')
        url = (f'https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF'
               f'/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif'
              )
                
        ## The r in 'fr' disables backslach escape sequence processing
        local_fileloc_filename=fr'{folder_input}/USGS_{resolution}_{usgs_filename}.tif'
        
        ## Retrieve the file using the weblink and local path with file name
        print('Data downloaded from : ')
        print(url)
        ## WRITE THE CODE BELOW
        #urllib.request.urlretrieve(url,local_fileloc_filename) #without progressbar for multiple USGS sites
        urllib.request.urlretrieve(url,local_fileloc_filename,MyProgressBar())
        
        
        print(f'Completed file {current_filenum} download with urllib2 out of {num_tiles_download}...')
        print(f'*************************************************************************************\n')
        
        current_filenum+=1
```

_output:_
```
Beginning file 1 download with urllib2  out of 2...
Data downloaded from : 
https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/current/n41w107/USGS_13_n41w107.tif
```

_output:_
```
100% (380715196 of 380715196) |##########| Elapsed Time: 0:00:17 Time:  0:00:17
```

_output:_
```
Completed file 1 download with urllib2 out of 2...
*************************************************************************************

Beginning file 2 download with urllib2  out of 2...
Data downloaded from : 
https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/current/n41w108/USGS_13_n41w108.tif
```

_output:_
```
100% (401527220 of 401527220) |##########| Elapsed Time: 0:00:19 Time:  0:00:19
```

_output:_
```
Completed file 2 download with urllib2 out of 2...
*************************************************************************************
```

## <span style="color:green">Step 3b: Plotting the downloaded (unmerged) DEMs along with watershed shapefile</span>

<ul>
<li> Plot the different DEMs using rasterio package </li>
<li> Also, plot the shapefile of the watershed </li>

```python
fig, ax = plt.subplots(figsize=(8, 8))

for lon in range(extent_right,extent_left+1,1):
    for lat in range(extent_bottom,extent_top+1,1):
        usgs_filename=f'n{lat:02d}w{lon:03d}'
        ## WRITE THE CODE BELOW
        local_raster_filename=fr'{folder_input}/USGS_{resolution}_{usgs_filename}.tif'
        raster = rasterio.open(local_raster_filename)
        rasterio.plot.show(raster,
                           ax=ax,
                           cmap='viridis')
        #print(f'lat: {lat},lon: {lon},file:{local_fileloc_filename}')
watershed.plot(ax=ax, 
           facecolor='none', 
           edgecolor='red')
plt.title("Unmerged Raster DEMs")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

```

_result:_
```
Text(53.722222222222214, 0.5, 'Longitude (DD)')
```

_result:_
```
<Figure size 800x800 with 1 Axes>
```

## Fetched resources (external URLs)

### Test JN File (notebook)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/main/Coursepage_DA3_DEM_Access_v3.ipynb

## <span style="color:green"><h1><center>DEM Accessing using a Shapefile</center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'>We will download DEM raster files from USGS National Elevation Dataset using the extents of watershed shapefile accessed using USGS site number. Later, the DEM raster files will be plotted along with watershed boundary.</p> 

## <span style="color:green"> Data Source </span>

<p style='text-align: justify;'>USGS 1/3 arc-second DEM</p>

## <span style="color:green">Overview of steps </span>
<ol type="1">
    <span style="color:red"><li>Using USGS Station Number, get the shapefile for a  basin (watershed) and it extents</li></span>
    <span style="color:red"><li>Download the DEM from USGS-Amazon Web Service</li></span>
     <span style="color:red"><li>Plotting the Unmerged Raster Tiles</li></span>



## <span style="color:green">Import the packages/modules required for this exercise</span>

We need different packages as shown below. It can be either installed using pip method or conda method.


```python
## Import the modules/packages/libraries required
import math
import numpy as np
import os
import matplotlib.pyplot as plt

from pynhd import NLDI
import urllib.request
import progressbar
import rasterio
import rasterio.plot
```

## <span style="color:green">Step 1a: Input USGS Site, DEM resolution, and create a directory</span> 
<ul>
<li>Input: <span style="color:red">USGS Site</span></li>
<li>Input: <span style="color:red">Desired resolution</span></li>
<li>Create: <span style="color:red">Folder for storing input raster files from USGS AWS</span></li>

```python
## Input the USGS site number to get the shapefile
## E.g. "04180000" has a drainage area of 270 sq mi and can downloaded within 2-3 minutes
## But "03335500" has a drainage area of 7267 sq mi and needs for time and space
## WRITE CODE BELOW
site_id='04180000' # Cedar Creek

## Resolution of required DEM
## USGS-AWS has different options like 1 arc-second (code = 1), 1/3 arc-second (code = 13), 1/9 arc-second (code = 19; currently unavailable)
## WRITE CODE BELOW
resolution='1'  

## Define a function for making a directory depending on whether it exists or not.
## We are creating a function so that it can be used later for creating three folders in the later modules
def check_create_path_func(path):
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print(f"The new directory \033[1m'{path}'\033[0m is created!")
    else:
        print(f"The new directory \033[1m'{path}'\033[0m is not created as it already exists!")
        
## Create a folder for storing DEMs using the earlier defined function
folder_input=f'./input_{site_id}'
## WRITE CODE BELOW

```

## <span style="color:green">Step 1b: Input USGS Site and get the basin</span> 

<ul>
<li>Input: <span style="color:red">Get a input station</span></li>
<li>Output: <span style="color:red">Find out the basin</span></li>
<li>Output: <span style="color:red">Save the basin file as shapefile</span></li>
    

```python
## Get the watershed using USGS station number using pynhd module
## WRITE THE CODE BELOW


## Other feature sources
## ‘nwissite’ for USGS NWIS Surface Water Sites (default)
## ‘comid’ for NHDPlus comid.
## ‘ca_gages’ for Streamgage catalog for CA SB19
## ‘gfv11_pois’ for USGS Geospatial Fabric V1.1 Points of Interest
## ‘huc12pp’ for HUC12 Pour Points
## ‘nmwdi-st’ for New Mexico Water Data Initative Sites
## ‘nwisgw’ for NWIS Groundwater Sites
## ‘ref_gage’ for geoconnex.us reference gages
## ‘vigil’ for Vigil Network Data
## ‘wade’ for Water Data Exchange 2.0 Sites
## ‘WQP’ for Water Quality Portal

## Plot the watershed
## DD indicates latitude/ longitude degrees is followed by an immediate by a decimal
ax = watershed.plot(facecolor="b", 
                    edgecolor="k", 
                    figsize=(8, 8))
plt.title(f"Shapefile corresponding to {site_id} site")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Saving the watershed file as a shapefile at the desired location
shapefile_fileloc_filename=f'{folder_input}/shape_{site_id}.shp'
watershed.to_file(filename=shapefile_fileloc_filename,
                  driver='ESRI Shapefile',
                  mode='w')

```

## <span style="color:green">Step 2: Get the extents for downloading DEM</span>

<ul>
<li> Extents of the basin (watershed) is obtained using .total_bounds </li>
<li> Then we will find the bounding extents using math floor and ceil function </li>
    

```python
## Get the min and max of latitude and longitude (or easting and northing)
extents_basin=watershed.total_bounds

## N or S and W or E may become a problem
print(f'Left Bounding Longtitude is {extents_basin[0]:.3f}\u00b0 or {abs(extents_basin[0]):.3f}\u00b0 W')
print(f'Right Bounding Longtitude is {extents_basin[2]:.3f}\u00b0 or {abs(extents_basin[2]):.3f}\u00b0 W')
print(f'Bottom Bounding Latitude is {extents_basin[1]:.3f}\u00b0 or {abs(extents_basin[1]):.3f}\u00b0 N')
print(f'Top Bounding Latitude is {extents_basin[3]:.3f}\u00b0 or {abs(extents_basin[3]):.3f}\u00b0 N')
```

```python
## DEMs are numbered using integer
## Calculate the largest integer that equals or not greater than left and bottom bounds
extent_left=abs(math.floor(extents_basin[0]))
extent_right=abs(math.floor(extents_basin[2]))
## You may be tempted to calculate the ceil of right extent
## But, number scheme is such that 84W indicates data from -84 to -83 deg W

## Calculate the smallest integer that equals or not less than right and upper bounds
extent_bottom=abs(math.ceil(extents_basin[1]))
extent_top=abs(math.ceil(extents_basin[3]))
## Similarly, you may be tempted to calculate the floor of bottom extent
## But, number scheme is again such that 40N includes data from +39 to +40 deg N 

## Calculate the number of tiles to be downloaded from USGS
num_tiles_download=(((extent_left+1)-extent_right)*((extent_top+1)-extent_bottom))
print(f"Number of tiles to be downloaded: {num_tiles_download}")
print(f"Left: {extent_left}, Right: {extent_right}, Bottom: {extent_bottom}, Top: {extent_top}")
```

```python
## Create a progress bar for monitoring the download process
class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()
```

## <span style="color:green">Step 3a: Downloading the DEM from USGS-Amazon Web Service</span>

<ul>
<li> Create a for loop and download the DEM covering the shapefile </li>
<li> Save it in a folder </li>

```python
current_filenum=1

for lon in (range(extent_right,extent_left+1,1)):
    for lat in (range(extent_bottom,extent_top+1,1)):
        usgs_filename=f'n{lat:02d}w{lon:03d}'
        
        print(f'Beginning file {current_filenum} download with urllib2  out of {num_tiles_download}...')
        url = (f'https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF'
               f'/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif'
              )
                
        ## The r in 'fr' disables backslach escape sequence processing
        local_fileloc_filename=fr'{folder_input}/USGS_{resolution}_{usgs_filename}.tif'
        
        ## Retrieve the file using the weblink and local path with file name
        print('Data downloaded from: ')
        print(url)
        ## WRITE THE CODE BELOW
        #urllib.request.urlretrieve(url,local_fileloc_filename) #without progressbar for multiple USGS sites
               
        
        
        print(f'Completed file {current_filenum} download with urllib2 out of {num_tiles_download}...')
        print(f'*************************************************************************************\n')
        
        current_filenum+=1
```

## <span style="color:green">Step 3b: Plotting the downloaded (unmerged) DEMs along with watershed shapefile</span>

<ul>
<li> Plot the different DEMs using rasterio package </li>
<li> Also, plot the shapefile of the watershed </li>

```python
fig, ax = plt.subplots(figsize=(8, 8))

for lon in range(extent_right,extent_left+1,1):
    for lat in range(extent_bottom,extent_top+1,1):
        usgs_filename=f'n{lat:02d}w{lon:03d}'
        local_raster_filename=fr'{folder_input}/USGS_{resolution}_{usgs_filename}.tif'
        raster=rasterio.open(local_raster_filename)
        rasterio.plot.show(raster,
                           ax=ax,
                           cmap='viridis'#different option - magma
                          )
        #print(f'lat: {lat},lon: {lon},file:{local_fileloc_filename}')
watershed.plot(ax=ax, 
           facecolor='none', 
           edgecolor='red')
plt.title("Unmerged Raster DEMs")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

```
