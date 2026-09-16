---
title: "test"
unit_id: 211
course_id: 0
level: "Foundation"
slug: test
is_course: 0
---

# test

Two Python tutorials for data processing: remote sensing fundamentals and DEM (Digital Elevation Model) access/processing workflows.

## Tutorial 1: Python Core Concepts for Remote Sensing Applications

**Authors:** Mohamed Abdelkader, Jorge Bravo, Marouane Temimi (Stevens Institute); Jibin Joseph (Purdue). **Source:** Introduction to Python_Core Concepts for RS Applications.pdf. **Topic:** FAIR Science in Climate. **Platform:** mygeohub.org, Jupyter Notebook, Anaconda 5.1.

**Learning Objectives:** Python syntax/structure, data types (integers, decimals, strings, lists, tuples, dictionaries), arithmetic operations, data manipulation, string formatting, control structures (loops, conditionals), collection iteration (crucial for satellite data processing).

**Content outline:** (1) Interactive environment; (2) Basic data types and remote sensing relevance; (3) Integer/decimal operations (measurements, calibrations); (4) String handling and annotation; (5) Lists, tuples, dictionaries (organizing/accessing sensor data); (6) Loops iterating through sequences (satellite data processing).

**Assignments:** Add new weather parameter (Solar Radiation, Visibility, etc.) to dictionary with hypothetical value; create f-string formatted output with dynamic data from dictionary; generate PDF with updated dictionary and message; submit Python script + readme documentation describing steps; naming convention: "Weather Data Analysis for [Parameter]".

**Resources:** Remote Sensing Tutorials, GOES-R Series Data Guide, GOES ABI (Advanced Baseline Imager) Realtime Imagery, GOES Image Viewer.

## Tutorial 2: HPC TOOL—DEM Accessing & Processing

**Authors:** Noah Oller Smith, Rajesh Kalyanam, Jibin Joseph, Venkatesh Merwade (Purdue). **Platform:** Jupyter Notebook, CyberGIS Compute (UIUC, cgjobsup.cigi.illinois.edu, HTTPS port 443). **Topic:** FAIR Science in Water Resources.

**Objective:** Access and process DEM data for larger watersheds at specified resolutions across CONUS (Continental US).

**Workflow (5 sequential steps):**

**Step 1:** Watershed_DEM_Raster_Connector—inputs site_id (e.g., '04180000'), resolution (e.g., '13' for 1/3 arc-second); downloads raster tiles covering watershed.

**Step 2:** DEM_Raster_Merging_Processor—merges multiple tiles into single raster (merged_resolution_site_id).

**Step 3:** DEM_Raster_Reprojection_Processor—reprojects merged raster and watershed shapefile to projected coordinate system.

**Step 4:** DEM_Raster_Clipping_Processor—clips reprojected raster to watershed boundary; **User interaction required:** Submit job, wait 2-3 min, download results locally (clipped_raster_{site_id}.tif).

**Step 5:** Visualization—display clipped raster using rasterio + matplotlib (viridis colormap).

**Libraries/Tools:** cybergis_compute_client (CyberGISCompute), rasterio (raster I/O), matplotlib.pyplot. **Output:** clipped_raster_{site_id}.tif (GeoTIFF format).

**Data resolution options:** 1 arc-second (~30m), 1/3 arc-second (~10m), per user needs.

**Workflow notes:** Each step generates job ID (jobid_dem_connector, jobid_dem_merge, jobid_dem_reproject) passed to subsequent steps; user must wait for job completion and download outputs before proceeding.

## Summarized attachments
- **Introduction to Python_Core Concepts for RS Applications** (Introduction to Python_Core Concepts for RS Applications.pdf, file): Tutorial by Mohamed Abdelkader, Jorge Bravo, Marouane Temimi (Stevens Institute), and Jibin Joseph (Purdue) on Python fundamentals for remote sensing applications including Python syntax and structure, data types (integers, decimals, strings, lists, tuples, dictionaries), arithmetic operations and data manipulation, string formatting, control structures (loops and conditionals), and iterating over data collections essential for satellite data processing, with resources on GOES-R satellite imagery, GOES ABI realtime data, and instructions for mygeohub Jupyter Notebook execution.
