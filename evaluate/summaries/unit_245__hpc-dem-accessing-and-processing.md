---
title: "Geospatial & Hydrological Science: HPC Based DEM Accessing and Processing (Single Job)"
unit_id: 245
course_id: 0
level: "Developer"
slug: hpc-dem-accessing-and-processing
is_course: 0
---

# Geospatial & Hydrological Science: HPC Based DEM Accessing and Processing (Single Job)

HPC-based tool for accessing and processing Digital Elevation Model (DEM) data for larger watersheds using USGS site ID and resolution. Prepared by Jibin Joseph, Rajesh Kalyanam (Rosen Center for Advanced Computing, Purdue University), Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University, joseph57@purdue.edu, vmerwade@purdue.edu). Part of FAIR Science in Water Resources.

Platform: CyberGIS community-centered platform (https://cyberfaces.org) for handling large number of DEM tiles. Login options: CILogon institutional credentials, ORCID, Google Account.

Workflow: Navigate Learn > Explore Modules; select course type "Courses"; locate "WaterSciCon24 Hands-On Workshop" or "I-GUIDE Forum Hands-On Workshop: Web-based Modules on Geospatial Data Processing Using Python"; click "Start now"; select "I-GUIDE Launch Link" Jupyter Notebook.

Jupyter Notebook kernels: iguide-ewd (v1) or geohydro-pynhd (v2); both have preinstalled modules.

Step 1 - Define variables: USGS site ID (example: 05331000 Mississippi River at St. Paul, MN), DEM resolution (1/3 arc-second example); large watershed example: ~36,000 sq. mi. area, requires HPC due to high RAM demands.

Step 2 - HPC Job Submission: CyberGIS user interface; Job Configuration Tab > Slurm Computing Configurations; set time (30 minutes example), CPUs per task (128 example); submit job; monitor progress in "Your Job Status" tab; download results from "Download Job Result" folder (preview folder).

Step 3 - Visualization: Download preview plot created for large watershed; transfer file from HPC to local platform; plot clipped DEM.

I-GUIDE Launch Links:
- Coursepage: https://jupyter.iguide.illinois.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FI-GUIDE%2Fhydroewd&urlpath=lab%2Ftree%2Fhydroewd%2FCoursepage_DEM_GeoEDF_v4.ipynb+&branch=2025_Miniworkshop
- Single Job: https://jupyter.iguide.illinois.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FI-GUIDE%2Fhydroewd&urlpath=lab%2Ftree%2Fhydroewd%2FDEM_HPC_Processing%2FDEM_SingleJob.ipynb+&branch=main

Documentation versions: Instructions_DP9_HPC_DEM_Processing_v01.pdf, v02.pdf with course variations.

## Summarized attachments
- **HPC Tool: Accessing & Processing Digital Elevation Model (DEM) data** (Instructions_DP9_HPC_DEM_Processing_v01.pdf, file): Tutorial by Jibin Joseph, Rajesh Kalyanam, and Venkatesh Merwade on HPC-based DEM processing for larger watersheds via CyberGIS platform. Covers CyberFaCES login (CILogon, ORCID, Google Account options), navigating to course modules, launching Jupyter Notebooks with iguide-ewd or geohydro-pynhd kernels. Details HPC job submission workflow: setting USGS site ID and DEM resolution, configuring Slurm Computing (time, CPUs per task), monitoring job status, downloading results and visualization plots, transferring files between HPC and local platform.
