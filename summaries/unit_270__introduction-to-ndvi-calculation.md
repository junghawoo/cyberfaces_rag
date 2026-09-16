---
title: "Introduction to NDVI Calculation"
unit_id: 270
course_id: 0
level: "Foundation"
slug: introduction-to-ndvi-calculation
is_course: 0
---

# Introduction to NDVI Calculation

Tutorial on calculating Normalized Difference Vegetation Index (NDVI) from multispectral imagery. Jupyter Notebook: https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Introduction%20to%20NDVI%20Calculation.ipynb.

NDVI definition: Quantitative greenness index (0-1 scale); 0=minimal/no greenness, 1=maximum greenness. Applications: vegetation health, cover, phenology (life cycle) assessment over large areas. Calculation basis: visible and near-infrared light reflection. Healthy vegetation: absorbs visible light, reflects near-infrared. Unhealthy/sparse vegetation: reflects more visible, less near-infrared.

R libraries: raster (spatial data), rgdal (I/O), rgeos (geometry), RColorBrewer (color palettes).

Data example: NAIP multispectral data (pre-fire Cold Springs Fire Site, Nederland, CO, 2013). File: m_3910505_nw_13_1_20130926_crop.tif.

GIS metadata: RasterLayer (2312 rows × 4377 cols = 10,119,624 cells), 1m×1m resolution, extent (457163, 461540, 4424640, 4426952 UTM zone 13), values 0-255, CRS: UTM zone 13 (GRS80 ellipsoid).

NDVI calculation: Formula = (NIR - Red) / (NIR + Red); uses band 4 (near-infrared), band 1 (red). R code: naip_ndvi <- (naip_multispectral_br[[4]] - naip_multispectral_br[[1]]) / (naip_multispectral_br[[4]] + naip_multispectral_br[[1]]).

Processing workflow: Load multispectral TIFF, convert stack to rasterbrick (faster), calculate NDVI via band ratio, plot visualization.

Visualization: plot(naip_ndvi) with title, no axes/box; hist(naip_ndvi) shows pixel distribution for temporal change analysis.

Data export: writeRaster() to GTiff format with INT2S datatype, overwrite option to "data/week-07/outputs/naip_ndvi_2013_prefire.tif".

Additional function: diff_rasters() calculates difference between two rasters (same CRS/extent). Usage: overlay(band1, band4, fun=diff_rasters) for band differences.

Temporal analysis: Compare NDVI distributions across multiple dates to assess vegetation productivity shifts and seasonal variations.

Foundation-level content for vegetation remote sensing analysis and geospatial data processing.

## Summarized attachments

- **Introduction to NDVI Calculation** (`https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Introduction%20to%20NDVI%20Calculation.ipynb`, notebook): Jupyter notebook demonstrating NDVI (Normalized Difference Vegetation Index) calculation from multispectral imagery using R libraries (raster, rgdal, rgeos, RColorBrewer). Covers NAIP pre-fire data processing, NDVI formula ((NIR - Red) / (NIR + Red)) using band ratios, visualization via plotting and histograms, GeoTIFF export, and raster difference calculations for temporal vegetation analysis.
