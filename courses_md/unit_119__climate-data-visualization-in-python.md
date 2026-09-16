---
title: "Climate data visualization in Python"
unit_id: 119
course_id: 4
level: "Expert"
slug: climate-data-visualization-in-python
is_course: 0
---

# Climate data visualization in Python

## Extracted resources (local files)

### Instructions for climate data visualization
*Source file:* `Instructions_for_climate_data_visualization.pdf`  ·  *type:* file

Climate data visualization using Cartopy 
 
Prepared by 
Qinqin Kong and Matthew Huber 
Department of Earth, Atmospheric, and Planetary Sciences 
kong97@purdue.edu  
Objective 
The main objective of this tutorial is to introduce the quick plot functionality of xarray and how 
to make publication quality map with Cartopy. 
 
Introduction 
Data visualization is an important step in research work flow. This tutorial will first introduce 
xarray’s plot functionality which is very convenient for making a quicky and dirty plot. Then we 
will delve into Cartopy which is a python package that can help us further refine our plot for 
publication purpose. We will first introduce the basics of Cartopy by creating a projection 
without any real data. Then we will use the results from climate data processing module to make 
a series of plots to show the potential functionality of Cartopy (matplotlib functions are highly 
compatible with Cartopy and heavily used in this module). Finally, we will draw our final plot 
and output it as a PDF file.   
 
Course material: 
Jupyter notebook:  
Climate_data_visualization_using_Cartopy_mygeohub.ipynb 
 
You can access the jupyter notebooks at:  
1) the “FAIR Climate and Water Science” course webpage in Mygeohub;  
2) https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master  
 
Pre-recorded video: 
The pre-recorded video for this tutorial is accessible in the YouTube Channel of the Climate 
Dynamics Prediction Lab:  
https://www.youtube.com/watch?v=jrFlTTP_Mkg&t=499s

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DV3/Climate_data_visualization_using_Cartopy_mygeohub.ipynb

# Python data visualization

This tutorial will first introduce the plotting functionality of Xarray which can enable you make a plot very quickly; then we talk about how to use cartopy to make publication quality maps.

```python
# import packages we need
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
import matplotlib as mpl
from matplotlib import gridspec
from cartopy.util import add_cyclic_point
import cmaps # make us have access to NCL color maps
```

```python
xr.set_options(display_style='html') # make the display_style of xarray more user friendly
%matplotlib inline
%config InlineBackend.figure_format = "retina" # make our figures look better 
```

____________
## 1. Quick plot functionality of Xarray
____________
xarray plotting functionality is a thin wrapper around the popular matplotlib library. 

```python
# use the North American air temperature dataset in Xarray tutorial
airtemps = xr.tutorial.open_dataset("air_temperature")
airtemps
```

**One-dimensional plot**

```python
# labels can also be used to easily create informative plots
air1d = airtemps.air.isel(lat=10, lon=10)
air1d[:200].plot(color="purple", marker="o",figsize=(10,4))
```

**adding to existing axis**

```python
fig, axes = plt.subplots(ncols=2,figsize=(10,4))
air1d.plot(ax=axes[0])
air1d.plot.hist(ax=axes[1])
plt.tight_layout()
plt.draw()
```

**Multiple lines in one plot**

```python
airtemps.air.isel(lon=10, lat=[19, 21, 22]).plot.line(x="time",figsize=(10,4))
```

**2-D map**

```python
air2d = airtemps.air.isel(time=500)
air2d.plot()
```

**contour plot**

```python
air2d.plot.contour()
```

**filled contour plot**

```python
air2d.plot.contourf(cmap='bwr')
```

```python
(air2d-273.15).plot.contourf(cmap='bwr',levels=np.arange(-30,30.1,5))
plt.title("North America temperature")
plt.ylabel("latitude")
plt.xlabel("longitude")
```

**Faceting**

```python
(airtemps.air-273.15).groupby('time.season').mean().plot(x="lon", y="lat", col="season", col_wrap=2,cmap='bwr')
```

Other types of plot that xarray supports: Streamplot, Quiver, Scatter; http://xarray.pydata.org/en/stable/user-guide/plotting.html

____________
## 2. Cartopy
____________
To start things off, we will introduce some basics of Cartopy to give you some ideas about what Cartopy can do!

### 2.1 Create a basic map projection using Cartopy
We create a basic map projection without using any real data. We will use the Cartopy feature interface (cfeature) to add some geographic features like ocean, lake, coastlines and borders. We will also add latitude and longitude gridlines.

```python
# Create and define the size of a figure object 
plt.figure(figsize=(8, 8))

# Create an axis with a basic PlateCarree projection style
ax = plt.axes(projection=ccrs.PlateCarree())

# try different projection, e.g. Robinson
#ax = plt.axes(projection=ccrs.Robinson())

# A full list of cartopy map projections: https://scitools.org.uk/cartopy/docs/latest/crs/projections.html

# Add natural features to map using cartopy.feature (cfeature)
ax.add_feature(cfeature.LAND, edgecolor='orange', facecolor='grey', zorder=0) # Lower zorders will be drawn first.
ax.add_feature(cfeature.LAKES, edgecolor='black', linewidth=0.2, facecolor='blue')
ax.add_feature(cfeature.OCEAN)

# Add country border lines
#ax.add_feature(cfeature.NaturalEarthFeature(category='cultural',
#                                           name='admin_0_countries',
#                                           scale='50m', #1:50million; three options: 10m, 50m, 110m
#                                           facecolor='none',
#                                           edgecolor='black',
#                                           linewidth=0.2))


# Add lat/lon gridlines
# Draw gridlines
#gl = ax.gridlines(crs=ccrs.PlateCarree(), linewidth=1, color='grey', draw_labels=True,linestyle='--')

# Manipulate latitude and longitude gridline numbers and spacing
#gl.ylocator = mticker.FixedLocator(np.arange(-80,80.1,40))
#gl.xlocator = mticker.FixedLocator(np.arange(-160, 160.1, 40))

# turn off gridline label on the top and right side
#gl.xlabels_top = False
#gl.ylabels_right = False

# For a list of available features in NaturalEarthFeature visit: https://www.naturalearthdata.com/features/
```

### 2.2 A map with data

```python
# read in our output from data processing
diff=xr.open_dataset('./output.nc')
diff
```

```python
# in the current environment, xarray.plot.pcolormesh (the default) doesn't work due to an incompatibility 
# issue between Cartopy and new matplotlib. So, we turn to use xarray.plot.imshow which requires longitude varing
# from -180 to 180. This issue can be resolved by updating cartopy to > 0.18.
# https://github.com/SciTools/cartopy/issues/1615
newlon=xr.where(diff.lon<180,diff.lon,diff.lon-360)
diff=diff.assign_coords(lon=newlon).sortby('lon')
```

```python
fig = plt.figure(figsize=(8,6))
ax = plt.axes(projection=ccrs.PlateCarree()) # Generate axes 
ax.coastlines('50m') # drawing coastlines
levels = np.arange(-10, 10.1, 2)
temp = diff.mean_diff.plot.imshow(ax=ax,
                      transform=ccrs.PlateCarree(), # What is the difference between 'transform' and 'projection'?
                      cmap=cmaps.sunshine_diff_12lev, # choose colormap
                       levels=levels, # discrete color bar
                      add_colorbar=False) # don't let xarray plot add colorbar automatically (which is the default)

# control color bar
cbar = plt.colorbar(temp,
                    orientation='horizontal', # control the orientation of color bar
                    shrink=0.7, # control the size of color bar relative to the axis
                    pad=0.073, # control the distance between color bar and the map
                    aspect=30, # control the width/height ratio of color bar
                    ticks=levels) # determine where to put the ticks
# control label size
cbar.ax.tick_params(labelsize=10)

# Add a title
plt.title('change in annual mean wet bulb temperature', fontsize=15)
plt.show()
```

### 2.3 What if we only want to plot data over land or certain area?

regionmask is a handy package to mask land, countries, or certain regions. Combining xarray and regionmask will make doing statistics over a certain region very easy.

```python
import regionmask
```

land mask

```python
landmask= regionmask.defined_regions.natural_earth.land_110.mask(diff)
landmask.plot()
```

```python
fig = plt.figure(figsize=(8,6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines('50m',linewidth=0.5)
levels = np.arange(-10, 10.1, 2)
temp = diff.mean_diff.where(landmask==0).plot.imshow(ax=ax,  # the only change happens here
                                          transform=ccrs.PlateCarree(),
                                          cmap=cmaps.sunshine_diff_12lev,
                                          levels=levels,
                                          add_colorbar=False)
cbar = plt.colorbar(temp,
                    orientation='horizontal',
                    shrink=0.7,
                    pad=0.073,
                    aspect=30,
                    ticks=levels)

cbar.ax.tick_params(labelsize=10)

plt.title('Change in annual mean wet bulb temperature', fontsize=15)
plt.show()
```

country mask

```python
# show the country code
fig = plt.figure(figsize=(20,6))
regionmask.defined_regions.natural_earth.countries_110.plot()
```

```python
countrymask=regionmask.defined_regions.natural_earth.countries_110.mask(diff,lon_name="lon", lat_name="lat")
# a xarray DataArray filled with country code
countrymask
```

```python
fig = plt.figure(figsize=(8,6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines('50m',linewidth=0.5)
levels = np.arange(-10, 10.1, 2)
temp = diff.mean_diff.where(countrymask==4).plot.imshow(ax=ax, # apply country mask
                                          transform=ccrs.PlateCarree(),
                                          cmap=cmaps.sunshine_diff_12lev,
                                          levels=levels,
                                          add_colorbar=False)
#ax.add_feature(cfeature.BORDERS,alpha=0.6) #add country border
#ax.set_extent([-170,-60,20,65]) # zoom in a certain area
cbar = plt.colorbar(temp,
                    orientation='horizontal',
                    shrink=0.7,
                    pad=0.073,
                    aspect=30,
                    ticks=levels)

cbar.ax.tick_params(labelsize=10)

plt.title('Change in annual mean wet bulb temperature for U.S.', fontsize=15)
plt.show()
```

An example of using regionmask to do statistics on a certain region: calculating land average temperature

```python
diff.mean_diff.where(landmask==0).weighted(np.cos(np.deg2rad(diff.lat))).mean(('lat','lon'))
```

### 2.4 Multiple maps sharing the same colorbar

```python
def subplot(data,axis,cmap,norm):
    g=data.where(landmask==0).plot.imshow(ax=axis,transform=ccrs.PlateCarree(),cmap=cmap,add_colorbar=False,norm=norm)
    axis.coastlines(linewidth=0.5)
    axis.set_title('')
    return g

def plot(diff):
    fig = plt.figure(figsize=[12, 5])
    ax0 = fig.add_subplot(121,projection=ccrs.PlateCarree())
    ax1 = fig.add_subplot(122,projection=ccrs.PlateCarree())
    fig.subplots_adjust(bottom=0, left=0,right=1, top=1,hspace=0.1,wspace=0.05)
    
    anno_opts = dict(xy=(0, 1.05), xycoords='axes fraction',va='baseline', ha='left')
    ax0.annotate('a. changes in annual mean wb', **anno_opts,fontsize=14)
    ax1.annotate('b. changes in annual q95 wb', **anno_opts,fontsize=14)
    
    cmap=cmaps.sunshine_diff_12lev
    levels=np.arange(-10, 10.1, 2)
    norm=mpl.colors.BoundaryNorm(levels,ncolors=len(levels)+1,extend='both') 
    # Generate a colormap index based on discrete intervals; 
    # colors are linearly distributed between these "bounds".
    
    # apply the same norm to both subplots which let them share the same color scale
    subplot(diff.mean_diff,ax0,cmap,norm)
    g=subplot(diff.q95_diff,ax1,cmap,norm)
    
    f=plt.gcf() #get the reference to the current figure
    cb=f.colorbar(g,ax=(ax0,ax1),orientation='horizontal', pad=0.05,shrink=0.5,ticks=levels,aspect=30) 
    cb.ax.tick_params(labelsize=12)
```

```python
plot(diff)
```

### 2.5 What if we want subplots of different sizes?
GridSpec can enable us Customize subplots layouts

```python
#plot a map
def Map(data,axis,norm,cmap):
    h=data.where(landmask==0).plot.imshow(ax=axis,transform=ccrs.PlateCarree(),add_colorbar=False,
                                                         norm=norm,cmap=cmap)
    gl=axis.gridlines(draw_labels=True,alpha=0)
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12}
    gl.xlabels_top = False
    gl.ylabels_right = False
    axis.coastlines(alpha=0.6)
    return h
# line plot about zonal average
def lineplot(axis,x,y):
    axis.plot(x,y,linewidth=2,color='blue')
    axis.set_xlabel('change in wb ($^\circ$C)',fontsize=12)
    axis.set_ylabel('Latitude',fontsize=12)
    axis.tick_params(axis='both', which='major', labelsize=12)
    axis.yaxis.set_ticks_position("right") # y axis ticks on the right
    axis.yaxis.set_label_position("right") # y axis labels on the right
def plot2(diff):
    levels=np.arange(-10, 10.1, 2)
    fig = plt.figure(figsize=(12,4))
    spec = gridspec.GridSpec(ncols=2, nrows=1,width_ratios=[10,1],wspace=-0.1) # 2 columns with a width ratio of 10:1
    ax0 = fig.add_subplot(spec[0], projection=ccrs.PlateCarree())
    ax1 = fig.add_subplot(spec[1])
    anno_opts = dict(xy=(0, 1.05), xycoords='axes fraction',va='baseline', ha='left')
    ax0.annotate('a. changes in annual mean wb', **anno_opts,fontsize=14)
    ax1.annotate('b', **anno_opts,fontsize=14)
    cmap=cmaps.sunshine_diff_12lev
    norm=mpl.colors.BoundaryNorm(levels,ncolors=len(levels)+1,extend='both')
    h=Map(diff.mean_diff,ax0,norm,cmap)
    cb=fig.colorbar(h,ax=ax0,orientation='vertical',ticks=levels,
                     pad=0.05,shrink=0.9)
    cb.ax.tick_params(labelsize=12)
    lineplot(ax1,diff.mean_diff.mean('lon'),diff.lat)
```

```python
plot2(diff)
```

### 2.6 What if we want to overlay something on the map to for example show the statistical significance

we can use the contourf plot with hatches to achieve it.

```python
fig = plt.figure(figsize=[8, 6])
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines('50m',linewidth=0.5)
levels=np.arange(-10, 10.1, 2)
cmap=cmaps.sunshine_diff_12lev
norm=mpl.colors.BoundaryNorm(levels,ncolors=len(levels)+1,extend='both')
temp = diff.mean_diff.where(landmask==0).plot.imshow(ax=ax,transform=ccrs.PlateCarree(),
                                              cmap=cmap,
                                              add_colorbar=False,norm=norm)
pvalue=xr.where(diff.mean_diff>5,0.01,0.09) # let's artificially create a p-value array

pvalue.where(landmask==0).plot.contourf(ax=ax,transform=ccrs.PlateCarree(),
                     colors='none',
                     levels=[0,0.05,1],
                     hatches=['....',None],
                     add_colorbar=False,
                     alpha=0)
cb=plt.colorbar(temp,orientation='horizontal', pad=0.05,shrink=0.5,ticks=levels,aspect=30) 
cb.ax.tick_params(labelsize=12)

plt.title('Change in annual mean wet bulb temperature for U.S.', fontsize=15)
plt.show()
```

____________
## 3. Our final plot
____________

```python
#plot a map
def Map(data,axis,norm,cmap,up):
    h=data.where(landmask==0).plot.imshow(ax=axis,transform=ccrs.PlateCarree(),add_colorbar=False,
                                   norm=norm,cmap=cmap)
    gl=axis.gridlines(draw_labels=True,alpha=0)
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12}
    gl.xlabels_top = False
    gl.ylabels_right = False
    if up:
        gl.xlabels_bottom = False
    axis.coastlines(alpha=0.6)
    return h
# line plot for zonal average
def lineplot(axis,x,y,up):
    axis.plot(x,y,linewidth=2,color='blue')
    axis.set_xlabel('change in wb ($^\circ$C)',fontsize=12)
    axis.set_ylabel('Latitude',fontsize=12)
    axis.tick_params(axis='both', which='major', labelsize=12)
    axis.yaxis.set_ticks_position("right") # y axis ticks on the right
    axis.yaxis.set_label_position("right") # y axis labels on the right
    if up:
        axis.set_xlabel('')
        axis.xaxis.set_ticklabels([])
def plot3(diff):
    levels=np.arange(-10, 10.1, 2)
    norm=mpl.colors.BoundaryNorm(levels,ncolors=len(levels)+1,extend='both')
    fig = plt.figure(figsize=(12,10))
    spec = gridspec.GridSpec(ncols=2, nrows=2,width_ratios=[10,1],hspace=0.2,wspace=-0.1) # 2 columns with a width ratio of 10:1
    ax0 = fig.add_subplot(spec[0], projection=ccrs.PlateCarree())
    ax1 = fig.add_subplot(spec[1])
    ax2 = fig.add_subplot(spec[2], projection=ccrs.PlateCarree())
    ax3 = fig.add_subplot(spec[3])
    anno_opts = dict(xy=(0, 1.05), xycoords='axes fraction',va='baseline', ha='left')
    ax0.annotate('a. changes in annual mean wb', **anno_opts,fontsize=14)
    ax1.annotate('b', **anno_opts,fontsize=14)
    ax2.annotate('c. changes in annual q95 wb', **anno_opts,fontsize=14)
    ax3.annotate('d', **anno_opts,fontsize=14)
    cmap=cmaps.sunshine_diff_12lev
    h=Map(diff.mean_diff,ax0,norm,cmap,True)
    lineplot(ax1,diff.mean_diff.mean('lon'),diff.lat,True)
    Map(diff.q95_diff,ax2,norm,cmap,False)
    lineplot(ax3,diff.mean_diff.mean('lon'),diff.lat,False)
    cb=fig.colorbar(h,ax=(ax0,ax2),orientation='vertical',
                     pad=0.05,shrink=0.8,aspect=30)
    cb.ax.tick_params(labelsize=12)
    
```

```python
plot3(diff)
plt.savefig("./final_plot.pdf", bbox_inches='tight')
```

### Workshop (link)
*URL:* https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master

# Binder

Binder
