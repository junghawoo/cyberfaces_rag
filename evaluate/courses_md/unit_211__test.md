---
title: "test"
unit_id: 211
course_id: 0
level: "Foundation"
slug: test
is_course: 0
---

# test

## Extracted resources (local files)

### Introduction to Python_Core Concepts for RS Applications
*Source file:* `Introduction to Python_Core Concepts for RS Applications.pdf`  ·  *type:* file

Introduction to Python: Core Concepts for Remote 
Sensing Applications 
Prepared by  
Mohamed Abdelkader1, Jorge Bravo1, Marouane Temimi 1, and Jibin Joseph2  
1Civil, Environmental, and Ocean Engineering Department, Stevens Institute of 
Technology 
2School of Civil Engineering, Purdue University 
mabdelka@stevens.edu 
 
FAIR Science in Climate 
 
 
Objective 
   - Understand the basic syntax and structure of Python programming. 
   - Learn to work with different Python data types, including integers, decimals, strings, 
lists, tuples, and dictionaries. 
   - Develop the ability to perform arithmetic operations and data manipulations in 
Python. 
   - Master the foundational concepts of string formatting for better output presentation. 
   - Gain familiarity with Python's control structures, including loops and conditional 
statements. 
   - Acquire the skills to manage and iterate over collections of data, which is crucial for 
processing remote sensing datasets. 
Overview of steps 
1. Introduction to Python's interactive environment and how it can be used in remote 
sensing. 
2. Exploration of Python's basic data types and their relevance to data representation in 
remote sensing. 
3. Performing and understanding operations between integers and decimals, simulating 
real-world measurements and calibrations. 
4. Handling and formatting strings to annotate and label remote sensing data. 
5. Creating and manipulating lists, tuples, and dictionaries, essential for organizing and 
accessing sensor data. 
6. Iterative processes in Python, learning to loop through data sequences which is 
common in satellite data processing.  
Resources 
Remote Sensing Tutorials 
Guide to GOES-R Series Data 
GOES ABI (Advanced Baseline Imager) Realtime Imagery 
GOES Image Viewer

Instructions 
1. Log on to mygeohub.org and launch Jupyter Notebook with Anaconda 5.1. 
2. Hit on Click Here to go to your Home Directory option to access your home directory. 
This is the location where you can store your code and data. 
3. It is advisable to create a separate folder to store code and data for this tutorial 
which makes it accessible in the future. Go ahead and create a folder named 
Module06 to store the code of the current tutorial.  
4. Click on the notebook file available on the course page. Hit the Save as option 
available in the File menu and save it in the earlier created folder. 
5. Review the introductory overview of Python's capabilities in remote sensing 
applications to understand the context and relevance of programming in this field.  
 
 
6. Review the instructions for using Jupyter Notebooks as our interactive computing 
environment.

7. Execute the code cell in #test_cell using Ctrl+Enter to practice running a simple print 
command. 
 
8. Run the provided code to see how variables work in Python and observe how a variable can 
change types from a string to a number. Notice how the 'print' function is used to clarify 
the output, making the data's context and changes clear and understandable.

9. Execute the code to observe how integers and decimals represent different data types in 
weather monitoring. Pay attention to the operations between them to see their combined 
effect on the results. 
 
10. Run the code to see how strings function to store and present textual data such as satellite 
names and note how formatted print statements enhance data readability.

11. Execute the code examples to observe how different methods of string formatting work in 
Python and how they can be applied to neatly display weather-related data.

12. Follow the examples provided to learn how lists are defined and used in Python for 
organizing diverse types of data, such as weather observations and satellite information. 
Pay attention to how lists can contain different data types and how this flexibility is 
advantageous in meteorological analysis. 
 
13. For this tutorial on tuples in Python, we're focusing on how to create an immutable 
collection of items, which is useful for storing fixed sets of data such as instrument names 
on satellites. Observe how once defined, the contents of the tuple cannot be altered, 
ensuring data integrity for constants in meteorological analysis.

14. This portion of the tutorial explains how to utilize dictionaries in Python to store and 
manipulate weather data parameters. Dictionaries allow us to create a structured dataset 
with key-value pairs, ideal for meteorological data management. Each key-value pair 
corresponds to a weather parameter and its measured value, making the data easy to access 
and update, as demonstrated by the addition of the 'UV Index' to the existing dictionary. 
 
15. This section introduces the concept of iterations using the `for` loop in Python.  
 
#Iteration_cell: By iterating over the keys of the `weather_parameters` dictionary, we 
print out each weather parameter, demonstrating a simple yet effective way to enumerate 
the keys in a dictionary. This operation mimics a common task in data handling where 
listing all the parameters in a dataset is necessary.

#Adding_parameters_Cell: Here we see how to enhance the `weather_parameters` 
dictionary by adding new entries. Specifically, we introduce 'Atmospheric Pressure' and 
'Dew Point' with corresponding values. Additionally, the snippet showcases string 
formatting in Python by using the `format()` method. With this technique, we can 
construct a readable and informative sentence that incorporates our data directly into the 
string, which is particularly useful for generating reports or output for further analysis. 
 
#Exploring_itmes_cell: In this code block, we continue to explore iterations with a `for` 
loop, this time iterating over both keys and values of the `weather_parameters` dictionary 
by utilizing the `.items()` method. This approach is crucial when one needs to process both 
the name (key) and the recorded measurement (value) of each weather parameter. The loop 
prints out each parameter and its corresponding value in a format that is suitable for 
reviewing collected meteorological data or preparing it for presentation or further 
computation. 
 
 
Ok, you have completed the tutorial! 
 
Turn-in 
For this assignment, you will be demonstrating your skills in manipulating and 
presenting meteorological data using Python dictionaries and iterations. Please follow 
the steps outlined below to complete your task and submit your work:

1. Add a new weather parameter to the `weather_parameters` dictionary: 
- Choose a weather parameter that is commonly monitored by geostationary satellites 
(for example, Solar Radiation, Visibility, etc.). 
- Insert the new weather parameter into the dictionary with a hypothetical value. 
- Print the updated dictionary to verify the addition of the new parameter. 
 
2. Create a formatted output using an f-string: 
 
- Craft a message using a formatted string literal (f-string) to include dynamic data from 
the `weather_parameters` dictionary. 
- Your message should be clear, informing the reader about one of the parameters and its 
value, mimicking a real-world data report. 
 
3. Prepare your submission documents: 
 
- Generate a PDF document that captures the final state of the `weather_parameters` 
dictionary, including the new parameter you added. 
- The document should also display the formatted message you created with the f-string. 
- Additionally, create a "readme" or instruction file that outlines the steps you followed 
to complete the assignment. This document should serve as a guide for anyone reviewing 
your code or results. 
 
4. Upload your documents to the designated submission platform: 
 
- Your submission should include the following: 
- The PDF document with your updated `weather_parameters` dictionary and formatted 
message. 
- The original Python script used to produce these results. 
- The "readme" or instruction file detailing the steps of your process. 
- Name your submission as "Weather Data Analysis for [Your Chosen Parameter]" to 
reflect the content of your work. 
- In the description or abstract, provide a brief overview of the contents of your 
submission, emphasizing the addition of the new weather parameter and the use of f-
strings in your analysis. 
 
Ensure that all files are correctly formatted, legible, and free of errors before submission. 
If you encounter any issues or have questions about the assignment, please reach out to 
your instructor or teaching assistant for guidance.

## Fetched resources (external URLs)

### test2 (notebook)
*URL:* https://github.com/I-GUIDE/hydroewd/blob/main/Coursepage_DEM_GeoEDF.ipynb

## <span style="color:green"><h1><center>HPC TOOL: DEM Accessing & Processing</center></h1></span>
<center>Prepared by <br>
    <b>Noah Oller Smith, Rajesh Kalyanam, Jibin Joseph and Venkatesh Merwade</b><br> 
Lyles School of Civil Engineering, Purdue University<br>
vmerwade@purdue.edu<br>
<b><br>
    FAIR Science in Water Resources</b><br></center>


## <span style="color:green">Objective</span>
<p style='text-align: justify;'> The objective of this tutorial is to peform the accessing and processing of DEM data for larger watershed and/or with resolution. We will input the site ID, resolution and this tutorial will give you back clipped raster for any regions across CONUS.</p> 

```python
## Let's try higher resolution of 1/3 arc-second
site_id = '04180000'
resolution = '13'
```

```python
params_dem_fetch = {"site_id": site_id,
                    "resolution": resolution}
params_dem_fetch
```

## <span style="color:green">HPC tool</span>
<p style='text-align: justify;'> TWe will use Cyber GIS comupte tool from UIUC</p> 

```python
import cybergis_compute_client
from cybergis_compute_client import CyberGISCompute
import os
```

## <span style="color:green">Step 1: Access DEM raster tiles to cover the watershed corresponding for given site_id and resolution</span>
<p style='text-align: justify;'> </p> 

```python
cybergis = CyberGISCompute(url="cgjobsup.cigi.illinois.edu", isJupyter=True, protocol="HTTPS", port=443, suffix="v2")
cybergis.show_ui(defaultJob="Watershed_DEM_Raster_Connector", input_params=params_dem_fetch)
```

## <span style="color:green">WAIT UNTIL LAST JOB IS FINISHED. CHECK "Your Job Status" TAB BEFORE PROCEEDING</span>
<p style='text-align: justify;'> </p> 

```python
## Collect the job id from previous job
jobid_dem_connector = cybergis.job.id
jobid_dem_connector
```

## <span style="color:green">Step 2: Merge the downloaded DEM raster tiles </span>
<p style='text-align: justify;'> </p> 

```python
params_dem_merge = {"input_path": jobid_dem_connector,
                    "merged_filename": f'merged_{resolution}_{site_id}'}
params_dem_merge
```

```python
cybergis = CyberGISCompute(url="cgjobsup.cigi.illinois.edu", isJupyter=True, protocol="HTTPS", port=443, suffix="v2")
cybergis.show_ui(defaultJob="DEM_Raster_Merging_Processor", input_params=params_dem_merge)
```

## <span style="color:green">WAIT UNTIL LAST JOB IS FINISHED. CHECK "Your Job Status" TAB BEFORE PROCEEDING</span>
<p style='text-align: justify;'> </p> 

```python
## Collect the job id from previous job
jobid_dem_merge = cybergis.job.id
jobid_dem_merge
```

## <span style="color:green">Step 3: Reproject the watershed shapefile and merged raster tile to projected coordinate system </span>
<p style='text-align: justify;'> </p> 

```python
params_dem_reproject = {"raster_path": jobid_dem_merge,
                        "site_id": site_id,
                        "resolution": resolution}
params_dem_reproject
```

```python
cybergis = CyberGISCompute(url="cgjobsup.cigi.illinois.edu", isJupyter=True, protocol="HTTPS", port=443, suffix="v2")
cybergis.show_ui(defaultJob="DEM_Raster_Reprojection_Processor", input_params=params_dem_reproject)
```

## <span style="color:green">WAIT UNTIL LAST JOB IS FINISHED. CHECK "Your Job Status" TAB BEFORE PROCEEDING</span>
<p style='text-align: justify;'> </p> 

```python
## Collect the job id from previous job
jobid_dem_reproject = cybergis.job.id
jobid_dem_reproject
```

## <span style="color:green">Step 4: Clip the reprojected raster tile using the projected watershed shapefile </span>
<p style='text-align: justify;'> </p> 

```python
params_dem_clip = {"raster_path": jobid_dem_reproject,
                   "site_id": site_id,
                   "resolution": resolution}
params_dem_clip
```

<h4 style="color:red;"> User Interaction Required </h4>

- Run the cell below 
- Click on "Submit Job" on the "Your Job Status" tabpage 
- Wait until Job is finished (2-3 mins)
- Switch to "Download Job Result" tabpage
- Choose "/" and click on Download
- Wait until downloading is finished
- Proceed to the next cell

```python
cybergis = CyberGISCompute(url="cgjobsup.cigi.illinois.edu", isJupyter=True, protocol="HTTPS", port=443, suffix="v2")
cybergis.show_ui(defaultJob="DEM_Raster_Clipping_Processor", input_params=params_dem_clip)
```

## <span style="color:green">VERY IMPORTANT. THERE ARE TWO STEPS HERE AS FOLLOWS: 
1. WAIT UNTIL LAST JOB IS FINISHED. CHECK "Your Job Status" TAB BEFORE PROCEEDING
2. GO TO "DOWNLOAD JOB ..." TAB AND CLICK DOWNLOAD TO SAVE THE FILE LOCALLY FOR PLOTTING</span>
<p style='text-align: justify;'> </p>

```python
clipped_output = cybergis.recentDownloadPath
clipped_output
if not os.path.isfile(os.path.join(clipped_output, f'clipped_raster_{site_id}.tif')):
    display(HTML('<h4 style="color:red;">It appears you did not download the job results per instruction above, please double check!</h4>'))
```

## <span style="color:green">Step 5: Visualize the clipped raster data </span>

```python
import matplotlib.pyplot as plt
import rasterio
import rasterio.plot

fig, ax = plt.subplots(figsize=(8, 8))

clipped_raster_output = cybergis.recentDownloadPath
local_raster_filename=fr'{clipped_raster_output}/clipped_raster_{site_id}.tif'
raster = rasterio.open(local_raster_filename)
rasterio.plot.show(raster,
                   ax=ax,
                   cmap='viridis')
## Free up memory
del raster
del fig,ax
```

## <span style="color:green">We are done. Congraluations! </span>
