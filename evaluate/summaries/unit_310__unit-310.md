---
title: "Unit 310"
unit_id: 310
---

# Unit 310

Course creation process hands-on session for CyberFaCES platform. Instructor access and CyberFaCES account required; visit www.cyberfaces.org to log in. Presented by I Luk Kim, Research Scientist at Rosen Center for Advanced Computing.

Six-step module creation process: (1) Level — defining target audience; (2) Description — Access settings (Public/Requires Enrollment/Hidden/Show on Browse Page), CyberFaCES account requirement, workshop date/time range; (3) Adding Learning Materials (5 material types); (4) Set Pre-requisites; (5) Achievement; (6) Publish — final review and publishing. Navigation via Dashboard page, Instructing menu on left sidebar.

Step 3 materials include: uploading PDFs, videos, presentations, resources; connecting external resources/supplementary materials; creating explanations, instructions, narrative content; embedding interactive coding exercises from Git repositories; creating assessments for knowledge retention. Jupyter Notebook integration requires public Git repository URL (format: https://github.com/<user>/<repo>/<branch>/mynotebook.ipynb). Example URL: https://github.com/yirugi/ci4fair/blob/main/jn-test.ipynb. Steps for GitHub integration: visit github.com, create account, create repository, upload Jupyter Notebook file, check URL.

Quiz configurations: Question Sets (Fixed: all questions in fixed order; Random: random subset in random order); Number of Questions; Pass Mark (percentage or number of questions required to pass).

Create course via Dashboard > Instructing > Build a Course button; add modules via search and module selection.

Jupyter Notebook exercise: "Downloading Watershed Corresponding to USGS Site Number" prepared by Jibin Joseph and Venkatesh Merwade (Lyles School of Civil Engineering, Purdue University; joseph57@purdue.edu, vmerwade@purdue.edu; FAIR Science in Water Resources). Objective: download watershed shapefile using USGS site number, save, and plot.

Python packages: os, matplotlib.pyplot, pynhd (NLDI module), pyproj (CRS module). Step 1a: input USGS site number (examples: 04180000 drainage area 270 sq mi, 03335500 drainage area 7267 sq mi), input desired DEM resolution, create folder for downloaded files; function check_create_path_func() for creating directories if not existing. Step 1b: use pynhd module to get watershed using USGS station number, plot watershed with latitude/longitude (DD) coordinates and coordinate reference system, save as shapefile. Step 2: get basin extents using .total_bounds, calculate bounding longitudes and latitudes using math floor/ceil, determine coordinate system.

## Summarized attachments
- **CI4FAIR_CyberFaCES_HandsOn** (CI4FAIR_CyberFaCES_HandsOn.pptx, pptx): PowerPoint presentation by I Luk Kim (Research Scientist, Rosen Center for Advanced Computing) on the CyberFaCES course creation process. Covers 6-step module creation workflow: Level (target audience), Description (access settings, enrollment requirements, date ranges), Materials (5 types including PDFs, videos, presentations, interactive coding exercises, assessments), Pre-requisites, Achievements, and Publishing. Details material types, Jupyter Notebook integration from Git repositories, quiz configurations (Fixed/Random question sets, pass marks), and GitHub integration steps for uploading Jupyter Notebook files.
