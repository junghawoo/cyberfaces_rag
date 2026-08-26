---
title: "Cyberinfrastructure for FAIR Science Workshop"
unit_id: 289
course_id: 0
level: "Expert"
slug: cyberinfrastructure-for-fair-science-workshop
is_course: 1
objectives:
  - "Help participants become familiar with and learn how to use the tools developed under an NSF Cyberinfrastructure for Sustained Scientific Innovation (CSSI) project, in order to make research data and workflows more FAIR (findable, accessible, interoperable and reusable)."
---

# Cyberinfrastructure for FAIR Science Workshop

**Description:** Tackling today’s grand challenges—ranging from growing populations to climate change and natural disasters—requires managing vast amounts of data from diverse sources. However, researchers often spend significant time wrangling complex data, especially streaming data from sensors, IoT devices, scientific instruments, and geospatial data. These datasets are often large, heterogeneous, and computationally intensive to process. Funded by the National Science Foundation (NSF), our project aims to develop reusable software solutions that address common data wrangling challenges across science and engineering disciplines and train the next-generation workforce in effectively using cyberinfrastructure skills and advanced computing resources. 

The goal of this hands-on workshop is to help participants become familiar with and learn how to use the tools developed under an NSF Cyberinfrastructure for Sustained Scientific Innovation (CSSI) project, in order to make research data and workflows more FAIR (findable, accessible, interoperable and reusable). The workshop activities will be organized around three themes:
* Wrangling data - Resource intensive data processing pipelines using the **_GeoEDF workflow library_**
* Managing continuous data streams - Sensor Data Management with **_StreamCI_** 
* Cyber training - Interactive online learning using the **_CyberFaces_** platform

(more information about these tools is provided in the attached PDF) 
Participants will also receive an overview of High-Performance Computing (HPC) and Cloud Computing on the NSF Anvil cluster and containerization technologies and have opportunities to interact with experts in these areas.

Participant support funds will be provided to assist with travel and lodging. Participants who complete workshop requirements will receive a certificate. Participants who create datasets, code and learning modules to share on these platforms will receive an additional honorarium.


-----

Date: August 4-5, 2025

Place: Purdue University, West Lafayette campus

[Additional Information is available here](https://drive.google.com/file/d/1JP7M6kY_JrQ31mhYj4DSfVSFAJZMcgHF/view?usp=sharing).

-----

# Workshop Schedule(DRAFT)
Day 1

8:30 - 11:30am:
* Welcome and Overview
* Presentation: GeoEDF Workflow Framework, application highlights
* Tutorial: Using and developing custom data connectors and processors
  * (Participants may prototype connectors and processors for their own data sources.)

1:00 - 2:30pm:
* Presentation: StreamCI data management and processing platform, application highlights
* Tutorial: Using StreamCI to ingest, query, and analyze sensor data
  * (Participants are encouraged to bring their own datasets to work with.)

Break (30 minutes)

3:00 - 5:00pm:
* Presentation: Supporting interactive online teaching and learning using CyberFaces; examples
* Tutorial: Creating and publishing interactive learning modules and training materials
  * (Participants can develop or begin designing their own content.)

Day 2

8:30 - 11:30am:
* Presentation: HPC and cloud computing on Anvil and containerization basics
* Parallel working sessions: 
	* Bring your datasets and application ideas
	* Discuss collaboration opportunities
	* Draft post-workshop implementation plan

* Develop use cases and plans for post-workshop implementation, Q&A.

11:30 am - 12:00 pm
* Wrap up and Q&A.
-----

# Eligibility & Application Process
This workshop is open to researchers, faculty and graduate students from U.S. institutions.
To apply, please send:
* Your CV
* A short statement of interest, including but not limited to:
    1. Which theme(s) you are most interested in
    1. How you plan to engage (e.g., bringing your own data, developing resource-intensive data processing and sensor data management pipelines, creating learning materials for use in your own instruction or contributing to the CyberFACES platform)
    1. Any plans for future collaboration or educational use of these tools.

[Submit your application here.](https://bit.ly/cssi4fair) 

Deadline: May 31, 2025.

This workshop is partially supported by National Science Foundation awards #1835822 and #2230092.

## Extracted resources (local files)

### Assessment
*Source file:* `GeoEDF_tutorial_08042025.pdf`  ·  *type:* quiz

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
08/04/2025

Use case: Creating a Greenness Map using NASA dataset
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l

Leaf Area Index (LAI) : Greenness Index 
•
Definition: LAI is the ratio of total leaf area to ground area (dimensionless).
•
Example: LAI = 3 means 3 m² of leaf surface per 1 m² of ground.
•
Ranges:
•
Grasslands: ~0.5–2
•
Forests: ~3–9 (depending on season and canopy type)
•
Unit: No unit (m²/m²)
•
Remote Sensing: LAI is often derived from satellite data (e.g., MODIS, 
Landsat, Sentinel).
•
Weighted Average LAI 
•
Summarizes the region’s vegetation status
•
Retains meaning because it reflects all the sub-pixel variation
•
Is just one number that captures complexity, useful for modeling or 
comparison
https://metergroup.com/education-guides/the-researchers-
complete-guide-to-leaf-area-index-lai/

Overall Greenness of the Upper Wabash River Watershed?
Our interested area
We want to create this weighted LAI map

GeoEDF workflow for use case I 
Connect to 
NASA MODIS 
LAI dataset for a 
specific date
The MCD15A3H dataset: global 4-day 
composite data for Leaf Area Index 
(LAI) and Fraction of 
Photosynthetically Active Radiation 
(FPAR) at a 500-meter resolution
Select the 
interested area, 
and find the LAI 
data channel
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
Output: netCDF file

Step 1: 
Download 
NASA LAI 
dataset 
•
The MCD15A3H dataset, available through the USGS LP DAAC, is a 
MODIS (Moderate Resolution Imaging Spectroradiometer) product 
•
global 4-day composite data for Leaf Area Index (LAI) and Fraction of 
Photosynthetically Active Radiation (FPAR) at a 500-meter resolution. It 
combines data from both the Terra and Aqua MODIS sensors to 
generate a single, best-available pixel value for each 4-day period.
•
Key Details:
•
Product: MODIS/Terra+Aqua Leaf Area Index/FPAR 4-Day L4 
Global 500m
•
Temporal Resolution: 4-day composite
•
Spatial Resolution: 500 meters
•
Variables: LAI, FPAR, quality flags, and standard deviations
•
Data Source: Combined data from 
both MODIS/Terra and MODIS/Aqua satellites
•
Data Access: Available through the LP DAAC Data Pool and NASA 
Earthdata Search
•
Data Format: Typically provided in HDF-EOS format
•
Key Applications: Used for a variety of applications including 
estimating photosynthesis, evapotranspiration, and net primary 
production, as well as understanding terrestrial carbon, water, 
and energy cycles.

$1:
   Input:
         NASAInput:
      url: "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15A3H.061/%{filename}"
      user: "rkalyana"
      password: ""
   Filter:
       Filename:
          PathFilter:
 
 pattern: "%{dtstring}/MCD15A3H.*.h09v07*.hdf"
      dtstring:
          DateTimeFilter:
        pattern: "%Y.%m.%d"
        start: "07/16/2002"
        exact_dates: true
$2:
  HDFEOSShapefileMask:
    hdffile: $1
    shapefile: "/home/jovyan/CI4FAIR/files/watershed/subs1_projected_171936.shp"
    datasets: ["Lai"]

NASAInput Connector Output
If you executed mcd15.yml, you would see the requested nc4 file was downloaded in  
/data/jobid/1/

Step 2: Read 
LAI data for 
the Wabash 
River area, 
and aggregate 
them for each 
subbasin 
• Module for aggregating the data values from an HDF 
file for a given shapefile containing polygons. 
• This supports both HDF4 and HDF5, but assumes 
that the files are in the HDF-EOS format. 
• All processing occurs in the latitude-longitude space 
by reprojecting the shapefile to WGS84 and 
extracting the lat-lon for each grid cell in the HDF file. 
• Extraction of cell lat-lon pairs for HDF4 files relies on 
the eos2dump utility. 
• This supports aggregating more than one subdataset 
from an HDF file.
• The resulting shapefile contains a separate field for 
each subdataset aggregate value

Final Results for 
mcd.yml workflow  
•
The HDFEOSShapefileMask  processor calculated 
weighted LAI for each subbasin (polygon). 
•
A shapefile, a standard vector data format in GIS, stores 
the location, shape, and attributes of geographic features.
•
It's not a single file, but a collection of related files, the 
most important being the .shp, .shx, and .dbf files.
•
The .shp file stores the feature geometry (points, lines, 
polygons).
•
The .shx file contains the index of the geometry. 
•
The .dbf file stores attribute data associated with each 
feature.

GeoEDF workflow for use case II 
Connect to 
NASA MODIS 
LAI dataset for a 
specific date
Select the 
interested area, 
and find the LAI 
data channel
Save weighted 
LAI for each 
subbasin to a 
GeoJSON file
The MCD15A3H dataset: global 4-day 
composite data for Leaf Area Index 
(LAI) and Fraction of 
Photosynthetically Active Radiation 
(FPAR) at a 500-meter resolution
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.

Step 3: Calculate LAI for 
each subbasin and save 
to a GeoJSON file 
• Once you have the shapefile, 
you can visualize the LAI by 
selecting the feature of interest, 
i.e., LAI, and plotting it. 
• If you prefer a text result file that 
has geometry and features, we can 
use another processor, 
Shapefile2GeoJSON. It converts a 
shapefile to a JSON file.

Final result 
of mcd15-
viz.yml 
workflow

Processor Development
• Build a processor using NVIDIA HPC Container Maker 
• TODO

### GeoEDF_Workshop_Flyer-v3 copy
*Source file:* `GeoEDF_Workshop_Flyer-v3 copy.pages`  ·  *type:* file

_[no extractable text]_

## Image text (OCR)

### `ci4fair.jpeg`
Workshop

Cyberinfrastructure
for FAIR Science
