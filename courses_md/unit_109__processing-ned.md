---
title: "Processing NED data to create elevation dataset for a study area"
unit_id: 109
course_id: 4
level: "Expert"
slug: processing-ned
is_course: 0
---

# Processing NED data to create elevation dataset for a study area

## Extracted resources (local files)

### Processing National Elevation Dataset (NED) tiles to Create Digital Elevation Model
*Source file:* `FAIR_DEM_Processing_With_Exercise.pdf`  ·  *type:* file

FAIR CLIMATE AND WATER SCIENCE 
Module DP6: Data Processing (DP) for Water Science 
Processing National Elevation Dataset (NED) tiles to Create Digital Elevation Model 
Prepared by Sayan Dey and Venkatesh Merwade 
Lyles School of Civil Engineering, Purdue University 
dey6@purdue.edu vmerwade@purdue.edu 
 
1. INTRODUCTION 
Digital Elevation Models (DEMs) are mostly available for download in tiles or chunks. Also, 
they may be in a coordinate system that is different from the one being used in a model. 
Therefore, after DEM tiles are downloaded, they need to undergo significant pre-processing to 
create the final elevation dataset which can be ingested into a hydrologic or hydrodynamic 
model. Commonly, these tiles need to be merged together, referred to as mosaicking, and then 
projected to the and then clipped to the boundary of a study area (area of interest).  
The objective of this exercise is to learn to programmatically pre-process National Elevation 
Dataset (NED) tiles to create a DEM corresponding to a study area boundary. Students are 
expected to have a basic understanding of GIS file formats (raster, shapefile) and Python. While 
this tutorial and the associated code can function standalone, students are recommended to have 
completed the Data Access (DA) module on downloading NED tiles before doing this module. 
2. COMPUTER REQUIREMENTS 
You must have a web browser, connection to the internet and login credentials for an account 
on www.mygeohub.org.  
3. DATA REQUIREMENTS 
There are two datasets required for this exercise: (i) a polygon shapefile depicting the region 
of interest (study area) for which the DEM is to be downloaded and (ii) NED tiles overlapping 
the study region.  
For this tutorial, we are going to use the same polygon shapefile that was used for the DA 
module. It is available at a public server that can be accessed by the following path: 
/srv/projects/cybertrainingfair/files/public/FAIR_Data_Access/NED_DEM_Download/Boun
dary.shp 
The NED tiles for this exercise are also made available in a folder in the same public server: 
/srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/DEM_Processing. 
The 
contents of this folder are same as the output of the DA module on NED download. 
Please note that these are read-only servers, so you do not have permission to write into this 
folder. Any new file/dataset generated during this exercise needs to be saved in your mygeohub 
directory.

You are also provided with a jupyter notebook, DEM_NED_DP_Module_Exercise.ipynb, for 
this exercise. It has code for initializing PyQGIS, and implements PyQGIS functions for 
processing the DEM. You will be guided by this tutorial to make some changes to the jupyter 
notebook to run the code. 
4. GETTING STARTED 
The first cell imports the os and sys module and initializes PyQGIS as shown in Figure 1. 
Please note that this cell only needs to be run once per session. 
 
Figure 1: Initializing PyQGIS in Jupyter notebook 
4.2 Provide inputs 
The next step is to provide the path to the following locations. The input files are made available 
to you in a public folder. You need to assign the paths of the following files/folders to variables: 
(i) The full path to polygon shapefile, Boundary.shp defining the study area is available at 
/srv/projects/cybertrainingfair/files/public/FAIR_Data_Access/NED_DEM_Download  
(ii) The full path to the input folder, that is, the folder containing the individual NED tiles 
overlapping the study area are available at: 
/srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/DEM_Processing  
(iii) Work folder where all intermediate and final files are stored (can be absolute or relative 
path). Please make sure that the folder exists in your local storage. Those using absolute 
paths should note that your mygeohub home is at the address: /home/mygeohub/username  
 
Figure 2(a): User inputs with relative path

4.3 Make a list of raster to be merged 
To merge the raster tiles, we need to first create a list of rasters. Unzipped NED tiles are in 
raster format and their name starts with “grd”. Raster format is essentially a folder containing 
data and associated files for 3D datasets. Therefore, we can populate the list of raster names 
by scanning through the contents of input folder and selecting those folders which start with 
“grd”. Additionally, print the contents of the list to ensure that the list is correctly populated. 
The list should contain two filepaths:  
['/srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/DEM
_Processing/grdn41w087_1', '/srv/projects/cybertrainingfair/files/publi
c/FAIR_Data_Processing/DEM_Processing/grdn41w088_1'] 
 
 
Figure 3: List of rasters to be merged 
 
4.4 Merge Raster tiles 
Now we are going to merge all the NED tiles into a single dataset. This can be done by using 
the gdal:merge algorithm for PyQGIS. This algorithm requires two inputs: a list containing the 
full path to all the DEMs that need to be merged, and the name (with full path) of the output 
file that will be created.  
In pyqgis, tools can be run using the processing.run() function which has the following syntax: 
processing.run(‘tool id’, {parameters}). The tool id is the name of the tool and the parameters 
are unique to each tool. In this case, tool id is “gdal:merge” and parameters required are INPUT 
and OUTPUT. You can see the full list of parameters here: 
https://docs.qgis.org/3.16/en/docs/user_manual/processing_algs/gdal/rastermiscellaneous.htm
l#merge 
Note that this process may take a long time depending on the size and number of NED tiles. 
So, it maybe a good idea to put a print statement after (and/or before) the merge to keep track 
of when the run finishes. In this case, it may take 5-8 minutes to run. Once completed, navigate 
to your work folder. You will find a new geotiff file with the name you specified.

Figure 4: Merging rasters 
 
 4.5 Project Merged Raster 
The next step is to convert the coordinate system of the merged raster to that of the input 
boundary polygon. This can be achieved using the “gdal:warpreproject” algorithm. First, we 
need to identify the target coordinate system, that is, the coordinate system of the shapefile by 
using QgsVectorLayer() to load the shapefile in a layer. We can then use the sourceCrs() 
method to access its coordinate system. 
Once you have the coordinate system, we can execute gdal:warpreproject in the same way as 
gdal:merge using processing.run(). The parameters are INPUT, TARGET_CRS and 
OUTPUT. You can access the full list of parameters here: 
https://docs.qgis.org/testing/en/docs/user_manual/processing_algs/gdal/rasterprojections.html
?highlight=warp%20reproject#warp-reproject 
Upon completion, check the work folder. A new geotiff file should appear there. 
 
Figure 5: Projecting raster 
 
4.6 Clip Raster 
The final step is to clip the raster to the boundary of the study area using the 
“gdal:cliprasterbymasklayer” algorithm. Similar to the previous steps, use processing.run() 
with the parameters INPUT, MASK and OUTPUT. The INPUT is the merged and projected 
raster (output of Section 4.5), MASK is the boundary polygon shapefile that will be used to 
clip the raster and OUTPUT is full path to the file where the clipped raster is stored. For more 
details, refer to the following link: 
https://docs.qgis.org/3.16/en/docs/user_manual/processing_algs/gdal/rasterextraction.html?hi
ghlight=gdal%20cliprasterbymasklayer#clip-raster-by-mask-layer  
 
 
Figure 6: Clipping raster by mask

4.7 Checking the Results 
We have provided code to create a simplistic plot of the final raster and boundary polygon. 
Update the path to the final raster and run the cell to see of the plot looks similar to the figure 
provided below. 
 
Figure 7: Code for plotting final raster and boundary 
 
 
Figure 8: Final plot

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP6/Coursepage_DP6_NED_DP_Markdown_Exercise.ipynb

<span><h1><center>Processing National Elevation Dataset (NED) tiles to Create Digital Elevation Model</center></h1></span>
<center>Prepared by <br>
    <b>Sayan Dey and Venkatesh Merwade</b><br> 
Purdue University<br>
FAIR Science in Water Resources<br></center>

### Initialize PyQGIS 
This code is used for initializing PyQGIS. You only need to execute this once per session. It should print "True" when the cell finishes running.

```python
# INITIALIZE PYQGIS (run once per session)
import sys, os
os.environ['QT_QPA_PLATFORM']='offscreen'
sys.path.append('/opt/conda/envs/ct-fair/share/qgis/python')
from qgis.core import *
from qgis.analysis import QgsNativeAlgorithms
#from qgis.utils import *
# import processing
# from processing.core.Processing import Processing 
from qgis import processing

qgs = QgsApplication([], False)
qgs.initQgis()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms()) 
```

### Define folder and file names for input and output
The input files are made available to you in a public folder. You need to assign the paths of the following files/folders to variables: <br>
1) The full path to polygon shapefile, <span style="color:blue">Boundary.shp </span>, defining the study area is available at <span style="color:blue"> /srv/projects/cybertrainingfair/files/public/FAIR_Data_Access/NED_DEM_Download  </span> <br>
2) The full path to the input folder, that is, the folder containing the individual NED tiles overlapping the study area are available at <span style="color:blue"> /srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/DEM_Processing </span> <br>
3) Work folder where all intermediate and final files are stored (can be absolute or relative path). Please make sure that the folder exists.

```python
# Figure 2(a)
```

### Make list of individual tiles
Make a list of tiles that need to be processed by finding all rasters in the input folder that start with "grd". Note that (i) NED rasters start with the term "grd" and (ii) rasters are essentially folders that contain data.

```python
# Figure 3
```

### Merge raster tiles
Use <span style="color:blue">gdal:merge</span> to merge all the tiles in the list

```python
# Figure 4
```

### Project merged raster
You need to find the coordinate system of the boundary shapefile and then use <span style="color:blue">gdal:warpreproject</span> to project the merged raster to the coordinate system of the boundary shapefile. 

```python
# Figure 5
```

### Clip raster 
Use <span style="color:blue">gdal:cliprasterbymasklayer</span> to clip the raster with boundary shapefile to create the final DEM.

```python
# Figure 6
```

### Create figure of boundary shapefile and final raster
Update the paths of the final DEM. Run the cell to create a figure containing the final raster and boundary shapefile. <br>
The raster should show up in a color gradient and the polygon, in red boundary, should allign with the raster. <br> 
We will delve into details of the code in the Data Visualization module. 

```python
# Figure 7
raster_file = "" # you need to edit this line only. Leave others untouched

import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
import rasterio.plot

poly_gdf = gpd.read_file(boundary_file)
src=rasterio.open(raster_file)
fig,ax =plt.subplots()
rasterio.plot.show(src,ax=ax)
poly_gdf.boundary.plot(ax=ax,facecolor='none', edgecolor='red')

```
