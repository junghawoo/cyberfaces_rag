---
title: "Creating curve number (CN) grid from landuse and soil data"
unit_id: 112
course_id: 4
level: "Developer"
slug: creating-curve
is_course: 0
---

# Creating curve number (CN) grid from landuse and soil data

## Extracted resources (local files)

### Creating Curve Number Grid from soil and landuse using PyQGIS
*Source file:* `CN_Grid_Creation_Instructions.pdf`  ·  *type:* file

FAIR CLIMATE AND WATER SCIENCE 
Creating Curve Number Grid from soil and landuse using PyQGIS  
Prepared by Sayan Dey and Venkatesh Merwade 
Lyles School of Civil Engineering, Purdue University 
 
1. INTRODUCTION 
Curve number (CN) is used to partition the precipitation on a grid into runoff. It is usually created 
using a lookup table that assigns curve number to a location (grid cell) based on the landuse and 
soil properties of that location. In this exercise, we create CN grid for a given area of interest 
defined by a polygon shapefile. This consists of 3 steps: 
i) 
Reclassifying National Land Cover Dataset (NLCD) raster  
ii) 
Creating soil raster from vector gSSURGO (gridded Soil Survey Geographic) data 
iii) 
Combining soil and landuse to calculate CN using a lookup table 
2. DATA REQUIREMENTS 
You are provided with a jupyter notebook, CN_Grid_Markdown_Exercise.ipynb, in mygeohub for 
this exercise. It has code for initializing PyQGIS and implements PyQGIS functions for creating 
CN. You will be guided by this tutorial to make some changes to the jupyter notebook to run the 
code. 
All data needed for this exercise are provided to you in a public folder, whose address is as follows: 
“/srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/CN_Grid” 
You are provided with the following files for this exercise in the public folder: 
i) 
Boundary shapefile (Boundary.shp) – This is a polygon shapefile denoting the 
watershed boundary 
 
ii) 
Soil data shapefile (Soil.shp) – This is a polygon shapefile containing gSSURGO data. 
It contains multiple features, each belonging to a specific soil type. There is a field 
named “HSG_Index” which stores the Hydrologic Soil Group. It is an integer field (1 
– HSG A, 2 – HSG B, 3 – HSG C and 4 – HSG D). For the sake of simplicity, A/D, 
B/D and C/D have been merged with A, B and C respectively.  
 
iii) 
Landuse raster (LU.tif) – GeoTiff file containing NLCD data. It is an integer raster with 
values 11 to 95, each denoting a specific landuse.  
 
iv) 
Curve Number Lookup Table (LookUp.csv) – This is a csv file that provides the CN 
value corresponding to each unique combination of soil group and landuse as shown 
below

LU 
Soil 
CN 
1 
1 
100 
1 
2 
100 
1 
3 
100 
1 
4 
100 
2 
1 
57 
2 
2 
72 
2 
3 
81 
2 
4 
86 
3 
1 
30 
3 
2 
58 
3 
3 
71 
3 
4 
78 
4 
1 
67 
4 
2 
77 
4 
3 
83 
4 
4 
87 
 
 
v) 
Landuse reclassify table (NLCD_reclass.csv) - This is a csv file that shows the 
reclassification rules for NLCD. It has three columns: min, max and value. Each row 
denotes a range of values from the original raster that will be reassigned a new value 
as per the “value” column. The reclassification rules are as follows: 
 
 
3. GETTING STARTED 
First, launch the Jupyter notebook tool from mygeohub. Make sure you are using the kernel Python 
[conda env:qgis]. Click on File >> Save As  and save your jupyter notebook. Refresh the tab to 
remove the Jupyter notebook from “Read Only” mode.  
3.1 Initialize PyQGIS 
The first cell imports the os and sys module and initializes PyQGIS as shown below. Please note 
that this cell only needs to be run once per session.

3.2 Import Libraries 
In addition to PyQGIS, we will also be using pandas.  
 
3.3 Define path and file names for input and output 
The next step is to provide the path to the input files and output folder. The input files are made 
available to you in a public folder, as mentioned in Section 2. You need to assign variables to paths 
of each of the files using os.path.join() as shown in the figure below. Remember, python is case-
sensitive, so be careful with naming of the variables. 
Finally, define your output folder (CN_Grid) in the same folder where your Jupyter notebook is 
saved. Check if the folder already exists using os.path.isdir(), and if it does not, create the folder 
using os.mkdir().

3.3 Check Data  
We need to ensure that input files are in the same coordinate system. You can do this by printing 
out the crs().authid() property of each dataset and check if they match.  
 
Your output should look like the following once you run the cell.  
 
The EPSG code of the Boundary and Soil data should match. 
 
4. PREPARING LANDUSE RASTER 
Landuse provided in this exercise has 15 categories. We will simplify the landuse by reclassifying 
into 4 categories as per the table below.  
 
The information on reclassification rules is provided to PyQGIS through the NLCD_reclass.csv 
file. Print the contents of NLCD_reclass.csv. The code and corresponding output are provided 
below:

The first row means that all values between 9 and 12 in the original landuse data will be allotted 
a value 1 in the reclassified raster. 
4.1 Create table layer for reclassification criterion 
Run the cell as is for creating a table layer from NLCD_reclass.csv.  
 
4.2 Reclassify Landuse Raster 
Now, we are ready to reclassify the raster using the native:reclassifybylayer tool. We use 
processing.run() to run the tool. The jupyter notebook contains a link to the qgis documentation 
that provides the full list of inputs/options for this tool.  
You will need to specify the following arguments: 
'INPUT_RASTER': full path pointing to the original NLCD file provided in the public folder 
'RASTER_BAND': 1, number of bands 
'INPUT_TABLE': table_lyr, 
'MIN_FIELD': 'min', 
'MAX_FIELD': 'max', 
'VALUE_FIELD': 'value' 
'NO_DATA': -9999, 
'RANGE_BOUNDARIES': 0, 
'NODATA_FOR_MISSING': False, 
'DATA_TYPE': 5, 
'OUTPUT': full path for the output file. Make sure the output file has the extension .tif.

Run this cell. Navigate to your output folder and check if the reclassified raster has been created. 
Make sure that its size is greater than zero (for this example, it should be around 36MB) 
 
5. PREPARING SOIL RASTER 
Soil data is available as polygon (vector) dataset. We convert it into raster dataset using 
gdal:rasterize(). For that, we need to specify the extent and resolution of the raster to be created 
5.1 Creating requisite expression for EXTENT 
We need to ensure that the soil raster has the same extent and pixel size (resolution) as the landuse 
raster. This is done using the "EXTENT" argument of gdal:rasterize. 
The EXTENT is a string containing the following formate: “coordinate for west bound, east bound, 
south bound, north bound [CRS Auth ID]”. 
To ensure that landuse and soil have the same extent, we extract these bounds from landuse raster. 
Refer to DEM download module on extracting bounds and coordinate system ID.  
For this case, it should look like: 
'224850.725009,296730.725009,3403431.244106,3516291.244106 [EPSG:26917]'. 
 
 
5.2 Extracting horizontal and vertical resolution of landuse 
Next get the resolution of the landuse raster

5.3 Converting Soil polygon to raster 
Finally, use the gdal:rasterize tool with processing.run() to convert the soil polygons to a raster. 
A list of arguments is given to you in the jupyter notebook. The syntax is similar to the 
native:reclassifybylayer tool used in previous section. 
 
Check the output folder for a new .tif file with size around 36MB. 
 
6. CALCULATING CN FOR EACH CELL 
We create a formula for assigning CN according to the Look Up table. The formula is a string 
that looks as follows: 
 
Bonus: Can you read the look up table from LookUp.csv file and parse the text to automatically 
create the above string from the csv file? Here A is landuse, B is soil.  
OR, you can simply proceed by typing in the above formula. 
Finally, use the gdal:rastercalculator to get the CN grid. It needs the following arguments (similar 
to reclassifybylayer tool) 
'INPUT_A': full path to reclassified landuse raster, 
'BAND_A':1, 
'INPUT_B': full path to soil raster, 
'BAND_B':1, 
'FORMULA': CN formula defined above, 
'NO_DATA':None, 
'RTYPE':4, 
'OPTIONS':'', 
'OUTPUT': full path to output file, make sure the output file is a .tif file

Check for a new file around 36MB in size in your output folder. 
 
EXERCISE: 
You have been provided with a code that plots the raster images. We will generate images for the 
three files we created in this exercise: 
i) 
Reclassified Landuse (lu_reclass_raster.tif) 
ii) 
Soil raster (soil_raster.tif) 
iii) 
CN raster (CN_grid.tif) 
You only need to change the first line. Provide the path to the created file. Example: for CN, the 
path is as shown in the figure below: 
 
Similarly, plot images for the final landuse and soil rasters. The images should look like the 
following.

Landuse 
 
Soil Raster

CN grid 
 
 
OK, you are done!

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP7/CN_Grid_Markdown_Exercise.ipynb

<span><h1><center>Creating Curve Number Grid from Soil and Landuse</center></h1></span>
<center>Prepared by <br>
    <b>Sayan Dey and Venkatesh Merwade</b><br> 
Purdue University<br>
FAIR Science in Water Resources<br></center>

### Initialize PyQGIS 
This code is used for initializing PyQGIS. You only need to execute this once per session.

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

### Import libraries
For this exercise, you will need one additional library: pandas. <br>
Note that os and sys were already imported in the previous cell

### Define path and file names for input and output
The input files are made available to you in a public folder. The path of the public folder is: <span style="color:blue"> /srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/CN_Grid   </span><br>
It has the following files:<br>
1) Boundary shapefile - <span style="color:blue">Boundary.shp  </span><br>
2) Soil data shapefile - <span style="color:blue">Soil.shp    </span><br>
3) Landuse raster - <span style="color:blue">LU.tif    </span><br>
4) Curve Number Lookup Table - <span style="color:blue">LookUp.csv     </span><br>
5) Landuse reclassify table - <span style="color:blue">NLCD_reclass.csv    </span><br>
Assign variables to these filenames (including the full path). You can use <span style="color:blue">_os.path.join()_</span> or string operations.<br>
Finally, define your output folder here. This is where you will store your intermediate files and final output. This should be located in your mygeohub storage space.

### Check Data
Check if geospatial input files are in the same coordinate system

### Preparing Landuse Raster 
The NLCD landuse raster contains many classes ranging from 11 to 95 as per NLCD code. We will be reclassifying these into 4 categories: Water (1), Medium Residential (2), Forest (3) and Agricultural (4). Print the NLCD_reclass.csv file to see the reclassification criterion.

#### Create table layer for reclassification criterion
The following code creates a layer containing the reclassification table using [QgsVectorLayer()](https://qgis.org/pyqgis/3.4/core/QgsVectorLayer.html#qgis.core.QgsVectorLayer) from a delimited file. This layer is required for specifying the reclassification cirterion. The text file needs to be input as a URI (Universal Resource Identifier). The URI for NLCD_reclass.csv is provided below.

```python
# run this cell, no change to be made
table_uri = 'file:///srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/CN_Grid/NLCD_reclass.csv?type=csv&detectTypes=yes&geomType=none&subsetIndex=no&watchFile=no'
table_lyr = QgsVectorLayer(table_uri, "", "delimitedtext")
```

#### Reclassify landuse raster
We will use [native:reclassifybylayer](https://docs.qgis.org/3.4/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html#reclassify-by-layer) with <span style="color:blue">_processing.run()_</span>. <br>
You will need to specify the following arguments: <br>
'INPUT_RASTER': full path to LU.tif,<br>
'RASTER_BAND': 1, <br>
'INPUT_TABLE': table_lyr, <br>
'MIN_FIELD': 'min', <br>
'MAX_FIELD': 'max', <br>
'VALUE_FIELD': 'value' <br>
'NO_DATA': -9999, <br>
'RANGE_BOUNDARIES': 0, <br>
'NODATA_FOR_MISSING': False, <br>
'DATA_TYPE': 5, <br>
'OUTPUT': full path to output file example: output_folder/lu_reclass_raster.tif<br>

```python
processing.run("native:reclassifybylayer", {
    'INPUT_RASTER': landuse_file,'RASTER_BAND':1,
    'INPUT_TABLE': table_lyr,
    'MIN_FIELD':'min','MAX_FIELD':'max','VALUE_FIELD':'value',
    'NO_DATA':-9999,'RANGE_BOUNDARIES':0,'NODATA_FOR_MISSING':False,'DATA_TYPE':5,
    'OUTPUT': os.path.join(output_folder,"lu_reclass_raster.tif")})
print("Landuse raster is ready!")
```

### Create Soil Raster
Soil data is available as polygon (vector) dataset.  We convert it into raster dataset using <span style="color:blue">_gdal:rasterize_</span>. We need to ensure that the soil raster has the same extent and pixel size (resolution) as the landuse raster. This is done using the "EXTENT" argument of <span style="color:blue">_gdal:rasterize_</span>.<br>

#### Creating requisite expression for EXTENT
The EXTENT argument of <span style="color:blue">_gdal:rasterize_</span> needs an expression (string) stating the west, east, south and north bounds of the raster as well as its coordinate system. The string has the syntax:<br>  "west bound, east bound, south  bound, north bound [CRS Auth ID]"<br> 

For this case, it should look like<br> '224850.725009,296730.725009,3403431.244106,3516291.244106 [EPSG:26917]'. <br>

Create a raster layer for the landuse raster. From the layer's extent, extract the coordinate system and bounds to create the string shown above.

#### Extracting horizontal and vertical resolution of landuse
From the landuse layer, get its resolution in X and Y direction using <span style="color:blue">rasterUnitsPerPixelX</span> and <span style="color:blue">rasterUnitsPerPixelY</span> attribute.

#### Converting Soil polygon to raster
Create a vector layer for soil data.
Use <span style="color:blue">_processing.run_</span> to execute <span style="color:blue">_gdal:rasterize_</span>. It has the following arguments: <br>
'INPUT': soil layer, <br>
'FIELD':'HSG_Index', <br>
'BURN':None, <br>
'UNITS':1, <br>
'WIDTH':pixelSizeX, <br>
'HEIGHT':pixelSizeY,  <br>
'EXTENT': expression, <br>
'NODATA':0, <br>
'OPTIONS':'', <br>
'DATA_TYPE':5, <br>
'INIT':None, <br>
'INVERT':False, <br>
'OUTPUT':full path to file where output is saved <br>

Hint: See how the reclassifybylayer tool has been used above.

### Calculating CN for each cell
We are going to use the <span style="color:blue">_gdal:rastercalculator_</span> to calculate the CN value for each corresponding cell of soil and landuse raster. The look up table provides the CN value for each pair of soil and landuse value/category. The information in the look up table needs to be converted to a formula (string) that the raster calculator can use to create the CN raster. <br>

The formula is as follows: <br>
'100* (A==1) + 57* logical_and(A==2, B==1) + 72* logical_and(A==2,B==2) + 81* logical_and(A==2,B==3)  + 86* logical_and(A==2,B==4) + <br> 
                '30* logical_and(A==3, B==1) + 58* logical_and(A==3,B==2) + 71* logical_and(A==3,B==3)  + 78* logical_and(A==3,B==4) + <br>
                '67* logical_and(A==4, B==1) + 77* logical_and(A==4,B==2) + 83* logical_and(A==4,B==3)  + 87* logical_and(A==4,B==4)' <br>

Can you read the look up table from LookUp.csv file and parse the text to create the above string? Here A is landuse, B is soil.

Finally, use the <span style="color:blue">_gdal:rastercalculator_</span> to get the CN grid. It needs the following arguments (similar to reclassifybylayer tool) <br>
'INPUT_A': full path to reclassified landuse raster, <br>
'BAND_A':1, <br>
'INPUT_B': full path to soil raster, <br>
'BAND_B':1, <br>
'FORMULA': CN formula defined above, <br>
'NO_DATA':None, <br>
'RTYPE':4, <br>
'OPTIONS':'', <br>
'OUTPUT': full path to output file, make sure the output file is a .tif file <br>

```python
# Exercise
raster_file = os.path.join(output_folder, "CN_grid.tif") # only edit this line

import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
import rasterio.plot

src=rasterio.open(raster_file)
fig,ax =plt.subplots()
rasterio.plot.show(src,ax=ax)
fig.set_size_inches(10,10)
```
