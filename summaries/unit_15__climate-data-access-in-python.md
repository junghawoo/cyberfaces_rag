---
title: "Climate data access in Python"
unit_id: 15
course_id: 4
level: "Expert"
slug: climate-data-access-in-python
is_course: 0
---

# Climate data access in Python

Tutorial for accessing CMIP6 climate model data in cloud using Python libraries (xarray, intake-esm, fsspec), avoiding large local downloads via cloud storage (Google Cloud/AWS).

**Authors:** Qinqin Kong and Matthew Huber, Department of Earth, Atmospheric, and Planetary Sciences, Purdue University (kong97@purdue.edu). **Course:** FAIR Climate and Water Science. **Source:** Instructions_for_climate_data_access.pdf; **Jupyter Notebook:** Acess_CMIP6_data_in_cloud_using_intake-esm_mygeohub.ipynb (GitHub: PurdueCyberTraining/fairclimatewater); **Video:** https://www.youtube.com/watch?v=RiAQt1aQUnE&t=866s (Climate Dynamics Prediction Lab); **Mybinder:** https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master

## Problem and Solution

**Challenge:** Massive climate model output size prevents easy data discovery (numerous GCMs/variables) and local downloads. **Solution:** Use intake-esm to access CMIP6 data in cloud with user-friendly search API, avoiding local storage while enabling internet-based data access.

## Xarray Fundamentals

**Xarray** handles labelled, multi-dimensional arrays (Dataset, DataArray). **Key features:** Lazy loading (data not loaded until accessed), dimension labels (sel, slice), time-series operations, NetCDF/Zarr I/O. **Operations:** Annual/monthly means (groupby, resample), zonal/temporal averages, time slicing, attribute preservation via xr.set_options(keep_attrs=True). **File I/O:** to_netcdf(), to_zarr() (chunked storage with bsddb3 alternatives), open_mfdataset() (parallel multi-file loading).

## Cloud Data Access Workflow

**Step 1 (Zarr stores):** fsspec.get_mapper() retrieves MutableMapping from Google Cloud (gs://) or AWS S3 (s3://) URLs; xr.open_zarr(consolidated=True) opens single stores.

**Step 2 (Manual search):** Download CMIP6 metadata CSV (Google: cmip6.storage.googleapis.com/pangeo-cmip6.csv; AWS: cmip6-pds.s3.amazonaws.com/pangeo-cmip6.csv); pandas DataFrame query by activity_id, source_id, experiment_id, table_id, variable_id, member_id, grid_label.

**Step 3 (Intake-ESM):** intake.open_esm_datastore() connects JSON catalog (Google: storage.googleapis.com/cmip6/pangeo-cmip6.json; AWS: cmip6-pds.s3.amazonaws.com/pangeo-cmip6.json) with metadata database. Execute queries (require_all_on=['source_id']), load multiple stores to dataset dictionary (to_dataset_dict(zarr_kwargs={'consolidated':True})).

## Data Variables and Metadata

**CMIP6 table structure:** activity_id, institution_id, source_id, experiment_id, member_id, table_id, variable_id, grid_label, zstore URL, version. **Example models:** CESM2, EC-Earth3-Veg, CMCC-CM2-HR4, ACCESS-ESM1-5. **Variables:** tas (temperature), tasmax, ps (pressure), rsds (radiation), etc. **Grids:** gn (native), gr (regridded).

**Libraries:** intake (data access API), xarray (array handling), zarr (chunked storage), fsspec (filesystem abstraction), pandas (metadata queries), bsddb3 (alternative storage backend).

## Summarized attachments
- **Climate data access: accessing CMIP6 data in cloud** (Instructions_for_climate_data_access.pdf, file): Tutorial by Qinqin Kong and Matthew Huber from Purdue University on accessing CMIP6 climate model data from cloud storage (Google Cloud, AWS) using Python's intake-esm library, explaining how to overcome challenges of massive climate model output size, data discovery across numerous models and variables, and local download limitations through user-friendly cloud-based search APIs and zarr-based streaming access.
- **Jupyter Notebook Exercise** (https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA4/Acess_CMIP6_data_in_cloud_using_intake-esm_mygeohub.ipynb, notebook): Interactive Jupyter notebook demonstrating xarray fundamentals for handling labelled multi-dimensional arrays (Dataset, DataArray), cloud data access workflow using fsspec and zarr for Google Cloud/AWS URLs, intake-esm for CMIP6 metadata catalog queries, and practical climate data operations including lazy loading, time-series slicing, unit conversions (e.g., Kelvin to Celsius), NetCDF/Zarr file I/O, and example queries for climate models like CESM2 and EC-Earth3-Veg.
