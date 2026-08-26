---
title: "Accessing peak streamflow timeseries from United States Geographic Survey (USGS)"
unit_id: 10
course_id: 4
level: "Expert"
slug: accessing-peak-streamflow
is_course: 0
---

# Accessing peak streamflow timeseries from United States Geographic Survey (USGS)

Tutorial for automatically accessing and downloading annual peak streamflow data from USGS National Water Information System (NWIS) Web Interface using Python in Jupyter Notebook. Part of FAIR Science in Water Resources curriculum and Data Access (DA) module of FAIR Cyber Training course at Purdue University.

Prepared by Jibin Joseph and Venkatesh Merwade (School of Civil Engineering, Purdue University, vmerwade@purdue.edu). Objective: access annual peak series (maximum flow during year) used in hydrology for hydraulic structure design, flood modeling, and flood mapping. NWIS contains >29,000 stream gages with peak streamflow data across United States.

Source file: peakstreamflow_instructions.pdf (Last Revised: 2022/03/30). Data source: https://waterdata.usgs.gov/nwis/sw (USGS gage station data in text format). Requirements: web browser with internet, MyGeoHub account (mygeohub.org), Jupyter Notebook.

Instructions include: logging into mygeohub.org and launching Jupyter Notebook from Resources > Tools; creating folder structure (/courses/FAIRScience/DA1); accessing notebook file from FAIR Course Page; saving read-only ipynb file using Save As to designated location; refreshing to enable editing; importing required Python packages (urllib.parse, urllib.request, os, pandas, matplotlib.pyplot); defining function GetPeakFlowData_func() with arguments for USGS station number and folder name; executing main code with station number input and folder location specification; saving raw delimiter-separated (tab-separated) data as text file (e.g., "Data_03335500_raw.txt"); extracting and processing date and peak flow columns; creating time series plot using pandas dataframe with axis labels and titles.

Example: Wabash River at Lafayette, IN (station 03335500) — plot shows maximum peak flow 175,000+ cfs occurring 1910-1920 corresponding to 1913 flood.

Turn-in assignments: (1) download Wabash River data, format as CSV, calculate 10-, 25-, 50-, 100-, 500-year flows using EV1 distribution in Jupyter Notebook; (2) create frequency plot (return period x-axis, flow y-axis).

Jupyter Notebook Exercise: https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA1/Coursepage_DA1_peakstreamflow_v09.ipynb (Revision 09). Code examples provided for packages import, function definition, main code execution, and time series plotting. Technical documentation includes FAIR data principles image (FAIR_data_principles.jpg).

## Summarized attachments
- **Peak Streamflow Instructions** (peakstreamflow_instructions.pdf, file): Tutorial on accessing and downloading annual peak streamflow data from USGS NWIS using Python in Jupyter Notebook. Includes instructions for MyGeoHub setup, folder structure creation, package imports (urllib.parse, urllib.request, os, pandas, matplotlib), defining GetPeakFlowData_func() to access data by USGS station number, storing raw and processed data as text files, and creating time series plots. Example uses Wabash River (station 03335500) showing 175,000+ cfs peak flow in 1913. Includes assignments for EV1 distribution calculations and frequency plots.
- **FAIR Data Principles** (FAIR_data_principles.jpg, image): Image containing text on FAIR data principles.
- **Jupyter Notebook Exercise** (github.com/PurdueCyberTraining/fairclimatewater, notebook): Jupyter Notebook (Revision 09, Last Revised 2022-03-30) demonstrating Python 3 code for downloading annual peak streamflow data from USGS Surface Data Portal, with sections for package imports, function definition, main code execution, and time series plotting using pandas dataframe.
