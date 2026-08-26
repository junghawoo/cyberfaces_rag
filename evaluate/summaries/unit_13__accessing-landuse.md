---
title: "Accessing landuse/landcover data from National Land Cover Database (NLCD)"
unit_id: 13
course_id: 4
level: "Developer"
slug: accessing-landuse
objectives:
  - ""
---

# Accessing landuse/landcover data from National Land Cover Database (NLCD)

Tutorial for downloading DEM (Digital Elevation Model) raster data from USGS National Elevation Dataset using watershed shapefile bounds, with visualization overlays.

**Authors:** Jibin Joseph and Venkatesh Merwade, Lyles School of Civil Engineering, Purdue University (joseph57@purdue.edu, vmerwade@purdue.edu). **Topic:** FAIR Science in Water Resources. **Source:** Coursepage_DA3_DEM_Access_v2.ipynb (GitHub: PurdueCyberTraining/fairclimatewater).

**Objective:** Download DEM raster files matching watershed extent using USGS site number; plot unmerged raster tiles with watershed boundary overlay. **Data source:** USGS 1/3 arc-second DEM.

## Three-Step Workflow

**Step 1a: Input Site and Setup**
- Input: USGS site number (e.g., "04180000" with 270 sq mi drainage area, downloadable in 2-3 min; or "03335500" with 7,267 sq mi, longer download)
- Input: DEM resolution (13 for 1/3 arc-second; 19 for 1/9 arc-second, unavailable)
- Create: Directory for storing input raster files

**Step 1b: Get Watershed Shapefile**
- Retrieve watershed from USGS site number via pynhd.NLDI
- Plot watershed boundary (facecolor='b', edgecolor='k')
- Save as shapefile

**Step 2: Calculate Extent Bounds**
- Use watershed.total_bounds to extract bounding box
- Calculate bounding extents using math.floor/ceil: (extent_left, extent_right, extent_bottom, extent_top)
- Determine number of tiles to download (typically 2-4 tiles for small-medium watersheds)
- Example output: Left=86, Right=85, Bottom=42, Top=42 → 2 tiles

**Step 3a: Download DEM Tiles from USGS-AWS**
- URL pattern: https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF/current/{usgs_filename}/USGS_{resolution}_{usgs_filename}.tif
- Filename convention: n{latitude:02d}w{longitude:03d} (e.g., n42w085)
- Download via urllib.request.urlretrieve() with progress bar monitoring
- Example: USGS_13_n42w085.tif (~419 MB, ~20 sec download)

**Step 3b: Plot Unmerged DEMs**
- Visualize each downloaded tile using rasterio.plot.show() with viridis colormap
- Overlay watershed boundary (facecolor='none', edgecolor='red') for context
- Display extent bounds in decimal degrees (DD)

## Libraries and Tools

**Python packages:** math, numpy, matplotlib.pyplot, pynhd (NLDI), urllib.request, progressbar, rasterio, rasterio.plot. **File format:** GeoTIFF (.tif).

**Key functions:** os.path.exists(), os.makedirs() (directory creation), watershed.plot(), watershed.total_bounds, math.floor(), math.ceil(), progressbar.ProgressBar, rasterio.open(), rasterio.plot.show().

**Output:** Individual DEM raster tiles with overlaid watershed shapefile, ready for merging and reprojection in subsequent modules.

## Summarized attachments
- **Jupyter Notebook Exercise** (https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA3-DEM_Access/Coursepage_DA3_DEM_Access_v2.ipynb, notebook): Interactive Jupyter notebook by Jibin Joseph and Venkatesh Merwade for downloading USGS National Elevation Dataset (NED) Digital Elevation Model raster tiles using watershed shapefile bounds, covering USGS site number input, DEM resolution selection (1/3 arc-second at 13, 1/9 arc-second at 19), watershed boundary retrieval via pynhd NLDI, extent calculation using math.floor/ceil, DEM tile download from USGS-AWS with progress tracking, and visualization of unmerged raster tiles overlaid with watershed boundaries using rasterio and matplotlib.
