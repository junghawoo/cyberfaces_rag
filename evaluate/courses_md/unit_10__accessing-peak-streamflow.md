---
title: "Accessing peak streamflow timeseries from United States Geographic Survey (USGS)"
unit_id: 10
course_id: 4
level: "Expert"
slug: accessing-peak-streamflow
is_course: 0
---

# Accessing peak streamflow timeseries from United States Geographic Survey (USGS)

## Extracted resources (local files)

### Peak Streamflow Instructions
*Source file:* `peakstreamflow_instructions.pdf`  ·  *type:* file

1 
 
Accessing and Downloading USGS Peak Streamflow Data (Time Series) 
 
Prepared by  
Jibin Joseph and Venkatesh Merwade  
School of Civil Engineering, Purdue University 
vmerwade@purdue.edu 
 
FAIR Science in Water Resources 
 
Objective 
The main objective of this tutorial is to automatically access and download annual peak 
streamflow data (annual peak series) from the United States Geographic Survey’s (USGS) 
National Water Information System (NWIS) Web Interface using Python code in Jupyter 
Notebook. At the end of the tutorial, you will be creating a time series plot of peakflow 
data. 
Introduction 
Annual peak series (maximum flow value during a year) is used in hydrology for many 
applications including the design of hydraulic structures and design flood modeling and 
mapping. NWIS has more than 29,000 stream gages with annual peak streamflow (aka 
peak flow) data across the United States. In this tutorial, you will download the annual 
maximum series for a station using a manual method. This may be also done using pandas 
or hydrofunctions packages. But, in this tutorial, we will be using string operations. Later, 
we will be using hydrofunctions package in the publication module. This tutorial is part of 
the Data Access (DA) module of FAIR Cyber Training course at Purdue University. 
 
Data Source and Software Requirements 
The data for individual USGS gage stations can be obtained from the link: 
https://waterdata.usgs.gov/nwis/sw. In this tutorial, we will write a code to obtain the data 
by using only the USGS station number and get the raw data in text format. You will need 
a web browser with an internet connection. You will also need an account on 
mygeohub.org to use the Jupyter Notebook on MyGeoHub.

2 
 
Instructions 
 
1. Log on to mygeohub.org. Navigate to Resources > Tools and launch Jupyter Notebook. 
2. Create a folder structure to store code and data for tutorials (for example:  
/courses/FAIRScience/DA1).  You must first create courses in the directory and so 
on. 
 
Figure 1: Folder Structure 
3. Now, on the FAIR Course Page, click on the notebook file available as shown below.  
 
Figure 2: Accessing the instructions and ipynb file 
[Note: If you see a page stating “Session Quota Exceeded”, close the recent sessions 
by clicking on  (cross mark button) under the options. Again, click on the .ipynb file. 
Another option is to close all the Jupyter Notebook sessions in Dashboard > My 
Sessions.] 
 
4. By default, the ipynb file would be in the read-only format. Hit the Save as option 
available in the File menu and save it in the earlier created folder (DA1).

3 
 
 
Figure 3: Read-only state for the ipynb file 
5. Enter the path as “/FAIRScience/DA1/peakstreamflow.ipynb” (shown below). Please note 
that you are saving the file in the parent folder “/home/mygeohub/<username>/courses/” 
which is not shown by default.  
 
Figure 4: Storing the ipynb file in desired location 
6. In order to change the read-only state, hit the refresh button in the browser (another 
option: close and re-open the ipynb file). Now, if you look at the folder, the book 
symbol (
) next to peakstreamflow.ipynb would be black color indicating that the code 
is not running at the moment.  
 
Figure 5: File State in the folder

4 
 
7. Once you open the file, it would turn a green color. At any point, if you feel that 
Notebook is not responding, you can use Restart the kernel   ( ) option to terminate the 
session and then start from the beginning. Also, when you run the cells one-by-one, 
asterisk sign on the left side of the cell ( 
) indicates that the particular cell is 
running. You have to wait until the asterisk sign changes to a number. 
 
8. Packages Import – Firstly, let us import the packages/modules required for this 
tutorial as shown below.  
 
Figure 6: Cell showing the packages to be imported 
 Execute the cell using Run ( 
) button. 
 
9. Function for data access and data storage - Secondly, let us define a function that takes 
the station number as input and stores the results in the user-specified folder location. 
There are two arguments for this function: USGS Station Number and the name of the 
folder where the output has to be stored. Also, this function includes a code for 
creating link to NWIS portal, accessing the data using the link, and storing the raw 
data at the user-defined location. The function also returns the peak streamflow as a 
list and the station name. You are given the script for the function and are not required to 
modify the lines. 
 
10. Main Code - Thirdly, we will write the main code. This will include USGS station 
number input from the user and also the folder location where the data will be stored. 
The folder can be assigned in two different ways, i.e. absolute (long pathname) and 
relative paths. We will use a relative path for this tutorial. Further, the above two 
parameters (station number and folder location) are then passed to the definition 
block. (Note: make sure you use the correct folder name/structure as per your 
directory structure). As mentioned earlier, the function returns the peak streamflow 
data and station name. You can try 03335500 as an example for the Wabash River at 
Lafayette, IN.

5 
 
 
Figure 7: Cell showing the main code of the tutorial 
11. The peak streamflow data (both raw data and processed data) will be saved in the 
“Results” folder as two separate files. The raw delimiter-separated (tab-separated) 
values are stored in a text file with the corresponding USGS Station number (for 
example, the data for USGS station - 03335500 Wabash River at Lafayette, IN - is stored 
as “Data_03335500_raw.txt”). 
 
12. Lastly, we will create a time series plot of peak flow by accessing the stored data using 
pandas dataframe. Let us write the code to plot the data. We will add axis labels and 
titles. 
 
Figure 8: Time Series Plot for Wabash River at Lafayette

6 
 
13. The plot for Wabash River at Lafayette, IN is obtained as below. It can be seen that the 
maximum peak flow occurred between 1910 and 1920 with a magnitude greater that 
175000 cfs. This corresponds to the flood in 1913. 
 
 
Figure 9: Time Series Plot for Wabash River at Lafayette 
 
Ok, you have completed the tutorial! 
 
Turn-in: 
 
1. Get data for Wabash River at Lafayette, format the text file to create a csv file and 
then get 10-, 25-, 50-, 100- and 500- year flow using EV1 distribution in Jupyter 
Notebook. 
2. Create a frequency plot (return period on x-axis and flow on y-axis) in Jupyter 
Notebook. 
 
 
 
Last Revised: 2022/03/30

## Image text (OCR)

### `FAIR_data_principles.jpg`
Bee J \ccessible —

R
oy
%

e

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DA1/Coursepage_DA1_peakstreamflow_v09.ipynb

## <span style="color:green">Introduction</span>
This program downloads annual peak streamflow data from USGS Surface Data Portal for a user input USGS gage station. Further, it stores as a text file (.txt) in an assigned location in Jupyter Notebook directory.

This code is written in Python 3 format.

Revision No: 09

Last Revised : 2022-03-30

## <span style="color:green">Import the packages/ modules required for this exercise</span>

We need a few packages for this module: urllib.parse, urllib.request and os

For plotting, we also need pandas and pyplot (from matplotlib)

```python
## Import the required Modules/Packages for obtaining the data from USGS NWIS Web Interface

## WRITE YOUR CODE BELOW

```

## <span style="color:green">Function for data access and data storage</span>
Let us write a few lines to create a function that takes the station number as input and stores the
results in the user-specified folder location. There are two arguments for this
function: USGS Station Number and the name of the folder where the output has to
be stored. Also, this function includes code for creating a link to NWIS Web Interface,
accessing the data using the link, and storing the raw data at the user-defined
location. The function also returns the peak streamflow as a list and the station name.

```python
## Define a function for obtaining the peak flow data from USGS NWIS Web Interface
## Input (Arguments) - station number and folder name
## Output (Return) - peak streamflow and station name
def GetPeakFlowData_func(station_number,FolderName):
    ## Building URLs
    var1 = {'site_no': station_number}
    part1 = 'https://nwis.waterdata.usgs.gov/nwis/peak?'
    part2 = '&agency_cd=USGS&format=rdb'
    link = (part1 + urllib.parse.urlencode(var1) + part2)
    print("The USGS Link is: \n",link)
    
    ## Opening the link & retrieving data
    response = urllib.request.urlopen(link)
    page_data = response.read()
    
    ## File name assigning & storing the raw data as text file
    ## w - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
    ## b - Opens in binary mode.
    with open(FolderName+'/Data_' + station_number + '_raw'  + '.txt', 'wb') as f1:
        f1.write(page_data)
    ## Usually we need to use f1.close() if we open a file using "open" statement
    ## But using "with open", the file is closed when the block inside the the with statement is exited 
    ## It is done internally.
    
    ## Check if the file has been automatically closed.
    #f.closed
     
    
    print("\nDownload complete for USGS Station Number: ", station_number)
    
    ## Converts html from bytes class to str class
    html = page_data.decode()
    ## Splits the string by \n and converts list
    html2 = html.split('\r\n')
    
    ## To extract the station name for returning from the function call
    line_no=0
    for line_no in range(len(html2)):
        ## Check if first six (use 0:7) characters is "#  USGS",
        if html2[line_no][0:7]=="#  USGS":
            station_name=html2[line_no][3:]
            break
        line_no+=1
    
    ## Define an empty string and list
    reqd_data = '' ## for storing data in the folder
    reqd_flow_list=[] ## to return from the function
    
    for line in html2[74:]:
        ## Splits each line to col by tab separator
        cols = line.split('\t')
        if len(cols) == 1:
            continue
        ## Joins only date and peakflow
        ## cols[2] corresponds to date of peak streamflow (format YYYY-MM-DD)
        ## cols[4] corresponds to annual peak streamflow value in cfs
        newline = ','.join([cols[2],(cols[4])])
        reqd_data += newline + '\n'
        
        ## Append the flow value to the list and return from the function call
        reqd_flow_list.append((cols[4]))

    
    ## Converts reqd_data from str class to bytes class
    reqd_data = reqd_data.encode()
    
    ## Saves the date and peakflow into a new file
    with open(FolderName+'/Data_' + station_number + '_reqd'  + '.txt', 'wb') as f2:
        f2.write(reqd_data)
        
    ## Check if the file has been automatically closed.
    #f.closed

    print("\nRaw Data and Processed Data is stored in the folder for station: ", station_name)
    
    ## Returns the peak streamflow data as a list (for calculation of the return period in the turn-in part) and the station name 
    ## (for using in plots)
    return (reqd_flow_list,station_name)
```

## <span style="color:green">Main Code</span>

This part includes a USGS station number input from the user and also the folder location where the data
will be stored. The above two parameters (station number and folder location) are then passed to the definition block. (Note: make sure you use the correct folder name/structure as per your directory structure). The function returns the peak streamflow data (as a list) and station name.

```python
## Main Code
## WRITE YOUR CODE BELOW

```

## <span style="color:green">Time Series Plot</span>

```python
## To create a time series plot of peak flow data by opening the saved file
import pandas as pd
## Assigning column names
colnames=['Date','PeakFlow']
df = pd.read_csv(FolderName+'/Data_' + station_number + '_reqd'  + '.txt',
                 header=None,names=colnames,parse_dates=[0])

## Setting the index of dataframe as the Date column
df=df.set_index(['Date'])

## Plotting
## WRITE YOUR CODE BELOW
```
