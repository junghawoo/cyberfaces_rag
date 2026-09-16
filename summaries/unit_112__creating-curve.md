---
title: "Creating curve number (CN) grid from landuse and soil data"
unit_id: 112
course_id: 4
level: "Developer"
slug: creating-curve
---

# Creating curve number (CN) grid from landuse and soil data

Geospatial hydrological modeling module creating Curve Number grids for precipitation-runoff partitioning using PyQGIS, QGIS, and geospatial data integration.

**Authors:** Sayan Dey and Venkatesh Merwade, Lyles School of Civil Engineering, Purdue University. **Topic:** FAIR Climate and Water Science. **Source:** CN_Grid_Creation_Instructions.pdf; **Jupyter Notebook:** CN_Grid_Markdown_Exercise.ipynb (GitHub: PurdueCyberTraining/fairclimatewater).

## Curve Number Overview and Methodology

Curve Number (CN) partitions precipitation into runoff based on landuse and soil properties via lookup table assignment. Three-step process: (1) reclassify National Land Cover Dataset (NLCD) raster; (2) create soil raster from gSSURGO (gridded Soil Survey Geographic) vector data; (3) combine soil and landuse using lookup table to calculate CN.

## Input Data and File Formats

**Data location:** /srv/projects/cybertrainingfair/files/public/FAIR_Data_Processing/CN_Grid

**Input files:** Boundary.shp (watershed boundary polygon shapefile); Soil.shp (gSSURGO polygon shapefile with HSG_Index field: 1=HSG A, 2=HSG B, 3=HSG C, 4=HSG D; merged A/D, B/D, C/D with A, B, C); LU.tif (GeoTIFF, NLCD data, integer raster, values 11-95); LookUp.csv (CN values for soil-landuse combinations); NLCD_reclass.csv (reclassification rules with min/max ranges and output values). Coordinate system: EPSG:26917.

## QGIS Processing Steps

**Jupyter environment:** Python kernel [conda env:qgis], mygeohub. **PyQGIS initialization:** imports os, sys; sets QT_QPA_PLATFORM='offscreen'; imports QgsApplication, QgsNativeAlgorithms, processing module; initializes qgs application.

**Landuse Reclassification:** Uses native:reclassifybylayer tool with processing.run(); inputs include INPUT_RASTER (LU.tif), RASTER_BAND (1), INPUT_TABLE (NLCD_reclass.csv as QgsVectorLayer), MIN_FIELD, MAX_FIELD, VALUE_FIELD parameters; output: lu_reclass_raster.tif (~36MB). Reclassifies NLCD categories (11-95) into four classes: Water (1), Medium Residential (2), Forest (3), Agricultural (4).

**Soil Rasterization:** Converts polygon shapefile to raster using gdal:rasterize; matches landuse raster extent and resolution. Extracts bounds (west/east/south/north, CRS) from landuse raster. Gets rasterUnitsPerPixelX/Y for pixel dimensions. Arguments: INPUT (Soil.shp), FIELD (HSG_Index), UNITS (1), WIDTH/HEIGHT (pixel size), EXTENT (bounds expression), NODATA (0), DATA_TYPE (5); output: soil_raster.tif (~36MB).

**CN Grid Calculation:** Uses gdal:rastercalculator combining reclassified landuse (A) and soil (B) rasters. Formula applies lookup table via logical_and() conditions: e.g., '100*(A==1) + 57*logical_and(A==2,B==1) + ...' assigning unique CN values to each soil-landuse pair combination. Outputs: CN_grid.tif (~36MB).

## Visualization and Validation

Plotting code uses matplotlib.pyplot, rasterio, rasterio.plot; generates images for reclassified landuse, soil raster, and final CN grid outputs.

**Additional tools:** pandas, geopandas, QgsVectorLayer, os.path.join(), os.path.isdir(), os.mkdir().

## Summarized attachments
- **Creating Curve Number Grid from soil and landuse using PyQGIS** (CN_Grid_Creation_Instructions.pdf, file): Tutorial document by Sayan Dey and Venkatesh Merwade on curve number grid creation through three-step process: reclassifying National Land Cover Dataset (NLCD) raster, converting gSSURGO polygon shapefile to soil raster, and combining landuse/soil rasters using lookup table to calculate CN values for precipitation-runoff partitioning in hydrological modeling.
- **Jupyter Notebook** (GitHub: PurdueCyberTraining/fairclimatewater, notebook): Interactive notebook CN_Grid_Markdown_Exercise.ipynb implementing PyQGIS-based curve number grid creation with watershed boundary shapefile input, landuse and soil data processing, reclassification and rasterization procedures, and CN grid calculation using QGIS processing tools and gdal raster calculator.
