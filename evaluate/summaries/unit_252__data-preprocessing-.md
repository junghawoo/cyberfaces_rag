---
title: "Data Preprocessing"
unit_id: 252
course_id: 0
level: "Foundation"
slug: data-preprocessing-
is_course: 0
---

# Data Preprocessing

Hydrological and climate data preprocessing workflow integrating USGS discharge data with gridded climate datasets for water resources modeling.

**Source:** Data_prep.ipynb (GitHub: VMerwadeGroup/CyberFaCES/blob/main/AI_DataPrep/Data_prep.ipynb). **Example site:** Cedar Creek Near Cedarville, IN (USGS 04180000), date range 1988-01-01 to 2023-01-01.

## Libraries and Data Access Tools

**Python packages:** numpy, pathlib, pandas, matplotlib.pyplot, hydrofunctions (hf), pygridmet (GridMET), pynhd (NLDI), requests, sklearn.preprocessing.

**Data sources:** 
1. **NLDI (National Linked Data Index):** retrieves watershed geometry and basin boundaries via pynhd.NLDI().get_basins() for site number lookup.
2. **USGS NWIS (hydrofunctions):** acquires streamflow time series via hf.NWIS() instantaneous (iv) data, parameter code 00060 (Discharge, cubic feet per second); data spans 1988-01-19 to 2023-01-02 (1,225,632 rows at 15-minute intervals).
3. **GridMET (pygridmet):** daily climate/weather grids via GridMET().gridmet_table variables.

## USGS Discharge Data Processing

**Instantaneous discharge:** Retrieved via hydrofunctions from NWIS REST service (https://nwis.waterservices.usgs.gov/nwis/iv/); upsampled 15-minute frequency with qualifiers field. **Daily discharge:** Downloaded via requests library from https://waterdata.usgs.gov/nwis/dv; format rdb (tab-separated). Data parsed using pd.read_csv(StringIO()), skipping metadata header lines. Resulting DataFrame: 12,785 rows with columns agency, site, datetime, discharge, quality. Discharge converted from cubic feet per second (cfs) to cubic meters per second (m³/s) via 0.0283168 multiplier. Final output: datetime index, single discharge column.

## GridMET Climate Data Retrieval and Aggregation

**GridMET variables (16 total):** pr (precipitation, mm), rmax (max relative humidity, %), rmin (min relative humidity, %), sph (specific humidity, kg/kg), srad (surface radiation, W/m²), th (wind direction, degrees), tmmn (minimum temperature, K), tmmx (maximum temperature, K), vs (wind speed, m/s), bi (burning index), fm100 (100-hour fuel moisture, %), fm1000 (1000-hour fuel moisture, %), erc (energy release component), etr (alfalfa reference evapotranspiration, mm), pet (grass reference evapotranspiration, mm), vpd (vapor pressure deficit, kPa).

**Data acquisition:** gridmet.get_bygeom() retrieves data for basin geometry using dates and variable subset (pr, rmax, rmin, tmmn, tmmx, vs, pet). Returns xarray.Dataset (39MB, dimensions 12,776 time steps × 10 lat × 11 lon grid). **DataFrame conversion:** daily.to_dataframe().reset_index() converts xarray Dataset to pandas DataFrame. **Spatial aggregation:** groupby("time").agg() calculates mean across lat/lon grid for each variable, producing single daily value per variable. Result: 12,776 rows × 7 climate columns.

## Data Integration and Export

**Concatenation:** pd.concat() merges discharge DataFrame and aggregated climate DataFrame on datetime index, producing unified model_df (12,785 rows × 8 columns: discharge, pr, rmax, rmin, tmmn, tmmx, vs, pet). Output exported to CSV via to_csv('model_df.csv'). Integrated dataset ready for ML/AI hydrological modeling with discharge as target variable and climate features as predictors.

## Summarized attachments
- **AI/ML Data Preprocessing** (https://github.com/VMerwadeGroup/CyberFaCES/blob/main/AI_DataPrep/Data_prep.ipynb, notebook): Jupyter notebook demonstrating hydrological and climate data preprocessing workflow retrieving USGS discharge data (hydrofunctions) for Cedar Creek (04180000) from 1988-2023, accessing watershed geometry via pynhd NLDI, acquiring GridMET daily climate variables (pr, rmax, rmin, tmmn, tmmx, vs, pet), aggregating spatial climate data, and merging discharge with climate datasets for ML/AI hydrological modeling preparation.
