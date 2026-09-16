---
title: "Python Fundamentals for Remote Sensing Applications"
unit_id: 210
course_id: 0
level: "Foundation"
slug: introduction-to-python-core-concepts-for-remote-sensing-applications
is_course: 0
objectives:
  - "Equip students with Python skills for automating the retrieval of meteorological data from the geostationary satellites."
  - "Introduce key Python libraries for handling remote sensing data."
---

# Python Fundamentals for Remote Sensing Applications

Three-lecture module on Python programming for remote sensing, emphasizing geostationary satellite data acquisition and analysis. Instructors: Mohamed Abdelkader, Jorge Bravo, Marouane Temimi (Civil, Environmental, Ocean Engineering, Stevens Institute); Jibin Joseph (Purdue Civil Engineering). Email: mabdelka@stevens.edu. Platform: mygeohub.org Jupyter Notebook with Anaconda 5.1. GitHub: MAbdelkader94/Python-for-RS-applications.

## Lecture 1: Introduction to Python Core Concepts

Covers foundational Python syntax and data manipulation for meteorological analysis using geostationary satellite data. Topics include: Python interactive environment, variable assignment and type flexibility, print functions for data reporting.

**Data Types**: Integers (hurricane category on Saffir-Simpson scale 1-5), floats/decimals (precise temperature readings in °C, humidity levels, precipitation amounts), strings (satellite names: GOES-16, GOES-17, Himawari-8, Meteosat-11, Elektro-L).

**String Formatting**: Concatenation, .format() method for structured output, f-strings (f"Hello, this is data from the {satellite} satellite"). Text formatting enhances clarity when labeling satellite imagery or creating weather map annotations.

**Collections**: Lists (store time series meteorological data: temperature, wind speed observations from geostationary satellites; mixed data types including booleans for retrieval success status, floats for readings, strings for parameter names, nested arrays). Tuples (immutable collections for satellite instruments: ABI, GLM, SEISS, EXIS, SUVI, MAG, SWEAP; fixed geographical coordinates; constants in meteorological calculations). Dictionaries (key-value pairs for structured meteorological data: Temperature (°C), Humidity (%), Wind Speed (km/h), Cloud Coverage (%), Precipitation (mm), UV Index, Atmospheric Pressure (hPa), Dew Point (°C)).

**Iterations**: For loops (enumerate dictionary keys; process key-value pairs via .items(); iterate over time series data). While loops (continue block execution while condition holds). Demonstrations: iterating weather_parameters dictionary; adding entries (Atmospheric Pressure, Dew Point, new meteorological parameters); constructing formatted output sentences using .format() with dynamic data insertion.

**Student Assignment**: Add new weather parameter (e.g., Solar Radiation, Visibility) to weather_parameters dictionary; create f-string formatted message; generate PDF submission with updated dictionary + formatted message + Python script + readme documentation.

## Lecture 2: Web Scraping and Data Download

Focuses on automating meteorological data acquisition from GOES-R series (GOES-16, GOES-17) via web scraping and cloud storage access.

**Manual Download Interface**: Brian K. Blaylock GOES-16 Data Download (https://home.chpc.utah.edu/~u0553130/Brian_Blaylock/cgi-bin/goes16_download.cgi). NOAA GOES on AWS documentation.

**Web Scraping Workflow**: Import datetime, requests, BeautifulSoup (bs4), xml.dom.minidom. Construct URL with parameters: source, satellite (GOES-16, GOES-17), domain (F=full disk, M=mesoscale), product (ABI-L1b-Rad=radiance, ABI-L2-CMI=cloud moisture imagery), date/time. Use requests.get() to retrieve HTML content; parse with BeautifulSoup. Extract download links (href attributes) from parsed HTML tags. Filter files by time difference from requested datetime (timestamp format: s%Y%j%H%M%S%f).

**Sequential Download**: Iterate filenames; construct AWS S3 URLs (https://noaa-goes{sat}.s3.amazonaws.com/{prd}{str}/{tme:%Y}/{tme:%j}/{tme:%H}/{filename}.nc). Use urllib.request.urlretrieve() or requests.get() for HTTP downloads. Optional: progressbar callback for tracking download progress.

**Parallel Download via Threading**: Define download_dem_file_func() for individual file retrieval. Create threading.Thread objects for concurrent downloads. Use thread.join() to synchronize completion. Expected speedup: 3x for multi-file acquisitions.

**AWS S3 Access**: Boto3 client (import boto3); specify S3 bucket (noaa-goes16), remote file path (ABI-L2-MCMIPF/YYYY/JJJ/HH/filename.nc), local destination. Use client.download_file() to retrieve from S3 directly.

**Libraries**: datetime, requests, BeautifulSoup, urllib, boto3, os.

## Lecture 3: Reading NetCDF Data with Python

Two complementary approaches for handling Network Common Data Form (NetCDF) files containing multidimensional remote sensing datasets.

**netCDF4 Library**: Dataset class for opening/inspecting/manipulating NetCDF files. Open file: Dataset(filepath). Access variables (e.g., CMI=Cloud and Moisture Imagery). Explore metadata: dimensions, variables, attributes. Modify existing data or create new datasets. Applications: climate analysis, weather prediction, environmental monitoring.

**Xarray Library**: Simplifies labeled multidimensional array handling. Load dataset: xarray.open_dataset(filepath). Display contents (dimensions, coordinates, variables, attributes). Plot directly: dataset['variable_name'].plot(). Access variable attributes. Example workflow: load ABI-L2-CMIPC data, display CMI variable properties.

**Data Product Examples**: ABI-L2-CMIPC (Cloud Moisture Imagery Product, mesoscale/CONUS domain). File naming: OR_ABI-L2-CMIPC-M3C13_G16_s{start_datetime}_e{end_datetime}_c{creation_datetime}.nc. Multiple channels (C01-C16) available; C13 = 10.3 μm infrared band.

**Visualization Techniques**: Matplotlib imshow() with custom colormaps (temperature-based: white→green→red→black gradient, 64-color palette). matplotlib.ticker for axis customization. Cartopy for geospatial projections.

**Geostationary Projection**: Extract projection metadata: goes_imager_projection variable. Parameters: satellite_height (m), longitude_of_projection_origin (central_lon), semi_major/semi_minor axes (Earth's ellipsoid), sweep_angle_axis. Scale x/y coordinates by satellite height to obtain physical distances. Create ccrs.Globe(semimajor_axis, semiminor_axis). Initialize ccrs.Geostationary(central_longitude, satellite_height, sweep_axis). Add subplot with projection; imshow() with transform parameter to apply geostationary coordinate system.

**Batch Processing**: Use glob to retrieve all .nc files matching pattern. Iterate through multiple files; apply projection transformations; generate multi-panel visualizations.

**Key Output Parameters**: Cloud Moisture Imagery (CMI) in brightness temperature (K or °C); infrared radiance data (ABI-L1b). Visualization: colored imagery with custom color-temperature mapping; geographic extent defined by x/y extent arrays; origin='upper' for satellite image coordinates.

**Libraries**: netCDF4 (Dataset), xarray, matplotlib, numpy (linspace, array operations), cartopy (ccrs), glob.

## Remote Sensing Context

**Data Sources**: USGS AWS (prd-tnm.s3.amazonaws.com), NOAA GOES on AWS (noaa-goes16.s3.amazonaws.com, noaa-goes17.s3.amazonaws.com).

**Geostationary Satellites**: GOES-16, GOES-17 (NOAA/USA), Himawari-8 (JMA/Japan), Meteosat-11 (EUMETSAT/Europe), Elektro-L (Roscosmos/Russia).

**Meteorological Parameters**: Temperature (°C), Humidity (%), Wind Speed (m/s or km/h), Cloud Coverage (%), Precipitation (mm), UV Index, Atmospheric Pressure (hPa), Dew Point (°C), Solar Radiation (W/m²), Visibility (km).

**Learning Outcomes**: Automate meteorological data retrieval; manipulate geostationary satellite imagery; understand NetCDF data structure; apply Python to climate/weather analysis; visualize remote sensing products on geographic projections.

**References**: Guide to GOES-R Series Data, GOES ABI Realtime Imagery, GOES Image Viewer, netCDF4-python documentation, Xarray documentation, Python datetime library, requests/urllib documentation.

## Summarized attachments
- **Introduction to Python_Core Concepts for RS Applications** (`Introduction to Python_Core Concepts for RS Applications.pdf`, file): Foundational tutorial on Python syntax and data types (integers, floats, strings, lists, tuples, dictionaries) with applications to meteorological data analysis using geostationary satellites. Covers variable assignment, operations, string formatting, collections manipulation, iterations with for loops, and assignment requirements.
- **Lecture 1: Introduction to Python: Core Concepts for Remote Sensing Applications** (https://github.com/MAbdelkader94/Python-for-RS-applications/blob/main/Lecture_01/Introduction_to_Python_Core%20Concepts_for_RS_Applications.ipynb, notebook): Interactive Jupyter notebook demonstrating Python fundamentals including variable types, data structures, and string formatting with practical examples using geostationary satellite metadata (GOES-16, satellite instruments) and weather parameters.
- **Lecture 2: Web Scraping and Data Download** (https://github.com/MAbdelkader94/Python-for-RS-applications/blob/main/Lecture_02/Web%20Scraping%20and%20Data%20Download.ipynb, notebook): Jupyter notebook on automating GOES-R data acquisition through web scraping and AWS S3 access. Demonstrates datetime handling, HTML parsing with BeautifulSoup, URL construction for NOAA data, HTTP requests for downloads, and Boto3 S3 client usage for direct cloud storage retrieval.
- **Lecture 3: Reading NetCDF Data with Python** (https://github.com/MAbdelkader94/Python-for-RS-applications/blob/main/Lecture_03/Reading_NetCDF_Data_with_Python.ipynb, notebook): Jupyter notebook covering NetCDF data handling using netCDF4 and Xarray libraries. Includes dataset loading, variable access, visualization with custom colormaps, cartopy-based geostationary projections, and batch processing of satellite imagery files.
