---
title: "Unit 366"
unit_id: 366
---

# Unit 366

Interactive Jupyter Notebook tutorial on Digital Elevation Model (DEM) processing and Topographic Wetness Index (TWI) generation, prepared by Jibin Joseph and Venkatesh Merwade (Lyles School of Civil and Construction Engineering, Purdue University, joseph57@purdue.edu, vmerwade@purdue.edu) under FAIR Science in Water Resources framework.

**Learning Objective:** Tutorial teaches merging, projecting, clipping DEM raster files, and generating TWI raster datasets using downloaded USGS National Elevation Dataset DEM raster files from previous DEM Downloading module. USGS-DEM available in 1 arc-second, 1/3 arc-second, or 1/9 arc-second spatial resolutions.

**Required Python Packages & Modules:**
math, matplotlib.pyplot, os, pynhd (PyNHD version tracking), pygeohydro (NWIS for site information), rasterio (raster.plot, raster.merge.merge, raster.warp.calculate_default_transform/reproject/Resampling), geopandas (shapefile reading), rasterio.mask.mask, shapely.geometry.mapping/Polygon, pathlib.Path, tempfile, pywbt (White Box Tools), numpy, pyproj.CRS.

**Processing Workflow Steps:**

1. **Read/Plot Unmerged Files:** Define USGS site ID, resolution, directory paths. Load watershed shapefile via geopandas.read_file(). Retrieve NWIS site information. Calculate tile extent bounds. Create rectangular boundary polygons to identify tiles overlapping watershed. Plot unmerged raster files (USGS_{resolution}_{usgs_filename}.tif) using rasterio.plot.show() with viridis colormap alongside watershed boundary.

2. **Merge Rasters:** Create folder_process, folder_intermediate, folder_results directories. Define merge_dem_raster_func() using rasterio.merge.merge(datasets, resampling=Resampling.nearest, method='first', target_aligned_pixels=False). Copy metadata from first dataset, update height/width/transform, write merged raster using rasterio.open() in write mode.

3. **Reproject to Projected Coordinate System:** Identify appropriate UTM zone based on watershed centroid location (latitude/longitude). Calculate zone for conterminous US (-138 to -54 longitude, zones 8-22). Estimate UTM CRS using watershed.estimate_utm_crs(datum_name='WGS 84'). Reproject watershed shapefile to UTM using to_crs() method. Reproject merged raster via reproject_raster_func() with calculate_default_transform() for new dimensions, rasterio.warp.reproject() for band-by-band transformation.

4. **Clip Raster:** Use clip_raster_with_shapefile_func() with rasterio.mask.mask() to extract raster values within reprojected shapefile geometry, optionally buffered. Update metadata (height, width, transform) and write clipped raster.

5. **Generate TWI:** White Box Tools (WBT) algorithms applied sequentially: BreachDepressions (fill depressions), D8Pointer (flow direction, D8 algorithm), DownslopeFlowpathLength, D8FlowAccumulation (specific contributing area), Slope (degrees), WetnessIndex. Output files: dem_corr, fdir, downslope_fp_length, sca, slope, twi raster files with site_id and resolution suffixes.

**Visualization:** Create figure subplots (2x3 layout) showing Clipped DEM, Breach Depressions Filled Raster, D8 Flow Direction Raster (index 1-128), Slope Raster (degrees), Flow Accumulation/Specific Contributing Area Raster (cells/meter), TWI Raster (dimensionless), overlaid with reprojected watershed shapefile boundary (white edge, 5 pt linewidth). Colorbars labeled with appropriate units. 98th percentile-clipped visualization for each dataset.

**Key Coordinate Systems:** EPSG:4326 (WGS84, geographic), EPSG:326xx (UTM projected zones based on centroid).

**Example Watershed:** Cedar Creek (site_id 03335000); alternative: Yellowstone River at Yellowstone Lake Outlet, YNP, WY (USGS 06186500).

## Summarized attachments

- **DEM Processing and Topographic Wetness Index Tutorial** (`Coursepage_DP6_DEM_Process_v3.ipynb`, Jupyter notebook): Interactive Python tutorial by Jibin Joseph and Venkatesh Merwade (Purdue Lyles School) demonstrating DEM raster merging, reprojection to projected coordinate systems, clipping with watershed boundaries, and TWI generation using White Box Tools, with visualization of processed DEMs, flow directions, slopes, and wetness indices for watershed analysis.
