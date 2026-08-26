---
title: "Accessing elevation data from National Elevation Dataset (NED)"
unit_id: 12
course_id: 4
level: "Developer"
slug: accessing-elevation
is_course: 0
---

# Accessing elevation data from National Elevation Dataset (NED)

## Extracted resources (local files)

### DA3 Instruction for downloading NED tiles
*Source file:* `DA3 Instruction for downloading NED tiles.pdf`  ·  *type:* file

FAIR CLIMATE AND WATER SCIENCE 
Module DA3: Data Access (DA) for Water Science 
Downloading Digital Elevation Model from National Elevation Dataset 
Prepared by Sayan Dey and Venkatesh Merwade 
Lyles School of Civil Engineering, Purdue University 
dey6@purdue.edu, vmerwade@purdue.edu 
 
1. INTRODUCTION 
Digital Elevation Models (DEMs) are the most common representation of topography in 
hydrologic and hydrodynamic applications. The United States Geological Survey (USGS) has 
created the National Elevation Dataset (NED), which provides seamless topographic 
representation of the entire Continental United States (CONUS). The NED is available for 
download in the form of tiles of size 1° × 1° (latitude-longitude). 
The objective of this exercise is to learn to access and download NED tiles overlapping a study 
area programmatically. This may involve the automated download of multiple NED tiles, 
depending on the size and location of the study area. Students are expected to have a basic 
understanding of GIS file formats (raster, shapefile) and Python. 
2. COMPUTER REQUIREMENTS 
You must have a web browser, connection to the internet and login credentials for an account 
on www.mygeohub.org.  
3. DATA REQUIREMENTS 
The key data required for this exercise is a polygon shapefile depicting the region of interest 
(study area) for which the DEM is to be downloaded. An example shapefile (Boundary.shp) is 
made 
available 
for 
this 
exercise 
in 
a 
public 
folder 
at: 
“/srv/projects/cybertrainingfair/files/public/FAIR_Data_Access/NED_DEM_Download” 
The example shapefile is a sub-watershed of the Wabash River, with its outlet at West 
Lafayette, IN. You can use any polygon shapefile for this exercise provided it only contains 
one polygon feature and the polygon feature is a simple polygon. 
You are also provided with a jupyter notebook, for this exercise. It has code for initializing 
PyQGIS, and some user defined functions that you will be using to download the NED tiles. 
The main code, where you call the user-defined function, is incomplete and you will be guided 
by this tutorial to complete the code and programmatically download the NED files.  
4. GETTING STARTED 
Working with geospatial data requires the use of geographic information systems (GIS). Here 
we use QGIS, an open source and free GIS software. Python support is available for QGIS 
through its Python QGIS API called PyQGIS (if you are interested in some additional reading,

visit: https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/). PyQGIS is already 
installed in the mygeohub Jupyter notebook. 
 
4.1 Initialize PyQGIS 
Make sure the kernel is set to [conda: qgis] by clicking on Tools >> kernel >> [conda:qgis]. 
The first task is to initialize PyQGIS which is established with the following code. Make sure 
to run this cell only once per session. 
 
Figure 1: Initializing PyQGIS in Jupyter notebook 
Note: Running this cell again (when PyQGIS is already initialized) may crash the kernel. If 
that happens, restart the kernel, clear all outputs and then run this cell once.  
4.2 Import libraries and provide inputs 
 The next step is to import libraries (modules) that will be used for carrying out specific tasks 
throughout the notebook. Import the four libraries as shown below in a new cell. 
 
Figure 2: Importing libraries (modules) 
The ftplib module is used for connecting to ftp sites and searching and accessing their contents. 
The math module provides access to simple math functions such as sum, mean, floor among 
others. The zipfile module is used for zipping and unzipping zip files. Finally, shutil module 
contains functions for operations on files, folders or collection of files. 
Next, we need to provide the code with the location of input and work folders and the name of 
the input shapefile as shown in Figure 3 below. The input folder is the one which has the 
shapefile. The work folder contains all intermediate and final files.  
Make sure to include .shp in the boundary file name. If you are using absolute paths to define 
your work folder, note that the path will follow the syntax: /home/mygeohub/<mygeohub 
id>/<path to the folder where shapefile is located>. In the example, I have created a folder 
named “QGIS_Modules” in my home folder (my username is dey6) as my work folder in

Figure 3(a). Alternatively, if you are using relative path, simply define your work folder using 
“./” as shown in Figure 3(b). 
 
Figure 3(a): Defining path and variable names 
 
Figure 3(b): Defining path or variable names with relative path 
4.3 User-defined functions 
We define two user-defined functions: one for unzipping zipped files (UnzipNED) and one 
for downloading NED (DownloadNED) tiles. These are provided in init_NED_code.ipynb. 
They are explained below: 
DownloadNED: This user-defined function takes in as input two integers – latitude and 
longitude – and downloads the NED tile corresponding to that latitude and longitude. It then 
returns the filename of the downloaded zip file.  
The function first connects to the NED ftp site (rockyftp.cr.usgs.gov) and then navigates to the 
folder where the zipped NED tiles are stored in the ftp server. In that folder, it searches and 
downloads the zipped file with the string “n<lat>w<long>” in its name (explained in more 
detail in Section 4.4). In case there are more than one zipped file with the same string in its 
name, it downloads the one that is largest in size.

Figure 4: User-defined function for downloading NED files. 
 
UnzipNED: This user-defined function (Figure 5) takes a zipped filename as input and unzips 
it. The zipped file must be located in the work folder. The unzipped files are also extracted in 
the work folder. 
 
Figure 5: User-defined function for unzipping zipped files.

4.4 Determining NED tiles to be downloaded 
We use these user-defined functions to download all the NED tiles that cover our study area.  
First, we need to identify the NED tiles that overlap the input polygon and make a list of 
latitudes and longitudes corresponding to those tiles. Each NED tile follows a naming 
convention such that its name contains the string “n<YY>w<XXX>”. This string, henceforth 
referred to as the name string, indicates the location and coverage of that tile. 
A NED tile with the name string “n<YY>w<XXX>” cover a 1° × 1° spatial extent spanning 
(YY-1) to YY and (XXX-1) to XX. For example, a tile with the name string “n41w087” covers 
the region between latitudes 40°N to 41°N and 86°W to 87°W as shown in Figure 6 below. 
Note that XXX and YY are always positive and refer to west longitudes and north latitudes 
respectively.  
 
Figure 6: Figure showing a NED DEM tile with the name string “n41w087”

To identify the NED tiles to be downloaded, we find the extents of the boundary polygon, that 
is, we find the northmost and southmost latitudes and the eastmost and westmost longitudes 
that enclose the polygon. This requires 3 steps: 
1) Convert the coordinate system of the boundary polygon to NAD1983 coordinate system 
(EPSG 4326): This can be implemented using the “native:reprojectlayer” tool in pyqgis. 
Tools in pyqgis are deployed by using the processing module (Figure 7). In this case, 
the python command is: 
processing.run(‘native:reprojectlayer’,{‘INPUT’: 
<input 
file 
name>, 
‘TARGET_CRS’: <target coordinate system>, ‘OUTPUT’: <output file name>}).  
For more information on the “native:reprojectlayer” tool, please refer to the link below: 
https://docs.qgis.org/3.16/en/docs/user_manual/processing_algs/qgis/vectorgeneral.ht
ml?highlight=native%20reprojectlayer#reproject-layer  
 
2) Create a vector layer for the reprojected polygon: we use the pyqgis command 
QgsVectorLayer() (Figure 7). The syntax is: 
layer = QgsVectorLayer(<input file>, <name of layer>, ‘ogr’) 
 
3) Access the extent object associated with a polygon object in QGIS to extract the bounds. 
You can access the extent object by using the code layer.extent() (Figure 7). 
 
The extent object has attributes, xMaximum, xMinimum, yMaximum and yMinimum, that 
allow us access these bounds. For example, print(ext.xMaximum) will return the westmost 
longitude. 
Once you have printed them, check Figure 7 for a possible solution or check with Figure 8 to 
see if your values are correct. 
 
 
Figure 7: Solution for determining the NED tiles to be downloaded

Figure 8: Figure showing location of input polygon which can be used to check the bounds 
printed using your code 
 
Once the extents are known, we can use the fact that NED tiles are 1° × 1° in size to populate 
the list of latitudes and longitudes for the relevant NED tiles to be downloaded for the input 
polygon? For example, list_long = [87,88] in this case. 
Bonus Exercise: Can you come up with a mathematical formula for automatically populating 
the list? (Hint: Taking the ceiling or the floor (depending on the location) provides the integer 
latitude and longitude that make the bounds completely containing the input boundary polygon. 
Use the range function to generate all intermediate latitude and longitudes.) 
Solution:  
 
Figure 9: Determining list of NED tiles for download based on extents

4.5 Looping through download and unzipping of NED tiles 
 
We find and download all the 1° × 1° NED tiles that overlap the bounds of the boundary 
polygon by looping across all integer latitudes and longitudes contained in the bounds. For 
each set of integer latitude and longitude, we get one NED tile. The latitude-longitude pairs are 
fed one by one to the DownloadNED function which downloads the relevant zipped NED tile. 
The output of DownloadNED is the file name of the downloaded zipped file which is fed into 
UnzipNED which then unzips these files. 
Create for-loops to go through the list of latitudes and longitudes created in Exercise 1 and call 
the DownloadNED and UnzipNED functions at appropriate places in the code for downloading 
all NED tiles overlapping with the input polygon. Provide appropriate print statements and 
comments to keep track of the progress of downloads.  
 
Figure 10: Downloading tiles by repeatedly calling DownloadNED and UnzipNED 
 
After running the code, you should get messages similar to Figure 11.  
 
Figure 11: Figure showing messages displayed while downloading NED tiles 
 
Next, go to your work folder (work_folder_name). Inside the work folder, you should find all 
the tiles (both zipped and unzipped) that overlap the input polygon boundary as shown in figure 
12.

Figure 12: Intermediate and final files in the work folder 
 
 
These tiles need to be preprocessed into a single DEM with the same coordinate system as the 
input boundary polygon before they can be used in any application, which we will do in the 
Data Processing Modules. Additionally, we will work on visualizing the DEM and polygon in 
the visualization module. 
Ok, you are done… for now!!!

## Image text (OCR)

### `FAIR_data_principles.jpg`
Bee J \ccessible —

R
oy
%

e

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA3-NED_Download/Coursepage_DA3_DEM_NED_Download_v2_Exercise.ipynb

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

```python
# IMPORT LIBRARIES
import ftplib, math, zipfile, shutil
```

```python
# USER INPUTS
input_folder_name = "/home/mygeohub/dey6/QGIS_Modules/DEM_Download/Class59100_B6/Input"
output_folder_name = "/home/mygeohub/dey6/QGIS_Modules/DEM_Download/Class59100_B6/Output" 
boundary_file =  "B6_simplify.shp"
```

```python
# USER DEFINED FUNCTION FOR DOWNLOADING TILES
def DownloadNED(lat,lon):
    lat = str(lat)
    if lon<100:
        lon = "0"+str(lon)
    else:
        lon = str(lon)    
    name = "n"+lat+"w"+lon
    with ftplib.FTP('rockyftp.cr.usgs.gov') as ftp:
        try:
            ftp.login()
            ftp.cwd('vdelivery/Datasets/Staged/Elevation/1/ArcGrid/')
            contents = ftp.nlst()
            filtered_contents = [f for f in contents if ((name in f) & (".zip" in f))]
            if len(filtered_contents) == 0:
                print("No file found for: " + name)        
            elif len(filtered_contents) == 1:
                final_file = filtered_contents[0]
                print("1 file found for current tile")
                print("Downloading " + final_file)
                fo = open(os.path.join(work_folder_name, final_file), 'wb')
                ftp.retrbinary("RETR " + final_file , fo.write)
                fo.close() 
                print("Download successful")
                return(final_file)                
            elif len(filtered_contents) > 1:
                print("More than 1 file found: Dowloading largest zip file")
                file_list = []
                ftp.sendcmd("TYPE i")
                for f in filtered_contents:
                    file_list.append((f,ftp.size(f)))
                file_list.sort(key=lambda s: s[1])
                final_file = file_list[-1] #return the largest file
                print("Downloading..." + final_file)
                fo = open(os.path.join(work_folder_name, final_file), 'wb')
                ftp.retrbinary("RETR " + final_file , fo.write)
                fo.close()
                print("Download successful")
                return(final_file)
            else:
                print("Unknown error with file download for:" + name)           
            
        except ftplib.all_errors as e:
            print('FTP error:', e)
    
```

```python
# USER DEFINED FUNCTION FOR UNZIPPING DOWNLOADED TILES
def UnzipNED(f):
    try:
        zfile1 = zipfile.ZipFile(work_folder_name + "/" + f, 'r')
        zfile1.extractall(work_folder_name)
        zfile1.close()
        print("NED unzipped successfully: " + f)
    except:
        print("Error in unzipping: " + f)
    
    
```

```python
# MAIN CODE STARTS
work_folder_name = os.path.join(input_folder_name, "WorkFolder")
if os.path.exists(work_folder_name) == False:
    os.mkdir(work_folder_name)
boundary_path = os.path.join(input_folder_name, boundary_file)
input_crs = QgsVectorLayer(boundary_path, '', 'ogr' ).crs().authid()
#processing.run('qgis:reprojectlayer',{'INPUT': full_input_path, 'TARGET_CRS':'EPSG:102673','OUTPUT': folder_name + "boundary_proj.shp"})
processing.run('native:reprojectlayer',{'INPUT': boundary_path, 'TARGET_CRS':'EPSG:4326','OUTPUT': work_folder_name + "/boundary_proj.shp"})

ext = QgsVectorLayer(work_folder_name + "/boundary_proj.shp", '', 'ogr' ).extent()
# print the extents here (Exercise 1)
print(ext.xMaximum())

# generate list of intermediate latitudes and longitudes (Exercise 2)
listNL= [] # list of latitudes for NED name string
listWL= [] # list of longitudes for NED name string
```

```python
# Looping through tiles to download
raster_names = [] # this is used to store the name of the rasters downloaded
for i in listNL:
    for j in listWL:
        # Exercise 3
        # call DownloadNED (input the parameters in correct order and save the returned value in a variable)
        # call UnzipNED (input file name generated in previous step)
        raster_names.append("grdn"+lat+"w"+lon + "_1") # storing names of downloaded rasters
print("Tile processing complete...")
```

```python
#Clean Up (run if you want to shut down qgis)
qgs.exitQgis()
```
