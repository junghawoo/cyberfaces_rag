---
title: "Processing NED data to create elevation dataset for a study area"
unit_id: 109
course_id: 4
level: "Expert"
slug: processing-ned
is_course: 0
---

# Processing NED data to create elevation dataset for a study area

Expert-level module from FAIR Climate and Water Science, Module DP6: Data Processing (DP) for Water Science — "Processing National Elevation Dataset (NED) tiles to Create Digital Elevation Model," prepared by Sayan Dey and Venkatesh Merwade, Lyles School of Civil Engineering, Purdue University (dey6@purdue.edu, vmerwade@purdue.edu).

**Local file:** `FAIR_DEM_Processing_With_Exercise.pdf`. **External resource:** Jupyter Notebook Exercise at https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP6/Coursepage_DP6_NED_DP_Markdown_Exercise.ipynb ("FAIR Science in Water Resources").

Objective: programmatically pre-process NED (National Elevation Dataset) DEM tiles — mosaicking (merging), reprojecting, and clipping to a study-area boundary — to build an elevation dataset for hydrologic/hydrodynamic modeling. Prerequisites: basic GIS file formats (raster, shapefile), Python, and ideally the prior Data Access (DA) module on downloading NED tiles. Requirements: web browser and account on www.mygeohub.org.

Data: (i) polygon shapefile Boundary.shp at read-only public server path /srv/projects/cybertrainingfair/files/public/FAIR_Data_Access/NED_DEM_Download; (ii) NED tiles at /srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/DEM_Processing (raster folders starting with "grd", e.g. grdn41w087_1, grdn41w088_1). Outputs go to the user's mygeohub home (/home/mygeohub/username).

Workflow uses the notebook DEM_NED_DP_Module_Exercise.ipynb with PyQGIS in Jupyter: initialize PyQGIS once per session (imports os/sys, sets QT_QPA_PLATFORM=offscreen, appends /opt/conda/envs/ct-fair/share/qgis/python, uses qgis.core, qgis.analysis QgsNativeAlgorithms, QgsApplication, processingRegistry). Steps: (1) define input/output paths; (2) build a list of "grd" rasters to merge; (3) merge tiles with the gdal:merge algorithm via processing.run('tool id', {parameters}) with INPUT/OUTPUT (5-8 minute runtime; produces GeoTIFF; QGIS 3.16 docs referenced); (4) reproject the merged raster with gdal:warpreproject (parameters INPUT, TARGET_CRS, OUTPUT), obtaining the target CRS from the boundary shapefile via QgsVectorLayer() and sourceCrs(); (5) clip with gdal:cliprasterbymasklayer (INPUT, MASK, OUTPUT) using the boundary polygon as mask; (6) verify results by plotting the final raster and boundary using geopandas (gpd.read_file), rasterio / rasterio.plot, and matplotlib.pyplot (raster in color gradient with red polygon boundary; details deferred to the Data Visualization module).

## Summarized attachments
- **Processing National Elevation Dataset (NED) tiles to Create Digital Elevation Model** (FAIR_DEM_Processing_With_Exercise.pdf, file): Comprehensive tutorial on programmatically pre-processing NED DEM tiles using PyQGIS. Prepared by Sayan Dey and Venkatesh Merwade from Purdue University. Details mosaicking (merging), reprojecting, and clipping processes using QGIS algorithms (gdal:merge, gdal:warpreproject, gdal:cliprasterbymasklayer), with example datasets (Boundary.shp and NED tiles grdn41w087_1, grdn41w088_1) and workflow steps including PyQGIS initialization, input/output path setup, creating raster lists, merging tiles (5-8 minute runtime), reprojecting to match boundary CRS, clipping to study area boundary, and verifying results through plotting.
- **Jupyter Notebook Exercise** (github.com/PurdueCyberTraining/fairclimatewater, notebook): Jupyter Notebook implementation of NED DEM processing workflow with PyQGIS code cells for initializing PyQGIS, defining folder/file paths, creating raster tile lists, merging tiles, reprojecting, clipping by mask layer, and visualizing final results with geopandas, rasterio, and matplotlib.
