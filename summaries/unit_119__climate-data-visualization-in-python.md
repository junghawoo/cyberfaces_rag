---
title: "Climate data visualization in Python"
unit_id: 119
course_id: 4
level: "Expert"
slug: climate-data-visualization-in-python
is_course: 0
---

# Climate data visualization in Python

This advanced unit covers climate data visualization using Cartopy and xarray, producing publication-quality maps. Prepared by Qinqin Kong and Matthew Huber (Department of Earth, Atmospheric, and Planetary Sciences, Purdue University). Contact: kong97@purdue.edu.

## Objective

Introduce xarray quick plot functionality and publication-quality map creation with Cartopy (Python package for geospatial data visualization). Tutorial progresses from quick xarray plots through Cartopy basics and refinements to final publication outputs.

## Course Materials

**Jupyter Notebook**: Climate_data_visualization_using_Cartopy_mygeohub.ipynb

## Summarized attachments
- **Instructions for climate data visualization** (Instructions_for_climate_data_visualization.pdf, file): Tutorial document by Qinqin Kong and Matthew Huber on climate data visualization using Cartopy for publication-quality maps, covering xarray quick plot functionality, Cartopy map projections, geographic features (coastlines, land, lakes), regionmask for land/country masking, grid lines, and multi-panel visualizations for climate data analysis.
- **Jupyter Notebook Exercise** (https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DV3/Climate_data_visualization_using_Cartopy_mygeohub.ipynb, notebook): Interactive notebook implementing xarray data visualization and Cartopy map production for climate data, including quick plots, map projections, cartopy features, regional masking with regionmask, multiple subplots with shared colorbars, and overlay of statistical significance with hatching patterns.
- **Workshop** (https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master, link): Binder environment providing interactive access to climate data visualization workshop materials.

**Access**: FAIR Climate and Water Science course (Mygeohub); https://mybinder.org/v2/gh/QINQINKONG/cybertraining_workshop/master

**Pre-recorded Video**: https://www.youtube.com/watch?v=jrFlTTP_Mkg&t=499s (Climate Dynamics Prediction Lab YouTube)

## Python Libraries

Core: numpy, matplotlib, xarray, Cartopy (ccrs, cfeature), matplotlib.ticker, gridspec, cartopy.util (add_cyclic_point), cmaps (NCL color maps access)

Optional: regionmask (land/country/region masking)

**Configuration**: `xr.set_options(display_style='html')`, `%matplotlib inline`, `%config InlineBackend.figure_format = "retina"` (Jupyter high-resolution display)

## Xarray Quick Plot Functionality

Xarray plotting wraps matplotlib for convenience. Supported plot types:

**1D Plots**:
- `.plot(color, marker, figsize)`: line plots with customization
- `.plot.hist()`: histograms
- `.plot.line(x="dimension")`: multi-line plots

**2D Maps**:
- `.plot()`: basic 2D map
- `.plot.contour()`: contour lines
- `.plot.contourf(cmap, levels)`: filled contours with colormap/level specification
- `groupby().plot(col, col_wrap)`: faceted plots (multiple subplots by category)

**Example Workflow**: Load North American air temperature dataset; select subsets (isel); apply calculations (e.g., Kelvin to Celsius conversion); plot with customized colormap and levels.

**Other Types**: Streamplot, Quiver, Scatter (http://xarray.pydata.org/en/stable/user-guide/plotting.html)

## Cartopy Map Production

### Map Projection Basics

Create figure + axes with projection: `plt.axes(projection=ccrs.PlateCarree())` (or Robinson, Stereographic, etc.)

**Available Projections**: https://scitools.org.uk/cartopy/docs/latest/crs/projections.html

**Natural Features** (cartopy.feature):
- `LAND` (facecolor, edgecolor)
- `LAKES` (edgecolor, linewidth, facecolor)
- `OCEAN` (color)
- `NaturalEarthFeature()`: countries, borders at scales 10m/50m/110m

**Gridlines**: `.gridlines(draw_labels=True, linestyle)` with `mticker.FixedLocator()` custom spacing; control labels: `xlabels_top`, `ylabels_right`, `ylabel_style` (size), `xlabel_style`

### Data Visualization on Maps

**Key Parameters**:
- `transform=ccrs.PlateCarree()`: data coordinate system (vs. projection = map display system)
- `.plot.imshow()`: raster-based plotting (xarray compatible); handles longitude coordinate adjustment (wrap -180 to 180)
- `.plot.pcolormesh()`: mesh grid plotting (compatibility issues with new Cartopy/matplotlib; use imshow as workaround)
- Colormaps: cmaps.sunshine_diff_12lev (custom NCL colormaps)
- Colorbar control: `orientation`, `shrink`, `pad`, `aspect`, `ticks`

**Cartopy/xarray Integration**:
```python
data.plot.imshow(ax=ax, transform=ccrs.PlateCarree(), cmap=cmap, levels=levels, add_colorbar=False)
```

### Regional Masking with regionmask

**Mask Types**:
- Land mask: `regionmask.defined_regions.natural_earth.land_110.mask(data)`
- Country mask: `regionmask.defined_regions.natural_earth.countries_110.mask(data, lon_name="lon", lat_name="lat")`

**Application**: Filter data with `.where(mask==code)` before plotting; example: land-only plots (`where(landmask==0)`), country-specific maps (`where(countrymask==4)` for U.S.)

**Statistics**: Weighted averaging over regions: `.weighted(np.cos(np.deg2rad(lat))).mean()`

### Advanced Layouts

**Multiple Maps Shared Colorbar**:
- Create subplots: `fig.add_subplot(projection=ccrs.PlateCarree())`
- Apply same norm to all: `mpl.colors.BoundaryNorm(levels, ncolors=len(levels)+1, extend='both')`
- Single colorbar spanning axes: `plt.colorbar(h, ax=(ax0, ax1), orientation='horizontal')`

**GridSpec Custom Layouts**:
- `gridspec.GridSpec(ncols, nrows, width_ratios, hspace, wspace)`
- Mix map (large) + line plot (narrow zonal average)
- Example: `width_ratios=[10,1]`, `wspace=-0.1` for tight side-by-side layout

**Line Plots (Zonal Averages)**:
- Extract mean along dimension: `data.mean('lon')`
- Customize axes: `yaxis.set_ticks_position("right")`, `yaxis.set_label_position("right")`

### Statistical Significance Visualization

**Hatching Overlay**:
```python
pvalue.plot.contourf(ax=ax, colors='none', levels=[0, 0.05, 1], 
                    hatches=['....', None], add_colorbar=False, alpha=0)
```
Shows p<0.05 regions with hatch pattern over base data.

## Final Publication Output

**Annotation**: `.annotate('label', xy=(0,1.05), xycoords='axes fraction', fontsize=14)` for subplot labels

**File Export**: `plt.savefig("path.pdf", bbox_inches='tight')` for publication-quality PDF

**Example Final Plot**: 2x2 grid with annual mean + Q95 wet bulb temperature maps, corresponding zonal average line plots, shared colorbar—suitable for peer-reviewed publication.

## Learning Outcomes

- Create quick exploratory plots with xarray
- Produce publication-quality geographic maps with Cartopy
- Apply map projections and geographic features
- Mask and filter regional data
- Design complex multi-panel figures with custom layouts
- Export high-resolution publication materials
