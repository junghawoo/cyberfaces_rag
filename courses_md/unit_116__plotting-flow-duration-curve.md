---
title: "Plotting flow duration curve"
unit_id: 116
course_id: 4
level: "Foundation"
slug: plotting-flow-duration-curve
is_course: 0
---

# Plotting flow duration curve

## Extracted resources (local files)

### Flow duration curve
*Source file:* `flowdurationcurve.pdf`  ·  *type:* file

Data Processing: Flow Duration Curve 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
School of Civil Engineering, Purdue University 
vmerwade@purdue.edu 
 
Spring 2020 
FAIR Science in Water Resources
 
 
Objective 
 
The objective of this tutorial is to plot a flow duration curve using daily discharge data for a USGS 
gaging station. This tutorial creates flow duration curves by computing exceedance probability 
using Weibull (1939) Plotting Position Formula, and plotting them on on linear-linear, log-linear 
and log-probability scale.  
 
Flow Duration Curve 
 
A flow duration curve, shown below, is a plot of streamflow values on y axis and exceedance 
probability on x-axis. The plot represents the percentage of time that flow in a stream is likely to 
be equal or exceed a particular value of interest. 
 
 
 
The exceedance (in our case) or non-exceedanace probability can be calculated as a percentage of 
given flow to be equaled or exceeded using a plotting position formula. This probability indicates 
the chance of occurring an event such as flooding. 
 
Steps for obtaining the flow duration curve 
 
Step 1: Sort the data in descending order

Step 2: Calculate the rank and reversing the rank to give the largest discharge a rank of 1 
Step 3: Calculate exceedance probability (P) using the most common plotting position formula 
given by Weibull (1939) as follows: 
 
 
where 
● P = the probability that a given flow will be equaled or exceeded (% of time 
● M = the ranked position on the listing (dimensionless) 
● n = the number of events for period of record (dimensionless) 
 
Step 4: Plot the FDC in different scale (linear-linear, log-linear and log-probability scale)as shown 
below. 
 
 
Typically, we plot hydrographs using discharge data, but a flow duration curve provides a 
different view of the data. Specifically, it’s shape shows how often and/or how long the 
watershed has a flow that exceeds a certain magnitude. This information can be useful to both 
understand the watershed behavior and/or design an engineering structure. The shape of a 
flow-duration curve at the ends is particularly important to understand watershed’s

hydrology. The high end of the curve describes the high flow characteristics and low end of 
the curve describes the low flow characteristics of a stream. A steep high end curve means the 
watershed has high flows for very short duration, which is a characteristic of a small flashy 
watershed or an urban area. A relatively flat high end curve means that the watershed sustains 
high flows for long duration, which may be a characteristic of a snow-dominated high flow 
area or regulated high flow releases from a reservoir. Similarly, a flatter low end curve means 
the stream is able to sustain low flows throughout the year due to regular baseflow or 
regulated release from a reservoir.  
Data Source 
 
Daily streamflow for any USGS gage can be obtained from the link: 
https://waterdata.usgs.gov/nwis/sw. In this tutorial, you will use hydrofunctions python library to 
download the streamflow data.  
 
Instructions 
1. Upload the notebook, flowdurationcurve.ipynb in your mygeohub account and 
open it.  
2. First, import the packages/modules required for this tutorial. We need the 
following packages: hydrofunctions (hf), pandas (pd), numpy (np), pyplot (plt) 
from matplotlib, stats (sp) from scipy, seaborn and probscale. You will write the 
code to import these functions. 
 
3. Next, you will create a cell that prompts the user to enter the following inputs: (i) 
USGS station code; (ii) start date (YYYY-MM-DD) and (iii) end date (YYYY-MM-
DD) to obtain the data using hydrofunctions. The format for both dates including 
the hyphen must be followed. You will write the code to define these variables and 
assign them values. Use the following names: “USGS_StationCode”, “Start_Date” 
and “End_Date” for storing the station number, start data and end date, 
respectively. Use Wabash River at Lafayette, IN (03335500) for a sample analysis 
period from 2017-01-01 to 2017-05-31 
 
4. Next, use hydrofuctions to get the data. Use any of the two options suggest in the 
notebook. You will write the code to get the data.

5. Next, check the data by printing the first n rows (default: 5). This is helpful for 
quickly testing if your object has the right type of data in it. You will notice that 
the time series is not sorted or rank, which is what we will need for computing the 
exceedance probabilities.  
6. We get the output from the hydrofunctions as "class function". By defining a new 
dataframe, let us store the data into pandas dataframe to do the manipulations. In 
the above data, we have two columns namely Discharge and Qualification Code. 
Let us rename the default column names and drop the qualification code column. 
7. Next, plot the Discharge Hydrograph for the analysis period using pyplot. You 
will have to write the code for this plot. 
 
 
 
8. Now, we have to calculate the exceedance probability using the Weibull (1939) 
plotting position formula. The steps involved in the process are discussed in the

Flow Duration Curve section. You will have to write the code for calculating the 
exceedance probability. 
 
9. You will see that the data are sorted after running the above code. What do you expect 
the first and last element in the exceed_prob list that was generated (is it 0% and 100% or 
100% and 0%, you print the output of exceed_prob to check this)? Are these exceedance 
or non-exceedance probabilities?  
10. Flow duration curve in linear-linear scale: Let us plot the flow duration curve with 
discharge in linear scale and exceedance probability in linear scale. You will have to 
write the code for plotting the FDC in linear-linear scale to get the plot as shown 
below.

11. Let us plot the flow duration curve in with discharge in logarithmic and exceedance 
probability in linear scale. You will have to write the code for plotting the FDC in 
logarithmic-linear scale to get the plot as shown below.

12. Let us change the linear scale of discharge to logarithmic scale for better visualisation at 
the two ends of the probability axis (i.e. extreme values) exceedance probability in 
probability scale (instead of linear scale). 
 
 
 
Ok, you have completed the tutorial! 
 
Turn in (by 04/16/2020) 
 
1. A PDF containing the three plots generated in the tutorial for Cedar Creek (04180000) from 
March 01. 2019 to May 31, 2019. 
a. Discharge Hydrograph 
b. Flow Duration Curve (Linear-Linear Scale) 
c. Flow Duration Curve (Log-Linear Scale) 
d. Flow Duration Curve (Log-Probability Scale) 
2. Plot two flow duration curve for 05551700, one from 1971-1990 and other from 1991-2010. 
Comment on how the flow duration curve has changed or not changed for these two

periods and what may be the reasons for that change or no change. Use Log scale for both 
plots. 
3. Repeat the same exercise as in (2) for 05568800 using time periods 1971-1985 and 1996-
2010. Comment on any changes or no changes in the two curves and possible reasons.

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DV2/flowdurationcurve.ipynb

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Import the packages/modules required for this exercise</span>\n",
    "\n",
    "We need the following packages: hydrofunctions (hf), pandas (pd), numpy (np), pyplot (plt) from matplotlib, stats (sp) from scipy, seaborn and probscale. The paranthesis contains the commonly used short forms for these libraries."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">USGS Station and Analysis Period</span>\n",
    "\n",
    "We need three inputs from the user for carrying out the analysis:\n",
    "<ol type=\"1\">\n",
    "    <span style=\"color:red\"><li> USGS station code</li></span>\n",
    "    <span style=\"color:red\"><li> Analysis start date </li></span>\n",
    "    <span style=\"color:red\"><li> Analysis end date </li></span>\n",
    "    \n",
    "<p style='text-align: justify;'><b><u> Note:</u></b> Both dates value should be entered in YYYY-MM-DD format (including the hyphen symbol). <br>\n",
    "<br>\n",
    "To check whether your code is working correcly, let us use  the USGS gage on Wabash River at Lafayette, IN (<b>03335500</b>) for a sample analysis period from <b>2017-01-01</b> to <b>2017-05-31</b>.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Input the required USGS Station and Analysis Period\n",
    "# WRITE A CODE TO DEFINE VARIABLES FOR STATION NUMBER,START DATE AND END DATE\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Obtain the data using hydrofunction from USGS NWIS</span>\n",
    "\n",
    "One of the two options below may be used to obtain the daily value \"dv\" of the streamflow\n",
    "\n",
    "#### <span style=\"color:red\">Option01</span>\n",
    "<code>data = hf.NWIS(USGS_StationCode,'dv',period='P365D') # P365D indicates past 365 days</code>\n",
    "\n",
    "#### <span style=\"color:red\">Option02</span>\n",
    "This more useful as discharges for desired period can be obtained and let us use this option in this tutorial. <br>\n",
    "<code>data = hf.NWIS(USGS_StationCode, 'dv', Start_Date,End_Date)</code>\n",
    "\n",
    "Finally, run <code>data.get_data()</code> to download the daily data from USGS."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#WRITE THE CODE TO DOWNLOAD DAILY STREAMFLOW FROM USGS USING HYDROFUNCTION\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Data Checking</span>\n",
    "\n",
    "<p style='text-align: justify;'>Now, let us check the data by printing the first n rows (default: 5) using the head statement. This is helpful for quickly testing if your object has the right type of data in it.</p>\n",
    "\n",
    "<u><b>Note:</b></u>\n",
    "    \n",
    "00060 is parameter code for Discharge (cfs)<br>\n",
    "00003 is the stat code for daily mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(data.df().head())\n",
    "print(\"\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Dataframe and Column name change</span>\n",
    "\n",
    "<p style='text-align: justify;'>We get the output from the hydrofunctions as \"class function\". By defining a new dataframe, let us store the data into pandas dataframe to do the manipulations. In the above data, we have two columns namely Discharge and Qualification Code. Let us rename the default column names and drop the qualification code column.</p>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "strflow=pd.DataFrame(data.df())\n",
    "strflow.columns=('Discharge','QC')\n",
    "strflow=strflow.drop(columns='QC')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Discharge hydrograph</span>\n",
    "\n",
    "\n",
    "Now, we will plot the discharge hydrograph for the analysis period."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#WRITE YOUR CODE HERE TO PLOT THE DISCHARGE HYDROGRAPH\n",
    "#ALSO PROVIDE AXIS TITLES WITH UNITS\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Calculation of Exceedance Probability</span>\n",
    "\n",
    "<p style='text-align: justify;'>Now, we have to calculate the exceedance probability using the Weibull (1939) plotting position formula. The steps involved in the process are outlined earlier.</p> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Calculation of exceedance probability\n",
    "# WRITE YOUR CODE HERE\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Flow Duration Curve in linear-linear scale</span>\n",
    "\n",
    "<p style='text-align: justify;'>Let us plot the flow duration curve with discharge in linear scale and exceedance probability in linear scale.</p> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Flow Duration Curve\n",
    "## Discharge in linear-linear scale\n",
    "# WRITE YOUR CODE HERE\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Flow Duration Curve in log-linear scale</span>\n",
    "\n",
    "<p style='text-align: justify;'>Let us plot the flow duration curve in with discharge in logarithmic and exceedance probability in linear scale.</p> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Flow Duration Curve\n",
    "## Discharge in log-linear scale\n",
    "## Variables (prob & flow) calculated above used for plotting\n",
    "# WRITE YOUR CODE HERE\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <span style=\"color:green\">Flow Duration Curve in log-probability scale</span>\n",
    "\n",
    "<p style='text-align: justify;'>Let us change the linear scale of discharge to logarithmic scale for better visualisation at the two ends of the probability axis (i.e. extreme values) exceedance probability in probability scale (instead of linear scale).</p> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Flow Duration Curve\n",
    "## Discharge in log-probability scale\n",
    "## Variables (prob & flow) calculated above used for plotting\n",
    "\n",
    "file_name4='./FDC_Log_Prob'+USGS_Station+'.png'\n",
    "fig, ax = plt.subplots(figsize=(8, 4))\n",
    "\n",
    "ax.plot(exceed_prob,flow)\n",
    "#ax.set_ylim(1e-2, 1e2)\n",
    "ax.set_yscale('log')\n",
    "ax.set_title('Flow Duration Curve for USGS Station: '+ USGS_Station +'\\n (Period:' + Start_Date + ' to ' + End_Date +')\\n[log-probability scale]' )\n",
    "## Add grid lines to both axes\n",
    "plt.grid(which = 'both')\n",
    "plt.xlabel('Exceedance Probability (%) \\n [in probability scale]')\n",
    "plt.ylabel('Discharge (cfs) \\n [in logarithmic scale]')\n",
    "ax.set_xlim(0.5, 99.5)\n",
    "ax.set_xscale('prob')\n",
    "\n",
    "seaborn.despine(fig=fig)\n",
    "plt.tight_layout()\n",
    "plt.savefig(file_name4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "deletable": false
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
    "kernelspec": {
        "display_name": "ct-fair",
        "language": "python",
        "name": "ct-fair"
    },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
