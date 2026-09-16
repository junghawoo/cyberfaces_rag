---
title: "Time Series Forecasting using Deep Learning"
unit_id: 251
course_id: 0
level: "Expert"
slug: time-series-forecasting-using-deep-learning
is_course: 0
objectives:
  - "Learning this module enables users to preprocess raw data and do the time series forecasting with Deep Learning libraries"
---

# Time Series Forecasting using Deep Learning

## Extracted resources (local files)

### Time_Series_201
*Source file:* `Time_Series_201.pdf`  ·  *type:* file

Time Series Forecasting 
- 201

PREVIOUS SESSION
•Simple Linear Regression
•Multiple Linear Regression
•AR models 
– ARIMA, SARIMA
•Smoothing Methods

DATASET
• Number of units sold of different category of items in different Walmart stores situated in different cities, over the past 6 years

WHAT PROBLEM ARE WE GOING TO SOLVE?
States x Categories x Departments x Items
48,000 Time Series
State = CA
Category = Foods
Department = Foods_1
Out of 48,000 different Time Series, we choose the following aggregated Time Series to forecast

WHY DO WE MODEL THE
FOOD
-WISE 
TIME SERIES AND NOT ITEM WISE TIME SERIES?!
Item X Sales
• Naked Eye Test: There is no discernable pattern that a model can capture
• Many inconsistent peaks and falls making it difficult to model

AUTO ARIMA
•Auto ARIMA is simply automated ARIMA 
– the computer 
decides the (
p,d,q ) (P,D,Q) combination
•Helpful when we have several significant lags:

AUTO ARIMA RESULTS
SARIMA Model Summary
• This model uses 5 lags to forecast values
• Mediocre performance, but it
captures some seasonality
• Maybe incorporating recent as well as not
- so
-recent past observations in the predictions, 
would yield better results. 
But using ARIMA for that wouldn't make so much sense!
Test MAPE = 30.37%
Test Set Actual vs Prediction

Deep Learning models for Time Series
Artificial (Deep) Neural Network
Recurrent Neural Network
Long
-Short Term Memory
Convolutional Neural Network
In this tutorial, we focus on ANN and LSTM. LSTM is an improved version of RNN.

Artificial (deep) Neural 
Network
•A neural network (ANN or DNN) can be thought of as a complicated function fitter!

A Simple 
illustration
• Multiple linear functions are combined, passed into a non
-linear activation function 
(a function used to fit non
-linear trends), to 
produce the output
• Major hyperparameters of an ANN 
–
Number of hidden layers, number of neurons in each layer, activation function

HOW DO WE USE AN ANN HERE?
• Feed in the lags of y(t) 
- y(t
- 1), y(t
- 2)…..y(t
- n)
• Decision to make 
-What number of n yields the best results?
•Use exogenous features such as day of the week, month of the year etc.
• Approach is similar to ARIMA/SARIMA, but introducing a non
-linear aspect 
(imagine, a non
-linear form of ARIMA)

PERFORMANCE OF DIFFERENT ANNS ON THE TEST SET

RNN 
– RECURRENT NEURAL NETWORKS
•RNN is an ANN whose architecture has slightly been modified, such that the network "remembers" what happened in the previous iteration. Apart from number of layers, and number of neurons, time
-steps also come 
into play.
• Used in video classification tasks, speech recognition, time
-series data 
etc.

LSTM 
–LONG SHORT TERM MEMORY
•A fancier version of RNNs, the difference being "how much" the network remembers at each time
- step.
• Problem with RNNs 
– a) prone to vanishing/exploding gradients problems and b) 
does it remember too much/too less information?
• Solution 
– input, forget and output gates
•The forget gate determines which relevant information from the prior steps is needed. The input gate decides what relevant information can be added from the current step, and the output gates finalize the next hidden state

UNIVARIATE LSTM
• We feed in only y(t
- 1)...y(t
-n), and no exogenous variables, and try different architectures
Architecture 1 
–
input variables are y(t
- 1) to y(t
-
5), with 50 LSTM units in the first layer
Architecture 2 
– input variables y(t
- 1) 
to y(t
- 30), with 
50 LSTM units in the first layer

MULTIVARIATE LSTM
• Include exogenous variables in the model
• Intuition 
-A regular ANN would consider that today is Christmas,
and wouldn't care if 
yesterday or the day before were Christmas
• But wait 
– if yesterday were Christmas,
and Christmas sales are still on, shouldn't the 
model care about Christmas until perhaps a week or two later?
Input array structure
Architectur
e

SUMMARY
Model
Time Series Intuition
ANN
Behaves like a non
-linear version 
ARIMA! Use this when you want all your input variables to have a direct relationship with the output
RNN
We haven't demonstrated an RNN in this tutorial. RNNs have a permanent memory. All of the information is passed through to the next RNN unit
LSTM
Unlike RNNs, LSTM units do not pass on the entire information into the next unit. Rather, forget and input gates decide what go into the next LSTM unit

MULTIVARIATE LSTM PERFORMANCE
Best MAPE so far!

## Fetched resources (external URLs)

### Jupyter Notebook for Time Series forecasting with Deep Learning (notebook)
*URL:* https://github.com/junghawoo/TimeSeriesForecastingDeepLearning101.git

[github: could not resolve raw content]

### Lecture Video for Time Series forecasting with Deep Learning 101 (link)
*URL:* https://cdnapisec.kaltura.com/html5/html5lib/v2.79.1/mwEmbedFrame.php/p/983291/uiconf_id/29134031/entry_id/1_jm27alsp?wid=_983291&iframeembed=true&playerId=kaltura_player&entry_id=1_jm27alsp&flashvars[streamerType]=auto&flashvars[localizationCode]=en&flas

# Spring 2023 Time Series Forecasting 101

Spring 2023 Time Series Forecasting 101

### More resources on Time series forecasting with Deep Learning (link)
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
