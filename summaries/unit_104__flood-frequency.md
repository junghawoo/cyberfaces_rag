---
title: "Flood frequency analysis and Flow Duration Curve"
unit_id: 104
course_id: 4
level: "Foundation"
slug: flood-frequency
is_course: 0
---

# Flood frequency analysis and Flow Duration Curve

This tutorial covers calculation of return period (recurrence interval, repeat interval) flows from peak flow data using statistical analysis. The module teaches how to compute flows corresponding to 100-year, 500-year, and other return periods (10, 25, 50, 250-year) for hydrologic design and risk assessment.

**Source materials:** Instruction document `ffareturnperiod_instructions.docx` prepared by Jibin Joseph and Venkatesh Merwade (vmerwade@purdue.edu); Jupyter Notebook `ffa_returnperiod.ipynb` available on GitHub at https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP1/Coursepage_DP1_ffareturnperiod_v05.ipynb. The tutorial is part of FAIR Science in Water Resources curriculum.

**Data source:** Peak flow data obtained from USGS Surface Data Portal (https://waterdata.usgs.gov/nwis/sw) using eight-digit USGS station numbers. The code programmatically retrieves raw data containing additional metadata.

**Environment and tools:** Execution on mygeohub.org platform using Jupyter Notebook with Anaconda 5.1. Python 3 implementation (Revision 05, last revised 2020-06-05) requiring packages: urllib.parse, urllib.request, math, scipy.stats, numpy (np), gamma, and invgamma from scipy.stats.

**Workflow steps:** (1) Log into mygeohub.org and launch Jupyter Notebook; (2) Access course notebook file and save locally in dedicated Module06 folder; (3) Input assigned USGS station number (eight digits) and station name; (4) Execute cell CELL-01 to load packages and provide code description; (5) Execute CELL-02 defining function GetAnnualPeakFlowData_f() to retrieve raw data from USGS link, decode output, extract required data (date and discharge), and store processed data with "_reqd" suffix; (6) Execute CELL-03 to input station number and run data retrieval function; (7) Review retrieved data file to identify continuous data period (minimum 30 years without gaps); account for water year convention (October-September); (8) Execute CELL-04 to input four year values (data period start/end, analysis period start/end); (9) Execute CELL-05 implementing return period calculation using moving window method with 1-year and 5-year time steps, utilizing Gamma Inverse Function for statistical computation.

**Assignment deliverables:** Create PDF of flood frequency table for 10, 25, 50, 100, 250, and 500-year return periods. Modify script to run frequency analysis with different time steps (1, 5, 10-year moving windows), each producing separate output files (TS1, TS5, TS10) with columns representing different return periods. Average column values across time-step files to populate table rows. Include Python script, PDF table, and readme/instruction file documenting creation steps. Upload all resources to HydroShare with resource name "Flood Frequency Plot for [station name]" and abstract describing PDF contents.

## Summarized attachments
- **Calculation of Return Period Flow from Peak Flow Data** (ffareturnperiod_instructions.docx, file): Instructions document by Jibin Joseph and Venkatesh Merwade for calculating return period flows from USGS peak flow data using Gamma Inverse Function statistical analysis, covering data retrieval from USGS Surface Data Portal, annual peak flow extraction, return period calculation for 100-year and 500-year events, moving window analysis methods, Jupyter notebook workflow with cell-by-cell execution steps, data quality checks for continuous records, and assignment requirements for flood frequency table generation.
- **Jupyter Notebook Exercise** (https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP1/Coursepage_DP1_ffareturnperiod_v05.ipynb, notebook): Interactive Jupyter notebook (Python 3, Revision 05) for flood frequency analysis implementing peak flow data retrieval from USGS via urllib, extraction of discharge and date information, scipy.stats gamma and invgamma functions for return period calculation, moving window methods with 1-year and 5-year time steps, return period computation for 10, 25, 50, 100, 250, and 500-year events, and output to text files stored in Results folder.
