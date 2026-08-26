---
title: "Introduction to NDVI Calculation"
unit_id: 270
course_id: 0
level: "Foundation"
slug: introduction-to-ndvi-calculation
is_course: 0
---

# Introduction to NDVI Calculation

## Fetched resources (external URLs)

### Introduction to NDVI Calculation (notebook)
*URL:* https://github.com/jakehosen/cybertraining_ecology/blob/main/Level%202/Introduction%20to%20NDVI%20Calculation.ipynb

# Setup
First we are going to do some housekeeping that includes loading some libraries and settings to get started.

```python
# load spatial packages
library(raster)
library(rgdal)
library(rgeos)
library(RColorBrewer)

# turn off factors
options(stringsAsFactors = FALSE)

```

## NDVI and related metrics
The Normalized Difference Vegetation Index (NDVI) is a quantitative index of greenness ranging from 0-1, where 0 represents minimal or no greenness and 1 represents maximum greenness.

NDVI is often used for a quantitate proxy measure of vegetation health, cover and phenology (life cycle stage) over large areas.

NDVI is calculated from the visible and near-infrared light reflected by vegetation. Healthy vegetation (left) absorbs most of the visible light that hits it, and reflects a large portion of near-infrared light. Unhealthy or sparse vegetation (right) reflects more visible light and less near-infrared light.

<div>
<img src="images/ndvi.jpg" width="300"/>
</div>

```python
# import the naip pre-fire data
naip_multispectral_st <- stack("data/week-07/naip/m_3910505_nw_13_1_20130926/crop/m_3910505_nw_13_1_20130926_crop.tif")

# convert data into rasterbrick for faster processing
naip_multispectral_br <- brick(naip_multispectral_st)
```

## GIS Metadata
GIS metadata is essential for properly importing and processing spatial data. Below is the relevant metadata for the multispectral GIS tile we just imported.

class      : RasterLayer<br>
dimensions : 2312, 4377, 10119624  (nrow, ncol, ncell)<br>
resolution : 1, 1  (x, y)<br>
extent     : 457163, 461540, 4424640, 4426952  (xmin, xmax, ymin, ymax)<br>
crs        : +proj=utm +zone=13 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs <br>
source     : memory<br>
names      : m_3910505_nw_13_1_20130926_crop.4 <br>
values     : 0, 255  (min, max)<br>

```python
# calculate ndvi with naip
naip_multispectral_br[[4]]

# calculate NDVI using the red (band 1) and nir (band 4) bands
naip_ndvi <- (naip_multispectral_br[[4]] - naip_multispectral_br[[1]]) / (naip_multispectral_br[[4]] + naip_multispectral_br[[1]])

# plot the data
plot(naip_ndvi,
     main = "NDVI of Cold Springs Fire Site - Nederland, CO \n Pre-Fire",
     axes = FALSE, box = FALSE)

```

### To determine how vegetation productivity shifts over time, we can use distributions of NDVI values for all the pixels in the GIS layer we're using for our calculations.

```python
# view distribution of NDVI values
hist(naip_ndvi,
  main = "NDVI: Distribution of pixels\n NAIP 2013 Cold Springs fire site",
  col = "springgreen",
  xlab = "NDVI Index Value")
```

```python
# Check if the directory exists using the function you created last week
check_create_dir("data/week-07/outputs/")

# Export your raster
writeRaster(x = naip_ndvi,
              filename="data/week-07/outputs/naip_ndvi_2013_prefire.tif",
              format = "GTiff", # save as a tif
              datatype='INT2S', # save as a INTEGER rather than a float
              overwrite = TRUE)  # OPTIONAL - be careful. This will OVERWRITE previous files.
```

```python
# create a function that subtracts two rasters

diff_rasters <- function(b1, b2){
  # this function calculates the difference between two rasters of the same CRS and extent
  # input: 2 raster layers of the same extent, crs that can be subtracted
  # output: a single different raster of the same extent, crs of the input rasters
  diff <- b2 - b1
  return(diff)
}
```

```python
band_diff <- overlay(naip_multispectral_br[[1]], naip_multispectral_br[[4]],
        fun = diff_rasters)

plot(band_diff,
     main = "Example difference calculation on imagery - \n this is not a useful analysis, just an example!",
     axes = FALSE, box = FALSE, legend = FALSE)

```
