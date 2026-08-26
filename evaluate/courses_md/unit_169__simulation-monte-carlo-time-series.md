---
title: "Simulation, Monte Carlo, & time series"
unit_id: 169
course_id: 6
level: "Foundation"
slug: simulation-monte-carlo-time-series
is_course: 0
---

# Simulation, Monte Carlo, & time series

## Fetched resources (external URLs)

### Notes: Simulation & Monte Carlo (notebook)
*URL:* https://github.com/PurdueCyberTraining/python4env/blob/main/Lec7-0-MonteCarlo/Lec9_ResevoirMonteCarlo.ipynb

# Lecture 9: Intro to reservoir simulation and Monte Carlo methods
ENVR 890-001: Python for Environmental Research, Fall 2020

October 23, 2020

By Andrew Hamilton. Some material adapted from Greg Characklis, David Gorelick and H.B. Zeff.

## Summary
In this lecture, we will learn how to use **Monte Carlo methods** to account for uncertainty/probability in computer models. We will then build a model a **reservoir simulation model** and apply Monte Carlo to see how uncertainty propagates through the system.

## Monte Carlo (MC) methods
### Intro
***See hand-written notes pdf, Part 1, for introductory context***

### Implementation
Here we will implement the simple MC problem introduced in the notes.

First, assume we have estimated that daily PM10 concentrations in a particular region is approximately normally distributed with a mean ($\mu$) of 90 ug/m3 and a standard deviation ($\sigma$) of 20 ug/m3. We saw in the notes how to estimate the probability of violating the 150 ug/m3 standard on any particular day, and how to calculate the 95 percentile of PM10. Here is how to do that with MC sampling.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import normal, lognormal
from scipy.stats import skew, kurtosis
```

```python
### define variables
mu = 90
sigma = 20
standard = 150
nsamples = 1000000
```

```python
### sample from normal distribution
pm10 = normal(mu, sigma, size = nsamples)
pm10
```

_result:_
```
array([96.43473056, 74.89176564, 87.08563391, ..., 81.13149679,
       96.85613204, 94.33673982])
```

```python
### get sample statistics & histogram. increase number of samples if necessary
print(f'Mean: {pm10.mean():.4f}')
print(f'Std: {pm10.std():.4f}')
print(f'Skew: {skew(pm10):.4f}')
print(f'Excess Kurtosis: {kurtosis(pm10):.4f}')
plt.hist(pm10, bins=20)
```

_output:_
```
Mean: 89.9954
Std: 20.0040
Skew: -0.0052
Excess Kurtosis: 0.0106
```

_result:_
```
(array([1.20000e+01, 6.20000e+01, 4.69000e+02, 2.11600e+03, 7.56600e+03,
        2.24740e+04, 5.40380e+04, 1.01802e+05, 1.55003e+05, 1.88053e+05,
        1.81107e+05, 1.38477e+05, 8.50910e+04, 4.12530e+04, 1.60700e+04,
        4.88900e+03, 1.21100e+03, 2.60000e+02, 3.60000e+01, 1.10000e+01]),
 array([ -4.60235481,   5.01678505,  14.6359249 ,  24.25506476,
         33.87420462,  43.49334448,  53.11248433,  62.73162419,
         72.35076405,  81.9699039 ,  91.58904376, 101.20818362,
        110.82732348, 120.44646333, 130.06560319, 139.68474305,
        149.3038829 , 158.92302276, 168.54216262, 178.16130248,
        187.78044233]),
 <BarContainer object of 20 artists>)
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### probability of violating standard?
violations = pm10 > standard
print(violations)
print()
```

_output:_
```
[False False False ... False False False]
```

```python
prob_violation = violations.mean()
print(f'Probability of violation: {prob_violation:.4f}')
```

_output:_
```
Probability of violation: 0.0014
```

```python
### 95th percentile of pm10?
p95_pm10 = np.quantile(pm10, 0.95)
print(f'95th percentile: {p95_pm10:.4f} ug/m3')
```

_output:_
```
95th percentile: 122.8542 ug/m3
```

Now consider the expected cardiovascular deaths based on pm10 from Lecture 4 (*note again that I made this up, not a real relationship*). 

$$deaths = \frac{15}{1 + \exp(-(PM10 - 80) / 35)}$$

We can very easily calculate statistics of interest for this quantity using our MC samples. This would be much more difficult to do analytically with pen and paper.

```python
### equation for cardiovascular deaths as a function of pm10 (numpy compatible)
def get_deaths_pm10(pm10_array):
    return 15 / (1 + np.exp(- ( pm10_array - 80 ) / 35))

deaths = get_deaths_pm10(pm10)
deaths
```

_result:_
```
array([9.22920738, 6.95365865, 8.25659277, ..., 7.62122124, 9.27189766,
       9.01495547])
```

```python
### look at distribution of deaths
print(f'Mean: {deaths.mean():.4f}')
print(f'Std: {deaths.std():.4f}')
print(f'Skew: {skew(deaths):.4f}')
print(f'Excess Kurtosis: {kurtosis(deaths):.4f}')
plt.hist(deaths)
```

_output:_
```
Mean: 8.4900
Std: 1.9638
Skew: -0.1811
Excess Kurtosis: -0.3880
```

_result:_
```
(array([   549.,   8752.,  42489., 111255., 193204., 244969., 222812.,
        134103.,  39348.,   2519.]),
 array([ 1.22804575,  2.53929623,  3.85054671,  5.1617972 ,  6.47304768,
         7.78429816,  9.09554864, 10.40679912, 11.7180496 , 13.02930008,
        14.34055056]),
 <BarContainer object of 10 artists>)
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### probability of more than 12 deaths?
deaths_g12 = deaths > 12
print(deaths_g12)
print()
```

_output:_
```
[False False False ... False False False]
```

```python
prob_deaths_gt12 = deaths_g12.mean()
print(f'Probability of >12 deaths: {prob_deaths_gt12:.4f}')
```

_output:_
```
Probability of >12 deaths: 0.0268
```

```python
### 95th percentile of pm10?
p95_deaths = np.quantile(deaths, 0.95)
print(f'95th percentile: {p95_deaths:.4f} deaths')
```

_output:_
```
95th percentile: 11.5926 deaths
```

## Reservoir simulation
### Intro
***See hand-written notes pdf, Part 2, for introductory context***

***Pick up here after notes Part 2 (sorry, my ipad died in the middle of writing the notes "live" in class)***

(inflow + precip) - (release + evap) = change in storage

change in storage = storage_t - storage_{t-1}

assume precip = evap = 0

storage_t - stoarge{t-1} = inflow - release

storage_t = storage_{t-1} + inflow - release

Assume storage_0 = 1 million acre-feet (MAF)
       inflow = 0.2 MAF
       demand = 0.4 MAF
       
       storage_1 = 0.8 MAF
       
Problems: negative storage.
        release = demand
        storage_t = storage_{t-1} + inflow - release
        check if stoarage_t < 0, if so:
            release = release + storage_t
            storage_t = 0

Assume storage_0 = 1 million acre-feet (MAF)
       inflow = 0.6 MAF
       demand = 0.4 MAF
       
       storage_1 = 1.2 MAF
       
Problem: define max storage as storage_max = 2 MAF
        check if storage_t > storage_max, if so:
            release += (storage_t - storage_max)
            storage = storage_max
            
Other complications which we won't cover in this class: 
    Min storage (dead storage)
    Min lake level (recreation)
    Min outflow environmental
            
        

### In-class exercises
**Implementing a deterministic model**
Consider, as in the notes, a reservoir with a maximum storage capacity of 2 MAF. 

**Exercise 1**: Write a function that will take as inputs the current storage, inflow, and demand, and return the reservoir release and the updated storage. Make sure that it works in both of the important edge cases: (1) when there is not enough water to meet demand, and (2) when the reservoir runs out of storage capacity.

**Exercise 2**: Assume that current storage is 1 MAF and that demand each year is equal to 0.5 MAF per year. Use a while loop to answer the following two questions: (1) If inflows are equal to 0.3 MAF/year, in which year will we first be unable to meet our demand? (2) If inflows are 0.6 MAF/year, in which year will we first spill excess water?

**Exercise 3:** Use a for loop to simulate the reservoir system over 20 years, and store the inflow, demand, release, and storage at each time step. Store the results in a NumPy array, and then plot all 4 outputs on the same plot. Do this for both inflow scenarios.

**Implementing an uncertain model with Monte Carlo sampling**

**Exercise 4**: In reality, inflows will vary stochastically from year to year. Repeat exercise 3, but with inflows that are sampled from a lognormal distribution with a mean of -1 and a standard deviation of 0.7 (remember these parameters are in log space).

**Exercise 5**: Now suppose we are interested in a probabilistic assessment of possible outcomes over 20 years. We don't just want to run a single 20-year simulation, but rather to run a Monte Carlo analysis of the *entire simulation*.
- Run 1000 simulations of 20-years each. Store the inflow, demand, release, and storage for each year in a 1000x20x4 NumPy array.

- Calculate the final storage in year 20. What are the mean and std? Plot a histogram.

- Calculate the distribution of water deficit fractions ((demand minus release)/demand). What are the mean and 95th percentile?

### Notes: Simulation, Monte Carlo, & time series (notebook)
*URL:* https://github.com/PurdueCyberTraining/python4env/blob/main/Lec7-1-Timeseries/Lec10_ReservoirTimeSeries.ipynb

# Lecture 10: Reservoir simulation and time series analysis
ENVR 890-001: Python for Environmental Research, Fall 2020

October 30, 2020

By Andrew Hamilton. Some material adapted from Greg Characklis, David Gorelick and H.B. Zeff.

## Summary
In this lecture, we will learn how to use **time series analysis** to create **synthetic streamflow records** using historical data. This will help us to improve our Monte Carlo analysis for a reservoir simulation model. We will use real data of historical inflows into Shasta Reservoir in northern California.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##read input data
shasta = pd.read_csv('shasta_inflow.csv', header=2)

## just care about inflow column
shasta = shasta.iloc[:, 0:2]
shasta.columns = ['date', 'inflow']
shasta
```

_result:_
```
date  inflow
0    Oct-80  18,040
1    Nov-80  18,040
2    Dec-80  27,590
3    Jan-81  36,940
4    Feb-81  49,280
..      ...     ...
475  May-20  31,934
476  Jun-20  23,458
477  Jul-20  20,061
478  Aug-20  18,682
479  Sep-20  18,143

[480 rows x 2 columns]
```

```python
## transform date to datetime type and set index 
##   (see here for datetime format specifiers: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
shasta['date'] = pd.to_datetime(shasta['date'], format='%b-%y')
shasta.index = shasta['date']
shasta = shasta.iloc[:, [1]]
shasta
```

_result:_
```
inflow
date              
1980-10-01  18,040
1980-11-01  18,040
1980-12-01  27,590
1981-01-01  36,940
1981-02-01  49,280
...            ...
2020-05-01  31,934
2020-06-01  23,458
2020-07-01  20,061
2020-08-01  18,682
2020-09-01  18,143

[480 rows x 1 columns]
```

```python
## create time step variable (note order of dates)
shasta['time'] = list(range(shasta.shape[0]))
shasta
```

_result:_
```
inflow  time
date                    
1980-10-01  18,040     0
1980-11-01  18,040     1
1980-12-01  27,590     2
1981-01-01  36,940     3
1981-02-01  49,280     4
...            ...   ...
2020-05-01  31,934   475
2020-06-01  23,458   476
2020-07-01  20,061   477
2020-08-01  18,682   478
2020-09-01  18,143   479

[480 rows x 2 columns]
```

```python
### plot data
plt.figure()
plt.plot(shasta['inflow'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb612c05400>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### weirdness here is because inflow is a string. turns out the data is formatted with commas at thousands. need to remove.
print(shasta['inflow'])
print()

shasta['inflow'] = [s.replace(',','') for s in shasta['inflow']]
print(shasta['inflow'])
print()

## now convert to numeric type
shasta['inflow'] = pd.to_numeric(shasta['inflow'])
shasta['inflow']
```

_output:_
```
date
1980-10-01    18,040
1980-11-01    18,040
1980-12-01    27,590
1981-01-01    36,940
1981-02-01    49,280
               ...  
2020-05-01    31,934
2020-06-01    23,458
2020-07-01    20,061
2020-08-01    18,682
2020-09-01    18,143
Name: inflow, Length: 480, dtype: object

date
1980-10-01    18040
1980-11-01    18040
1980-12-01    27590
1981-01-01    36940
1981-02-01    49280
              ...  
2020-05-01    31934
2020-06-01    23458
2020-07-01    20061
2020-08-01    18682
2020-09-01    18143
Name: inflow, Length: 480, dtype: object
```

_result:_
```
date
1980-10-01    18040
1980-11-01    18040
1980-12-01    27590
1981-01-01    36940
1981-02-01    49280
              ...  
2020-05-01    31934
2020-06-01    23458
2020-07-01    20061
2020-08-01    18682
2020-09-01    18143
Name: inflow, Length: 480, dtype: int64
```

```python
### plot data
plt.figure()
plt.plot(shasta['inflow'])

plt.figure()
plt.hist(shasta['inflow'])
```

_result:_
```
(array([367.,  56.,  22.,  20.,   5.,   3.,   3.,   2.,   1.,   1.]),
 array([ 11800.,  52560.,  93320., 134080., 174840., 215600., 256360.,
        297120., 337880., 378640., 419400.]),
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

```python
### fit to lognormal distribution
from scipy.stats import lognorm, gamma, norm

ln_shape, ln_loc, ln_scale = lognorm.fit(shasta['inflow'])
ln_shape, ln_loc, ln_scale
```

_result:_
```
(1.17000294351462, 11488.66279965279, 17421.080931349352)
```

```python
### check fit
shasta['inflow'].mean()
print(f"Mean: data = {shasta['inflow'].mean()}, fit = {lognorm.mean(ln_shape, ln_loc, ln_scale)}")
print(f"Std: data = {shasta['inflow'].std()}, fit = {lognorm.std(ln_shape, ln_loc, ln_scale)}")
```

_output:_
```
Mean: data = 46920.05, fit = 46029.228979321575
Std: data = 52118.67731949871, fit = 59134.531366248055
```

```python
### plot theoretical distribution vs histogram
flow = np.arange(0, 400000, 1000)
ln_pdf = lognorm.pdf(flow, ln_shape, ln_loc, ln_scale)

plt.hist(shasta['inflow'], density=True, bins=30)
plt.plot(flow, ln_pdf)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb60a56f438>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### now generate a synthetic record of length 480 months (40 years)
shasta['synthetic1_inflow'] = lognorm.rvs(ln_shape, ln_loc, ln_scale, size=480)
shasta['synthetic1_inflow']
```

_result:_
```
date
1980-10-01    114881.544148
1980-11-01     18010.212413
1980-12-01     53064.301113
1981-01-01     21992.309629
1981-02-01     72251.516684
                  ...      
2020-05-01     33519.012963
2020-06-01     26073.375601
2020-07-01     19172.927826
2020-08-01     39590.383968
2020-09-01     50158.195868
Name: synthetic1_inflow, Length: 480, dtype: float64
```

```python
### plot historical vs synthetic
plt.figure()
plt.plot(shasta['inflow'], label='historic')
plt.plot(shasta['synthetic1_inflow'], label='synthetic1_inflow')
plt.legend()

### first 5 years
plt.figure()
plt.plot(shasta['inflow'].iloc[:60], label='historic')
plt.plot(shasta['synthetic1_inflow'].iloc[:60], label='synthetic1_inflow')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7fb60a4747f0>
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
### what about seasonality? we know that flow varies in predictable way from season to season.
shasta['month'] = shasta.index.month

monthly_mean = shasta.groupby('month').mean()['inflow']
monthly_std = shasta.groupby('month').std()['inflow']
monthly_std
```

_result:_
```
month
1     66399.428282
2     84932.869224
3     73653.921698
4     54323.871697
5     30773.351441
6     13698.485590
7      5627.160451
8      4179.013259
9      4718.133359
10     8136.188860
11    15923.530043
12    49743.751787
Name: inflow, dtype: float64
```

```python
monthly_mean_synthetic1 = shasta.groupby('month').mean()['synthetic1_inflow']
monthly_std_synthetic1 = shasta.groupby('month').std()['synthetic1_inflow']

plt.plot(monthly_mean, color='k')
plt.plot(monthly_mean + monthly_std, color='k', ls=':')
plt.plot(monthly_mean - monthly_std, color='k', ls=':')

plt.plot(monthly_mean_synthetic1, color='royalblue')
plt.plot(monthly_mean_synthetic1 + monthly_std_synthetic1, color='royalblue', ls=':')
plt.plot(monthly_mean_synthetic1 - monthly_std_synthetic1, color='royalblue', ls=':')

plt.xlabel('month')
plt.ylabel('inflow (AF)')
```

_result:_
```
Text(0, 0.5, 'inflow (AF)')
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### Want to account for seasonality and autocorrelation. First log transform.
shasta['log'] = np.log(shasta['inflow'])
plt.plot(shasta['log'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb60a3c7cc0>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### check for trend over time? if so you would want to remove (then add back later) by working with residuals
import statsmodels.formula.api as sm

lm_log_time = sm.ols('log ~ time', data=shasta)
lm_log_time_fit = lm_log_time.fit()
print(lm_log_time_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                    log   R-squared:                       0.004
Model:                            OLS   Adj. R-squared:                  0.002
Method:                 Least Squares   F-statistic:                     1.943
Date:                Tue, 26 Jan 2021   Prob (F-statistic):              0.164
Time:                        09:33:36   Log-Likelihood:                -534.02
No. Observations:                 480   AIC:                             1072.
Df Residuals:                     478   BIC:                             1080.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     10.3341      0.067    153.710      0.000      10.202      10.466
time           0.0003      0.000      1.394      0.164      -0.000       0.001
==============================================================================
Omnibus:                       71.243   Durbin-Watson:                   0.581
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              100.018
Skew:                           1.094   Prob(JB):                     1.91e-22
Kurtosis:                       3.461   Cond. No.                         553.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
### seems to be no trend here, but if so you would want to remove (then add back later) by working with residuals
```

```python
### There are a few ways to deal with this, but we will "deseasonalize" data by converting to monthly z-scores
monthly_mean_log = shasta.groupby('month').mean()['log']
monthly_std_log = shasta.groupby('month').std()['log']

shasta['deseas'] = shasta['log'].copy()
for i in range(1, 13):
    mu = monthly_mean_log[i]
    sigma = monthly_std_log[i]
    shasta['deseas'].loc[shasta['month'] == i] = (shasta['deseas'].loc[shasta['month'] == i] - mu) / sigma
    
plt.plot(shasta['deseas'])
```

_output:_
```
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb60a05b710>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
plt.hist(shasta['deseas'])
```

_result:_
```
(array([ 11.,  61., 101., 118.,  73.,  50.,  32.,  22.,   8.,   4.]),
 array([-2.06683404, -1.53048268, -0.99413133, -0.45777997,  0.07857138,
         0.61492274,  1.1512741 ,  1.68762545,  2.22397681,  2.76032816,
         3.29667952]),
 <BarContainer object of 10 artists>)
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### This looks more random! But let's check whether autocorrelation seems significant
plt.figure()
plt.scatter(shasta['deseas'].iloc[1:], shasta['deseas'].iloc[:-1])
```

_result:_
```
<matplotlib.collections.PathCollection at 0x7fb609f982e8>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
from statsmodels.graphics.tsaplots import plot_acf
plt.figure()
fig = plot_acf(shasta['deseas'])
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
shasta
```

_result:_
```
inflow  time  synthetic1_inflow  month        log    deseas
date                                                                   
1980-10-01   18040     0      114881.544148     10   9.800347 -0.444284
1980-11-01   18040     1       18010.212413     11   9.800347 -0.731735
1980-12-01   27590     2       53064.301113     12  10.225209 -0.530423
1981-01-01   36940     3       21992.309629      1  10.517050 -0.444682
1981-02-01   49280     4       72251.516684      2  10.805274 -0.297438
...            ...   ...                ...    ...        ...       ...
2020-05-01   31934   475       33519.012963      5  10.371427 -0.299713
2020-06-01   23458   476       26073.375601      6  10.062967 -0.233931
2020-07-01   20061   477       19172.927826      7   9.906533 -0.101971
2020-08-01   18682   478       39590.383968      8   9.835316  0.084289
2020-09-01   18143   479       50158.195868      9   9.806040 -0.089005

[480 rows x 6 columns]
```

```python
### create lag variables to deal with auto-correlation
shasta['deseas_l1'] = np.nan
shasta['deseas_l2'] = np.nan
shasta['deseas_l3'] = np.nan
shasta['deseas_l12'] = np.nan

shasta['deseas_l1'].iloc[1:] = shasta['deseas'].values[:-1]
shasta['deseas_l2'].iloc[2:] = shasta['deseas'].values[:-2]
shasta['deseas_l3'].iloc[3:] = shasta['deseas'].values[:-3]
shasta['deseas_l12'].iloc[12:] = shasta['deseas'].values[:-12]

shasta
```

_output:_
```
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
```

_result:_
```
inflow  time  synthetic1_inflow  month        log    deseas  \
date                                                                      
1980-10-01   18040     0      114881.544148     10   9.800347 -0.444284   
1980-11-01   18040     1       18010.212413     11   9.800347 -0.731735   
1980-12-01   27590     2       53064.301113     12  10.225209 -0.530423   
1981-01-01   36940     3       21992.309629      1  10.517050 -0.444682   
1981-02-01   49280     4       72251.516684      2  10.805274 -0.297438   
...            ...   ...                ...    ...        ...       ...   
2020-05-01   31934   475       33519.012963      5  10.371427 -0.299713   
2020-06-01   23458   476       26073.375601      6  10.062967 -0.233931   
2020-07-01   20061   477       19172.927826      7   9.906533 -0.101971   
2020-08-01   18682   478       39590.383968      8   9.835316  0.084289   
2020-09-01   18143   479       50158.195868      9   9.806040 -0.089005   

            deseas_l1  deseas_l2  deseas_l3  deseas_l12  
date                                                     
1980-10-01        NaN        NaN        NaN         NaN  
1980-11-01  -0.444284        NaN        NaN         NaN  
1980-12-01  -0.731735  -0.444284        NaN         NaN  
1981-01-01  -0.530423  -0.731735  -0.444284         NaN  
1981-02-01  -0.444682  -0.530423  -0.731735         NaN  
...               ...        ...        ...         ...  
2020-05-01  -0.542635  -1.699564  -0.972306    1.206725  
2020-06-01  -0.299713  -0.542635  -1.699564    0.973991  
2020-07-01  -0.233931  -0.299713  -0.542635    1.203015  
2020-08-01  -0.101971  -0.233931  -0.299713    1.069099  
2020-09-01   0.084289  -0.101971  -0.233931    0.463861  

[480 rows x 10 columns]
```

```python
### set up autoregressive models with different lags
lm_log_ar = sm.ols('deseas ~ deseas_l1 + deseas_l2 + deseas_l3 + deseas_l12', data=shasta)
lm_log_ar_fit = lm_log_ar.fit()
print(lm_log_ar_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 deseas   R-squared:                       0.475
Model:                            OLS   Adj. R-squared:                  0.470
Method:                 Least Squares   F-statistic:                     104.6
Date:                Tue, 26 Jan 2021   Prob (F-statistic):           2.19e-63
Time:                        09:33:37   Log-Likelihood:                -511.32
No. Observations:                 468   AIC:                             1033.
Df Residuals:                     463   BIC:                             1053.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.0049      0.034      0.147      0.883      -0.061       0.071
deseas_l1      0.6332      0.046     13.620      0.000       0.542       0.725
deseas_l2      0.0377      0.055      0.687      0.492      -0.070       0.146
deseas_l3      0.0512      0.047      1.095      0.274      -0.041       0.143
deseas_l12     0.0029      0.035      0.083      0.934      -0.065       0.071
==============================================================================
Omnibus:                       77.037   Durbin-Watson:                   2.009
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              158.450
Skew:                           0.899   Prob(JB):                     3.92e-35
Kurtosis:                       5.212   Cond. No.                         3.06
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
### set up autoregressive models with different lags
lm_log_ar = sm.ols('deseas ~ deseas_l1 + deseas_l2 + deseas_l3', data=shasta)
lm_log_ar_fit = lm_log_ar.fit()
print(lm_log_ar_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 deseas   R-squared:                       0.477
Model:                            OLS   Adj. R-squared:                  0.473
Method:                 Least Squares   F-statistic:                     143.7
Date:                Tue, 26 Jan 2021   Prob (F-statistic):           3.50e-66
Time:                        09:33:37   Log-Likelihood:                -517.27
No. Observations:                 477   AIC:                             1043.
Df Residuals:                     473   BIC:                             1059.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.0018      0.033      0.056      0.955      -0.063       0.067
deseas_l1      0.6345      0.046     13.818      0.000       0.544       0.725
deseas_l2      0.0380      0.054      0.698      0.485      -0.069       0.145
deseas_l3      0.0522      0.046      1.137      0.256      -0.038       0.142
==============================================================================
Omnibus:                       80.825   Durbin-Watson:                   2.010
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              171.644
Skew:                           0.912   Prob(JB):                     5.34e-38
Kurtosis:                       5.304   Cond. No.                         3.01
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
### set up autoregressive models with different lags
lm_log_ar = sm.ols('deseas ~ deseas_l1 + deseas_l2', data=shasta)
lm_log_ar_fit = lm_log_ar.fit()
print(lm_log_ar_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 deseas   R-squared:                       0.476
Model:                            OLS   Adj. R-squared:                  0.473
Method:                 Least Squares   F-statistic:                     215.5
Date:                Tue, 26 Jan 2021   Prob (F-statistic):           2.53e-67
Time:                        09:33:37   Log-Likelihood:                -518.51
No. Observations:                 478   AIC:                             1043.
Df Residuals:                     475   BIC:                             1056.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.0017      0.033      0.053      0.958      -0.063       0.066
deseas_l1      0.6383      0.046     13.951      0.000       0.548       0.728
deseas_l2      0.0713      0.046      1.559      0.120      -0.019       0.161
==============================================================================
Omnibus:                       77.902   Durbin-Watson:                   2.007
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              163.116
Skew:                           0.886   Prob(JB):                     3.80e-36
Kurtosis:                       5.247   Cond. No.                         2.33
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
### set up autoregressive models with different lags
lm_log_ar = sm.ols('deseas ~ deseas_l1', data=shasta)
lm_log_ar_fit = lm_log_ar.fit()
print(lm_log_ar_fit.summary())
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 deseas   R-squared:                       0.473
Model:                            OLS   Adj. R-squared:                  0.472
Method:                 Least Squares   F-statistic:                     428.5
Date:                Tue, 26 Jan 2021   Prob (F-statistic):           2.15e-68
Time:                        09:33:37   Log-Likelihood:                -520.49
No. Observations:                 479   AIC:                             1045.
Df Residuals:                     477   BIC:                             1053.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.0008      0.033      0.024      0.981      -0.064       0.065
deseas_l1      0.6878      0.033     20.700      0.000       0.622       0.753
==============================================================================
Omnibus:                       75.055   Durbin-Watson:                   2.098
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              154.700
Skew:                           0.861   Prob(JB):                     2.56e-34
Kurtosis:                       5.188   Cond. No.                         1.01
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
### set up autoregressive models with different lags
lm_log_ar = sm.ols('deseas ~ deseas_l1 + deseas_l12', data=shasta)
lm_log_ar_fit = lm_log_ar.fit()
print(lm_log_ar_fit.summary())
### although deseas_l12 is not significant, this one is still best in terms of AIC/BIC, so let's go with it.
```

_output:_
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                 deseas   R-squared:                       0.471
Model:                            OLS   Adj. R-squared:                  0.468
Method:                 Least Squares   F-statistic:                     206.7
Date:                Tue, 26 Jan 2021   Prob (F-statistic):           5.89e-65
Time:                        09:33:37   Log-Likelihood:                -513.07
No. Observations:                 468   AIC:                             1032.
Df Residuals:                     465   BIC:                             1045.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.0051      0.034      0.152      0.879      -0.061       0.071
deseas_l1      0.6837      0.034     19.996      0.000       0.617       0.751
deseas_l12     0.0116      0.034      0.339      0.735      -0.056       0.079
==============================================================================
Omnibus:                       71.085   Durbin-Watson:                   2.095
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              141.035
Skew:                           0.849   Prob(JB):                     2.37e-31
Kurtosis:                       5.085   Cond. No.                         1.18
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
### now look at residuals to see if they look like "white noise" (uncorrelated & normally distributed)
shasta['ar_resid'] = lm_log_ar_fit.resid
print(shasta)

plt.figure()
plt.plot(shasta['ar_resid'])

plt.figure()
plt.hist(shasta['ar_resid'])

plt.figure()
fig = plot_acf(shasta['ar_resid'].iloc[12:])
```

_output:_
```
inflow  time  synthetic1_inflow  month        log    deseas  \
date                                                                      
1980-10-01   18040     0      114881.544148     10   9.800347 -0.444284   
1980-11-01   18040     1       18010.212413     11   9.800347 -0.731735   
1980-12-01   27590     2       53064.301113     12  10.225209 -0.530423   
1981-01-01   36940     3       21992.309629      1  10.517050 -0.444682   
1981-02-01   49280     4       72251.516684      2  10.805274 -0.297438   
...            ...   ...                ...    ...        ...       ...   
2020-05-01   31934   475       33519.012963      5  10.371427 -0.299713   
2020-06-01   23458   476       26073.375601      6  10.062967 -0.233931   
2020-07-01   20061   477       19172.927826      7   9.906533 -0.101971   
2020-08-01   18682   478       39590.383968      8   9.835316  0.084289   
2020-09-01   18143   479       50158.195868      9   9.806040 -0.089005   

            deseas_l1  deseas_l2  deseas_l3  deseas_l12  ar_resid  
date                                                               
1980-10-01        NaN        NaN        NaN         NaN       NaN  
1980-11-01  -0.444284        NaN        NaN         NaN       NaN  
1980-12-01  -0.731735  -0.444284        NaN         NaN       NaN  
1981-01-01  -0.530423  -0.731735  -0.444284         NaN       NaN  
1981-02-01  -0.444682  -0.530423  -0.731735         NaN       NaN  
...               ...        ...        ...         ...       ...  
2020-05-01  -0.542635  -1.699564  -0.972306    1.206725  0.052203  
2020-06-01  -0.299713  -0.542635  -1.699564    0.973991 -0.045411  
2020-07-01  -0.233931  -0.299713  -0.542635    1.203015  0.038914  
2020-08-01  -0.101971  -0.233931  -0.299713    1.069099  0.136501  
2020-09-01   0.084289  -0.101971  -0.233931    0.463861 -0.157126  

[480 rows x 11 columns]
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
### ok, so we have "whitened" data! Now what? Now we can turn around and create synthetic data by reversing the process

## first, generate synthetic normally distributed data:
shasta['synthetic2_noise'] = norm.rvs(shasta['ar_resid'].mean(), shasta['ar_resid'].std(), size=shasta.shape[0])

plt.plot(shasta['ar_resid'])
plt.plot(shasta['synthetic2_noise'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb60885b780>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### now apply the AR relationship. here is a function to get regression prediction
def predict_ar(lag1, lag12):
    return lm_log_ar_fit.params[0] + lm_log_ar_fit.params[1] * lag1 + lm_log_ar_fit.params[2] * lag12
```

```python
### We need 12 years of lagged data to start, we can use the last 12 years of real data
max_lag = 12
nrow = shasta.shape[0]

synth_ar = list(shasta['deseas'].iloc[-max_lag:])
synth_ar
```

_result:_
```
[-0.09792584872618817,
 -0.5475876282161891,
 -0.09502852787233809,
 -0.2982314261607055,
 -0.9723064332676717,
 -1.6995636521606121,
 -0.5426345851536128,
 -0.29971257285774494,
 -0.2339307085905822,
 -0.10197063412202698,
 0.08428937601882568,
 -0.08900534098288752]
```

```python
### now add prediction plus noise to get AR time series
for i in range(nrow):
    lag12 = synth_ar[i]
    lag1 = synth_ar[i + max_lag - 1]
    prediction = predict_ar(lag1, lag12)
    noise = shasta['synthetic2_noise'].iloc[i]
    synth_ar.append(prediction + noise)
    
shasta['synthetic2_deseas'] = synth_ar[-nrow:]
shasta
```

_result:_
```
inflow  time  synthetic1_inflow  month        log    deseas  \
date                                                                      
1980-10-01   18040     0      114881.544148     10   9.800347 -0.444284   
1980-11-01   18040     1       18010.212413     11   9.800347 -0.731735   
1980-12-01   27590     2       53064.301113     12  10.225209 -0.530423   
1981-01-01   36940     3       21992.309629      1  10.517050 -0.444682   
1981-02-01   49280     4       72251.516684      2  10.805274 -0.297438   
...            ...   ...                ...    ...        ...       ...   
2020-05-01   31934   475       33519.012963      5  10.371427 -0.299713   
2020-06-01   23458   476       26073.375601      6  10.062967 -0.233931   
2020-07-01   20061   477       19172.927826      7   9.906533 -0.101971   
2020-08-01   18682   478       39590.383968      8   9.835316  0.084289   
2020-09-01   18143   479       50158.195868      9   9.806040 -0.089005   

            deseas_l1  deseas_l2  deseas_l3  deseas_l12  ar_resid  \
date                                                                
1980-10-01        NaN        NaN        NaN         NaN       NaN   
1980-11-01  -0.444284        NaN        NaN         NaN       NaN   
1980-12-01  -0.731735  -0.444284        NaN         NaN       NaN   
1981-01-01  -0.530423  -0.731735  -0.444284         NaN       NaN   
1981-02-01  -0.444682  -0.530423  -0.731735         NaN       NaN   
...               ...        ...        ...         ...       ...   
2020-05-01  -0.542635  -1.699564  -0.972306    1.206725  0.052203   
2020-06-01  -0.299713  -0.542635  -1.699564    0.973991 -0.045411   
2020-07-01  -0.233931  -0.299713  -0.542635    1.203015  0.038914   
2020-08-01  -0.101971  -0.233931  -0.299713    1.069099  0.136501   
2020-09-01   0.084289  -0.101971  -0.233931    0.463861 -0.157126   

            synthetic2_noise  synthetic2_deseas  
date                                             
1980-10-01          0.178656           0.121771  
1980-11-01          0.338606           0.420622  
1980-12-01          0.363002           0.654605  
1981-01-01          0.750616           1.199845  
1981-02-01         -0.323290           0.490922  
...                      ...                ...  
2020-05-01          0.536813           0.701929  
2020-06-01          0.679631           1.165452  
2020-07-01         -0.441069           0.368543  
2020-08-01          0.027794           0.306072  
2020-09-01          0.304888           0.527532  

[480 rows x 13 columns]
```

```python
### this synthetic time series (noise + AR relationship) looks similar to our original deseasonalized data
plt.plot(shasta['deseas'])
plt.plot(shasta['synthetic2_deseas'])

```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb60884e630>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### next step is to reseasonalize by converting from monthly z-scores back to log-scale data
shasta['synthetic2_log'] = shasta['synthetic2_deseas'].copy()
for i in range(1, 13):
    mu = monthly_mean_log[i]
    sigma = monthly_std_log[i]
    shasta['synthetic2_log'].loc[shasta['month'] == i] = shasta['synthetic2_log'].loc[shasta['month'] == i] * sigma + mu
    
plt.plot(shasta['log'])
plt.plot(shasta['synthetic2_log'])
```

_output:_
```
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
/home/andrew/.local/lib/python3.6/site-packages/pandas/core/indexing.py:670: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  iloc._setitem_with_indexer(indexer, value)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb608a02b70>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### lastly, we take the exp to convert from log scale back to inflows in AF
shasta['synthetic2_inflow'] = np.exp(shasta['synthetic2_log'])
```

```python
### plot original data vs synthetic1 vs synthetic2
plt.figure()
plt.plot(shasta['inflow'], color='k', label='historic')
plt.plot(shasta['synthetic1_inflow'], color='royalblue', label='synth1')
plt.plot(shasta['synthetic2_inflow'], color='firebrick', label='synth2')
plt.legend()

plt.figure()
plt.plot(shasta['inflow'].iloc[60:120], color='k', label='historic')
plt.plot(shasta['synthetic1_inflow'].iloc[60:120], color='royalblue', label='synth1')
plt.plot(shasta['synthetic2_inflow'].iloc[60:120], color='firebrick', label='synth2')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7fb6086fc7b8>
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
### look at monthly statistics (log space)
monthly_mean_synthetic2 = shasta.groupby('month').mean()['synthetic2_inflow']
monthly_std_synthetic2 = shasta.groupby('month').std()['synthetic2_inflow']

plt.plot(monthly_mean, color='k', label='historic')
plt.plot(monthly_mean + monthly_std, color='k', ls=':')
plt.plot(monthly_mean - monthly_std, color='k', ls=':')

plt.plot(monthly_mean_synthetic1, color='royalblue', label='synth1')
plt.plot(monthly_mean_synthetic1 + monthly_std_synthetic1, color='royalblue', ls=':')
plt.plot(monthly_mean_synthetic1 - monthly_std_synthetic1, color='royalblue', ls=':')

plt.plot(monthly_mean_synthetic2, color='firebrick', label='synth2')
plt.plot(monthly_mean_synthetic2 + monthly_std_synthetic2, color='firebrick', ls=':')
plt.plot(monthly_mean_synthetic2 - monthly_std_synthetic2, color='firebrick', ls=':')

plt.xlabel('month')
plt.ylabel('inflow (AF)')
plt.legend()
```

_result:_
```
<matplotlib.legend.Legend at 0x7fb6085ea9e8>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### Now what can we do with this? Run it through (very simplified) Shasta Reservoir!
storage_max = 4.5e6    ## max storage at shasta is ~4.5 million AF
storage_tmin1 = 2.25e6   ## let's assume it starts half full
inflow = list(shasta['inflow'])   ## inflow in AF/month
demand = shasta['inflow'].mean() * 0.8  ## assume demand is 80% of average inflow

### function for releases based on demand and max storage capacity
def get_release_storage(storage_tmin1, storage_max, inflow, demand):
    release = demand
    storage_t = storage_tmin1 + inflow - release
    if storage_t < 0:
        release += storage_t
        storage_t = 0
    elif storage_t > storage_max:
        release += (storage_t - storage_max)
        storage_t = storage_max
    return release, storage_t

release_1, storage_1 = get_release_storage(storage_tmin1, storage_max, inflow[0], demand)
release_1, storage_1
```

_result:_
```
(37536.04, 2230503.96)
```

```python
### run through simulation & store results in pandas
shasta['release'] = -1.
shasta['storage'] = -1.

for t in range(nrow):
    release, storage_t = get_release_storage(storage_tmin1, storage_max, inflow[t], demand)    
    shasta['release'].iloc[t] = release
    shasta['storage'].iloc[t] = storage_t
    storage_tmin1 = storage_t

shasta

plt.figure()
plt.plot(shasta['release'])

plt.figure()
plt.plot(shasta['storage'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb608518400>]
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
### repeat for synthetic data
storage_max = 4.5e6    ## max storage at shasta is ~4.5 million AF
storage_tmin1 = 2.25e6   ## let's assume it starts half full
inflow = list(shasta['synthetic2_inflow'])   ## inflow in AF/month
demand = shasta['inflow'].mean() * 0.8  ## assume demand is 80% of average (historical) inflow

shasta['synthetic2_release'] = -1.
shasta['synthetic2_storage'] = -1.

for t in range(nrow):
    release, storage_t = get_release_storage(storage_tmin1, storage_max, inflow[t], demand)    
    shasta['synthetic2_release'].iloc[t] = release
    shasta['synthetic2_storage'].iloc[t] = storage_t
    storage_tmin1 = storage_t

plt.figure()
plt.plot(shasta['synthetic2_release'])

plt.figure()
plt.plot(shasta['synthetic2_storage'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb6085c9d68>]
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
### what if demand is expected to grow by 0.1%/month?
### repeat for synthetic data
storage_max = 4.5e6    ## max storage at shasta is ~4.5 million AF
storage_tmin1 = 2.25e6   ## let's assume it starts half full
inflow = list(shasta['synthetic2_inflow'])   ## inflow in AF/month

demand_0 = shasta['inflow'].mean() * 0.8  ## assume demand is 80% of average (historical) inflow at start
demand = [demand_0 * (1.001)**t for t in range(nrow)]
# demand
```

```python
shasta['synthetic2_release'] = -1.
shasta['synthetic2_storage'] = -1.

for t in range(nrow):
    release, storage_t = get_release_storage(storage_tmin1, storage_max, inflow[t], demand[t])    
    shasta['synthetic2_release'].iloc[t] = release
    shasta['synthetic2_storage'].iloc[t] = storage_t
    storage_tmin1 = storage_t

plt.figure()
plt.plot(shasta['synthetic2_release'])

plt.figure()
plt.plot(shasta['synthetic2_storage'])
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb60857f8d0>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

***In your homework***, you will see how to combine time series analysis with Monte Carlo simulation from last week. This will involve repeated sampling of 20-year time series, and then probabilistic analysis of metrics of interest from the simulation. 

For now, let's generate 10,000 different synthetic inflow scenarios, each of which is 20 years (240 months) long. We will store the final synthetic inflows in a 10,000x240 NumPy array. We want to use NumPy arrays rather than Pandas for all synthetic generation steps (e.g. white noise, deseasonalized residual, etc), since this is significantly faster and simpler when dealing with a lot of repitition.

```python
## variables for sythetic data
nyear = 20
nmonth = nyear * 12
nsim = 10000

## first, generate synthetic normally distributed data:
noise = norm.rvs(shasta['ar_resid'].mean(), shasta['ar_resid'].std(), size=(nsim, nmonth))

print(noise.shape)
print(noise)
```

_output:_
```
(10000, 240)
[[ 0.58780411 -1.72563719 -0.10635834 ... -0.57030258  0.63904325
   0.28372727]
 [ 0.02539586  0.69151012  0.3505246  ... -0.68341048  0.11217919
  -1.49344143]
 [-2.42999786  0.12961479 -0.37177003 ...  0.4280387   0.15804027
  -1.50793818]
 ...
 [ 1.15189798 -0.23668158 -0.13849252 ...  0.78081952  0.73628996
  -0.92320619]
 [-1.89791799  0.23785564 -0.73786243 ... -0.03576285  0.75790621
  -1.19363385]
 [-0.09153109 -0.26897751  0.62093091 ... -0.63924938  0.60399939
   0.51170247]]
```

```python
### now apply the AR relationship. here is a function to apply regression prediction
def predict_ar(lag1, lag12):
    return lm_log_ar_fit.params[0] + lm_log_ar_fit.params[1] * lag1 + lm_log_ar_fit.params[2] * lag12

### We need 12 years of lagged data to start, we can use the last 12 years of real data
max_lag = 12
deseas = np.zeros((nsim, nmonth+max_lag))
deseas[:, :max_lag] = list(shasta['ar_resid'].iloc[-max_lag:])
### now add prediction plus noise to get AR time series
for i in range(nmonth):
    lag12 = deseas[:, i]
    lag1 = deseas[:, i + max_lag - 1]
    prediction = predict_ar(lag1, lag12)
    deseas[:, i + max_lag] = prediction + noise[:, i]

deseas = deseas[:, max_lag:]
    
print(deseas.shape)
print(deseas)
```

_output:_
```
(10000, 240)
[[ 0.48066059 -1.39744982 -1.05350027 ... -1.22315472 -0.19123686
   0.16682274]
 [-0.08174767  0.63515557  0.79315951 ... -1.01923235 -0.59518547
  -1.89879283]
 [-2.53714138 -1.60559454 -1.46122915 ...  1.20682979  0.99414858
  -0.83695819]
 ...
 [ 1.04475446  0.47720022  0.19614175 ...  0.99363978  1.41989266
   0.0558683 ]
 [-2.00506151 -1.13354856 -1.50456409 ... -0.57255909  0.38922983
  -0.9281568 ]
 [-0.19867461 -0.40527987  0.35217684 ... -1.30107569 -0.2819441
   0.31970319]]
```

```python
## now reseasonalize using the monthly means and stds, to get to log-scale inflows
month = [t % 12 + 1 for t in range(nmonth)]
log = deseas.copy()
for i in range(nmonth):
    mu = monthly_mean_log[month[i]]
    sigma = monthly_std_log[month[i]]
    log[:, i] = log[:, i] * sigma + mu
print(log.shape)
print(log)
```

_output:_
```
(10000, 240)
[[11.25372659  9.91702266 10.55543831 ...  9.57099761 10.03343038
  10.7559759 ]
 [10.80598674 11.55833498 11.82024911 ...  9.63104538  9.85923221
   9.18355845]
 [ 8.85121882  9.74894749 10.2761774  ... 10.28654033 10.54461418
   9.99186341]
 ...
 [11.70280837 11.43078732 11.41134081 ... 10.22376356 10.72821139
  10.67151357]
 [ 9.27481388 10.13012078 10.24649652 ...  9.76257454 10.28374994
   9.9224399 ]
 [10.71289982 10.71819182 11.51821207 ...  9.54805269  9.99431393
  10.87235374]]
```

```python
### lastly, exponentiate to get back to original scale (AF/month)
synth_inflow = np.exp(log)

print(synth_inflow.shape)
print(synth_inflow)
```

_output:_
```
(10000, 240)
[[ 77166.95385576  20272.54237638  38385.62478938 ...  14342.71758198
   22775.26557165  46909.51890486]
 [ 49315.15598237 104645.63113661 135978.09768384 ...  15230.34935767
   19134.19269448   9735.73530897]
 [  6982.89465186  17136.18327035  29032.68086153 ...  29335.10870053
   37972.37405291  21847.97259981]
 ...
 [120910.8012063   92114.46942355  90340.4695791  ...  27550.15840527
   45625.01380929  43110.14237269]
 [ 10665.97323441  25087.394179    28183.62786329 ...  17371.29716678
   29253.3665509   20382.66160589]
 [ 44931.74396912  45170.15335397 100530.06066114 ...  14017.37195115
   21901.57717992  52699.10449791]]
```

```python
### plot next to original data to make sure it looks ok
for s in range(10):
    plt.plot(synth_inflow[s, :], alpha=0.3)
plt.plot(shasta['inflow'].iloc[:nmonth].values, color='k', lw=2)
```

_result:_
```
[<matplotlib.lines.Line2D at 0x7fb608751080>]
```

_result:_
```
<Figure size 432x288 with 1 Axes>
```

```python
### save data for homework
np.savetxt('synth_inflow.csv', synth_inflow, delimiter=',')
```

**This has been a very brief intro to the large field of time series analysis**. Here are some other interesting concepts that you can explore on your own if you are so inclined. Email me if you'd like a list of references.
1. Auto-regressive moving average (ARMA) models add correlated error terms to an AR model, which can help create more sustained devations from "normal" behavior
1. Auto-regressive integrated moving average (ARIMA) models add an "integration" term which accounts for linear trends
1. ARIMAX models add exogenous predictor variables (X) to an ARIMA model. For example maybe you want to provide an el nino-southern oscillation (ENSO) signal that effects inflows.
1. Fourier analysis is an alternative to manual deseasonalization, by breaking down the signal into harmonic waves
1. Wavelet analysis is a more "fuzzy" version of Fourier analysis, which allows for quasi-harmonic signals (e.g., ENSO)
1. Multivariate synthetic time series with copulas, vector auto-regression, and other methods
2. Semiparametric sampling for finer-scale structure that is hard to capture with parametric methods (e.g., daily streamflow is much more irregular than monthly streamflow).
1. Hidden Markov Models are another cool alternative, which allows for random transitions between different "regimes" (e.g., wet period vs dry period), and then different probability distributions for streamflow within each regime
