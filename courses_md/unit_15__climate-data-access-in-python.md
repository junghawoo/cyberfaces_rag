---
title: "Climate data access in Python"
unit_id: 15
course_id: 4
level: "Expert"
slug: climate-data-access-in-python
is_course: 0
---

# Climate data access in Python

## Extracted resources (local files)

### Climate data access: accessing CMIP6 data in cloud
*Source file:* `Instructions_for_climate_data_access.pdf`  ·  *type:* file

Climate data access: accessing CMIP6 data in cloud 
 
Prepared by 
Qinqin Kong and Matthew Huber 
Department of Earth, Atmospheric, and Planetary Sciences 
kong97@purdue.edu  
Objective 
The main objective of this tutorial is to introduce how to access CMIP6 data in cloud with 
intake-esm in Jupyter Notebook.   
 
Introduction 
Massive climate model output size has posed great challenges to data access. First, data can be 
difficult to discover given the potential large number of GCMS and variables. Second, climate 
model output is usually quite large and cannot be easily downloaded locally. These two 
challenges can be solved by using intake-esm to access CMIP6 data in cloud. The user-friendly 
search API makes data query easy, and we can avoid downloading data locally by directly 
accessing data in cloud through internet.  
 
Course material: 
Jupyter notebook: Acess_CMIP6_data_in_cloud_using_intake-esm_mygeohub.ipynb 
You can access this jupyter notebook at:  
1) the “FAIR Climate and Water Science” course webpage in Mygeohub;  
2) https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master  
 
Pre-recorded video: 
The pre-recorded video for this tutorial is accessible in the YouTube Channel of the Climate 
Dynamics Prediction Lab: https://www.youtube.com/watch?v=RiAQt1aQUnE&t=866s

## Image text (OCR)

### `FAIR_data_principles.jpg`
Bee J \ccessible —

R
oy
%

e

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA4/Acess_CMIP6_data_in_cloud_using_intake-esm_mygeohub.ipynb

# Python Data Access

We will first breifly introduce the functionality of Xarray, and then access CMIP6 data in goole cloud with intake-esm

____________
## 1. Xarray
____________

```python
import xarray as xr
import zarr
xr.set_options(display_style='html') # make the display_style of xarray more user friendly
```

```python
# use the North American air temperature dataset in Xarray tutorial
tas = xr.tutorial.open_dataset("air_temperature")
# we have a xarray dataset: A labelled 3-D array!
tas
```

```python
# access the xarray DataArray within the Dataset; xarray hasn't load the data into memory (xarray is lazy).
tas.air
```

```python
# let's acess year 2013 and 2014 separately and write them to our home directory
tas.sel(time='2013').to_netcdf('./tas_2013.nc')
tas.sel(time='2014').to_netcdf('./tas_2014.nc')
```

```python
# read in one of the two files that we just output
tas=xr.open_dataset('./tas_2013.nc')
tas.air
```

```python
Tc=tas.air-273.15
# now we do calculations, xarray loads data into memory
# but we lost the attributes
# that's because xarray, by default only keep attributes in unambiguous circumstances
Tc
```

```python
# set option globally to inform xarray always keep attributes
# you can also pass in keep_attrs=* within many individual xarray operations 
xr.set_options(keep_attrs=True)
```

```python
# do the calculation again: attributes are kept
Tc=tas.air-273.15
Tc
```

```python
# but with wrong unit (kelvin) which we need to change manually
Tc.attrs["units"] ='degC'
Tc
```

```python
# Now let's output Tc to zarr format using xarray
# we need to change Tc from xarray DataArray to xarray Dataset first!
Tc.to_dataset().to_zarr('./Tc_zarr/')
```

```python
# let's check what we get!

! ls ./
```

```python
# read in again
Tc_zr=xr.open_zarr('./Tc_zarr/')
# zarr automatically chunked the array for us when we output it above. We can also manually set the chunk size
Tc_zr.air
```

```python
# Above, all the chunks are stored within a directory containing many small files
# which may not be preferable on a HPC cluster
# zarr offer several other storage alternatives
import bsddb3
store = zarr.DBMStore('./Tc_zarr.bdb', open=bsddb3.btopen)
Tc_zr.to_zarr(store)
# we need to close the store explicitly
store.close()
```

```python
# let's check what we get

! ls ./
```

```python
# xarray can open multiple files in parallel
# by default it will be chunked in the way that each file correspond to one chunk
tas_mf=xr.open_mfdataset('./tas_*.nc',parallel=True)
tas_mf
```

lots of useful functionality of xarray: **the power of labelling!**

```python
# easy index by label
tas.air.sel(time='2013-07-01',lat=slice(50,20),lon=slice(250,300))
```

```python
# annual mean
tas.air.mean('time')
```

```python
# zonal averages at certain latitudes
tas.air.mean('time').sel(lat=slice(50,30)).mean('lon')
```

```python
# monthly mean value (climatological monthly mean if we have say 30 years)
# groupby can be very handy
tas.air.groupby('time.month').mean()
```

```python
# resample: daily maximum
tas.air.resample({'time':'D'}).max()
```

____________
## 2. Acess CMIP6 data in the Cloud
____________

### 2.1 Opening a single Zarr data store

A standalone Zarr data store can be opened using xarray’s ```open_zarr()``` function. The function takes a Python-native ```MutableMapping``` as input, which can be acquired from a Zarr store URL using ```fsspec```

```python
# fsspec: Filesystem interfaces to work with remote filesystems
import fsspec
```

```python
# create a MutableMapping from a store URL
mapper = fsspec.get_mapper("gs://cmip6/CMIP6/CMIP/AS-RCEC/TaiESM1/1pctCO2/r1i1p1f1/Amon/hfls/gn/v20200225/")
```

```python
# read in
# consolidate metadata objects into a single one which can increase the speed of reading the array metadata
ds = xr.open_zarr(mapper, consolidated=True)
ds
```

### 2.2 Manually searching the catalog

Wait! Where can I get the zstore URL?

- We can download a master CSV file enumerating all available data stores
- we can interact with the spreadsheet through a pandas DataFrame to search and explore for relevant data using the CMIP6 controlled vocabulary

```python
import pandas as pd
# for Google Cloud:
df = pd.read_csv("https://cmip6.storage.googleapis.com/pangeo-cmip6.csv")
# for AWS S3:
# df = pd.read_csv("https://cmip6-pds.s3.amazonaws.com/pangeo-cmip6.csv")
df
```

_result:_
```
activity_id       institution_id      source_id       experiment_id  \
0       HighResMIP                 CMCC   CMCC-CM2-HR4  highresSST-present   
1       HighResMIP                 CMCC   CMCC-CM2-HR4  highresSST-present   
2       HighResMIP                 CMCC   CMCC-CM2-HR4  highresSST-present   
3       HighResMIP                 CMCC   CMCC-CM2-HR4  highresSST-present   
4       HighResMIP                 CMCC   CMCC-CM2-HR4  highresSST-present   
...            ...                  ...            ...                 ...   
514813        CMIP  EC-Earth-Consortium  EC-Earth3-Veg          historical   
514814        CMIP  EC-Earth-Consortium  EC-Earth3-Veg          historical   
514815        CMIP  EC-Earth-Consortium  EC-Earth3-Veg          historical   
514816        CMIP  EC-Earth-Consortium  EC-Earth3-Veg          historical   
514817        CMIP  EC-Earth-Consortium  EC-Earth3-Veg          historical   

       member_id table_id variable_id grid_label  \
0       r1i1p1f1     Amon          ps         gn   
1       r1i1p1f1     Amon        rsds         gn   
2       r1i1p1f1     Amon        rlus         gn   
3       r1i1p1f1     Amon        rlds         gn   
4       r1i1p1f1     Amon         psl         gn   
...          ...      ...         ...        ...   
514813  r1i1p1f1     Amon         tas         gr   
514814  r1i1p1f1     Amon        tauu         gr   
514815  r1i1p1f1     Amon         hur         gr   
514816  r1i1p1f1     Amon         hus         gr   
514817  r1i1p1f1     Amon        tauv         gr   

                                                   zstore  dcpp_init_year  \
0       gs://cmip6/CMIP6/HighResMIP/CMCC/CMCC-CM2-HR4/...             NaN   
1       gs://cmip6/CMIP6/HighResMIP/CMCC/CMCC-CM2-HR4/...             NaN   
2       gs://cmip6/CMIP6/HighResMIP/CMCC/CMCC-CM2-HR4/...             NaN   
3       gs://cmip6/CMIP6/HighResMIP/CMCC/CMCC-CM2-HR4/...             NaN   
4       gs://cmip6/CMIP6/HighResMIP/CMCC/CMCC-CM2-HR4/...             NaN   
...                                                   ...             ...   
514813  gs://cmip6/CMIP6/CMIP/EC-Earth-Consortium/EC-E...             NaN   
514814  gs://cmip6/CMIP6/CMIP/EC-Earth-Consortium/EC-E...             NaN   
514815  gs://cmip6/CMIP6/CMIP/EC-Earth-Consortium/EC-E...             NaN   
514816  gs://cmip6/CMIP6/CMIP/EC-Earth-Consortium/EC-E...             NaN   
514817  gs://cmip6/CMIP6/CMIP/EC-Earth-Consortium/EC-E...             NaN   

         version  
0       20170706  
1       20170706  
2       20170706  
3       20170706  
4       20170706  
...          ...  
514813  20211207  
514814  20211207  
514815  20211207  
514816  20211207  
514817  20211207  

[514818 rows x 11 columns]
```

```python
# query it based on your needs!
df_subset = df.query("activity_id=='CMIP' & source_id=='CESM2' & table_id=='Amon' & variable_id=='tas' \
                     & member_id=='r1i1p1f1' & grid_label=='gn'")
df_subset
```

```python
# we have a bunch of zstore URLs
df_subset.zstore.values
```

```python
# let's say we want to access the last one!
zstore = df_subset.zstore.values[-1]
mapper = fsspec.get_mapper(zstore)
ds = xr.open_zarr(mapper, consolidated=True)
ds
```

### 2.3 working with multiple data stores at the same time
- It seems not user friendly to open all zstores one by one manually.

- ```intake-ESM``` can help combine several data stores to form a dataset.

- ```intake-ESM``` is an addon of ```intake``` which is a python package aiming to provide a consistent data access API.

```python
import intake
```

```python
# for Google Cloud:

# provide a link to an esm collection file which have a bunch of metadata including 
# how data stores can be combined to yield highly aggregated datasets
col = intake.open_esm_datastore("https://storage.googleapis.com/cmip6/pangeo-cmip6.json")
# Using this esm collection file, intake-esm connect a database (CSV file) that contains data assets locations 
# and associated metadata.
col

# for AWS S3:
#col = intake.open_esm_datastore("https://cmip6-pds.s3.amazonaws.com/pangeo-cmip6.json")
```

```python
col.df.head() #viewed as a DataFrame
```

```python
# do query!
query = dict(experiment_id=['historical'],
             table_id='Amon',
             variable_id=['tas','tasmax'],
             member_id = 'r1i1p1f1',
             grid_label='gn')
# intake-esm provides functionality to execute queries against the catalog
col_subset = col.search(require_all_on=['source_id'], **query)
# subset catalog and get some metrics grouped by 'source_id'
col_subset.df.groupby('source_id')[['experiment_id', 'variable_id', 'table_id']].nunique()
```

```python
col_subset.df #viewed as a DataFrame
```

```python
# intake-esm provides functionality to directly loads data to a dictionary of xarray dataset
dset_dict = col_subset.to_dataset_dict(zarr_kwargs={'consolidated': True})
```

```python
list(dset_dict.keys())
```

```python
# we got a xarry dataset that contains two xarray DataArray
dset_dict['CMIP.CSIRO.ACCESS-ESM1-5.historical.Amon.gn']
```

### https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master (link)
*URL:* https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master

# Binder

Binder
