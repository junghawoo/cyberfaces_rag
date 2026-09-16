---
title: "Time Series forecasting 101"
unit_id: 250
course_id: 0
level: "Expert"
slug: time-series-forecasting-101-
is_course: 0
objectives:
  - "Learning this module enables users to preprocess raw data and do the time series forecasting"
---

# Time Series forecasting 101

**Description:** It explores Machine Learning to analyze and forecast time series data in high-performance computing environments. Next course is to use Deep Learning for time series forecasting.

## Extracted resources (local files)

### Time_Series_101
*Source file:* `Time_Series_101.pdf`  ·  *type:* file

Time Series 
Forecasting 
- 101

WHAT IS A TIME SERIES?
•A time series is a series of data points indexed in time order. Most commonly, a time series is a sequence taken at successive equally spaced points in time.
•TS data are collected and used in every type of businesses.
•Example of time series:
•Monthly salesHourly stock closing pricesQuarterly unemployment rateAnnual GDPDaily airline filled seats

OUR DATASET
•Number of miles travelled by air, rail
and 
road since 1990 January
•Type of data 
– monthly

Pre
-processing steps
Remember, time
-series data must have:
an index with equal increments.
must be of datetime type, when working with Python
Daterange
is a pandas
function that
is handy in
redefining time 
series
indexes.
Check
pandas.date_range — pandas 1.5.3 documentation (pydata.org)
Here, we perform the following:

Time series components
A time series can 
be decomposed 
into the following 
components:
Level 
– the mean of all points

SIMPLE LINEAR REGRESSION
FOR TIME SERIES
•Target variable – y(t)​
•Predictor – indexed 
t ​(1,2,3....t)
•Y(t) is expected to 
function the trendline​
•Evaluation of 
predictors, 
model like traditional 
linear regression​
•Con – Does not 
capture seasonality

MULTIPLE LINEAR REGRESSION
FOR TIME SERIES
•Target – y(t)​
•Predictors – indexed t, seasons 
(dummied), sometimes other 
exogenous variables.​
•
Exogenous variables are 
independent predictors.
•
For example, if we 
use number of bananas sold 
at time t-1 
to predict number of apples 
at time t, number of 
bananas becomes an 
exogenous variable​
•Captures seasonality
2 – 12 Represent seasons taking binary values (0 or 1).

INTRODUCTION TO ACF AND PACF
Lags are time series n times removed. For
example, lag 1 (y(t
-
1)) for a time series
1,2,3,4 would be
NaN
, 1, 2 , 3

ACF
AC 
– Auto correlation, as its name suggests,
represents 
correlation between lags. For
example, it represents the 
correlation of the
time series with itself in a way.
The ACF 
– autocorrelation
function is a 
visual representation of the table above

PACF
• Suppose the variable y(t) is correlated to both
y(t
- 1) and y(t
- 2) 
(lag 1 and lag 2 series). This
would mean that y(t
- 1) and y(t
- 2) 
would also
be correlated. What if we want to know the
true 
effect of y(t
-2) on y(t), removing its
relationship with y(t
- 1)?
• The PACF does exactly that! It indicates the
"true correlation" 
between a series and its n
- lag.

STATIONARITY
•A time series is said to be stationary if the statistical properties such as
mean, variance, and auto
-
correlation do not change over time.
• ADF (Augmented Dickey-Fuller) test is a statistical 
significance test which means the test will give results 
in hypothesis tests with null and alternative hypotheses. As 
a result, we will have a p-value from which we will need 
to make inferences about the time series, whether it is 
stationary or not.

AUTO
-REGRESSIVE
MODEL
• The AR model, as its name suggests, is a
regression model 
with significant
lags acting as
predictors of y(t).
• The conditions to fit an AR model are:
• The time series should be stationary. If not, it
should be 
differences and made
stationary
• The lag variables should be significant. The
number of lags to 
be included in the model is
picked using the
PACF
• ACFs whose lags' significance reduces
geometrically indicate 
that a time series is good
to model with the AR model.

AR MODEL
EXAMPLE
• Consider the railways data's original series, and
its 
differenced plot.
•
Performing the ADF test on the differenced data
• Visualizing the
acf
and
pacf of the differenced
data
• There is no geometric decrease of lag
-significance in the ACF. 
This is enough to
assume that we won't get a great AR model

AR MODEL 
– MODELLING 
AND PERFORMANCE
•Not all variables are significant
•Performance of the model not that great
as expected

ARIMA
•ARIMA is a combination of the AR and MA model.
•The MA (moving average) model
is a category of models that attempts to
reduce 
the prediction errors by
taking the error of the previous
time index as an input.
•The AR model has already been covered
• The ARIMA model takes in 3
hyperparameters 
– ( p,d,q
)
• P is the
number of significant lags
as seen in the PACF. This is for the AR part
•D is the order of differencing required to make the series stationary
• Q is the number of significant lags as seen in the ACF. This is for the MA part

ARIMA example
•Let us model the same time series and see if we get improved results
•Since both ACF and PACF show 4 significant lags after differencing of 1 to make the series stationary,
we set (
p,d,q
) 
to (4,1,4)
•Note that ideally, the ACF and/or PACF would show a geometric trend
•Observe how the model fails in the validation part. It fails to capture the seasonality.

SARIMA
•SARIMA stands for seasonal ARIMA. ARIMA fails to capture seasonality by itself. So, we add a seasonal component.
• Y(t) =
ay(t
- 1)+by(t
- 2)….+
s1y(t
- 12) ….beta+error
•Along with the (p,d,q) we also need to tune the seasonal order 
-
(P,D,Q,S). For this we observe the signifiance of the lags at a seasonal level. For example, if the frequency of the data is 12 (12 months in a year), we observe what the ACF and PACF say about lag 12.

SARIMA example
•Again, let us attempt to improve our results on the rail time series
•In SARIMA, when the frequency is 12, differencing by 12 is equivalent to seasonal differencing by 1.
•ACF and PACF both show significant lag
- 12
•Setting seasonal order to (1,1,1,12)

SARIMA example
Though not all the features are significant, observe how the results improved

Smoothing Methods
•Smoothing methods are involve averaging out past and present observations to get a ball
-park forecast. 
Hence, 'smoothing'.
•The simplest smoothing method would just be averaging out, let us say, the previous 5 observation. 1,2,3,2,2 in the past points would yield a prediction 
of 10/5 = 2
•There are variations of smoothing:
•Simple
Exponential Smoothing
•Double Exponential Smoothing
• Holt
-Winter's Smoothing

Simple Exponential Smoothing
•Form of weighted average where recent observations are given highest weights
•Larger the value of T, lesser is (1
- alpha)^T
•Alpha is the learning rate, which is defined by the user.

Double Exponential Smoothing
• Simple Exponential does not account for trend and yields flat forecasts.
• Double exponential smoothing
factors in a trend 
component
• The Lt equation means that the level at time t is a weighted average of the actual value at time t and the level in the previous period, adjusted for trend
• The Tt equation means that the trend at time t is a weighted average of the trend in the previous period and the more recent information on the change in level.3

Triple (Holt
-Winter's) Exponential Smoothing
• Holt
-Winter's smoothing factors in level, trend, and seasonality.
• The trend
equation now 
includes
adjustment for 
seasonality
• The seasonality equation is added to the forecast function

Additive vs Multiplicative Trend/Seasonality
•Additive means linear (straight line), and multiplicative means there are changes to widths or heights of periods over time (percentage increase).

WHAT NEXT?
• Auto ARIMA
• Complex time
-series data
•Deep Learning models for Time
- series

APPENDIX 
- EQUATIONS
• Simple linear regression 
- Y(t) = beta0 + beta1*t
• Multiple Linear Regression - beta0 + 
beta1*t + beta2*season1.....beta13*season12
• AR Model -Y(t) =
ay(t
- 1)+by(t
- 2)….+
beta+error
• MA Model 
- Y(t) =
beta + ay(t
- 1)+be(t
- 1) + error
• Simple Exponential smoothing
-
• Double Exponential Smoothing
• Triple Exponential Smoothing

## Fetched resources (external URLs)

### Jupyter Notebook for Time Series forecasting (notebook)
*URL:* https://github.com/junghawoo/TimeSeriesForecasting101.git

[github: could not resolve raw content]

### Lecture Video for Time Series forecasting 101 (link)
*URL:* https://cdnapisec.kaltura.com/p/983291/sp/98329100/embedIframeJs/uiconf_id/29134031/partner_id/983291?iframeembed=true&playerId=kaltura_player&entry_id=1_jm27alsp&flashvars[streamerType]=auto&flashvars[localizationCode]=en&flashvars[leadWithHTML5]=true&fl

_[no content]_

### More resources on Time series forecasting (link)
*URL:* https://www.rcac.purdue.edu/training/time-series-forecasting-101

# RCAC            - Time Series Forecasting 101

RCAC            - Time Series Forecasting 101
Fortress Archive Monthly Maintenance
—
July 1, 2026 8:00am - 12:00pm EDT
Anvil Hero
Time Series Forecasting 101
Time Series Forecasting 101 explores Machine Learning and Deep Learning techniques to analyze and forecast time series data in high-performance computing environments. Some familiarity with Machine Learning, Deep Learning, and Python programming is recommended.
Schedule:
The
Events
page will show the next scheduled session.
Prerequisites:
Familiarity with machine learning, deep learning, and python programming.
Lecture Recording:
Materials:
Time Series Forecasting 101 Presentation Slides
(2.18 MB)
Time Series Forecasting 201 Presentation Slides
(1.98 MB)
Exercise Files
(32.22 MB)
