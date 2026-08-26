---
title: "Geospatial & Hydrological Science: DEM Access and Visualization from USGS AWS [v09]"
unit_id: 277
course_id: 0
level: "Foundation"
slug: dem-access-and-visualization-from-usgs-aws
is_course: 0
---

# Geospatial & Hydrological Science: DEM Access and Visualization from USGS AWS [v09]

Jupyter Notebook-based tutorial for accessing and downloading Digital Elevation Models (DEMs) from USGS National Elevation Dataset via Amazon Web Service (AWS). Instructors: Jibin Joseph and Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University). Part of "Mini-Workshop: CyberTraining on Geospatial Data Processing using Python for Hydrology" offered via CyberFaCES platform (cyberfaces.org).

## Platform & Environment

Jupyter Notebook: JN-DEM Access (hosted on CyberFaCES Jupyter Hub). Kernel: ct-fair (conda environment with preinstalled packages). Login: CILogon (institutional credentials: Purdue, UIUC, etc.) or Google Account. Alternative reference documents: Instructions_DA3_DEM_Access_using_Shapefile_v09.pdf, Instructions_DA3_DEM_Access_v09.pdf, Instructions_DA3_DEM_Access_v09b.pdf, Instructions_DA3_DEM_Access_v10.pdf. External notebook: GitHub I-GUIDE/hydroewd repository (Coursepage_DA3_DEM_Access_v9a.ipynb).

## Objective & Workflow

Download DEM raster tiles from USGS-AWS for user-specified watersheds (defined by USGS streamflow gauge station numbers) and visualize alongside watershed shapefiles. Three-step overview: (1) Input USGS site number and DEM resolution; obtain shapefile; (2) Estimate bounding box extents; determine tile file names; (3) Download DEM rasters from USGS-AWS; plot unmerged tiles with shapefile.

## Data & Requirements

DEM Data Source: USGS Stage Products (https://prd-tnm.s3.amazonaws.com). Spatial resolutions available: 1 arc-second, 1/3 arc-second (code 13), 1/9 arc-second (code 19; currently unavailable). Coverage: Varies by location including Alaska, Hawaii, Puerto Rico.

Required Python packages: pynhd (access USGS Hydro Network-Linked Data Index/NLDI shapefile database), urllib (HTTP data download), progressbar (download progress tracking), rasterio (geospatial raster I/O and visualization), geopandas (vector data manipulation), shapely (geometric operations), numpy, matplotlib, folium (interactive mapping).

## Tutorial Steps

**Step 0 (Package Import)**: Import essential modules including numpy, geopandas, shapely, rasterio, pynhd, pygeohydro, urllib, progressbar, matplotlib. Version checks for reproducibility.

**Step 1a (USGS Site & Directory Setup)**: Input USGS site ID (e.g., 04180000: 270 sq mi, ~2-3 min download; 03335500: 7267 sq mi, longer). Use pynhd NLDI to fetch watershed shapefile. Alternative feature sources: nwissite (USGS NWIS Surface Water Sites), comid (NHDPlus), ca_gages (CA streamgages), gfv11_pois (USGS Geospatial Fabric V1.1 POIs), huc12pp (HUC12 Pour Points), nmwdi-st (New Mexico Water Data Initiative), nwisgw (NWIS Groundwater), ref_gage (geoconnex reference gages), vigil (Vigil Network), wade (Water Data Exchange 2.0), WQP (Water Quality Portal). Create directory structure: ~/scratch/DEM_Access/data_<site_id>/raw_<site_id>/. Includes helper function check_create_path_func() for directory creation.

**Step 1b (Watershed Visualization & Storage)**: Get site info via NWIS().get_info(). Transform watershed to Albers Equal Area projection (EPSG:5070) for area calculation in square miles. Create GeoDataFrame with station point (latitude/longitude from site_info). Plot watershed polygon with station marker. Save shapefile locally using watershed.to_file().

**Step 1c (Inset Map Creation)**: Load US boundary (cb_2018_us_conus_5m.shp) and HUC2 region shapefiles. Calculate watershed centroid. Use spatial join (gpd.sjoin) to identify HUC2 region. Create buffered bounding box polygon. Generate multi-panel visualization: main US map with HUC2 regions, zoomed inset showing watershed and site location.

**Step 2 (Extent Calculation)**: Extract bounding box using .total_bounds (left, bottom, right, top). Use math.floor/ceil to convert decimal coordinates to integer tile indices. USGS DEM naming scheme: 84W tile spans -84 to -83 deg; 40N includes +39 to +40 deg.

**Step 3 (DEM Tile Overlap Detection)**: Iterate latitude/longitude ranges; create rectangular polygon for each DEM tile. Use gpd.overlay() to find intersection with watershed. Append lon/lat pairs to overlap_lonlat list. Calculate total tiles in bounding region vs. tiles within watershed boundary.

**Step 4a (Sequential Download)**: Iterate overlap_lonlat list. Construct USGS filename format: n{lat:02d}w{lon:03d}. Build AWS URL: https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/{resolution}/TIFF/current/{filename}/USGS_{resolution}_{filename}.tif. Use urllib.request.urlretrieve() to download GeoTIFF files. Optional: progressbar integration (MyProgressBar() callback) for download tracking.

**Step 4b (Threaded/Parallel Download)**: Define download_dem_file_func() for individual tile downloads. Create threading.Thread objects for concurrent downloads. Thread.join() to synchronize completion. Compare sequential vs. parallel timing (typical speedup: 3x faster for multi-tile watersheds).

**Step 4c (Visualization)**: Open raster files using rasterio.open(). Plot using rasterio.plot functionality. Overlay watershed shapefile on DEM tiles using matplotlib. Title includes resolution metadata (1 arc-second, 1/3 arc-second, 1/9 arc-second).

## Example Datasets & Case Studies

Default example: USGS 03335000 (Wildcat Creek near Lafayette, IN; <1000 sq mi drainage area, recommended for limited resources). Driftwood River near Edinburgh (Indiana; 1062 sq mi). Challenge example: USGS 06186500 (Yellowstone River at Yellowstone Lake Outlet, YNP, Wyoming; demonstrates larger watersheds).

## Key Concepts & Outputs

Coordinate Reference Systems (CRS): EPSG:4326 (WGS84), EPSG:5070 (Albers Equal Area). Watershed shapefile format (.shp, .shx, .dbf). Output directory structure: input_<site_id> containing downloaded GeoTIFF tiles (USGS_{resolution}_{filename}.tif). Area calculations: 1 square meter = 0.386102 square miles. Raster file format: GeoTIFF (.tif).

## Learning Outcomes

Access remote USGS geospatial datasets programmatically. Delineate watersheds using USGS streamflow gauge identifiers. Calculate watershed extents and statistics. Download large raster datasets efficiently (sequential vs. threaded approaches). Visualize geospatial vector and raster data. Prepare DEM data for hydrological modeling (flood simulation, inundation mapping).

References: Hawker et al. 2018 (DEM perspectives for flood modeling); Saksena & Merwade 2015 (DEM resolution and accuracy for flood mapping); Chegini et al. 2021 (HyRiver: Hydroclimate Data Retriever, JOSS). Python documentation: urllib.request, Rasterio (MapBox).

## Summarized attachments

- **PDF-Instructions: DEM Access using Shapefile** (`Instructions_DA3_DEM_Access_using_Shapefile_v09.pdf`, file): Tutorial instructions prepared by Jibin Joseph and Venkatesh Merwade covering DEM access and visualization from USGS AWS. Introduces Digital Elevation Models, explains watershed delineation and topographic analysis, outlines three-step workflow: input USGS site number and get shapefile, estimate bounding box extents, download DEM rasters from USGS-AWS and plot with shapefile overlay. Specifies required packages (pynhd, urllib, progressbar, rasterio) and references USGS Stage Products.
- **PDF-Instructions: DEM Access v09** (`Instructions_DA3_DEM_Access_v09.pdf`, file): Version 9 tutorial instructions for DEM access and visualization from USGS AWS, containing equivalent content to the shapefile version with detailed workflow steps and Python package requirements.
- **AI_Co_Scientist_Report: DEM Access v09b** (`Instructions_DA3_DEM_Access_v09b.pdf`, file): Version 9b tutorial instructions covering DEM access and visualization from USGS AWS with details on watershed delineation, USGS NLDI database queries, and raster tile download/visualization procedures.
- **AI_Co_Scientist_Report: DEM Access v10** (`Instructions_DA3_DEM_Access_v10.pdf`, file): Version 10 tutorial instructions for DEM access from USGS-AWS, representing the latest iteration of the workflow documentation.
- **JN-DEM Access** (https://github.com/I-GUIDE/hydroewd/blob/2025_Miniworkshop/Coursepage_DA3_DEM_Access_v9a.ipynb, Jupyter notebook): Interactive notebook for DEM access and visualization. Covers importing required packages (pynhd, rasterio, folium, geopandas, urllib), inputting USGS site numbers, retrieving watershed shapefiles, calculating DEM tile extents, and downloading GeoTIFF raster tiles from USGS-AWS. Includes steps for sequential and threaded/parallel downloads for efficiency comparison, and plotting unmerged DEM tiles overlaid with watershed boundaries.
