---
title: "Geospatial & Hydrological Science: DEM Access and Visualization from USGS AWS [v09]"
unit_id: 277
course_id: 0
level: "Foundation"
slug: dem-access-and-visualization-from-usgs-aws
is_course: 0
---

# Geospatial & Hydrological Science: DEM Access and Visualization from USGS AWS [v09]

## Extracted resources (local files)

### PDF-Instructions
*Source file:* `Instructions_DA3_DEM_Access_using_Shapefile_v09.pdf`  ·  *type:* file

DEM Access and Visualization from USGS AWS 
 
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
4. Select “Mini-Workshop: CyberTraining on Geospatial Data Processing using 
Python for Hydrology” course from the list of courses as shown below.  
 
 
 
5. Click on “Start now” and you will be able to see the material for completing this 
workshop. If you have not completed the Pre-workshop, please complete the 
first item. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here also.  First, we will complete the Geospatial 
& Hydrological Science: DEM Access and Visualization from USGS AWS. Select

“JN-DEM Access” Jupyter Notebook and it will redirect to the Interactive Jupyter 
Notebook Hub. 
7. Again, either you can select your institutional credentials (Purdue, UIUC, etc. ) or 
your Google Account in the dropdown. Also, select the “Remember this selection” 
option for future easy access to CyberFaCES. Enter the credentials to log on to the 
CyberFaCES platform. 
 
 
8. Be patient until the Notebook opens, and make sure it has the correct Kernel (ct-
fair) as shown below. This kernel has all modules preinstalled for completing this 
tutorial. 
 
 
Step 0: Import the packages/modules required for this exercise 
9. Run the first code cell to import the essential modules in the current kernel. If you 
hit “Shift + L”, the line number will show for all Code block (it will not show for 
Markdown cell). 
10. Run the next code block to print the version number of the packages available in 
the “ct-fair” kernel that we are going to use in the tutorial. 
11. Run the next code to see the map of all USGS sites (including Alaska, Hawaii, and 
Puerto Rico). The Hydro Network-Linked Data Index (NLDI; https://waterdata.usgs
.gov/blog/nldi-intro/) has some missing watersheds in NLDI database. So you may 
get the watershed of all sites shown on the map. 
12. We will select a watershed with a drainage area less than 1000 sq mi as we are no
t running this tutorial in HPC. Later we will select a watershed with higher drain
age area in the HPC tutorial. We will go ahead with USGS 03335000 WILDCAT C
REEK NEAR LAFAYETTE, IN (located closer to Purdue University in Indiana) as 
shown on the map below. This map is created using folium python package.

Step 1a: Input USGS Site, DEM resolution, and create a directory 
13. Now, we have to input the USGS site number, desired resolution, and create the 
folder to save the DEM raster files. You have to write the code to provide a site id, 
and cell resolution. The code will get the shapefile for the watershed with “pynhd” 
package module using the USGS site number. Downloading the files may take 
some time depending on the speed of the internet connection. Complete the cell in 
the Jupyter Notebook file as shown in the below figure. 
 
14. Next, we will display the watershed on a folium map to see the watershed and the 
corresponding USGS site on the map.

15. Now, run the code to create the required folder 
directory. After executing the code, do you see a new 
folder is created in ~/scratch/DEM_Access folder as 
shown below? If not, check your code again and 
execute the code block again.  
 
Step 1b: Input USGS Site and get the basin 
16. We will plot the watershed shapefile and save it to a local directory.  Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You do not have to 
write the code to get the watershed boundary and save it with a name inside the 
folder created in the previous cell. Execution of this code will add files in the input 
directory. 
  
17. If you use the default USGS site number, you should get a shapefile similar to the 
one shown below. The shapefile corresponding to the USGS Site – Driftwood River 
near Edinburgh – located in Indiana with a drainage area of 1062 sq. mi is plotted 
below. You can also change the USGS site number according to your study area 
provided it is available in the NLDI database. Additionally, the shapefile will be 
saved to the folder (/scratch/DEM_Access/data_<site_id>) defined earlier.

Step 1c: Creating an Inset Map 
18. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the state to which the county belongs. Just run the 
cell. You do not have to write any code for this cell. You will get a plot with US 
boundary and Ohio HUC-2 region as shown below. Note that HUC2 region will 
change depending on the location of the watershed. You will get a warning, but it 
is ok as we are calculating the centroid to find the HUC2 region. 
 
 
Step 2: Get the extent for downloading DEM 
19. To download the DEM for this watershed, we have to find the four coordinates of 
the bounding box of this shapefile. Run the code in the next code block to these 
four bounds. We are doing this because this is how the DEM raster tiles are saved 
by USGS.  
20. Next, we will use the maximum and minimum integer values of latitude and 
longitude.  The integer values will be used to create the file names of the DEM 
raster files available in the USGS-AWS portal. Just run the cell. You do not have to 
write any code for this cell.

Step 3: Find DEM tiles that overlap with the watershed boundary 
21. Now, let us create a list of possible pairs of latitude and longitude corresponding 
to DEM raster tiles that intersect with the watershed. This helps us to download 
the required DEM tiles. You have to write the code for the intersection process. 
 
22. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
Step 4a: Sequential download - Downloading the DEM from USGS-Amazon Web 
Service 
23. Now, we will create the file names using the extents from the earlier cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

24. After executing the code, you will see the files are getting downloaded and the 
status of the download can be seen from the progressbar. Once it is completed, 
check the folder to see whether the tif files are saved in the folder (raw_<site_id>) 
as shown below. 
 
 
Step 4b: Threading for faster download 
25. In the previous step, the DEM tiles were downloaded sequentially (one after the 
other). Now, we will explore multithreading to download the files concurrently to 
reduce the time requirements. You have to write the code for threading to 
download the files faster.

26. Run the next code block and let us look at the time improvement using 
multithreading. For the watershed, we can download the DEM tiles three times 
faster (your values may be a little different, it is OK). This is useful when we deal 
with larger watersheds. 
 
Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed 
shapefile 
27. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
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
28. Let us see if you can download DEM for the watershed boundary corresponding 
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

### PDF_Instructions
*Source file:* `Instructions_DA3_DEM_Access_using_Shapefile_v09.pdf`  ·  *type:* file

DEM Access and Visualization from USGS AWS 
 
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
4. Select “Mini-Workshop: CyberTraining on Geospatial Data Processing using 
Python for Hydrology” course from the list of courses as shown below.  
 
 
 
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

### PDF-Instructions
*Source file:* `Instructions_DA3_DEM_Access_v09.pdf`  ·  *type:* file

DEM Access and Visualization from USGS AWS 
 
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
4. Select “Mini-Workshop: CyberTraining on Geospatial Data Processing using 
Python for Hydrology” course from the list of courses as shown below.  
 
 
 
5. Click on “Start now” and you will be able to see the material for completing this 
workshop. If you have not completed the Pre-workshop Survey, please complete 
the first item. Also, remember to complete the Assessment and Post-workshop 
Survey once you have completed all modules in this workshop. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here also.  First, we will complete the Geospatial & 
Hydrological Science: DEM Access and Visualization from USGS AWS. Select “JN-

DEM Access” Jupyter Notebook and it will redirect to the Interactive Jupyter 
Notebook Hub. 
7. Again, either you can select your institutional credentials (Purdue, UIUC, etc. ) or 
your Google Account in the dropdown. Also, select the “Remember this selection” 
option for future easy access to CyberFaCES. Enter the credentials to log on to the 
CyberFaCES platform. 
 
 
8. Be patient until the Notebook opens, and make sure it has the correct Kernel (ct-
fair) as shown below. This kernel has all python packages preinstalled for 
completing this tutorial. 
 
 
Step 0: Import the packages/modules required for this exercise 
9. Run the first code cell to import the essential modules in the current kernel. If you 
hit “Shift + L” (you can enable it by View > Show Line Numbers), the line number w
ill show for all Code block (it will not show for Markdown cell). 
10. Run the next code block to print the version number of the packages available in 
the “ct-fair” kernel that we are going to use in the tutorial. Knowing exact package 
versions helps reproduce result in different platforms/ machine. 
11. Run the next code to see the map of all USGS sites (including Alaska, Hawaii, and 
Puerto Rico). The Hydro Network-Linked Data Index (NLDI; https://waterdata.usgs
.gov/blog/nldi-intro/) has some missing watersheds in NLDI database. So you may
not get the watershed/ shapefile of all sites shown on the map. 
12. Now, we will select a watershed with a drainage area of less than 1000 sq mi as w
e have limited resources in this currently. Later, we will select a watershed with h
igher drainage area in the HPC tutorial. Let’s go ahead with USGS 03335000 WIL

DCAT CREEK NEAR LAFAYETTE, IN (located closer to Purdue University in In
diana) as shown on the map below.  
 
Step 1a: Input USGS Site, DEM resolution, and create a directory 
13. Now, we have to input the USGS site number, desired spatial resolution, and 
create the folder to save the DEM raster files. You have to write the code to provide 
a site id, and cell resolution. The code will get the shapefile for the watershed with 
“pynhd” package module using the USGS site number from the NLDI database. 
Complete the cell in the Jupyter Notebook file as shown in the below figure. 
 
14. Next, we will display the watershed on a folium map to see the watershed and the 
corresponding USGS site on the map.

15. Now, run the next code to create the required folder 
directory. After executing the code, do you see a new 
folder is created in ~/scratch/DEM_Access folder as 
shown? If not, check your code again and execute the 
code block again.  
 
Step 1b: Plot the basin and save the shapefile locally 
16. We will plot the watershed shapefile and save it to a local directory.  Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code to save the watershed boundary as a shapefile with a name inside the 
folder created in the previous cell. Execution of this code will add files in the input 
directory.

17. If you use the USGS site number as mentioned earlier, you should get a shapefile 
similar to the one shown below. The shapefile corresponding to the USGS Site – 
Driftwood River near Edinburgh – located in Indiana with a drainage area of 1062 
sq. mi is plotted below. You can also change the USGS site number according to 
your study area provided it is available in the NLDI database. Additionally, the 
shapefile will be saved to the folder (/scratch/DEM_Access/data_<site_id>) 
defined earlier. 
 
 
 
Step 1c: Creating an Inset Map 
18. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the HUC02 region to which the waetrshed belongs. 
Just run the cell. You do not have to write any code for this cell. You will get a plot 
with US boundary and Ohio HUC-2 region as shown below. Note that HUC2 
region will change depending on the location of the watershed. You will get a 
warning, but it is ok as we are calculating the centroid to find the HUC2 region. 
 
 
Step 2: Get the extent for downloading DEM 
19. To download the DEM for this watershed, we have to find the four coordinates of 
the bounding box of this shapefile. Run the code in the next code block to these 
four bounds. We are doing this because this is how the DEM raster tiles are saved 
by USGS.

20. Next, we will use the maximum and minimum integer values of latitude and 
longitude.  The integer values will be used to create the file names of the DEM 
raster files available in the USGS-AWS portal. Just run the cell. You do not have to 
write any code for this cell. 
 
 
Step 3: Find DEM tiles that overlap with the watershed boundary 
21. Now, let us create a list of possible pairs of latitude and longitude corresponding 
to DEM raster tiles that intersect with the watershed. This helps us to download 
the required DEM tiles. You have to write the code for the intersection process. 
 
22. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
Step 4a: Sequential download - Downloading the DEM from USGS-Amazon Web 
Service 
23. Now, we will create the file names using the extents from the earlier cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

24. After executing the code, you will see the files are getting downloaded and the 
status of the download can be seen from the progressbar. Once it is completed, 
check the folder to see whether the tif files are saved in the folder (raw_<site_id>) 
as shown below. 
 
 
Step 4b: Threading for faster download 
25. In the previous step, the DEM tiles were downloaded sequentially (one after the 
other). Now, we will explore multithreading to download the files concurrently to 
reduce the time requirements. You have to write the code for threading to 
download the files faster.

26. Run the next code block and let us look at the time improvement using 
multithreading. For the watershed, we can download the DEM tiles three times 
faster (your values may be a little different, it is OK). This is useful when we deal 
with larger watersheds. 
 
Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed 
shapefile 
27. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
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
28. Let us see if you can download DEM for the watershed boundary corresponding 
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

### AI_Co_Scientist_Report
*Source file:* `Instructions_DA3_DEM_Access_v09b.pdf`  ·  *type:* file

DEM Access and Visualization from USGS AWS 
 
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
4. Select “I-GUIDE Forum 2025 Hands-on Tutorial: CyberTraining on Geospatial 
Data Processing using Python for Hydrology” course from the list of courses as 
shown below.  
5. Click on “Start now” and you will be able to see the material for completing this 
workshop. If you have not completed the Pre-workshop Survey, please complete 
the first item. Also, remember to complete the Assessment and Post-workshop 
Survey once you have completed all modules in this workshop. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here also.  First, we will complete the Geospatial & 
Hydrological Science: DEM Access and Visualization from USGS AWS. Select “JN-
DEM Access” Jupyter Notebook and it will redirect to the Interactive Jupyter 
Notebook Hub. 
7. Be patient until the Notebook opens, and make sure it has the correct Kernel (ct-
fair) as shown below. This kernel has all python packages preinstalled for 
completing this tutorial. 
 
 
Step 0: Import the packages/modules required for this exercise

8. Run the first code cell to import the essential modules in the current kernel. If you 
hit “Shift + L” (you can enable it by View > Show Line Numbers), the line number w
ill show for all Code block (it will not show for Markdown cell). 
9. Run the next code block to print the version number of the packages available in 
the “ct-fair” kernel that we are going to use in the tutorial. Knowing exact package 
versions helps reproduce result in different platforms/ machine. 
10. Run the next code to see the map of all USGS sites (including Alaska, Hawaii, and 
Puerto Rico). The Hydro Network-Linked Data Index (NLDI; https://waterdata.usgs
.gov/blog/nldi-intro/) has some missing watersheds in NLDI database. So you may
not get the watershed/ shapefile of all sites shown on the map. 
11. Now, we will select a watershed with a drainage area of less than 1000 sq mi as w
e have limited resources in this currently. Later, we will select a watershed with h
igher drainage area in the HPC tutorial. Let’s go ahead with USGS 03335000 WIL
DCAT CREEK NEAR LAFAYETTE, IN (located closer to Purdue University in In
diana) as shown on the map below.  
 
Step 1a: Input USGS Site, DEM resolution, and create a directory 
12. Now, we have to input the USGS site number, desired spatial resolution, and 
create the folder to save the DEM raster files. You have to write the code to provide 
a site id, and cell resolution. The code will get the shapefile for the watershed with 
“pynhd” package module using the USGS site number from the NLDI database. 
Complete the cell in the Jupyter Notebook file as shown in the below figure.

13. Next, we will display the watershed on a folium map to see the watershed and the 
corresponding USGS site on the map. 
 
14. Now, run the next code to create the required folder 
directory. After executing the code, do you see a new 
folder is created in ~/scratch/DEM_Access folder as 
shown? If not, check your code again and execute the 
code block again.  
 
Step 1b: Plot the basin and save the shapefile locally 
15. We will plot the watershed shapefile and save it to a local directory.  Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code to save the watershed boundary as a shapefile with a name inside the 
folder created in the previous cell. Execution of this code will add files in the input 
directory.

16. If you use the USGS site number as mentioned earlier, you should get a shapefile 
similar to the one shown below. The shapefile corresponding to the USGS Site – 
Driftwood River near Edinburgh – located in Indiana with a drainage area of 1062 
sq. mi is plotted below. You can also change the USGS site number according to 
your study area provided it is available in the NLDI database. Additionally, the 
shapefile will be saved to the folder (/scratch/DEM_Access/data_<site_id>) 
defined earlier. 
 
 
 
Step 1c: Creating an Inset Map 
17. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the HUC02 region to which the waetrshed belongs. 
Just run the cell. You do not have to write any code for this cell. You will get a plot 
with US boundary and Ohio HUC-2 region as shown below. Note that HUC2 
region will change depending on the location of the watershed. You will get a 
warning, but it is ok as we are calculating the centroid to find the HUC2 region.

Step 2: Get the extent for downloading DEM 
18. To download the DEM for this watershed, we have to find the four coordinates of 
the bounding box of this shapefile. Run the code in the next code block to these 
four bounds. We are doing this because this is how the DEM raster tiles are saved 
by USGS.  
19. Next, we will use the maximum and minimum integer values of latitude and 
longitude.  The integer values will be used to create the file names of the DEM 
raster files available in the USGS-AWS portal. Just run the cell. You do not have to 
write any code for this cell. 
 
 
Step 3: Find DEM tiles that overlap with the watershed boundary 
20. Now, let us create a list of possible pairs of latitude and longitude corresponding 
to DEM raster tiles that intersect with the watershed. This helps us to download 
the required DEM tiles. You have to write the code for the intersection process.

21. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
Step 4a: Sequential download - Downloading the DEM from USGS-Amazon Web 
Service 
22. Now, we will create the file names using the extents from the earlier cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

23. After executing the code, you will see the files are getting downloaded and the 
status of the download can be seen from the progressbar. Once it is completed, 
check the folder to see whether the tif files are saved in the folder (raw_<site_id>) 
as shown below. 
 
 
Step 4b: Threading for faster download 
24. In the previous step, the DEM tiles were downloaded sequentially (one after the 
other). Now, we will explore multithreading to download the files concurrently to 
reduce the time requirements. You have to write the code for threading to 
download the files faster.

25. Run the next code block and let us look at the time improvement using 
multithreading. For the watershed, we can download the DEM tiles three times 
faster (your values may be a little different, it is OK). This is useful when we deal 
with larger watersheds. 
 
Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed 
shapefile 
26. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
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
27. Let us see if you can download DEM for the watershed boundary corresponding 
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

### AI_Co_Scientist_Report
*Source file:* `Instructions_DA3_DEM_Access_v10.pdf`  ·  *type:* file

DEM Access and Visualization from USGS AWS 
 
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
4. Select “I-GUIDE Forum 2025 Hands-on Tutorial: CyberTraining on Geospatial 
Data Processing using Python for Hydrology” course from the list of courses as 
shown below.  
5. Click on “Start now” and you will be able to see the material for completing this 
workshop. If you have not completed the Pre-workshop Survey, please complete 
the first item. Also, remember to complete the Assessment and Post-workshop 
Survey once you have completed all modules in this workshop. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here also.  First, we will complete the Geospatial & 
Hydrological Science: DEM Access and Visualization from USGS AWS. Select “JN-
DEM Access” Jupyter Notebook and it will redirect to the Interactive Jupyter 
Notebook Hub. 
7. Be patient until the Notebook opens, and make sure it has the correct Kernel (ct-
fair) as shown below. This kernel has all python packages preinstalled for 
completing this tutorial. 
 
 
Step 0: Import the packages/modules required for this exercise

8. Run the first code cell to import the essential modules in the current kernel. If you 
hit “Shift + L” (you can enable it by View > Show Line Numbers), the line number w
ill show for all Code block (it will not show for Markdown cell). 
9. Run the next code block to print the version number of the packages available in 
the “ct-fair” kernel that we are going to use in the tutorial. Knowing exact package 
versions helps reproduce result in different platforms/ machine. 
10. Run the next code to see the map of all USGS sites (including Alaska, Hawaii, and 
Puerto Rico). The Hydro Network-Linked Data Index (NLDI; https://waterdata.usgs
.gov/blog/nldi-intro/) has some missing watersheds in NLDI database. So you may
not get the watershed/ shapefile of all sites shown on the map. 
11. Now, we will select a watershed with a drainage area of less than 1000 sq mi as w
e have limited resources in this currently. Later, we will select a watershed with h
igher drainage area in the HPC tutorial. Let’s go ahead with USGS 03335000 WIL
DCAT CREEK NEAR LAFAYETTE, IN (located closer to Purdue University in In
diana) as shown on the map below.  
 
Step 1a: Input USGS Site, DEM resolution, and create a directory 
12. Now, we have to input the USGS site number, desired spatial resolution, and 
create the folder to save the DEM raster files. You have to write the code to provide 
a site id, and cell resolution. The code will get the shapefile for the watershed with 
“pynhd” package module using the USGS site number from the NLDI database. 
Complete the cell in the Jupyter Notebook file as shown in the below figure.

13. Next, we will display the watershed on a folium map to see the watershed and the 
corresponding USGS site on the map. 
 
14. Now, run the next code to create the required folder 
directory. After executing the code, do you see a new 
folder is created in ~/scratch/DEM_Access folder as 
shown? If not, check your code again and execute the 
code block again.  
 
Step 1b: Plot the basin and save the shapefile locally 
15. We will plot the watershed shapefile and save it to a local directory.  Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code to save the watershed boundary as a shapefile with a name inside the 
folder created in the previous cell. Execution of this code will add files in the input 
directory.

16. If you use the USGS site number as mentioned earlier, you should get a shapefile 
similar to the one shown below. The shapefile corresponding to the USGS Site – 
Driftwood River near Edinburgh – located in Indiana with a drainage area of 1062 
sq. mi is plotted below. You can also change the USGS site number according to 
your study area provided it is available in the NLDI database. Additionally, the 
shapefile will be saved to the folder (/scratch/DEM_Access/data_<site_id>) 
defined earlier. 
 
 
 
Step 1c: Creating an Inset Map 
17. Additionally, let's generate an inset map utilizing the shapefiles for the 
Contiguous United States and the HUC02 region to which the waetrshed belongs. 
Just run the cell. You do not have to write any code for this cell. You will get a plot 
with US boundary and Ohio HUC-2 region as shown below. Note that HUC2 
region will change depending on the location of the watershed. You will get a 
warning, but it is ok as we are calculating the centroid to find the HUC2 region.

Step 2: Get the extent for downloading DEM 
18. To download the DEM for this watershed, we have to find the four coordinates of 
the bounding box of this shapefile. Run the code in the next code block to these 
four bounds. We are doing this because this is how the DEM raster tiles are saved 
by USGS.  
19. Next, we will use the maximum and minimum integer values of latitude and 
longitude.  The integer values will be used to create the file names of the DEM 
raster files available in the USGS-AWS portal. Just run the cell. You do not have to 
write any code for this cell. 
 
 
Step 3: Find DEM tiles that overlap with the watershed boundary 
20. Now, let us create a list of possible pairs of latitude and longitude corresponding 
to DEM raster tiles that intersect with the watershed. This helps us to download 
the required DEM tiles. You have to write the code for the intersection process.

21. The next cell defines a function for tracking the progress of downloading the raster 
files as these files have large sizes. Showing the progress of downloading will be 
helpful when you have a slow-speed internet connection. Just run the cell. You do 
not have to write any code for this cell. 
Step 4a: Sequential download - Downloading the DEM from USGS-Amazon Web 
Service 
22. Now, we will create the file names using the extents from the earlier cell and then 
use the “urllib” module to retrieve the files from USGS-AWS portal. Complete the 
cell in the Jupyter Notebook file as shown in the below figure. You have to write 
the code for retrieving the files. It might take some time to complete the execution 
of the cell as the downloading of the raster files may take some time depending on 
the speed of the internet connection. Execution of this cell will add the raster files 
to the defined input directory.

23. After executing the code, you will see the files are getting downloaded and the 
status of the download can be seen from the progressbar. Once it is completed, 
check the folder to see whether the tif files are saved in the folder (raw_<site_id>) 
as shown below. 
 
 
Step 4b: Threading for faster download 
24. In the previous step, the DEM tiles were downloaded sequentially (one after the 
other). Now, we will explore multithreading to download the files concurrently to 
reduce the time requirements. You have to write the code for threading to 
download the files faster.

25. Run the next code block and let us look at the time improvement using 
multithreading. For the watershed, we can download the DEM tiles three times 
faster (your values may be a little different, it is OK). This is useful when we deal 
with larger watersheds. 
 
Step 4d: Plotting the downloaded (single/unmerged) DEMs along with watershed 
shapefile 
26. Lastly, let us plot all the downloaded raster files along with the shapefile to see if 
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
27. Let us see if you can download DEM for the watershed boundary corresponding 
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

## Fetched resources (external URLs)

### JN-DEM Access (notebook)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/2025_Miniworkshop/Coursepage_DA3_DEM_Access_v9a.ipynb

## <span style="color:green"><h1><center>DEM Access and Visualization from USGS AWS</center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'>We will download DEM raster files from USGS National Elevation Dataset Amazon Web Service using the extents of watershed shapefile accessed using USGS site number. Later, the DEM raster files will be plotted along with watershed boundary.</p> 

## <span style="color:green"> Data Source and Availibility </span>

<p style='text-align: justify;'>USGS-DEM, available in 1 or 1/3 or 1/9 arc-second</p>

<img src="DataAvailibility_202504.png" alt="Data Availibility" style="max-width: 100%; height: auto;">


## <span style="color:green">Overview of steps </span>
<ol type="1">
    <span style="color:red"><li>Using USGS Station Number, get the shapefile for a  basin (watershed) and it extents</li></span>
    <span style="color:red"><li>Download the DEM from USGS-Amazon Web Service</li></span>
     <span style="color:red"><li>Plotting the Unmerged Raster Tiles</li></span>



## <span style="color:green">Step 0: Import the packages/modules required for this exercise</span>

We need different packages as shown below. It can be either installed using pip method or conda method.


```python
## Import the modules/packages/libraries required
import math
import numpy as np
import os
from os.path import expanduser
import matplotlib.pyplot as plt

from pynhd import NLDI
from pygeohydro import NWIS

import urllib.request
import progressbar
import rasterio
import rasterio.plot

import geopandas as gpd
from shapely.geometry import Polygon, Point

from datetime import datetime

import sys
sys.path.append("/srv/shared/data_dem_access/")
from USGS_sites_map import create_USGS_sites_map,display_watershed_site 
```

```python
## Display the verison numbers of important packages
print(f"NumPy version: {np.__version__}")
import pynhd
print(f"PyNHD version: {pynhd.__version__}")
del pynhd
import pygeohydro
print(f"PyGeoHydro version: {pygeohydro.__version__}")
del pygeohydro
print(f"Rasterio version: {rasterio.__version__}")
print(f"GeoPandas version: {gpd.__version__}")
import shapely
print(f"Shapely version: {shapely.__version__}")
del shapely
print(f"Python version: {sys.version}")
```

## <span style="color:green">Find the USGS Site ID from below map with drainage area less than 1000 sq mi</span> 
<ul>
<li>1. Zoom-in into <span style="color:red">desired location.</span></li>
<li>2. Pick the USGS site and <span style="color:red"> copy the site number.</span></li>

```python
create_USGS_sites_map()
```

## <span style="color:green">Step 1a: Input USGS Site, DEM resolution, and create a directory</span> 
<ul>
<li>Input: <span style="color:red">USGS Site ID</span></li>
<li>Input: <span style="color:red">Desired spatial resolution in arc-seconds. Either 1 for 1 arc-second, 13 for 1/3 arc-second, or 19 for 1/9 arc-second</span></li>
<li>Create: <span style="color:red">Folder for storing input raster files from USGS AWS</span></li>

```python
## Input the USGS site number to get the shapefile
## E.g. "04180000" has a drainage area of 270 sq mi and can downloaded within 2-3 minutes
## But "03335500" has a drainage area of 7267 sq mi and needs for time and space
## WRITE CODE BELOW


## Get site identifiers
site_info = NWIS().get_info({"site": site_id}, expanded=True)


## Get the watershed using USGS station number using pynhd module
## Check if watershed shapefile exist in USGS Hydro Network-Linked Data Index (NLDI) database
try:
    watershed=NLDI().get_basins(site_id,fsource='nwissite')
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
    print(f"Shapefile exists in NLDI databse for USGS {site_id} : {site_info['station_nm'].iloc[0]}.")
    
except Exception:
    print(f"No shapefile exists in NLDI databse for USGS {site_id} : {site_info['station_nm'].iloc[0]}.\nTrying a local collection...")
    watersheds_local_collection=gpd.read_file("/srv/shared/data_dem_access/USGS_polygons.shp")
    watershed=watersheds_local_collection[watersheds_local_collection.identifier==site_id]
    ## Adding "USGS-" to identifier column
    watershed.loc[:,'identifier'] = watershed['identifier'].apply(lambda x: f"USGS-{x}")
    print(f"\n\nShapefile exists in local collection and is available")
    
except Exception:
    print(f"Sorry!\nNo shapefile exists in local collection also for USGS {site_id} : {site_info['station_nm'].iloc[0]}.\nPlease select another USGS site.")
```

```python
## Resolution of required DEM
## USGS-AWS offers data in different spatial resolution like 1/3 arc second (code = 13), 1/9 arc second (code = 19; currently unavailable)
## WRITE CODE BELOW

```

## <span style="color:green">Display the watershed and USGS site</span> 
<ul>

```python
display_watershed_site(site_id)
```

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
folder_input=f"{folder_main}/data_{site_id}"
check_create_path_func(folder_input)
dem_files_store=f'{folder_input}/raw_{site_id}'
check_create_path_func(dem_files_store)
```

## <span style="color:green">Step 1b: Plot the basin and save the shapefile locally</span> 

<ul>
<li>Input: <span style="color:red">Get a input station</span></li>
<li>Output: <span style="color:red">Plot the basin using geopandas</span></li>
<li>Output: <span style="color:red">Save the basin file as shapefile</span></li>
    

```python
## Transform to Albers Equal Area projection (EPSG:5070)
watershed_albers = watershed.to_crs(epsg=5070)
## Calculate the area in square miles
## 1 square meter = 0.386102 square miles
watershed_albers['area_sq_mi'] = watershed_albers.area / 1e6 * 0.386102  
#print(watershed_albers['area_sq_mi'][0])

## Get site identifiers
site_info = NWIS().get_info({"site": site_id}, expanded=True)

## Gage site
point = gpd.GeoDataFrame(geometry=[Point(site_info["dec_long_va"].iloc[0],
                                        site_info["dec_lat_va"].iloc[0])], 
                         crs="EPSG:4326")

## Plot the watershed
## DD indicates latitude/ longitude degrees is in decimal
ax = watershed.plot(facecolor="blue", 
                    edgecolor="black", 
                    alpha=0.35,
                    figsize=(8, 8))
point.plot(ax=ax, color='red', marker='*', markersize=100, label='Site Location')

plt.title(f"Watershed Shapefile in {watershed.crs} Projected CRS\n(USGS:{site_id}, "+
          f"Area = {round(watershed_albers['area_sq_mi'].iloc[0],2)} sq. mi.)")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Saving the watershed file as a shapefile at desired location
## WRITE THE CODE BELOW




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
## Filter the dataframe by matching the site identifier column and obtaining the first value from HUC2 NAME column
specific_huc = watershed_with_huc[watershed_with_huc['identifier'] == f'USGS-{site_id}']['NAME'].iloc[0]
selected_huc2=huc_map_proj[huc_map_proj['NAME']==specific_huc]
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
point.plot(ax=ax, color='red', marker='*', markersize=25, label='Site Location')
ax.set_xlim(xmin=-135)
ax.set_ylim(ymin=15)
ax.set_title(f"Inset Map for the watershed\n(for USGS {site_id}: {site_info['station_nm'].iloc[0]})")

## Plot the inset HUC2 (HUC2 map)
inset_ax = fig.add_axes([0.16, 0.23, 0.2, 0.2])  # [left, bottom, width, height]
selected_huc2.plot(ax=inset_ax, color='lightblue', edgecolor='black')
watershed_map.plot(ax=inset_ax, color='blue', edgecolor=None)
watershed_bbox_gdf.plot(ax=inset_ax, color=None, edgecolor='red',alpha=0.5)
point.plot(ax=inset_ax, color='red', marker='*', markersize=20, label='Site Location')
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

## <span style="color:green">Step 4a (sequential download): Downloading the DEM from USGS-Amazon Web Service</span>

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

## <span style="color:green">Step 4a (threading for faster download): Downloading the DEM from USGS-Amazon Web Service</span>

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

## <span style="color:green">Step 4a: Time Comparison</span>

```python
## Time Comparison

print(f'Time taken for sequential downloading: {end_time_seq-start_time_seq}')
print(f'Time taken for parallel downloading: {end_time_thread-start_time_thread}')
print(f'\nEfficiency: {round((end_time_seq-start_time_seq)/(end_time_thread-start_time_thread),1)}')

```

## <span style="color:green">Step 4b: Plotting the downloaded (single/unmerged) DEMs along with watershed shapefile</span>

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
    title=f"Unmerged Raster DEMs with a spatial resolution of {arc_seconds[resolution]}\n (for USGS {site_id}: {site_info['station_nm'].iloc[0]})"
else:
    title=f"Single Raster DEMwith a spatial resolution of {arc_seconds[resolution]}\n (for USGS {site_id}: {site_info['station_nm'].iloc[0]})"
    
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
