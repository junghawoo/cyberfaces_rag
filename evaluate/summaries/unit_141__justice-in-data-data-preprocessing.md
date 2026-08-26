---
title: "Justice in Data: Data Preprocessing"
unit_id: 141
course_id: 10
level: "Foundation"
slug: justice-in-data-data-preprocessing
is_course: 0
---

# Justice in Data: Data Preprocessing

## Summary

Foundation-level boot-camp module on data preprocessing in Python, part of the "Justice in Data" course. Combines slide deck `Data_Preprocessing.pdf`, a pre-survey, and a recorded lecture/hands-on session.

Slides define data preprocessing as preparing data for analysis by cleaning, transforming, and selecting relevant features: handling missing/duplicate data, feature scaling, encoding categorical data, dimensionality reduction, and splitting into training/testing sets. Emphasizes improving data accuracy, handling outliers (via normalization/standardization), enabling feature scaling, and encoding categorical data into numerical form for machine-learning algorithms. Names key Python libraries: NumPy, Pandas, Scikit-learn, and Matplotlib.

External resources: Data Preprocessing Pre-Survey (utaedu.questionpro.com survey link) and a Data Preprocessing Recording (YouTube video wrY1YBKfmwU, https://www.youtube.com/watch?v=wrY1YBKfmwU). The recorded session (instructor references Dr. Eisner, Jessica, Tanner, Janae, Junaid's drone/thermal-imaging outlier example in Texas) walks through preprocessing concepts including how to decide whether to remove or keep outliers (physical-plausibility and data-collection-error reality checks), scaling geospatial/remote-sensing data to a common spatial resolution, and scaling time-series to a common temporal resolution.

Hands-on activities run in Jupyter notebooks on the MyGeoHub platform (mygeohub), covering two notebooks. Activity 1 uses a building energy dataset (columns like `prim_class_Jalen`, univ_lab, office buildings, university dorms) loaded from a GitHub CSV (`file_name.csv`): demonstrates `pandas`, `df.head()`, `df.tail()`, detecting NaN (not-a-number) values, `df.dropna()` on single columns, filtering columns by splitting column names on underscore (string split, zero-indexing) to select only Prim class buildings, `fillna(0)` to replace NaNs with zeros, plotting with matplotlib.pyplot (plt) and matplotlib.dates (mdates), legend placement (loc='best'/'northwest'), and converting a string timestamp column to datetime via `pd.to_datetime` (with UTC timezone, e.g. January 1 2010). Activity 2 uses a USGS water-quality/discharge dataset (`measurements.csv`, site 05057000) with columns measured_rating_diff (good/fair/bad), party_name (e.g. lph), control_type: demonstrates boolean filtering `df[df.measured_rating_diff=='good']`, `reset_index()`, the `.isin(options)` method, combining multiple conditions with the `&` operator, and other conditional operators (==, !=, >, <, >=, <=). Discusses efficiency of reading CSVs with `pd.read_csv` versus copying/pasting data, and doing preprocessing in Python versus Excel find-and-replace.

## Summarized attachments

- **Data Preprocessing Slides** (Data_Preprocessing.pdf, file): Slide presentation defining data preprocessing steps (cleaning, transforming, selecting relevant features), handling missing/duplicate data, scaling features, encoding categorical data, reducing dimensionality, and splitting data into training/testing sets with emphasis on importance for data accuracy, outlier handling, feature scaling, and categorical data encoding using Python libraries NumPy, Pandas, Scikit-learn, and Matplotlib.

- **Data Preprocessing Pre-Survey** (https://utaedu.questionpro.com/a/TakeSurvey?tt=MxlZJPX44gQECHrPeIW9eQ%3D%3D, remote resource): Pre-course assessment survey to establish baseline knowledge and measure content comprehension.

- **Data Preprocessing Recording** (https://www.youtube.com/watch?v=wrY1YBKfmwU, remote resource): Recorded lecture session covering data preprocessing concepts including outlier decision-making, data cleaning techniques, Python libraries for preprocessing, and hands-on demonstrations of removing NaN values, filtering columns by name patterns, and boolean filtering with multiple conditions.
