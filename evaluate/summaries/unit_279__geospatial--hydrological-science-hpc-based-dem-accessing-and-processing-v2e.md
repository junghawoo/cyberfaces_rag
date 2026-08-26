---
title: "Geospatial & Hydrological Science: DEM Processing and Topographic Wetness Index (TWI) [v2e]"
unit_id: 279
course_id: 0
level: "Expert"
slug: geospatial--hydrological-science-hpc-based-dem-accessing-and-processing-v2e
is_course: 0
---

# Geospatial & Hydrological Science: DEM Processing and Topographic Wetness Index (TWI) [v2e]

This expert-level tutorial, prepared by Jibin Joseph and Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University), teaches Digital Elevation Model (DEM) processing and Topographic Wetness Index (TWI) generation for hydrological applications. The FAIR Science in Water Resources module covers complete DEM preprocessing and raster analysis using Python-based Jupyter Notebook within the CyberFaCES platform.

**Key Topics and Data Processing Steps:**
- DEM acquisition from USGS National Elevation Dataset in 1 arc-second, 1/3 arc-second, or 1/9 arc-second resolutions
- Merging/mosaicking of multiple DEM raster tiles using rasterio.merge function
- Reprojection from geographic coordinate system (EPSG:4326, WGS84) to projected coordinate system (UTM zones, EPSG:326xx series)
- Clipping rasters using shapefile masks to define watershed regions
- TWI generation using White Box Tools (WBT) geospatial algorithms

**Required Python Packages:** rasterio (raster operations: merging, reprojecting, masking), geopandas (shapefile handling), pyproj (coordinate system transformations), shapely (geometric clipping operations), pywbt (topographic wetness index), pynhd/pygeohydro (USGS data retrieval), matplotlib (visualization).

**Module Workflow:** Define variables (USGS site number, resolution, directories); plot unmerged raster tiles alongside watershed shapefile; merge overlapping DEM tiles; find appropriate UTM zone based on watershed centroid; reproject shapefile and raster to UTM; clip reprojected raster to study area with optional buffer; apply White Box Tools algorithms (BreachDepressions, D8Pointer, D8FlowAccumulation, Slope) to generate intermediate files; compute TWI using specific contributing area and slope raster. Example uses Cedar Creek watershed (USGS 03335000) and Yellowstone River (USGS 06186500).

**Prerequisites:** CyberFaCES platform login (institutional credentials, ORCID, or Google Account); ct-fair kernel with preinstalled modules. Material available on CyberFaCES platform within "Mini-Workshop: CyberTraining on Geospatial Data Processing using Python for Hydrology" and "I-GUIDE Forum 2025 Hands-on Tutorial" courses.

**Learning Objectives:** Merge raster tiles, transform coordinate systems, clip DEMs to study regions, generate topographic indices for hydrological analysis.

## Summarized attachments

- **Instructions_DP6_DEM_Process_TWI_v06.pdf** (`Instructions_DP6_DEM_Process_TWI_v06.pdf`, file): Detailed PDF instructions prepared by Jibin Joseph and Venkatesh Merwade (Purdue LSCE) for the DEM processing and Topographic Wetness Index generation tutorial, covering the complete workflow: merging DEM raster tiles, reprojecting from geographic to projected coordinate systems, clipping to watershed boundaries, and generating intermediate rasters (depression-filled DEM, flow direction, flow accumulation, slope) before computing TWI using White Box Tools. Includes specific USGS site examples (Cedar Creek 03335000, Yellowstone River 06186500) and detailed step-by-step visual instructions for the CyberFaCES platform.

- **Instructions_DP6_DEM_Process_TWI_v06b.pdf** (`Instructions_DP6_DEM_Process_TWI_v06b.pdf`, file): Updated version of the DEM processing instructions (duplicate variant with minor revisions) prepared by Joseph and Merwade for the I-GUIDE Forum 2025 Hands-on Tutorial course on CyberFaCES, maintaining the same pedagogical structure and examples as the prior version.

- **JN-DEM Processing and TWI** (https://github.com/I-GUIDE/hydroewd/blob/2025_Miniworkshop/Coursepage_DP6_DEM_Process_v2e.ipynb, Jupyter notebook): Interactive Python notebook hosted on GitHub containing executable code cells for merging DEM tiles via rasterio.merge, reprojecting to appropriate UTM zones using pyproj and rasterio.warp, clipping reprojected rasters using geopandas and shapely, and generating TWI through White Box Tools (BreachDepressions, D8Pointer, D8FlowAccumulation, Slope, WetnessIndex algorithms) with visualization of intermediate and final raster outputs.
