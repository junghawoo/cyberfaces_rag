---
title: "test course1"
unit_id: 198
course_id: 0
level: "Foundation"
slug: test-course1
is_course: 1
---

# test course1

## Summary

Test/foundation course module bundling two hydrology-geospatial Jupyter notebooks on Digital Elevation Model (DEM) workflows, prepared by Jibin Joseph and Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University; joseph57@purdue.edu, vmerwade@purdue.edu) under the "FAIR Science in Water Resources" initiative.

Extracted local file `Solution_DP6_DEM_Processing_v2.ipynb` (DEM Processing) teaches merging, projecting, and clipping DEM raster files sourced from the USGS 1/3 arc-second National Elevation Dataset (downloaded in a prior DEM Downloading module). Four steps: (1) read and plot original files; (2) merge/mosaic tiles; (3) reproject/transform from Geographic (GCS) to Projected Coordinate System (PCS); (4) clip/mask using a watershed shapefile. Imports: math, matplotlib.pyplot, os, pynhd (NLDI), rasterio, rasterio.plot, geopandas, rasterio.merge.merge, rasterio.warp (calculate_default_transform, reproject, Resampling), pyproj, rasterio.mask.mask, shapely.geometry.mapping (versions rasterio 1.3.8, geopandas 0.13.0, pyproj 3.6.0). Uses USGS sites 04180000 and 03343000 (Wabash River at Vincennes, IN — 13907 sq mi). Defines helper functions check_create_path_func, merge_dem_raster_func, reproject_raster_func, clip_raster_with_shapefile_func. Computes UTM zone from watershed centroid to build EPSG:326## CRS strings (conterminous US zone logic), plus estimate_utm_crs(datum_name='WGS 84'). Creates input/intermediate/results folders and writes merged, reprojected, and clipped GeoTIFFs plus a projected ESRI Shapefile; plots elevation rasters with viridis colormap and colorbars in DD and Easting/Northing (meters).

Fetched external resources: a placeholder "Testing" link (https://google.com, Google landing text) and "test123" notebook (https://github.com/I-GUIDE/hydroewd/blob/main/Coursepage_DA3_DEM_Access_v3.ipynb) titled "DEM Accessing using a Shapefile." That notebook downloads DEM raster tiles from the USGS-Amazon Web Service (prd-tnm.s3.amazonaws.com StagedProducts/Elevation TIFF) using watershed shapefile extents fetched via USGS station number through the pynhd NLDI module, using math floor/ceil to compute tile counts (n{lat}w{lon} naming), a MyProgressBar class with progressbar/urllib.request for download monitoring, and rasterio for plotting unmerged tiles with the watershed boundary. Notes NLDI feature sources: nwissite, comid, ca_gages, gfv11_pois, huc12pp, nmwdi-st, nwisgw, ref_gage, vigil, wade, WQP. Example site 04180000 = Cedar Creek (270 sq mi); 03335500 = 7267 sq mi. Resolution codes: 1 arc-second (1), 1/3 arc-second (13), 1/9 arc-second (19, unavailable).

## Summarized attachments

- **Solution_DP6_DEM_Processing_v2.ipynb** (Solution_DP6_DEM_Processing_v2.ipynb, Jupyter notebook): Tutorial on DEM raster processing including merging multiple tiles, reprojecting from geographic to projected coordinate systems using UTM zones, and clipping to watershed boundaries using geopandas and rasterio with visualization examples.

- **Testing** (https://google.com, remote resource): No machine-readable content extracted.

- **test123** (https://github.com/I-GUIDE/hydroewd/blob/main/Coursepage_DA3_DEM_Access_v3.ipynb, Jupyter notebook): GitHub notebook for downloading DEM raster tiles from USGS-AWS using watershed shapefile extents obtained via USGS station numbers with the pynhd NLDI module, including tile counting, progress-bar download monitoring, and unmerged tile visualization with watershed boundary overlays.
