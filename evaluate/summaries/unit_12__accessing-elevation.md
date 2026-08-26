---
title: "Accessing elevation data from National Elevation Dataset (NED)"
unit_id: 12
course_id: 4
level: "Developer"
slug: accessing-elevation
is_course: 0
---

# Accessing elevation data from National Elevation Dataset (NED)

Developer-level module (course "FAIR Climate and Water Science", Module DA3: Data Access (DA) for Water Science) on programmatically downloading Digital Elevation Model (DEM) tiles from the USGS National Elevation Dataset (NED), which provides seamless topographic coverage of the Continental United States (CONUS) as 1° × 1° latitude-longitude tiles. Prepared by Sayan Dey and Venkatesh Merwade (dey6@purdue.edu, vmerwade@purdue.edu), Lyles School of Civil Engineering, Purdue University.

Local resource: `DA3 Instruction for downloading NED tiles.pdf` — a tutorial requiring a mygeohub.org account (www.mygeohub.org), basic GIS (raster, shapefile) and Python knowledge. Data requirement: a single-feature polygon shapefile of the study area; example `Boundary.shp` (a Wabash River sub-watershed with outlet at West Lafayette, IN) is provided in the public folder `/srv/projects/cybertrainingfair/files/public/FAIR_Data_Access/NED_DEM_Download`. Uses QGIS via the PyQGIS Python API (PyQGIS Developer Cookbook at docs.qgis.org) inside a mygeohub Jupyter notebook with the [conda: qgis] kernel; starter notebook `init_NED_code.ipynb`.

Workflow: (1) initialize PyQGIS once per session (QgsApplication, QgsNativeAlgorithms, QT_QPA_PLATFORM=offscreen); (2) import Python libraries ftplib (FTP access), math, zipfile, shutil, and set input/work folder paths and boundary shapefile name; (3) user-defined functions DownloadNED(lat, lon) — connects to the NED FTP server rockyftp.cr.usgs.gov, navigates to vdelivery/Datasets/Staged/Elevation/1/ArcGrid/, finds zip files matching the tile name string "n<lat>w<long>" (e.g. n41w087 covers 40–41°N, 86–87°W), downloading the largest match via retrbinary — and UnzipNED(f) which extracts zips into the work folder; (4) determine required tiles by reprojecting the boundary polygon to NAD1983 / EPSG:4326 with processing.run('native:reprojectlayer', ...), loading it with QgsVectorLayer(..., 'ogr'), and reading layer.extent() attributes xMaximum, xMinimum, yMaximum, yMinimum; a bonus exercise derives tile lat/lon lists (e.g. list_long = [87,88]) with ceiling/floor and range(); (5) loop over latitude/longitude lists calling DownloadNED and UnzipNED for every overlapping tile, collecting raster names ("grdn<lat>w<lon>_1"); (6) optional qgs.exitQgis() cleanup. Downloaded tiles must later be mosaicked/reprojected in the Data Processing modules and visualized in the visualization module.

Also includes OCR text from `FAIR_data_principles.jpg` (FAIR: Findable, Accessible…) and the fetched exercise notebook `Coursepage_DA3_DEM_NED_Download_v2_Exercise.ipynb` from the GitHub repo PurdueCyberTraining/fairclimatewater (DA3-NED_Download folder), which contains the full PyQGIS initialization, inputs (example `B6_simplify.shp`), DownloadNED/UnzipNED code, and three exercises (print extents, build lat/lon lists, download loop).

## Summarized attachments
- **DA3 Instruction for downloading NED tiles** (DA3 Instruction for downloading NED tiles.pdf, file): Comprehensive tutorial by Sayan Dey and Venkatesh Merwade for programmatically downloading USGS National Elevation Dataset (NED) Digital Elevation Model tiles using PyQGIS and Python in a Jupyter notebook, covering PyQGIS initialization, library imports (ftplib, math, zipfile, shutil), user-defined functions for downloading and unzipping NED tiles from the USGS FTP server (rockyftp.cr.usgs.gov), determining overlapping tiles by reprojecting boundary shapefiles to NAD1983/EPSG:4326, extracting layer extents, and looping through latitude/longitude lists to download all required tiles for a study area.
