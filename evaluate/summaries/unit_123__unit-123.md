---
title: "Unit 123"
unit_id: 123
---

# Unit 123

Tutorial on creating and publishing Jupyter Notebook tools in MyGeoHub. Prepared by Jibin Joseph and Venkatesh Merwade (School of Civil Engineering, Purdue University, vmerwade@purdue.edu). Part of FAIR Science in Water Resources. Last Revised: 2021/06/02.

Tool creation focuses on hydrograph and flow duration curve plotting. Data source: USGS daily streamflow from https://waterdata.usgs.gov/nwis/sw. Python packages: hydrofunctions (download streamflow for USGS station and time period), ipywidgets (textbox and button widgets), IPython.display.

Step-by-step instructions: (1) Log into mygeohub.org, navigate Resources > Tools, launch Jupyter Notebook; (2) Create folder structure (/courses/FAIRScience/Pub2); (3) Access FAIR Course Page, click notebook file; (4) Save as in read-only mode to designated folder (/FAIRScience/Pub2/toolcreation.ipynb); (5) Refresh browser to enable editing; (6) Import packages (pandas, matplotlib, hydrofunctions, ipywidgets); (7) Add sample image using Markdown cell or IPython.display code cell; (8) Create definition blocks: DailyDischargeData_func (hydrofunctions to fetch data), DischargeHydrographPlot_func (matplotlib plotting); (9) Create textbox widgets for USGS station number, start date, end date inputs; (10) Create button widget linking to discharge data and hydrograph functions; (11) Define ExceedProb_func (exceedance probability calculation) and FlowDurCurveLinLin_func (flow duration curve plotting); (12) Create second button linked to FDC functions; (13) Display buttons in tab container widget for organization.

Tool testing: Click Appmode (top menu bar) to convert notebook to web application (hides code, read-only markdown); example input: USGS Station 03335500, dates 2017-01-01 to 2017-06-30; generates discharge hydrograph and flow duration curve plots.

Tool publication: MyGeoHub Resources > Tools > Start a new Tool; input unique name (e.g., "hfdctool"), title, description; select "Publish as a Jupyter Notebook"; click Register tool; access tool status page (https://mygeohub.org/tools/<unique_tool_name>/status); launch terminal window in Jupyter Notebook Home Directory (New > Terminal); use svn checkout command to download tool code; navigate to tool folder (bin folder for ipynb code, data folder for data, middleware folder for invoke script); duplicate ipynb file, move to bin folder, rename as "toolcode.ipynb"; modify invoke script in middleware folder; use svn add and svn commit commands to upload to repository (requires MyGeoHub password); request admin review (Dashboard > My Drafts); ~3 business days for admin approval. Tool reference format: "Author (Year), \"Tool Name,\" https://mygeohub.org/tools/<unique_tool_name>".

## Summarized attachments
- **Tool Creation and Publishing Instructions** (toolcreationpublishing_instructions_v3.pdf, file): Comprehensive tutorial by Jibin Joseph and Venkatesh Merwade on creating and publishing Jupyter Notebook tools in MyGeoHub for hydrograph and flow duration curve plotting. Covers tool creation with ipywidgets (textbox, button widgets), definition functions for fetching USGS daily streamflow data using hydrofunctions and plotting with matplotlib, testing via Appmode, and publication workflow including SVN checkout, file organization (bin, data, middleware folders), invoke script modification, and admin approval process.
