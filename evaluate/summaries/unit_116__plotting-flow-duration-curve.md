---
title: "Plotting flow duration curve"
unit_id: 116
course_id: 4
level: "Foundation"
slug: plotting-flow-duration-curve
is_course: 0
---

# Plotting flow duration curve

Hydrological data visualization tutorial for computing and plotting flow duration curves (FDC) from USGS streamflow records using exceedance probability analysis.

**Authors:** Jibin Joseph and Venkatesh Merwade, School of Civil Engineering, Purdue University. **Topic:** FAIR Science in Water Resources. **Spring 2020.** **Source:** flowdurationcurve.pdf; **Jupyter Notebook:** flowdurationcurve.ipynb (GitHub: PurdueCyberTraining/fairclimatewater/blob/main/DV2/).

## Objective and Methodology

Plot flow duration curves using daily discharge data from USGS gaging stations via Weibull (1939) plotting position formula for exceedance probability calculation. Flow duration curve = streamflow values (y-axis) vs. exceedance probability (x-axis); represents percentage of time flow equals or exceeds specific value. Curve shape reveals watershed behavior: steep high end = short-duration high flows (flashy/urban watersheds); flat high end = sustained high flows (snow-dominated, regulated releases); flat low end = sustained baseflow (regular releases, reservoirs).

## Computational Steps

**Step 1:** Sort daily discharge data descending. **Step 2:** Calculate rank with largest discharge = 1. **Step 3:** Calculate exceedance probability via Weibull formula: P = M/(n+1), where P = exceedance probability (%), M = ranked position, n = total events. **Step 4:** Plot FDC on three scales: linear-linear (discharge/probability both linear), log-linear (discharge logarithmic, probability linear), log-probability (discharge logarithmic, probability scale).

## Data Access and Libraries

**Data source:** USGS NWIS daily streamflow (https://waterdata.usgs.gov/nwis/sw). **Python libraries:** hydrofunctions (hf, retrieve NWIS data), pandas (pd, dataframe manipulation), numpy (np), matplotlib.pyplot (plt, plotting), scipy.stats (sp), seaborn (visualization), probscale (probability scale plotting). **USGS parameters:** 00060 (Discharge, cubic feet per second), 00003 (daily mean). **Hydrofunctions options:** hf.NWIS(station_code, 'dv', period) or hf.NWIS(station_code, 'dv', start_date, end_date); call .get_data() to download.

## Tutorial Example and Assignment

**Example:** Wabash River at Lafayette, IN (USGS 03335500), 2017-01-01 to 2017-05-31. **Outputs:** Discharge hydrograph, FDC (linear-linear, log-linear, log-probability scales). **Assignment:** (1) Cedar Creek (04180000), Mar 01, 2019 to May 31, 2019 - produce three FDC plots; (2) USGS 05551700, compare FDC for periods 1971-1990 vs 1991-2010 (log scale), document changes/reasons; (3) USGS 05568800, compare 1971-1985 vs 1996-2010 (log scale), analyze shifts. **Jupyter kernel:** ct-fair (Python 3.6.5).

## Summarized attachments
- **Flow duration curve** (flowdurationcurve.pdf, file): Comprehensive tutorial document by Jibin Joseph and Venkatesh Merwade on computing and plotting flow duration curves using daily discharge data, explaining Weibull plotting position formula, exceedance probability calculations, and interpretation of FDC shapes for watershed characterization.
- **Jupyter Notebook Exercise** (https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DV2/flowdurationcurve.ipynb, notebook): Interactive Jupyter notebook with code cells for importing hydrofunctions, pandas, numpy, matplotlib, scipy libraries; downloading USGS streamflow data; calculating exceedance probabilities; and generating three-scale FDC plots (linear-linear, log-linear, log-probability).
