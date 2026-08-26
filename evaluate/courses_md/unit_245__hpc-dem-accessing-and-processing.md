---
title: "Geospatial & Hydrological Science: HPC Based DEM Accessing and Processing (Single Job)"
unit_id: 245
course_id: 0
level: "Developer"
slug: hpc-dem-accessing-and-processing
is_course: 0
---

# Geospatial & Hydrological Science: HPC Based DEM Accessing and Processing (Single Job)

## Extracted resources (local files)

### PDF-HPC DEM Processing
*Source file:* `Instructions_DP9_HPC_DEM_Processing_v01.pdf`  ·  *type:* file

HPC Tool: Accessing & Processing Digital Elevation 
Model (DEM) data for larger waterhseds 
 
Prepared by  
Jibin Joseph^, Rajesh Kalyanam* and Venkatesh Merwade^  
* Rosen Center for Advanced Computing, Purdue University  
^ Lyles School of Civil Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
In this tutorial, we will use HPC resources to access and process DEM for larger 
watersheds with USGS site ID and resolution. We will use community-centered 
CyberGIS platform to work with higher number of DEM tiles. 
 
Instructions 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
    
 
2. Either you can select Sign in with CILogon with institutional credentials or 
ORCID or use Google Account 
(there are a number of login 
options in the dropdown and if 
nothing works you may need to 
register as a new user as you are 
accessing CyberFaCES for the 
first time). Also, select the 
“Remember this selection” option

for future easy access to CyberFaCES. 
 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”. 
4. Check Type on the left as “Courses” and select “WaterSciCon24 Hands-On 
Workshop: Web-based Modules on Geospatial Data Processing Using Python” 
course from the list of courses as shown below.  
 
 
 
5. Click on “Start 
now” and you 
will be able to 
see the material 
for completing 
this workshop. 
If you have not 
completed the 
Pre-Workshop, 
please complete 
the first item. 
6. The handout (in 
PDF 
format) 
and the Jupyter 
Notebook 
for 
the 
coding 
exercises 
for 
this workshop can be found here.  Now, we will complete the Geospatial & 
Hydrological Science: HPC Based DEM Accessing and Processing (Single Job). 
Select “I-GUIDE Launch Link” Jupyter Notebook and it will redirect to the 
Interactive Jupyter Notebook Hub. Please note that we are using different Jupyter 
Hub here. 
7. Again, either you can select your institutional credentials or ORCID or your 
Google Account. Select the remember your login option for future access to 
CyberFaces. Enter the credentials to log on to the CyberFaCES platform. 
8. Be patient until the Notebook opens, and it has the correct Kernel (iguide-ewd) as 
shown below. This kernel 
has all modules preinstalled 
for completing this tutorial. 
9. Run the first code cell to im
port the essential modules i
n the current kernel. Also, e
xecute the next cell to get th

e version number of the packages that we will be using in this module. 
 
Step 1: Define the variables  
10. Define the USGS site ID and resolution. We will use 05331000 for Mississippi River 
at St. Paul, MN and the resolution as 1/3 arc-second. This watershed has an area 
of around 36000 sq. mi. and it can be completed using earlier modules due to high 
RAM requirements. 
Step 2: HPC Job Submission 
11. Run the next cell and it will show the user interface of CyberGIS. In the Job 
Configuration Tab, go to Slurm Computing Configurations, set the time to 30 
minutes and number of CPUs per task as 128. Submit the job and be patient.

12. Once the job is completed you will see Job is completed. You can get the current 
progress in “Your Job Status” tab. 
13. Now, select the preview folder in the 
Download 
Job 
Result 
and 
click 
Download. Wait until it is completed.  
 
 
Step 3: Plotting the clipped DEM (preview) 
14. Run the next cell to download the preview plot created for the large watershed. 
The file downloaded from HPC to local platform and is plotted. 
 
Ok, you have now completed the tutorial successfully. Congratulations!

### Screenshot_28-7-2025_142046_www.rcac.purdue.edu
*Source file:* `Instructions_DP9_HPC_DEM_Processing_v02.pdf`  ·  *type:* file

HPC Tool: Accessing & Processing Digital Elevation 
Model (DEM) data for larger waterhseds 
 
Prepared by  
Jibin Joseph^, Rajesh Kalyanam* and Venkatesh Merwade^  
* Rosen Center for Advanced Computing, Purdue University  
^ Lyles School of Civil Engineering, Purdue University 
joseph57@purdue.edu, vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
 
Introduction 
 
In this tutorial, we will use HPC resources to access and process DEM for larger 
watersheds with USGS site ID and resolution. We will use community-centered 
CyberGIS platform to work with higher number of DEM tiles. 
 
Instructions 
1. Open a browser and navigate to the following link “https://cyberfaces.org“. Click 
on the Login at the upper right side. 
    
 
2. Either you can select Sign in with CILogon with institutional credentials or 
ORCID or use Google Account 
(there are a number of login 
options in the dropdown and if 
nothing works you may need to 
register as a new user as you are 
accessing CyberFaCES for the 
first time). Also, select the 
“Remember this selection” option

for future easy access to CyberFaCES. 
 
3. Navigate to “Learn” on the top ribbon and select “Explore Modules”. 
4. Check Type on the left as “Courses” and select “I-GUIDE Forum Hands-On 
Workshop: Web-based Modules on Geospatial Data Processing Using Python” 
course from the list of courses as shown below.  
 
5. Click on “Start now” and you will be able to see the material for completing this 
workshop. If you have not completed the Pre-Workshop, please complete the first 
item. 
6. The handout (in PDF format) and the Jupyter Notebook for the coding exercises 
for this workshop can be found here.  Now, we will complete the Geospatial & 
Hydrological Science: HPC Based DEM Accessing and Processing (Single Job). 
Select “I-GUIDE Launch Link” Jupyter Notebook and it will redirect to the 
Interactive Jupyter Notebook Hub. Please note that we are using different Jupyter 
Hub here. 
7. Again, either you can select your institutional credentials or your Google Account. 
Select the remember your login option for future access to CyberFaces. Enter the 
credentials to log on to the CyberFaCES platform. 
8. Be 
patient 
until 
the 
Notebook opens, and it has 
the 
correct 
Kernel 
(geohydro-pynhd) 
as 
shown below. This kernel 
has all modules preinstalled 
for completing this tutorial. 
9. Run the first code cell to im
port the essential modules in the current kernel. Also, execute the next cell to get t
he version number of the packages that we will be using in this module. 
 
Step 1: Define the variables  
10. Define the USGS site ID and resolution. We will use 05331000 for Mississippi River 
at St. Paul, MN and the resolution as 1/3 arc-second. This watershed has an area 
of around 36000 sq. mi. and it cannot be completed using earlier modules due to 
high RAM requirements. 
Step 2: HPC Job Submission 
11. Run the next cell and it will show the user interface of CyberGIS. In the Job 
Configuration Tab, go to Slurm Computing Configurations, set the time to 30 
minutes and number of CPUs per task as 128. Submit the job and be patient.

12. Once the job is completed you will see Job is completed. You can get the current 
progress in “Your Job Status” tab. 
13. Now, select the preview folder in the 
Download 
Job 
Result 
and 
click 
Download. Wait until it is completed.  
 
 
Step 3: Plotting the clipped DEM (preview) 
14. Run the next cell to download the preview plot created for the large watershed. 
The file downloaded from HPC to local platform and is plotted.

Ok, you have now completed the tutorial successfully. Congratulations!

## Fetched resources (external URLs)

### I-GUIDE Launch Link (link)
*URL:* https://jupyter.iguide.illinois.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FI-GUIDE%2Fhydroewd&urlpath=lab%2Ftree%2Fhydroewd%2FCoursepage_DEM_GeoEDF_v4.ipynb+&branch=2025_Miniworkshop

[github: could not resolve raw content]

### JN-SingleHPC (notebook)
*URL:* https://jupyter.iguide.illinois.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FI-GUIDE%2Fhydroewd&urlpath=lab%2Ftree%2Fhydroewd%2FDEM_HPC_Processing%2FDEM_SingleJob.ipynb+&branch=main

[github: could not resolve raw content]
