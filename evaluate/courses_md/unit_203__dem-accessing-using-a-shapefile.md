---
title: "Geospatial & Hydrological Science: DEM Accessing using a Shapefile"
unit_id: 203
course_id: 0
level: "Foundation"
slug: dem-accessing-using-a-shapefile
is_course: 0
---

# Geospatial & Hydrological Science: DEM Accessing using a Shapefile

## Module content

---
title: "Introduction"
teaching: 10
exercises: 3
---

:::::::::::::::::::::::::::::::::::::: questions 

- Why QGIS?
- How to start QGIS on HPC Clusters?
- How to load and visualize data in QGIS?
- How to process and export data in QGIS?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Explain why we should use QGIS
- Demonstrate how to start QGIS on HPC Clusters
- Demonstrate how to load and visualize data in QGIS
- Demonstrate how to process and export data in QGIS

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction to QGIS

GIS stands for ‘Geographical Information System’. We can use a GIS application, such as ArcGIS and QGIS to manipulate spatial information. 

QGIS is a free and open-source software that runs on various operating systems. It offers a wide range of functionality, such as vector and raster analysis, geoprocessing, geocoding, georeferencing, web mapping, and 3D visualization. QGIS also supports many data formats and standards, such as Shapefile, GeoTIFF, GeoJSON, WMS, WFS, and PostGIS.

Why QGIS? It's free and flexible.

 1. Cost-free: Enjoy QGIS without any financial burden. It's completely free, no hidden fees.
 2. Free as in "Do It Your Way": You could extend QGIS to meet your specific needs, sponsor development or contribute your own code.
 3. Works where you work: Run QGIS on macOS, Windows, and Linux (so available for HPC Clusters). 
 4. Always getting better: Benefit from rapid development because anyone can add new features and improve on existing ones.
 6. Never get stuck: Access extensive documentation and a large and active supportive community is there for help. 
 7. Easily integrate Artificial Intelligence (AI) and GeoAI.

## Open QGIS on Clusters

We can start QGIS via ThinLinc Client or Gateway. 

#### 1. Start QGIS via ThinLinc

Follow up with [the Setup page](https://rcac-geo.github.io/workshop-qgis/index.html#software-setup), and connect with ThinLinc. There are two ways to start QGIS via ThinLinc. The two ways are fundamentally the same but one is interactive, and the other is typing code.

##### (1) Interactive Way

To open QGIS as an interactive job, we could go to "Cluster Software" and select "QGIS", as the figure below:

<img width="391" alt="Picture1" src="https://github.com/user-attachments/assets/1df48747-d717-442e-9af5-c25d4dc9f78d" />

Then select the "workshop" queue as below:

<img width="406" alt="Screenshot 2025-02-24 at 4 15 16 PM" src="https://github.com/user-attachments/assets/72d72419-4484-4e6e-9fed-3ec2fdf4920d" />

Then hit "No":

<img width="529" alt="Screenshot 2025-02-24 at 4 15 41 PM" src="https://github.com/user-attachments/assets/e3ea5e98-e83e-4d77-ba9c-bba7c62fbea3" />

Now input two cores and five minutes and hit Okay. You don't need to specifically request memory because memory will be relocated proportional with cores. But if you do, include unit such as "4G".

<img width="608" alt="Screenshot 2025-02-24 at 4 16 10 PM" src="https://github.com/user-attachments/assets/55a2b0be-3bc1-447c-a44d-04c4ec6a7e60" />

##### (2) Typing Code Way

We could start the Terminal as below:

<img width="186" alt="Screenshot 2025-02-25 at 9 51 03 AM" src="https://github.com/user-attachments/assets/c06429f8-15b6-4242-b416-080085cf8f23" />

To look up QGIS module, we could do:

```sh
module spider qgis
```

To start an interactive job and open QGIS:

```sh
sinteractive -A workshop -N1 -c8 -t8:00:00
module load qgis
qgis
```



#### 2. Start QGIS via Gateway

Gateway, also named Open OnDemand, is a Web interface includes file explorer, interactive apps including QGIS.​ We have to use our own accounts to login Gateway, not the training accounts we used for this workshop. 
Go to [Negishi Gateway](https://gateway.negishi.rcac.purdue.edu), login with our purdue accounts (when we have account on Clusters) and connect QGIS as the figure below.

<img width="911" alt="Screenshot 2025-02-25 at 10 05 05 AM" src="https://github.com/user-attachments/assets/f575bf3a-e6bd-468b-92ad-4a3b93405788" />


::::::::::::::::::::::::::::::::::::: callout

We could also open QGIS with Gateway, in the [Typing Code Way](https://rcac-geo.github.io/workshop-qgis/introduction.html#typing-code-way). We could start a terminal as below.

![Start Terminal in Gateway](https://github.com/user-attachments/assets/aac3d529-c726-4793-b3db-e90e55a260fc)


::::::::::::::::::::::::::::::::::::::::::::::::


## View Spatial Data

In Geographic Information Systems (GIS), data is primarily represented in two fundamental formats: vector and raster.

#### Vector Data

* Representation:
   - Vector data uses geometric objects—points, lines, and polygons—to represent spatial features.
   - Points represent individual locations (e.g., a city, a tree).
   - Lines represent linear features (e.g., roads, rivers).
   - Polygons represent areas (e.g., lakes, buildings, administrative boundaries).   
* Characteristics:
  - Precision: Vector data is excellent for representing discrete features with clear boundaries, offering high precision.
  - Scalability: Vector data can be scaled up or down without losing quality.
  - Data Storage: Typically, vector data requires less storage space than raster data for representing discrete features.
  - Use Cases: Best suited for representing features with distinct boundaries, such as roads, property lines, and political boundaries.
* Vector File Types:
  - Shapefile (.shp): A very common geospatial vector data format for GIS software. It actually consists of several files (.shp, .shx, .dbf, etc.)
  - GeoJSON (.geojson): A popular open standard format that uses JavaScript Object Notation (JSON) to represent geographic features.
  - KML/KMZ: Used by Google Earth for displaying geographic data.
  - File format is handled by GDAL/OGR package with a [full list](https://gdal.org/en/stable/drivers/vector/)



#### Raster Data

* Representation:
  - Raster data represents spatial information as a grid of cells (pixels). Each cell contains a value representing a specific attribute (e.g., elevation, temperature, land cover).   
* Characteristics:
  - Continuous Data: Raster data is ideal for representing continuous attributes, such as elevation, temperature, and satellite imagery.
  - Data Storage: Raster data can require significant storage space, especially at high resolutions.
  - Analysis: Raster data is well-suited for spatial analysis involving calculations and modeling.
  - Use Cases: Best suited for representing continuous surfaces, such as elevation models, satellite imagery, and aerial photographs.
* Raster File Types:
  - TIFF: Basic image format, no geographic information.
  - GeoTIFF: A TIFF file with added geospatial metadata, enabling it to be used in GIS applications.
  - COG (Cloud Optimized GeoTIFF): A type of GeoTIFF with a specific data structure optimized for fast access in cloud environments, often using tiled data storage.
  - File format is handled by GDAL/OGR package with a [full list](https://gdal.org/en/stable/drivers/raster/)
 
#### Key Differences 

* Structure: Vector data uses geometric shapes, while raster data uses a grid of cells.
* Data Type: Vector is for discrete features, raster is for continuous phenomena.
* Precision: Vector is generally more precise, while raster's precision depends on cell size.
* Storage: Vector often uses less storage for discrete features. Raster data storage size is heavily dependant on resolution.

#### Load Spatial Data
##### (1) Load vector data from files
* Step1: Layer -> Add Layer -> Add Vector Layer
  
<img width="554" alt="Picture2" src="https://github.com/user-attachments/assets/58bc28a8-7fe8-4dfd-8a54-495dbbfe1e6d" />

* Step2: Input your path of "alaska.shp" and hit "add"
  
![](https://github.com/user-attachments/assets/b68a9319-68f0-4502-9bb5-d3d6b87b33d0)

* Step 3: You will see the shapefile has been added to Layers as below.

![](https://github.com/user-attachments/assets/c5ba1734-88ee-4cc8-a79c-dd2f2b0cb1fb)


::::::::::::::::::::::::::::::::::::: challenge 
## Challenge 1: Try yourself
try yourself to add airports.shp to layers.

:::::::::::::::::::::::: solution 

<img width="613" alt="Picture3" src="https://github.com/user-attachments/assets/f4d958c0-3acb-42a9-855e-4505cbca2c04" />

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: callout

When adding a data source, QGIS attempts to identify its Coordinate Reference System (CRS) from sources like a shapefile's .prj file. If no CRS information is found, QGIS prompts you to specify it. You can modify this behavior in Settings -> Options -> CRS to automatically assign either the project's CRS or a designated default CRS. (Graser et al., 2017)

::::::::::::::::::::::::::::::::::::::::::::::::

##### (2) Load CSV files
* Step 1: Layer -> Add Layer -> Add Delimited Text Layer 
* Step 2: Make changes as the red box in the picture below.

<img width="893" alt="Screenshot 2025-02-25 at 2 41 23 PM" src="https://github.com/user-attachments/assets/4ccee5c6-a3d0-4292-8751-04b044d875b0" />


* Step 3: You will see the shapefile has been added to Layers as below.
  
<img width="612" alt="Picture4" src="https://github.com/user-attachments/assets/db0dd043-5c42-48c2-b929-c48f24f010b6" />

##### (3) Load Raster files
* Step1: Layer -> Add Layer -> Add Raster Layer
* Step2: Input your path of "landcover.img" and hit "add"

![](https://github.com/user-attachments/assets/6566ea7f-8ca9-4def-96b3-ae16671039bf)

* Step 3: You will see the raster has been added to Layers as below.

<img width="428" alt="Picture5" src="https://github.com/user-attachments/assets/a849f162-7ad8-473b-a1e3-d6ad34a82e31" />

::::::::::::::::::::::::::::::::::::: challenge 
## Challenge 1: Try yourself
try yourself to add SR_50M_alaska_nad.tif (Hillshade GeoTiff) to layers.

:::::::::::::::::::::::: solution 

![](https://github.com/user-attachments/assets/e10386e9-d1c0-4736-8b9e-6618cf1a5db4)

:::::::::::::::::::::::::::::::::
## Challenge 2: A Question?

Did you find anything weird about the Hillshade image showing above?

:::::::::::::::::::::::: solution 

Yep, the hillshade should be in the North instead of the South. Let's check data Properties and change looking.

![](https://github.com/user-attachments/assets/ff8ff053-8a82-4335-a06d-e4086adb8986)

![](https://github.com/user-attachments/assets/67208203-a4ac-40c6-838f-8fe9d0a3ae10)

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

## Process Spatial Data
#### Filter Vector Data

Scenario: My Grandma wants to have a trip in Alaska but doctor said she shouldn't go to places with high elevation due to the heart problem. So I will find airports with low elevantion for her. For example, I found the airport with elevation lower than 1000 ft.

Solution: 

* Step1: Right click the data "airports" and select "Filter"

![](https://github.com/user-attachments/assets/b330ca5e-42e5-4d01-b587-4e74762b0375)


* Step2: Select "ELEV" from "Fields", and input the Specific Filter Expression as below:

![](https://github.com/user-attachments/assets/98e26b3a-6329-41eb-b769-3cb38434cce5)

* Step3: Hit "OK" and now only airport with elevation lower than 1000 ft show up.
* Step4-Export data: right click the data and selelct "Export" -> "Save Features As". Input information as figure below and hit "OK".

![](https://github.com/user-attachments/assets/5be55894-3ede-42bd-a888-36efda92b202)
  
#### Raster Calculation

Scenario: I'd like find some sunny slope where my Grandma and I can go skiing. So I found the places where Hillshade is smaller than 100, for example.

Solution:

* Step1: Turn on the Processing Toolbox if it's off, and Search "Raster Calculator".

![](https://github.com/user-attachments/assets/fb3965b0-0754-4f43-b7af-d9f30a4c1ac4)
![](https://github.com/user-attachments/assets/26b8ed3a-0484-4c83-be15-a50e89d9c5b9)


* Step2: Input the "Input Layers", "Expression", "Output CRS", and "Calculated" as the Output file.

![](https://github.com/user-attachments/assets/50d49743-2cb9-466a-806e-a077f31629d0)


* Step3: Hit "Run" and change the looking of output.

![](https://github.com/user-attachments/assets/a6e51da6-479c-4008-ad97-05333452897d)

* You have already written out the output file. But if you didn't, you could always export the data via right clicking it and select "Export" -> "Save As". Then input information as figure below and hit "OK".

![](https://github.com/user-attachments/assets/8074e204-dc55-4533-af9b-0dc1e85fc0d0)

  
::::::::::::::::::::::::::::::::::::: keypoints 

- QGIS is a free and open-source software that runs on various platforms, such as Windows, Mac, and Linux.
- QGIS has a large and active community of users and developers who contribute to its features, plugins, documentation, and support. 
- We can use QGIS via ThinLinc Client or Gateway on HPC Clusters. 
- We learned how to load and visualize vector and raster data.
- We learned how to process data and export them.

::::::::::::::::::::::::::::::::::::::::::::::::

## Extracted resources (local files)

### PDF-Instructions_DEM Access
*Source file:* `Instructions_DA3_DEM_Access_using_Shapefile_v05.pdf`  ·  *type:* file

Downloading USGS Digital Elevation Model (DEM) 
corresponding to a streamflow gauging station 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
Digital Elevation Model (DEM) is a type of raster data that represents the bare surface of 
the earth after removing all natural and built features. DEMs are created from ground 
surveys, digitizing existing hardcopy topographic maps, or remote sensing techniques[1]. 
DEMs are used to delineate watersheds or catchments and other topographic-related 
characteristics such as slope, stream drainage density, and topographic index.  DEMs are 
also needed in hydraulic and hydrodynamic models simulating and mapping flood 
inundation extents[2].  
 
The objective of this tutorial is to learn how to access and download a DEM for a user-
specified area in the form of a shapefile from the United States Geological Survey (USGS) 
Stage Products available at “https://prd-tnm.s3.amazonaws.com/”. 
 
Computer Requirements 
 
The tutorial can be completed through Python-based Jupyter Notebook with a proper 
conda environment with the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “Python [ct-fair]” kernel in the CyberFaCES 
platform. The user does not have to install any modules to complete this tutorial in the 
CyberFaCES platform. However, if a user wants to use this in another platform, the 
following packages are needed: (1) pynhd[3] (for getting shapefile based on a USGS site 
number), (2) urllib[4] (for accessing the DEM data), (3) progressbar (to indicate the speed 
and progress of data download), and (4) rasterio[5] (to plot the unmerged raster tiles).  
  
Overview of steps

1. Input the USGS site number and resolution of DEM required. Use the site number 
to get the shapefile. 
2. Estimate the bounds of the shapefile and determine the file names. 
3. Download the DEM rasters from USGS and plot them along with the shapefile. 
 
Instructions 
 
1. Open a browser and navigate to the following link “https://cyberface.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with instituional credentials or use 
Google Account (you may need to register as new user if you are accessing 
CyberFaCES for the first time). 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”. 
4. Select “Geospatial and Hydrological Science: DEM Accessing using a Shapefile” 
link from the list of modules as shown below.

5. Click on “Start now” and you will be able to see the material for completing this 
module. Select “JN-DEM Access” Jupyter Notebook and it will redirect to the 
Jupyter Lab.  
6. Again, either you can select your institution in dropdown or your Google Account. 
Enter the credentials to log on to the CyberFaCES platform. 
7. Be patient until the Notebook opens, and it has the correct Kernel (ct-fair) as shown 
below. This kernel has all modules preinstalled for completing this tutorial. 
 
 
8. Run the first code cell to import the essential modules in the current kernel. If you 
hit “Shift + L”, the line number will show for all Code block. 
9. Now, we have to input the USGS site number, desired resolution, and create the 
folder to save the DEM raster files. You have to write the code to provide a site id,  
cell resolution, and folder location. Downloading the files may take some time 
depending on the speed of the internet connection. Complete the cell in the Jupyter 
Notebook file as shown in the below figure. 
 
10. After executing the code, do you see a new folder is created in the 
hydroewd/DEM_Access folder as shown below? If not, check your code again and 
execute the code block again.

11. Let us get the shapefile for the watershed with “pynhd” package module using the 
USGS site number. We will plot the watershed shapefile and save it to a local 
directory.  Complete the cell in the Jupyter Notebook file as shown in the below 
figure. You have to write the code to get the watershed boundary and save it with 
a name inside the folder created in the previous cell. Execution of this code will 
add files in the input directory. 
  
12. If you use the default USGS site number, you should get a shapefile similar to the 
one shown below. The shapefile corresponding to the USGS Site – Driftwood River 
near Edinburgh – located in Indiana with a drainage area of 1062 sq. mi is plotted 
below. You can also change the USGS site number according to your study area 
provided it is available in the NLDI database. Additionally, the shapefile will be 
saved to the folder defined earlier.

13. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the state to which the county belongs. Just run the 
cell. You do not have to write any code for this cell. You will get a plot with US 
boundary and Ohio HUC-2 region as shown below. Note that HUC2 region will 
change depending on the location of the watershed. 
 
 
14.  Now, we have to find the four extents of the shapefile and use the maximum and 
minimum integer values of latitude and longitude. The integer values are used to 
create the file names of the DEM raster files available in the USGS-AWS portal. 
Complete the cell in the Jupyter Notebook file as shown in the below figure. Just 
run the cell. You do not have to write any code for this cell.

15. Now, let us create a list of possible pairs of latitude and longitude corresponding 
to DEM raster tiles which intersects with the watershed. This helps us to download 
the required DEM tiles. You have to write the code for the intersection process. 
 
16. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
17. Now, we will create the file names using the extents in the former cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

18. In the previous step, the DEM tiles were downloaded sequentially (one after the 
other). Now, we will explore multithreading to download the files concurrently to 
reduce the time requirements. Run the next two code blocks and let us look at the 
time improvement using multithreading. For the watershed, we can download the 
DEM tiles three times faster (your values may be a little different, it is OK). This is 
useful when we deal with larger watersheds. 
 
19. After executing the code, you will see the files are getting downloaded and the 
status of the download can be seen from the progressbar. Once it is completed, 
check the folder to see whether the tif files are saved in the folder (raw_<site_id>) 
as shown below.

20. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
the process was successful. Complete the cell in the Jupyter Notebook file as 
shown in the below figure. Just run the cell. You don’t have to write any code for 
creating a filename to access the raster file and open the raster file using “rasterio” 
module. The plot of unmerged rasters for “Driftwood River near Edinburgh” is 
shown below.   
 
 
What you have done here is to access the USGS data remotely and download the 
DEM tiles that overlap with the shapefile of the watershed boundary 
corresponding to the input USGS streamflow gauge. The DEM tiles are not 
projected or clipped to the watershed boundary. Processing these tiles is covered 
in a separate DEM processing module. All the data that was downloaded during 
this tutorial are stored in “input_StationID” in your working directory. In this case, 
the name of the working directory is “input_04180000”. If you run the same 
module for another station, a new folder will be created with the same naming 
convention to store the new data.

21. Let us see if you can download DEM for the watershed boundary corresponding 
to a gaging site in Florida (“USGS 02273000 Kissimmee River at S-65E near 
Okeechobee, FL”) and can plot the DEM tiles for this boundary. If you get a plot 
similar to the below figure, you are now an expert in automatically accessing and 
downloading USGS DEM data. The plot of the above mentioned river is shown 
below. 
 
 
 
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

### PDF-Instructions_DEM Access
*Source file:* `Instructions_DA3_DEM_Access_using_Shapefile_v07.pdf`  ·  *type:* file

Downloading USGS Digital Elevation Model (DEM) for 
the contributing area to a streamflow gauging station 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
Digital Elevation Model (DEM) is a type of raster data that represents the bare surface of 
the earth after removing all natural and built features. DEMs are created from ground 
surveys, digitizing existing hardcopy topographic maps, or remote sensing techniques[1]. 
DEMs are used to delineate watersheds or catchments and other topographic-related 
characteristics such as slope, stream drainage density, and topographic index.  DEMs are 
also needed in hydraulic and hydrodynamic models simulating and mapping flood 
inundation extents[2].  
 
The objective of this tutorial is to learn how to access and download a DEM for a user-
specified area in the form of a shapefile from the United States Geological Survey (USGS) 
Stage Products available at “https://prd-tnm.s3.amazonaws.com/”. 
 
Pre-requisites 
 
You must have a login (CI login will also work with either institutional or Google 
Account) for the CyberFaCES platform. If you do not have a login, please visit 
www.cyberfaces.org and click on Register.  
 
Computer Requirements 
 
The tutorial can be completed through Python-based Jupyter Notebook with a proper 
conda environment with the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “ct-fair” kernel in the CyberFaCES 
platform. The user does not have to install any modules to complete this tutorial in the 
CyberFaCES platform. However, if a user wants to use this in another platform, the 
following packages are needed: (1) pynhd[3] (for getting shapefile based on a USGS site

number), (2) urllib[4] (for accessing the DEM data), (3) progressbar (to indicate the speed 
and progress of data download), and (4) rasterio[5] (to plot the unmerged raster tiles).  
  
Overview of steps 
 
1. Input the USGS site number and resolution of DEM required. Use the site number 
to get the shapefile. 
2. Estimate the bounds of the shapefile and determine the file names. 
3. Download the DEM rasters from USGS and plot them along with the shapefile. 
 
Instructions 
 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with institutional credentials or ORCID 
or use Google Account (there are a number of login options in the dropdown and 
if nothing works you may need to register as a new user as you are accessing 
CyberFaCES for the first time). Also, select the “Remember this selection” option 
for future easy access to CyberFaCES. 
 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”.

4. Check Type on the left as “Courses” and select “WaterSciCon24 Hands-On 
Workshop: Web-based Modules on Geospatial Data Processing Using Python” 
course from the list of courses as shown below.  
 
 
 
5. Click on “Start now” and you will be able to see the material for completing this 
workshop. If you have not completed the Pre-Workshop, please complete the first 
item. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here.  First, we will complete the Geospatial & 
Hydrological Science: DEM Accessing using a Shapefile module. Select “JN-DEM 
Access” Jupyter Notebook and it will redirect to the Interactive Jupyter Notebook 
Hub.  
7. Again, either you can select your institutional credentials or ORCID or your 
Google Account in the dropdown. Also, select the “Remember this selection” 
option for future easy access to CyberFaCES. Enter the credentials to log on to the 
CyberFaCES platform.

8. Be patient until the Notebook opens, and it has the correct Kernel (ct-fair) as shown 
below. This kernel has all modules preinstalled for completing this tutorial. 
 
 
Step 0: Import the packages/modules required for this exercise 
9. Run the first code cell to import the essential modules in the current kernel. If you 
hit “Shift + L”, the line number will show for all Code block (it will not show for 
Markdown cell). 
Step 1a: Input USGS Site, DEM resolution, and create a directory 
10. Now, we have to input the USGS site number, desired resolution, and create the 
folder to save the DEM raster files. You have to write the code to provide a site id,  
cell resolution, and folder location. Downloading the files may take some time 
depending on the speed of the internet connection. Complete the cell in the Jupyter 
Notebook file as shown in the below figure. 
 
11. Run the next code block to print the version number 
of the packages available in the “ct-fair” kernel that 
we are going to use in the tutorial. 
12. After executing the code, do you see a new folder is 
created in ~/scratch/DEM_Access folder as shown 
below? If not, check your code again and execute 
the code block again.

Step 1b: Input USGS Site and get the basin 
13. Let us get the shapefile for the watershed with “pynhd” package module using the 
USGS site number. We will plot the watershed shapefile and save it to a local 
directory.  Complete the cell in the Jupyter Notebook file as shown in the below 
figure. You have to write the code to get the watershed boundary and save it with 
a name inside the folder created in the previous cell. Execution of this code will 
add files in the input directory. 
  
14. If you use the default USGS site number, you should get a shapefile similar to the 
one shown below. The shapefile corresponding to the USGS Site – Driftwood River 
near Edinburgh – located in Indiana with a drainage area of 1062 sq. mi is plotted 
below. You can also change the USGS site number according to your study area 
provided it is available in the NLDI database. Additionally, the shapefile will be 
saved to the folder (/scratch/DEM_Access/data_<site_id>) defined earlier.

Step 1c: Creating an Inset Map 
15. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the state to which the county belongs. Just run the 
cell. You do not have to write any code for this cell. You will get a plot with US 
boundary and Ohio HUC-2 region as shown below. Note that HUC2 region will 
change depending on the location of the watershed. You will get a warning, but it 
is ok as we are calculating the centroid to find the HUC2 region. 
 
 
Step 2: Get the extent for downloading DEM 
16. To download the DEM for this watershed, we have to find the four coordinates of 
the bounding box of this shapefile. Run the code in the next code block to these 
four bounds. We are doing this because this is how the DEM raster tiles are saved 
by USGS.  
17. Next, we will use the maximum and minimum integer values of latitude and 
longitude.  The integer values will be used to create the file names of the DEM 
raster files available in the USGS-AWS portal. Just run the cell. You do not have to 
write any code for this cell.

Step 3: Find DEM tiles that overlap with the watershed boundary 
18. Now, let us create a list of possible pairs of latitude and longitude corresponding 
to DEM raster tiles that intersect with the watershed. This helps us to download 
the required DEM tiles. You have to write the code for the intersection process. 
 
19. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
Step 4a: Sequential download - Downloading the DEM from USGS-Amazon Web 
Service 
20. Now, we will create the file names using the extents from the earlier cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

21. After executing the code, you will see the files are getting downloaded and the 
status of the download can be seen from the progressbar. Once it is completed, 
check the folder to see whether the tif files are saved in the folder (raw_<site_id>) 
as shown below. 
 
 
Step 4b: Threading for faster download 
22. In the previous step, the DEM tiles were downloaded sequentially (one after the 
other). Now, we will explore multithreading to download the files concurrently to 
reduce the time requirements. You have to write the code for threading to 
download the files faster.

23. Run the next code block and let us look at the time improvement using 
multithreading. For the watershed, we can download the DEM tiles three times 
faster (your values may be a little different, it is OK). This is useful when we deal 
with larger watersheds. 
 
Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed 
shapefile 
24. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
the process was successful. Complete the cell in the Jupyter Notebook file as 
shown in the below figure. Just run the cell. You don’t have to write any code for 
creating a filename to access the raster file and open the raster file using “rasterio” 
module. The plot of unmerged rasters for “Driftwood River near Edinburgh” is 
shown below.

What you have done here is to access the USGS data remotely and download the 
DEM tiles that overlap with the shapefile of the watershed boundary 
corresponding to the input USGS streamflow gauge. The DEM tiles are not 
projected or clipped to the watershed boundary. Processing these tiles is covered 
in a separate DEM processing module. All the data that was downloaded during 
this tutorial are stored in “input_StationID” in your working directory. In this case, 
the name of the working directory is “input_04180000”. If you run the same 
module for another station, a new folder will be created with the same naming 
convention to store the new data.  
25. Let us see if you can download DEM for the watershed boundary corresponding 
to a gaging site in Florida (“USGS 02273000 Kissimmee River at S-65E near 
Okeechobee, FL”) and can plot the DEM tiles for this boundary. If you get a plot 
similar to the below figure, you are now an expert in automatically accessing and 
downloading USGS DEM data. The plot of the above mentioned river is shown 
below.

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

### PDF-Instructions_DEM Access
*Source file:* `Instructions_DA3_DEM_Access_using_Shapefile_v08.pdf`  ·  *type:* file

Downloading USGS Digital Elevation Model (DEM) for 
the contributing area to a streamflow gauging station 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
Digital Elevation Model (DEM) is a type of raster data that represents the bare surface of 
the earth after removing all natural and built features. DEMs are created from ground 
surveys, digitizing existing hardcopy topographic maps, or remote sensing techniques[1]. 
DEMs are used to delineate watersheds or catchments and other topographic-related 
characteristics such as slope, stream drainage density, and topographic index.  DEMs are 
also needed in hydraulic and hydrodynamic models simulating and mapping flood 
inundation extents[2].  
 
The objective of this tutorial is to learn how to access and download a DEM for a user-
specified area in the form of a shapefile from the United States Geological Survey (USGS) 
Stage Products available at “https://prd-tnm.s3.amazonaws.com/”. 
 
Pre-requisites 
 
You must have a login (CI login will also work with either institutional or Google 
Account) for the CyberFaCES platform. If you do not have a login, please visit 
www.cyberfaces.org and click on Register.  
 
Computer Requirements 
 
The tutorial can be completed through Python-based Jupyter Notebook with a proper 
conda environment with the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “ct-fair” kernel in the CyberFaCES 
platform. The user does not have to install any modules to complete this tutorial in the 
CyberFaCES platform. However, if a user wants to use this in another platform, the 
following packages are needed: (1) pynhd[3] (for getting shapefile based on a USGS site

number), (2) urllib[4] (for accessing the DEM data), (3) progressbar (to indicate the speed 
and progress of data download), and (4) rasterio[5] (to plot the unmerged raster tiles).  
  
Overview of steps 
 
1. Input the USGS site number and resolution of DEM required. Use the site number 
to get the shapefile. 
2. Estimate the bounds of the shapefile and determine the file names. 
3. Download the DEM rasters from USGS and plot them along with the shapefile. 
 
Instructions 
 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with institutional credentials (Purdue, 
UIUC, etc. ) or use Google Account (there are a number of login options in the 
dropdown and if nothing works you may need to register as a new user as you are 
accessing CyberFaCES for the first time – DO NOT USE ORCID). Also, select the 
“Remember this selection” option for future easy access to CyberFaCES. 
 
3. Navigate to “Learn” on the top ribbon and select “Take Course” as shown below.

. 
4. Select “I-GUIDE Forum 2024 Hands-on Tutorial: CyberTraining on Geospatial 
Data Processing using Python” course from the list of courses as shown below.  
 
 
 
5. Click on “Start now” and you will be able to see the material for completing this 
workshop. If you have not completed the Pre-workshop, please complete the first 
item. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here also.  First, we will complete the Geospatial 
& Hydrological Science: DEM Accessing using a Shapefile module. Select “JN-

DEM Access” Jupyter Notebook and it will redirect to the Interactive Jupyter 
Notebook Hub.  
7. Again, either you can select your institutional credentials (Purdue, UIUC, etc. ) or 
your Google Account in the dropdown. Also, select the “Remember this selection” 
option for future easy access to CyberFaCES. Enter the credentials to log on to the 
CyberFaCES platform. 
 
 
8. Be patient until the Notebook opens, and it has the correct Kernel (ct-fair) as shown 
below. This kernel has all modules preinstalled for completing this tutorial. 
 
 
Step 0: Import the packages/modules required for this exercise 
9. Run the first code cell to import the essential modules in the current kernel. If you 
hit “Shift + L”, the line number will show for all Code block (it will not show for 
Markdown cell). 
Step 1a: Input USGS Site, DEM resolution, and create a directory 
10. Now, we have to input the USGS site number, desired resolution, and create the 
folder to save the DEM raster files. You have to write the code to provide a site id,  
cell resolution, and folder location. Downloading the files may take some time 
depending on the speed of the internet connection. Complete the cell in the Jupyter 
Notebook file as shown in the below figure.

11. Run the next code block to print the version number 
of the packages available in the “ct-fair” kernel that 
we are going to use in the tutorial. 
12. After executing the code, do you see a new folder is 
created in ~/scratch/DEM_Access folder as shown 
below? If not, check your code again and execute 
the code block again. 
 
Step 1b: Input USGS Site and get the basin 
13. Let us get the shapefile for the watershed with “pynhd” package module using the 
USGS site number. We will plot the watershed shapefile and save it to a local 
directory.  Complete the cell in the Jupyter Notebook file as shown in the below 
figure. You have to write the code to get the watershed boundary and save it with 
a name inside the folder created in the previous cell. Execution of this code will 
add files in the input directory.

14. If you use the default USGS site number, you should get a shapefile similar to the 
one shown below. The shapefile corresponding to the USGS Site – Driftwood River 
near Edinburgh – located in Indiana with a drainage area of 1062 sq. mi is plotted 
below. You can also change the USGS site number according to your study area 
provided it is available in the NLDI database. Additionally, the shapefile will be 
saved to the folder (/scratch/DEM_Access/data_<site_id>) defined earlier. 
       
 
 
Step 1c: Creating an Inset Map 
15. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the state to which the county belongs. Just run the 
cell. You do not have to write any code for this cell. You will get a plot with US 
boundary and Ohio HUC-2 region as shown below. Note that HUC2 region will

change depending on the location of the watershed. You will get a warning, but it 
is ok as we are calculating the centroid to find the HUC2 region. 
 
 
Step 2: Get the extent for downloading DEM 
16. To download the DEM for this watershed, we have to find the four coordinates of 
the bounding box of this shapefile. Run the code in the next code block to these 
four bounds. We are doing this because this is how the DEM raster tiles are saved 
by USGS.  
17. Next, we will use the maximum and minimum integer values of latitude and 
longitude.  The integer values will be used to create the file names of the DEM 
raster files available in the USGS-AWS portal. Just run the cell. You do not have to 
write any code for this cell. 
 
 
Step 3: Find DEM tiles that overlap with the watershed boundary 
18. Now, let us create a list of possible pairs of latitude and longitude corresponding 
to DEM raster tiles that intersect with the watershed. This helps us to download 
the required DEM tiles. You have to write the code for the intersection process.

19. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
Step 4a: Sequential download - Downloading the DEM from USGS-Amazon Web 
Service 
20. Now, we will create the file names using the extents from the earlier cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

21. After executing the code, you will see the files are getting downloaded and the 
status of the download can be seen from the progressbar. Once it is completed, 
check the folder to see whether the tif files are saved in the folder (raw_<site_id>) 
as shown below. 
 
 
Step 4b: Threading for faster download 
22. In the previous step, the DEM tiles were downloaded sequentially (one after the 
other). Now, we will explore multithreading to download the files concurrently to 
reduce the time requirements. You have to write the code for threading to 
download the files faster.

23. Run the next code block and let us look at the time improvement using 
multithreading. For the watershed, we can download the DEM tiles three times 
faster (your values may be a little different, it is OK). This is useful when we deal 
with larger watersheds. 
 
Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed 
shapefile 
24. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
the process was successful. Complete the cell in the Jupyter Notebook file as 
shown in the below figure. Just run the cell. You don’t have to write any code for 
creating a filename to access the raster file and open the raster file using “rasterio” 
module. The plot of unmerged rasters for “Driftwood River near Edinburgh” is 
shown below.

What you have done here is to access the USGS data remotely and download the 
DEM tiles that overlap with the shapefile of the watershed boundary 
corresponding to the input USGS streamflow gauge. The DEM tiles are not 
projected or clipped to the watershed boundary. Processing these tiles is covered 
in a separate DEM processing module. All the data that was downloaded during 
this tutorial are stored in “input_StationID” in your working directory. In this case, 
the name of the working directory is “input_04180000”. If you run the same 
module for another station, a new folder will be created with the same naming 
convention to store the new data.  
25. Let us see if you can download DEM for the watershed boundary corresponding 
to a gaging site in Wyoming (“USGS 06186500 Yellowstone River at Yellowstone 
Lk Outlet YNP, WY”) and can plot the DEM tiles for this boundary. If you get a 
plot similar to the below figure, you are now an expert in automatically accessing 
and downloading USGS DEM data. The plot of the above mentioned river is 
shown below.

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

### PDF-Instructions_DEM Access
*Source file:* `Instructions_DEM_Access_using_Shapefile_v05.pdf`  ·  *type:* file

Downloading USGS Digital Elevation Model (DEM) 
corresponding to a streamflow gauging station 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
Digital Elevation Model (DEM) is a type of raster data that represents the bare surface of 
the earth after removing all natural and built features. DEMs are created from ground 
surveys, digitizing existing hardcopy topographic maps, or remote sensing techniques[1]. 
DEMs are used to delineate watersheds or catchments and other topographic-related 
characteristics such as slope, stream drainage density, and topographic index.  DEMs are 
also needed in hydraulic and hydrodynamic models simulating and mapping flood 
inundation extents[2].  
 
The objective of this tutorial is to learn how to access and download a DEM for a user-
specified area in the form of a shapefile from the United States Geological Survey (USGS) 
Stage Products available at “https://prd-tnm.s3.amazonaws.com/”. 
 
Computer Requirements 
 
The tutorial can be completed through Python-based Jupyter Notebook with a proper 
conda environment with the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “Python [ct-fair]” kernel in the CyberFaCES 
platform. The user does not have to install any modules to complete this tutorial in the 
CyberFaCES platform. However, if a user wants to use this in another platform, the 
following packages are needed: (1) pynhd[3] (for getting shapefile based on a USGS site 
number), (2) urllib[4] (for accessing the DEM data), (3) progressbar (to indicate the speed 
and progress of data download), and (4) rasterio[5] (to plot the unmerged raster tiles).  
  
Overview of steps

1. Input the USGS site number and resolution of DEM required. Use the site number 
to get the shapefile. 
2. Estimate the bounds of the shapefile and determine the file names. 
3. Download the DEM rasters from USGS and plot them along with the shapefile. 
 
Instructions 
 
1. Open a browser and navigate to the following link “https://cyberface.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with instituional credentials or use 
Google Account (you may need to register as new user if you are accessing 
CyberFaCES for the first time). 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”. 
4. Select “Geospatial and Hydrological Science: DEM Accessing using a Shapefile” 
link from the list of modules as shown below.

5. Click on “Start now” and you will be able to see the material for completing this 
module. Select “JN-DEM Access” Jupyter Notebook and it will redirect to the 
Jupyter Lab.  
6. Again, either you can select your institution in dropdown or your Google Account. 
Enter the credentials to log on to the CyberFaCES platform. 
7. Be patient until the Notebook opens, and it has the correct Kernel (ct-fair) as shown 
below. This kernel has all modules preinstalled for completing this tutorial. 
 
 
8. Run the first code cell to import the essential modules in the current kernel. 
9. Now, we have to input the USGS site number, desired resolution, and create the 
folder to save the DEM raster files. You have to write the code to provide a site id,  
cell resolution, and folder location. Downloading the files may take some time 
depending on the speed of the internet connection. Complete the cell in the Jupyter 
Notebook file as shown in the below figure. 
 
10. After executing the code, do you see the a new folder is created in the 
hydroewd/DEM_Access folder as shown below? If not, check your code again and 
execute the code block again.

11. Let us get the shapefile for the watershed with “pynhd” package module using the 
USGS site number. We will plot the watershed shapefile and save it to a local 
directory.  Complete the cell in the Jupyter Notebook file as shown in the below 
figure. You have to write the code to get the watershed boundary and save it with 
a name inside the folder created in the previous cell. Execution of this code will 
add files in the input directory. 
  
12. If you use the default USGS site number, you should get a shapefile similar to the 
one shown below. The shapefile corresponding to the USGS Site - Cedar Creek 
Near Cedarville – located in Indiana with a drainage area of 270 sq. mi is plotted 
below. You can also change the USGS site number according to your study area 
provided it is available in the NLDI database. Additionally, the shapefile will be 
saved to the folder defined earlier.

13. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the state to which the county belongs. Just run the 
cell. You do not have to write any code for this cell. You will get a plot with US 
boundary and Great Lakes HUC-2 region as shown below. Note that HUC2 region 
will change depending on the location of the watershed. 
 
 
14.  Now, we have to find the four extents of the shapefile and use the maximum and 
minimum integer values of latitude and longitude. The integer values are used to 
create the file names of the DEM raster files available in the USGS-AWS portal. 
Complete the cell in the Jupyter Notebook file as shown in the below figure. Just 
run the cell. You do not have to write any code for this cell.

15. Now, let us find the latitude and longitude of the DEM raster which intersects with 
the watershed. This helps us to download the required DEM tiles. You have to 
write the code for the intersection process. 
 
16. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
17. Now, we will create the file names using the extents in the former cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

18. After executing the code, you will see the files are getting downloaded through 
progressbar. Once it is completed, check the folder to see whether the tif files are 
saved in the folder as shown below. 
 
19. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
the process was successful. Complete the cell in the Jupyter Notebook file as 
shown in the below figure. Just run the cell. You don’t have to write any code for 
creating a filename to access the raster file and open the raster file using “rasterio” 
module. The plot of unmerged rasters for “Cedar Creek near Cedarville” is shown 
below.

What you have done here is to access the USGS data remotely and download the 
DEM tiles that overlap with the shapefile of the watershed boundary 
corresponding to the input USGS streamflow gauge. The DEM tiles are not 
projected or clipped to the watershed boundary. Processing these tiles is covered 
in a separate DEM processing module. All the data that was downloaded during 
this tutorial are stored in “input_StationID” in your working directory. In this case, 
the name of the working directory is “input_04180000”. If you run the same 
module for another station, a new folder will be created with the same naming 
convention to store the new data.  
20. Let us see if you can download DEM for the watershed boundary corresponding 
to another gauging site (“01502632”) and can plot the DEM tiles for this boundary. 
If you get a plot similar to the below figure, you are now an expert in automatically 
accessing and downloading USGS DEM data. The plot of Susquehanna River at 
Bainbridge, New York is shown below.

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

### Solution_DA3_DEM_Access_v4
*Source file:* `Solution_DA3_DEM_Access_v4.ipynb`  ·  *type:* file

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

import geopandas as gpd
from shapely.geometry import Polygon
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
site_id ='03335500'
#"09037500" #WILLIAMS FORK NEAR PARSHALL, CO
#07103700	FOUNTAIN CREEK NEAR COLORADO SPRINGS, CO.
#09064500	HOMESTAKE CREEK NEAR RED CLIFF, CO.
#09241000 ELK RIVER AT CLARK, CO.	CO

## Resolution of required DEM
## USGS-AWS has different options like 1/3 arc second (code = 13), 1/9 arc second (code = 19; currently unavailable)
## WRITE CODE BELOW
resolution='1'  

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


```

## <span style="color:green">Step 3: Find DEM tiles which overlap with watershed bondary</span>

<ul>
<li> Create a rectangular boundary file using the extents </li>
<li> Make sure the rectangular boundary file have the same projection as the watershed </li>
<li> If the rectangular boundary file overlaps with the watershed, add the lon and lat pair to a list </li>

```python
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

## <span style="color:green">Step 4a: Downloading the DEM from USGS-Amazon Web Service</span>

<ul>
<li> Create a for loop anf download the DEM covering the shapefile </li>
<li> Save it in a folder </li>

```python
current_filenum=1

# Iterate over the locations list and print each pair
for location in overlap_lonlat:
    print("Latitude:", location[1] ,"N ;", ", Longitude:", location[0],"W")

    usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
    
    print(f'Beginning file {current_filenum} download with urllib2  out of {len(overlap_lonlat)}...')
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
    
    
    print(f'Completed file {current_filenum} download with urllib2 out of {len(overlap_lonlat)}...')
    print(f'*************************************************************************************\n')
    
    current_filenum+=1
```

## <span style="color:green">Step 4b: Plotting the downloaded (unmerged) DEMs along with watershed shapefile</span>

<ul>
<li> Plot the different DEMs using rasterio package </li>
<li> Also, plot the shapefile of the watershed </li>

```python
fig, ax = plt.subplots(figsize=(8, 8))

for location in overlap_lonlat:
        usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
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

## Fetched resources (external URLs)

### JN - DEM Access (notebook)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/main/DEM_Access/Coursepage_DA3_DEM_Access_v4f.ipynb

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

<p style='text-align: justify;'>USGS DEM with varying resolutions (1 arc-second or 1/3 arc-second or 1/9 arc-second)</p>

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

import geopandas as gpd
from shapely.geometry import Polygon

from datetime import datetime

from os.path import expanduser
```

```python
## Print the version number
import pynhd
print("PyNHD version: ",pynhd.__version__)
del pynhd

print("Rasterio version: ",rasterio.__version__)
print("Geopandas version: ",gpd.__version__)

import shapely
print("Shapely version: ",shapely.__version__)
del shapely
```

## <span style="color:green">Step 1a: Input USGS Site, DEM resolution, and create a directory</span> 
<ul>
<li>Input: <span style="color:red">USGS Site</span></li>
<li>Input: <span style="color:red">Desired resolution</span></li>
<li>Create: <span style="color:red">Folder for storing input raster files from USGS AWS</span></li>

```python
## Input the USGS site number to get the shapefile
## E.g. "04180000" has a drainage area of 270 sq mi and can downloaded within 2-3 minutes
## But "03335500" has a drainage area of 7267 sq mi and needs more time and space
## WRITE CODE BELOW


## Resolution of required DEM
## USGS-AWS has different options like 1/3 arc second (code = 13), 1/9 arc second (code = 19; currently unavailable)
## WRITE CODE BELOW



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
folder_main=f"{expanduser('~')}/scratch/DEM_Access"
check_create_path_func(folder_main)

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

## Transform to Albers Equal Area projection (EPSG:5070)
watershed_albers = watershed.to_crs(epsg=5070)
## Calculate the area in square miles
## 1 square meter = 0.386102 square miles
watershed_albers['area_sq_mi'] = watershed_albers.area / 1e6 * 0.386102  
#print(watershed_albers['area_sq_mi'][0])

## Plot the watershed
## DD indicates latitude/ longitude degrees is in decimal
ax = watershed.plot(facecolor="b", 
                    edgecolor="k", 
                    figsize=(8, 8))
plt.title(f"Watershed Shapefile in {watershed.crs} Projected CRS\n(USGS:{site_id}, "+
          f"Area = {round(watershed_albers['area_sq_mi'].iloc[0],2)} sq. mi.)")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Saving the watershed file as a shapefile at desired location
shapefile_fileloc_filename=f'{folder_input}/shape_{site_id}.shp'
watershed.to_file(filename=shapefile_fileloc_filename,
                  driver= 'ESRI Shapefile',
                  mode='w')
```

## <span style="color:green">Step 1c: Creating an Inset Map</span> 

<ul>
<li>Input: <span style="color:red">Get a input station</span></li>
<li>Output: <span style="color:red">Find out the basin</span></li>
<li>Output: <span style="color:red">Save the basin file as shapefile</span></li>
    

```python
# Load shapefiles
watershed_map=gpd.read_file(f'{folder_input}/shape_{site_id}.shp')
us_map = gpd.read_file("/srv/shared/data_dem_access/cb_2018_us_conus_5m.shp")
huc_map = gpd.read_file("/srv/shared/data_dem_access/HUC2_modified6.shp")
huc_map_proj=huc_map.to_crs(watershed_map.crs)
## Create a geodataframe from the watershed centroid centroids to a DataFrame
watershed_centroid_gdf = gpd.GeoDataFrame(geometry=watershed_map['geometry'].centroid)
## Add other fields/ columns from watershed shapefile by merge
watershed_centroid_gdf = watershed_centroid_gdf.merge(watershed_map.drop(columns='geometry'), 
                                                    left_index=True, 
                                                    right_index=True)
## Join the corresponding HUC2 region with the centroid shapefile
watershed_with_huc = gpd.sjoin(watershed_centroid_gdf, huc_map_proj, 
                               how="left"#, 
                               #predicate='within'
                              )
specific_huc_map = watershed_with_huc[watershed_with_huc['identifier'] == f'USGS-{site_id}']['NAME'].iloc[0]
selected_huc2=huc_map_proj[huc_map_proj['NAME']==specific_huc_map]
## Bounding box
watershed_bbox = watershed_map.total_bounds
print("Watershed Bounding Box: ",watershed_bbox)
## Calculate the factors for adjusting the limits the rectangular box
xmin_factor = 0.98
xmax_factor = 1.02
ymin_factor = 0.98
ymax_factor = 1.02

## Construct a Polygon from the bounding box
watershed_bbox_polygon = Polygon([(watershed_bbox[0]*xmin_factor, watershed_bbox[1]*ymin_factor),
                        (watershed_bbox[2]*xmax_factor, watershed_bbox[1]*ymin_factor),
                        (watershed_bbox[2]*xmax_factor, watershed_bbox[3]*ymax_factor),
                        (watershed_bbox[0]*xmin_factor, watershed_bbox[3]*ymax_factor)])
watershed_bbox_gdf = gpd.GeoDataFrame(geometry=[watershed_bbox_polygon])
watershed_bbox_gdf.crs = watershed_map.crs
## Plot the main map (US map)
fig, ax = plt.subplots(figsize=(10, 10))
us_map.to_crs(watershed_map.crs).plot(ax=ax, color='lightgrey', edgecolor='black')
selected_huc2.plot(ax=ax, color='lightblue', edgecolor='black')
watershed_map.plot(ax=ax, color='blue', edgecolor=None)
watershed_bbox_gdf.plot(ax=ax, color=None, edgecolor='red',alpha=0.5)
ax.set_xlim(xmin=-135)
ax.set_ylim(ymin=15)
ax.set_title('Inset Map for the watershed')

## Plot the inset HUC2 (HUC2 map)
inset_ax = fig.add_axes([0.16, 0.23, 0.2, 0.2])  # [left, bottom, width, height]
selected_huc2.plot(ax=inset_ax, color='lightblue', edgecolor='black')
watershed_map.plot(ax=inset_ax, color='blue', edgecolor=None)
watershed_bbox_gdf.plot(ax=inset_ax, color=None, edgecolor='red',alpha=0.5)
inset_ax.set_title('HUC2 Map and Watershed')
# Remove axes numbers for the inset map
#inset_ax.axis('off')
plt.show()
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
## Calculate largest integer that equals or not greater than left and bottom bounds
extent_left=abs(math.floor(extents_basin[0]))
extent_right=abs(math.floor(extents_basin[2]))
## You may be tempted to calculate the ceil of right extent
## But, number scheme is such that 84W indicates data from -84 to -83 deg W

## Calculate smallest integer that equals or not less than right and upper bounds
extent_bottom=abs(math.ceil(extents_basin[1]))
extent_top=abs(math.ceil(extents_basin[3]))
## Similarly, you may be tempted to calculate the floor of bottom extent
## But, number scheme is again such that 40N includes data from +39 to +40 deg N 
```

## <span style="color:green">Step 3: Find DEM tiles that overlap with the watershed bondary</span>

<ul>
<li> Create a rectangular boundary file using the extents </li>
<li> Make sure the rectangular boundary file have the same projection as the watershed </li>
<li> If the rectangular boundary file overlaps with the watershed, add the lon and lat pair to a list </li>

```python
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
        ## Create a polygon from the corner points
        rectangular_boundary = Polygon([corner_left_bottom,corner_right_bottom,
                                        corner_right_top,corner_left_top])
        ## Create a GeoDataFrame from the polygon
        rectangular_gdf = gpd.GeoDataFrame(geometry=[rectangular_boundary])
        ## Assign the CRS to watershed's CRS
        rectangular_gdf.crs = watershed.crs
        ## WRITE THE CODE BELOW
        ## Use the overlay operation to find the intersection
        
        
        ## Check if any intersection and append the lat and lon
        if not intersection.empty:
            #print("The rectangular polygon overlaps with the shapefile.")
            overlap_lonlat.append((lon,lat))     
print("The required lon and lat pairs are: \n",overlap_lonlat)
## Calulate the number of tiles to be downloaded from USGS
num_tiles_download=(((extent_left+1)-extent_right)*((extent_top+1)-extent_bottom))
print(f"\nNumber of tiles required to cover the entire region: {num_tiles_download}")
print(f"Left: {extent_left}, Right: {extent_right}, Bottom: {extent_bottom}, Top: {extent_top}")
print(f"\nNumber of tiles within watershed boundary: {len(overlap_lonlat)}")
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

## <span style="color:green">Step 4a : Sequential download - Downloading the DEM from USGS-Amazon Web Service</span>

<ul>
<li> Create a for loop anf download the DEM covering the shapefile </li>
<li> Save it in a folder </li>

```python
start_time_seq=datetime.now()

current_filenum=1

# Iterate over the locations list and print each pair
for location in overlap_lonlat:
    print("Latitude:", location[1] ,"N ;", ", Longitude:", location[0],"W")

    usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
    
    print(f'Beginning file download with urllib2 ({current_filenum}/{len(overlap_lonlat)})...')
    url = (f'https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF'
           f'/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif'
          )
            
    ## The r in 'fr' disables backslach escape sequence processing
    local_fileloc_filename=fr'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif'
    
    ## Retrieve the file using the weblink and local path with file name
    print('Data downloaded from : ')
    print(url)
    ## WRITE THE CODE BELOW
    #urllib.request.urlretrieve(url,local_fileloc_filename) #without progressbar for multiple USGS sites
    
     
    print(f"Completed file download ({current_filenum}/{len(overlap_lonlat)} and save to '{local_fileloc_filename}'...")
    print(f'*************************************************************************************\n')
    
    current_filenum+=1

end_time_seq=datetime.now()
```

## <span style="color:green">Step 4b: Threading for faster download - Downloading the DEM from USGS-Amazon Web Service</span>

```python
import threading

def download_dem_file_func(usgs_filename, local_fileloc_filename):
    try:
        #urllib.request.urlretrieve(url, local_fileloc_filename,MyProgressBar())
        print(f'Beginning file download for {usgs_filename}...')
        urllib.request.urlretrieve(f'https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF'
                                   f'/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif',
        local_fileloc_filename)
        print(f"Completed file download and saved to '{local_fileloc_filename}'")
    except Exception as e_value:
        print(f"Error downloading {url}: {e_value}")

start_time_thread=datetime.now()

## Create empty list and append the names
usgs_file_list=[]
local_fileloc_filename_list=[]
for location in overlap_lonlat:
    usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
    usgs_file_list.append(f'n{location[1]:02d}w{location[0]:03d}')
    local_fileloc_filename_list.append(fr'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif')

## Threading for parallel download to reduce time
threads = []
for usgs_file, filename in zip(usgs_file_list, local_fileloc_filename_list):
    #print(url,filename)
    ## WRITE THE CODE BELOW
    
    
    
    
         
## Wait for all threads to finish to avoid unexpected behavior or incorrect output
for thread in threads:
    thread.join()
end_time_thread=datetime.now()
```

## <span style="color:green">Step 4c: Time Comparison</span>

```python
## Time Comparison

print(f'Time taken for sequential downloading: {end_time_seq-start_time_seq}')
print(f'Time taken for parallel downloading: {end_time_thread-start_time_thread}')
print(f'\nEfficiency: {round((end_time_seq-start_time_seq)/(end_time_thread-start_time_thread),1)}')
```

## <span style="color:green">Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed shapefile</span>

<ul>
<li> Plot the single or different DEMs using rasterio package </li>
<li> Also, plot the shapefile of the watershed </li>

```python
## Creating the dictionary for using resolution in title
arc_seconds = {
    "1": "1 arc-second",
    "13": "1/3 arc-second",
    "19": "1/9 arc-second"
}

if (len(overlap_lonlat)>1):
    title=f"Unmerged Raster DEMs\n (for USGS {site_id} and {arc_seconds[resolution]} resolution)"
else:
    title=f"Single Raster DEM\n (for USGS {site_id} and {arc_seconds[resolution]} resolution)"
    
fig, ax = plt.subplots(figsize=(8, 8))

for location in overlap_lonlat:
        usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
        local_raster_filename=fr'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif'
        raster = rasterio.open(local_raster_filename)
        ## WRITE THE CODE BELOW
        
        
        
        
        #print(f'lat: {lat},lon: {lon},file:{local_fileloc_filename}')
## WRITE THE CODE BELOW        





plt.title(title)
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")
```

### JN-DEM Access (notebook)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/main/DEM_Access/Coursepage_DA3_DEM_Access_v4f.ipynb

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

<p style='text-align: justify;'>USGS DEM with varying resolutions (1 arc-second or 1/3 arc-second or 1/9 arc-second)</p>

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

import geopandas as gpd
from shapely.geometry import Polygon

from datetime import datetime

from os.path import expanduser
```

```python
## Print the version number
import pynhd
print("PyNHD version: ",pynhd.__version__)
del pynhd

print("Rasterio version: ",rasterio.__version__)
print("Geopandas version: ",gpd.__version__)

import shapely
print("Shapely version: ",shapely.__version__)
del shapely
```

## <span style="color:green">Step 1a: Input USGS Site, DEM resolution, and create a directory</span> 
<ul>
<li>Input: <span style="color:red">USGS Site</span></li>
<li>Input: <span style="color:red">Desired resolution</span></li>
<li>Create: <span style="color:red">Folder for storing input raster files from USGS AWS</span></li>

```python
## Input the USGS site number to get the shapefile
## E.g. "04180000" has a drainage area of 270 sq mi and can downloaded within 2-3 minutes
## But "03335500" has a drainage area of 7267 sq mi and needs more time and space
## WRITE CODE BELOW


## Resolution of required DEM
## USGS-AWS has different options like 1/3 arc second (code = 13), 1/9 arc second (code = 19; currently unavailable)
## WRITE CODE BELOW



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
folder_main=f"{expanduser('~')}/scratch/DEM_Access"
check_create_path_func(folder_main)

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

## Transform to Albers Equal Area projection (EPSG:5070)
watershed_albers = watershed.to_crs(epsg=5070)
## Calculate the area in square miles
## 1 square meter = 0.386102 square miles
watershed_albers['area_sq_mi'] = watershed_albers.area / 1e6 * 0.386102  
#print(watershed_albers['area_sq_mi'][0])

## Plot the watershed
## DD indicates latitude/ longitude degrees is in decimal
ax = watershed.plot(facecolor="b", 
                    edgecolor="k", 
                    figsize=(8, 8))
plt.title(f"Watershed Shapefile in {watershed.crs} Projected CRS\n(USGS:{site_id}, "+
          f"Area = {round(watershed_albers['area_sq_mi'].iloc[0],2)} sq. mi.)")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Saving the watershed file as a shapefile at desired location
shapefile_fileloc_filename=f'{folder_input}/shape_{site_id}.shp'
watershed.to_file(filename=shapefile_fileloc_filename,
                  driver= 'ESRI Shapefile',
                  mode='w')
```

## <span style="color:green">Step 1c: Creating an Inset Map</span> 

<ul>
<li>Input: <span style="color:red">Get a input station</span></li>
<li>Output: <span style="color:red">Find out the basin</span></li>
<li>Output: <span style="color:red">Save the basin file as shapefile</span></li>
    

```python
# Load shapefiles
watershed_map=gpd.read_file(f'{folder_input}/shape_{site_id}.shp')
us_map = gpd.read_file("/srv/shared/data_dem_access/cb_2018_us_conus_5m.shp")
huc_map = gpd.read_file("/srv/shared/data_dem_access/HUC2_modified6.shp")
huc_map_proj=huc_map.to_crs(watershed_map.crs)
## Create a geodataframe from the watershed centroid centroids to a DataFrame
watershed_centroid_gdf = gpd.GeoDataFrame(geometry=watershed_map['geometry'].centroid)
## Add other fields/ columns from watershed shapefile by merge
watershed_centroid_gdf = watershed_centroid_gdf.merge(watershed_map.drop(columns='geometry'), 
                                                    left_index=True, 
                                                    right_index=True)
## Join the corresponding HUC2 region with the centroid shapefile
watershed_with_huc = gpd.sjoin(watershed_centroid_gdf, huc_map_proj, 
                               how="left"#, 
                               #predicate='within'
                              )
specific_huc_map = watershed_with_huc[watershed_with_huc['identifier'] == f'USGS-{site_id}']['NAME'].iloc[0]
selected_huc2=huc_map_proj[huc_map_proj['NAME']==specific_huc_map]
## Bounding box
watershed_bbox = watershed_map.total_bounds
print("Watershed Bounding Box: ",watershed_bbox)
## Calculate the factors for adjusting the limits the rectangular box
xmin_factor = 0.98
xmax_factor = 1.02
ymin_factor = 0.98
ymax_factor = 1.02

## Construct a Polygon from the bounding box
watershed_bbox_polygon = Polygon([(watershed_bbox[0]*xmin_factor, watershed_bbox[1]*ymin_factor),
                        (watershed_bbox[2]*xmax_factor, watershed_bbox[1]*ymin_factor),
                        (watershed_bbox[2]*xmax_factor, watershed_bbox[3]*ymax_factor),
                        (watershed_bbox[0]*xmin_factor, watershed_bbox[3]*ymax_factor)])
watershed_bbox_gdf = gpd.GeoDataFrame(geometry=[watershed_bbox_polygon])
watershed_bbox_gdf.crs = watershed_map.crs
## Plot the main map (US map)
fig, ax = plt.subplots(figsize=(10, 10))
us_map.to_crs(watershed_map.crs).plot(ax=ax, color='lightgrey', edgecolor='black')
selected_huc2.plot(ax=ax, color='lightblue', edgecolor='black')
watershed_map.plot(ax=ax, color='blue', edgecolor=None)
watershed_bbox_gdf.plot(ax=ax, color=None, edgecolor='red',alpha=0.5)
ax.set_xlim(xmin=-135)
ax.set_ylim(ymin=15)
ax.set_title('Inset Map for the watershed')

## Plot the inset HUC2 (HUC2 map)
inset_ax = fig.add_axes([0.16, 0.23, 0.2, 0.2])  # [left, bottom, width, height]
selected_huc2.plot(ax=inset_ax, color='lightblue', edgecolor='black')
watershed_map.plot(ax=inset_ax, color='blue', edgecolor=None)
watershed_bbox_gdf.plot(ax=inset_ax, color=None, edgecolor='red',alpha=0.5)
inset_ax.set_title('HUC2 Map and Watershed')
# Remove axes numbers for the inset map
#inset_ax.axis('off')
plt.show()
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
## Calculate largest integer that equals or not greater than left and bottom bounds
extent_left=abs(math.floor(extents_basin[0]))
extent_right=abs(math.floor(extents_basin[2]))
## You may be tempted to calculate the ceil of right extent
## But, number scheme is such that 84W indicates data from -84 to -83 deg W

## Calculate smallest integer that equals or not less than right and upper bounds
extent_bottom=abs(math.ceil(extents_basin[1]))
extent_top=abs(math.ceil(extents_basin[3]))
## Similarly, you may be tempted to calculate the floor of bottom extent
## But, number scheme is again such that 40N includes data from +39 to +40 deg N 
```

## <span style="color:green">Step 3: Find DEM tiles that overlap with the watershed bondary</span>

<ul>
<li> Create a rectangular boundary file using the extents </li>
<li> Make sure the rectangular boundary file have the same projection as the watershed </li>
<li> If the rectangular boundary file overlaps with the watershed, add the lon and lat pair to a list </li>

```python
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
        ## Create a polygon from the corner points
        rectangular_boundary = Polygon([corner_left_bottom,corner_right_bottom,
                                        corner_right_top,corner_left_top])
        ## Create a GeoDataFrame from the polygon
        rectangular_gdf = gpd.GeoDataFrame(geometry=[rectangular_boundary])
        ## Assign the CRS to watershed's CRS
        rectangular_gdf.crs = watershed.crs
        ## WRITE THE CODE BELOW
        ## Use the overlay operation to find the intersection
        
        
        ## Check if any intersection and append the lat and lon
        if not intersection.empty:
            #print("The rectangular polygon overlaps with the shapefile.")
            overlap_lonlat.append((lon,lat))     
print("The required lon and lat pairs are: \n",overlap_lonlat)
## Calulate the number of tiles to be downloaded from USGS
num_tiles_download=(((extent_left+1)-extent_right)*((extent_top+1)-extent_bottom))
print(f"\nNumber of tiles required to cover the entire region: {num_tiles_download}")
print(f"Left: {extent_left}, Right: {extent_right}, Bottom: {extent_bottom}, Top: {extent_top}")
print(f"\nNumber of tiles within watershed boundary: {len(overlap_lonlat)}")
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

## <span style="color:green">Step 4a : Sequential download - Downloading the DEM from USGS-Amazon Web Service</span>

<ul>
<li> Create a for loop anf download the DEM covering the shapefile </li>
<li> Save it in a folder </li>

```python
start_time_seq=datetime.now()

current_filenum=1

# Iterate over the locations list and print each pair
for location in overlap_lonlat:
    print("Latitude:", location[1] ,"N ;", ", Longitude:", location[0],"W")

    usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
    
    print(f'Beginning file download with urllib2 ({current_filenum}/{len(overlap_lonlat)})...')
    url = (f'https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF'
           f'/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif'
          )
            
    ## The r in 'fr' disables backslach escape sequence processing
    local_fileloc_filename=fr'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif'
    
    ## Retrieve the file using the weblink and local path with file name
    print('Data downloaded from : ')
    print(url)
    ## WRITE THE CODE BELOW
    #urllib.request.urlretrieve(url,local_fileloc_filename) #without progressbar for multiple USGS sites
    
     
    print(f"Completed file download ({current_filenum}/{len(overlap_lonlat)} and save to '{local_fileloc_filename}'...")
    print(f'*************************************************************************************\n')
    
    current_filenum+=1

end_time_seq=datetime.now()
```

## <span style="color:green">Step 4b: Threading for faster download - Downloading the DEM from USGS-Amazon Web Service</span>

```python
import threading

def download_dem_file_func(usgs_filename, local_fileloc_filename):
    try:
        #urllib.request.urlretrieve(url, local_fileloc_filename,MyProgressBar())
        print(f'Beginning file download for {usgs_filename}...')
        urllib.request.urlretrieve(f'https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF'
                                   f'/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif',
        local_fileloc_filename)
        print(f"Completed file download and saved to '{local_fileloc_filename}'")
    except Exception as e_value:
        print(f"Error downloading {url}: {e_value}")

start_time_thread=datetime.now()

## Create empty list and append the names
usgs_file_list=[]
local_fileloc_filename_list=[]
for location in overlap_lonlat:
    usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
    usgs_file_list.append(f'n{location[1]:02d}w{location[0]:03d}')
    local_fileloc_filename_list.append(fr'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif')

## Threading for parallel download to reduce time
threads = []
for usgs_file, filename in zip(usgs_file_list, local_fileloc_filename_list):
    #print(url,filename)
    ## WRITE THE CODE BELOW
    
    
    
    
         
## Wait for all threads to finish to avoid unexpected behavior or incorrect output
for thread in threads:
    thread.join()
end_time_thread=datetime.now()
```

## <span style="color:green">Step 4c: Time Comparison</span>

```python
## Time Comparison

print(f'Time taken for sequential downloading: {end_time_seq-start_time_seq}')
print(f'Time taken for parallel downloading: {end_time_thread-start_time_thread}')
print(f'\nEfficiency: {round((end_time_seq-start_time_seq)/(end_time_thread-start_time_thread),1)}')
```

## <span style="color:green">Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed shapefile</span>

<ul>
<li> Plot the single or different DEMs using rasterio package </li>
<li> Also, plot the shapefile of the watershed </li>

```python
## Creating the dictionary for using resolution in title
arc_seconds = {
    "1": "1 arc-second",
    "13": "1/3 arc-second",
    "19": "1/9 arc-second"
}

if (len(overlap_lonlat)>1):
    title=f"Unmerged Raster DEMs\n (for USGS {site_id} and {arc_seconds[resolution]} resolution)"
else:
    title=f"Single Raster DEM\n (for USGS {site_id} and {arc_seconds[resolution]} resolution)"
    
fig, ax = plt.subplots(figsize=(8, 8))

for location in overlap_lonlat:
        usgs_filename=f'n{location[1]:02d}w{location[0]:03d}'
        local_raster_filename=fr'{dem_files_store}/USGS_{resolution}_{usgs_filename}.tif'
        raster = rasterio.open(local_raster_filename)
        ## WRITE THE CODE BELOW
        
        
        
        
        #print(f'lat: {lat},lon: {lon},file:{local_fileloc_filename}')
## WRITE THE CODE BELOW        





plt.title(title)
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")
```
