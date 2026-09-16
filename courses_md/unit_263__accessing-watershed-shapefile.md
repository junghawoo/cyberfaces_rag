---
title: "Accessing Watershed Shapefile Using Python"
unit_id: 263
course_id: 0
level: "Foundation"
slug: accessing-watershed-shapefile
is_course: 0
---

# Accessing Watershed Shapefile Using Python

## Extracted resources (local files)

### Instructions_AccessingShapefile_cyberfaces_v2.pdf
*Source file:* `Instructions_AccessingShapefile_cyberfaces_v2.pdf`  ·  *type:* pdf

Accessing Watershed Shaepfile Corresponding to USGS 
Site Number 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil and Construction Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
This workflow demonstrates how to access and visualize watershed boundaries for a 
given USGS site. Using the pynhd package’s NLDI (Network Linked Data Index) service, 
we query a watershed polygon by providing a site number and then export the results as 
a shapefile. The shapefile can be saved locally for future use or analysis. To ensure correct 
geographic representation, the pyproj CRS (Coordinate Reference System) is applied. 
Finally, the watershed shapefile is plotted to provide a clear spatial visualization, making 
it easier to integrate into hydrologic studies, geospatial analyses, or data-driven mapping 
projects. 
 
 
Computer Requirements 
 
The tutorial can be completed through Python-based Jupyter Notebook with a proper 
conda environment with the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “ct-fair” kernel in the CyberFaCES 
platform. The user does not have to install any modules for completing this tutorial in 
the CyberFaCES platform. However, if a user wants to use this in another platform, the 
pynhd package is needed for getting shapefile based on a USGS site number.  
  
 
Overview of steps 
 
1. Input the USGS site number and get the shapefile. 
2. Plot the shapefile.

Instructions 
 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with institutional credentials or ORCID 
or use Google Account (there are a number of login options in the dropdown and 
if nothing works you may need to register as a new user as you are accessing 
CyberFaCES for the first time). Also, select the “Remember this selection” option 
for future easy access to CyberFaCES. 
 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”. 
4. Select “Accessing Watershed Shapefile Using Python” module from the list of 
modules. 
5. Click on “Start now” and you will be able to see the material for completing this 
module. Click on the Jupyter Notebook file containing the workflow to access the 
shapefile. 
6. Again, either you can select your institutional credentials or ORCID or your 
Google Account in the dropdown. Also, select the “Remember this selection” 
option for future easy access to CyberFaCES. Enter the credentials to log on to the 
CyberFaCES platform.

7. Be patient until the Notebook is fetched from GitHub and gets loaded in Jupyter 
Hub environment. Make sure that it has the correct Kernel (ct-fair) as shown below. 
This kernel has all modules preinstalled for completing this tutorial. 
 
8. Run the first code cell to import the essential packages in the current kernel. 
9. Step 1a - Now, we have to input the USGS site number, and create the folder to 
save the downloaded shapefile. You have to write the code to provide a site id,  
and folder location. Complete the cell in the Jupyter Notebook file as shown in the 
below figure. 
 
10. Let us get the shapefile for the watershed using “pynhd” module using the site 
number. We will plot the watershed shapefile and save it to a local directory.  
Complete the cell in the Jupyter Notebook file as shown in the below figure. You

have to write the code to get the watershed boundary and save it with a name 
inside the folder created in the previous cell. Execution of this code will add files 
in the input directory. 
 
11. Step 1b - If you use the default USGS site number, you should get a shapefile 
similar to the one shown below. The shapefile corresponding to the USGS Site - 
Cedar Creek Near Cedarville – located in Indiana with a drainage area of 270 sq. 
mi is plotted below. You can also change the USGS site number according to your 
study area provided it is available in the NLDI database. 
 
 
12. Step 2 – In the next step, we determine the coordinate system and spatial extents 
of the shapefile. The data is referenced in EPSG:4326 (WGS84 Geographic 
Coordinate System), which represents locations in degrees of latitude and 
longitude. This CRS is widely used for global datasets, mapping, and geospatial 
analysis. However, for advanced or area‐based calculations, transformation into a

Projected Coordinate System (PCS) may be required. The calculated extents 
(bounding values) specify the geographic boundaries of the basin, providing a 
framework for visualization and further spatial analysis. 
 
13. Let us see if you can download the watershed boundary corresponding to the 
assigned USGS site and plot the boundary. The assigned watershed can be found 
in Brightspace grade center.  
 
Ok, you have now completed the tutorial successfully. Congratulations! 
 
References 
1. Chegini, T., Li, H. Y., & Leung, L. R. (2021). HyRiver: Hydroclimate Data Retriever. 
Journal of Open Source Software, 6(66), 3175.

### Instructions_DA0_AccessingShapefile_cyberfaces_v3.pdf
*Source file:* `Instructions_DA0_AccessingShapefile_cyberfaces_v3.pdf`  ·  *type:* pdf

Accessing Watershed Shaepfile Corresponding to USGS 
Site Number 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil and Construction Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
This workflow demonstrates how to access and visualize watershed boundaries for a 
given USGS site. Using the pynhd package’s NLDI (Network Linked Data Index) service, 
we query a watershed polygon by providing a site number and then export the results as 
a shapefile. The shapefile can be saved locally for future use or analysis. To ensure correct 
geographic representation, the pyproj CRS (Coordinate Reference System) is applied. 
Finally, the watershed shapefile is plotted to provide a clear spatial visualization, making 
it easier to integrate into hydrologic studies, geospatial analyses, or data-driven mapping 
projects. 
 
 
Computer Requirements 
 
The tutorial can be completed through Python-based Jupyter Notebook with a proper 
conda environment using the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “ct-fair” kernel in the CyberFaCES 
platform. The user does not have to install any modules for completing this tutorial in 
the CyberFaCES platform. However, if a user wants to use this in another platform, the 
pynhd package is needed for getting shapefile based on a USGS site number.  
  
 
Overview of steps 
 
1. Input the USGS site number and get the shapefile. 
2. Plot the shapefile.

Instructions 
 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with institutional credentials or ORCID 
or use Google Account (there are a number of login options in the dropdown and 
if nothing works you may need to register as a new user as you are accessing 
CyberFaCES for the first time). Also, select the “Remember this selection” option 
for future easy access to CyberFaCES. 
 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”. 
4. Select “Accessing Watershed Shapefile Using Python” module from the list of 
modules. 
5. Click on “Start now” and you will be able to see the material for completing this 
module. Click on the Jupyter Notebook file containing the workflow to access the 
shapefile. 
6. Be patient until the Notebook is fetched from GitHub and gets loaded in Jupyter 
Hub environment. Make sure that it has the correct Kernel (ct-fair) as shown below. 
This kernel has all modules preinstalled for completing this tutorial.

7. Run the first code cell to import the essential packages in the current kernel. 
8. Step 1a - Now, we have to input the USGS site number, and create the folder to 
save the downloaded shapefile. You have to write the code to provide a site id,  
and folder location. Complete the cell in the Jupyter Notebook file as shown in the 
below figure. 
 
9. Let us get the shapefile for the watershed using “pynhd” module using the site 
number. We will plot the watershed shapefile and save it to a local directory.  
Complete the cell in the Jupyter Notebook file as shown in the below figure. You 
have to write the code to get the watershed boundary and save it with a name 
inside the folder created in the previous cell. Execution of this code will add files 
in the input directory.

10. Step 1b - If you use the default USGS site number, you should get a shapefile 
similar to the one shown below. The shapefile corresponding to the USGS Site - 
Cedar Creek Near Cedarville – located in Indiana with a drainage area of 270 sq. 
mi is plotted below. You can also change the USGS site number according to your 
study area provided it is available in the NLDI database. 
 
 
 
11. Step 2 – In the next step, we determine the coordinate system and spatial extents 
of the shapefile. The data is referenced in EPSG:4326 (WGS84 Geographic 
Coordinate System), which represents locations in degrees of latitude and 
longitude. This CRS is widely used for global datasets, mapping, and geospatial 
analysis. However, for advanced or area‐based calculations, transformation into a 
Projected Coordinate System (PCS) may be required. The calculated extents

(bounding values) specify the geographic boundaries of the basin, providing a 
framework for visualization and further spatial analysis. 
 
12. Let us see if you can download the watershed boundary corresponding to the 
assigned USGS site and plot the boundary. The assigned watershed can be found 
in Brightspace grade center.  
 
Ok, you have now completed the tutorial successfully. Congratulations! 
 
References 
1. Chegini, T., Li, H. Y., & Leung, L. R. (2021). HyRiver: Hydroclimate Data Retriever. 
Journal of Open Source Software, 6(66), 3175.

### Instructions_DA0_AccessingShapefile_cyberfaces_v4.pdf
*Source file:* `Instructions_DA0_AccessingShapefile_cyberfaces_v4.pdf`  ·  *type:* pdf

Accessing Watershed Shaepfile Corresponding to USGS 
Site Number 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
Lyles School of Civil and Construction Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
This workflow demonstrates how to access and visualize watershed boundaries for a 
given USGS site. Using the pynhd package’s NLDI (Network Linked Data Index) service, 
we query a watershed polygon by providing a site number and then export the results as 
a shapefile. The shapefile can be saved locally for future use or analysis. To ensure correct 
geographic representation, the pyproj CRS (Coordinate Reference System) is applied. 
Finally, the watershed shapefile is plotted to provide a clear spatial visualization, making 
it easier to integrate into hydrologic studies, geospatial analyses, or data-driven mapping 
projects. 
 
 
Computer Requirements 
 
The tutorial can be completed through Python-based Jupyter Notebook with a proper 
conda environment using the required modules (packages or libraries). This tutorial is 
created for use within the CyberFaCES platform. All the essential modules required to 
complete this tutorial are already available in “ct-fair” kernel in the CyberFaCES 
platform. The user does not have to install any modules for completing this tutorial in 
the CyberFaCES platform. However, if a user wants to use this in another platform, the 
pynhd/geopandas packages are needed for getting shapefile based on a USGS site 
number.  
  
 
Overview of steps 
 
1. Input the USGS site number and get the shapefile. 
2. Plot the shapefile.

Instructions 
 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
 
 
2. Either you can select Sign in with CILogon with institutional credentials or ORCID 
or use Google Account (there are a number of login options in the dropdown and 
if nothing works you may need to register as a new user as you are accessing 
CyberFaCES for the first time). Also, select the “Remember this selection” option 
for future easy access to CyberFaCES. 
 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”. 
4. Select “Accessing Watershed Shapefile Using Python” module from the list of 
modules. 
5. Click on “Start now” and you will be able to see the material for completing this 
module. Click on the Jupyter Notebook file containing the workflow to access the 
shapefile. 
6. Be patient until the Notebook is fetched from GitHub and gets loaded in Jupyter 
Hub environment. Make sure that it has the correct Kernel (ct-fair) as shown below. 
This kernel has all modules preinstalled for completing this tutorial.

7. Run the first code cell to import the essential packages in the current kernel. 
8. Step 1a - Now, we have to input the USGS site number, and create the folder to 
save the downloaded shapefile. You have to write the code to provide a site id,  
and folder location. Complete the cell in the Jupyter Notebook file as shown in the 
below figure. 
 
9. Let us retrieve the watershed shapefile using the NLDI service by querying the site 
number. We will plot the watershed shapefile and save it to a local directory.  
Complete the cell in the Jupyter Notebook file as shown in the below figure. You 
have to write the code to get the watershed boundary and save it with a name 
inside the folder created in the previous cell. Execution of this code will add files 
in the input directory.

10. Step 1b - If you use the default USGS site number, you should get a shapefile 
similar to the one shown below. The shapefile corresponding to the USGS Site - 
Cedar Creek Near Cedarville – located in Indiana with a drainage area of 270 sq. 
mi is plotted below. You can also change the USGS site number according to your 
study area provided it is available in the NLDI database. 
 
 
 
11. Step 1c – You can access the site information stored in the NLDI such as latitude, 
longitude, HUC2 ID, etc., in this step.

12. Step 2 – In the next step, we determine the coordinate system and spatial extents 
of the shapefile. The data is referenced in EPSG:4326 (WGS84 Geographic 
Coordinate System), which represents locations in degrees of latitude and 
longitude. This CRS is widely used for global datasets, mapping, and geospatial 
analysis. However, for advanced or area‐based calculations, transformation into a 
Projected Coordinate System (PCS) may be required. The calculated extents 
(bounding values) specify the geographic boundaries of the basin, providing a 
framework for visualization and further spatial analysis. 
 
13. Let us see if you can download the watershed boundary corresponding to the 
assigned USGS site and plot the boundary. The assigned watershed can be found 
in Brightspace grade center.  
 
Ok, you have now completed the tutorial successfully. Congratulations! 
 
References 
1. Chegini, T., Li, H. Y., & Leung, L. R. (2021). HyRiver: Hydroclimate Data Retriever. 
Journal of Open Source Software, 6(66), 3175.

## Fetched resources (external URLs)

### Jupyter Notebook File (link)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/main/Watershed_Access/Coursepage_DA0_Watershed_Access.ipynb

## <span style="color:green"><h1><center>Downloading Watershed Corresponding to USGS Site Number</center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'>We will watershed shapefile using USGS site number. Save the shapefile and plot it.</p> 

## <span style="color:green">Import the packages/modules required for this exercise</span>

We need different packages as shown below. It can be either installed using pip method or conda method.


```python
## Import the modules/packages/libraries required
import os
import matplotlib.pyplot as plt

from pynhd import NLDI
from pyproj import CRS
```

## <span style="color:green">Step 1a: Input USGS Site, DEM resolution, and create a directory</span> 
<ul>
<li>Input: <span style="color:red">USGS Site</span></li>
<li>Input: <span style="color:red">Desired resolution</span></li>
<li>Create: <span style="color:red">Folder for storing downloaded files from USGS AWS</span></li>

```python
## Input the USGS site number to get the shapefile
## E.g. "04180000" has a drainage area of 270 sq mi and can downloaded within 2-3 minutes
## But "03335500" has a drainage area of 7267 sq mi and needs for time and space
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


## Plot the watershed
## DD indicates latitude/ longitude degrees is followed by immediately followed by decimal
ax = watershed.plot(facecolor="b", 
                    edgecolor="k", 
                    figsize=(8, 8))
plt.title(f"Shapefile corresponding to {site_id} site\n(Coordinate Reference System - {watershed.crs})")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Saving the watershed file as a shapefile at desired location
## WRITE THE CODE BELOW


```

## <span style="color:green">Step 2: Get the Extents and Coordinate System of the shapefile</span>

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

print("\n\n")

print(f"The coordinate system of the watershed is - {watershed.crs}")
```

### Jupyter Notebook File (notebook)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/main/Watershed_Access/Coursepage_DA0_Watershed_Access.ipynb

## <span style="color:green"><h1><center>Downloading Watershed Corresponding to USGS Site Number</center></h1></span>
<center>Prepared by <br>
    <b>Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
joseph57@purdue.edu, vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'>We will watershed shapefile using USGS site number. Save the shapefile and plot it.</p> 

## <span style="color:green">Import the packages/modules required for this exercise</span>

We need different packages as shown below. It can be either installed using pip method or conda method.


```python
## Import the modules/packages/libraries required
import os
import matplotlib.pyplot as plt

from pynhd import NLDI
from pyproj import CRS
```

## <span style="color:green">Step 1a: Input USGS Site, DEM resolution, and create a directory</span> 
<ul>
<li>Input: <span style="color:red">USGS Site</span></li>
<li>Input: <span style="color:red">Desired resolution</span></li>
<li>Create: <span style="color:red">Folder for storing downloaded files from USGS AWS</span></li>

```python
## Input the USGS site number to get the shapefile
## E.g. "04180000" has a drainage area of 270 sq mi and can downloaded within 2-3 minutes
## But "03335500" has a drainage area of 7267 sq mi and needs for time and space
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


## Plot the watershed
## DD indicates latitude/ longitude degrees is followed by immediately followed by decimal
ax = watershed.plot(facecolor="b", 
                    edgecolor="k", 
                    figsize=(8, 8))
plt.title(f"Shapefile corresponding to {site_id} site\n(Coordinate Reference System - {watershed.crs})")
plt.xlabel("Longitude (DD)")
plt.ylabel("Longitude (DD)")

## Saving the watershed file as a shapefile at desired location
## WRITE THE CODE BELOW


```

## <span style="color:green">Step 2: Get the Extents and Coordinate System of the shapefile</span>

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

print("\n\n")

print(f"The coordinate system of the watershed is - {watershed.crs}")
```
