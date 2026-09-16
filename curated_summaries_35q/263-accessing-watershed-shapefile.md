# Accessing Watershed Shapefile Using Python

- **ID:** 263
- **Type:** Module / Unit
- **Slug:** `accessing-watershed-shapefile`
- **Level:** 1
- **Length:** 30 min
- **Created:** 2024-09-05 12:32:20  ·  **Updated:** 2025-09-06 22:38:32

## Description
This workflow demonstrates how to access and visualize watershed boundaries for a given USGS site. Using the pynhd package’s NLDI (Network Linked Data Index) service, we query a watershed polygon by providing a site number and then export the results as a shapefile. The shapefile can be saved locally for future use or analysis. To ensure correct geographic representation, the pyproj CRS (Coordinate Reference System) is applied. Finally, the watershed shapefile is plotted to provide a clear spatial visualization, making it easier to integrate into hydrologic studies, geospatial analyses, or data-driven mapping projects.
