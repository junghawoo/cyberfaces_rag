---
title: "Unit 312"
unit_id: 312
---

# Unit 312

## Extracted resources (local files)

### GeoEDF_Presentation.pdf
*Source file:* `GeoEDF_Presentation.pdf`  ·  *type:* pdf

GeoEDF: An Extensible Geospatial Data 
Framework for FAIR Science
Rajesh Kalyanam

GeoEDF Grant
An Extensible Geospatial Data Framework Towards 
FAIR Science 
To help data-driven sciences to be more
Findable, Accessible, Interoperable, Reusable
funded by U.S. National Science Foundation (NSF) CSSI program 
award #: 1835822, Oct 2018 - Sep 2025
Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and 
do not necessarily reflect the views of the National Science Foundation.

GeoEDF Vision
Image by Dr. X. Carol Song (GeoEDF PI)

Example Agricultural Economics Workflow
Multidisciplinary 
domains often need to 
access diverse datasets 
and integrate them 
with existing models
Image by Dr. Uris Baldos (GeoEDF Co-PI)

Reality!
Working through 
the specifics reveals 
the more messy 
details!

GeoEDF Design Principles
Streamline data 
wrangling in 
research workflows
Enable researchers to 
break down a complex 
research task into a 
collection of data 
acquisition and 
processing sub-tasks
Promote FAIR 
science principles
Integrate GeoEDF and 
cyberinfrastructure to 
implicitly & explicitly 
promote FAIR science 
principles
Provide reusable and 
scalable workflow 
building blocks
Improve the efficiency of 
day-to-day research 
workflows by enabling 
standardization, reuse, 
composition, and 
scalable execution
03 
01 
02

GeoEDF Components
Reusable Data 
Connectors
Implement various 
data access protocols, 
enable data acquisition 
from popular 
repositories
Reusable Data 
Processors
Implement domain 
agnostic & domain 
specific geospatial 
processing operations
Plug-and-play 
Workflow Composer
Enable the 
composition of 
individual connectors 
& processors into 
complex workflows 
GeoEDF
Enable researchers to conceive of geospatial data driven 
workflows as a sequence of data acquisition and processing steps 
that can be carried out using pre-existing or user contributed 
connectors and processors

Data Connector Examples
NASA
MODIS, SMAP, other Earthdata DAACs
USGS
Elevation, land use, hydrography, Gage, NLDI
USDA
Soil, land cover, land use
CUASHI
Rainfall, Hydroshare resources
EarthStat
Crop data
FAO
Arable land, harvest data
CIESIN
Population data
EPA
Water quality
Others (no API yet)
Open Data Cubes, Google Earth Engine, ESS-Dive

Data Processor Examples
Domain 
Independent
Reproject, resample, format transformation, filter, mosaic, clip/mask, 
aggregate (spatial & temporal), visualization, reclassification
Hydrology
Terrain analysis, flood models
Digital Ag
Query, spatial/temporal filter, ML training, decision support
Sustainability
Downsample, (weighted) aggregate, FEWS models

Plug-and-play Workflow Composer
❖Workflow Framework defining
➢Standardized interfaces for connectors and processors
➢Syntax and semantics of defining and composing instances of connectors and 
processors into scientific workflows
➢Scripts for binding and executing connectors and processors
❖Workflow Engine transforming
➢“Declarative”, abstract workflows into code executing on heterogeneous compute 
resources
➢Transforms a GeoEDF workflow into a Pegasus workflow DAX (with nesting)
➢Utilizes framework scripts when running workflow jobs

GeoEDF in a nutshell
Workflows are sequences 
of connector and 
processor instances
Connector and 
Processor instances 
specified in YAML
Connector and 
Processor Python 
classes
Kalyanam, R., Zhao, L., Song, X.C., Merwade, V., Jin, J., Baldos, U. and Smith, J., 2020. GeoEDF: An extensible geospatial data framework for fair science. In Practice and 
Experience in Advanced Research Computing 2020: Catch the Wave (pp. 207-214).

Example Hydrologic Workflow
Apply GeoEDF principles

Corresponding GeoEDF Workflow
 $1:
        Input:
            NASAInput:
                  url: https://e4ftl01.cr.usgs.gov/MOTAMCD15A3H.006/%{file}
                 user: rkalyana
                  password: 
       Filter:
          file:
             PathFilter:
                  pattern: '%{dtstring}/MCD15A3H.*.h09v07*.hdf'
          dtstring:         
              DateTimeFilter:
                   pattern: ‘%Y.%m.%d’
                   start: 07/16/2002
  $2:
    HDFEOSShapefileMask:
      hdffile: $1
              shapefile: /home/mygeohub/rkalyana/subs1_projected_171936.shp
              datasets: [Lai]

Corresponding GeoEDF Workflow
  $1:
         Input:
             NASAInput:
                   url: https://e4ftl01.cr.usgs.gov/MOTAMCD15A3H.006/%{file}
                  user: rkalyana
                   password: 
         Filter:
             file:
                 PathFilter:
                      pattern: '%{dtstring}/MCD15A3H.*.h09v07*.hdf'
            dtstring:         
                 DateTimeFilter:
                     pattern: ‘%Y.%m.%d’
                     start: 07/16/2002
       
  $2:
           HDFEOSShapefileMask:
       hdffile: $1
                 shapefile: /home/mygeohub/rkalyana/subs1_projected_171936.shp
                 datasets: [Lai]
Data connector
Data processor
Dynamically 
bound variable
Python 
class
Workflow 
stage
●
Filters provide bindings for variables
●
They promote modularization and can 
implement complex spatial and temporal 
filtering
●
Filters help restrict the data that is actually 
“downloaded”

Workflow Framework
Scripts
• Shell script for running a 
workflow “stage” with 
bindings for variables, 
stage references 
(standardized script for 
Pegasus workflow tasks)
• Python scripts for 
processing, decrypting 
bindings and and 
executing a “plugin”
• General scripts for 
collect, merge 
operations
Python Classes
• GeoEDFPlugin
• Parent class for all 
plugins
• Methods for analyzing 
dependencies
• Methods for setting 
bindings
• GeoEDFExecutor
• Agnostic method for 
constructing plugin 
class & object
• Calls the specific 
plugin method
Packaging
• Python package pushed 
to PyPI
• Docker image with 
framework package and 
common geospatial 
Linux libraries (e.g., 
GDAL, rasterio, pyqgis) 
as a base image for all 
plugins

Workflow Engine
Scripts
• Python scripts for 
constructing Pegasus 
subdax for a particular 
workflow stage 
• Separate Python script 
for generating a final 
Pegasus dax return 
workflow outputs
Python Classes
• GeoEDFWorkflow
• High level class for 
instantiating, 
executing, and 
monitoring a 
workflow
• WorkflowBuilder
• Primary class for 
building Pegasus 
catalogs and workflow 
DAX
• Generates separate 
jobs for building and 
executing a subdax
Packaging
• Versioned PyPI package
• Support for various 
execution “brokers”, 
configurations
• Typically installed on a 
Pegasus workflow 
submit node

Workflow Execution using Pegasus
❖Connectors need to bind filter variables in order; arbitrary number of 
variable bindings may be generated; each binding “retrieves” arbitrary 
number of files
❖Processors may need to process an arbitrary number of files retrieved by 
a connector
❖Each connector or processor turns into its own “sub-workflow”
❖Top-level DAX builds and executes these sub-workflows as it goes
❖Sub-workflows only transfer back data necessary to construct the next 
”stage” sub-workflow; viz., filter values, file listing
❖Final step returns outputs
❖*Connectors/processors can have arbitrary software dependencies 
(containerization is a good idea!)
❖**Public-private keypair generated for each workflow to encrypt sensitive 
strings (viz. any field left blank for user input in workflow definition)

Connector, Processor Contribution Process
Import parent 
class
Define required and 
optional params
Set param values in 
init method
Define the required 
“get” or “process” 
method
Ensure key outputs 
are written to 
target_path

Connector, Processor Contribution Process
Add dependencies 
to setup.py

Connector, Processor Contribution Process
Make simple modifications 
to Nvidia HPC container 
maker (hpccm) recipe file

Connector, Processor Contribution Process
Build script generates 
Singularity recipe and builds 
container image (.sif) file

Connector, Processor Contribution Process
(1) Contribute 
connectors/processors via GitHub 
PRs
(2) Detect changes, build 
Singularity container, push to 
registry server
(3) Query registry for list of 
connector, processor containers

CI Integration
Connector 
Python class
Processor 
Python class
GitHub 
repo
CI/CD 
pipeline
Singularity 
Container 
registry (AWS)
GeoEDF 
YAML 
workflow
GeoEDF 
workflow 
engine
Condor pool/HPC/local 
execution host
Container image
Workflow job
GeoEDF 
framework
CI environment
Pegasus
Result data
Middleware
Shared 
Storage

Deployment
➢Publicly available gateway
➢Deployed in Jupyter notebook 
environment
➢Job submission to Purdue’s 
campus clusters via HUBzero 
submit tool
➢Self-contained Docker container
➢Can use to build and test new 
connectors, processors
➢Run on your own machine
➢Zero2JupyterHub helm chart 
deployment
➢Custom GeoEDF Jupyter 
notebook image
➢Local job submission/HPC 
submission via Bosco

### GeoEDF_tutorial_07162025.pdf
*Source file:* `GeoEDF_tutorial_07162025.pdf`  ·  *type:* pdf

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
08/04/2025
Purdue Research Computing

Use case: Creating a Greenness Map Using NASA Dataset
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l
•
Standard satellite images indicate the presence of green areas
•
MODIS LAI provides a scientific, quantitative measurement of vegetation density within those areas, making 
it much more helpful for ecological and environmental studies.
vs.

Leaf Area Index (LAI) : Greenness Index 
LAI is the ratio of total 
leaf area to ground 
area (dimensionless).
Example: LAI = 3 
means 3 m² of leaf 
surface per 1 m² of 
ground.
Ranges
Grasslands: ~0.5–2
Forests: ~3–9 
(depending on 
season and canopy 
type)
Weighted LAI
Summarizes the 
region’s vegetation 
status 
Meadow
https://pixabay.com/photos/landscape-agriculture-
meadow-hay-8060760/
Amazon rainforest canopy
https://pictures.butlernature.com/brazil/images/a
mazon_200307.html 
https://metergroup.com/education-guides/the-researchers-complete-guide-to-leaf-area-index-lai/

Overall Greenness of the subbasins in the Upper Wabash River Watershed?
Our area of interest: Indiana 
We want to create this weighted LAI map

GeoEDF workflow use case I 
Connect to 
NASA MODIS 
LAI dataset for a 
specific date
Download LAI dataset from NASA 
OPeNDAP Servers
Select the 
interested area, 
and find the LAI 
subdataset
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
Output: NetCDF file

Step 1: Download 
NASA 
MODIS LAI dataset 
•
The MCD15A3H dataset, available through theUSGS LP DAAC, is a 
MODIS product
•
MODIS = an instrument (sensor)
•
MODIS = Moderate Resolution Imaging Spectroradiometer
•
It's mounted on two satellites: Terra and Aqua
•
It collects raw radiance data (light reflected/emitted from Earth)
•
MODIS data products = derived geophysical datasets
•
NASA processes MODIS raw data into scientific "products" like:
•
LAI (Leaf Area Index) — MCD15A3H
•
NDVI (Vegetation index)
•
LST (Land Surface Temperature)
•
Snow cover
•
Fire products
•
These are not raw satellite images but gridded, pre-processed data 
layers
Aqua satellite

The MCD15A3H 
dataset
•
Global 4-day composite data for Leaf Area Index (LAI) and Fraction 
of Photosynthetically Active Radiation (FPAR) at a 500-meter 
resolution. It combines data from both the Terra and Aqua MODIS 
sensors to generate a single, best-available pixel value for each 4 
days.
•
Key Details:
•
Product: MODIS/Terra+Aqua Leaf Area Index/FPAR 4-Day L4 
Global 500m
•
Temporal Resolution: 4-day composite
•
Spatial Resolution: 500 meters. Each pixel covers 500 
meters by 500 meters.
•
Variables: LAI, FPAR, quality flags, and standard deviations
•
Data Source: Combined data from 
both MODIS/Terra and MODIS/Aqua satellites
•
Data Access: Available through the LP DAAC Data Pool and 
NASA Earthdata Search
•
Data Format: Typically provided in HDF-EOS format
•
Key Applications: Used for a variety of applications including 
estimating photosynthesis, evapotranspiration, and net 
primary production, as well as understanding terrestrial 
carbon, water, and energy cycles.

Dataset Downloads 
from OPeNDAP Servers
NASA input connector automates these manual file 
search/download procedures.
1.
Check if a dataset exists on a specific date. If no 
data exists, a 'Resource not found' (404) error 
page appears. 
2.
Since we are interested in Indiana, pick an HDF 
file that contains tiles covering Indiana ( h09v07)
3.
Choose a file extension (.nc4) to download
Open-source Project for a Network 
Data Access Protocol (OPeNDAP)

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
 h09v07 tiles include parts of 
Indiana, Illinois, Ohio, and 
surrounding areas in the U.S.

NASAInput Connector Output
If your connector was successful, you will see the requested NC4 file was downloaded in  
/data/jobid/1/

NASA Panoply 
Data Viewer
• You can use this GUI 
software to view the 
variables contained in a 
.nc4 file. 
• Dataset: whole nc4 file
• Subdataset: Fpar_500m, 
Lai_500m,…
• We will use the 
‘Lai_500m' 
variable/subdataset only. 
LAI quantifies the one-sided green leaf area per unit ground area, while FPAR measures the 
fraction of photosynthetically active radiation absorbed by a plant canopy.
Both variables are crucial inputs for models that estimate surface photosynthesis, 
evapotranspiration, and net primary production, contributing to the understanding of terrestrial 
energy, carbon, and water cycles.

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

How Does the 
Processor Get 
Connector Data?
HDFEOSShapefileMask requires three 
parameters. 
1. HDFFile is the filename of the NASA input 
connector downloaded.
2. A shapefile defines the geometries of the 
subbasins of interest. LAI is calculated for each 
subbasin. 
3. Datasets: This is a list of subdatasets or 
variable names that the Processor looks for in the 
HDFFile. One of the subdatasets of the given 
HDFFile must have a variable containing “Lai”. In 
our case, the processor finds the “Lai_500m” 
variable has the substring “Lai”.

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
File browser shows /geoedf/workflows/jobid/output/

GeoEDF workflow use case II 
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
GeoJSON

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

GeoJSON
• JSON-based:
• GeoJSON leverages the simplicity and readability of JSON for representing geographic 
data.
• Geographic Features:
• It supports various geometry types, including points, line strings, polygons, and multi-
part geometries like MultiPoint, MultiLineString, and MultiPolygon.
• Attributes:
• GeoJSON allows for the inclusion of non-spatial attributes (properties) associated with 
geographic features, providing additional context and information.
• Feature and FeatureCollection:
• Data is typically organized into "features," which represent individual geographic objects, 
and "feature collections," which group multiple features.
• Open Standard:
• GeoJSON is an open standard, meaning it's freely available for anyone to use and 
implement without licensing restrictions.

Final Results 
of mcd15-
viz.yml 
workflow

Processor Development
• Build a processor using NVIDIA HPC Container Maker 
• A Recipe file is needed to create a container (Docker or 
Singularity)
• HPC Container Maker can create both Docker and Singularity from 
the same recipe.

What is HPCCM?
• HPCCM = HPC Container Maker
• It’s a Python-based tool that generates container recipes (for 
Singularity or Docker) using high-level, reusable Python building 
blocks.
Benefit
Description
Modularity
Use reusable blocks for common software (e.g., gdal(), openmpi())
Multiple Formats
Output both Dockerfile and Singularity recipes from the same source
Consistency
Ensures reproducible builds across formats and projects
Less Error-Prone
Fewer manual commands, easier to maintain
HPC-Ready
Includes building blocks for compilers, MPI, CUDA, etc., common in HPC 
environments

HPCCM Recipe 
•
It copies the 
files/shapefile2geojson 
directory to the Singularity 
image’s /shapefile2geoson 
directory.
 
•
Then, “pip3 install” installs 
our package to the container.

In this line:
• hpccm is a tool that auto-generates container definition files
• --format singularity means: "Generate a Singularity definition file 
(not Dockerfile, etc.)"
• > Singularity means: Save the output to a file literally named 
Singularity

In this line:
• singularity is the command-line tool used to build and run containers
• build tells it to build a container image
• Shapefile2GeoJSON.sif is the output image file (the final container)
• Singularity is the input definition file (from the previous step)

GeoEDF 
documentation
https://geoedf.readthedocs.io/en/
latest/index.html

Thank you!
Questions?

H09v07 tiles
 h09v07
This identifies the tile location in the MODIS Sinusoidal Tiling System, 
which covers the Earth in a global grid:
h09 = horizontal tile index 9
v07 = vertical tile index 7
Each tile covers ~10° × 10° at the equator (~1113 km × 1113 km).
So h09v07 refers to a specific region of Earth — for example:
 It includes parts of Indiana, Illinois, Ohio, and surrounding areas in 
the U.S.

OPeNDAP server: Comparison with Others 
Feature
OPeNDAP
HTTP/Web Server
FTP Server
Purpose
Remote access to 
subsets of structured 
scientific data
Serving files and 
webpages
File transfer
Data Access
Allows partial data 
extraction (e.g. specific 
variables, time slices, 
lat/lon ranges)
Usually downloads 
entire file
Transfers entire file
Protocol
Uses DAP (Data Access 
Protocol)
Uses HTTP/S
Uses FTP protocol
Query Support
 Can send structured 
queries for specific 
dimensions, variables, 
or ranges
 No native query 
support
 No query support
Output
Returns binary or 
structured 
(NetCDF/XML) response
Static file or HTML
Binary file
Client Libraries
Works with tools like 
xarray, netCDF4-
python, MATLAB, IDL
General-purpose 
browsers or curl
FTP clients, shell
Efficiency
Highly efficient for large 
datasets (e.g., climate 
models, satellite rasters)
Inefficient for large data
Inefficient if only part of 
data is needed

### GeoEDF_tutorial_07252025.pdf
*Source file:* `GeoEDF_tutorial_07252025.pdf`  ·  *type:* pdf

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
Purdue University

Overcoming the data wrangling challenge
2
5-year framework implementation project
Multidisciplinary collaboration: Hydrology, ABE, Ag econ, Water quality
Multi-modal dissemination
Image credits: By www.python.org - www.python.org, GPL, 
https://commons.wikimedia.org/w/index.php?curid=34991651
connectors + 
processors
workflow 
building 
blocks
YAML workflows
workflow 
engine

GeoEDF Use case: Creating a Greenness Map Using NASA Dataset
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l
•
Standard satellite images indicate the presence of green areas
•
MODIS LAI provides a scientific, quantitative measurement of vegetation density within those areas, making it 
much more helpful for ecological and environmental studies.
vs.

Leaf Area Index (LAI) : Greenness Index 
LAI is the ratio of total 
leaf area to ground 
area (dimensionless).
Example: LAI = 3 
means 3 m² of leaf 
surface per 1 m² of 
ground.
Ranges
Grasslands: ~0.5–2
Forests: ~3–9 
(depending on 
season and canopy 
type)
Weighted LAI
Summarizes the 
region’s vegetation 
status 
Meadow
https://pixabay.com/photos/landscape-agriculture-
meadow-hay-8060760/ 
Amazon rainforest canopy
https://pictures.butlernature.com/brazil/images/am
azon_200307.html 
https://metergroup.com/education-guides/the-researchers-complete-guide-to-leaf-area-index-lai/

Why Do Hydrologists Care About LAI? 
Spatial region of Interest:
The Wabash River in Indiana 
Hydrologists aim to develop 
this weighted LAI map.
Hydrologists use Leaf Area 
Index (LAI) because it’s a key 
variable linking vegetation to 
the water cycle — particularly 
in processes like
•
Evapotranspiration
•
Rainfall interception
•
Soil moisture and infiltration
•
Runoff & Streamflow Response.

GeoEDF workflow use case I 
Connect to NASA 
MODIS LAI 
dataset for a 
specific date
Download LAI dataset from NASA 
OPeNDAP Servers
Select the 
interested area, 
and find the LAI 
subdataset
Compute the average LAI for each 
subbasin defined in the given Shape 
file. Each subbasin has a single average 
LAI value. It generates an output Shape 
file.
Output: NetCDF file

Step 1: Download NASA MODIS LAI dataset 
• The MCD15A3H dataset, available through the USGS LP 
DAAC, is a MODIS product
• MODIS = an instrument (sensor)
• MODIS = Moderate Resolution Imaging 
Spectroradiometer
• It's mounted on two satellites: Terra and Aqua
• It collects raw radiance data (light 
reflected/emitted from Earth)
• MODIS data products = derived geophysical datasets
• These are not raw satellite images but gridded, pre-
processed data layers
Aqua satellite

The MCD15A3H dataset: LAI, FPAR
It combines data from both the Terra and Aqua 
MODIS sensors to generate a single, best-
available pixel value for each 4 days.
Global 4-day composite data for Leaf Area Index 
(LAI) and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter resolution.
Both variables are used to calculate surface 
photosynthesis, evapotranspiration, and net 
primary production, which in turn are used to 
calculate terrestrial energy, carbon, and water 
cycle processes, as well as the biogeochemistry 
of vegetation.
8

Connectors Abstract Away the Specifics of Connecting and Transferring Data
NASA OPeNDAP Servers: 
Open-source Project for a Network Data Access Protocol 
(OPeNDAP)
Data query
Check if a dataset exists on a specific date. If no data exists, a 
'Resource not found' (404) error page appears
Filtering
Since we are interested in Indiana, pick an HDF file that contains 
tiles covering Indiana ( h09v07)
Transfer
Choose a file extension (.nc4) to download
NASA input connector automates the implementation of a specific 
protocol (OPeNDAP) for the data query, filtering, and transfer.

Example Hydrologic Workflow
Apply GeoEDF principles

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
 The H09V07 grid identifier 
encompasses parts of Indiana, Illinois, 
Ohio, and surrounding areas in the U.S.
Corresponding GeoEDF Workflow

Looking into a NASA Connector’s Output
• Variables contained in a 
NC4 file 
• Dataset: whole NC4 file
• Subdataset: Fpar_500m, 
Lai_500m,…
• ‘Lai_500m' variable 
contains the Leaf Area Index 
for each pixel (500m x 
500m)
LAI quantifies the one-sided green leaf area per unit ground area, while FPAR measures the fraction of 
photosynthetically active radiation absorbed by a plant canopy.
Both variables are crucial inputs for models that estimate surface photosynthesis, evapotranspiration, and net 
primary production, contributing to the understanding of terrestrial energy, carbon, and water cycles.

Step 2: Read LAI Data, Aggregate them for Subbasins
• Module for aggregating the data values from an HDF file 
for a given shapefile containing polygons. 
• This supports both HDF4 and HDF5, but assumes that 
the files are in the HDF-EOS format. 
• All processing occurs in the latitude-longitude space by 
reprojecting the shapefile to WGS84 and extracting the 
lat-lon for each grid cell in the HDF file. 
• Extraction of cell lat-lon pairs for HDF4 files relies on the 
eos2dump utility. 
• This supports aggregating more than one subdataset 
from an HDF file.
• The resulting shapefile contains a separate field for each 
subdataset aggregate value

How Does the Processor Get Connector Data?
HDFEOSShapefileMask requires three parameters. 
1. HDFFile is the filename of the NASA input 
connector downloaded.
2. A shapefile defines the geometries of the 
subbasins of interest. LAI is calculated for each 
subbasin. 
3. Datasets: This is a list of subdatasets or variable 
names that the Processor looks for in the HDFFile. 
One of the subdatasets of the given HDFFile must 
have a variable containing “Lai”. In our case, the 
processor finds the “Lai_500m” variable has the 
substring “Lai”.

Final Results for mcd.yml workflow  
•
The HDFEOSShapefileMask  processor calculated weighted 
LAI for each subbasin (polygon). 
•
A shapefile, a standard vector data format in GIS, stores the 
location, shape, and attributes of geographic features.
•
It's not a single file, but a collection of related files, the most 
important being the .shp, .shx, and .dbf files.
•
The .shp file stores the feature geometry (points, lines, 
polygons).
•
The .shx file contains the index of the geometry. 
•
The .dbf file stores attribute data associated with each 
feature.
File browser shows /geoedf/workflows/jobid/output/

GeoEDF workflow use case II 
Connect to NASA 
MODIS LAI 
dataset for a 
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
composite data for Leaf Area Index (LAI) 
and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter 
resolution
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
GeoJSON

Step 3: Convert a Shapefile into a GeoJSON file 
• Once you have the shapefile, you 
can visualize the LAI by selecting the 
feature of interest, i.e., LAI, and 
plotting it. 
• If you prefer a text result file that 
has geometry and features, we can 
use another processor, 
Shapefile2GeoJSON. It converts a 
shapefile to a JSON file.

Final Results of mcd15-viz.yml workflow

Processor Development
• Build a processor using NVIDIA HPC Container Maker 
• A Recipe file is needed to create a container (Docker or Singularity)
• HPC Container Maker can create both Docker and Singularity from the 
same recipe. 
• HPCCM is optional. You can still make a Docker container using a 
Dockerfile or a Singularity recipe. 
• Test a new Singularity container locally; if successful, push to the 
GeoEDF connector/processor repo.

What is HPCCM?
• HPCCM = HPC Container Maker
• It’s a Python-based tool that generates container recipes (for 
Singularity or Docker) using high-level, reusable Python building 
blocks.
Benefit
Description
Modularity
Use reusable blocks for common software (e.g., gdal(), openmpi())
Multiple Formats
Output both Dockerfile and Singularity recipes from the same source
Consistency
Ensures reproducible builds across formats and projects
Less Error-Prone
Fewer manual commands, easier to maintain
HPC-Ready
Includes building blocks for compilers, MPI, CUDA, etc., common in HPC 
environments

HPCCM Recipe 
•
It copies the 
files/shapefile2geojson 
directory to the Singularity 
image’s /shapefile2geoson 
directory.
 
•
Then, “pip3 install” installs our 
package to the container.
•
Now, users can execute 
Shapefile2GeoJSON by 
providing either parameter: 
•
input directory
•
shapefile name

Building Shapefile2GeoJSON Singularity Container
In this line:
• hpccm is a tool that auto-generates container definition files
• --format singularity means: "Generate a Singularity definition file 
(not Dockerfile, etc.)"
• > Singularity means: Save the output to a file literally named 
Singularity. “shapefile2geoson.def” could have been better naming.

Building Shapefile2GeoJSON Singularity Container
In this line:
• singularity is the command-line tool used to build and run containers
• build tells it to build a container image
• Shapefile2GeoJSON.sif is the output image file (the final container)
• Singularity is the input definition file (from the previous step)

GeoEDF documentation
https://geoedf.readthedocs.io/en/l
atest/index.html

Thank you!
Questions?
thompscs@purdue.edu
wooj@purdue.edu

GeoJSON
• JSON-based:
• GeoJSON leverages the simplicity and readability of JSON for representing 
geographic data.
• Geographic Features:
• It supports various geometry types, including points, line strings, polygons, and 
multi-part geometries like MultiPoint, MultiLineString, and MultiPolygon.
• Attributes:
• GeoJSON allows for the inclusion of non-spatial attributes (properties) associated 
with geographic features, providing additional context and information.
• Feature and FeatureCollection:
• Data is typically organized into "features," which represent individual geographic 
objects, and "feature collections," which group multiple features.
• Open Standard:
• GeoJSON is an open standard, meaning it's freely available for anyone to use and 
implement without licensing restrictions.

What is H09v07 tile?
 h09v07
This identifies the tile location in the MODIS Sinusoidal Tiling System, which covers 
the Earth in a global grid:
h09 = horizontal tile index 9
v07 = vertical tile index 7
Each tile covers ~10° × 10° at the equator (~1113 km × 1113 km).
So h09v07 refers to a specific region of Earth — for example:
 It includes parts of Indiana, Illinois, Ohio, and surrounding areas in the U.S.

OPeNDAP server: Comparison with Others 
Feature
OPeNDAP
HTTP/Web Server
FTP Server
Purpose
Remote access to subsets of 
structured scientific data
Serving files and webpages
File transfer
Data Access
Allows partial data extraction (e.g. 
specific variables, time slices, 
lat/lon ranges)
Usually downloads entire file
Transfers entire file
Protocol
Uses DAP (Data Access Protocol)
Uses HTTP/S
Uses FTP protocol
Query Support
 Can send structured queries 
for specific dimensions, variables, 
or ranges
 No native query support
 No query support
Output
Returns binary or structured 
(NetCDF/XML) response
Static file or HTML
Binary file
Client Libraries
Works with tools like xarray, 
netCDF4-python, MATLAB, IDL
General-purpose browsers or curl
FTP clients, shell
Efficiency
Highly efficient for large datasets 
(e.g., climate models, satellite 
rasters)
Inefficient for large data
Inefficient if only part of data is 
needed

### GeoEDF_tutorial_07312025.pdf
*Source file:* `GeoEDF_tutorial_07312025.pdf`  ·  *type:* pdf

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
Purdue University
08/04/2025

JS2 Aug 5 Maintenance
• This tutorial uses the JupyterHub running on the Jetstream2 cluster.
• JS2 will perform routine infrastructure maintenance from 7 am to 7 
p.m. on August 5. 
• https://jetstream-cloud.org/news-events/news/25-07-11_gpu-
maintenance.html
• During this maintenance, you will not be able to run notebooks in 
GeoEDF tutorials. 
2

EARTHDATA LOGIN Account required!
• If you have not created an EarthData 
account, create one before starting 
this tutorial
• https://urs.earthdata.nasa.gov/home
• Downloading the NASA DAAC MODIS 
dataset requires an account ID and a 
Password. 
• Without these, the GeoEDF NASA 
Input connector fails to download 
data.
3

Your GeoEDF tutorials are accessible at
https://149-165-151-111.js2proxy.cacao.run/hub/user-redirect/git-
pull?repo=https%3A%2F%2Fgithub.com%2Fgeoedf%2FCI4FAIR&urlpat
h=lab%2Ftree%2FCI4FAIR%2FGeoEDF_Tutorial_01.ipynb+&branch=mai
n 
oAlso available at:  https://tinyurl.com/ci4fair-geoedf
o Or, link at CyberFaces module: 
<link to module>
oUse provided username & password here
4

Overcoming the data wrangling challenge
5
5-year framework implementation project
Multidisciplinary collaboration: Hydrology, ABE, Ag econ, Water quality
Multi-modal dissemination
Image credits: By www.python.org - www.python.org, GPL, 
https://commons.wikimedia.org/w/index.php?curid=34991651
connectors + 
processors
workflow 
building 
blocks
YAML workflows
workflow 
engine

GeoEDF Workflow
• A logical flow to run connectors and 
processors
• Users write a YAML file to specify the 
execution sequences
• The execution sequence: $1, $2, $3,…
• The output of the previous step can 
serve as the input to the next processor. 
• Colored terms are reserved keywords
• The Pegasus WMS system manages 
actual workflows. 
6

GeoEDF Connectors
Download data for you
• A class instance that searches for the data you want and 
downloads it
Speed up data acquisition
• Suitable for frequently repeated downloading tasks
• Users select the data range (start date, end date) and 
frequency (daily, monthly, etc.).
• Download data faster ( parallel downloads)
Already exists! 
• Search for existing connectors before you write your own 
• You can revise the existing one to cater to new 
requirements
7

GeoEDF Connectors
• List of some of the popular connectors already available, what kind of 
data each handles
8

GeoEDF Processors
• A class/instance that computes something
• Does not have to use Connector outputs as input
• Can do any operations, such as
• Reproject, resample images,
• filter, clip/mask images,
• change formats, 
• Aggregate multiple datasets, e.g., compute 
averages, min, max value,
• Visualize data 
• Create new outputs
• An understanding of the input parameters of existing 
Processors is required.  
9

GeoEDF Processors
• List of some of the popular processors already available, summary 
of what operation they do
10

Hydrologic Use case: Creating a Greenness Map Using NASA Dataset
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l
•
Standard satellite images indicate the presence of green areas
•
MODIS LAI provides a scientific, quantitative measurement of vegetation density within those areas, making it 
much more helpful for ecological and environmental studies.
vs.

Leaf Area Index (LAI) : Greenness Index 
LAI is the ratio of total 
leaf area to ground 
area (dimensionless).
Example: LAI = 3 
means 3 m² of leaf 
surface per 1 m² of 
ground.
Ranges
Grasslands: ~0.5–2
Forests: ~3–9 
(depending on 
season and canopy 
type)
Weighted LAI
Summarizes the 
region’s vegetation 
status 
Meadow
https://pixabay.com/photos/landscape-agriculture-
meadow-hay-8060760/ 
Amazon rainforest canopy
https://pictures.butlernature.com/brazil/images/am
azon_200307.html 
https://metergroup.com/education-guides/the-researchers-complete-guide-to-leaf-area-index-lai/

Why Do Hydrologists Care About LAI? 
Spatial region of Interest:
The Wabash River in Indiana 
Hydrologists aim to develop 
this weighted LAI map.
Hydrologists use Leaf Area 
Index (LAI) because it’s a key 
variable linking vegetation to 
the water cycle — particularly 
in processes like
•
Evapotranspiration
•
Rainfall interception
•
Soil moisture and infiltration
•
Runoff & Streamflow Response.

GeoEDF workflow use case I 
Connect to NASA 
MODIS LAI 
dataset for a 
specific date
Download LAI dataset from NASA 
OPeNDAP Servers
Select the 
interested area, 
and find the LAI 
subdataset
Compute the average LAI for each 
subbasin defined in the given Shape 
file. Each subbasin has a single average 
LAI value. It generates an output Shape 
file.
Output: NetCDF file

Step 1: Download NASA MODIS LAI dataset 
• The MCD15A3H dataset, available through the USGS LP 
DAAC, is a MODIS product
• MODIS = an instrument (sensor)
• MODIS = Moderate Resolution Imaging 
Spectroradiometer
• It's mounted on two satellites: Terra and Aqua
• It collects raw radiance data (light 
reflected/emitted from Earth)
• MODIS data products = derived geophysical datasets
• These are not raw satellite images but gridded, pre-
processed data layers
Aqua satellite

The MCD15A3H dataset: LAI, FPAR
It combines data from both the Terra and Aqua 
MODIS sensors to generate a single, best-
available pixel value for each 4 days.
Global 4-day composite data for Leaf Area Index 
(LAI) and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter resolution.
Both variables are used to calculate surface 
photosynthesis, evapotranspiration, and net 
primary production, which in turn are used to 
calculate terrestrial energy, carbon, and water 
cycle processes, as well as the biogeochemistry 
of vegetation.
16

Connectors Abstract Away the Specifics of Connecting and Transferring Data
NASA OPeNDAP Servers: 
Open-source Project for a Network Data Access Protocol 
(OPeNDAP)
Data query
Check if a dataset exists on a specific date. If no data exists, a 
'Resource not found' (404) error page appears
Filtering
Since we are interested in Indiana, pick an HDF file that contains 
tiles covering Indiana ( h09v07)
Transfer
Choose a file extension (.nc4) to download
NASA input connector automates the implementation of a specific 
protocol (OPeNDAP) for the data query, filtering, and transfer.
Browse the list of available dates:
https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15
A3H.061/ 
You must be logged in to Earthdata.gov to access the OPeNDAP 
server.

Example Hydrologic Workflow
Apply GeoEDF principles

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
 The H09V07 grid identifier 
encompasses parts of Indiana, Illinois, 
Ohio, and surrounding areas in the U.S.
Corresponding GeoEDF Workflow

Looking into a NASA Connector’s Output
• Variables contained in a 
NC4 file 
• Dataset: whole NC4 file
• Subdataset: Fpar_500m, 
Lai_500m,…
• ‘Lai_500m' variable 
contains the Leaf Area Index 
for each pixel (500m x 
500m)
LAI quantifies the one-sided green leaf area per unit ground area, while FPAR measures the fraction of 
photosynthetically active radiation absorbed by a plant canopy.
Both variables are crucial inputs for models that estimate surface photosynthesis, evapotranspiration, and net 
primary production, contributing to the understanding of terrestrial energy, carbon, and water cycles.

Understanding Jupyter Notebooks
•
What is a Jupyter Notebook?
A Jupyter Notebook is an interactive digital notebook that 
lets you write and run code, see results instantly, and 
combine text, images, and charts — all in one place. 
Scientists, data analysts, and students widely use it.
•
How Does It Work?
•
You use a web browser to interact with the notebook 
(like visiting a website).
Behind the scenes, your code is sent to a Jupyter 
Server, which runs the code and sends the results back 
to your screen.
•
You can view outputs like numbers, graphs, maps, or 
tables — right below your code.
•
Key Features:
•
 Code + Text: Mix explanation and computation
•
 Live Code: Click “Run” to execute each cell
•
 Great for learning, exploring, and explaining ideas
•
 Works from any device with a browser — but runs 
on the server
21

Step 2: Read LAI Data, Aggregate them for Subbasins
• Module for aggregating the data values from an HDF file 
for a given shapefile containing polygons. 
• This supports both HDF4 and HDF5, but assumes that 
the files are in the HDF-EOS format. 
• All processing occurs in the latitude-longitude space by 
reprojecting the shapefile to WGS84 and extracting the 
lat-lon for each grid cell in the HDF file. 
• Extraction of cell lat-lon pairs for HDF4 files relies on the 
eos2dump utility. 
• This supports aggregating more than one subdataset 
from an HDF file.
• The resulting shapefile contains a separate field for each 
subdataset aggregate value

How Does the Processor Get Connector Data?
HDFEOSShapefileMask requires three parameters. 
1. HDFFile is the filename of the NASA input 
connector downloaded.
2. A shapefile defines the geometries of the 
subbasins of interest. LAI is calculated for each 
subbasin. 
3. Datasets: This is a list of subdatasets or variable 
names that the Processor looks for in the HDFFile. 
One of the subdatasets of the given HDFFile must 
have a variable containing “Lai”. In our case, the 
processor finds the “Lai_500m” variable has the 
substring “Lai”.

Final Results for mcd.yml workflow  
•
The HDFEOSShapefileMask  processor calculated weighted 
LAI for each subbasin (polygon). 
•
A shapefile, a standard vector data format in GIS, stores the 
location, shape, and attributes of geographic features.
•
It's not a single file, but a collection of related files, the most 
important being the .shp, .shx, and .dbf files.
•
The .shp file stores the feature geometry (points, lines, 
polygons).
•
The .shx file contains the index of the geometry. 
•
The .dbf file stores attribute data associated with each 
feature.
File browser shows /geoedf/workflows/jobid/output/

GeoEDF workflow use case II 
Connect to NASA 
MODIS LAI 
dataset for a 
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
composite data for Leaf Area Index (LAI) 
and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter 
resolution
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
GeoJSON

Step 3: Convert a Shapefile into a GeoJSON file 
• Once you have the shapefile, you 
can visualize the LAI by selecting the 
feature of interest, i.e., LAI, and 
plotting it. 
• If you prefer a text result file that 
has geometry and features, we can 
use another processor, 
Shapefile2GeoJSON. It converts a 
shapefile to a JSON file.

Final Results of mcd15-viz.yml workflow
•
/data/jobid/1 contains the nc4 file NASA input connector 
downloaded
•
/data/jobid/2 contains the Shapefiles. It stores geometric 
location and attribute information about geographic features 
like points, lines, and polygons.
•
/data/jobid/3 contains the final results, but has been moved 
to the geoedf/workflows/jobid/output

Processor Development
• Build a processor using NVIDIA HPC Container Maker 
• A Recipe file is needed to create a container (Docker or Singularity)
• HPC Container Maker can create both Docker and Singularity from the 
same recipe. 
• HPCCM is optional. You can still make a Docker container using a 
Dockerfile or a Singularity recipe. 
• Test a new Singularity container locally; if successful, push to the 
GeoEDF connector/processor repo.

What is HPCCM?
• HPCCM = HPC Container Maker
• It’s a Python-based tool that generates container recipes (for 
Singularity or Docker) using high-level, reusable Python building 
blocks.
Benefit
Description
Modularity
Use reusable blocks for common software (e.g., gdal(), openmpi())
Multiple Formats
Output both Dockerfile and Singularity recipes from the same source
Consistency
Ensures reproducible builds across formats and projects
Less Error-Prone
Fewer manual commands, easier to maintain
HPC-Ready
Includes building blocks for compilers, MPI, CUDA, etc., common in HPC 
environments

HPCCM Recipe 
•
It copies the 
files/shapefile2geojson 
directory to the Singularity 
image’s /shapefile2geoson 
directory.
 
•
Then, “pip3 install” installs our 
package to the container.
•
Now, users can execute 
Shapefile2GeoJSON by 
providing either parameter: 
•
input directory
•
shapefile name

Building Shapefile2GeoJSON Singularity Container
In this line:
• hpccm is a tool that auto-generates container definition files
• --format singularity means: "Generate a Singularity definition file 
(not Dockerfile, etc.)"
• > Singularity means: Save the output to a file literally named 
Singularity. “shapefile2geoson.def” could have been better naming.

Building Shapefile2GeoJSON Singularity Container
In this line:
• singularity is the command-line tool used to build and run containers
• build tells it to build a container image
• Shapefile2GeoJSON.sif is the output image file (the final container)
• Singularity is the input definition file (from the previous step)

GeoEDF documentation
https://geoedf.readthedocs.io/en/l
atest/index.html

Thank you!
Questions?
thompscs@purdue.edu
wooj@purdue.edu

GeoJSON
• JSON-based:
• GeoJSON leverages the simplicity and readability of JSON for representing 
geographic data.
• Geographic Features:
• It supports various geometry types, including points, line strings, polygons, and 
multi-part geometries like MultiPoint, MultiLineString, and MultiPolygon.
• Attributes:
• GeoJSON allows for the inclusion of non-spatial attributes (properties) associated 
with geographic features, providing additional context and information.
• Feature and FeatureCollection:
• Data is typically organized into "features," which represent individual geographic 
objects, and "feature collections," which group multiple features.
• Open Standard:
• GeoJSON is an open standard, meaning it's freely available for anyone to use and 
implement without licensing restrictions.

What is H09v07 tile?
 h09v07
This identifies the tile location in the MODIS Sinusoidal Tiling System, which covers 
the Earth in a global grid:
h09 = horizontal tile index 9
v07 = vertical tile index 7
Each tile covers ~10° × 10° at the equator (~1113 km × 1113 km).
So h09v07 refers to a specific region of Earth — for example:
 It includes parts of Indiana, Illinois, Ohio, and surrounding areas in the U.S.

OPeNDAP server: Comparison with Others 
Feature
OPeNDAP
HTTP/Web Server
FTP Server
Purpose
Remote access to subsets of 
structured scientific data
Serving files and webpages
File transfer
Data Access
Allows partial data extraction (e.g. 
specific variables, time slices, 
lat/lon ranges)
Usually downloads entire file
Transfers entire file
Protocol
Uses DAP (Data Access Protocol)
Uses HTTP/S
Uses FTP protocol
Query Support
 Can send structured queries 
for specific dimensions, variables, 
or ranges
 No native query support
 No query support
Output
Returns binary or structured 
(NetCDF/XML) response
Static file or HTML
Binary file
Client Libraries
Works with tools like xarray, 
netCDF4-python, MATLAB, IDL
General-purpose browsers or curl
FTP clients, shell
Efficiency
Highly efficient for large datasets 
(e.g., climate models, satellite 
rasters)
Inefficient for large data
Inefficient if only part of data is 
needed

### GeoEDF_tutorial_08012025.pdf
*Source file:* `GeoEDF_tutorial_08012025.pdf`  ·  *type:* pdf

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
Purdue University
08/04/2025

JS2 Aug 5 Maintenance
• This tutorial uses the JupyterHub running on the Jetstream2 cluster.
• JS2 will perform routine infrastructure maintenance from 7 am to 7 
p.m. on August 5. 
• https://jetstream-cloud.org/news-events/news/25-07-11_gpu-
maintenance.html
• During this maintenance, you will not be able to run notebooks in 
GeoEDF tutorials. 
2

EARTHDATA LOGIN Account required!
• If you have not created an EarthData 
account, create one before starting 
this tutorial
• https://urs.earthdata.nasa.gov/home
• Downloading the NASA DAAC MODIS 
dataset requires an account ID and a 
Password. 
• Without these, the GeoEDF NASA 
Input connector fails to download 
data.
3

Your GeoEDF Tutorials Are Available at
ohttps://tinyurl.com/ci4fair-geoedf
oOr, at the CyberFaces module: 
https://www.cyberfaces.org/learn/module/312-geoedf-workflow-framework-
application-highlights
o Use the provided username & password distributed today.
4

Cyberfaces.org 
• How to access 
CI4FAIR workshop
1. Go to Learn tab 
2. Take a course 
3. Cyberinfrastructure  
for FAIR Sciences
4. Start Now button
• All the slides are 
available at the 
CI4FAIR workshop.
5

GeoEDF Module
6

Overcoming the data wrangling challenge
7
5-year framework implementation project
Multidisciplinary collaboration: Hydrology, ABE, Ag econ, Water quality
Multi-modal dissemination
Image credits: By www.python.org - www.python.org, GPL, 
https://commons.wikimedia.org/w/index.php?curid=34991651
connectors + 
processors
workflow 
building 
blocks
YAML workflows
workflow 
engine

Some Examples of Participants’ Datasets
•
Atmospheric forcings Analysis of Record for 
Calibration (AORC), streamflow and 
evapotranspiration datasets 
•
Availability: The AORC dataset is hosted by 
NOAA on Amazon Web Services (AWS) and is 
available for download.
•
Interested in wrangling weather, climate, 
snow, and landcover datasets
•
Processing an extensive database of 
Unmanned Aerial Vehicles (UAV) remote 
sensing data for precision agriculture water 
management
•
Processors for disaster resilience and urban 
infrastructures
•
Processing map-based data, agricultural 
flooding in Arkansas, the Mississippi Delta 
region, surface water, and crop yield statistics 
datasets
•
Wildfire risk assessment 
•
Develop a new connector/processor for 
community weather data from LoRa sensors 
or instrument streams
8

Systems overview
• Will add a diagram explaining the physical locations of JS2, Anvil, 
Earthdata, Geddes, Cyberfaces, and users’ laptop.
9

GeoEDF Workflow
• A logical flow to run connectors 
and processors
• Users write a YAML file to specify 
the execution sequences
• The execution sequence: $1, $2, 
$3,…
• The output of the previous step 
can serve as the input to the next 
processor. 
• Colored terms are reserved 
keywords
• The Pegasus WMS system 
manages actual workflows. 
10

Edit your workflow file: mcd15.yml and mcd15-viz.yml
• Open mcd15.yml, and mcd15-viz.yml 
• Replace user and password with your Earthdata login ID/password
11
$1:
   Input:
         NASAInput:
      url: "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15A3H.061/%{filename}"
      user: your NASA Earthdata ID
      password: your NASA Earthdata Password
   
• Please make sure you are not using the example account “rkalyana”
• If you don’t provide a password here, you will be asked to type it in 
during Jupyter notebook run.

Now, Run the execute workflow cell
• WorkflowEngine.execute_workflow('/home/jovyan/CI4FAIR/workflow
/mcd15.yml','mcd’)
• If you have not typed in your password, it will ask for your password
• Please make sure you’re not using a dummy user id, 
• Add a screenshot here for Tutorial 1
12

GeoEDF Connectors
Download data for you.
• A class instance that searches for the data you want and 
downloads it.
• It does not use cached files.
Speed up data acquisition
• Suitable for frequently repeated downloading tasks
• Users select the data range (start date, end date) and frequency 
(daily, weekly, monthly, etc.).
• Download data faster ( parallel downloads)
Already exists! 
• Search for existing connectors before you write your own 
• You can revise the existing one to cater to new requirements
13

GeoEDF Connectors
• List of some of the popular connectors already available, what kind of 
data each handles
14

GeoEDF Processors
• A class/instance that computes something
• Does not have to use Connector outputs as input
• Can do any operations, such as
• Reproject, resample images,
• filter, clip/mask images,
• change formats, 
• Aggregate multiple datasets, e.g., compute 
averages, min, max value,
• Visualize data 
• Create new outputs
• An understanding of the input parameters of existing 
Processors is required.  
15

GeoEDF Processors
• List of some of the popular processors already available, summary 
of what operation they do
16

Hydrologic Use case: Creating a Greenness Map Using NASA Dataset
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l
•
Standard satellite images indicate the presence of green areas
•
MODIS LAI provides a scientific, quantitative measurement of vegetation density within those areas, making it 
much more helpful for ecological and environmental studies.
vs.

Leaf Area Index (LAI) : Greenness Index 
LAI is the ratio of total 
leaf area to ground 
area (dimensionless).
Example: LAI = 3 
means 3 m² of leaf 
surface per 1 m² of 
ground.
Ranges
Grasslands: ~0.5–2
Forests: ~3–9 
(depending on 
season and canopy 
type)
Weighted LAI
Summarizes the 
region’s vegetation 
status 
Meadow
https://pixabay.com/photos/landscape-agriculture-
meadow-hay-8060760/ 
Amazon rainforest canopy
https://pictures.butlernature.com/brazil/images/am
azon_200307.html 
https://metergroup.com/education-guides/the-researchers-complete-guide-to-leaf-area-index-lai/

Why Do Hydrologists Care About LAI? 
Spatial region of Interest:
The Wabash River in Indiana 
Hydrologists aim to develop 
this weighted LAI map.
Hydrologists use Leaf Area 
Index (LAI) because it’s a key 
variable linking vegetation to 
the water cycle — particularly 
in processes like
•
Evapotranspiration
•
Rainfall interception
•
Soil moisture and infiltration
•
Runoff & Streamflow Response.

GeoEDF workflow use case I 
Connect to NASA 
MODIS LAI 
dataset for a 
specific date
Download LAI dataset from NASA 
OPeNDAP Servers
Select the 
interested area, 
and find the LAI 
subdataset
Compute the average LAI for each 
subbasin defined in the given Shape 
file. Each subbasin has a single average 
LAI value. It generates an output Shape 
file.
Output: NetCDF file

Step 1: Download NASA MODIS LAI dataset 
• The MCD15A3H dataset, available through the USGS LP 
DAAC, is a MODIS product
• MODIS = an instrument (sensor)
• MODIS = Moderate Resolution Imaging 
Spectroradiometer
• It's mounted on two satellites: Terra and Aqua
• It collects raw radiance data (light 
reflected/emitted from Earth)
• MODIS data products = derived geophysical datasets
• These are not raw satellite images but gridded, pre-
processed data layers
Aqua satellite

The MCD15A3H dataset: LAI, FPAR
It combines data from both the Terra and Aqua 
MODIS sensors to generate a single, best-available 
pixel value for each 4 days.
For each pixel (i.e., location on Earth), the "best" 
observation from that 4-day window is selected. 
“Best” typically means:
•
Least cloud cover
•
Highest quality score
•
View angle closest to nadir
Global 4-day composite data for Leaf Area Index 
(LAI) and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter resolution.
Both variables are used to calculate surface 
photosynthesis, evapotranspiration, and net 
primary production, which in turn are used to 
calculate terrestrial energy, carbon, and water 
cycle processes, as well as the biogeochemistry of 
vegetation.
22

Connectors Abstract Away the Specifics of Connecting and Transferring Data
NASA OPeNDAP Servers: 
Open-source Project for a Network Data Access Protocol 
(OPeNDAP)
Data query
Check if a dataset exists on a specific date. If no data exists, a 
'Resource not found' (404) error page appears
Filtering
Since we are interested in Indiana, pick an HDF file that contains 
tiles covering Indiana ( h09v07)
Transfer
Choose a file extension (.nc4) to download
NASA input connector automates the implementation of a specific 
protocol (OPeNDAP) for the data query, filtering, and transfer.
Browse the list of available dates:
https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15
A3H.061/ 
You must be logged in to Earthdata.gov to access the OPeNDAP 
server.

Example Hydrologic Workflow
Apply GeoEDF principles

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
 The H09V07 grid identifier 
encompasses parts of Indiana, Illinois, 
Ohio, and surrounding areas in the U.S.
Corresponding GeoEDF Workflow

Looking into a NASA Connector’s Output
• Variables contained in a 
NC4 file 
• Dataset: whole NC4 file
• Subdataset: Fpar_500m, 
Lai_500m,…
• ‘Lai_500m' variable 
contains the Leaf Area Index 
for each pixel (500m x 
500m)
LAI quantifies the one-sided green leaf area per unit ground area, while FPAR measures the fraction of 
photosynthetically active radiation absorbed by a plant canopy.
Both variables are crucial inputs for models that estimate surface photosynthesis, evapotranspiration, and net 
primary production, contributing to the understanding of terrestrial energy, carbon, and water cycles.

Understanding Jupyter Notebooks
•
What is a Jupyter Notebook?
A Jupyter Notebook is an interactive digital notebook that 
lets you write and run code, see results instantly, and 
combine text, images, and charts — all in one place. 
Scientists, data analysts, and students widely use it.
•
How Does It Work?
•
You use a web browser to interact with the notebook 
(like visiting a website).
Behind the scenes, your code is sent to a Jupyter 
Server, which runs the code and sends the results back 
to your screen.
•
You can view outputs like numbers, graphs, maps, or 
tables — right below your code.
•
Key Features:
•
 Code + Text: Mix explanation and computation
•
 Live Code: Click “Run” to execute each cell
•
 Great for learning, exploring, and explaining ideas
•
 Works from any device with a browser — but runs 
on the server
27

Step 2: Read LAI Data, Aggregate them for Subbasins
• Module for aggregating the data values from an HDF file 
for a given shapefile containing polygons. 
• This supports both HDF4 and HDF5, but assumes that 
the files are in the HDF-EOS format. 
• All processing occurs in the latitude-longitude space by 
reprojecting the shapefile to WGS84 and extracting the 
lat-lon for each grid cell in the HDF file. 
• Extraction of cell lat-lon pairs for HDF4 files relies on the 
eos2dump utility. 
• This supports aggregating more than one subdataset 
from an HDF file.
• The resulting shapefile contains a separate field for each 
subdataset aggregate value

How Does the Processor Get Connector Data?
HDFEOSShapefileMask requires three parameters. 
1. HDFFile is the filename of the NASA input 
connector downloaded.
2. A shapefile defines the geometries of the 
subbasins of interest. LAI is calculated for each 
subbasin. 
3. Datasets: This is a list of subdatasets or variable 
names that the Processor looks for in the HDFFile. 
One of the subdatasets of the given HDFFile must 
have a variable containing “Lai”. In our case, the 
processor finds the “Lai_500m” variable has the 
substring “Lai”.

Final Results for mcd.yml workflow  
•
The HDFEOSShapefileMask  processor calculated weighted 
LAI for each subbasin (polygon). 
•
A shapefile, a standard vector data format in GIS, stores the 
location, shape, and attributes of geographic features.
•
It's not a single file, but a collection of related files, the most 
important being the .shp, .shx, and .dbf files.
•
The .shp file stores the feature geometry (points, lines, 
polygons).
•
The .shx file contains the index of the geometry. 
•
The .dbf file stores attribute data associated with each 
feature.
File browser shows /geoedf/workflows/jobid/output/

GeoEDF workflow use case II 
Connect to NASA 
MODIS LAI 
dataset for a 
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
composite data for Leaf Area Index (LAI) 
and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter 
resolution
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
GeoJSON

Step 3: Convert a Shapefile into a GeoJSON file 
• Once you have the shapefile, you 
can visualize the LAI by selecting the 
feature of interest, i.e., LAI, and 
plotting it. 
• If you prefer a text result file that 
has geometry and features, we can 
use another processor, 
Shapefile2GeoJSON. It converts a 
shapefile to a JSON file.

Final Results of mcd15-viz.yml workflow
•
/data/jobid/1 contains the nc4 file NASA input connector 
downloaded
•
/data/jobid/2 contains the Shapefiles. It stores geometric 
location and attribute information about geographic features 
like points, lines, and polygons.
•
/data/jobid/3 contains the final results, but has been moved 
to the geoedf/workflows/jobid/output

Processor Development
• Build a processor using NVIDIA HPC Container Maker 
• A Recipe file is needed to create a container (Docker or Singularity)
• HPC Container Maker can create both Docker and Singularity from the 
same recipe. 
• HPCCM is optional. You can still make a Docker container using a 
Dockerfile or a Singularity recipe. 
• Test a new Singularity container locally; if successful, push to the 
GeoEDF connector/processor repo.

What is HPCCM?
• HPCCM = HPC Container Maker
• It’s a Python-based tool that generates container recipes (for 
Singularity or Docker) using high-level, reusable Python building 
blocks.
Benefit
Description
Modularity
Use reusable blocks for common software (e.g., gdal(), openmpi())
Multiple Formats
Output both Dockerfile and Singularity recipes from the same source
Consistency
Ensures reproducible builds across formats and projects
Less Error-Prone
Fewer manual commands, easier to maintain
HPC-Ready
Includes building blocks for compilers, MPI, CUDA, etc., common in HPC 
environments

HPCCM Recipe 
•
It copies the 
files/shapefile2geojson 
directory to the Singularity 
image’s /shapefile2geoson 
directory.
 
•
Then, “pip3 install” installs our 
package to the container.
•
Now, users can execute 
Shapefile2GeoJSON by 
providing either parameter: 
•
input directory
•
shapefile name

Building Shapefile2GeoJSON Singularity Container
In this line:
• hpccm is a tool that auto-generates container definition files
• --format singularity means: "Generate a Singularity definition file 
(not Dockerfile, etc.)"
• > Singularity means: Save the output to a file literally named 
Singularity. “shapefile2geoson.def” could have been better naming.

Building Shapefile2GeoJSON Singularity Container
In this line:
• singularity is the command-line tool used to build and run containers
• build tells it to build a container image
• Shapefile2GeoJSON.sif is the output image file (the final container)
• Singularity is the input definition file (from the previous step)

GeoEDF documentation
https://geoedf.readthedocs.io/en/latest/index.html

GeoEDF is Open Source
40
•
Clone the repo and play with 
the code
•
You can contribute to the 
GeoEDF
•
Report issues
•
fix bugs
•
Add new 
connectors/processors. 
•
The GeoEDF paper and 
Presentation video at 
PEARC20 conference is 
available at 
https://dl.acm.org/doi/10.114
5/3311790.3396631
https://github.com/geoedf/

Thank you!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra slides
42

GeoJSON
• JSON-based:
• GeoJSON leverages the simplicity and readability of JSON for representing 
geographic data.
• Geographic Features:
• It supports various geometry types, including points, line strings, polygons, and 
multi-part geometries like MultiPoint, MultiLineString, and MultiPolygon.
• Attributes:
• GeoJSON allows for the inclusion of non-spatial attributes (properties) associated 
with geographic features, providing additional context and information.
• Feature and FeatureCollection:
• Data is typically organized into "features," which represent individual geographic 
objects, and "feature collections," which group multiple features.
• Open Standard:
• GeoJSON is an open standard, meaning it's freely available for anyone to use and 
implement without licensing restrictions.

What is H09v07 tile?
 h09v07
This identifies the tile location in the MODIS Sinusoidal Tiling System, which covers 
the Earth in a global grid:
h09 = horizontal tile index 9
v07 = vertical tile index 7
Each tile covers ~10° × 10° at the equator (~1113 km × 1113 km).
So h09v07 refers to a specific region of Earth — for example:
 It includes parts of Indiana, Illinois, Ohio, and surrounding areas in the U.S.

OPeNDAP server: Comparison with Others 
Feature
OPeNDAP
HTTP/Web Server
FTP Server
Purpose
Remote access to subsets of 
structured scientific data
Serving files and webpages
File transfer
Data Access
Allows partial data extraction (e.g. 
specific variables, time slices, 
lat/lon ranges)
Usually downloads entire file
Transfers entire file
Protocol
Uses DAP (Data Access Protocol)
Uses HTTP/S
Uses FTP protocol
Query Support
 Can send structured queries 
for specific dimensions, variables, 
or ranges
 No native query support
 No query support
Output
Returns binary or structured 
(NetCDF/XML) response
Static file or HTML
Binary file
Client Libraries
Works with tools like xarray, 
netCDF4-python, MATLAB, IDL
General-purpose browsers or curl
FTP clients, shell
Efficiency
Highly efficient for large datasets 
(e.g., climate models, satellite 
rasters)
Inefficient for large data
Inefficient if only part of data is 
needed

### GeoEDF_tutorial_08032025.pdf
*Source file:* `GeoEDF_tutorial_08032025.pdf`  ·  *type:* pdf

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
Purdue University
08/04/2025

Scheduled Maintenance Alert
• This tutorial runs on JupyterHub hosted on the Jetstream2 (JS2) cluster.
•
Scheduled Maintenance
Date: August 5
Time: 7:00 AM – 7:00 PM (local time)
Maintenance Details
•
Note: You will not be able to run notebooks from the GeoEDF tutorials 
during this time.
2

EARTHDATA Account Required!
• Before starting this tutorial, make sure 
you have an Earthdata account:
 
https://urs.earthdata.nasa.gov/home
• Accessing MODIS datasets from NASA 
DAAC requires your Earthdata username 
and password.
• Without valid credentials, the GeoEDF 
NASA Input Connector will fail to 
download the data.
3

Your GeoEDF Tutorials Are Available at
ohttps://tinyurl.com/ci4fair-geoedf
oOr, at the CyberFaces module: 
https://www.cyberfaces.org/learn/module/312-geoedf-
workflow-framework-application-highlights
o Log in to JupyterHub using the username and password 
provided today.
4

If You Don’t See CI4FAIR directory, do “git clone”
5
Getting Started with the Terminal
1. Open the Terminal
Click the Terminal icon on your JupyterLab interface.
2. Clone the Workshop Repository
Copy and paste the following command into the terminal: git clone https://github.com/geoedf/CI4FAIR 
3. Check the File Explorer
You will now see a new folder named CI4FAIR in the File Browser on the left side.

Cyberfaces.org 
• How to access the CI4FAIR 
workshop
1.
Go to the Learn tab 
2.
Select Take a course 
3.
Choose Cyberinfrastructure  for 
FAIR Sciences
4.
Click the Start Now button
• All workshop slides are available 
within the CI4FAIR course 
materials.
6

GeoEDF Module
7

Overcoming the data wrangling challenge
8
5-year framework implementation project
Multidisciplinary collaboration: Hydrology, ABE, Ag econ, Water quality
Multi-modal dissemination
Image credits: By www.python.org - www.python.org, GPL, 
https://commons.wikimedia.org/w/index.php?curid=34991651
connectors + 
processors
workflow 
building 
blocks
YAML workflows
workflow 
engine

Exploring Your Data: Use Cases & Workflows
•
Wrangling datasets related to:
•
Weather, climate, snow, and land cover
•
Large-scale processing of:
•
UAV-based remote sensing data for precision 
agriculture and water management
•
Workflow development for:
•
Disaster resilience and urban infrastructure 
monitoring
•
Analysis of map-based datasets:
•
Agricultural flooding in Arkansas and the 
Mississippi Delta
•
Surface water and crop yield statistics
•
Wildfire risk assessment using spatial and 
temporal indicators
•
Extending Capabilities
      Develop new connectors/processors for:
•
Community-collected weather data (e.g., 
LoRa sensors, instrument streams)
9

Architecture Behind the GeoEDF Tutorial Environment
10
8/3/2025
USER01
USER02
USER35
…

GeoEDF Workflow
Define Workflow Logic with YAML
• Specify the execution flow of connectors 
and processors using a YAML file.
• Use step references like $1, $2, $3, … to 
define the sequence.
• The output of one step can be used as the 
input to the next.
• Terms highlighted in color are reserved 
keywords.
• The Pegasus WMS (https://pegasus.isi.edu/) 
manages and executes the actual workflow 
behind the scenes.
11

Understanding Jupyter Notebooks
•
What is a Jupyter Notebook?
A Jupyter Notebook is an interactive digital notebook that lets 
you write and run code, see results instantly, and combine text, 
images, and charts — all in one place. Scientists, data analysts, 
and students widely use it.
•
How Does It Work?
•
You use a web browser to interact with the notebook (like 
visiting a website).
Behind the scenes, your code is sent to a Jupyter Server, 
which runs the code and sends the results back to your 
screen.
•
You can view outputs like numbers, graphs, maps, or tables 
— right below your code.
•
Key Features:
•
 Code + Text: Mix explanation and computation
•
 Live Code: Click “Run” to execute each cell
•
 Great for learning, exploring, and explaining ideas
•
 Works from any device with a browser — but runs on 
the server
12

Let’s Edit the Workflow File
• Replace the user and password fields in both mcd15.yml and mcd15-
viz.yml with your own NASA Earthdata login credentials.
13
$1:
   Input:
         NASAInput:
      url: "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15A3H.061/%{filename}"
      user: your NASA Earthdata ID
      password: your NASA Earthdata Password
   
Make sure you do not use the example account rkalyana.
After saving the YAML files:
• If the password is not specified in the file, you will be prompted to enter it 
when running the Jupyter notebook.

Time to Run a Workflow!
• Executing this cell will submit a job with the specified workflow.
• The current job name is mcd5000, and job names must be unique.
• For subsequent submissions, change mcd5000 to a different name, 
an arbitrary one.
14

GeoEDF Connectors
Automatically Download Data
• A class instance that searches for and downloads your 
requested data.
• Note: It does not use cached files—downloads are always 
fresh.
Accelerate Data Acquisition
• Ideal for tasks that involve frequent or repeated downloads.
• Specify your desired date range (start/end) and frequency 
(daily, weekly, monthly, etc.).
• Supports parallel downloading for faster data retrieval.
Ready-to-Use Connectors
• Before creating a new connector, check for existing ones.
• You can easily modify existing connectors to meet your 
specific needs.
15

Examples of GeoEDF Connector
 Flood Risk Analysis for U.S. Dams
Connector: GeoEDF.connector.input.DamFIMInput
Downloads: Flood inundation maps (TIFF) from USACE for a specified dam
 Documentation
 Agricultural Production & Sustainability
Connector: GeoEDF.connector.input.FAOInput
Downloads: U.N. FAOSTAT data for selected crops and products
 Documentation
 Hydrology and Vegetation Monitoring
Connector: GeoEDF.connector.input.NASAInput
Downloads: Data (e.g., Greenness Index) from NASA DAAC
 Documentation
16

GeoEDF Processors
• A class/instance that computes something
• Does not have to use Connector outputs as input
• Can do any operations, such as
• Reproject, resample images,
• filter, clip/mask images,
• change formats, 
• Aggregate multiple datasets, e.g., compute 
averages, min, max value,
• Visualize data 
• Create new outputs
• An understanding of the input parameters of existing 
Processors is required.  
17

Examples of GeoEDF Processor
 CSV to HAR (for GEMPACK)
Processor: GeoEDF.processor.CSV2HAR
Task: Converts a CSV (Comma-Separated Values) file into a HAR (Header Array) 
file, the standard input format for the GEMPACK economic modeling software.
 Documentation
 Aggregate HDF Data by Region
Processor: GeoEDF.processor.HDFEOSShapefileMask
Task: Aggregates values in an HDF file using spatial regions defined in a polygon 
shapefile (e.g., states, countries, watersheds).
 Documentation
 Run InVEST Models
Processor: GeoEDF.processor.InVESTModel
Task: Runs any InVEST ecosystem service model using the official model API.
 Documentation
18

Hydrologic Use Case: Creating a Greenness Map
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l
•
Standard satellite images indicate the presence of green areas
•
MODIS LAI provides a scientific, quantitative measurement of vegetation density within those areas, making it 
much more helpful for ecological and environmental studies.
vs.

Leaf Area Index (LAI) : Greenness Index 
LAI is the ratio of total 
leaf area to ground 
area (dimensionless).
Example: LAI = 3 
means 3 m² of leaf 
surface per 1 m² of 
ground.
Ranges
Grasslands: ~0.5–2
Forests: ~3–9 
(depending on 
season and canopy 
type)
Weighted LAI
Summarizes the 
region’s vegetation 
status 
Meadow
https://pixabay.com/photos/landscape-agriculture-
meadow-hay-8060760/ 
Amazon rainforest canopy
https://pictures.butlernature.com/brazil/images/am
azon_200307.html 
https://metergroup.com/education-guides/the-researchers-complete-guide-to-leaf-area-index-lai/

Why Do Hydrologists Care About LAI? 
Spatial region of Interest:
The Wabash River in Indiana 
Hydrologists aim to develop 
this weighted LAI map.
Hydrologists use Leaf Area 
Index (LAI) because it’s a key 
variable linking vegetation to 
the water cycle — particularly 
in processes like
•
Evapotranspiration
•
Rainfall interception
•
Soil moisture and infiltration
•
Runoff & Streamflow Response.

GeoEDF Workflow Use Case I 
Connect to NASA 
MODIS LAI 
dataset for a 
specific date
Download LAI dataset from NASA 
OPeNDAP Servers
Select the 
interested area, 
and find the LAI 
subdataset
Compute the average LAI for each 
subbasin defined in the given Shape 
file. Each subbasin has a single average 
LAI value. It generates an output Shape 
file.
Output: NetCDF file

Step 1: Download NASA MODIS LAI Dataset 
• The MCD15A3H dataset, available through the USGS 
LP DAAC, is a MODIS product
• MODIS = an instrument (sensor)
• MODIS = Moderate Resolution Imaging 
Spectroradiometer
• It's mounted on two satellites: Terra and Aqua
• It collects raw radiance data (light 
reflected/emitted from Earth)
• MODIS data products = derived geophysical datasets
• These are not raw satellite images but gridded, pre-
processed data layers
Aqua satellite

The MCD15A3H Dataset: LAI, FPAR
 MODIS 4-Day Composite (LAI & FPAR)
• Combines Terra & Aqua MODIS data to select the 
best-quality pixel every 4 days
• “Best” = minimal clouds, highest quality, nadir view
• Global coverage at 500m resolution
 Used for:
• Estimating photosynthesis, evapotranspiration, net 
primary production
• Modeling energy, carbon, and water cycles in 
ecosystems
24

Manual Weekly LAI Download Steps
To download weekly LAI data for a 
date range, you would need to:
1.
Log in to Earthdata
2.
Browse dates at: 
https://opendap.cr.usgs.gov/openda
p/hyrax/DP131/MOTA/MCD15A3H.0
61/
3.
Manually select the exact date 
for each week
4.
Choose the desired file format 
and download
5.
Repeat this for every week in 
your range
25

Connectors Simplify Data Access
Data query
Check if a dataset exists on a specific date. If no data exists, a 
'Resource not found' (404) error page appears
Filtering
Since we are interested in Indiana, pick an HDF file that contains 
tiles covering Indiana ( h09v07)
Transfer
Choose a file extension (.nc4) to download
The NASA input connector automates the implementation of a 
specific protocol (OPeNDAP) for the data query, filtering, and 
transfer.
Filter:
       Filename:
          PathFilter:
 
 pattern: 
"%{dtstring}/MCD15A3H.*.h09v07*.hdf"
      dtstring:
          DateTimeFilter:
        pattern: "%Y.%m.%d"
        start: "07/16/2002”
 
end: “12/24/2005”
        period: W
        exact_dates: true
This workflow downloads LAI data from 
07/16/2002 to 12/24/2005 for area h09v07, 
on a weekly basis.

Example Hydrologic Workflow
Apply GeoEDF principles

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
 The H09V07 grid identifier 
encompasses parts of Indiana, Illinois, 
Ohio, and surrounding areas in the U.S.
Corresponding GeoEDF Workflow

Looking Into a NASA Connector’s Output
• Variables contained in a 
NC4 file 
• Dataset: whole NC4 file
• Subdataset: Fpar_500m, 
Lai_500m,…
• ‘Lai_500m' variable 
contains the Leaf Area Index 
for each pixel (500m x 
500m)
LAI quantifies the one-sided green leaf area per unit ground area, while FPAR measures the fraction of 
photosynthetically active radiation absorbed by a plant canopy.
Both variables are crucial inputs for models that estimate surface photosynthesis, evapotranspiration, and net 
primary production, contributing to the understanding of terrestrial energy, carbon, and water cycles.

Step 2: Read LAI Data, Aggregate by Subbasins
This module aggregates data values from HDF files using a 
shapefile of polygonal subbasins.
• Supports both HDF4 and HDF5 in HDF-EOS format.
• Reprojects the shapefile to WGS84 and processes data 
in latitude-longitude space.
• Uses eos2dump utility to extract lat-lon coordinates 
from HDF4 files.
• Supports aggregation of multiple subdatasets from a 
single HDF file.
• Output shapefile includes a separate field for each 
aggregated subdataset.

How Does the Processor Get Connector Data?
 HDFEOSShapefileMask Parameters
This processor requires three parameters:
•
HDFFile: The filename of the HDF file 
downloaded by the NASA input 
connector.
•
Shapefile: Defines the subbasin 
geometries. LAI will be aggregated for 
each subbasin.
•
Datasets: A list of subdatasets or variable 
names to extract from the HDFFile.
At least one variable must include the 
substring "Lai".
Example: The processor identifies 
"Lai_500m" because it contains "Lai".

Workflow Output: mcd.yml
HDFEOSShapefileMask Processor Overview
•
Calculates weighted LAI for each subbasin (polygon) 
using a shapefile.
What is a Shapefile?
A shapefile is a common vector data format in GIS that 
stores the location, shape, and attributes of geographic 
features.
It consists of multiple files, typically including:
•
.shp — Stores the feature geometry (points, lines, 
polygons)
•
.shx — Index of the geometry
•
.dbf — Attribute data for each feature
All three are required for shapefile-based processing.
File browser shows /geoedf/workflows/jobid/output/

33
GeoEDF Workflow Use Case II: Tutorial_02

GeoEDF Workflow Use Case II 
Connect to NASA 
MODIS LAI 
dataset for a 
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
composite data for Leaf Area Index (LAI) 
and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter 
resolution
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
GeoJSON

Step 3: Convert a Shapefile into a GeoJSON File 
• Once you have the shapefile, you 
can visualize the LAI by selecting the 
feature of interest, i.e., LAI, and 
plotting it. 
• If you prefer a text result file that 
has geometry and features, we can 
use another processor, 
Shapefile2GeoJSON. It converts a 
shapefile to a JSON file.

Workflow Output: mcd15-viz.yml
•
/data/jobid/1 contains the NC4 file downloaded by the 
NASA input connector.
•
/data/jobid/2 contains the shapefiles, which define the 
geometry and attributes of geographic features (e.g., points, 
lines, and polygons).
•
/data/jobid/3 (presumably) contains the processed output 
after running the workflow. 
•
It has been moved to the /geoedf/workflows/jobid/output

Let’s Build a Singularity Container (Processor)
37
Here’s what the build-local-image.sh script does:
•
Navigates to the project directory containing the shapefile2geojson code and HPCCM recipe.
•
Generates a Singularity definition file (Singularity) from a recipe.hpccm using the HPCCM tool, 
targeting Singularity version 3.5.
•
Builds a Singularity container image named Shapefile2GeoJSON.sif using the generated 
definition file, with sudo since building requires root privileges.
•
Moves the final container image to the /images directory and deletes the intermediate 
Singularity file to clean up.

Processor Development
• Build a processor using NVIDIA HPC Container Maker 
• A Recipe file is needed to create a container (Docker or Singularity)
• HPC Container Maker can create both Docker and Singularity from the 
same recipe. 
• HPCCM is optional. You can still make a Docker container using a 
Dockerfile or a Singularity recipe. 
• Test a new Singularity container locally; if successful, push to the 
GeoEDF connector/processor repo.

What is HPCCM?
• HPCCM = HPC Container Maker
• It’s a Python-based tool that generates container recipes (for 
Singularity or Docker) using high-level, reusable Python building 
blocks.
Benefit
Description
Modularity
Use reusable blocks for common software (e.g., gdal(), openmpi())
Multiple Formats
Output both Dockerfile and Singularity recipes from the same source
Consistency
Ensures reproducible builds across formats and projects
Less Error-Prone
Fewer manual commands, easier to maintain
HPC-Ready
Includes building blocks for compilers, MPI, CUDA, etc., common in HPC 
environments

HPCCM Recipe 
HPCCM Recipe Overview for Shapefile2GeoJSON
•
The recipe copies the files/shapefile2geojson/ 
directory into the container at 
/shapefile2geojson.
•
It then installs the package using:
       pip3 install /shapefile2geojson 
•
After building the container, users can run 
Shapefile2GeoJSON by specifying:
•
An input directory, and
•
A shapefile name

Building Shapefile2GeoJSON Singularity Container
In this line:
• hpccm is a tool that auto-generates container definition files
• --format singularity means: "Generate a Singularity definition file 
(not Dockerfile, etc.)"
• > Singularity means: Save the output to a file literally named 
Singularity. “shapefile2geoson.def” could have been better naming.

Building Shapefile2GeoJSON Singularity Container
In this line:
• singularity is the command-line tool used to build and run containers
• build tells it to build a container image
• Shapefile2GeoJSON.sif is the output image file (the final container)
• Singularity is the input definition file (from the previous step)

GeoEDF documentation
https://geoedf.readthedocs.io/en/latest/index.html

GeoEDF is Open Source
44
 Get Involved with GeoEDF
•
Clone the repository and experiment with 
the code
•
Contribute by:
•
Reporting issues
•
Fixing bugs
•
Adding new connectors and processors
https://github.com/geoedf/

More webinar recordings about GeoEDF
• Learn more about GeoEDF through the PEARC20 conference paper 
and presentation
• I-GUIDE VCO: GeoEDF: A Framework for Designing and Executing 
Geospatial Research Workflows
45

Thank You!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra Slides
47

GeoJSON
• JSON-based:
• GeoJSON leverages the simplicity and readability of JSON for representing 
geographic data.
• Geographic Features:
• It supports various geometry types, including points, line strings, polygons, and 
multi-part geometries like MultiPoint, MultiLineString, and MultiPolygon.
• Attributes:
• GeoJSON allows for the inclusion of non-spatial attributes (properties) associated 
with geographic features, providing additional context and information.
• Feature and FeatureCollection:
• Data is typically organized into "features," which represent individual geographic 
objects, and "feature collections," which group multiple features.
• Open Standard:
• GeoJSON is an open standard, meaning it's freely available for anyone to use and 
implement without licensing restrictions.

What is H09v07 Tile?
 h09v07
This identifies the tile location in the MODIS Sinusoidal Tiling System, which covers 
the Earth in a global grid:
h09 = horizontal tile index 9
v07 = vertical tile index 7
Each tile covers ~10° × 10° at the equator (~1113 km × 1113 km).
So h09v07 refers to a specific region of Earth — for example:
 It includes parts of Indiana, Illinois, Ohio, and surrounding areas in the U.S.

OPeNDAP Server: Comparison with Others 
Feature
OPeNDAP
HTTP/Web Server
FTP Server
Purpose
Remote access to subsets of 
structured scientific data
Serving files and webpages
File transfer
Data Access
Allows partial data extraction (e.g. 
specific variables, time slices, 
lat/lon ranges)
Usually downloads entire file
Transfers entire file
Protocol
Uses DAP (Data Access Protocol)
Uses HTTP/S
Uses FTP protocol
Query Support
 Can send structured queries 
for specific dimensions, variables, 
or ranges
 No native query support
 No query support
Output
Returns binary or structured 
(NetCDF/XML) response
Static file or HTML
Binary file
Client Libraries
Works with tools like xarray, 
netCDF4-python, MATLAB, IDL
General-purpose browsers or curl
FTP clients, shell
Efficiency
Highly efficient for large datasets 
(e.g., climate models, satellite 
rasters)
Inefficient for large data
Inefficient if only part of data is 
needed

### GeoEDF_tutorial_08042025.pdf
*Source file:* `GeoEDF_tutorial_08042025.pdf`  ·  *type:* pdf

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
08/04/2025
Purdue Research Computing

Use case: Creating a Greenness Map using NASA dataset
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l
•
Standard satellite images indicate the presence of green areas
•
MODIS LAI provides a scientific, quantitative measurement of vegetation density within those areas, making 
it much more helpful for ecological and environmental studies.
vs.

Leaf Area Index (LAI) : Greenness Index 
https://metergroup.com/education-guides/the-
researchers-complete-guide-to-leaf-area-
index-lai/
LAI is the ratio of total leaf 
area to ground area 
(dimensionless).
Example: LAI = 3 means 3 m² 
of leaf surface per 1 m² of 
ground.
Ranges:
Grasslands: ~0.5–2
Forests: ~3–9 (depending on 
season and canopy type)
Unit: No unit (m²/m²)
https://metergroup.com/education-guides/the-
researchers-complete-guide-to-leaf-area-
index-lai/

Overall Greenness of the subbasins in the Upper Wabash River Watershed?
Our interested area
We want to create this weighted LAI map

GeoEDF workflow use case I 
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
subdataset
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
Output: netCDF file

Step 1: Download 
NASA 
MODIS LAI dataset 
•
The MCD15A3H dataset, available through theUSGS LP DAAC, is a 
MODIS product
•
MODIS = an instrument (sensor)
•
MODIS = Moderate Resolution Imaging Spectroradiometer
•
It's mounted on two satellites: Terra and Aqua
•
It collects raw radiance data (light reflected/emitted from Earth)
•
MODIS data products = derived geophysical datasets
•
NASA processes MODIS raw data into scientific "products" like:
•
LAI (Leaf Area Index) — MCD15A3H
•
NDVI (Vegetation index)
•
LST (Land Surface Temperature)
•
Snow cover
•
Fire products
•
These are not raw satellite images but gridded, pre-processed data 
layers
Aqua satellite

The MCD15A3H 
dataset
•
Global 4-day composite data for Leaf Area Index (LAI) and Fraction of 
Photosynthetically Active Radiation (FPAR) at a 500-meter resolution. It 
combines data from both the Terra and Aqua MODIS sensors to generate a 
single, best-available pixel value for each 4 days.
•
Key Details:
•
Product: MODIS/Terra+Aqua Leaf Area Index/FPAR 4-Day L4 Global 
500m
•
Temporal Resolution:4-day composite
•
Spatial Resolution: 500 meters. Each pixel covers 500 meters by 
500 meters.
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
production, as well as understanding terrestrial carbon, water, and 
energy cycles.

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
If your connector was successful, you will see the requested NC4 file was downloaded in  
/data/jobid/1/

NASA Panoply 
Data Viewer
• You can use this GUI 
software to view the 
variables contained in a 
.nc4 file. 
• Dataset: whole nc4 file
• Subdataset: Fpar_500m, 
Lai_500m,…
• We will use the 
‘Lai_500m' 
variable/subdataset only. 
LAI quantifies the one-sided green leaf area per unit ground area, while FPAR measures the 
fraction of photosynthetically active radiation absorbed by a plant canopy.
Both variables are crucial inputs for models that estimate surface photosynthesis, 
evapotranspiration, and net primary production, contributing to the understanding of terrestrial 
energy, carbon, and water cycles.

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

How Does the 
Processor Get 
Connector Data?
•
HDFEOSShapefileMask requires three 
parameters. 
1. HDFFile is the filename of the NASA input 
connector downloaded.
2. A shapefile designates a file that contains the 
area of interest for which we want to calculate 
the weighted average LAI.
3. Datasets: This is a list of subdatasets or 
variable names that the Processor looks for in the 
HDFFile. One of the subdatasets of the given 
HDFFile must have a variable containing “Lai”. In 
our case, the processor finds the “Lai_500m” 
variable has the substring “Lai”.

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
File explorer shows /geoedf/workflows/jobid/output/

GeoEDF workflow use case II 
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

GeoJSON
• JSON-based:
• GeoJSON leverages the simplicity and readability of JSON for representing geographic 
data.
• Geographic Features:
• It supports various geometry types, including points, line strings, polygons, and multi-
part geometries like MultiPoint, MultiLineString, and MultiPolygon.
• Attributes:
• GeoJSON allows for the inclusion of non-spatial attributes (properties) associated with 
geographic features, providing additional context and information.
• Feature and FeatureCollection:
• Data is typically organized into "features," which represent individual geographic objects, 
and "feature collections," which group multiple features.
• Open Standard:
• GeoJSON is an open standard, meaning it's freely available for anyone to use and 
implement without licensing restrictions.

Final Results 
of mcd15-
viz.yml 
workflow

Processor Development
• Build a processor using NVIDIA HPC Container Maker 
• TODO

### GeoEDF_tutorial_08042025.pdf
*Source file:* `GeoEDF_tutorial_08042025.pdf`  ·  *type:* pdf

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

### GeoEDF_tutorial_08042025.pdf
*Source file:* `GeoEDF_tutorial_08042025.pdf`  ·  *type:* pdf

GeoEDF Connector/Processor 
Tutorial
Christopher Thompson, Jungha Woo
Purdue University
08/04/2025

Scheduled Maintenance Alert
• This tutorial runs on JupyterHub hosted on the Jetstream2 (JS2) cluster.
•
Scheduled Maintenance
Date: August 5
Time: 7:00 AM – 7:00 PM (local time)
Maintenance Details
•
Note: You will not be able to run notebooks from the GeoEDF tutorials 
during this time.
2

EARTHDATA Account Required!
• Before starting this tutorial, make sure 
you have an Earthdata account:
 
https://urs.earthdata.nasa.gov/home
• Accessing MODIS datasets from NASA 
DAAC requires your Earthdata username 
and password.
• Without valid credentials, the GeoEDF 
NASA Input Connector will fail to 
download the data.
3

Your GeoEDF Tutorials Are Available at
ohttps://tinyurl.com/ci4fair-geoedf
oOr, at the CyberFaces module: 
https://www.cyberfaces.org/learn/module/312-geoedf-
workflow-framework-application-highlights
o Log in to JupyterHub using the username and password 
provided today.
4

If You Don’t See CI4FAIR directory, do “git clone”
5
Getting Started with the Terminal
1. Open the Terminal
Click the Terminal icon on your JupyterLab interface.
2. Clone the Workshop Repository
Copy and paste the following command into the terminal: git clone https://github.com/geoedf/CI4FAIR 
3. Check the File Explorer
You will now see a new folder named CI4FAIR in the File Browser on the left side.

Cyberfaces.org 
• How to access the CI4FAIR 
workshop
1.
Go to the Learn tab 
2.
Select Take a course 
3.
Choose Cyberinfrastructure  for 
FAIR Sciences
4.
Click the Start Now button
• All workshop slides are available 
within the CI4FAIR course 
materials.
6

GeoEDF Module
7

Overcoming the data wrangling challenge
8
5-year framework implementation project
Multidisciplinary collaboration: Hydrology, ABE, Ag econ, Water quality
Multi-modal dissemination
Image credits: By www.python.org - www.python.org, GPL, 
https://commons.wikimedia.org/w/index.php?curid=34991651
connectors + 
processors
workflow 
building 
blocks
YAML workflows
workflow 
engine

Exploring Your Data: Use Cases & Workflows
•
Wrangling datasets related to:
•
Weather, climate, snow, and land cover
•
Large-scale processing of:
•
UAV-based remote sensing data for precision 
agriculture and water management
•
Workflow development for:
•
Disaster resilience and urban infrastructure 
monitoring
•
Analysis of map-based datasets:
•
Agricultural flooding in Arkansas and the 
Mississippi Delta
•
Surface water and crop yield statistics
•
Wildfire risk assessment using spatial and 
temporal indicators
•
Extending Capabilities
      Develop new connectors/processors for:
•
Community-collected weather data (e.g., 
LoRa sensors, instrument streams)
9

Architecture Behind the GeoEDF Tutorial Environment
10
8/4/2025
USER01
USER02
USER35
…

GeoEDF Workflow
Define Workflow Logic with YAML
• Specify the execution flow of connectors 
and processors using a YAML file.
• Use step references like $1, $2, $3, … to 
define the sequence.
• The output of one step can be used as the 
input to the next.
• Terms highlighted in color are reserved 
keywords.
• The Pegasus WMS (https://pegasus.isi.edu/) 
manages and executes the actual workflow 
behind the scenes.
11

Understanding Jupyter Notebooks
•
What is a Jupyter Notebook?
A Jupyter Notebook is an interactive digital notebook that lets 
you write and run code, see results instantly, and combine text, 
images, and charts — all in one place. Scientists, data analysts, 
and students widely use it.
•
How Does It Work?
•
You use a web browser to interact with the notebook (like 
visiting a website).
Behind the scenes, your code is sent to a Jupyter Server, 
which runs the code and sends the results back to your 
screen.
•
You can view outputs like numbers, graphs, maps, or tables 
— right below your code.
•
Key Features:
•
 Code + Text: Mix explanation and computation
•
 Live Code: Click “Run” to execute each cell
•
 Great for learning, exploring, and explaining ideas
•
 Works from any device with a browser — but runs on 
the server
12

Let’s Edit the Workflow File
• Replace the user and password fields in both mcd15.yml and mcd15-
viz.yml with your own NASA Earthdata login credentials.
13
$1:
   Input:
         NASAInput:
      url: "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15A3H.061/%{filename}"
      user: your NASA Earthdata ID
      password: your NASA Earthdata Password
   
Make sure you do not use the example account rkalyana.
After saving the YAML files:
• If the password is not specified in the file, you will be prompted to enter it 
when running the Jupyter notebook.

Time to Run a Workflow!
• Executing this cell will submit a job with the specified workflow.
• The current job name is mcd5000, and job names must be unique.
• For subsequent submissions, change mcd5000 to a different name, 
an arbitrary one.
14

GeoEDF Connectors
Automatically Download Data
• A class instance that searches for and downloads your 
requested data.
• Note: It does not use cached files—downloads are always 
fresh.
Accelerate Data Acquisition
• Ideal for tasks that involve frequent or repeated downloads.
• Specify your desired date range (start/end) and frequency 
(daily, weekly, monthly, etc.).
• Supports parallel downloading for faster data retrieval.
Ready-to-Use Connectors
• Before creating a new connector, check for existing ones.
• You can easily modify existing connectors to meet your 
specific needs.
15
Parallel Processing

Examples of GeoEDF Connector
 Flood Risk Analysis for U.S. Dams
Connector: GeoEDF.connector.input.DamFIMInput
Downloads: Flood inundation maps (TIFF) from USACE for a specified dam
 Documentation
 Agricultural Production & Sustainability
Connector: GeoEDF.connector.input.FAOInput
Downloads: U.N. FAOSTAT data for selected crops and products
 Documentation
 Hydrology and Vegetation Monitoring
Connector: GeoEDF.connector.input.NASAInput
Downloads: Data (e.g., Greenness Index) from NASA DAAC
 Documentation
16

GeoEDF Processors
• A class/instance that computes something
• Does not have to use Connector outputs as input
• Can do any operations, such as
• Reproject, resample images,
• filter, clip/mask images,
• change formats, 
• Aggregate multiple datasets, e.g., compute 
averages, min, max value,
• Visualize data 
• Create new outputs
• An understanding of the input parameters of existing 
Processors is required.  
17

Examples of GeoEDF Processor
CSV to HAR (for GEMPACK)
Processor: GeoEDF.processor.CSV2HAR
Task: Converts a CSV (Comma-Separated Values) file into a HAR (Header Array) file, the 
standard input format for the GEMPACK economic modeling software.
 Documentation
Aggregate HDF Data by Region
Processor: GeoEDF.processor.HDFEOSShapefileMask
Task: Aggregates values in an HDF file using spatial regions defined in a polygon shapefile 
(e.g., states, countries, watersheds).
 Documentation
Run InVEST Models
Processor: GeoEDF.processor.InVESTModel
Task: Runs any InVEST ecosystem service model using the official model API.
 Documentation
18

Hydrologic Use Case: Creating a Greenness Map
NLDAS Vegetation Greenness Fraction
https://ldas.gsfc.nasa.gov/nldas/lai-greenness 
NASA Blue Marble Next Generation Map
https://visibleearth.nasa.gov/images/74092/july-blue-marble-next-generation/74094l
•
Standard satellite images indicate the presence of green areas
•
MODIS LAI provides a scientific, quantitative measurement of vegetation density within those areas, making it 
much more helpful for ecological and environmental studies.
vs.

Leaf Area Index (LAI) : Greenness Index 
LAI is the ratio of total 
leaf area to ground 
area (dimensionless).
Example: LAI = 3 
means 3 m² of leaf 
surface per 1 m² of 
ground.
Ranges
Grasslands: ~0.5–2
Forests: ~3–9 
(depending on 
season and canopy 
type)
Weighted LAI
Summarizes the 
region’s vegetation 
status 
Meadow
https://pixabay.com/photos/landscape-agriculture-
meadow-hay-8060760/ 
Amazon rainforest canopy
https://pictures.butlernature.com/brazil/images/am
azon_200307.html 
https://metergroup.com/education-guides/the-researchers-complete-guide-to-leaf-area-index-lai/

Why Do Hydrologists Care About LAI? 
Spatial region of Interest:
The Wabash River in Indiana 
Hydrologists aim to develop 
this weighted LAI map.
Hydrologists use Leaf Area 
Index (LAI) because it’s a key 
variable linking vegetation to 
the water cycle — particularly 
in processes like
•
Evapotranspiration
•
Rainfall interception
•
Soil moisture and infiltration
•
Runoff & Streamflow Response.

GeoEDF Workflow Use Case I 
Connect to NASA 
MODIS LAI 
dataset for a 
specific date
Download LAI dataset from NASA 
OPeNDAP Servers
Select the 
interested area, 
and find the LAI 
subdataset
Compute the average LAI for each 
subbasin defined in the given Shape 
file. Each subbasin has a single average 
LAI value. It generates an output Shape 
file.
Output: NetCDF file

Step 1: Download NASA MODIS LAI Dataset 
• The MCD15A3H dataset, available through the USGS LP 
DAAC, is a MODIS product
• MODIS = an instrument (sensor)
• MODIS = Moderate Resolution Imaging 
Spectroradiometer
• It's mounted on two satellites: Terra and Aqua
• It collects raw radiance data (light 
reflected/emitted from Earth)
• MODIS data products = derived geophysical datasets
• These are not raw satellite images but gridded, pre-
processed data layers
Aqua satellite

The MCD15A3H Dataset: LAI, FPAR
 MODIS 4-Day Composite (LAI & FPAR)
• Combines Terra & Aqua MODIS data to select the 
best-quality pixel every 4 days
• “Best” = minimal clouds, highest quality, nadir view
• Global coverage at 500m resolution
 Used for:
• Estimating photosynthesis, evapotranspiration, net 
primary production
• Modeling energy, carbon, and water cycles in 
ecosystems
24

Manual Weekly LAI Download Steps
To download weekly LAI data for a 
date range, you would need to:
1.
Log in to Earthdata
2.
Browse dates at: 
https://opendap.cr.usgs.gov/openda
p/hyrax/DP131/MOTA/MCD15A3H.0
61/
3.
Manually select the exact date for 
each week
4.
Choose the desired file format and 
download
5.
Repeat this for every week in your 
range
25

Connectors Simplify Data Access
Data query
Check if a dataset exists on a specific date. If no data exists, a 
'Resource not found' (404) error page appears
Filtering
Since we are interested in Indiana, pick an HDF file that contains 
tiles covering Indiana ( h09v07)
Transfer
Choose a file extension (.nc4) to download
The NASA input connector automates the implementation of a 
specific protocol (OPeNDAP) for the data query, filtering, and 
transfer.
Filter:
       Filename:
          PathFilter:
 
 pattern: 
"%{dtstring}/MCD15A3H.*.h09v07*.hdf"
      dtstring:
          DateTimeFilter:
        pattern: "%Y.%m.%d"
        start: "07/16/2002”
 
end: “12/24/2005”
        period: W
        exact_dates: true
This workflow downloads LAI data from 
07/16/2002 to 12/24/2005 for area h09v07, 
on a weekly basis.

Example Hydrologic Workflow
Apply GeoEDF principles

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
 The H09V07 grid identifier 
encompasses parts of Indiana, Illinois, 
Ohio, and surrounding areas in the U.S.
Corresponding GeoEDF Workflow

Looking Into a NASA Connector’s Output
Variables contained in a NC4 
file 
• Dataset: whole NC4 file
• Subdataset: Fpar_500m, 
Lai_500m,…
‘Lai_500m' variable contains 
the Leaf Area Index for each 
pixel (500m x 500m)
Our connector downloaded a .nc4 file, which is a NetCDF-4 format based on HDF5.
This means the file stores multidimensional scientific data (e.g., time, latitude, longitude, variables) in a 
structured, efficient, and self-describing format commonly used in Earth and environmental sciences.

Step 2: Read LAI Data, Aggregate by Subbasins
This module aggregates data values from HDF files using a 
shapefile of polygonal subbasins.
• Supports both HDF4 and HDF5 in HDF-EOS format.
• Reprojects the shapefile to WGS84 and processes data 
in latitude-longitude space.
• Uses eos2dump utility to extract lat-lon coordinates 
from HDF4 files.
• Supports aggregation of multiple subdatasets from a 
single HDF file.
• Output shapefile includes a separate field for each 
aggregated subdataset.

How Does the Processor Get Connector Data?
 HDFEOSShapefileMask Parameters
This processor requires three parameters:
•
HDFFile: The filename of the HDF file 
downloaded by the NASA input 
connector.
•
Shapefile: Defines the subbasin 
geometries. LAI will be aggregated for 
each subbasin.
•
Datasets: A list of subdatasets or variable 
names to extract from the HDFFile.
At least one variable must include the 
substring "Lai".
Example: The processor identifies 
"Lai_500m" because it contains "Lai".

Workflow Output: mcd.yml
HDFEOSShapefileMask Processor Overview
•
Calculates weighted LAI for each subbasin 
(polygon) using a shapefile.
What is a Shapefile?
A shapefile is a common vector data format in GIS 
that stores the location, shape, and attributes of 
geographic features.
It consists of multiple files, typically including:
•
.shp — Stores the feature geometry (points, 
lines, polygons)
•
.shx — Index of the geometry
•
.dbf — Attribute data for each feature
All three are required for shapefile-based 
processing.
File browser shows /geoedf/workflows/jobid/output/

33
GeoEDF Workflow Use Case II: Tutorial_02

GeoEDF Workflow Use Case II 
Connect to NASA 
MODIS LAI 
dataset for a 
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
composite data for Leaf Area Index (LAI) 
and Fraction of Photosynthetically Active 
Radiation (FPAR) at a 500-meter 
resolution
Compute the average LAI for each 
subbasin defined in the given Shape file. 
Each subbasin has a single average LAI 
value. It generates an output Shape file.
GeoJSON

Step 3: Convert a Shapefile into a GeoJSON File 
• Once you have the shapefile, you 
can visualize the LAI by selecting the 
feature of interest, i.e., LAI, and 
plotting it. 
• If you prefer a text result file that 
has geometry and features, we can 
use another processor, 
Shapefile2GeoJSON. It converts a 
shapefile to a JSON file.

Workflow Output: mcd15-viz.yml
•
/data/jobid/1 contains the NC4 file downloaded by the 
NASA input connector.
•
/data/jobid/2 contains the shapefiles, which define the 
geometry and attributes of geographic features (e.g., points, 
lines, and polygons).
•
/data/jobid/3 (presumably) contains the processed output 
after running the workflow. 
•
It has been moved to the /geoedf/workflows/jobid/output

Let’s Build a Singularity Container (Processor)
37
Here’s what the build-local-image.sh script does:
•
Navigates to the project directory containing the shapefile2geojson code and HPCCM recipe.
•
Generates a Singularity definition file (Singularity) from a recipe.hpccm using the HPCCM tool, 
targeting Singularity version 3.5.
•
Builds a Singularity container image named Shapefile2GeoJSON.sif using the generated 
definition file, with sudo since building requires root privileges.
•
Moves the final container image to the /images directory and deletes the intermediate 
Singularity file to clean up.

Verifying Your Singularity Container Build
If you successfully built a Singularity 
container, it will be saved in the 
/images directory.
•
 Note:
Due to JupyterLab’s sandboxing, some system 
directories like /images may not appear in the 
File Explorer.
 To verify:
1.
Open a Terminal.
2.
Run the following command to list 
the container: 
“ls /images”
3.
You should see the container file 
(e.g., Shapefile2GeoJSON.sif) listed 
there.
38

Processor Development with NVIDIA HPC Container Maker
Build Custom Processors for GeoEDF using Containers
• Write a recipe file to define software dependencies and environment 
settings.
• Use NVIDIA HPC Container Maker (HPCCM) to generate both Docker and 
Singularity containers from the same recipe — saving time and effort.
• HPCCM is optional — you can still use traditional Dockerfile or Singularity 
definition files.
• Test your container locally with Singularity.
• Once verified, push your containerized processor to the GeoEDF 
connector/processor repository for reuse.

What is HPCCM?
• HPCCM = HPC Container Maker
• It’s a Python-based tool that generates container recipes (for 
Singularity or Docker) using high-level, reusable Python building 
blocks.
Benefit
Description
Modularity
Use reusable blocks for common software (e.g., gdal(), openmpi())
Multiple Formats
Output both Dockerfile and Singularity recipes from the same source
Consistency
Ensures reproducible builds across formats and projects
Less Error-Prone
Fewer manual commands, easier to maintain
HPC-Ready
Includes building blocks for compilers, MPI, CUDA, etc., common in HPC 
environments

HPCCM Recipe 
HPCCM Recipe Overview for Shapefile2GeoJSON
•
The recipe copies the files/shapefile2geojson/ 
directory into the container at 
/shapefile2geojson.
•
It then installs the package using:
       pip3 install /shapefile2geojson 
•
After building the container, users can run 
Shapefile2GeoJSON by specifying:
•
An input directory, and
•
A shapefile name

Building Shapefile2GeoJSON Singularity Container
In this line:
• hpccm is a tool that auto-generates container definition files
• --format singularity means: "Generate a Singularity definition file 
(not Dockerfile, etc.)"
• > Singularity means: Save the output to a file literally named 
Singularity. “shapefile2geoson.def” could have been better naming.

Building Shapefile2GeoJSON Singularity Container
In this line:
• singularity is the command-line tool used to build and run containers
• build tells it to build a container image
• Shapefile2GeoJSON.sif is the output image file (the final container)
• Singularity is the input definition file (from the previous step)

GeoEDF documentation
https://geoedf.readthedocs.io/en/latest/index.html

GeoEDF is Open Source
45
 Get Involved with GeoEDF
•
Clone the repository and experiment with 
the code
•
Contribute by:
•
Reporting issues
•
Fixing bugs
•
Adding new connectors and processors
https://github.com/geoedf/

More webinar recordings about GeoEDF
• Learn more about GeoEDF through the PEARC20 conference paper 
and presentation
• I-GUIDE VCO: GeoEDF: A Framework for Designing and Executing 
Geospatial Research Workflows
46

Thank You!
Questions?
Chris Thompson
thompscs@purdue.edu
Jungha Woo
wooj@purdue.edu

Extra Slides
48

GeoJSON
• JSON-based:
• GeoJSON leverages the simplicity and readability of JSON for representing 
geographic data.
• Geographic Features:
• It supports various geometry types, including points, line strings, polygons, and 
multi-part geometries like MultiPoint, MultiLineString, and MultiPolygon.
• Attributes:
• GeoJSON allows for the inclusion of non-spatial attributes (properties) associated 
with geographic features, providing additional context and information.
• Feature and FeatureCollection:
• Data is typically organized into "features," which represent individual geographic 
objects, and "feature collections," which group multiple features.
• Open Standard:
• GeoJSON is an open standard, meaning it's freely available for anyone to use and 
implement without licensing restrictions.

What is H09v07 Tile?
 h09v07
This identifies the tile location in the MODIS Sinusoidal Tiling System, which covers 
the Earth in a global grid:
h09 = horizontal tile index 9
v07 = vertical tile index 7
Each tile covers ~10° × 10° at the equator (~1113 km × 1113 km).
So h09v07 refers to a specific region of Earth — for example:
 It includes parts of Indiana, Illinois, Ohio, and surrounding areas in the U.S.

OPeNDAP Server: Comparison with Others 
Feature
OPeNDAP
HTTP/Web Server
FTP Server
Purpose
Remote access to subsets of 
structured scientific data
Serving files and webpages
File transfer
Data Access
Allows partial data extraction (e.g. 
specific variables, time slices, 
lat/lon ranges)
Usually downloads entire file
Transfers entire file
Protocol
Uses DAP (Data Access Protocol)
Uses HTTP/S
Uses FTP protocol
Query Support
 Can send structured queries 
for specific dimensions, variables, 
or ranges
 No native query support
 No query support
Output
Returns binary or structured 
(NetCDF/XML) response
Static file or HTML
Binary file
Client Libraries
Works with tools like xarray, 
netCDF4-python, MATLAB, IDL
General-purpose browsers or curl
FTP clients, shell
Efficiency
Highly efficient for large datasets 
(e.g., climate models, satellite 
rasters)
Inefficient for large data
Inefficient if only part of data is 
needed
