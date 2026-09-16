---
title: "Timeseries Analysis - Optimizing Model Parameters"
unit_id: 107
course_id: 4
level: "Expert"
slug: timeseries-analysis-optimizing
is_course: 0
---

# Timeseries Analysis - Optimizing Model Parameters

## Extracted resources (local files)

### Flowchart
*Source file:* `flow chart.pptx`  ·  *type:* file

_[no extractable text]_

### Optimization of Daily Streamflow Forecasting Model
*Source file:* `Optimization_of_Daily_Streamflow_Forecasting_Model.pdf`  ·  *type:* file

FAIR CLIMATE AND WATER SCIENCE  
Module 2: Data Processing (DP) for Water Science 
Optimization of Daily Streamflow Forecasting Model 
Prepared by Pin-Ching Li, Sayan Dey and Venkatesh Merwade 
Lyles School of Civil Engineering, Purdue University 
vmerwade@purdue.edu 
1. INTRODUCTION 
Accurate streamflow forecasting is a real-world analytic challenge in hydrology and 
hydraulics. The behavior of streamflow time series is described in streamflow 
forecasting model with parameters and variables. These parameters could be different 
based on different scenarios and datasets. An optimization method is necessary for 
shooting the optimal parameters with provided datasets.  
The flowchart of optimizing a streamflow forecasting model is shown below. This 
whole process is divided into three tutorials. This tutorial is the second tutorial in the 
scenario. Students would learn how to optimize a streamflow forecasting model: Holt-
Winters’ model through training and validation process. Holt-Winters’ seasonal method 
is known as triple exponential smoothing model, which contains components for 
smoothing, capturing trend, and seasonality in a dataset. The prediction of fine-tuned 
model is evaluated by the test set with loss function: Mean Squared Error (MSE).

2. COMPUTER AND DATA REQUIREMENTS 
A web browser is required for this tutorial with good internet connection and login 
credentials for an account on www.mygeohub.org. For this exercise, a Jupyter notebook 
file, optimization_forecasting_exercise.ipynb, is provided to you. It has code for 
downloading USGS streamflow dataset by hydrofunctions, and a class for Holt-Winters’ 
model. This script is adapted from the original script developed by Sergeev (2018).  
3. GET AND PLOT DATA 
Write code using hydrofunctions library to get daily streamflow data for station 
03335500 from 01/01/2019 to 06/30/2019 and plot the hydrograph. 
4. HOLT-WINTER’S EXPONENTIAL MODEL(HWEM) 
This code is provided to you and is explained below. Holt-Winter’s model is a triple 
exponential smoothing equation which is a linear combination of three components: 
the value of dataset 
tl , trend 
tb , and seasonal component 
ts with corresponding 
parameters: , , and . The Holt-Winters equation is shown below. Details of 
Holt-Winter’s class are elaborated in the appendix. 
𝑦̂𝑡+𝑚= 𝑙𝑡+ 𝑚𝑏𝑡+ 𝑠𝑡−𝐿+1+(𝑚−1) 𝑚𝑜𝑑𝐿      −(1) 
𝑙𝑡= 𝛼(𝑦𝑡−𝑠𝑡−𝐿) + (1 −𝛼)(𝑙𝑡−1 + 𝑏𝑡−1) −(2) 
𝑏𝑡= 𝛽(𝑙𝑡−𝑙𝑡−1) + (1 −𝛽)𝑏𝑡−1                 −(3) 
𝑠𝑡= 𝛾(𝑦𝑡−𝑙𝑡) + (1 −𝛾)𝑠𝑡−𝐿                      −(4) 
L is the seasonal index; m is the trend index.  
5. OPTIMIZATION OF HWEM 
To optimize Holt-Winter’s model, the streamflow dataset is divided into three sets: 
training, validation and test set, where the training and validation set are used to 
optimize the model (training process) and the test set is kept for final evaluation (testing 
process). The accuracy of the final evaluation is a firm indication of how well the model 
performs.  
In training process, our model is constructed with the training set. The prediction made 
by current model is compared by the validation set. Based on the evaluation provided 
by validation set, the parameters in current model is updated. Until the error converges, 
the training process would stop and return the current parameters. The optimal model 
with minimum error is found.

5.1 Create a function compute prediction error 
Mean square error (MSE) is the loss function for evaluation of the Holt-Winter’s model. 
Split the input series into training and validation set with the given validation data size. 
Forecast the streamflow by Holt-Winter’s model with training set. The result of 
forecasting is evaluated by the validation set to get the error of the overall prediction. 
This error is returned as the score of the model with current parameters. The code below 
just gives you a skeleton of what is needed. Use this to complete the function to return 
MSE in each training process. 
 
5.2 Main Code to minimize the mean_squared_error 
Minimize() function in scipy.optimize is a function to minimize the objective function 
using optimization algorithm chosen by user. The optimization algorithm is similar to 
what you’ve heard before, such as gradient descent and Newton method. In this tutorial, 
Truncated Newton conjugate gradient “TNC” is chosen as the algorithm to minimize 
the error obtain from objective function created in last step. The parameters of Holt-
Winter’s model range from zero to one. 
Most of the code is provided to you. Fill out the blanks or dashed lines to complete it.  
Original Dataset 
Training Process 
Testing Process

You will get the result: 
 
5.3 Report the error of training and test process 
Fill the blank in the following code to get the errors. 
 
 
Plot the result of prediction and observation. 
 
Homework- Forecast streamflow of the USGS streamflow gage for station 08158000 
by using six months of 2018 data with Holt-Winters model and first order exponential 
smoothing model. Optimize the model and report the errors and their final parameters.

Using the optimized parameters, predict the flows for next one month. Plot the 
predicted hydrograph. 
6. APPENDIX: HWEM CLASS 
HWEM class is built as the code from Sergeev (2018). Python Class serves as a user-
defined blueprint for bundling attributes of object and functions together. The method 
__init__(self, arguments) in a class is a constructor used to initialize an instance (“self”) 
in HoltWinters class. The attributes of “self” are streamflow dataset (series), the length 
of seasonality (slen), the parameters of Holt-Winters’ model (alpha, beta, gamma), and 
the prediction horizon (n_preds). 
 
After the “self” instance is initialized, some functions are created for the initial value 
of trend and seasonality. The level term need only last step observation which could be 
satisfied by applying observation in t =0 as an initial value. However, the initial trend 
and seasonality trace more steps back so that we could only provide the average value 
of trend and seasonality as the guess of initial value. 
Trend value is defined as the trend behavior within the length of season in our model. 
The initial_trend function is defined for dealing with the boundary value b0 in equation 
(3). Trend values are calculated through the entire season by dividing the difference 
between the start and the end with the length of seasonality. The initial trend value is 
obtained by averaging the trend values we have for a whole season. 
 
The initial_seasonal_components function is defined for dealing with the initial value 
from s0-L to s0 in eq. (4). The average of differences between seasonally averaged value 
of observation and observation within a season is taken as the seasonality (seasonal 
variation of streamflow). The initial value of seasonality is the average value of seasonal 
variation in every season.

The prediction of model is done within the function of triple_exponential_smoothing(). 
The smoothing process is explicit (forward). In the first step (i = 0), there is no need for 
prediction. The observation value is taken as the result. Initial level value l0, Trend value 
b0, and seasonality s0 (remainder would be zero because i is zero) is appended to the list.  
𝑦̂𝑡+𝑚= 𝑙𝑡+ 𝑚𝑏𝑡+ 𝑠𝑡−𝐿+1+(𝑚−1) 𝑚𝑜𝑑𝐿      −(1) 
𝑙𝑡= 𝛼(𝑦𝑡−𝑠𝑡−𝐿) + (1 −𝛼)(𝑙𝑡−1 + 𝑏𝑡−1) −(2) 
𝑏𝑡= 𝛽(𝑙𝑡−𝑙𝑡−1) + (1 −𝛽)𝑏𝑡−1                 −(3) 
𝑠𝑡= 𝛾(𝑦𝑡−𝑙𝑡) + (1 −𝛾)𝑠𝑡−𝐿                      −(4) 
 
The result is appended with the 𝑦̂𝑡+𝑚 value obtained from the eq. (1). When doing the 
prediction, the formula of level lt is changed as eq (2*). lt is not based on an observation 
𝑦𝑡, yet the previous prediction 𝑦𝑡̂ is applied. At the same spot, 𝑠𝑡 is obtained based 
on eq (4*) instead. Therefore, the uncertainty increases because the prediction is made 
with the previous prediction rather than an observation. 
𝑙𝑡= 𝛼(𝑦𝑡̂ −𝑠𝑡−𝐿) + (1 −𝛼)(𝑙𝑡−1 + 𝑏𝑡−1) −(2 ∗) 
𝑠𝑡= 𝛾(𝑦𝑡̂ −𝑙𝑡) + (1 −𝛾)𝑠𝑡−𝐿                      −(4 ∗)

Reference: 
1. Sergeev, D. (2018). Open Machine Learning Course. Topic 9. Part 1. Time series 
analysis in Python. https://medium.com/open-machine-learning-course/open-
machine-learning-course-topic-9-time-series-analysis-in-python-a270cb05e0b3. 
Accessed 17 Feb 2020

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP4/Coursepage_DP4_optimization_forecasting_exercise.ipynb

```python
class HoltWinters:
    """
    Holt-Winters model
    # series - initial time series
    # slen - length of a season
    # alpha, beta, gamma - Holt-Winters model coefficients
    # n_preds - predictions 
    """   
    def __init__(self, series, slen, alpha, beta, gamma, n_preds):
        self.series = series
        self.slen = slen
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.n_preds = n_preds
        
    def initial_trend(self):
        sum = 0.0
        for i in range(self.slen):
            sum += float(self.series[i+self.slen] - self.series[i]) / self.slen
        return sum / self.slen  
    
    def initial_seasonal_components(self):
        seasonals = {}
        season_averages = []
        n_seasons = int(len(self.series)/self.slen)
        # let's calculate season averages
        for j in range(n_seasons):
            # seasonal mean of streamflow
            season_averages.append(sum(self.series[self.slen*j:self.slen*(j+1)])/float(self.slen))
        # let's calculate initial values
        for i in range(self.slen):
            sum_of_vals_over_avg = 0.0
            for j in range(n_seasons):
                sum_of_vals_over_avg += self.series[self.slen*j+i]-season_averages[j]
            seasonals[i] = sum_of_vals_over_avg/n_seasons
        return seasonals   
    def triple_exponential_smoothing(self):
        self.result = []
        self.Smooth = []
        self.Season = []
        self.Trend = []
        seasonals = self.initial_seasonal_components()        
        for i in range(len(self.series)+self.n_preds):
            if i == 0: # components initialization
                smooth = self.series[0]
                trend = self.initial_trend()
                self.result.append(self.series[0])
                self.Smooth.append(smooth)
                self.Trend.append(trend)
                self.Season.append(seasonals[i%self.slen])                
                continue                
            if i >= len(self.series): # predicting
                m = i - len(self.series) + 1
                val = self.result[i-1]
                last_smooth, smooth = smooth, self.alpha*(val-seasonals[i%self.slen]) + (1-self.alpha)*(smooth+trend)
                trend = self.beta * (smooth-last_smooth) + (1-self.beta)*trend
                seasonals[i%self.slen] = self.gamma*(val-smooth) + (1-self.gamma)*seasonals[i%self.slen]
                self.result.append((smooth + m*trend) + seasonals[i%self.slen])                
                # when predicting we increase uncertainty on each step
            else:
                val = self.series[i-1]
                last_smooth, smooth = smooth, self.alpha*(val-seasonals[i%self.slen]) + (1-self.alpha)*(smooth+trend)
                trend = self.beta * (smooth-last_smooth) + (1-self.beta)*trend
                seasonals[i%self.slen] = self.gamma*(val-smooth) + (1-self.gamma)*seasonals[i%self.slen]
                self.result.append(smooth+trend+seasonals[i%self.slen])                
            self.Smooth.append(smooth)
            self.Trend.append(trend)
            self.Season.append(seasonals[i%self.slen])
```

```python
from sklearn.metrics import mean_squared_error
def Train_Score(params, series, slen, validsize, loss_function=mean_squared_error):
    """
        Returns error         
        param   - parameter for optimization
        series   - timeseries dataset
        validsize- size of validation dataset
    """
    values = series.values
    alpha, beta, gamma = params
    
    training_dataset =
    validation_dataset = 
    model_result = 
    error = loss_function(...,...)
    return error
```

```python
%%time
#print CPU times and Wall time
from scipy.optimize import minimize     #for optimization

# prediction horizon is the same as the size of test dataset and validation dataset
predicts = 5
# split dataset into (training+validation) and test dataset
datatrain = ...
# initializing model parameters alpha, beta and gamma
x_iguess = [0.7, 0.1, 0.3] 
# season length is assumed to be 13 days
slength  = 13

# Minimizing the value of loss function
opt = minimize(...)

# take optimal values
alpha_final, beta_final, gamma_final = opt.x
print('alpha', 'beta ', 'gamma')
print("{:.3f}".format(alpha_final), "{:.3f}".format(beta_final),"{:.3f}".format(gamma_final))

# forecasting for the next (predicts) days with optimal parameters
model = HoltWinters(...)
model.triple_exponential_smoothing()
```

```python
# Report the error
MSE_train = Train_Score(...)
print('MSE of training Process:')
print("{:.2f}".format(MSE_train))
MSE_test = mean_squared_error(...)
print('MSE of testing Process:')
print("{:.2f}".format(MSE_test))
```

```python
# Plot the result
plt.plot(Time, Daily.discharge)
plt.plot(Time,model.result)
ax.set(xlabel='Date', 
       ylabel='Discharge Value (cfs)',
       title='Wabash River at Lafayette Station 2019');
plt.show()
```
