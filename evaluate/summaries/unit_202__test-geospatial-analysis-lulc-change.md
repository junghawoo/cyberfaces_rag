---
title: "Test - Geospatial Analysis (LULC Change)"
unit_id: 202
course_id: 0
level: "Developer"
slug: test-geospatial-analysis-lulc-change
is_course: 0
---

# Test - Geospatial Analysis (LULC Change)

This unit contains geospatial analysis exercises for DEM (Digital Elevation Model) data access and LULC (Land Use/Land Cover) change analysis, prepared by Jibin Joseph and Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University) as part of FAIR Science in Water Resources.

## DEM Accessing using a Shapefile (Solution_DA3_DEM_Access_v2.ipynb and Coursepage_DA3_DEM_Access_v3.ipynb)

**Objective**: Download DEM raster files from USGS National Elevation Dataset using watershed shapefile extents obtained from USGS site numbers, then plot DEMs with watershed boundary overlays.

**Data Source**: USGS 1/3 arc-second DEM and 1 arc-second DEM (resolution options: code 13 for 1/3 arc-second, code 1 for 1 arc-second, code 19 for 1/9 arc-second currently unavailable).

**Workflow Overview**:
1. Using USGS Station Number: retrieve shapefile for basin/watershed and its spatial extents
2. Download DEM from USGS-Amazon Web Service (prd-tnm.s3.amazonaws.com)
3. Plot unmerged raster tiles with watershed boundary

**Python Libraries**: math, numpy, os, matplotlib.pyplot, pynhd (NLDI module), urllib.request, progressbar, rasterio, rasterio.plot

**Step-by-Step Implementation**:

Step 1a: Input USGS site ID and DEM resolution; create directory structure using check_create_path_func() function. Example sites: 09241000 (Elk River at Clark CO), 09037500 (Williams Fork near Parshall CO), 07103700 (Fountain Creek near Colorado Springs CO), 09064500 (Homestake Creek near Red Cliff CO), 04180000 (Cedar Creek). Folder naming: ./input_{site_id}.

Step 1b: Retrieve watershed using pynhd NLDI().get_basins(site_id) method; plot with facecolor, edgecolor parameters; save as ESRI Shapefile using .to_file() with driver='ESRI Shapefile', mode='w'. Example: shape_{site_id}.shp

Step 2: Extract basin extents using .total_bounds property; calculate bounding coordinates (left, right, bottom, top) using math.floor() and math.ceil() functions. DEM tile numbering scheme: n{lat:02d}w{lon:03d} format (e.g., n41w107, n41w108). Calculate number of tiles: (extent_left+1-extent_right) × (extent_top+1-extent_bottom). Example output: 2 tiles for site 09241000 with bounds West 107-108°, North 40-41°.

Step 3a: Download DEMs via loop over latitude/longitude ranges; construct USGS AWS URLs: https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif. Use urllib.request.urlretrieve() with custom MyProgressBar class for download progress tracking. Example downloads: USGS_13_n41w107.tif (380.7 MB, ~17s), USGS_13_n41w108.tif (401.5 MB, ~19s).

Step 3b: Plot unmerged raster tiles using matplotlib.subplots() with figsize=(8,8); open rasters with rasterio.open() and display using rasterio.plot.show() with cmap='viridis' (or 'magma'); overlay watershed shapefile with .plot(ax=ax, facecolor='none', edgecolor='red'). Coordinate labels: "Longitude (DD)" for x-axis, "Longitude (DD)" for y-axis (note: ylabel mislabeled as Longitude instead of Latitude in original).

**Associated Resources**: BlankPage.pdf (blank test document), GitHub repository at https://github.com/I-GUIDE/hydroewd/blob/main/Coursepage_DA3_DEM_Access_v3.ipynb

**Technical Notes**: Tile numbering scheme requires floor for left/bottom bounds (84W indicates -84 to -83°W), ceil for right/top bounds (40N includes +39 to +40°N); drainage area examples show 270 sq mi downloads in 2-3 minutes vs. 7267 sq mi requiring longer processing. Feature source options in pynhd: nwissite (default), comid, ca_gages, gfv11_pois, huc12pp, nmwdi-st, nwisgw, ref_gage, vigil, wade, WQP.

## Summarized attachments

- **BlankPage.pdf** (BlankPage.pdf, file): No machine-readable content extracted.

- **Solution_DA3_DEM_Access_v2.ipynb** (Solution_DA3_DEM_Access_v2.ipynb, Jupyter notebook): Tutorial for downloading DEM raster tiles from USGS-AWS using watershed shapefile extents obtained via USGS station numbers with the pynhd NLDI module, including tile counting and plotting unmerged tiles with watershed boundary overlays.

- **Coursepage_DA3_DEM_Access_v3.ipynb** (https://github.com/I-GUIDE/hydroewd/blob/main/Coursepage_DA3_DEM_Access_v3.ipynb, Jupyter notebook): GitHub notebook demonstrating the complete DEM data access workflow including USGS station number input, shapefile creation, extent extraction, USGS-AWS tile downloading with progress monitoring, and visualization of unmerged raster tiles.
