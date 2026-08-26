---
title: "Introduction to Geostationary Satellites and Their Data Analysis & Interpretation Techniques"
unit_id: 229
course_id: 0
level: "Foundation"
slug: introduction-to-geostationary-satellites-and-their-data-analysis--interpretation-techniques
is_course: 0
objectives:
  - "This course is designed for students and researchers who are eager to engage with the practical aspects of geostationary satellite data manipulation using Python. Through comprehensive, hands-on Jupyter notebooks, participants will gain fluency in the tools and techniques essential for the analysis and interpretation of data from specific satellites covered in the course materials."
---

# Introduction to Geostationary Satellites and Their Data Analysis & Interpretation Techniques

**Description:** An introduction to geostationary satellites and their applications is provided. The use of SatPy, a Python library for satellite data processing, is covered. Observations from geostationary satellites such as Himawari and GOES satellites are included for study. The course is designed for those interested in weather and environmental studies.

## Extracted resources (local files)

### Instructions
*Source file:* `Instructions.pdf`  ·  *type:* file

Introduction to Geostationary Satellites and Their Data 
Analysis & Interpretation Techniques 
 
Prepared by  
Mohamed Abdelkader1, Jorge Bravo1, Marouane Temimi1, and Jibin Joseph2  
1Civil, Environmental, and Ocean Engineering Department, Stevens Institute of 
Technology 
2School of Civil Engineering, Purdue University 
mabdelka@stevens.edu 
 
FAIR Science in Climate 
 
 
Objective 
This course is designed for students and researchers who are eager to engage with the practical 
aspects of geostationary satellite data manipulation using Python. Through comprehensive, hands-
on Jupyter notebooks, participants will gain fluency in the tools and techniques essential for the 
analysis and interpretation of data from specific satellites covered in the course materials. 
Overview of steps 
Students are encouraged to utilize the Jupyter notebooks and accompanying PDF solution files to 
navigate the course content step-by-step. These resources are structured to guide learners through 
the process of analyzing data from various geostationary satellites, including Advanced Himawari 
Imager, Advanced Meteorological Imager, and Geostationary Operational Environmental 
Satellite. Each notebook is enriched with comments that not only explain the code but also 
contextualize the data handling techniques applied. This structured approach ensures that students 
not only learn how to execute data analysis tasks but also understand the underlying principles and 
applications of the data they work with. 
Resources 
Part 1: Fundamentals of remote sensing 
Remote Sensing Tutorials 
Part 2: Introduction to Geostationary Satellites 
1. Introduction to Geostationary Satellites: 
o Geostationary Satellites: These satellites orbit the Earth at the same rotational 
speed as the planet, allowing them to remain fixed over a specific geographic

region. They provide continuous monitoring of atmospheric conditions and space 
weather. You can find more information about NASA satellites.  
o Geostationary Orbit: Learn about the unique characteristics of geostationary 
orbits and how these satellites maintain their positions above specific regions on 
Earth. Read more here. 
2. Advanced Himawari Imager (AHI): 
o Overview: The Advanced Himawari Imager (AHI) is part of the Himawari series 
of geostationary satellites. It provides data for better forecasting, improved 
numerical weather prediction accuracy, and enhanced environmental monitoring. 
AHI data is crucial for advanced warning during dangerous weather events.  
o Himawari-8: Himawari-8, equipped with AHI, captures visible light and infrared 
images of the Asia-Pacific region.  
3. Advanced Meteorological Imager (AMI): 
o Geo-Kompsat-2A (GK2A): The GK2A satellite features the new Advanced 
Meteorological Imager (AMI) with significantly higher radiometric, spectral, and 
spatial resolution than its predecessor. AMI provides critical data for weather 
forecasting, climate monitoring, and environmental observation.  
4. Geostationary Operational Environmental Satellites (GOES): 
o Overview: GOES satellites provide advanced imagery and atmospheric 
measurements of Earth’s Western Hemisphere. They offer real-time mapping of 
lightning activity, solar monitoring, and space weather observations. GOES-East 
(formerly GOES-R) and GOES-West (formerly GOES-U) watch over more than 
half the globe.  
o GOES-R Series: The GOES-R Series includes GOES-16 (East) and GOES-17 
(West). These satellites significantly improve detection and observation of 
environmental phenomena affecting public safety, property, and economic health.  
Guide to GOES-R Series Data 
GOES ABI (Advanced Baseline Imager) Realtime Imagery 
GOES Image Viewer 
Instructions 
 
The course is organized around a series of lectures, each corresponding to specific satellite data 
and accompanied by detailed Jupyter notebooks and solution PDFs. Here's how to navigate the 
materials: 
 
• Lecture 1: Advanced Himawari Imager (AHI) Data Analysis 
• Notebook: Introduction to AHI data manipulation. 
• Solution PDF: Detailed step-by-step solutions for AHI data analysis.

o Lecture 2: Advanced Meteorological Imager (AMI) Data Analysis 
o Notebook: Techniques for processing AMI satellite data. 
o Solution PDF: Comprehensive solutions for exercises on AMI data. 
 
 Lecture 3: Geostationary Operational Environmental Satellite (GOES) Data Analysis 
 Notebook: Exploration of GOES satellite data handling. 
 Solution PDF: Step-by-step guide through GOES data analysis tasks.

## Fetched resources (external URLs)

### Beginner’s Guide to GOES-R Series Data (link)
*URL:* https://www.goes-r.gov/downloads/resources/documents/Beginners_Guide_to_GOES-R_Series_Data.pdf

Beginner’s Guide to GOES-R 
Series Data
Version 1.3
How to acquire, analyze, and visualize GOES-R Series data 
Resources compiled by GEO Program Science
Last Updated on September 8, 2025

Document Change Record
Version
Date
Slides Affected
Description
1.0
10/21/2020
All
Initial
1.1
2/8/2021
8, 12, 15-17, 19-21, 
24, 26-29
The following content was added: additional GOES-R imagery 
viewing platforms; AWS “S3 Explorer” user interface for file 
browsing; Geo2Grid software; Python packages (satpy, 
GOES-2-Go, goespy); section on GIS processing (converting 
netCDF files to GeoTIFFs, transforming data to shapefiles).
1.2
5/23/2024
5-9, 12, 14-16, 31-33
Updates include: New figures for GOES-R series satellite and 
GOES satellite constellation; adjustments needed post GOES-
18 designation as GOES-West; updates to multiple links
1.3
9/8/2025
1, 5-9, 12-17, 19-24, 
27, 28, 30-37
Updates to descriptions and figures to reflect GOES-19 as the 
new operational GOES-East; updates to multiple links and 
their descriptions; remove OCC data access description
2

Contents
Part 1: The GOES-R Series
●
Introduction to the GOES-R Series 
5
●
GOES-R Series Instruments
6
●
Advanced Baseline Imager (ABI)
7
●
ABI Mesoscale Domains
8
●
GOES-R Data Products 
9
●
Product Maturity and Data Availability
10
Part 2: Where Can I Access the Data?
●
View GOES-R Imagery
12
●
View GOES-R Imagery with AWIPS
13
●
Access Data Files: NOAA CLASS
14
●
Access Data Files: Amazon, Microsoft
15
●
Access Data Files: Google Cloud
16
●
Use Python to Retrieve Data from AWS
17
Part 3: How Can I Display the Data?
●
Visualize with Command Line: Geo2Grid
19
●
Visualize with Python: Basics 
20
●
Visualize with Python: Custom Packages
21
●
Visualize with Earth Engine
22
●
Technique: Radiance to Reflectance
23
●
Technique: Generating Composites
24
Part 4: How Can I Process the Data Using GIS?
●
Make GOES-R Series Data GIS-compatible
26
●
Convert NetCDF files to GeoTIFFs
27
●
Transform Discrete Data to Shapefiles
28
Part 5: Frequently Asked Questions
●
How are GOES-R Series files formatted?
30
●
How do I pre-process GOES-R Series data?
31
●
How are AB1 L1b products georeferenced?
32
●
Why is data not available on a given date?
33
●
Other Questions and Contact
34
Appendix A: Acronym List
35
Appendix B: Deprecated Script Examples
36
3

Part 1.
The GOES-R Series
4

Introduction to the GOES-R Series
●
Geostationary Operational Environmental Satellites (GOES) are developed, 
launched and operated in a collaborative effort by NOAA and NASA, and 
have been in operation since 1975.
●
The latest generation of geostationary satellites is the GOES-R Series, 
with its first launch in 2016.
●
The GOES-R Series is a four satellite program, which maintains two 
operational satellites at all times, a third standby satellite in “storage 
mode” on-orbit as a ready spare, and the fourth also in “storage mode”.
Figure 1. GOES-R series 
fleet locations as of June 
2025. The geographic 
ranges of GOES-East 
and GOES-West 
together cover the 
North American 
continent. 
Table 1. Status 
summary of each 
GOES-R series 
satellite. 
Satellite
GOES-R (GOES-16)
GOES-S (GOES-17)
GOES-T (GOES-18)
GOES-U (GOES-19)
Launch date
Nov. 19, 2016
Mar. 1, 2018
Mar. 1, 2022
Jun. 25, 2024
Current status
Standby (104.7⁰ W)
Storage (89.5⁰ W)
Operational (137⁰ W)
Operational (75.2⁰ W)
Operational position
GOES-East
GOES-West
GOES-West
GOES-East
Operations start
Dec. 18, 2017
Feb. 12, 2019
Jan. 4, 2023
Apr. 7, 2025
Operations end
Apr. 7, 2025
Jan. 4, 2023
–
–
5

GOES-R Series Instruments
Earth-pointing:
●
Advanced Baseline Imager (ABI) - the primary instrument for imaging Earth’s weather, 
oceans and environment. See Slide 7 for more details. 
●
Geostationary Lightning Mapper (GLM) - a single-channel, near-infrared optical 
transient detector that can identify momentary changes in an optical scene, indicating 
the presence of lightning. 
Sun-pointing:
●
Extreme Ultraviolet and X-ray Irradiance Sensors (EXIS) - monitors solar irradiance in 
the upper atmosphere using two primary sensors: the Extreme Ultraviolet Sensor 
(EUVS) and the X-Ray Sensor (XRS). 
●
Solar Ultraviolet Imager (SUVI) - a  telescope that monitors the sun in the extreme 
ultraviolet wavelength range, detecting solar flares and solar eruptions, and compiling 
full disk solar images.
●
Compact Coronagraph (CCOR) - instrument carried only on GOES-19 that images the 
outer layer of the sun’s atmosphere (corona), helping to detect and characterize 
Coronal Mass Ejections (CMEs).
In-situ:
●
Magnetometer (MAG for GOES-16/GOES-17, GMAG for GOES-18/GOES-19) - measures the space environment magnetic field that 
controls charged particle dynamics in the outer region of the magnetosphere.
●
Space Environment In-Situ Suite (SEISS) - monitors proton, electron, and heavy ion fluxes in the magnetosphere using four sensors: the 
Energetic Heavy Ion Sensor (EHIS), the High and Low Magnetospheric Particle Sensors (MPS-HI and MPS-LO), and the Solar and Galactic 
Proton Sensor (SGPS).
Figure 2. GOES-R Series satellites are composed of 6 
(7 on GOES-19) instruments, and powered by a solar 
panel array. 
6

Advanced Baseline Imager (ABI)
●
ABI is a multi-channel passive imaging radiometer that images Earth’s weather, oceans and environment with 
16 spectral bands (2 visible, 4 near-infrared, and 10 infrared channels). 
○
ABI Bands Technical Summary Chart
●
Spatial resolution is 0.5, 1, or 2 km, depending on the band (see above-linked chart).
●
Geographic coverage 
○
Full Disk: a circular image depicting nearly full coverage of the Western hemisphere (GOES-East/GOES-West). 
○
CONUS/PACUS : a 3,000 (lat) by 5,000 (lon) km rectangular image depicting the Continental US (CONUS) (GOES-East) or 
the Pacific Ocean including Hawaii (PACUS) (GOES-West).
○
Mesoscale: a 1,000 by 1,000 km rectangular image. GOES-East and GOES-West both alternate between two different 
mesoscale geographic regions (domains). See Slide 8 for a complete description of mesoscale domains. 
●
ABI has multiple scan modes. 
○
Mode 6 - The default operational mode for GOES-East & West. Produces a full disk every 10 minutes, a CONUS/PACUS 
image every 5 minutes, and images of both mesoscale domains every 60 seconds.
○
Mode 4 - A contingency mode. Produces only a full disk image every 5 minutes.
○
Mode 3 - The default operational mode for GOES-R satellites until April 2019 when it was replaced by Mode 6.  Produced 
a full disk every 15 minutes, a CONUS image every 5 minutes,  and images of both mesoscale domains every 60 seconds. 
■
A “cooling timeline” version of  Mode 3 was also utilized by GOES-17, starting in February 2020, to mitigate image 
saturation due to the loop heat pipe (LHP) anomaly during the seasons of extra solar heating (late Feb-early April, 
late Aug-early Oct). Mode 3 cooling timeline produces a full disk image every 15 minutes, and images of both 
mesoscale domains every 2 minutes.
7

ABI Mesoscale Domains
●
Mesoscale domains are 1,000 by 1,000 km movable rectangular 
regions. Mesoscale scans frequently revisit an area of interest to 
monitor regional conditions. 
●
GOES-East and GOES-West each have two default domains (see 
Fig. 4), however the domains can be positioned anywhere within 
the full disk upon request.  Requests are placed by National 
Weather Service (NWS) Weather Forecast Offices (WFOs).
○
Figure 3 shows the mesoscale requests by month.
○
Check out the live feed of current mesoscale locations.
●
In Mode 6, the ABI on both GOES-East and GOES-West scans 
either the same mesoscale domain every 30 seconds, or two 
separate mesoscale domains every 60 seconds.
Figure 3. The frequency of mesoscale domain requests varies over time, 
peaking during summer months.
Figure 4a. The 
GOES-East 
default 
mesoscale 
scan sectors 
are the East 
Coast and 
Midwest. 
MESO 1 (East Coast)
MESO 2 (Midwest)
Figure 4b. The 
GOES-West 
default 
mesoscale 
scan sectors 
are the West 
Coast and 
Alaska. 
MESO 1 (West Coast)
MESO 2 (Alaska)
8

GOES-R Data Products
Here is a list of all the GOES-R products made available to the user community by NOAA.
●
Level 0 (L0):
○
L0 products are observation data received directly from the satellite instruments. The data are not easily 
accessible nor meaningful to most users prior to processing by the ground system.
●
Level 1b (L1b): 
○
L1b products are calibrated and, where applicable, geographically-corrected, L0 data. This means that the data 
have been processed so that the values are in standard units of physical quantities.
○
For ABI, the L1b product is radiances. This is useful for users who require radiance units, instead of 
reflectance/brightness temperature (Kelvin) units. 
○
All of the instruments have L1b products distributed except GLM, which is only provided as an L2+ product.
○
For technical information, see the Product User Guide (PUG) Volume 3: L1b Products, found on the OSPO 
GOES-R Documents page.
●
Level 2+ Products:
○
L2+ products contain environmental physical qualities, such as cloud top height or land surface temperature. 
Aside from the GLM Lightning Detection Product, the data source for these products is the ABI L1b data.
○
The mission-critical ABI product is Cloud and Moisture Imagery (CMI), which utilizes all 16 ABI spectral bands, 
and is used to generate an array of products aiding forecasters in monitoring and predicting weather hazards.
○
For technical information, see the PUG Volume 5: L2+ Products, found on the OSPO GOES-R Documents page.
9

Product Maturity and Data Availability
●
Before GOES-R satellites take off, pre-launch verification determines that systems are functioning.
●
However, most instrument, L1b, and L2+ product validation is fully realized after launch with post-
launch product tests that use actual earth, solar, and space observations. Calibration and 
characterization also continue after launch to maintain data product quality. 
●
Product Maturity Levels, summarized:
○
Beta: Data are preliminary and non-operational; undergoing testing and initial calibration and validation. Beta 
products have been minimally validated and may still contain significant errors. 
○
Provisional: Data are ready for operations. Performance has been tested and documented over a subset of 
conditions, locations, and periods. Validation is still ongoing; known anomalies are documented and available 
to the user community.
○
Full: Product is operational. All known anomalies are documented and shared with the user community. 
Performance has been tested and documented over a wide range of conditions. 
●
Data Availability:
○
CLASS and NCEI (see Slide 14) have all data from launch onward available to end-users.
○
Cloud-based platforms (see Slides 15 and 16) typically have only provisional data and onwards available to 
users. However, the length of time of the data archive may vary between vendors.
○
To determine when a particular product advanced to a certain maturity level, explore the Peer/Stakeholder 
Product Validation Reviews.
10

Part 2.
Where Can I Access the Data?
11

View GOES-R Imagery
●
There are a variety of platforms designed for viewing and downloading recent GOES-R images and animated 
image loops, but not for analyzing the data.
●
GOES Image Viewer shows ABI bands, band composites, and GLM data from the past 20 hours.
○
For any active storm, a console describes the weather event and provides a real-time animation.
●
CIRA “RAMMB” Slider provides near real-time ABI bands, composites and some L2+ products, including GLM, 
along with imagery from other satellites (Himawari, Meteosat, JPSS, GEO-KOMPSAT) from the past 7 days.
●
CSSP GeoSphere displays only ABI data, but with a two week rolling archive. Data is processed using the open-
source software Geo2Grid, which can be used by anyone (see Slide 19).
●
NASA Worldview can overlay select ABI data (Channels 2 and 13, Fire Temperature, and Air Mass, Dust, and 
GeoColor composites) from the past 90 days with hundreds of atmospheric, oceanic, and environmental layers.
●
RealEarth is another platform for intercomparison of ABI imagery with various global satellite products. ABI 
imagery is provided in near real-time, but only archived for three days. 
●
NOAA’s Space Weather Prediction Center (SWPC) provides near real-time SUVI and CCOR imagery.
○
SWPC also provides near real-time observations for the other non-imaging GOES-R space weather instruments
●
Other viewing platforms:
○
NASA SPoRT illustrates ABI bands and several composites, but only has a one day archive.
○
SSEC Viewer provides near real time imagery of all ABI channels and a True Color composite.
○
For additional viewing platforms, see the “GOES ABI (Advanced Baseline Imager) Realtime Imagery” web page.
12

View GOES-R Imagery with AWIPS
●
AWIPS (Advanced Weather Interactive Processing System) is the software used by the National 
Weather Service (NWS) to display and analyze meteorological data.
●
Unidata developed and supports a modified non-operational version of AWIPS which is a free and 
open-source software that any user can download to view GOES-R Series data through a similar lens 
as weather forecasting offices (WFOs).
○
CAVE (Common AWIPS Visualization Environment) is a 
Java application which runs on Linux, Mac, and Windows. 
Follow these steps to download CAVE to your device. 
○
AWIPS data can be accessed through the cloud using the 
EDEX Server. When prompted by the Connectivity 
Preferences Dialog, select the EDEX-cloud server.
○
Read Unidata’s CAVE User Manual to learn how to 
interact with and customize the AWIPS tools. See the 
GOES East/West Section for instructions specific to 
GOES-R channels, products, and RGB Composites.
■
For more detail, review the entire user manual, 
with particular attention to Section 2.2.
■
See p.56-63 for image display and time cadence 
options, and p.53-55 for viewing preferences.
Figure 5. The AWIPS display can overlay L2+ products and visible 
imagery, such as Land Surface Temperature and Channel 2.
13

Access Data Files: NOAA CLASS
●
The NOAA Comprehensive Large Array-data Stewardship System (CLASS) repository is the official site 
for accessing all available GOES-R Series Products.
○
Begin by selecting the product of interest from the search bar, such as GOES-R Series ABI Products (GRABIPRD) 
(partially restricted L1b and L2+ Data Products).
○
Use the Temporal and Advanced Search options to filter the data by time, date, satellite, geographic scale, and 
product. It is possible to include up to 10,000 files in an order. Click “Quick Search and Order”, then “Register”.
○
Fill in your contact information to create a Guest User Profile. Once you are logged into CLASS as a guest, the 
option to “Place Order” will appear. If you are a returning CLASS user, log in before beginning your data search.
○
When the order has been processed (up to 48 hours for large order sizes), instructions will be sent to the email 
address provided. The email will offer two options for accessing the file(s):
■
1.  Authenticate and download from CLASS via FTPS. This requires a robust FTP client. Use “anonymous” 
as the FTP user ID, and your email address as the password. 
■
2.  Download each file individually from the CLASS website.
●
A similar but easier website to navigate is NCEI's Archive Information Request System (AIRS).
○
Using the AIRS system, there is no need to set up an account.
○
It is possible to filter, search, and order up to 30 days worth of files, and access up to 1,000 files per order.
○
An email will be sent with download instructions for the processed files, with options for web and FTP downloads.
○
Another interface for downloading NCEI’s archive of GOES-R Series data is NCEI Dataset Search.
14

Access Data Files: Amazon, Microsoft
Amazon Web Service (AWS) - ABI L1b and L2+, GLM L2, and SUVI, SEISS, MAG, and EXIS L1b products 
are available in AWS S3 Buckets. These open datasets can be accessed by the public from AWS for free. 
●
User interfaces for browsing and downloading the available products:
○
The AWS S3 Explorer interface can be used to browse the individual satellite buckets (GOES-16, GOES-17, 
GOES-18, GOES-19).
○
Alternatively, users with AWS accounts can browse the buckets via the AWS S3 Console.
●
Options for scripted/bulk downloading: 
○
AWS Command Line Interface, rclone (see rclone tutorial for GOES data access), and the Python s3fs library
(see Slide 17 for more information on using Python to download data).
●
See the README file under “Documentation” on the AWS page for GOES-specific instructions 
and file naming.
●
ABI L1b Full Disk and CONUS data are being reprocessed and archived in the AWS buckets.
●
A separate AWS S3 Bucket holds CCOR data (GOES-19 only).
Microsoft Planetary Computer - GOES-R Series products are stored in a Azure blob container.  
●
The products currently available are: ABI Cloud & Moisture Imagery,  select ABI L2+ derived 
products, and GLM L2 Lightning Detection which can be accessed from Azure for free.
15

Access Data Files: Google Cloud
●
Google Cloud - ABI L1b and L2+, GLM L2, and SUVI, SEISS, MAG, and EXIS L1b products are 
available in different buckets for GOES-16, GOES-17, GOES-18, and GOES-19. 
○
GOES-R data can be browsed and pulled directly from the Google Cloud website. The data itself is stored in a 
Google Cloud Storage Bucket, while the indexed metadata is available in BigQuery.
○
The buckets can be filtered by product name and date, but be prepared with the product abbreviation and the 
day-of-the-year of interest, because there are few descriptors on the Google Cloud website.
○
Downloading the data requires authentication with a Google account (not Google Cloud specific).
■
Without a Google account, data access is still possible using a Cloud Storage API link.
○
BigQuery offers 1TB of querying per month for free. Additionally, a Google Cloud free trial provides $300 in 
credit, valid for 90 days, which can be used to explore other Google Cloud services.  
■
Follow the “How to process weather satellite data in real-time in BigQuery” tutorial to visualize GOES-R 
data using Google Cloud and the gsutil command-line utility.
●
Google Earth Engine (GEE) - A cloud-based platform for geospatial analysis. This service runs 
through Google Cloud, and pulls GOES-R datasets from the Google Cloud buckets.
○
Only two GOES-R L2+ products are currently available in the GEE Data Catalog:  Multi-band Cloud and 
Moisture Imagery (MCMI) and Fire Detection and Characterization (FDC). 
○
Apply for a free noncommercial GEE account to use this platform. It may take 1-2 days for account approval. 
○
See Slide 22 for more information on how to use GEE as a tool for image analysis and visualization.
16

Use Python to Retrieve Data from AWS
●
The following sample scripts demonstrate two different ways to retrieve GOES-R files from AWS using 
Python. The scripts must be edited to use the correct prefix for the file of interest. 
○
For GOES-R file naming conventions, see the AWS README documentation.
●
Script #1: “Visualize GOES-16 Data from S3” by Hamed Alemohammad
○
This script bypasses downloading data to a local device by pulling data directly from the AWS S3 Bucket, visualizing 
the data, and saving the image as a png. Recommended edits to Script #1 follow, based on a 1/6/21 review:
○
In [2]: Adjust information to reflect the specific satellite/product/date of interest. Be wary that not all products 
have data for multiple bands (if not, remove “band” attribute), or have images for every date.
○
In [5]: Change “M3” to “M6” (mode 3 to mode 6) if the imagery of interest was created after April 2, 2019.
■
This reflects the switch in ABI’s default scan mode. See Slide 7 for more information on scan modes. 
○
In [8]: Change “Rad” to other variable name, if the product of interest is not an ABI L1b Radiance Product.
●
Script #2: “Download GOES AWS” by Brian Blaylock, Ph.D.
○
This simple script demonstrates how to do a scripted download of GOES-R files from AWS using anonymous 
credentials. Files are stored at a local directory. Recommended edits to Script #2 follow, based on a 1/6/21 review:
○
Line 12 : Adjust the bucket name from 's3://noaa-goes16/' to “goes17”, “goes18”, or “goes19” in place of “goes16” 
if applicable. 
○
Line 17 : Correct the prefix from 'noaa-goes17/ABI-L2-MCMIPC/2019/240/00/' to the file of interest.
●
The GOES-2-Go and goespy Python packages can further streamline the download (see Slide 21).
17

Part 3.
How Can I Display the Data?
18

Visualize with Command Line: Geo2Grid
●
The free CSSP Geo2Grid software package is a set of command line tools which 
facilitate the creation of projected satellite images, developed at CIMSS/SSEC.
●
Installation and setup:
○
Install the Geo2Grid software package on a device running Anaconda/Miniconda: 
■
In command line, run: conda create -c conda-forge -n geo2grid 
polar2grid, then conda activate geo2grid
■
Download ABI L1b files of interest, and store in a local directory.
○
Alternatively, use pip to install:
■
Install the PyPI package:  pip install polar2grid
■
Or, clone the git repository and install using:  pip install .
●
Use the ABI L1b Reader to read data, and write to single band GeoTIFF files:
○
geo2grid -r abi_l1b -w geotiff -f <path_to_files> 
●
RGB composites can be be generated by specifying -p [product] (Figure 6):
○
geo2grid -r abi_l1b -w geotiff -p true_color -f <path_to_files>
○
Products: True color*, natural color* air mass, ash, dust, fog, and night microphysics.
○
*These RGBs are ratio-sharpened, enhanced, and an atmospheric correction is applied.
●
Other functions include: remapping data to a different projection, subsetting data to a geographic bounding 
box, and setting the file output format to a png.
●
For more information, see Geo2Grid Basics and Examples for Working with ABI Data.  
Figure 6. GeoTIFFs created using 
Geo2Grid. 6a (top): GOES-16 CONUS 
true color. 6b (bottom): GOES-17 
PACUS natural color.
19

Visualize with Python: Basics
●
Import data to Python directly from AWS (see Slide 17 and Slide 19 for examples), or 
from a local directory.
●
Visualize GOES-R imagery using Python packages: xarray and matplotlib.
○
Xarray processes GOES-R data as multidimensional arrays. Matplotlib plots data to generate 
images with legends. Figure 7a adapted from Script #1 output.
●
Georeference GOES-R imagery using Cartopy package.
○
Cartopy helps georeference data, so that geographic features like state borders can be 
overlaid. Cartopy should be used instead of Basemap, a package that is now deprecated.
○
Script #3: “Mapping GOES-16 True Color” by Brian Blaylock, Ph.D. A step by step explanation 
for how to render and georeference a GOES-16 ABI true color image. Figure 7b created by 
following this script. Recommended edits to Script #3 follow, based on a 6/27/25 review:
■
Under “Open the GOES-16 NetCDF File”, “Overlay Nighttime IR when dark”, “Can we make 
plots for a Mesoscale scan?”, and “Can we do this for a Full Disk Scan? It's possible…” sections, 
the linked files are no longer accessible. Instead, download files locally (e.g., from AWS) and 
reference those in the FILE line.
■
Under “Using other projections”, “Plot with Cartopy: Plate Carrée Cylindrical Projection”, and 
“Can we make plots for a Mesoscale scan?” sections, the ax.imshow extent lines need to 
reference the x and y values. Replace the extent lines with extent=(x.values.min(), 
x.values.max(), y.values.min(), y.values.max()).
●
Script #4: “Accessing GOES data with the Planetary Computer STAC API.”
○
A script with code instructing how to access ABI data from blob storage on Azure.
Figure 7. GOES-16 visualized with 
Python. 7a (top) ABI L1b Channel 2 
Full Disk Radiances from Jan 5th, 
2021. 7b (bottom): True Color 
CONUS from June 4th, 2020.
20

Visualize with Python: Custom Packages
●
The prior Python examples employ widely-used packages for processing any environmental data. 
However, by using more specialized Python packages, it is possible to process and visualize GOES-R 
imagery with fewer lines of code. Follow the respective installation guides and documentation. 
●
Satpy - a Python package for reading, writing and manipulating satellite imagery by the PyTroll Team.
○Satpy processes GOES-R data using specialized readers: abi_l1b, abi_l2_nc, and glm_l2. Satpy’s capabilities include 
generating composites, extracting measured values, resampling to a uniform grid, slicing and subsetting scenes. 
○See Satpy’s “Quickstart” webpage for an overview, and “Reading Data with the Scene” for an ABI L1b example.
○Script #5: “GOES-16 Mosaic”- Pull files from AWS, or load local files, then join all 16 bands with ImageMagick.
○Script #6: “GOES-16 ABI - True Color Animation” - Combine single ABI timesteps to create an mp4 video file.
●
GOES-2-go - a Python package created by Brian Blaylock, Ph.D. 
○Downloads and reads ABI and GLM data from AWS. A user may retrieve the 
latest GOES-R data, select images from a specific time and date, or choose a 
series of images from a date range.
○Creates multispectral RGB composites, based on recipes from RAMMB/CIRA, such as True Color, 
Natural Color, Air Mass, and Day Cloud Phase Distinction. See Script #7: “Demo RGB Recipes”.
●
goespy - a Python package created by Steven Pestana and Paulo Alexandre Mello.
○Simplifies downloading from AWS with two functions: ABI_Downloader and GLM_Downloader.
○Script #8: “Downloading and plotting GOES-R imagery with goespy and xarray” - Demonstrates 
goespy utility.
Script #6 changes 
based on a 7/11/25 
review - in the first 
cell: 
Add demo to the 
satpy imports:  
from satpy 
import Scene, 
demo
Adjust the  
BASE_DIR path to a 
local directory, then 
add the line
satpy.demo.abi_
l1b.get_hurrica
ne_florence_abi
(base_dir=BASE_
DIR)
Script #7 changes based on a 7/11/25 
review: 
When calling G = GOES().latest(), 
specify a currently operational satellite, 
e.g., G = 
GOES(satellite=19).latest()
When calling the nearesttime
function, change the format to 
GOES(satellite=16, 
domain="F").nearesttime("2021
-01-01 18:00")
Comment out any functions from 
“Carpenter_Workshop”
21

Visualize with Earth Engine
●
Google Earth Engine (GEE) is a cloud-based platform for 
geospatial data analysis. The following list summarizes the 
advantages of imagery processing using GEE:
○
The GOES-R imagery stored in the GEE Data Catalog is already 
georeferenced. Therefore, it only requires a few lines of script 
to display an image accurately (Figure 8).
○
GEE provides advanced image processing tools designed for 
satellite imagery analysis, offered through several APIs.
○
The GEE Data Catalog stores many datasets, including imagery 
from MODIS, Landsat, and Sentinel, which are updated daily. 
Synthesizing dissimilar satellite products is possible in GEE. 
○
GEE takes advantage of Google’s infrastructure to execute 
high speed parallel processing. This is helpful for handling large 
collections of images, without using local computing resources.
○
For an introduction to GEE, check out the GEE Community Tutorials. 
●
Be aware of the following:  
○
To use this platform, it is necessary to apply for a free GEE account, which may take a day or two to get approved. 
○
Two GOES-R L2+ products are currently available in the GEE Data Catalog:  Multi-band Cloud and Moisture Imagery 
(MCMI) and Fire Detection and Characterization (FDC). Sample scripts are available in the dataset descriptions.
Figure 8. GOES-16 CONUS False Color image on June 
12th, 2020, visualized using GEE.
22

Technique: Radiance to Reflectance
●
When using the ABI L1b Radiance product, it may be beneficial to convert from the unit radiance, 
which takes into account the solar irradiance and Earth-Sun distance. For the reflective bands (1-6), 
convert to reflectance. For the emissive bands (7-16), convert to brightness temperature (Kelvin). 
●
Reflectance conversion equation: reflectance ρ𝑓𝑓v = kappa factor κ *  radiance Lv
○
The kappa factor is included in the metadata for every L1b file, stored as the variable 'kappa0'
○
For more information on the reflectance conversion, or how to convert to brightness temperature, see the 
PUG Volume 3: L1b Products, found on the OSPO GOES-R Documents page (Revision 2.3, pages 27-28).
●
Script #9: “True-Color Image: GOES-R ABI L1b Radiances” by Danielle Losos. 
○
This Jupyter Notebook demonstrates several useful techniques for processing and visualizing the L1b 
Radiance product to create a georeferenced RGB True-Color image.
○
Compare to the Script #3 methodology for creating true color images from the L2+ MCMI product.
■
See Slide 24 for background on using multiple bands to generate true-color composite images. 
○
Alternative approach for converting radiance to reflectance values is documented in the tutorial: 
“Jupyter Notebook for Working with GOES-16 Data” by Opens Commons Consortium (OCC). 
However, this script errs in using constant values to convert between radiance and reflectance. It is 
recommended to always use the coefficients embedded in that particular image’s metadata for 
conversion to reflectance or brightness temperature.
■
A section of the OCC script shows how to visualize Geostationary Lightning Mapper (GLM) 
point data.
Script #9 changes based on a 
7/1/25 review: 
To avoid an error in cell 
In [15] add the following: 
import warnings
np.warnings = warnings
23

Technique: Generating Composites
●
"Band stacking" is the process of overlaying certain bands to create composite imagery. Read “Satellite 
imagery RGB: Adding Value, Saving Time” for background on how composites aid weather forecasting.
●
A popular composite image type is an RGB True Color, which uses red, green, and blue wavelength 
imagery to mimic the appearance of the Earth to the human eye.
○
ABI has blue and red visible channels (bands 1 and 2), but not a green visible channel. The near infrared (NIR) 
channel (band 3) can serve as a proxy for the green band. Script #3 shows how to create an RGB True Color image 
from bands 1, 2, and 3 of the MCMI product. MCMI is a single file with all 16 bands resampled to 2 km resolution. 
○
Using three separate CMI files for the three bands is less data intensive and achieves a higher resolution. 
However, band 2 has 0.5 km resolution while bands 1 and 3 have 1 km resolution, which makes multi-band 
operations difficult. Thus, it is necessary to resample band 2. Script #9 demonstrates how to resample using a 
Rebin function. 
●
Other ABI RGB composites do not simulate true color, but instead highlight various atmospheric and 
surface features, such as the Air Mass RGB, Day Cloud Phase Distinction RGB, and Dust RGB. 
○
Satpy and GOES-2-Go packages automate the generation of common ABI composites.
●
Another common composite is NDVI (normalized difference vegetation index). This index determines 
vegetative health by finding a the difference between a pixel’s reflectance in red and NIR wavelengths.
■
Script #10: Shows how to easily calculate NDVI of a Landsat image in Python using the module Earthpy. 
To calculate NDVI using ABI, substitute band 2 as the red band and band 3 as the NIR band. 
24

Part 4.
How Can I Process the Data 
Using GIS?
25

Make GOES-R Series Data GIS-compatible
●
The native format for GOES-R products is netCDF files (see Slide 30) which are not always compatible 
with GIS. To process products using GIS software, it may be necessary to change the data format.
●
Raster and vector models are the two primary ways to represent geospatial data for visualization in GIS.
○
Raster Models: grids of rectangular pixels, with each pixel assigned a value that corresponds 
to the measured environmental feature. To learn more, read “What is raster data?”.
■
Since GOES-R netCDF files store variables in multidimensional arrays, most products 
can be converted easily to raster file formats (Slide 27).
■
Over a hundred raster file types are supported by the open-source platform QGIS. 
Common formats for storing satellite imagery include TIFF, IMG, GRID, JPEG, JP2, 
BMP, GIF, PNG, BIL/BIP/BSQ, and DAT.
○
Vector Models: points, lines, or polygons used to explicitly delineate the boundaries of 
environmental features. Each geometry (a point/line/polygon) may have associated attributes 
which describe the characteristics of the feature. For more information, read “Vector Data”. 
■
GOES-R netCDF multidimensional arrays cannot be modeled by vectors without 
transforming the data.
■
Shapefiles are the most widely used vector format and are compatible with any GIS 
platform. Other file formats for storing vector data include GeoJSON, KML/KMZ, 
TIN, and DXF. 
Figure 9. This graphic shows how
point/line/polygon vectors and raster 
grids model surfaces differently. 
Source:
Saylor Academy 
26

Convert NetCDF files to GeoTIFFs 
●
NetCDF files are compatible with select GIS platforms. QGIS Version 3.2+ can handle some GOES-R 
products. Within QGIS, go to Add Layer > Add Raster Layer, then select a variable when prompted.
●
GeoTIFFs are regarded as the industry standard for georeferenced raster data.
The conversion of GOES-R netCDF arrays to single-band GeoTIFF rasters can 
be accomplished in command line, using GDAL or Geo2Grid (see Slide 19). 
○
Install the package Geospatial Data Abstraction Library (GDAL). Use the command
gdal_translate NETCDF:"Input_file.nc":Variable_name Output_file.tif
○
For example: gdal_translate NETCDF:"OR_ABI-L1b-RadC-M6C01_G16_s2021 
0010016176_e20210010018549_c20210010019000.nc":Rad Sample_Output.tif
●
The collection of scripts, “GOES-R NetCDF to GeoTIFFs” by Danielle Losos, 
can assist with batch retrieval and conversion. These scripts automate the file 
download by pulling data from a given satellite, product, and date from AWS.
○
Script #11: “L1b Channel Loop” – Loops through the 16 netCDF files 
contained in an ABI L1b Radiance product, and converts each to a GeoTIFF.
○
Script #12: “L2 Products” – Visualizes and converts the chosen GOES-R L2+ 
ABI product variable, e.g., Cloud Top Height, from a netCDF file to a GeoTIFF.
○
Script #13: “Clip with Shapefile” – Clips a netCDF file image to a shapefile 
boundary, and saves the region of interest as a GeoTiff (Fig. 10). 
Figure 10. 
GOES-16 L2+ 
CMI clipped to 
the Minnesota 
border, 
converted to a 
GeoTIFF, and 
visualized in 
QGIS using 
Script #13.
Script #12 changes based on a 
7/3/25 review: In cell In [9] -
change xr.open_rasterio to 
rioxarray.open_rasterio, 
add tiled="NO" argument to 
netCDF_file.rio.to_raster
Script #13 changes based on a 
7/3/25 review: In cell In [15]
- change xr.open_rasterio
to 
rioxarray.open_rasterio, 
change netCDF_file.crs to 
netCDF_file.rio.crs
27

Transform Discrete Data to Shapefiles 
●
Discrete data, also known as thematic or categorical data, is used to represent features that have 
defined boundaries. Vector models are better suited for discrete than continuous variables. 
○
Several ABI L2+ products have discrete variables, including the Clear Sky Mask which provides a binary 
classification for each pixel: “clear” or “cloudy”; Aerosol Detection; and Cloud Top Phase.
○
Most GOES-R products have a Data Quality Flag (DQF) layer, a discrete variable which classifies each pixel’s usability 
into categories like “good quality”, “conditionally usable”, or “out of range”.
●
Script #14: “Discrete variable to shapefile” by Danielle Losos.
○
This script transforms ABI products to shapefiles by polygonizing gridded data. A vector polygon is created for each 
connected region of pixels in the array sharing  a common value.  
○
For example, the Clear Sky Mask 
can be polygonized to a vector 
layer where each polygon has an 
attribute equal to 0 for cloud-free 
or 1 for cloud-covered (Fig. 11).
Figure 11. Clear Sky Mask vector layer 
(left image) is used to mask an RGB-false 
color raster in QGIS (right image).
Script #14 changes based on a 7/3/25 review: 
In the first cell, add import rioxarray
In cell In [9] -
change xr.open_rasterio to rioxarray.open_rasterio, 
change netCDF_file.crs to netCDF_file.rio.crs, 
change Projection.ImportFromProj4(goesR_crs) to 
Projection.ImportFromProj4(goesR_crs.to_proj4())
28

Part 5.
Frequently Asked Questions
29

How are GOES-R Series files formatted?
●
GOES-R Series product files use the netCDF-4 format, a general-purpose scientific data file format. 
●
More details on netCDF files:
○
GOES-R Series products may have any of the following types of attributes
■
title : a global attribute that is a character array providing a succinct description of what is in the dataset. 
■
Conventions : a global attribute that is a character array for the name of the conventions followed by the product.
■
long_name : long descriptive name for each variable. 
■
_FillValue : a scalar value that identifies missing data. 
■
Valid_range : a delimited vector of two numbers specifying the minimum and maximum valid values for the variable to which it is attached.
■
scale_factor and add_offset : these attributes are used together to provide simple data compression to store floating-point data as small 
integers in a product data file.
■
units : a character string that specifies the units used for the variable’s data.
○
A netCDF file also includes the dimensions that are used to size dimensional variables.
○
For a quick look at the contents of a netCDF file, use the ncdump command line tool from Unidata’s netCDF package.
○
The netCDF ABI L1b/L2+ gridded product files are compressed to reduce the file size. For information on how to unpack data, see 
Slide 31. For more details on netCDF files, refer to the PUG Volume 1: Main, found on the OSPO GOES-R Documents page (Revision 
2.3, pages 8-14).
●
Other file formats:
○
Flexible Image Transport System (FITS) format is used alongside netCDF for the SUVI Solar EUV Imagery product.
○
FITs is the primary format used for the CCOR data products, with their auxiliary files in netCDF format.
○
Unix text file format is used in a small subset of the Level 1b and 2+ semi-static source data files.
○
Hierarchical Data Format (HDF)  is used for several Level 1b semi-static source data files.
30

How do I pre-process GOES-R Series data?
●
GOES-R Series data are packed in compressed files, which must be “unpacked” for integer analysis. 
Images can be visualized without unpacking, since scaled integers are still proportional to each other.
●
What is packed data?
○
In order to minimize file size, many of the ABI L1b/L2+ products use 16-bit scaled integers for physical data 
quantities rather than 32-bit floating point values. 
○
To convert data back to the actual value associated with the physical quantity, the user must multiply by a scale 
factor and add an offset to the 16-bit scaled integer.
●
How do I unpack data?
○
To unpack the data, apply the attributes using the following equation: 
unpacked_value = packed_value * scale_factor + add_offset
○
The variables ‘scale_factor’ and ‘add_offset’ are included in the metadata for each file. The scale factor is calculated 
with the formula (Max Value - Min Value)/65530, and the offset is the product’s expected minimum value.
○
Here is a sample conversion for band 8: Brightness temperature(Kelvin) = (2,305 * 0.04225) + 138.05 = 235.44 K
○
Before unpacking, check to ensure that the program in use is not automatically applying the scale factor and offset.
●
How do I remove data that is fill, out of range, or missing, from the image? 
○
These faulty data types can be masked using data quality flags (DQFs), convention attributes which associate 
integer values with a categorization of the data quality. 
○
For more information on packed data or DQFs, see the PUG Volume 1: Main, found on the OSPO GOES-R 
Documents page (Revision 2.3, pages 21 or 16, respectively).
31

How are ABI L1b products georeferenced?
●
ABI uses a fixed grid whose native coordinate values are the 
East/West scanning angle and North/South elevation angle in units of 
radians relative to the location of the satellite.
○
The ABI fixed grid is a projection based on the viewing perspective of the 
idealized location of a satellite in geosynchronous orbit. This allows the 
same data points in every product to be at the same location on Earth.
○
The fixed grid is rectified to an ellipsoid defined by the Geodetic Reference 
System 1980 (GRS80) earth model.
○
For all ABI gridded L1b/L2+ products, the names of the coordinate variables 
are x (E/W scanning angle) and y (N/S elevation angle) (Figure 13).
○
Additionally, there is a “grid_mapping” attribute which is attached to data 
variables whose values are associated with specific earth locations.
○
For ABI L1b/L2+ gridded products, the grid mapping attribute specifies the 
projection (GRS80), the lat/lon origin of the projection, and a parameter that 
identifies the ABI scanning pattern.
●
Grid mappings coupled with the coordinate variables provide the 
means to determine the latitude and longitude of a data point.
○
See the PUG Volume 3: L1b Products, found on the OSPO GOES-R 
Documents page (Revision 2.3, pages 8-26), for an in-depth explanation.  
Figure 13. Every data point is plotted on the 
ABI fixed grid as a distance from the (0,0) origin, 
in units x (East to West Scanning Angle) and y 
(North to South Elevation Angle).
32

Why are data not available on a given date?
●
Cloud-based platforms have select L2+ Product availability.
○
Once a GOES-R Series product has reached provisional maturity status, cloud-based platforms may release the product. 
○
When there is demonstrated user interest in a product, vendors may backfill their archive to include the dates requested. 
This may include beta maturity levels of the product.
○
If there is no demonstrated user interest in the product, vendors may choose not to release the entire available 
collection. For this reason, collection length may vary between products on cloud-based platforms. 
●
To retrieve pre-provisional GOES-R Series products, search on NOAA CLASS to access the entire archive of 
products made available to users. CLASS stores products with beta, provisional, and full maturity status. 
●
Occasionally, there is missing GOES-R Series data on select dates and times.
○
To investigate whether data is missing due to issues with data reception, check out the SSEC’s Monitoring Web Page. 
Follow these instructions for tips on how to navigate this website:
1. First, select the GOES-R Series satellite of interest, then choose a date of interest at the top of the page.
2. Each row represents the data quality of full disk, CONUS, and mesoscale images for every hour of the day.
3. The “DB: SSEC” section reports missing data due to GOES Rebroadcast (GRB) reception issues. 
KEY- light green: 100% received, yellow: 96 -100% received, light red: < 96% received, dark red: missing
4. The “PDA via STAR” section reports missing data due to errors with Product Distribution and Access (PDA).
KEY (same as above with two more categories) - blue & orange: data available from PDA but missing or late 
○
Also, check out OSPO’s Satellite Alert Messages to see if there were any outages reported on that day
33

Other Questions and Contact
Other Questions
●
For unanswered questions, try browsing the GOES-R Series FAQ Page or NCEI’s GOES-R Series Page.
●
Additional resources are available on the Office of Satellite and Product Operations (OSPO) GOES-R 
documents page, including links to the most recent Product User’s Guides (Volumes 1-5) and the 
Product Algorithm Theoretical Basis Documents (ATBDs). The GOES-R Series Documents page also 
contains links to many helpful GOES-R documents.
●
Useful links for background information: Mission Overview, GOES History, GOES-R Data Book 
(technical overview of satellite and ground systems)
Contact
●
Get in touch by emailing the Satellite Products and Services Division (SPSD) User Services at  
SPSD.UserServices@noaa.gov. Please share your questions, concerns, or suggestions for how this 
GOES-R beginner’s guide could be more helpful.
●
Show us how you are using GOES-R data in your own work by using #goesrguide when you post on 
social media!
34

Appendix A: Acronym List
ABI - Advanced Baseline Imager
AIRS - Archive Information Request System 
ATBD - Algorithm Theoretical Basis Documents 
AWIPS - Advanced Weather Interactive  Processing 
System
AWS - Amazon Web Service
CAVE - Common AWIPS Visualization Environment
CCOR - Compact Coronagraph
CIMSS - Cooperative Institute for Meteorological 
Satellite Studies
CIRA - Cooperative Institute for Research in the 
Atmosphere 
CLASS - Comprehensive Large Array-data 
Stewardship System
CMI - Cloud and Moisture Imagery 
CONUS - Continental U.S. 
CSSP - Community Satellite Processing Package
DQF - Data Quality Flag
EHIS - Energetic Heavy Ion Sensor 
EUVS - Extreme Ultraviolet Sensor
EXIS - Extreme Ultraviolet and X-ray Irradiance 
Sensors
FDC - Fire Detection and Characterization 
FITS - Flexible Image Transport System  
FTP - File Transfer Protocol
GDAL - Geospatial Data Abstraction Library 
GEE - Google Earth Engine
GIS - Geographic Information System
GLM - Geostationary Lightning Mapper
GOES - Geostationary Operational Environmental 
Satellite
GRB - GOES Rebroadcast
GRS80 - Geodetic Reference System 1980
HDF - Hierarchical Data Format
L0/L1b/L2+ - Level 0/ Level 1b/ Level 2+
MAG - Magnetometer
MCMI - Multi-band Cloud and Moisture Imagery 
MESO 1/2 - Mesoscale Domain Sector 1/2
MPS-HI/LO - Magnetospheric Particle Sensor -
High/Low
NASA - National Aeronautics and Space 
Administration
NCEI - National Centers for Environmental 
Information
NDVI - Normalized Difference Vegetation Index
NetCDF - Network Common Data Format
NIR - Near-infrared 
NOAA - National Oceanic and Atmospheric 
Administration
NWS - National Weather Service 
OCC - Opens Commons Consortium 
OSPO - Office of Satellite and Product Operations
PACUS - Pacific U.S. 
PDA - Product Distribution and Access
PUG - Product User Guide
RAMMB - Regional and Mesoscale Meteorology 
Branch 
RGB - Red-Green-Blue 
SEISS - Space Environment In-Situ Suite 
SGPS - Solar and Galactic Proton Sensor 
SPoRT - Short-term Prediction Research and 
Transition Center
SPSD - Satellite Products and Services Division
SSEC - Space Science and Engineering Center
SUVI - Solar Ultraviolet Imager 
SWPC - Space Weather Prediction Center
WFO - Weather Forecast Office
Additional acronyms defined on the 
GOES-R  Series Acronym Page
35

Appendix B: Deprecated Script Examples
●
Slides in this appendix were included in a previous version of the GOES-R Beginner’s Guide, but 
the script examples include older Python functions that are now deprecated
●
We are continuing to include these older slides in case the functional parts of the scripts provide 
enough information for a user to start using it and possibly find a workaround on their own
36

Transform Continuous Data to Shapefiles 
●
Continuous data represents variables that change progressively across surfaces. Most GOES-R 
products contain continuous variables, like radiance, reflectance, temperature, or pressure.
○
Continuous variables are not modeled well by vector data. Transforming satellite imagery to vectors requires 
generalization of data into categories (i.e., discrete intervals) which results in a loss of detail and accuracy.
○
However, certain geospatial analytic operations can only be performed on vector data. 
●
Script #B-1: “Continuous variable to contour to shapefile” by Danielle Losos.
○
This script converts ABI products to shapefiles by first transforming the continuous variable into a contour plot 
of n discrete intervals. Next, the concentric rings of the contour plot are converted into shapefile polygons. 
○
As the number of contour intervals, n, increases, the accuracy of the vector model improves (Figure B-1). The 
trade off for a higher n is a longer processing time and ultimately a larger file size.
Script #B-1 changes: 
Perform similar 
changes as described in 
the Script #14 changes
The actual shapefile 
creation in cells IN 
10-12 include 
deprecated functions, 
and the direct 
replacements produce 
unrealistic results
Figure B-1. GOES-
16 CONUS L2+ 
Land Surface 
Temperature 
visualized as a 
contour plot with 
5, 15, and 50 
discrete intervals.
n = 5
n = 
15
n = 
50
37

### JN-File (link)
*URL:* https://github.com/MAbdelkader94/Introduction-to-Geostationary-Satellites/blob/main/Lecture_01_AHI.ipynb

## SatPy - Part 1: Exploring Advanced Himawari Imager (AHI) data

For detailed documentation, visit [SatPy Documentation](https://satpy.readthedocs.io/en/latest/index.html).

SatPy is a powerful library for **reading**, **manipulating**, and **displaying** data from remote sensors, primarily related to meteorology. It also provides the capability to **save** this data as images or in various formats.

SatPy excels at generating images with **individual channels or bands** and creating **RGB composites** directly from satellite instrument data.

The pyresample library is used for **resampling data** in different areas with specific projections or uniform grids.

Additionally, Satpy offers various **atmospheric corrections** and **visual enhancements**, either directly within Satpy or through the PySpectral and TrollImage packages.

# Advanced Himawari Imager (AHI) data
https://www.earthdata.nasa.gov/sensors/ahi

```python
urls2dwn = ['https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B01_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B02_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B03_JP01_R05_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B04_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B05_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B06_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B07_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B08_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B09_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B10_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B11_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B12_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B13_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B14_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B15_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B16_JP01_R20_S0101.DAT.bz2']
```

```python
import requests
import os

# Specify the local directory where you want to save the files.
local_directory = "Output_data"
# Ensure that the local directory exists; create it if it doesn't.
## Your code goes here:

#######################

# Iterate through the URLs and download files.
for urld in urls2dwn:
    # Extract the filename from the URL.
    ntw = urld.split('/')[-1]
    
    # Construct the complete path to save the file in the local directory.
    file_path = os.path.join(local_directory, ntw)
    
    # Send an HTTP GET request to the URL.
    resp = requests.get(urld)
    
    # Check if the response is successful (status code 200).
    if resp.status_code == 200:
        # Write the content to the file in binary mode.
        with open(file_path, "wb") as file:
            file.write(resp.content)
        print(f"File '{ntw}' downloaded and saved to '{local_directory}'.")
    else:
        print(f"Failed to download '{ntw}' from the URL: {urld}")

```

## Loading and Visualizing Satellite Data

# SatPy is well-suited for working with geostationary satellite data, such as GOES-R or Himawari:

```python
# Importing the warnings module and setting it to ignore all warnings.
# This is useful to prevent unnecessary warning messages from cluttering the notebook output.

## Your code goes here:

#######################
```

```python
# Importing Scene from the satpy module. Scene is used to represent satellite data 
# and allows for operations like reading, resampling, compositing, and saving data.
## Your code goes here:

#######################


# Importing find_files_and_readers from satpy. This function is used to automatically
# locate satellite data files and determine the appropriate reader based on the 
# metadata and contents of the files.
## Your code goes here:

#######################
```

This line imports the debug_on function from the satpy.utils module, which is used to enable detailed debug logging in Satpy. This can be helpful for troubleshooting and understanding the internal workings of Satpy processes.

```python
## Your code goes here:

#######################
```

## Searching for Native MSG Data

```python
 # Importing datetime for date and time operations
## Your code goes here:

#######################
```

```python
fMSGn = find_files_and_readers(start_time = datetime(2024,3,2,16,0),  # Set start time for file search
                            #end_time = datetime(2019,7,22,12,59),   # Optional: Set end time for file search
                            base_dir = 'Output_data',  # Set the base directory for the search
                            reader = 'ahi_hsd')  # Specify the file reader
## Your code goes here:
        # Display the found files
```

```python
## Your code goes here:
            # Import the glob module to find files using pattern matching
```

```python
## Your code goes here:

#######################

# List all files matching the specified pattern in the directory, useful for handling multiple files

# scn = Scene(reader = 'seviri_l1b_native', filenames = fnames)  # Create a Scene object using the SEVIRI L1B native reader with the specified filenames
```

> **SatPy** always expects the original file names!

So, do not change them when saving the data on your local machine. Otherwise, SatPy will not be able to open the files.

```python
# Creating a Scene object using the file information gathered by find_files_and_readers function
## Your code goes here:

#######################

```

```python
# Accessing the attributes of the Scene object to retrieve metadata and other information
## Your code goes here:

#######################

```

```python
# Creating a Scene object from the filenames specified in fMSGn
## Your code goes here:

#######################
```

```python
# Accessing the attributes of the Scene object to view metadata information
## Your code goes here:

#######################
```

```python
# Retrieve and print all available dataset names in the scene
## Your code goes here:



#######################
```

The `scn.load(['IR_108'], upper_right_corner='NE')` line in ther code bellow is used for loading a specific dataset from a satellite scene in Satpy. Let's break down what each part does:

1. `scn`: This is your Satpy `Scene` object, which contains data from satellite files that you've previously loaded.

2. `.load()`: This method is used to load specific datasets from the satellite files into memory, making them ready for processing and analysis.

3. `['IR_108']`: This is a list containing the names of the datasets you want to load. In this case, you're loading the dataset named `IR_108`, which typically refers to infrared imagery at a wavelength of 10.8 micrometers. This wavelength is often used for cloud imaging, among other applications.

4. `upper_right_corner='NE'`: This parameter specifies how the data should be oriented when loaded. `NE` means that the upper right corner of the data should be in the northeast. This can be important for getting the geographical orientation correct, especially when dealing with global or hemispherical datasets.

After running this line, the `IR_108` dataset will be loaded into your scene and ready for further processing, such as visualization or analysis.

```python
## Your code goes here:


#######################
```

The scn.keys() method in Satpy is used to retrieve a list of all the dataset keys available in the currently loaded Scene object.

```python
## Your code goes here:


#######################
```

```python
# Show the 'IR_108' dataset using Satpy's built-in visualization capabilities
## Your code goes here:


#######################
```

```python
%matplotlib inline
# Plot the 'IR_108' channel using matplotlib's imshow function
## Your code goes here:


#######################
```

```python
# Import the matplotlib library for creating visualizations in Python
## Your code goes here:


#######################
```

```python
# Create a figure and an axes object with specified figure size
## Your code goes here:

#######################

# Display the data from the 'IR_108' channel of the satellite scene using a grayscale color map
## Your code goes here:

#######################

# Hide the axis labels and ticks to focus on the image only
## Your code goes here:

#######################

# Add a colorbar to the plot with a fraction size of the plot, useful for scale/reference
## Your code goes here:

#######################

# Display the figure with all its components
## Your code goes here:

#######################
```

```python
# Accessing the 'IR_108' dataset from the Scene object 'scn'
# - 'scn' is a Scene object, used for handling satellite data.
# - 'IR_108' specifies an infrared channel at 10.8 micrometers.
# This dataset is used for cloud imaging, surface temperature, and atmospheric analysis in meteorology.
## Your code goes here:

#######################
```

# Radiance Calibration

```python
# Load the data for the 10.8μm band.
# The parameter [10.8] specifies the wavelength of the band in micrometers.
scn.load([10.3], 

         # Specify the calibration to radiance values.
         # "radiance" calibration converts the data to radiometric units (mW m-2 sr-1 (cm-1)-1).
         ## Your code goes here:
         calibration=, 

         # Set the orientation of the image.
         # "upper_right_corner='NE'" aligns the image with its upper right corner to the northeast.
         upper_right_corner='NE')
```

# Brightness Temperature Calibration

```python
# Load the data for the 10.8μm band again, this time for a different calibration.
scn.load([10.3], 

         # Specify the calibration to brightness temperatures.
         # "brightness_temperature" calibration converts the data to temperature units (Kelvin).
         ## Your code goes here:

         calibration=, 

         # Maintain the same orientation as before.
         upper_right_corner='NE')
```

```python
# List all the datasets currently loaded into the Scene object 'scn'
## Your code goes here:



#######################
```

```python
# Convert the keys view to a list to enable indexing
## Your code goes here:

#######################


# Access the second dataset key
## Your code goes here:

#######################

# Extract the central wavelength from the 'wavelength' attribute of the second dataset key
## Your code goes here:

#######################

# Print the central wavelength and the key for the second dataset
## Your code goes here:


#######################
```

```python
# Create a figure and two subplot axes, arranged horizontally, with specified size
## Your code goes here:


#######################

# Display the values of the second dataset in the Scene on the first subplot (ax1) using a grayscale color map
im1 = ax1.imshow(scn[scn.keys()[1]].values, cmap="Greys")
# Remove the axis labels and ticks for ax1
ax1.set_axis_off()

# Display the values of the first dataset in the Scene on the second subplot (ax2) using a grayscale color map
im2 = ax2.imshow(scn[scn.keys()[0]].values, cmap="Greys")
# Remove the axis labels and ticks for ax2
ax2.set_axis_off()

# Set the title for ax2
ax2.set_title("10.8μm Brightness temperature")
# Set the title for ax1
ax1.set_title("10.8μm Radiance")

# Add a colorbar next to ax1, adjusting its size
fig.colorbar(im1, ax=ax1, fraction=.05)
# Add a colorbar next to ax2, adjusting its size
fig.colorbar(im2, ax=ax2, fraction=.05)

# Display the figure
## Your code goes here:

#######################
```

```python
# Access the x-coordinates (longitude values) of the 'IR_108' data array in the Scene object
## Your code goes here:


#######################
```

```python
# define palette (matplotlib style)
cmap = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#b6ffb6', '#79ff79', '#00ff00', '#ff8e8e', '#ff5151', '#ff0000', '#aa0000', '#550000', '#00ffff', '#00bef3', '#0079ca', 
        '#0028a2', '#000079', '#fbfb00', '#e7e700', '#d2d200', '#baba00', '#a6a600', '#8e8e00', '#797900', '#656500', '#dbdbdb', '#d2d2d2', '#cacaca', '#c2c2c2', '#bababa', '#b2b2b2', 
        '#aaaaaa', '#a6a6a6', '#9e9e9e', '#969696', '#8e8e8e', '#868686', '#7d7d7d', '#757575', '#6d6d6d', '#656565', '#5d5d5d', '#595959', '#515151', '#494949', '#414141', '#393939',
        '#313131', '#282828', '#202020', '#181818', '#141414', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',]
```

```python
# Retrieve the area definition (spatial reference) associated with the 'IR_108' data array from its attributes
## Your code goes here:


#######################
```

```python
# Convert the area definition to a Cartopy Coordinate Reference System (CRS) object for mapping and visualization
## Your code goes here:


#######################
```

```python
# Convert the area definition to a Cartopy CRS (Coordinate Reference System) object for accurate mapping
## Your code goes here:

#######################

# Create a figure with specific size
## Your code goes here:

#######################

# Add axes to the figure with the specified projection (crs)
ax = plt.axes(projection=crs)

# Draw coastlines on the map for reference
ax.coastlines()

# Add gridlines to the map
ax.gridlines()

# Display the 'IR_108' data as an image, using the converted Cartopy CRS for correct geographical placement
plt.imshow(scn['B13'], transform=crs, extent=crs.bounds, origin='upper')

# Add a color bar to the plot, labeling it with the data's unit of measurement
plt.colorbar(label=scn['B13'].attrs['units'])

# Display the plot
## Your code goes here:

#######################
```

```python
# Import the NumPy library, which provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays
## Your code goes here:

#######################
```

```python
# Create an array of levels for the color map, spanning from -109 to 56, with the same length as the 'cmap'
## Your code goes here:

#######################

# Create a BoundaryNorm object for the color map to ensure proper coloring based on specified levels
norm = plt.cm.colors.BoundaryNorm(levels, len(levels))

# Create a ListedColormap using the 'cmap' colors and the custom norm
irmap = plt.cm.colors.ListedColormap(cmap)

# Display results

# Convert the area definition to a Cartopy CRS (Coordinate Reference System) object for accurate mapping
## Your code goes here:

#######################

# Create a figure with specific size
## Your code goes here:

#######################

# Add axes to the figure with the specified projection (crs)
## Your code goes here:

#######################

# Draw coastlines on the map for reference
## Your code goes here:

#######################

# Add gridlines to the map
## Your code goes here:

#######################

# Display the 'IR_108' data as an image, using the converted Cartopy CRS for correct geographical placement
# Set the minimum and maximum values for the color map (vmin and vmax)
# Use the custom 'irmap' color map and apply the 'norm' for color scaling
## Your code goes here:

#######################

# Add a color bar to the plot, labeling it with the data's unit of measurement
## Your code goes here:

#######################

# Display the plot
p## Your code goes here:

#######################
```

### Jupyter Notebook (notebook)
*URL:* https://github.com/MAbdelkader94/Introduction-to-Geostationary-Satellites/blob/main/Lecture_01_AHI.ipynb

## SatPy - Part 1: Exploring Advanced Himawari Imager (AHI) data

For detailed documentation, visit [SatPy Documentation](https://satpy.readthedocs.io/en/latest/index.html).

SatPy is a powerful library for **reading**, **manipulating**, and **displaying** data from remote sensors, primarily related to meteorology. It also provides the capability to **save** this data as images or in various formats.

SatPy excels at generating images with **individual channels or bands** and creating **RGB composites** directly from satellite instrument data.

The pyresample library is used for **resampling data** in different areas with specific projections or uniform grids.

Additionally, Satpy offers various **atmospheric corrections** and **visual enhancements**, either directly within Satpy or through the PySpectral and TrollImage packages.

# Advanced Himawari Imager (AHI) data
https://www.earthdata.nasa.gov/sensors/ahi

```python
urls2dwn = ['https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B01_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B02_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B03_JP01_R05_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B04_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B05_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B06_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B07_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B08_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B09_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B10_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B11_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B12_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B13_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B14_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B15_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B16_JP01_R20_S0101.DAT.bz2']
```

```python
import requests
import os

# Specify the local directory where you want to save the files.
local_directory = "Output_data"
# Ensure that the local directory exists; create it if it doesn't.
## Your code goes here:

#######################

# Iterate through the URLs and download files.
for urld in urls2dwn:
    # Extract the filename from the URL.
    ntw = urld.split('/')[-1]
    
    # Construct the complete path to save the file in the local directory.
    file_path = os.path.join(local_directory, ntw)
    
    # Send an HTTP GET request to the URL.
    resp = requests.get(urld)
    
    # Check if the response is successful (status code 200).
    if resp.status_code == 200:
        # Write the content to the file in binary mode.
        with open(file_path, "wb") as file:
            file.write(resp.content)
        print(f"File '{ntw}' downloaded and saved to '{local_directory}'.")
    else:
        print(f"Failed to download '{ntw}' from the URL: {urld}")

```

## Loading and Visualizing Satellite Data

# SatPy is well-suited for working with geostationary satellite data, such as GOES-R or Himawari:

```python
# Importing the warnings module and setting it to ignore all warnings.
# This is useful to prevent unnecessary warning messages from cluttering the notebook output.

## Your code goes here:

#######################
```

```python
# Importing Scene from the satpy module. Scene is used to represent satellite data 
# and allows for operations like reading, resampling, compositing, and saving data.
## Your code goes here:

#######################


# Importing find_files_and_readers from satpy. This function is used to automatically
# locate satellite data files and determine the appropriate reader based on the 
# metadata and contents of the files.
## Your code goes here:

#######################
```

This line imports the debug_on function from the satpy.utils module, which is used to enable detailed debug logging in Satpy. This can be helpful for troubleshooting and understanding the internal workings of Satpy processes.

```python
## Your code goes here:

#######################
```

## Searching for Native MSG Data

```python
 # Importing datetime for date and time operations
## Your code goes here:

#######################
```

```python
fMSGn = find_files_and_readers(start_time = datetime(2024,3,2,16,0),  # Set start time for file search
                            #end_time = datetime(2019,7,22,12,59),   # Optional: Set end time for file search
                            base_dir = 'Output_data',  # Set the base directory for the search
                            reader = 'ahi_hsd')  # Specify the file reader
## Your code goes here:
        # Display the found files
```

```python
## Your code goes here:
            # Import the glob module to find files using pattern matching
```

```python
## Your code goes here:

#######################

# List all files matching the specified pattern in the directory, useful for handling multiple files

# scn = Scene(reader = 'seviri_l1b_native', filenames = fnames)  # Create a Scene object using the SEVIRI L1B native reader with the specified filenames
```

> **SatPy** always expects the original file names!

So, do not change them when saving the data on your local machine. Otherwise, SatPy will not be able to open the files.

```python
# Creating a Scene object using the file information gathered by find_files_and_readers function
## Your code goes here:

#######################

```

```python
# Accessing the attributes of the Scene object to retrieve metadata and other information
## Your code goes here:

#######################

```

```python
# Creating a Scene object from the filenames specified in fMSGn
## Your code goes here:

#######################
```

```python
# Accessing the attributes of the Scene object to view metadata information
## Your code goes here:

#######################
```

```python
# Retrieve and print all available dataset names in the scene
## Your code goes here:



#######################
```

The `scn.load(['IR_108'], upper_right_corner='NE')` line in ther code bellow is used for loading a specific dataset from a satellite scene in Satpy. Let's break down what each part does:

1. `scn`: This is your Satpy `Scene` object, which contains data from satellite files that you've previously loaded.

2. `.load()`: This method is used to load specific datasets from the satellite files into memory, making them ready for processing and analysis.

3. `['IR_108']`: This is a list containing the names of the datasets you want to load. In this case, you're loading the dataset named `IR_108`, which typically refers to infrared imagery at a wavelength of 10.8 micrometers. This wavelength is often used for cloud imaging, among other applications.

4. `upper_right_corner='NE'`: This parameter specifies how the data should be oriented when loaded. `NE` means that the upper right corner of the data should be in the northeast. This can be important for getting the geographical orientation correct, especially when dealing with global or hemispherical datasets.

After running this line, the `IR_108` dataset will be loaded into your scene and ready for further processing, such as visualization or analysis.

```python
## Your code goes here:


#######################
```

The scn.keys() method in Satpy is used to retrieve a list of all the dataset keys available in the currently loaded Scene object.

```python
## Your code goes here:


#######################
```

```python
# Show the 'IR_108' dataset using Satpy's built-in visualization capabilities
## Your code goes here:


#######################
```

```python
%matplotlib inline
# Plot the 'IR_108' channel using matplotlib's imshow function
## Your code goes here:


#######################
```

```python
# Import the matplotlib library for creating visualizations in Python
## Your code goes here:


#######################
```

```python
# Create a figure and an axes object with specified figure size
## Your code goes here:

#######################

# Display the data from the 'IR_108' channel of the satellite scene using a grayscale color map
## Your code goes here:

#######################

# Hide the axis labels and ticks to focus on the image only
## Your code goes here:

#######################

# Add a colorbar to the plot with a fraction size of the plot, useful for scale/reference
## Your code goes here:

#######################

# Display the figure with all its components
## Your code goes here:

#######################
```

```python
# Accessing the 'IR_108' dataset from the Scene object 'scn'
# - 'scn' is a Scene object, used for handling satellite data.
# - 'IR_108' specifies an infrared channel at 10.8 micrometers.
# This dataset is used for cloud imaging, surface temperature, and atmospheric analysis in meteorology.
## Your code goes here:

#######################
```

# Radiance Calibration

```python
# Load the data for the 10.8μm band.
# The parameter [10.8] specifies the wavelength of the band in micrometers.
scn.load([10.3], 

         # Specify the calibration to radiance values.
         # "radiance" calibration converts the data to radiometric units (mW m-2 sr-1 (cm-1)-1).
         ## Your code goes here:
         calibration=, 

         # Set the orientation of the image.
         # "upper_right_corner='NE'" aligns the image with its upper right corner to the northeast.
         upper_right_corner='NE')
```

# Brightness Temperature Calibration

```python
# Load the data for the 10.8μm band again, this time for a different calibration.
scn.load([10.3], 

         # Specify the calibration to brightness temperatures.
         # "brightness_temperature" calibration converts the data to temperature units (Kelvin).
         ## Your code goes here:

         calibration=, 

         # Maintain the same orientation as before.
         upper_right_corner='NE')
```

```python
# List all the datasets currently loaded into the Scene object 'scn'
## Your code goes here:



#######################
```

```python
# Convert the keys view to a list to enable indexing
## Your code goes here:

#######################


# Access the second dataset key
## Your code goes here:

#######################

# Extract the central wavelength from the 'wavelength' attribute of the second dataset key
## Your code goes here:

#######################

# Print the central wavelength and the key for the second dataset
## Your code goes here:


#######################
```

```python
# Create a figure and two subplot axes, arranged horizontally, with specified size
## Your code goes here:


#######################

# Display the values of the second dataset in the Scene on the first subplot (ax1) using a grayscale color map
im1 = ax1.imshow(scn[scn.keys()[1]].values, cmap="Greys")
# Remove the axis labels and ticks for ax1
ax1.set_axis_off()

# Display the values of the first dataset in the Scene on the second subplot (ax2) using a grayscale color map
im2 = ax2.imshow(scn[scn.keys()[0]].values, cmap="Greys")
# Remove the axis labels and ticks for ax2
ax2.set_axis_off()

# Set the title for ax2
ax2.set_title("10.8μm Brightness temperature")
# Set the title for ax1
ax1.set_title("10.8μm Radiance")

# Add a colorbar next to ax1, adjusting its size
fig.colorbar(im1, ax=ax1, fraction=.05)
# Add a colorbar next to ax2, adjusting its size
fig.colorbar(im2, ax=ax2, fraction=.05)

# Display the figure
## Your code goes here:

#######################
```

```python
# Access the x-coordinates (longitude values) of the 'IR_108' data array in the Scene object
## Your code goes here:


#######################
```

```python
# define palette (matplotlib style)
cmap = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#b6ffb6', '#79ff79', '#00ff00', '#ff8e8e', '#ff5151', '#ff0000', '#aa0000', '#550000', '#00ffff', '#00bef3', '#0079ca', 
        '#0028a2', '#000079', '#fbfb00', '#e7e700', '#d2d200', '#baba00', '#a6a600', '#8e8e00', '#797900', '#656500', '#dbdbdb', '#d2d2d2', '#cacaca', '#c2c2c2', '#bababa', '#b2b2b2', 
        '#aaaaaa', '#a6a6a6', '#9e9e9e', '#969696', '#8e8e8e', '#868686', '#7d7d7d', '#757575', '#6d6d6d', '#656565', '#5d5d5d', '#595959', '#515151', '#494949', '#414141', '#393939',
        '#313131', '#282828', '#202020', '#181818', '#141414', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',]
```

```python
# Retrieve the area definition (spatial reference) associated with the 'IR_108' data array from its attributes
## Your code goes here:


#######################
```

```python
# Convert the area definition to a Cartopy Coordinate Reference System (CRS) object for mapping and visualization
## Your code goes here:


#######################
```

```python
# Convert the area definition to a Cartopy CRS (Coordinate Reference System) object for accurate mapping
## Your code goes here:

#######################

# Create a figure with specific size
## Your code goes here:

#######################

# Add axes to the figure with the specified projection (crs)
ax = plt.axes(projection=crs)

# Draw coastlines on the map for reference
ax.coastlines()

# Add gridlines to the map
ax.gridlines()

# Display the 'IR_108' data as an image, using the converted Cartopy CRS for correct geographical placement
plt.imshow(scn['B13'], transform=crs, extent=crs.bounds, origin='upper')

# Add a color bar to the plot, labeling it with the data's unit of measurement
plt.colorbar(label=scn['B13'].attrs['units'])

# Display the plot
## Your code goes here:

#######################
```

```python
# Import the NumPy library, which provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays
## Your code goes here:

#######################
```

```python
# Create an array of levels for the color map, spanning from -109 to 56, with the same length as the 'cmap'
## Your code goes here:

#######################

# Create a BoundaryNorm object for the color map to ensure proper coloring based on specified levels
norm = plt.cm.colors.BoundaryNorm(levels, len(levels))

# Create a ListedColormap using the 'cmap' colors and the custom norm
irmap = plt.cm.colors.ListedColormap(cmap)

# Display results

# Convert the area definition to a Cartopy CRS (Coordinate Reference System) object for accurate mapping
## Your code goes here:

#######################

# Create a figure with specific size
## Your code goes here:

#######################

# Add axes to the figure with the specified projection (crs)
## Your code goes here:

#######################

# Draw coastlines on the map for reference
## Your code goes here:

#######################

# Add gridlines to the map
## Your code goes here:

#######################

# Display the 'IR_108' data as an image, using the converted Cartopy CRS for correct geographical placement
# Set the minimum and maximum values for the color map (vmin and vmax)
# Use the custom 'irmap' color map and apply the 'norm' for color scaling
## Your code goes here:

#######################

# Add a color bar to the plot, labeling it with the data's unit of measurement
## Your code goes here:

#######################

# Display the plot
p## Your code goes here:

#######################
```

### jn-test (notebook)
*URL:* https://github.com/MAbdelkader94/Introduction-to-Geostationary-Satellites/blob/main/Lecture_01_AHI.ipynb

## SatPy - Part 1: Exploring Advanced Himawari Imager (AHI) data

For detailed documentation, visit [SatPy Documentation](https://satpy.readthedocs.io/en/latest/index.html).

SatPy is a powerful library for **reading**, **manipulating**, and **displaying** data from remote sensors, primarily related to meteorology. It also provides the capability to **save** this data as images or in various formats.

SatPy excels at generating images with **individual channels or bands** and creating **RGB composites** directly from satellite instrument data.

The pyresample library is used for **resampling data** in different areas with specific projections or uniform grids.

Additionally, Satpy offers various **atmospheric corrections** and **visual enhancements**, either directly within Satpy or through the PySpectral and TrollImage packages.

# Advanced Himawari Imager (AHI) data
https://www.earthdata.nasa.gov/sensors/ahi

```python
urls2dwn = ['https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B01_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B02_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B03_JP01_R05_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B04_JP01_R10_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B05_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B06_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B07_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B08_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B09_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B10_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B11_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B12_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B13_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B14_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B15_JP01_R20_S0101.DAT.bz2',
 'https://noaa-himawari9.s3.amazonaws.com/AHI-L1b-Japan/2024/03/02/1600/HS_H09_20240302_1600_B16_JP01_R20_S0101.DAT.bz2']
```

```python
import requests
import os

# Specify the local directory where you want to save the files.
local_directory = "Output_data"
# Ensure that the local directory exists; create it if it doesn't.
## Your code goes here:

#######################

# Iterate through the URLs and download files.
for urld in urls2dwn:
    # Extract the filename from the URL.
    ntw = urld.split('/')[-1]
    
    # Construct the complete path to save the file in the local directory.
    file_path = os.path.join(local_directory, ntw)
    
    # Send an HTTP GET request to the URL.
    resp = requests.get(urld)
    
    # Check if the response is successful (status code 200).
    if resp.status_code == 200:
        # Write the content to the file in binary mode.
        with open(file_path, "wb") as file:
            file.write(resp.content)
        print(f"File '{ntw}' downloaded and saved to '{local_directory}'.")
    else:
        print(f"Failed to download '{ntw}' from the URL: {urld}")

```

## Loading and Visualizing Satellite Data

# SatPy is well-suited for working with geostationary satellite data, such as GOES-R or Himawari:

```python
# Importing the warnings module and setting it to ignore all warnings.
# This is useful to prevent unnecessary warning messages from cluttering the notebook output.

## Your code goes here:

#######################
```

```python
# Importing Scene from the satpy module. Scene is used to represent satellite data 
# and allows for operations like reading, resampling, compositing, and saving data.
## Your code goes here:

#######################


# Importing find_files_and_readers from satpy. This function is used to automatically
# locate satellite data files and determine the appropriate reader based on the 
# metadata and contents of the files.
## Your code goes here:

#######################
```

This line imports the debug_on function from the satpy.utils module, which is used to enable detailed debug logging in Satpy. This can be helpful for troubleshooting and understanding the internal workings of Satpy processes.

```python
## Your code goes here:

#######################
```

## Searching for Native MSG Data

```python
 # Importing datetime for date and time operations
## Your code goes here:

#######################
```

```python
fMSGn = find_files_and_readers(start_time = datetime(2024,3,2,16,0),  # Set start time for file search
                            #end_time = datetime(2019,7,22,12,59),   # Optional: Set end time for file search
                            base_dir = 'Output_data',  # Set the base directory for the search
                            reader = 'ahi_hsd')  # Specify the file reader
## Your code goes here:
        # Display the found files
```

```python
## Your code goes here:
            # Import the glob module to find files using pattern matching
```

```python
## Your code goes here:

#######################

# List all files matching the specified pattern in the directory, useful for handling multiple files

# scn = Scene(reader = 'seviri_l1b_native', filenames = fnames)  # Create a Scene object using the SEVIRI L1B native reader with the specified filenames
```

> **SatPy** always expects the original file names!

So, do not change them when saving the data on your local machine. Otherwise, SatPy will not be able to open the files.

```python
# Creating a Scene object using the file information gathered by find_files_and_readers function
## Your code goes here:

#######################

```

```python
# Accessing the attributes of the Scene object to retrieve metadata and other information
## Your code goes here:

#######################

```

```python
# Creating a Scene object from the filenames specified in fMSGn
## Your code goes here:

#######################
```

```python
# Accessing the attributes of the Scene object to view metadata information
## Your code goes here:

#######################
```

```python
# Retrieve and print all available dataset names in the scene
## Your code goes here:



#######################
```

The `scn.load(['IR_108'], upper_right_corner='NE')` line in ther code bellow is used for loading a specific dataset from a satellite scene in Satpy. Let's break down what each part does:

1. `scn`: This is your Satpy `Scene` object, which contains data from satellite files that you've previously loaded.

2. `.load()`: This method is used to load specific datasets from the satellite files into memory, making them ready for processing and analysis.

3. `['IR_108']`: This is a list containing the names of the datasets you want to load. In this case, you're loading the dataset named `IR_108`, which typically refers to infrared imagery at a wavelength of 10.8 micrometers. This wavelength is often used for cloud imaging, among other applications.

4. `upper_right_corner='NE'`: This parameter specifies how the data should be oriented when loaded. `NE` means that the upper right corner of the data should be in the northeast. This can be important for getting the geographical orientation correct, especially when dealing with global or hemispherical datasets.

After running this line, the `IR_108` dataset will be loaded into your scene and ready for further processing, such as visualization or analysis.

```python
## Your code goes here:


#######################
```

The scn.keys() method in Satpy is used to retrieve a list of all the dataset keys available in the currently loaded Scene object.

```python
## Your code goes here:


#######################
```

```python
# Show the 'IR_108' dataset using Satpy's built-in visualization capabilities
## Your code goes here:


#######################
```

```python
%matplotlib inline
# Plot the 'IR_108' channel using matplotlib's imshow function
## Your code goes here:


#######################
```

```python
# Import the matplotlib library for creating visualizations in Python
## Your code goes here:


#######################
```

```python
# Create a figure and an axes object with specified figure size
## Your code goes here:

#######################

# Display the data from the 'IR_108' channel of the satellite scene using a grayscale color map
## Your code goes here:

#######################

# Hide the axis labels and ticks to focus on the image only
## Your code goes here:

#######################

# Add a colorbar to the plot with a fraction size of the plot, useful for scale/reference
## Your code goes here:

#######################

# Display the figure with all its components
## Your code goes here:

#######################
```

```python
# Accessing the 'IR_108' dataset from the Scene object 'scn'
# - 'scn' is a Scene object, used for handling satellite data.
# - 'IR_108' specifies an infrared channel at 10.8 micrometers.
# This dataset is used for cloud imaging, surface temperature, and atmospheric analysis in meteorology.
## Your code goes here:

#######################
```

# Radiance Calibration

```python
# Load the data for the 10.8μm band.
# The parameter [10.8] specifies the wavelength of the band in micrometers.
scn.load([10.3], 

         # Specify the calibration to radiance values.
         # "radiance" calibration converts the data to radiometric units (mW m-2 sr-1 (cm-1)-1).
         ## Your code goes here:
         calibration=, 

         # Set the orientation of the image.
         # "upper_right_corner='NE'" aligns the image with its upper right corner to the northeast.
         upper_right_corner='NE')
```

# Brightness Temperature Calibration

```python
# Load the data for the 10.8μm band again, this time for a different calibration.
scn.load([10.3], 

         # Specify the calibration to brightness temperatures.
         # "brightness_temperature" calibration converts the data to temperature units (Kelvin).
         ## Your code goes here:

         calibration=, 

         # Maintain the same orientation as before.
         upper_right_corner='NE')
```

```python
# List all the datasets currently loaded into the Scene object 'scn'
## Your code goes here:



#######################
```

```python
# Convert the keys view to a list to enable indexing
## Your code goes here:

#######################


# Access the second dataset key
## Your code goes here:

#######################

# Extract the central wavelength from the 'wavelength' attribute of the second dataset key
## Your code goes here:

#######################

# Print the central wavelength and the key for the second dataset
## Your code goes here:


#######################
```

```python
# Create a figure and two subplot axes, arranged horizontally, with specified size
## Your code goes here:


#######################

# Display the values of the second dataset in the Scene on the first subplot (ax1) using a grayscale color map
im1 = ax1.imshow(scn[scn.keys()[1]].values, cmap="Greys")
# Remove the axis labels and ticks for ax1
ax1.set_axis_off()

# Display the values of the first dataset in the Scene on the second subplot (ax2) using a grayscale color map
im2 = ax2.imshow(scn[scn.keys()[0]].values, cmap="Greys")
# Remove the axis labels and ticks for ax2
ax2.set_axis_off()

# Set the title for ax2
ax2.set_title("10.8μm Brightness temperature")
# Set the title for ax1
ax1.set_title("10.8μm Radiance")

# Add a colorbar next to ax1, adjusting its size
fig.colorbar(im1, ax=ax1, fraction=.05)
# Add a colorbar next to ax2, adjusting its size
fig.colorbar(im2, ax=ax2, fraction=.05)

# Display the figure
## Your code goes here:

#######################
```

```python
# Access the x-coordinates (longitude values) of the 'IR_108' data array in the Scene object
## Your code goes here:


#######################
```

```python
# define palette (matplotlib style)
cmap = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#b6ffb6', '#79ff79', '#00ff00', '#ff8e8e', '#ff5151', '#ff0000', '#aa0000', '#550000', '#00ffff', '#00bef3', '#0079ca', 
        '#0028a2', '#000079', '#fbfb00', '#e7e700', '#d2d200', '#baba00', '#a6a600', '#8e8e00', '#797900', '#656500', '#dbdbdb', '#d2d2d2', '#cacaca', '#c2c2c2', '#bababa', '#b2b2b2', 
        '#aaaaaa', '#a6a6a6', '#9e9e9e', '#969696', '#8e8e8e', '#868686', '#7d7d7d', '#757575', '#6d6d6d', '#656565', '#5d5d5d', '#595959', '#515151', '#494949', '#414141', '#393939',
        '#313131', '#282828', '#202020', '#181818', '#141414', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',]
```

```python
# Retrieve the area definition (spatial reference) associated with the 'IR_108' data array from its attributes
## Your code goes here:


#######################
```

```python
# Convert the area definition to a Cartopy Coordinate Reference System (CRS) object for mapping and visualization
## Your code goes here:


#######################
```

```python
# Convert the area definition to a Cartopy CRS (Coordinate Reference System) object for accurate mapping
## Your code goes here:

#######################

# Create a figure with specific size
## Your code goes here:

#######################

# Add axes to the figure with the specified projection (crs)
ax = plt.axes(projection=crs)

# Draw coastlines on the map for reference
ax.coastlines()

# Add gridlines to the map
ax.gridlines()

# Display the 'IR_108' data as an image, using the converted Cartopy CRS for correct geographical placement
plt.imshow(scn['B13'], transform=crs, extent=crs.bounds, origin='upper')

# Add a color bar to the plot, labeling it with the data's unit of measurement
plt.colorbar(label=scn['B13'].attrs['units'])

# Display the plot
## Your code goes here:

#######################
```

```python
# Import the NumPy library, which provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays
## Your code goes here:

#######################
```

```python
# Create an array of levels for the color map, spanning from -109 to 56, with the same length as the 'cmap'
## Your code goes here:

#######################

# Create a BoundaryNorm object for the color map to ensure proper coloring based on specified levels
norm = plt.cm.colors.BoundaryNorm(levels, len(levels))

# Create a ListedColormap using the 'cmap' colors and the custom norm
irmap = plt.cm.colors.ListedColormap(cmap)

# Display results

# Convert the area definition to a Cartopy CRS (Coordinate Reference System) object for accurate mapping
## Your code goes here:

#######################

# Create a figure with specific size
## Your code goes here:

#######################

# Add axes to the figure with the specified projection (crs)
## Your code goes here:

#######################

# Draw coastlines on the map for reference
## Your code goes here:

#######################

# Add gridlines to the map
## Your code goes here:

#######################

# Display the 'IR_108' data as an image, using the converted Cartopy CRS for correct geographical placement
# Set the minimum and maximum values for the color map (vmin and vmax)
# Use the custom 'irmap' color map and apply the 'norm' for color scaling
## Your code goes here:

#######################

# Add a color bar to the plot, labeling it with the data's unit of measurement
## Your code goes here:

#######################

# Display the plot
p## Your code goes here:

#######################
```
