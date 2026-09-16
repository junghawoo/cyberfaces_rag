---
title: "Cyberinfrastructure for FAIR Science Workshop"
unit_id: 289
course_id: 0
level: "Expert"
slug: cyberinfrastructure-for-fair-science-workshop
is_course: 1
objectives:
  - "Help participants become familiar with and learn how to use the tools developed under an NSF Cyberinfrastructure for Sustained Scientific Innovation (CSSI) project, in order to make research data and workflows more FAIR (findable, accessible, interoperable and reusable)."
---

# Cyberinfrastructure for FAIR Science Workshop

Hands-on workshop funded by National Science Foundation (NSF) to address data wrangling challenges across science and engineering disciplines. Supported by NSF awards #1835822 and #2230092. Dates: August 4-5, 2025; Location: Purdue University, West Lafayette campus.

Objective: Help participants use tools from NSF Cyberinfrastructure for Sustained Scientific Innovation (CSSI) project to make research data and workflows FAIR (findable, accessible, interoperable, reusable).

Focus areas: Managing vast amounts of data from diverse sources (streaming data from sensors, IoT devices, scientific instruments, geospatial data); large, heterogeneous, computationally intensive datasets requiring data wrangling.

Three themes: (1) Wrangling data — Resource intensive data processing pipelines using GeoEDF workflow library; (2) Managing continuous data streams — Sensor Data Management with StreamCI; (3) Cyber training — Interactive online learning using CyberFaces platform. Additional topics: High-Performance Computing (HPC) and Cloud Computing on NSF Anvil cluster; containerization technologies.

Day 1 Schedule: 8:30-11:30am Welcome, GeoEDF Workflow Framework presentation, tutorial on custom data connectors and processors (participants can prototype); 1:00-2:30pm StreamCI data management platform presentation, tutorial on ingesting/querying/analyzing sensor data; Break (30 min); 3:00-5:00pm CyberFaces interactive online teaching presentation, tutorial on creating/publishing learning modules.

Day 2 Schedule: 8:30-11:30am HPC/cloud computing on Anvil and containerization presentation, parallel working sessions (bring datasets, discuss collaborations, draft implementation plans); 11:30am-12:00pm wrap-up and Q&A.

Eligibility: Researchers, faculty, graduate students from U.S. institutions. Application requirements: CV, statement of interest (which themes, engagement approach, collaboration/educational plans). Deadline: May 31, 2025. Support: travel/lodging funds, certificate for completing requirements, honorarium for creating datasets/code/modules.

GeoEDF tutorial materials: Creating Greenness Map using NASA NLDAS Vegetation Greenness Fraction dataset. Use case: Upper Wabash River Watershed. Leaf Area Index (LAI) — vegetation greenness index, ratio of leaf area to ground area (dimensionless); Forests ~3-9, Grasslands ~0.5-2. NASA MCD15A3H dataset: MODIS global 4-day composite LAI/FPAR at 500m resolution (Terra+Aqua), available through USGS LP DAAC, HDF-EOS format. Workflow: NASAInput connector (URL opendap.cr.usgs.gov, filename filters), HDFEOSShapefileMask processor (aggregates data by shapefile polygons), output shapefile with weighted LAI per subbasin, Shapefile2GeoJSON processor for visualization. Shapefile components: .shp (geometry), .shx (index), .dbf (attributes). Processor development using NVIDIA HPC Container Maker.

## Summarized attachments
- **GeoEDF Connector/Processor Tutorial** (GeoEDF_tutorial_08042025.pdf, quiz): Tutorial by Christopher Thompson and Jungha Woo on creating a Greenness Map using NASA NLDAS Vegetation Greenness Fraction dataset and NASA Blue Marble Next Generation Map. Covers Leaf Area Index (LAI) as vegetation greenness metric for forests (3-9) and grasslands (0.5-2). Details GeoEDF workflow for Upper Wabash River Watershed including NASA MCD15A3H MODIS dataset (4-day global composite at 500m resolution), NASAInput connector configuration, HDFEOSShapefileMask processor for data aggregation by polygon, shapefile output formats, and Shapefile2GeoJSON processing for visualization.
