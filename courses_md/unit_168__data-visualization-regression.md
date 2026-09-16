---
title: "Data, visualization, & regression"
unit_id: 168
course_id: 6
level: "Foundation"
slug: data-visualization-regression
is_course: 0
---

# Data, visualization, & regression

## Fetched resources (external URLs)

### Homework (notebook)
*URL:* https://github.com/PurdueCyberTraining/python4env/blob/main/Lec6-HW6/HW6_DataVizRegression.ipynb

# Homework 6: Finding, visualizing, and regressing data
ENVR 890-001: Python for Environmental Research, Fall 2020

By Andrew Hamilton. 

**Due October 23 before class**

This assignment is open ended. I'd like you to do the following:
1. Find an interesting dataset related to the environmental science, engineering, and/or public health. A number of important online data sources are listed in Lecture 7 (and I'm sure I missed some others). Alternatively, you can use a dataset that you have from your own research.
1. Read that dataset into Python, and clean it if necessary (e.g., NAN's or weird anomalous values)
1. Perform any interesting analysis or groupings if you want to (e.g., annual or monthly groupings). Not necessary if this isn't helpful for your data.
1. Create at least two different visualizations (e.g., line plots, scatter plots, histograms, box plots, etc.)
1. Perform at least two regressions using your data. These don't necessarily need to be valid and/or interesting statistically, I just want to see that you know how to do it. But of course interesting is better!

Send me your results in a well-documented Jupyter notebook describing what you did.

### Notes: Findable, Interoperable, Accessible, & Reusable (FAIR) environmental data (notebook)
*URL:* https://github.com/PurdueCyberTraining/python4env/blob/main/Lec6-0-EnvData/Lec7_EnvironmentalData.ipynb

# Lecture 7: FAIR data and environmental research
ENVR 890-001: Python for Environmental Research, Fall 2020

October 9, 2020

By Andrew Hamilton. Some material adapted from Matthew Huber & Ashley Dicks (Purdue University).

Thanks to Drs. Venkatesh Merwade, Matthew Huber, Carol Song, and Lan Zhao at Purdue University, and the FACT Cyber Training Fellowship (funded under NSF Award #1829764), for training me in FAIR data and science best practices. 

### Summary
The use and production of data is fundamental to all research, including environmental science, engineering, and health. Data are stored in a wide variety of formats and locations, from curated online databases to individual spreadsheets to pdf tables. In this lesson, we will learn how to download data from a number of online repositories in order to use in our research. We will also learn about FAIR data standards and best practices for making your own data available to other researchers.

### Major public environmental data sources
1. [USGS National Water Information System](https://waterdata.usgs.gov/nwis)
    - Stream flow, water quality, water use, etc.
    - Usually easier to search for specific location (e.g., [Bolin Creek](https://waterdata.usgs.gov/nwis/uv?site_no=0209734440))
1. [Natural Resources Conservation Service (NRCS)](https://www.wcc.nrcs.usda.gov/snow/)
    - Snow depth, water supply forecasts, etc.
1. [NOAA National Centers for Environmental Information](https://www.ncdc.noaa.gov/data-access)
    - Historical weather data, severe weather database, etc.
1. [EPA Air Data](https://www.epa.gov/outdoor-air-quality-data)
    - Current & historical air quality data
    - Automated plot generation & data downloads
1. [EPA Dataset Giveaway](https://edg.epa.gov/metadata/catalog/main/home.page)
    - Many different datasets on climate change, locations of Superfund sites, environmental justice, etc.
1. [CDC National Center for Environmental Health](https://www.cdc.gov/nceh/data.htm)
    - Many datasets about asthma, lead poisoning, nutrition, etc.
1. [Organization for Co-operation and Economic Development (OECD) Data](https://data.oecd.org/)
    - Country-scale data on environment (air pollution, water withdrawals, CO2 emissions, etc.)
    - Energy, healthcare, development, etc.
1. [The National Map (USGS)](https://viewer.nationalmap.gov/basic/)
    - National Hydrography Dataset
    - Digital Elevation Maps
    - Place names, transportation networks
1. [Multi-Resolution Land Characteristics Consortium (MRLC)](https://www.mrlc.gov/data?f%5B0%5D=category%3Aland%20cover)
    - Land use/land cover datasets
1. [National Center for Atmospheric Research (NCAR) Research Data Archive](https://rda.ucar.edu/)
    - Tons of gridded oceanic & atmospheric datasets & reanalyses

### 4 ways to upload data into Python
1. Download csv/xlsx, and use ``pd.read_csv()``, ``pd.read_excel()``

1. Copy online table into Excel, then follow #1
    - e.g., USGS "Tab-separated" output format
    
1. Using special Python APIs
    - [EPA Envirofacts Data Service API](https://www.epa.gov/enviro/web-services)
    - These APIs can be pretty tricky to use, and each one will be different. They often require special python packages and/or an account with the provider. But if you need to download a lot of different datasets, or get updated data regularly, it may be worthwhile to figure out.
    - [Here](https://techrando.com/2019/07/04/how-to-use-the-environmental-protection-agencys-epas-api-to-pull-data/) is an example of how to use with EPA Envirofacts, but I haven't actually used it.
    - [Here](http://kapadia.github.io/usgs/) is a package for interfacing with the USGS API, but I haven't used this either.
    
1. Query online table directly using url (often the most convenient)

We will use USGS streamflow data from Bolin Creek in Chapel Hill, NC. If you click on the Bolin Creek link above on the USGS website, you will find information about how to download data from this location. One of the options for any query is to get data in csv format, which will open a new browser window with a table of data. For example, [here](https://nwis.waterdata.usgs.gov/nwis/uv?cb_00060=on&cb_00065=on&format=rdb&site_no=0209734440&period=&begin_date=2019-10-02&end_date=2020-10-09). Pandas allows us to access this webpage and access the data directly, rather than having to first save a csv file to our computer:

```python
import pandas as pd
import numpy as np
```

```python
### Use USGS Bolin Creek website to get tab-separated data. Fill in address, header, and delimiter
data_address = 'https://nwis.waterdata.usgs.gov/nwis/uv?cb_00060=on&cb_00065=on&format=rdb&site_no=0209734440&period=&begin_date=2019-10-02&end_date=2020-10-09'
header = 30
delimiter = '\t'
df = pd.read_csv(data_address, header=header, delimiter=delimiter)
```

```python
df = df.iloc[1:, :]
df
```

_result:_
```
agency_cd     site_no          datetime tz_cd 89527_00065  \
1          USGS  0209734440  2019-10-02 00:00   EDT        1.21   
2          USGS  0209734440  2019-10-02 00:15   EDT        1.21   
3          USGS  0209734440  2019-10-02 00:30   EDT        1.21   
4          USGS  0209734440  2019-10-02 00:45   EDT        1.20   
5          USGS  0209734440  2019-10-02 01:00   EDT        1.21   
...         ...         ...               ...   ...         ...   
35395      USGS  0209734440  2020-10-09 10:15   EDT        1.62   
35396      USGS  0209734440  2020-10-09 10:30   EDT        1.62   
35397      USGS  0209734440  2020-10-09 10:45   EDT        1.61   
35398      USGS  0209734440  2020-10-09 11:00   EDT        1.62   
35399      USGS  0209734440  2020-10-09 11:15   EDT        1.63   

      89527_00065_cd 89528_00060 89528_00060_cd  
1                  A        0.00            A:R  
2                  A        0.00            A:R  
3                  A        0.00            A:R  
4                  A        0.00            A:R  
5                  A        0.00            A:R  
...              ...         ...            ...  
35395              P        1.19              P  
35396              P        1.19              P  
35397              P        1.10              P  
35398              P        1.19              P  
35399              P        1.28              P  

[35399 rows x 8 columns]
```

Once you have an example url, you can often figure out how to automatically get data for new dates or locations. For example, how would you change the query to download data from January 1, 2015, to the present?

```python
## To save the data for later, use pandas to_csv()
df.to_csv('bolin_creek.csv', sep=',', index=False)
```

### FAIR research
<img src="stall_fair.PNG" style="width: 400px;" />(Image cred: Stall, 2018)

**FAIR** data is:
- **F**indable: The datasets and resources should be easily located by humans and computers
- **A**ccessible: After the dataset is found, the user needs to be able to easily access the datasets
- **I**nteroperable: The datasets need to be in a format that is usable by others, therefore needs to satisfy the following 
- **R**eusable: The datasets need to be able to be used by various people, therefore must have clear metadata

<img src="wilkinson2016_box2.PNG" style="width: 800px;" />(Image cred: Wilkinson et al., 2016)

<img src="huber_fair.PNG" style="width: 600px;" />(Image cred: Matthew Huber et al., [*MyGeoHub*](https://mygeohub.org/cybertraining))

<img src="stall_dataChallenges.PNG" style="width: 800px;" />(Image cred: Stall, 2018)

<img src="rosenberg2020_fig1.PNG" style="width: 600px;" />(Image cred: Rosenberg et al., 2020)

<img src="hutton2016_fig1.PNG" style="width: 800px;" />(Image cred: Hutton et al., 2016)

<img src="stall_dataEcosystem.PNG" style="width: 600px;" />(Image cred: Stall, 2018)

[Coalition for Publishing Data in the Earth and Space Sciences, Enabling FAIR Data Project](https://copdess.org/enabling-fair-data-project/)
- Scientific orgs: American Geophysical Union(AGU), European Geosciences Union (AGU), etc.
- Publishers: AGU, PNAS, Nature, Science, Elsevier, Wiley, etc.
- Repositories & Data Infrastructure

**More reading on FAIR/open data and science:**
- AGU FAIR data working group presentation ([Stall, 2018, Big Data Interagency Working Group](https://www.nitrd.gov/nitrdgroups/images/0/02/Enabling-FAIR-Data-ESES-ShelleyStall.pdf))
- FAIR guiding principles for scientific data management and stewardship ([Wilkinson et al, 2020, *Scientific Data*](https://www.nature.com/articles/sdata201618%22))
- MyGeoHub description of FAIR principles ([Merwade, Huber, Song, Huang, Zhao, *MyGeoHub*](https://mygeohub.org/cybertraining/fair))
- Most computational hydrology is not reproducible, so is it really science? ([Hutton et al., 2016, *Water Resources Research*](https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1002/2016WR019285))
- History, promises, and challenges of open science/open data for public health research ([Huston et al., 2019, *Canada Communicable Disease Report*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6781855/#:~:text=Open%20Data%20is%20based%20on,that%20inform%20and%20support%20them))
- Best practices for performing reproducible research, focused on complex computer modeling workflows ([Rosenberg et al., 2020, *Journal of Water Resources Planning and Management*](https://ascelibrary.org/doi/full/10.1061/%28ASCE%29WR.1943-5452.0001215))
- Great lecture on how scientists can improve reproducibility/reusability by learning from the open-source software community ([McElreath, 2020, *YouTube*](https://www.youtube.com/watch?v=zwRdO9_GGhY&t=0s&ab_channel=RichardMcElreath))

### Sharing your research products
Repositories for sharing research products (data and/or code)
1. [HydroShare](https://www.hydroshare.org/landingPage/)
1. [Nature Scientific Data list of repositories](https://www.nature.com/sdata/policies/repositories#climate)
1. GitHub + Zenodo
    - e.g., my [GitHub repository](https://github.com/ahamilton144/hamilton-2020-managing-financial-risk-tradeoffs-for-hydropower) for code associated with a research paper. See "Tags" for snapshot versions associated with each submission. Each snapshot is downloadable on Zenodo and has a permanent DOIs.

### Notes: Regression (notebook)
*URL:* https://github.com/PurdueCyberTraining/python4env/blob/main/Lec6-2-Regression/Lec8_Regression.ipynb

# Lecture 8: Regression
ENVR 890-001: Python for Environmental Research, Fall 2020

October 16, 2020

By Andrew Hamilton.

### Summary
Linear regression is ubiquitous across a wide range of science, engineering, and public health applications. This is not a statistics class, so we won't spend much time on the theory. Rather, we will focus on implementing linear regression and related concepts in Python. However, you should absolutely learn some statistics (or consult with an expert) before using these concepts in your research! 

### Read in our data

I downloaded from the [EPA Acid Rain emissions reporting database](https://ampd.epa.gov/ampd/). This dataset contains statewide quarterly emissions of SO2, NOx, and CO2 from eligible coal plants in NC and SC from 1997-2020.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm

df = pd.read_csv('NC_SC_acid_rain_emissions.csv', sep=',', header=1)
df.columns = ['state', 'year', 'quarter', 'program', 'so2', 'nox', 'co2', 'heatinput']
df
```

_result:_
```
state  year  quarter program       so2        nox           co2  \
0      NC  2017        1     ARP  3088.057   6627.984  1.177807e+07   
1      NC  2017        2     ARP  3771.224   7770.051  1.259458e+07   
2      NC  2017        3     ARP  6054.505  10265.869  1.707442e+07   
3      NC  2017        4     ARP  3307.317   7532.182  1.140865e+07   
4      NC  2018        1     ARP  3930.952   8266.694  1.362151e+07   
..    ...   ...      ...     ...       ...        ...           ...   
185    SC  2015        4     ARP  1274.022   2197.494  6.405202e+06   
186    SC  2016        1     ARP  2079.528   2809.411  7.043278e+06   
187    SC  2016        2     ARP  1954.405   2613.211  7.139541e+06   
188    SC  2016        3     ARP  2521.992   3559.830  9.782372e+06   
189    SC  2016        4     ARP  1422.015   2311.351  6.182728e+06   

        heatinput  
0    1.439023e+08  
1    1.495152e+08  
2    2.002756e+08  
3    1.421079e+08  
4    1.649823e+08  
..            ...  
185  7.870638e+07  
186  8.058031e+07  
187  8.186110e+07  
188  1.142828e+08  
189  7.385218e+07  

[190 rows x 8 columns]
```

**Scatterplot to look at data, NOx vs year**

```python
sns.scatterplot('year', 'nox', data=df)
```

_result:_
```
<AxesSubplot:xlabel='year', ylabel='nox'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

### Linear regression, NOx against year

In general, we can write linear regression as:

$$y_i = \beta_0 + \beta_1 x_{i1} + ... + \beta_p x_{ip} + \varepsilon_i$$

for all data points $i$ with independent variables (regressors) $\mathbf{x}$ and dependent variable $y$. Ordinary Least Squares (OLS) tries to find the coefficients $\boldsymbol{\beta}$ that minimize the sum of the squared errors, $\boldsymbol{\varepsilon}$.

In the current context, we can simplify this as:

$$NOx_i = \beta_0 + \beta_1 YEAR_{i} + \varepsilon_i$$

where $\beta_0$ is the intercept and $\beta_1$ is the slope of the regression line.

```python
df.head()
```

_result:_
```
state  year  quarter program       so2        nox          co2    heatinput
0    NC  2017        1     ARP  3088.057   6627.984  11778066.24  143902340.0
1    NC  2017        2     ARP  3771.224   7770.051  12594579.74  149515188.3
2    NC  2017        3     ARP  6054.505  10265.869  17074422.27  200275610.8
3    NC  2017        4     ARP  3307.317   7532.182  11408654.15  142107926.7
4    NC  2018        1     ARP  3930.952   8266.694  13621514.75  164982269.3
```

```python
### Define linear regression object, with equation written in quotes (no need to write constant term)
lm_nox_year = sm.ols('nox ~ year', data=df)
lm_nox_year
```

_result:_
```
<statsmodels.regression.linear_model.OLS at 0x7f2d3680d940>
```

```python
### run regression
lm_nox_year_fit = lm_nox_year.fit()
lm_nox_year_fit
```

_result:_
```
<statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7f2cd74f5d68>
```

```python
### print regression summary statistics
print(lm_nox_year_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                    nox   R-squared:                       0.601
Model:                            OLS   Adj. R-squared:                  0.599
Method:                 Least Squares   F-statistic:                     283.2
Date:                Mon, 25 Jan 2021   Prob (F-statistic):           2.29e-39
Time:                        17:41:19   Log-Likelihood:                -2017.0
No. Observations:                 190   AIC:                             4038.
Df Residuals:                     188   BIC:                             4045.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept   3.564e+06   2.11e+05     16.910      0.000    3.15e+06    3.98e+06
year       -1766.3185    104.952    -16.830      0.000   -1973.354   -1559.283
==============================================================================
Omnibus:                       57.876   Durbin-Watson:                   0.300
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              127.782
Skew:                           1.392   Prob(JB):                     1.79e-28
Kurtosis:                       5.896   Cond. No.                     5.88e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.88e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
### regression coefficients (betas)
lm_nox_year_fit.params
```

_result:_
```
Intercept    3.564446e+06
year        -1.766318e+03
dtype: float64
```

```python
### get predicted nox as a function of year based on regression
def predict_nox_year(params, years):
    return params[0] + params[1] * years
```

```python
years = np.arange(1995, 2021)
prediction = predict_nox_year(lm_nox_year_fit.params, years)
prediction
```

_result:_
```
array([ 4.06404353e+04,  3.88741168e+04,  3.71077983e+04,  3.53414799e+04,
        3.35751614e+04,  3.18088429e+04,  3.00425244e+04,  2.82762060e+04,
        2.65098875e+04,  2.47435690e+04,  2.29772506e+04,  2.12109321e+04,
        1.94446136e+04,  1.76782952e+04,  1.59119767e+04,  1.41456582e+04,
        1.23793398e+04,  1.06130213e+04,  8.84670282e+03,  7.08038435e+03,
        5.31406588e+03,  3.54774741e+03,  1.78142894e+03,  1.51104693e+01,
       -1.75120800e+03, -3.51752647e+03])
```

```python
sns.scatterplot('year', 'nox', data=df)
plt.plot(years, prediction, color='k')
plt.ylabel('NOx emissions (tons)')
plt.xlabel('Year')
```

_result:_
```
Text(0.5, 0, 'Year')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Check if regression conditions are met - normality?**

```python
plt.hist(df['nox'])
```

_result:_
```
(array([67., 52., 29., 10., 12.,  8.,  4.,  2.,  3.,  3.]),
 array([  947.276 ,  8392.7264, 15838.1768, 23283.6272, 30729.0776,
        38174.528 , 45619.9784, 53065.4288, 60510.8792, 67956.3296,
        75401.78  ]),
 <BarContainer object of 10 artists>)
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Try log transform of data**

```python
df['nox_log'] = np.log(df['nox'])
df.head()
```

_result:_
```
state  year  quarter program       so2        nox          co2    heatinput  \
0    NC  2017        1     ARP  3088.057   6627.984  11778066.24  143902340.0   
1    NC  2017        2     ARP  3771.224   7770.051  12594579.74  149515188.3   
2    NC  2017        3     ARP  6054.505  10265.869  17074422.27  200275610.8   
3    NC  2017        4     ARP  3307.317   7532.182  11408654.15  142107926.7   
4    NC  2018        1     ARP  3930.952   8266.694  13621514.75  164982269.3   

    nox_log  
0  8.799056  
1  8.958032  
2  9.236580  
3  8.926940  
4  9.019990
```

```python
plt.figure()
sns.scatterplot('year', 'nox_log', data=df)
plt.ylabel('log(NOx emissions (tons))')
plt.xlabel('Year')

plt.figure()
plt.hist(df['nox_log'])
```

_result:_
```
(array([ 1.,  6., 21., 13., 26., 35., 33., 24., 21., 10.]),
 array([ 6.8535905 ,  7.29129006,  7.72898963,  8.1666892 ,  8.60438876,
         9.04208833,  9.4797879 ,  9.91748746, 10.35518703, 10.79288659,
        11.23058616]),
 <BarContainer object of 10 artists>)
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**QQ-plot**

```python
from statsmodels.graphics.gofplots import qqplot
fig = qqplot(df['nox_log'], line='s')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Test for normality with Shapiro-Wilk test**

```python
from scipy.stats import shapiro
stat, p = shapiro(df['nox_log'])
print(stat, p)
```

_output:_
```
0.9855313897132874 0.048119135200977325
```

**Try Box-Cox transformation**

```python
from scipy.stats import boxcox
df['nox_bc'], lam = boxcox(df['nox'])
lam
```

_result:_
```
0.06979101291062871
```

```python
plt.figure()
sns.scatterplot('year', 'nox_bc', data=df)
plt.ylabel('NOx emissions (transformed, unitless)')
plt.xlabel('Year')

plt.figure()
plt.hist(df['nox_bc'])

plt.figure()
fig = qqplot(df['nox_bc'], line='s')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

_result:_
```
<Figure size 432x288 with 0 Axes>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
stat, p = shapiro(df['nox_bc'])
print(stat, p)
```

_output:_
```
0.9870161414146423 0.07854940742254257
```

```python
lm_nox_year = sm.ols('nox_bc ~ year', data=df)
lm_nox_year_fit = lm_nox_year.fit()
print(lm_nox_year_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 nox_bc   R-squared:                       0.753
Model:                            OLS   Adj. R-squared:                  0.752
Method:                 Least Squares   F-statistic:                     574.6
Date:                Mon, 25 Jan 2021   Prob (F-statistic):           4.55e-59
Time:                        17:41:21   Log-Likelihood:                -246.62
No. Observations:                 190   AIC:                             497.2
Df Residuals:                     188   BIC:                             503.7
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    466.9815     18.929     24.670      0.000     429.641     504.322
year          -0.2259      0.009    -23.972      0.000      -0.245      -0.207
==============================================================================
Omnibus:                       26.575   Durbin-Watson:                   0.399
Prob(Omnibus):                  0.000   Jarque-Bera (JB):                7.850
Skew:                           0.143   Prob(JB):                       0.0197
Kurtosis:                       2.046   Cond. No.                     5.88e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.88e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
prediction = predict_nox_year(lm_nox_year_fit.params, years)
sns.scatterplot('year', 'nox_bc', data=df)
plt.plot(years, prediction, color='k')
plt.ylabel('NOx emissions (transformed, unitless)')
plt.xlabel('Year')
```

_result:_
```
Text(0.5, 0, 'Year')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Transforming prediction back to original scale**

```python
def box_cox_inverse(x, lam):
    if lam > 0:
        return (x * lam + 1) ** (1 / lam)
    elif lam == 0:
        return np.exp(x)
    else:
        print('Invalid lambda')
```

```python
prediction_tons = box_cox_inverse(prediction, lam)
prediction_tons
```

_result:_
```
array([52216.590779  , 46953.24555762, 42186.9382547 , 37873.9405973 ,
       33974.08501916, 30450.49838173, 27269.35381267, 24399.63955304,
       21812.94376475, 19483.25430688, 17386.77254423, 15501.7403034 ,
       13808.27914118, 12288.24113698, 10925.07046593,  9703.67505167,
        8610.30763844,  7632.45566018,  6758.73932123,  5978.8173373 ,
        5283.29981864,  4663.66780818,  4112.19901692,  3621.89932696,
        3186.43965874,  2800.09782425])
```

```python
sns.scatterplot('year', 'nox', data=df)
plt.plot(years, prediction_tons, color='k')
plt.ylabel('NOx emissions (tons)')
plt.xlabel('Year')
```

_result:_
```
Text(0.5, 0, 'Year')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Check for homoskedasticity**

```python
resids = lm_nox_year_fit.resid
sns.scatterplot(df['year'], resids)
```

_result:_
```
<AxesSubplot:xlabel='year'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Account for state differences**

```python
sns.scatterplot('year', 'nox_bc', data=df, hue = 'state')
```

_result:_
```
<AxesSubplot:xlabel='year', ylabel='nox_bc'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

Now we want to add an additional regressor, so that our regression reads:

$$NOx_i = \beta_0 + \beta_1 YEAR_{i}  + \beta_2 IS\_SC_i + \varepsilon_i$$

where $\beta_0$ is the intercept, $\beta_1$ is the slope with respect to year, and $\beta_2$ is a constant shift if the observation comes from SC.

```python
lm_nox_year_state = sm.ols('nox_bc ~ year + state', data=df)
lm_nox_year_state_fit = lm_nox_year_state.fit()
print(lm_nox_year_state_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 nox_bc   R-squared:                       0.920
Model:                            OLS   Adj. R-squared:                  0.919
Method:                 Least Squares   F-statistic:                     1073.
Date:                Mon, 25 Jan 2021   Prob (F-statistic):          3.36e-103
Time:                        17:41:21   Log-Likelihood:                -139.91
No. Observations:                 190   AIC:                             285.8
Df Residuals:                     187   BIC:                             295.6
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept     467.7094     10.824     43.212      0.000     446.357     489.062
state[T.SC]    -1.4557      0.074    -19.698      0.000      -1.602      -1.310
year           -0.2259      0.005    -41.923      0.000      -0.237      -0.215
==============================================================================
Omnibus:                       26.245   Durbin-Watson:                   1.208
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               63.314
Skew:                          -0.589   Prob(JB):                     1.78e-14
Kurtosis:                       5.571   Cond. No.                     5.88e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.88e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
def predict_nox_year_state(params, years, SC_binary):
    return params[0] + params[1] * SC_binary + params[2] * years
```

```python
years = np.arange(1995, 2021)
SC_isSC = np.ones(len(years))
NC_isSC = np.zeros(len(years))
prediction_SC = predict_nox_year_state(lm_nox_year_state_fit.params, years, SC_isSC)
prediction_NC = predict_nox_year_state(lm_nox_year_state_fit.params, years, NC_isSC)
```

```python
sns.scatterplot('year', 'nox_bc', data=df, hue='state')
plt.plot(years, prediction_SC, color='orange')
plt.plot(years, prediction_NC, color='blue')
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f2cd6f77a58>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
prediction_tons_SC = box_cox_inverse(prediction_SC, lam)
prediction_tons_NC = box_cox_inverse(prediction_NC, lam)
sns.scatterplot('year', 'nox', data=df, hue='state')
plt.plot(years, prediction_tons_SC, color='orange')
plt.plot(years, prediction_tons_NC, color='blue')
plt.ylabel('NOx emissions (tons)')
plt.xlabel('Year')
```

_result:_
```
Text(0.5, 0, 'Year')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Interaction effects**

```python
lm_nox_year_state_int = sm.ols('nox_bc ~ year*state', data=df)
lm_nox_year_state_int_fit = lm_nox_year_state_int.fit()
print(lm_nox_year_state_int_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 nox_bc   R-squared:                       0.920
Model:                            OLS   Adj. R-squared:                  0.919
Method:                 Least Squares   F-statistic:                     715.8
Date:                Mon, 25 Jan 2021   Prob (F-statistic):          7.27e-102
Time:                        17:41:22   Log-Likelihood:                -139.36
No. Observations:                 190   AIC:                             286.7
Df Residuals:                     186   BIC:                             299.7
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept          456.4890     15.304     29.828      0.000     426.298     486.680
state[T.SC]         20.9851     21.643      0.970      0.334     -21.712      63.682
year                -0.2203      0.008    -28.917      0.000      -0.235      -0.205
year:state[T.SC]    -0.0112      0.011     -1.037      0.301      -0.032       0.010
==============================================================================
Omnibus:                       30.977   Durbin-Watson:                   1.227
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               80.473
Skew:                          -0.677   Prob(JB):                     3.35e-18
Kurtosis:                       5.887   Cond. No.                     1.54e+06
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.54e+06. This might indicate that there are
strong multicollinearity or other numerical problems.
```

**Interaction is not significant in this case, but let's visualize model anyway**

```python
def predict_nox_year_state_int(params, years, SC_binary):
    return params[0] + params[1] * SC_binary + params[2] * years + params[3] * SC_binary * years
```

```python
prediction_SC = predict_nox_year_state_int(lm_nox_year_state_int_fit.params, years, SC_isSC)
prediction_NC = predict_nox_year_state_int(lm_nox_year_state_int_fit.params, years, NC_isSC)
```

```python
sns.scatterplot('year', 'nox_bc', data=df, hue='state')
plt.plot(years, prediction_SC, color='orange')
plt.plot(years, prediction_NC, color='blue')
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f2cd6e78c18>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Check for quarterly effects?**

```python
df.head()
```

_result:_
```
state  year  quarter program       so2        nox          co2    heatinput  \
0    NC  2017        1     ARP  3088.057   6627.984  11778066.24  143902340.0   
1    NC  2017        2     ARP  3771.224   7770.051  12594579.74  149515188.3   
2    NC  2017        3     ARP  6054.505  10265.869  17074422.27  200275610.8   
3    NC  2017        4     ARP  3307.317   7532.182  11408654.15  142107926.7   
4    NC  2018        1     ARP  3930.952   8266.694  13621514.75  164982269.3   

    nox_log     nox_bc  
0  8.799056  12.150325  
1  8.958032  12.445746  
2  9.236580  12.971333  
3  8.926940  12.387710  
4  9.019990  12.561771
```

```python
sns.scatterplot('year', 'nox_bc', data=df, hue='quarter')
```

_result:_
```
<AxesSubplot:xlabel='year', ylabel='nox_bc'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
lm_nox_year_state_q = sm.ols('nox_bc ~ year + state + quarter', data=df)
lm_nox_year_state_q_fit = lm_nox_year_state_q.fit()
print(lm_nox_year_state_q_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 nox_bc   R-squared:                       0.920
Model:                            OLS   Adj. R-squared:                  0.919
Method:                 Least Squares   F-statistic:                     716.8
Date:                Mon, 25 Jan 2021   Prob (F-statistic):          6.50e-102
Time:                        17:41:22   Log-Likelihood:                -139.25
No. Observations:                 190   AIC:                             286.5
Df Residuals:                     186   BIC:                             299.5
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept     468.1001     10.820     43.261      0.000     446.754     489.446
state[T.SC]    -1.4557      0.074    -19.713      0.000      -1.601      -1.310
year           -0.2261      0.005    -41.972      0.000      -0.237      -0.215
quarter        -0.0378      0.033     -1.141      0.255      -0.103       0.028
==============================================================================
Omnibus:                       24.609   Durbin-Watson:                   1.170
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               58.340
Skew:                          -0.554   Prob(JB):                     2.15e-13
Kurtosis:                       5.478   Cond. No.                     5.89e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.89e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

**Probably don't want quarter as an integer (implies linear relationship between seasons). Let's redo as categorical.**

```python
df['quarter_cat'] = [str(q) for q in df['quarter']]
type(df['quarter_cat'][0])
```

_result:_
```
str
```

```python
lm_nox_year_state_q = sm.ols('nox_bc ~ year + state + quarter_cat', data=df)
lm_nox_year_state_q_fit = lm_nox_year_state_q.fit()
print(lm_nox_year_state_q_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 nox_bc   R-squared:                       0.923
Model:                            OLS   Adj. R-squared:                  0.921
Method:                 Least Squares   F-statistic:                     439.1
Date:                Mon, 25 Jan 2021   Prob (F-statistic):          3.18e-100
Time:                        17:41:22   Log-Likelihood:                -136.47
No. Observations:                 190   AIC:                             284.9
Df Residuals:                     184   BIC:                             304.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept          468.3186     10.722     43.679      0.000     447.165     489.472
state[T.SC]         -1.4557      0.073    -19.896      0.000      -1.600      -1.311
quarter_cat[T.2]    -0.1836      0.103     -1.784      0.076      -0.387       0.019
quarter_cat[T.3]     0.0063      0.103      0.061      0.951      -0.197       0.209
quarter_cat[T.4]    -0.1913      0.104     -1.838      0.068      -0.397       0.014
year                -0.2262      0.005    -42.372      0.000      -0.237      -0.216
==============================================================================
Omnibus:                       35.056   Durbin-Watson:                   1.091
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               98.919
Skew:                          -0.742   Prob(JB):                     3.31e-22
Kurtosis:                       6.208   Cond. No.                     5.89e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.89e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

**ANOVA test for difference in mean between NC vs SC**

```python
## For ANOVA test we need to separate samples
df_nc = df.loc[df['state'] == 'NC', :]
df_sc = df.loc[df['state'] == 'SC', :]
plt.figure()
sns.scatterplot(df_nc['year'], df_nc['nox_bc'])
sns.scatterplot(df_sc['year'], df_sc['nox_bc'])
plt.figure()
sns.boxplot('state', 'nox_bc', data=df)
```

_result:_
```
<AxesSubplot:xlabel='state', ylabel='nox_bc'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
## ANOVA test
from scipy.stats import f_oneway

f_oneway(df_nc['nox_bc'], df_sc['nox_bc'])
```

_result:_
```
F_onewayResult(statistic=37.51228177961962, pvalue=5.197934502526843e-09)
```

**Test for difference in mean between quarters in NC**

```python
plt.figure()
sns.scatterplot('year', 'nox_bc', data=df_nc, hue='quarter')
plt.figure()
sns.boxplot('quarter', 'nox_bc', data=df_nc)
```

_result:_
```
<AxesSubplot:xlabel='quarter', ylabel='nox_bc'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
df_nc_q1 = df_nc.loc[df_nc['quarter'] == 1, :]
df_nc_q2 = df_nc.loc[df_nc['quarter'] == 2, :]
df_nc_q3 = df_nc.loc[df_nc['quarter'] == 3, :]
df_nc_q4 = df_nc.loc[df_nc['quarter'] == 4, :]

f_oneway(df_nc_q1['nox_bc'], df_nc_q2['nox_bc'], df_nc_q3['nox_bc'], df_nc_q4['nox_bc'])
```

_result:_
```
F_onewayResult(statistic=0.09676903132215894, pvalue=0.9616321455374468)
```

### In-class exercise
Run a regression to test whether there has been a statistically significant reduction in reported CO2 emissions in North Carolina (note: this only comes from a subset of coal plants, not a full picture of CO2 emissions). Perform any statistical checks & transformations if necessary.

### Data smoothing 

```python
sns.scatterplot('year','so2', data=df_nc)
```

_result:_
```
<AxesSubplot:xlabel='year', ylabel='so2'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Simple smoothing - line segments through means of each year**

```python
df_nc_yearly = df_nc.groupby('year').mean()
df_nc_yearly
```

_result:_
```
quarter            so2          nox           co2     heatinput  \
year                                                                    
1997      2.5  127989.569250  70669.34550  1.891000e+07  1.846805e+08   
1998      2.5  122145.952750  62181.96625  1.840558e+07  1.803841e+08   
1999      2.5  114485.645250  50356.93975  1.824346e+07  1.787225e+08   
2000      2.5  113360.592750  40214.40225  1.851418e+07  1.817438e+08   
2001      2.5  112621.635000  36084.66050  1.770498e+07  1.739513e+08   
2002      2.5  115748.281250  36426.42525  1.821641e+07  1.807777e+08   
2003      2.5  115510.188250  33165.90575  1.796947e+07  1.772706e+08   
2004      2.5  118080.042000  29430.57625  1.822001e+07  1.798254e+08   
2005      2.5  125233.896750  26937.31225  1.889529e+07  1.871322e+08   
2006      2.5  115535.805250  25763.45125  1.849483e+07  1.832767e+08   
2007      2.5   92706.619500  14854.43550  1.942336e+07  1.936955e+08   
2008      2.5   56757.513500  13663.03800  1.899975e+07  1.891311e+08   
2009      2.5   27737.030750   9695.69150  1.660579e+07  1.662373e+08   
2010      2.5   29156.794500  12402.79050  1.857341e+07  1.888504e+08   
2011      2.5   18376.713750  10335.92050  1.591590e+07  1.644430e+08   
2012      2.5   13385.650000  11003.66425  1.498127e+07  1.621570e+08   
2013      2.5   10564.165250  10449.11650  1.445974e+07  1.628024e+08   
2014      2.5    9126.791000   9599.49275  1.525883e+07  1.714681e+08   
2015      2.5    6872.400250   8871.41975  1.430315e+07  1.688474e+08   
2016      2.5    5790.259250   8012.82800  1.414550e+07  1.696785e+08   
2017      2.5    4055.275750   8049.02150  1.321393e+07  1.589503e+08   
2018      2.5    3945.472750   8251.59225  1.340741e+07  1.661804e+08   
2019      2.5    4108.766500   7324.56725  1.274872e+07  1.567650e+08   
2020      2.0    1188.000333   3027.47500  6.364370e+06  8.615907e+07   

        nox_log     nox_bc  
year                        
1997  11.163785  16.901895  
1998  11.028650  16.609806  
1999  10.823826  16.169793  
2000  10.599301  15.695576  
2001  10.490887  15.469261  
2002  10.500311  15.488872  
2003  10.399083  15.280033  
2004  10.242635  14.964076  
2005  10.152503  14.780413  
2006  10.107995  14.690208  
2007   9.604678  13.681939  
2008   9.521321  13.519425  
2009   9.175735  12.856142  
2010   9.419980  13.323796  
2011   9.221948  12.946537  
2012   9.289517  13.074610  
2013   9.248840  12.995421  
2014   9.147264  12.804471  
2015   9.068997  12.656915  
2016   8.964904  12.461561  
2017   8.980152  12.488778  
2018   9.010064  12.544199  
2019   8.865978  12.278350  
2020   7.824974  10.438184
```

```python
sns.scatterplot('year','so2', data=df_nc)
plt.plot(df_nc_yearly.index, df_nc_yearly['so2'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f2cd6cbaf28>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

**Lowess smoothing**

```python
from statsmodels.nonparametric.smoothers_lowess import lowess

## fraction of data to use for each smoothed value (b/w 0 and 1, default is 0.67)
lowess_frac = 0.2

## get smoothed points
smooth = lowess(df_nc['so2'], df_nc['year'], frac=lowess_frac)
index_smooth, so2_smooth = np.transpose(smooth)
```

```python
sns.scatterplot('year','so2', data=df_nc)
plt.plot(index_smooth, so2_smooth)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f2cd6ef4160>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

### Notes: Visualization (notebook)
*URL:* https://github.com/PurdueCyberTraining/python4env/blob/main/Lec6-1-Visualization/Lec6_Visualization.ipynb

# Lecture 6: Visualization
ENVR 890-001: Python for Environmental Research, Fall 2020

September 25, 2020

By Andrew Hamilton. 

### Summary
No matter what type of research you do (lab experiments, public surveys, computer modeling, etc.), data visualization is a crucial skill. Programming languages like Python give us a high degree of flexibility and allow us to tailor our visualization to the data at hand. Today we will learn the basics of how to set up figures, and then go through many examples of different types of plots and customizations.

### The Basics
The main plotting package for Python is ``matplotlib``, and its ``pyplot`` module, which is typically imported with the alias ``plt``. Another helpful library which we will use later in the lecture is ``seaborn``, typically imported as ``sns``

```python
import numpy as np
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns
```

```python
## adjust default plot font size
matplotlib.rcParams.update({'font.size': 18})
```

The most important arguments to any plotting function are the data. For our first example, let's plot two simple parabolas.

```python
def parabola(a, b, c, x):
    return a + b * x + c * x **2

X = np.arange(-10, 10)
X
```

_result:_
```
array([-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2,
         3,   4,   5,   6,   7,   8,   9])
```

```python
Y1 = [parabola(-2, 0, 1, x) for x in X]
Y2 = [parabola(5, -2, -0.5, x) for x in X]
Y2
```

_result:_
```
[-25.0,
 -17.5,
 -11.0,
 -5.5,
 -1.0,
 2.5,
 5.0,
 6.5,
 7.0,
 6.5,
 5.0,
 2.5,
 -1.0,
 -5.5,
 -11.0,
 -17.5,
 -25.0,
 -33.5,
 -43.0,
 -53.5]
```

Now let's plot these two y variables over the domain of x.

```python
### plot Y1
plt.plot(X, Y1)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65e2f5d9e8>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### plot Y1 & Y2 together, and fix figure size
fig = plt.figure(figsize = (10, 6))
plt.plot(X, Y1)
plt.plot(X, Y2)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65dae9c048>]
```

_result:_
```
<Figure size 720x432 with 1 Axes>
```

```python
### plot Y1 & Y2 separately from 1 cell
fig = plt.figure(figsize = (10, 6))
plt.plot(X, Y1)
fig = plt.figure(figsize = (10, 6))
plt.plot(X, Y2)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65dad8e668>]
```

_result:_
```
<Figure size 720x432 with 1 Axes>
```

_result:_
```
<Figure size 720x432 with 1 Axes>
```

Now let's add some custom x and y labels, as well as a legend.

```python
fig = plt.figure(figsize = (10, 6))
plt.plot(X, Y1, label='First parabola')
plt.plot(X, Y2, label='Second parabola')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7f65dadaafd0>
```

_result:_
```
<Figure size 720x432 with 1 Axes>
```

We can also customize the line's color, style, thickness, transparency, etc., and change the legend location. Many more [colors here](https://matplotlib.org/3.3.0/gallery/color/named_colors.html), and other options for [plot here](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html).

```python
fig = plt.figure(figsize = (10, 6))
plt.plot(X, Y1, label='First parabola', color='mediumturquoise', linestyle='--', linewidth=4, alpha=0.9)
plt.plot(X, Y2, label='Second parabola', color='mediumslateblue', marker='d', alpha=0.4)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='upper center')
```

_result:_
```
<matplotlib.legend.Legend at 0x7f65dacc6eb8>
```

_result:_
```
<Figure size 720x432 with 1 Axes>
```

### In-class exercise
Let's create some fake data to represent annual snowfall in two locations, one colder and one warmer.
1. Create an x variable that includes the integers from 1920 to 2020.
1. Create one y variable that is random draws from an [exponential distribution](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html) with a scale parameter of 10, with the same length as x. (this is the colder climate)
1. Create a second y variable that is random draws from a [lognormal distribution](https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html) with a mean of 0.5 and a standard deviation of 1, with the same length as x. (this is the warmer climate)
1. Plot both time series. Label the x axis "Year" and the y axis "Annual snowfall (inches)". Create a legend where the first series is labeled "Colder" and the second is labeled "Warmer". Color them using colder and warmer-looking colors of your choice.

### Importing and cleaning real data
Let's read in some Chapel Hill weather data (from NOAA National Climate Data Center, https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USC00311677/detail)

```python
### read in data. ignore first row ("header") where I have written info about where data was downloaded.
df = pd.read_csv('chapel_hill_weather.csv', header = 1)
df
```

_result:_
```
STATION                    NAME       DATE  PRCP  SNOW  TMAX  TMIN
0      USC00311677  CHAPEL HILL 2 W, NC US   1/1/1920  0.00   0.0  67.0  46.0
1      USC00311677  CHAPEL HILL 2 W, NC US   1/2/1920  0.00   0.0  60.0  22.0
2      USC00311677  CHAPEL HILL 2 W, NC US   1/3/1920  0.00   0.0  30.0  12.0
3      USC00311677  CHAPEL HILL 2 W, NC US   1/4/1920  0.00   0.0  36.0  18.0
4      USC00311677  CHAPEL HILL 2 W, NC US   1/5/1920  0.00   0.0  34.0   9.0
...            ...                     ...        ...   ...   ...   ...   ...
36318  USC00311677  CHAPEL HILL 2 W, NC US  7/30/2020  2.00   0.0  90.0  69.0
36319  USC00311677  CHAPEL HILL 2 W, NC US  7/31/2020  0.03   0.0  88.0  70.0
36320  USC00311677  CHAPEL HILL 2 W, NC US   8/1/2020  0.00   NaN  93.0  74.0
36321  USC00311677  CHAPEL HILL 2 W, NC US   8/2/2020  0.00   NaN  93.0  74.0
36322  USC00311677  CHAPEL HILL 2 W, NC US   8/4/2020  2.41   0.0  80.0  66.0

[36323 rows x 7 columns]
```

```python
### Organize data
## rename columns
df.columns = ['station', 'name', 'date', 'precip', 'snow', 'tmax', 'tmin']
df
```

_result:_
```
station                    name       date  precip  snow  tmax  \
0      USC00311677  CHAPEL HILL 2 W, NC US   1/1/1920    0.00   0.0  67.0   
1      USC00311677  CHAPEL HILL 2 W, NC US   1/2/1920    0.00   0.0  60.0   
2      USC00311677  CHAPEL HILL 2 W, NC US   1/3/1920    0.00   0.0  30.0   
3      USC00311677  CHAPEL HILL 2 W, NC US   1/4/1920    0.00   0.0  36.0   
4      USC00311677  CHAPEL HILL 2 W, NC US   1/5/1920    0.00   0.0  34.0   
...            ...                     ...        ...     ...   ...   ...   
36318  USC00311677  CHAPEL HILL 2 W, NC US  7/30/2020    2.00   0.0  90.0   
36319  USC00311677  CHAPEL HILL 2 W, NC US  7/31/2020    0.03   0.0  88.0   
36320  USC00311677  CHAPEL HILL 2 W, NC US   8/1/2020    0.00   NaN  93.0   
36321  USC00311677  CHAPEL HILL 2 W, NC US   8/2/2020    0.00   NaN  93.0   
36322  USC00311677  CHAPEL HILL 2 W, NC US   8/4/2020    2.41   0.0  80.0   

       tmin  
0      46.0  
1      22.0  
2      12.0  
3      18.0  
4       9.0  
...     ...  
36318  69.0  
36319  70.0  
36320  74.0  
36321  74.0  
36322  66.0  

[36323 rows x 7 columns]
```

```python
## convert date column to datetime type
df.date = pd.to_datetime(df['date'])
df
```

_result:_
```
station                    name       date  precip  snow  tmax  \
0      USC00311677  CHAPEL HILL 2 W, NC US 1920-01-01    0.00   0.0  67.0   
1      USC00311677  CHAPEL HILL 2 W, NC US 1920-01-02    0.00   0.0  60.0   
2      USC00311677  CHAPEL HILL 2 W, NC US 1920-01-03    0.00   0.0  30.0   
3      USC00311677  CHAPEL HILL 2 W, NC US 1920-01-04    0.00   0.0  36.0   
4      USC00311677  CHAPEL HILL 2 W, NC US 1920-01-05    0.00   0.0  34.0   
...            ...                     ...        ...     ...   ...   ...   
36318  USC00311677  CHAPEL HILL 2 W, NC US 2020-07-30    2.00   0.0  90.0   
36319  USC00311677  CHAPEL HILL 2 W, NC US 2020-07-31    0.03   0.0  88.0   
36320  USC00311677  CHAPEL HILL 2 W, NC US 2020-08-01    0.00   NaN  93.0   
36321  USC00311677  CHAPEL HILL 2 W, NC US 2020-08-02    0.00   NaN  93.0   
36322  USC00311677  CHAPEL HILL 2 W, NC US 2020-08-04    2.41   0.0  80.0   

       tmin  
0      46.0  
1      22.0  
2      12.0  
3      18.0  
4       9.0  
...     ...  
36318  69.0  
36319  70.0  
36320  74.0  
36321  74.0  
36322  66.0  

[36323 rows x 7 columns]
```

```python
# index by date
df.index = df['date']
# remove unnecessary columns
df = df.loc[:, ['precip', 'snow', 'tmax', 'tmin']]
df
```

_result:_
```
precip  snow  tmax  tmin
date                                
1920-01-01    0.00   0.0  67.0  46.0
1920-01-02    0.00   0.0  60.0  22.0
1920-01-03    0.00   0.0  30.0  12.0
1920-01-04    0.00   0.0  36.0  18.0
1920-01-05    0.00   0.0  34.0   9.0
...            ...   ...   ...   ...
2020-07-30    2.00   0.0  90.0  69.0
2020-07-31    0.03   0.0  88.0  70.0
2020-08-01    0.00   NaN  93.0  74.0
2020-08-02    0.00   NaN  93.0  74.0
2020-08-04    2.41   0.0  80.0  66.0

[36323 rows x 4 columns]
```

```python
## Get year, month, day for each
df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
df
```

_result:_
```
precip  snow  tmax  tmin  year  month  day
date                                                  
1920-01-01    0.00   0.0  67.0  46.0  1920      1    1
1920-01-02    0.00   0.0  60.0  22.0  1920      1    2
1920-01-03    0.00   0.0  30.0  12.0  1920      1    3
1920-01-04    0.00   0.0  36.0  18.0  1920      1    4
1920-01-05    0.00   0.0  34.0   9.0  1920      1    5
...            ...   ...   ...   ...   ...    ...  ...
2020-07-30    2.00   0.0  90.0  69.0  2020      7   30
2020-07-31    0.03   0.0  88.0  70.0  2020      7   31
2020-08-01    0.00   NaN  93.0  74.0  2020      8    1
2020-08-02    0.00   NaN  93.0  74.0  2020      8    2
2020-08-04    2.41   0.0  80.0  66.0  2020      8    4

[36323 rows x 7 columns]
```

```python
## Only keep data since 1970
df = df.loc[df['year'] >= 1970, :]
df
```

_result:_
```
precip  snow  tmax  tmin  year  month  day
date                                                  
1970-01-01    0.10   NaN  61.0  35.0  1970      1    1
1970-01-02    0.09   NaN  38.0  23.0  1970      1    2
1970-01-03    0.00   NaN  37.0  25.0  1970      1    3
1970-01-04    0.00   NaN  49.0  23.0  1970      1    4
1970-01-05    0.00   NaN  41.0  17.0  1970      1    5
...            ...   ...   ...   ...   ...    ...  ...
2020-07-30    2.00   0.0  90.0  69.0  2020      7   30
2020-07-31    0.03   0.0  88.0  70.0  2020      7   31
2020-08-01    0.00   NaN  93.0  74.0  2020      8    1
2020-08-02    0.00   NaN  93.0  74.0  2020      8    2
2020-08-04    2.41   0.0  80.0  66.0  2020      8    4

[18136 rows x 7 columns]
```

```python
### Clean data
# remove NANs by assuming previous value (note, this is not the most sophisticated way to fill data)
nrows = df.shape[0]
ncols = df.shape[1]
np.isnan(df)
```

_result:_
```
precip   snow   tmax   tmin   year  month    day
date                                                        
1970-01-01   False   True  False  False  False  False  False
1970-01-02   False   True  False  False  False  False  False
1970-01-03   False   True  False  False  False  False  False
1970-01-04   False   True  False  False  False  False  False
1970-01-05   False   True  False  False  False  False  False
...            ...    ...    ...    ...    ...    ...    ...
2020-07-30   False  False  False  False  False  False  False
2020-07-31   False  False  False  False  False  False  False
2020-08-01   False   True  False  False  False  False  False
2020-08-02   False   True  False  False  False  False  False
2020-08-04   False  False  False  False  False  False  False

[18136 rows x 7 columns]
```

```python
print("Fraction of nan's before:")
print(np.isnan(df).sum(axis=0) / nrows)
print()
```

_output:_
```
Fraction of nan's before:
precip    0.003088
snow      0.124173
tmax      0.005293
tmin      0.008602
year      0.000000
month     0.000000
day       0.000000
dtype: float64
```

```python
### replace nan's with previous value in time
for i in range(nrows):
    for j in range(ncols):
        if np.isnan(df.iloc[i, j]):
            df.iloc[i, j] = df.iloc[i - 1, j]
            
print("Fraction of nan's after:")
print(np.isnan(df).sum(axis=0) / nrows)
```

_output:_
```
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:1763: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  isetter(loc, value)
```

_output:_
```
Fraction of nan's after:
precip    0.0
snow      0.0
tmax      0.0
tmin      0.0
year      0.0
month     0.0
day       0.0
dtype: float64
```

```python
### Plot data as time series
plt.plot(df.precip)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65e374fdd8>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
plt.plot(df.snow)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65dab74780>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
plt.plot(df.tmax)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65dab51f98>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
plt.plot(df.tmin)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65dad27780>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
## Looks like a bad data value - tmin probably wasn't >120 in January
df.loc[df.tmin > 100, :]
```

_result:_
```
precip  snow  tmax   tmin  year  month  day
date                                                   
1988-01-27     0.0   0.0  31.0  123.0  1988      1   27
```

```python
## Let's look at that data in context of neighbors
i = np.argmax(df.tmin)
print(i)
df.iloc[(i - 2):(i + 3), :]
```

_output:_
```
6474
```

_result:_
```
precip  snow  tmax   tmin  year  month  day
date                                                   
1988-01-25    0.05   0.0  56.0   24.0  1988      1   25
1988-01-26    0.42   0.0  43.0   23.0  1988      1   26
1988-01-27    0.00   0.0  31.0  123.0  1988      1   27
1988-01-28    0.00   0.0  36.0   13.0  1988      1   28
1988-01-29    0.00   0.0  45.0   14.0  1988      1   29
```

```python
## Let's reset that value based on previous value (note: you could also do average, or leave blank)
df.iloc[i, 3] = df.iloc[i - 1, 3]
df.iloc[(i - 2):(i + 3), :]
### Note: this particular warning about "setting a value based on a copy of a slice" occurs a lot, personally I ignore it
```

_output:_
```
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:1763: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  isetter(loc, value)
```

_result:_
```
precip  snow  tmax  tmin  year  month  day
date                                                  
1988-01-25    0.05   0.0  56.0  24.0  1988      1   25
1988-01-26    0.42   0.0  43.0  23.0  1988      1   26
1988-01-27    0.00   0.0  31.0  23.0  1988      1   27
1988-01-28    0.00   0.0  36.0  13.0  1988      1   28
1988-01-29    0.00   0.0  45.0  14.0  1988      1   29
```

```python
plt.plot(df.tmin)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65da7aada0>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

### Many ways to visualize

```python
## Function for plotting time series over period
def plot_weather(df, colname, ylabel, startyear=df.year.min(), endyear=df.year.max()):
    data = df.loc[(df['year'] >= startyear) & (df['year'] <= endyear), colname]
    fig = plt.figure(figsize = (12,8))
    plt.plot(data)
    plt.xlabel('Year')
    plt.ylabel(ylabel)
```

```python
plot_weather(df, 'precip', 'Precip (mm)')
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
plot_weather(df, 'precip', 'Precip (mm)', 1998, 2002)
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
plot_weather(df, 'snow', 'Snow (mm)', 1998, 2002)
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
## Function for plotting multiple time series over period
def plot_weather_multi(df, colnames, ylabel, startyear=df.year.min(), endyear=df.year.max()):
    data = df.loc[(df['year'] >= startyear) & (df['year'] <= endyear)]
    fig = plt.figure(figsize = (12,8))
    for colname in colnames:
        plt.plot(data[colname], label=colname)
    plt.xlabel('Year')
    plt.ylabel(ylabel)
    plt.legend()
```

```python
plot_weather_multi(df, ['tmin', 'tmax'], 'Temperature (F)', 1998, 2002)
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
## How do min and max temperatures compare? Scatterplot.
fig = plt.figure(figsize = (12,8))
plt.scatter(df['tmin'], df['tmax'])
plt.xlabel('tmin')
plt.ylabel('tmax')
```

_result:_
```
Text(0, 0.5, 'tmax')
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
## customizing with color and transparency
fig = plt.figure(figsize = (12,8))
plt.scatter(df['tmin'], df['tmax'], color='k', alpha=0.1)
plt.xlabel('tmin')
plt.ylabel('tmax')
```

_result:_
```
Text(0, 0.5, 'tmax')
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
## what about scattering by month?
markers = ['o', '<', '^', '>', '<', 's', 'p', 'P', '*', 'h', 'X', 'D']
colors = ['navy', 'mediumslateblue', 'turquoise', 'springgreen', 'forestgreen', 'greenyellow', 'yellow', 'gold', 'orange', 'orangered', 'firebrick', 'mediumvioletred']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig = plt.figure(figsize = (12,8))
for i in range(12):
    data = df.loc[df['month'] == (i+1), :]
    plt.scatter(data['tmin'], data['tmax'], color=colors[i], marker=markers[i], alpha=0.3, label=months[i])
plt.xlabel('tmin')
plt.ylabel('tmax')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7f65d9ed6320>
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
## histogram of tmin vs tmax
fig = plt.figure(figsize = (12,8))
plt.hist(df['tmin'], color='b', alpha=0.5, label='tmin')
plt.hist(df['tmax'], color='r', alpha=0.5, label='tmax')
plt.xlabel('Temperature (F)')
plt.ylabel('Count')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7f65d9e13cc0>
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
## histogram of tmax by season. Use "density" to make sure all have equal area.
seasons = ['winter', 'spring', 'summer', 'fall']
season_months =  {'winter': [0, 1, 11],
           'spring': [2, 3, 4],
           'summer': [5, 6, 7],
           'fall': [8, 9, 10]}
colors = {'winter': 'navy', 
          'spring': 'springgreen',
          'summer': 'gold',
          'fall': 'firebrick'}

fig = plt.figure(figsize = (12,8))
for k in seasons:
    is_season = [m in season_months[k] for m in df['month']]
    data = df.loc[is_season, :]
    plt.hist(data['tmax'], color=colors[k], density=True, alpha=0.4, label=k)
plt.xlabel('Max temperature (F)')
plt.ylabel('Density')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7f65da790748>
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
##### seaborn is another plotting package with some nice clean functions. plays nice with matplotlib parameters.
## kde plot
fig = plt.figure(figsize = (12,8))
for k in seasons:
    is_season = [m in season_months[k] for m in df['month']]
    data = df.loc[is_season, :]
    sns.kdeplot(data['tmax'], color=colors[k], shade=True, label=k)
plt.xlabel('Max temperature (F)')
plt.ylabel('Density')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7f65da212390>
```

_result:_
```
<Figure size 864x576 with 1 Axes>
```

```python
## boxplots
sns.boxplot(x = df['month'], y = df['tmax'])
plt.legend
```

_result:_
```
<function matplotlib.pyplot.legend(*args, **kwargs)>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
## violin plots
## alternatively with seaborn, can just write colnames. We can also specify tick labels.
sns.violinplot(x = 'month', y = 'tmax', data = df, color = 'lightgrey')
plt.xlabel('Month')
plt.ylabel('Max temperature (F)')
```

_result:_
```
Text(0, 0.5, 'Max temperature (F)')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
## Grouping data using the "groupby" function
df_monthly_mean = df.groupby('month').mean()
df_monthly_mean
```

_result:_
```
precip      snow       tmax       tmin         year        day
month                                                                  
1      0.123146  0.068539  49.871091  27.924059  1994.804084  15.987237
2      0.123305  0.062246  53.745263  30.096842  1994.759298  14.602807
3      0.143085  0.022141  61.744681  37.311170  1995.553191  15.997340
4      0.114395  0.000395  71.622368  45.698026  1994.853289  15.508553
5      0.136257  0.000000  78.370443  54.657552  1995.227214  16.026042
6      0.142921  0.000000  85.472848  62.853642  1994.707947  15.507947
7      0.139035  0.000000  89.059425  66.854313  1994.824920  15.980831
8      0.150769  0.000000  87.603048  65.821074  1994.677270  15.968191
9      0.151400  0.000000  81.950202  59.720054  1994.292059  15.485868
10     0.120378  0.000000  71.802477  46.817471  1994.271186  15.973924
11     0.116961  0.002510  62.453189  37.381954  1994.107870  15.466079
12     0.117397  0.018327  53.655378  31.319389  1994.256972  16.003984
```

```python
## plot by month with different line styles. Also replace x label ticks.
plt.plot(df_monthly_mean['tmax'], ls = ':', label='tmax')
plt.plot(df_monthly_mean['tmin'], ls = '--', label='tmin')
plt.legend()
ticks = plt.xticks(list(range(1, 13)), months, rotation=90)
plt.xlabel('Month')
plt.ylabel('Temperature (F)')
```

_result:_
```
Text(0, 0.5, 'Temperature (F)')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
df_annual_sum = df.groupby('year').sum()
df_annual_sum
```

_result:_
```
precip  snow     tmax     tmin  month   day
year                                             
1970   44.05   0.5  25739.0  17330.0   2382  5738
1971   52.99   5.5  25424.0  17555.0   2382  5738
1972   52.48   2.5  25135.0  17296.0   2384  5767
1973   37.87  13.0  23830.0  16147.0   2289  5242
1974   36.89   0.0  23428.0  15357.0   2227  5242
1975   51.23   0.0  25942.0  16864.0   2382  5738
1976   33.61   0.0  25681.0  16062.0   2384  5767
1977   37.60   3.5  25715.0  16095.0   2382  5738
1978   54.49   7.5  25024.0  15316.0   2382  5738
1979   49.09  14.5  20679.0  13202.0   2041  4746
1980   47.77  25.1  25736.0  15988.0   2384  5767
1981   39.76   3.9  25473.0  15403.0   2382  5738
1982   56.40   0.5  25353.0  16235.0   2368  5693
1983   64.08   5.3  24877.0  15009.0   2382  5738
1984   50.40   5.0  25352.0  16353.0   2384  5767
1985   54.59   6.7  26283.0  16976.0   2382  5738
1986   33.30   1.3  26440.0  16727.0   2382  5738
1987   45.39  14.3  26034.0  16710.0   2382  5738
1988   36.23   6.8  25993.0  16174.0   2384  5767
1989   57.28  11.5  25656.0  16313.0   2382  5738
1990   44.84   0.0  27223.0  17564.0   2382  5738
1991   39.02   0.0  26486.0  18297.0   2382  5738
1992   49.79   0.0  25225.0  17795.0   2384  5767
1993   48.63   4.9  25591.0  17707.0   2382  5738
1994   41.60   1.5  25744.0  17683.0   2382  5738
1995   53.23   0.8  25417.0  17585.0   2382  5738
1996   56.97  12.4  25133.0  17406.0   2384  5767
1997   39.15   0.2  23927.0  16461.0   2010  5242
1998   50.93   0.5  26420.0  18148.0   2382  5738
1999   61.25   0.0  26151.0  17591.0   2382  5738
2000   42.47  20.7  25621.0  17199.0   2384  5767
2001   40.13   1.2  26064.0  17421.0   2382  5738
2002   46.57   0.0  26180.0  17903.0   2382  5738
2003   57.11   4.5  25246.0  17657.0   2382  5738
2004   42.33  15.2  25808.0  17888.0   2384  5767
2005   45.40   0.4  25955.0  17772.0   2382  5738
2006   50.86   0.0  26222.0  17738.0   2382  5738
2007   34.82   0.0  26779.0  18035.0   2382  5738
2008   55.39   0.0  25931.0  17611.0   2384  5767
2009   47.65   0.0  25331.0  17588.0   2382  5738
2010   38.15   0.0  25963.0  17760.0   2382  5738
2011   39.40   0.0  26285.0  17981.0   2382  5738
2012   43.26   0.0  26303.0  18249.0   2384  5767
2013   53.08   0.0  24528.0  17036.0   2328  5630
2014   43.48   0.1  24134.0  16468.0   2276  5487
2015   54.43  24.0  25052.0  17539.0   2289  5489
2016   47.71   0.0  23688.0  16513.0   2158  5176
2017   36.42   3.0  23544.0  16309.0   2080  5199
2018   68.96  44.5  22774.0  15975.0   2038  4887
2019   43.35   0.0  25179.0  17523.0   2300  5515
2020   34.92   0.0  14563.0  10352.0    834  3137
```

```python
## Regression plot (we will cover regression in more detail next week)
sns.regplot(df_annual_sum.index, df_annual_sum['precip'], ci=90)
```

_result:_
```
<AxesSubplot:xlabel='year', ylabel='precip'>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
## Stacking multiple plots
df_annual_max = df.groupby('year').max()
df_annual_min = df.groupby('year').min()
df_annual_selected = df_annual_max[['tmax']]
df_annual_selected['tmin'] = df_annual_min[['tmin']]
df_annual_selected.columns = ['tmax_max', 'tmin_min']
df_annual_selected
```

_output:_
```
/home/andrew/.local/lib/python3.6/site-packages/ipykernel_launcher.py:5: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  """
```

_result:_
```
tmax_max  tmin_min
year                    
1970      98.0       4.0
1971      97.0       7.0
1972      96.0       4.0
1973      93.0       9.0
1974      94.0      17.0
1975      96.0       9.0
1976      98.0       4.0
1977     105.0       1.0
1978      97.0       2.0
1979      92.0       5.0
1980      98.0       6.0
1981      98.0       4.0
1982      94.0       0.0
1983     104.0       0.0
1984      94.0       7.0
1985      99.0      -8.0
1986     101.0       5.0
1987     101.0      16.0
1988     106.0       8.0
1989      98.0       9.0
1990     101.0      17.0
1991      98.0      15.0
1992      96.0      19.0
1993      99.0      13.0
1994      95.0      -4.0
1995      98.0      11.0
1996      97.0       3.0
1997      98.0      13.0
1998      99.0      18.0
1999     102.0      12.0
2000      96.0       8.0
2001      96.0      15.0
2002     101.0      17.0
2003      95.0      11.0
2004      96.0      11.0
2005     102.0      13.0
2006      98.0      16.0
2007     104.0      15.0
2008      98.0      15.0
2009      98.0       8.0
2010     100.0      13.0
2011     102.0      15.0
2012     104.0      17.0
2013      94.0      17.0
2014      98.0       6.0
2015      98.0       5.0
2016      96.0      14.0
2017      98.0       8.0
2018      97.0       2.0
2019      99.0      15.0
2020      97.0      23.0
```

```python
fig, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, figsize = (12, 12))
ax11.plot(df_annual_sum.index, df_annual_sum['precip'])
ax12.plot(df_annual_max.index, df_annual_max['precip'])
ax21.plot(df_annual_sum.index, df_annual_sum['snow'])
ax22.plot(df_annual_max.index, df_annual_max['snow'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7f65d9b89f28>]
```

_result:_
```
<Figure size 864x864 with 4 Axes>
```

```python
## subplots with seaborn
fig, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, figsize = (12, 12))
sns.regplot(df_annual_sum.index, df_annual_sum['precip'], ax=ax11)
sns.regplot(df_annual_max.index, df_annual_max['precip'], ax=ax12)
sns.regplot(df_annual_sum.index, df_annual_sum['snow'], ax=ax21)
sns.regplot(df_annual_max.index, df_annual_max['snow'], ax=ax22)
```

_result:_
```
<AxesSubplot:xlabel='year', ylabel='snow'>
```

_result:_
```
<Figure size 864x864 with 4 Axes>
```

```python
## Adjusting spacing of plot
fig, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, figsize = (12, 12))
fig.subplots_adjust(hspace=0.15, wspace=0.25)


sns.regplot(df_annual_sum.index, df_annual_sum['precip'], ax=ax11)
ax11.set_ylabel('Total precip (mm)')
ax11.set_xlabel('')
sns.regplot(df_annual_max.index, df_annual_max['precip'], ax=ax12)
ax12.set_ylabel('Max precip (mm)')
ax12.set_xlabel('')
sns.regplot(df_annual_sum.index, df_annual_sum['snow'], ax=ax21)
ax21.set_ylabel('Total snow (mm)')
ax21.set_xlabel('')
sns.regplot(df_annual_max.index, df_annual_max['snow'], ax=ax22)
ax22.set_ylabel('Max snow (mm)')
ax22.set_xlabel('')
```

_result:_
```
Text(0.5, 0, '')
```

_result:_
```
<Figure size 864x864 with 4 Axes>
```

```python
## pairplot
df_annual_combined = df_annual_sum.loc[:, ['precip', 'snow']].copy()
columns = df_annual_combined.columns
columns = [c + '_sum' for c in columns]
df_annual_combined.columns = columns
df_annual_combined
```

_result:_
```
precip_sum  snow_sum
year                      
1970       44.05       0.5
1971       52.99       5.5
1972       52.48       2.5
1973       37.87      13.0
1974       36.89       0.0
1975       51.23       0.0
1976       33.61       0.0
1977       37.60       3.5
1978       54.49       7.5
1979       49.09      14.5
1980       47.77      25.1
1981       39.76       3.9
1982       56.40       0.5
1983       64.08       5.3
1984       50.40       5.0
1985       54.59       6.7
1986       33.30       1.3
1987       45.39      14.3
1988       36.23       6.8
1989       57.28      11.5
1990       44.84       0.0
1991       39.02       0.0
1992       49.79       0.0
1993       48.63       4.9
1994       41.60       1.5
1995       53.23       0.8
1996       56.97      12.4
1997       39.15       0.2
1998       50.93       0.5
1999       61.25       0.0
2000       42.47      20.7
2001       40.13       1.2
2002       46.57       0.0
2003       57.11       4.5
2004       42.33      15.2
2005       45.40       0.4
2006       50.86       0.0
2007       34.82       0.0
2008       55.39       0.0
2009       47.65       0.0
2010       38.15       0.0
2011       39.40       0.0
2012       43.26       0.0
2013       53.08       0.0
2014       43.48       0.1
2015       54.43      24.0
2016       47.71       0.0
2017       36.42       3.0
2018       68.96      44.5
2019       43.35       0.0
2020       34.92       0.0
```

```python
for c in ['precip', 'snow']:
    df_annual_combined[c + '_max'] = df_annual_max[c]    
df_annual_combined
```

_result:_
```
precip_sum  snow_sum  precip_max  snow_max
year                                            
1970       44.05       0.5        2.41       0.5
1971       52.99       5.5        2.05       3.0
1972       52.48       2.5        2.39       2.0
1973       37.87      13.0        2.25       6.0
1974       36.89       0.0        2.30       0.0
1975       51.23       0.0        2.80       0.0
1976       33.61       0.0        1.66       0.0
1977       37.60       3.5        2.23       2.5
1978       54.49       7.5        3.50       6.0
1979       49.09      14.5        3.00      10.5
1980       47.77      25.1        4.62       8.5
1981       39.76       3.9        3.86       3.0
1982       56.40       0.5        3.10       0.5
1983       64.08       5.3        2.19       3.5
1984       50.40       5.0        2.86       3.0
1985       54.59       6.7        4.42       2.5
1986       33.30       1.3        2.47       1.0
1987       45.39      14.3        3.27       4.0
1988       36.23       6.8        2.49       6.5
1989       57.28      11.5        2.31       3.5
1990       44.84       0.0        4.11       0.0
1991       39.02       0.0        2.23       0.0
1992       49.79       0.0        3.07       0.0
1993       48.63       4.9        3.38       2.5
1994       41.60       1.5        3.15       1.5
1995       53.23       0.8        4.57       0.5
1996       56.97      12.4        6.60       3.2
1997       39.15       0.2        1.79       0.2
1998       50.93       0.5        3.27       0.5
1999       61.25       0.0        7.68       0.0
2000       42.47      20.7        5.12      11.8
2001       40.13       1.2        3.01       0.7
2002       46.57       0.0        4.02       0.0
2003       57.11       4.5        1.72       2.3
2004       42.33      15.2        1.72       3.8
2005       45.40       0.4        2.42       0.3
2006       50.86       0.0        4.23       0.0
2007       34.82       0.0        3.25       0.0
2008       55.39       0.0        4.80       0.0
2009       47.65       0.0        2.60       0.0
2010       38.15       0.0        3.00       0.0
2011       39.40       0.0        2.65       0.0
2012       43.26       0.0        3.80       0.0
2013       53.08       0.0        4.88       0.0
2014       43.48       0.1        4.42       0.1
2015       54.43      24.0        2.63       4.0
2016       47.71       0.0        4.33       0.0
2017       36.42       3.0        2.00       3.0
2018       68.96      44.5        6.25       7.0
2019       43.35       0.0        2.79       0.0
2020       34.92       0.0        2.80       0.0
```

c1 + c2
c1 + c3
c1 + c4
c2 + c3
c2 + c4
c3 + c4

```python
sns.pairplot(df_annual_combined)
```

_result:_
```
<seaborn.axisgrid.PairGrid at 0x7f65da58fcc0>
```

_result:_
```
<Figure size 720x720 with 20 Axes>
```

```python
sns.pairplot(df_annual_combined, kind='reg', diag_kind='kde')
```

_result:_
```
<seaborn.axisgrid.PairGrid at 0x7f65d1ceac18>
```

_result:_
```
<Figure size 720x720 with 20 Axes>
```

```python
sns.pairplot(df, vars=['precip', 'tmin', 'tmax'], hue='month', plot_kws={'alpha': 0.2})
```

_result:_
```
<seaborn.axisgrid.PairGrid at 0x7f65d1502780>
```

_result:_
```
<Figure size 627.675x540 with 12 Axes>
```

```python
## what if we just want winter months?
winter_rows = [i for i in range(df.shape[0]) if df['month'].iloc[i] in [12, 1, 2]]
```

```python
df_winter = df.iloc[winter_rows, :]
df_winter
```

_result:_
```
precip  snow  tmax  tmin  year  month  day
date                                                  
1970-01-01    0.10   0.0  61.0  35.0  1970      1    1
1970-01-02    0.09   0.0  38.0  23.0  1970      1    2
1970-01-03    0.00   0.0  37.0  25.0  1970      1    3
1970-01-04    0.00   0.0  49.0  23.0  1970      1    4
1970-01-05    0.00   0.0  41.0  17.0  1970      1    5
...            ...   ...   ...   ...   ...    ...  ...
2020-02-24    0.00   0.0  62.0  24.0  2020      2   24
2020-02-25    0.48   0.0  53.0  45.0  2020      2   25
2020-02-26    0.02   0.0  65.0  49.0  2020      2   26
2020-02-28    0.00   0.0  49.0  26.0  2020      2   28
2020-02-29    0.00   0.0  52.0  26.0  2020      2   29

[4498 rows x 7 columns]
```

```python
sns.pairplot(df_winter, vars=['precip', 'tmin', 'tmax'], hue='month', plot_kws={'alpha': 0.2})
```

_result:_
```
<seaborn.axisgrid.PairGrid at 0x7f65d0f36208>
```

_result:_
```
<Figure size 627.675x540 with 12 Axes>
```

```python
## Using colormaps
plt.scatter(df_annual_min['tmin'], df_annual_max['tmax'], c = df_annual_max.index, cmap = 'viridis')
cbar = plt.colorbar()
cbar.set_label('Year')
plt.xlabel('Min Temperature (F)')
plt.ylabel('Max Temperature (F)')
```

_result:_
```
Text(0, 0.5, 'Max Temperature (F)')
```

_result:_
```
<Figure size 432x288 with 2 Axes>
```

```python
## Saving your figures
plt.scatter(df_annual_min['tmin'], df_annual_max['tmax'], c = df_annual_max.index, cmap = 'viridis')
cbar = plt.colorbar()
cbar.set_label('Year')
plt.xlabel('Min Temperature (F)')
plt.ylabel('Max Temperature (F)')

# save as png with 300 dpi resolution
plt.savefig('annual_min_vs_max_temp.png', bbox_inches='tight', dpi=300)

# save as eps vector format so you can edit in Illustrator
plt.savefig('annual_min_vs_max_temp.eps', bbox_inches='tight')
```

_result:_
```
<Figure size 432x288 with 2 Axes>
```
