---
title: "Flood frequency analysis and Flow Duration Curve"
unit_id: 104
course_id: 4
level: "Foundation"
slug: flood-frequency
is_course: 0
---

# Flood frequency analysis and Flow Duration Curve

## Extracted resources (local files)

### Calculation of Return Period Flow from Peak Flow Data
*Source file:* `ffareturnperiod_instructions.docx`  ·  *type:* file

Calculation of Return Period Flow from Peak Flow Data 
Prepared by 
Jibin Joseph and Venkatesh Merwade 
 of , 
vmerwade@purdue.edu

FAIR Science in Water Resources
Objective
The main objective of this tutorial is to calculate the return period flow. In general, return period (aka recurrence interval or repeat interval) is an average time or an estimated average time between events such as earthquakes, floods, landslides, droughts, or a river discharge flows to occur. In our case, we will be dealing only with stream flow. Particularly, in this tutorial, we would be calculating flow corresponding to 100, and 500 year return period.  
Data Source
For the manual calculation of return period flow, the annual peak flow data can be obtained from the link: https://waterdata.usgs.gov/nwis/sw. In this tutorial, the code itself obtains the data and performs the calculation. You are not required to get the data manually.
Overview of steps
Obtain peak flow data (raw data containing additional information) from USGS Surface Data Portal. 
Extract the peak flow data required for the calculation.
Calculate the return period peak flow using Gamma Inverse Function.
Instructions
Log on to mygeohub.org and launch Jupyter Notebook with Anaconda 5.1.
Hit on Click Here to go to your Home Directory option to access your home directory. This is the location where you can store your code and data.
It is advisable to create a separate folder to store code and data for this tutorial which makes it accessible in the future. Go ahead and create a folder named Module06 to store the code and data of the current tutorial. 
Click on the notebook file available on the course page. Hit the Save as option available in the File menu and save it in the earlier created folder.
Use the table below to write the eight digit station number and station name assigned to you.
 Fill out the table below:
Now, open the ipynb file (ffa_returnperiod.ipynb). Initially, the book symbol () next to ffa_returnperiod.ipynb would be black color indicating that the code is not running at the moment. Once you open the file, it would turn green color. At some point, if you feel that Notebook is not responding, you can use Restart the kernel() option to terminate the session and then start from the beginning. Also, when you run the cell one-by-one, asterisk sign on the left side of the cell () indicates that the particular cell is running. You have to wait until asterisk sign changes to a number.
The first cell (CELL-01) gives a description about the code and also import the packages/modules required for this tutorial. Execute the first cell using Run ( ) button.
The second cell (CELL-02) contains a definition block which takes the station number and folder name from the main code (from CELL-03). Then, it creates a link and collects the raw data (it is similar Data Access tutorial). Further, it stores the raw and processed data in the Results folder. Also, it returns a list containing the flow data and station name for further steps. Execute the second cell.
The third cell (CELL-03) prompts to input the station number assigned for the tutorial. It executes the definition block and stores the data in the folder. Go ahead and execute the third cell. Now, open the text file with suffix “_reqd”. Note down the starting and ending year which is continuously available within the raw data excluding the gap in data. Then, decide on starting and ending year for the analysis period such that there is atleast 30 years within the continuous data period. Remember that there should not be any break in the analysis period. It is not a good idea to use the data that includes a gap. For example, there is a break in year (no data for 1916-1931) for the data shown below. In this case, starting year of available continuous data period would be 1932. 
Note: In the figure given below, the last date of peak flow is shown as 2011-12-15. The USGS considers the water year from October to September. As the date lies between Oct - 2011 and Sep - 2012, the last date is considered to be in 2012 water year. Hence the last year of data is to be considered as 2012 (not as 2011).
Fill out the table below:
The fourth cell (CELL-04) prompts you to enter the four values obtained in the previous step for carrying out the analysis. This should be properly entered otherwise you will get an error message Error in length of data and check whether it is continuous. Execute CELL-04 and give the years accordingly.
Now, let us write the code in the fifth cell (CELL-05) to perform the calculation for obtaining the final result (return period flow). 
Here, moving window method of 30 years is used with different time steps (1, and 5). The results will stored as in text file in the Results folder. 
You will get a completion message if everything was correct.
Ok, you have completed the tutorial!
Turn-in
Create pdf of flood frequency table for 10, 25, 50, 100, 250 and 500 year. Modify the script to get different files that run the frequency analysis using different time steps for a moving window analysis (1, 5 and 10 year). Each file stores results from one time step, which is reflected in the file name. TS1 (time step1) means the window moves by one year.  In each file, columns 10, 25, 50 etc. represent the values for different return periods. Take the average of each column to get the value for one of the rows in the attached pdf file. You can repeat this process to fill other rows in the table using the file corresponding to each moving window time step.
Also, include a "readme" or instruction file containing the steps involved to create the table along with the resource. 
Upload the pdf file, python script and readme file on HydroShare as a resource. Name the resource in the as “Flood Frequency Plot for <your station name>”. In the abstract, describe about the contents in the pdf file.
 | Assigned Station
USGS Station Number | 
River/Creek Name | 
Parameters | Year
Starting Year of Data Period | 
Ending Year of Data Period | 
Starting Year of Analysis Period | 
Ending Year of Analysis Period |

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP1/Coursepage_DP1_ffareturnperiod_v05.ipynb

## <span style="color:green">Introduction</span>
This program downloads peak flow data from USGS Surface Data Portal for a USER_INPUT station and calculates the flow 
corresponding to (different) return period

This code is written in Python 3 format

Revision No: 05

Last Revised : 2020-06-05

## <span style="color:green">Import the packages/modules required for this exercise</span>

<p> We need the following packages: urllib.parse, urllib.request, math, scipy.stats, numpy (np), gamma from scipy.stats, and invgamma from scipy.stats. The paranthesis contains the commonly used short forms for these libraries.</p>

```python
## Import the required Modules/Packages for obtaining the data from portal
import urllib.parse
import urllib.request
import os

## Import the required Modules/Packages for calculating return period flow using Gamma Inverse Function
import math
import scipy.stats
import numpy as np
#import csv
from scipy.stats import gamma
from scipy.stats import invgamma
```

## <span style="color:green">Definition of Function for retrieval of Peak Flow Data</span> 

<p style='text-align: justify;'>Let us define the first definition block in Python to collect the data from the USGS web link using urllib package. This definition block will be later invoked in the code.</p>
<ul>
<li>Step 1: <span style="color:red">Build the url using the station code.</span></li>
<li>Step 2: <span style="color:red">Access the data using the url and gather the data (date, flow data, station name</span></li>
<li>Step 3: <span style="color:red">Decode the data and extract only the required data</span></li>
<li>Step 4: <span style="color:red">Return the flow data and station name</span></li>

```python
## Define a function for obtaining the peak flow data from USGS Surface Data Portal
def GetAnnualPeakFlowData_f(station_number,FolderName):
    """
    Input: Station Number, Folder Name
    Output: Peak Flow Values, Station Name
    """
    ## Building URLs
    var1 = {'site_no': station_number}
    part1 = 'https://nwis.waterdata.usgs.gov/nwis/peak?'
    part2 = '&agency_cd=USGS&format=rdb'
    link = (part1 + urllib.parse.urlencode(var1) + part2)
    print("The USGS Link is: \t")
    print (link)
    
    ## Opening the link & retrieving data
    response = urllib.request.urlopen(link)
    html = response.read()
    
    ## Assigning the location & Storing the Original Data
    
    #DataStore=FolderName + station_number + ".txt"
    with open(FolderName+'Data_' + station_number + '_raw'  + '.txt', 'wb') as f1:
        f1.write(html)
    f1.close
    
    ## Converts html from bytes class to str class
    html = html.decode()
    ## Splits the string by \n and converts list
    html2 = html.split('\r\n')
    
    ## To get the station name 
    line_no=0
    for line_no in range(len(html2)):
        ## Check if first six (use 0:7) characters is "#  USGS",
        if html2[line_no][0:7]=="#  USGS":
            station_name=html2[line_no][3:]
            break
        line_no+=1
    
    ## Define an empty string
    reqd_data = 'Year,Discharge'+'\n'
    #print(type(reqd_data))
    reqd_flow_list=[]
    reqd_flow_list.append(["Year","Discharge"])
    
    for line in html2[74:]:
        ## Splits each line to col by tab separator
        cols = line.split('\t')
        if len(cols) == 1:
            continue
        ## Joins only date and peakflow
        ## cols[2] corresponds to Date of peak streamflow (format YYYY-MM-DD)
        ## cols[4] corresponds to Annual peak streamflow value in cfs
        newline = ','.join([cols[2],cols[4]])
        reqd_data += newline + '\n'
        reqd_flow_list.append((cols[4]))

    
    ## Converts reqd_data from str class to bytes class
    reqd_data = reqd_data.encode() 
    ## Saves the date and peakflow into a new file
    with open(FolderName+'Data_' + station_number + '_reqd'  + '.txt', 'wb') as f2:
        f2.write(reqd_data)
    f2.close
    print ('\n')
    print("Raw Data and Processed Data is stored in Results Folder.")
    #print(reqd_data)
    
    ## Returns the peak flow data as list for calculation of return period
    return (reqd_flow_list,station_name)
```

## <span style="color:green">MAIN CODE</span> 
Now, the user has to input the station number of the desired USGS Station. It executes the definition block and stores the data in the folder.

```python
## Main Code

station_number=input("Enter USGS Station Number of the Required Station (USGS Station Number/site_no) \t")
print('\t')
FolderName="./Results/"

## Make folder to save the results
if os.path.exists(FolderName) == False:
    os.mkdir(FolderName)

peakflow_list_wb,station_name=GetAnnualPeakFlowData_f(station_number,FolderName)
print("\nThe station name is:", station_name,"\n")
```

_output:_
```
Enter USGS Station Number of the Required Station (USGS Station Number/site_no) 	03335500
	
The USGS Link is: 	
https://nwis.waterdata.usgs.gov/nwis/peak?site_no=03335500&agency_cd=USGS&format=rdb


Raw Data and Processed Data is stored in Results Folder.

The station name is: USGS 03335500 WABASH RIVER AT LAFAYETTE, IN
```

## <span style="color:green">Years for Analysis</span> 

Now, the user has to input enter the four values for dates. This should be properly entered otherwise you will get an error message "Error in length of data and check whether it is continuous".

```python
## Enter the four years for carrying out the analysis
## Input data & analysis years

data_start_year=int(input("Enter the starting year of DATA PERIOD (excluding initial break period):"))
print('\t')
data_end_year=int(input("Enter the ending year of DATA PERIOD:"))
print('\t')
analysis_start_year=int(input("Enter the starting year of ANALYSIS PERIOD:"))
print('\t')
analysis_end_year=int(input("Enter the ending year of ANALYSIS PERIOD:"))
print('\t')
```

## <span style="color:green">Calculation of Return Period</span> 
Next, we have to write the code for performing the calculations of return period flow using moving average method.

```python
<WRITE YOUR CODE HERE>

```
