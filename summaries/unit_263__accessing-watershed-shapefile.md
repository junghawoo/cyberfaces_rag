---
title: "Accessing Watershed Shapefile Using Python"
unit_id: 263
course_id: 0
level: "Foundation"
slug: accessing-watershed-shapefile
is_course: 0
---

# Accessing Watershed Shapefile Using Python

This unit demonstrates accessing and visualizing watershed boundaries for USGS sites using Python, shapefile export, and geospatial coordinate systems. Prepared by Jibin Joseph and Venkatesh Merwade (Lyles School of Civil and Construction Engineering, Purdue University) as FAIR Science in Water Resources. Contact: joseph57@purdue.edu, vmerwade@purdue.edu.

## Overview and Objectives

**Primary Objectives**: Access and visualize watershed boundaries for given USGS sites; save shapefiles locally; plot spatial visualizations; integrate into hydrologic studies and geospatial mapping projects.

**Workflow Summary**: Query watershed polygons via pynhd NLDI (Network Linked Data Index) service using USGS site numbers; export as shapefiles; apply pyproj Coordinate Reference Systems (CRS) for correct geographic representation; visualize watershed boundaries spatially.

## Computer Requirements and Setup

**Environment**: Python-based Jupyter Notebook with conda environment and required modules/packages/libraries.

**Platform Integration**: Tutorial created for CyberFaCES platform (https://cyberfaces.org). Essential modules preinstalled in "ct-fair" kernel—no manual module installation required for CyberFaCES users.

**External Platform Requirements**: For non-CyberFaCES platforms, require pynhd package (versions v2, v3) or pynhd/geopandas packages (version v4) for USGS site shapefile retrieval.

**Versions**: Three instructional document versions exist (v2, v3, v4) with minor differences:
- v2: Basic pynhd access workflow
- v3: Enhanced v2 documentation  
- v4: Adds geopandas support; includes Step 1c accessing NLDI site information (latitude, longitude, HUC2 ID, etc.)

## CyberFaCES Platform Access Instructions

1. Navigate https://cyberfaces.org; click Login (upper right).
2. Select authentication: CILogon (institutional credentials), ORCID, or Google Account; check "Remember this selection."
3. Navigate "Learn" tab > "Explore Modules."
4. Select "Accessing Watershed Shapefile Using Python" module.
5. Click "Start now" to access module materials.
6. Click Jupyter Notebook file to access shapefile workflow.
7. Authenticate (same options as step 2); check "Remember this selection."
8. Wait for Notebook fetch from GitHub; load in JupyterHub. Verify "ct-fair" kernel selected.

## Python Implementation

**Required Libraries**:
```python
import os
import matplotlib.pyplot as plt
from pynhd import NLDI
from pyproj import CRS
```

(v4 adds geopandas for enhanced shapefile handling)

**Step 1a - USGS Site Input and Directory Creation**:
- Input USGS site number (string format)
- Define folder location for downloaded shapefiles
- Implement check_create_path_func() to create/verify directories; prints status
- Example drainage areas: Cedar Creek (04180000) = 270 sq mi (2-3 min download); Wabash River (03335500) = 7267 sq mi (longer processing)

**Step 1b - Watershed Shapefile Retrieval and Visualization**:
- Use pynhd NLDI().get_basins(site_id) to query watershed boundary
- Plot watershed with facecolor="b", edgecolor="k", figsize=(8,8)
- Display title showing site_id and CRS; xlabel/ylabel "Longitude (DD)"
- Save shapefile locally: .to_file(filename, driver='ESRI Shapefile', mode='w')
- Default example: Cedar Creek Near Cedarville, Indiana (270 sq mi drainage area)
- Supports custom USGS site numbers available in NLDI database

**Step 1c (v4 Only) - NLDI Site Information Access**:
- Access latitude, longitude, HUC2 ID stored in NLDI service

**Step 2 - Coordinate System and Spatial Extents**:
- Determine CRS and bounding values (extents)
- Data default: EPSG:4326 (WGS84 Geographic Coordinate System) = latitude/longitude degrees
- Widely used for global datasets, mapping, geospatial analysis
- Advanced/area-based calculations may require transformation to Projected Coordinate System (PCS)
- Extract extents using .total_bounds property; print formatted bounding box (Left/Right Longitude, Bottom/Top Latitude with °W/°N notation)
- Display CRS: print(watershed.crs)

## External Resources

**GitHub Repository - Jupyter Notebooks**: https://github.com/I-GUIDE/hydroewd/blob/main/Watershed_Access/Coursepage_DA0_Watershed_Access.ipynb

## Summarized attachments
- **Instructions_AccessingShapefile_cyberfaces_v2.pdf** (Instructions_AccessingShapefile_cyberfaces_v2.pdf, pdf): Workflow documentation by Jibin Joseph and Venkatesh Merwade demonstrating watershed boundary access using pynhd NLDI service to query and export shapefile for a given USGS site number with coordinate reference system transformation and visualization using Cedar Creek example (USGS site 04180000 with 270 sq. mi. drainage area).
- **Instructions_DA0_AccessingShapefile_cyberfaces_v3.pdf** (Instructions_DA0_AccessingShapefile_cyberfaces_v3.pdf, pdf): Updated instructions for accessing watershed shapefiles via pynhd NLDI service with steps to input USGS site number, retrieve watershed polygon, plot visualization, and determine coordinate system (EPSG:4326 WGS84) and spatial extents for hydrologic analysis.
- **Instructions_DA0_AccessingShapefile_cyberfaces_v4.pdf** (Instructions_DA0_AccessingShapefile_cyberfaces_v4.pdf, pdf): Latest version adding Step 1c to access site information stored in NLDI (latitude, longitude, HUC2 ID) using pynhd and geopandas packages for watershed boundary retrieval and analysis.
- **Jupyter Notebook File** (https://github.com/I-GUIDE/hydroewd/blob/main/Watershed_Access/Coursepage_DA0_Watershed_Access.ipynb, notebook): Interactive notebook implementing watershed shapefile download using USGS site number with pynhd NLDI service, shapefile plotting, coordinate system determination, and spatial extent calculation for watershed boundary analysis.

**Reference**: Chegini, T., Li, H. Y., & Leung, L. R. (2021). HyRiver: Hydroclimate Data Retriever. Journal of Open Source Software, 6(66), 3175.

## Key Concepts and Workflows

- **Network Linked Data Index (NLDI)**: Service providing access to hydrological network-linked datasets
- **Shapefile Format**: Standard geospatial vector format for polygon/boundary representation
- **Coordinate Reference Systems (CRS)**: EPSG:4326 (WGS84 geographic), projected systems for area calculations
- **Spatial Extents**: Bounding box defining basin geographic boundaries
- **Watershed Boundary Visualization**: Spatial plotting for hydrologic analysis integration
- **Scalability**: Single site to multi-site watershed queries; time scales with drainage area

## Learning Outcomes

Upon completion, users can:
1. Query watershed boundaries using USGS site numbers via pynhd
2. Export watershed shapefiles to local directories
3. Visualize watershed spatial boundaries using matplotlib
4. Understand and apply geographic coordinate reference systems
5. Calculate and interpret spatial extents (bounding coordinates)
6. Integrate watershed data into hydrologic modeling and geospatial projects

## Homework Integration

Assignment instructions direct students to download watershed boundaries for assigned USGS sites (available in course grade center/Brightspace). Requires completing Steps 1-2 for specified watershed sites.

**Completion Status**: "Ok, you have now completed the tutorial successfully. Congratulations!"
