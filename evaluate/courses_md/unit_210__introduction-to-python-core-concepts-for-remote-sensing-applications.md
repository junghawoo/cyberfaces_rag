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

**Description:** Welcome to the "Python Fundamentals for Remote Sensing Applications" module. This educational resource is designed to equip learners with the essential Python programming skills needed for Remote Sensing applications, with a focus on the manipulation of geostationary satellite data.

## Extracted resources (local files)

### Introduction to Python_Core Concepts for RS Applications
*Source file:* `Introduction to Python_Core Concepts for RS Applications.pdf`  ·  *type:* file

Introduction to Python: Core Concepts for Remote 
Sensing Applications 
Prepared by  
Mohamed Abdelkader1, Jorge Bravo1, Marouane Temimi 1, and Jibin Joseph2  
1Civil, Environmental, and Ocean Engineering Department, Stevens Institute of 
Technology 
2School of Civil Engineering, Purdue University 
mabdelka@stevens.edu 
 
FAIR Science in Climate 
 
 
Objective 
   - Understand the basic syntax and structure of Python programming. 
   - Learn to work with different Python data types, including integers, decimals, strings, 
lists, tuples, and dictionaries. 
   - Develop the ability to perform arithmetic operations and data manipulations in 
Python. 
   - Master the foundational concepts of string formatting for better output presentation. 
   - Gain familiarity with Python's control structures, including loops and conditional 
statements. 
   - Acquire the skills to manage and iterate over collections of data, which is crucial for 
processing remote sensing datasets. 
Overview of steps 
1. Introduction to Python's interactive environment and how it can be used in remote 
sensing. 
2. Exploration of Python's basic data types and their relevance to data representation in 
remote sensing. 
3. Performing and understanding operations between integers and decimals, simulating 
real-world measurements and calibrations. 
4. Handling and formatting strings to annotate and label remote sensing data. 
5. Creating and manipulating lists, tuples, and dictionaries, essential for organizing and 
accessing sensor data. 
6. Iterative processes in Python, learning to loop through data sequences which is 
common in satellite data processing.  
Resources 
Remote Sensing Tutorials 
Guide to GOES-R Series Data 
GOES ABI (Advanced Baseline Imager) Realtime Imagery 
GOES Image Viewer

Instructions 
1. Log on to mygeohub.org and launch Jupyter Notebook with Anaconda 5.1. 
2. Hit on Click Here to go to your Home Directory option to access your home directory. 
This is the location where you can store your code and data. 
3. It is advisable to create a separate folder to store code and data for this tutorial 
which makes it accessible in the future. Go ahead and create a folder named 
Module06 to store the code of the current tutorial.  
4. Click on the notebook file available on the course page. Hit the Save as option 
available in the File menu and save it in the earlier created folder. 
5. Review the introductory overview of Python's capabilities in remote sensing 
applications to understand the context and relevance of programming in this field.  
 
 
6. Review the instructions for using Jupyter Notebooks as our interactive computing 
environment.

7. Execute the code cell in #test_cell using Ctrl+Enter to practice running a simple print 
command. 
 
8. Run the provided code to see how variables work in Python and observe how a variable can 
change types from a string to a number. Notice how the 'print' function is used to clarify 
the output, making the data's context and changes clear and understandable.

9. Execute the code to observe how integers and decimals represent different data types in 
weather monitoring. Pay attention to the operations between them to see their combined 
effect on the results. 
 
10. Run the code to see how strings function to store and present textual data such as satellite 
names and note how formatted print statements enhance data readability.

11. Execute the code examples to observe how different methods of string formatting work in 
Python and how they can be applied to neatly display weather-related data.

12. Follow the examples provided to learn how lists are defined and used in Python for 
organizing diverse types of data, such as weather observations and satellite information. 
Pay attention to how lists can contain different data types and how this flexibility is 
advantageous in meteorological analysis. 
 
13. For this tutorial on tuples in Python, we're focusing on how to create an immutable 
collection of items, which is useful for storing fixed sets of data such as instrument names 
on satellites. Observe how once defined, the contents of the tuple cannot be altered, 
ensuring data integrity for constants in meteorological analysis.

14. This portion of the tutorial explains how to utilize dictionaries in Python to store and 
manipulate weather data parameters. Dictionaries allow us to create a structured dataset 
with key-value pairs, ideal for meteorological data management. Each key-value pair 
corresponds to a weather parameter and its measured value, making the data easy to access 
and update, as demonstrated by the addition of the 'UV Index' to the existing dictionary. 
 
15. This section introduces the concept of iterations using the `for` loop in Python.  
 
#Iteration_cell: By iterating over the keys of the `weather_parameters` dictionary, we 
print out each weather parameter, demonstrating a simple yet effective way to enumerate 
the keys in a dictionary. This operation mimics a common task in data handling where 
listing all the parameters in a dataset is necessary.

#Adding_parameters_Cell: Here we see how to enhance the `weather_parameters` 
dictionary by adding new entries. Specifically, we introduce 'Atmospheric Pressure' and 
'Dew Point' with corresponding values. Additionally, the snippet showcases string 
formatting in Python by using the `format()` method. With this technique, we can 
construct a readable and informative sentence that incorporates our data directly into the 
string, which is particularly useful for generating reports or output for further analysis. 
 
#Exploring_itmes_cell: In this code block, we continue to explore iterations with a `for` 
loop, this time iterating over both keys and values of the `weather_parameters` dictionary 
by utilizing the `.items()` method. This approach is crucial when one needs to process both 
the name (key) and the recorded measurement (value) of each weather parameter. The loop 
prints out each parameter and its corresponding value in a format that is suitable for 
reviewing collected meteorological data or preparing it for presentation or further 
computation. 
 
 
Ok, you have completed the tutorial! 
 
Turn-in 
For this assignment, you will be demonstrating your skills in manipulating and 
presenting meteorological data using Python dictionaries and iterations. Please follow 
the steps outlined below to complete your task and submit your work:

1. Add a new weather parameter to the `weather_parameters` dictionary: 
- Choose a weather parameter that is commonly monitored by geostationary satellites 
(for example, Solar Radiation, Visibility, etc.). 
- Insert the new weather parameter into the dictionary with a hypothetical value. 
- Print the updated dictionary to verify the addition of the new parameter. 
 
2. Create a formatted output using an f-string: 
 
- Craft a message using a formatted string literal (f-string) to include dynamic data from 
the `weather_parameters` dictionary. 
- Your message should be clear, informing the reader about one of the parameters and its 
value, mimicking a real-world data report. 
 
3. Prepare your submission documents: 
 
- Generate a PDF document that captures the final state of the `weather_parameters` 
dictionary, including the new parameter you added. 
- The document should also display the formatted message you created with the f-string. 
- Additionally, create a "readme" or instruction file that outlines the steps you followed 
to complete the assignment. This document should serve as a guide for anyone reviewing 
your code or results. 
 
4. Upload your documents to the designated submission platform: 
 
- Your submission should include the following: 
- The PDF document with your updated `weather_parameters` dictionary and formatted 
message. 
- The original Python script used to produce these results. 
- The "readme" or instruction file detailing the steps of your process. 
- Name your submission as "Weather Data Analysis for [Your Chosen Parameter]" to 
reflect the content of your work. 
- In the description or abstract, provide a brief overview of the contents of your 
submission, emphasizing the addition of the new weather parameter and the use of f-
strings in your analysis. 
 
Ensure that all files are correctly formatted, legible, and free of errors before submission. 
If you encounter any issues or have questions about the assignment, please reach out to 
your instructor or teaching assistant for guidance.

## Fetched resources (external URLs)

### Lecture 1: Introduction to Python: Core Concepts for Remote Sensing Applications (notebook)
*URL:* https://github.com/MAbdelkader94/Python-for-RS-applications/blob/main/Lecture_01/Introduction_to_Python_Core%20Concepts_for_RS_Applications.ipynb

# Introduction to Python: Core Concepts for Remote Sensing Applications

Python is a powerful and easy-to-learn programming language, characterized by its high-level efficient data structures and a simple yet effective object-oriented programming system. Its elegant syntax and dynamic typing, combined with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas, including remote sensing and weather monitoring through geostationary data analysis.

Although Python is utilized across a diverse range of fields, it has recently become the most popular language for scientific programming, particularly in the domain of geospatial and environmental data analysis. This has been facilitated by the integration with libraries such as NumPy for handling arrays and matrices, and Matplotlib for data visualization, among others.

This tutorial doesn't assume prior knowledge of Python, but it also doesn't delve into the language in great detail. The focus here is to emphasize how to manipulate arrays for image processing in the context of extracting meaningful insights from geostationary satellite data, a critical component in weather monitoring and analysis.


## Jupyter Notebooks

Traditionally, a Python program is executed using the command `python filename.py`, where `filename.py` is a file containing Python source code.

However, for this course, we will be utilizing Jupyter Notebook servers and code notebooks. These notebooks allow us to combine both text and code, organized in cells, providing a convenient platform for experimenting with new concepts and documenting our processes, especially when working with geostationary data for weather monitoring.

To initiate the notebook server, execute the command `jupyter notebook` from your command line.

If you have existing notebooks you wish to open, navigate to the directory containing those notebooks before running the aforementioned command, facilitating easy access to them later. The server runs continuously while we are using the notebooks.

Once the server is up and running, and the browser window is open, you can choose to open a pre-existing notebook or create a new one. Inside the notebook, you can write and execute both text and code, a seamless environment that is particularly handy for data analysis and visualization in weather monitoring projects. Save the state of a notebook at any time using `Ctrl+S`, which preserves both the code and the results of any executions.

We have an installation guide available to assist you in setting up Python and Jupyter on your computer, to ensure you can actively participate in this course and explore weather monitoring through geostationary data analysis.


```python
# test_cell
# This is a comment because it starts with #

# This is a code cell, an essential tool in analyzing geostationary data.

# Execute the cell with Ctrl+Enter. Give it a try.

# The print function can be used to display various outputs, such as weather data insights.

################################# WRITE YOUR CODE BELOW ################################
                     # printing a string, later we will use it to display data insights.
########################################################################################
```

_output:_
```
Hello World
```

```python
################################# WRITE YOUR CODE BELOW ################################
                # printing a number, which can be a representation of data like temperature or wind speed in our later analyses.
########################################################################################
```

_output:_
```
4
```

## Basic Python

In Python, variables do not need to be declared explicitly; they are defined when used for the first time. Moreover, although it is not recommended, they can change type by being redefined. This feature can be particularly useful in the dynamic analysis of weather data, where you might be handling various types of data attributes like temperature readings (numerical data) or weather descriptions (string data).

```python
################################# WRITE YOUR CODE BELOW ################################
          # Assigning the name of a geostationary satellite to the variable x
          # Printing the value of x, which will display the satellite name
########################################################################################
```

_output:_
```
GOES-16
```

```python
################################# WRITE YOUR CODE BELOW ################################
        # This could represent a meteorological parameter, such as 5°C temperature or 5 m/s wind speed
                                                # Printing a message along with the value of x, 
                                                #including units, to provide a clear context for the meteorological data
########################################################################################
```

_output:_
```
The average Temperature is:  5 °C
```

```python
################################# WRITE YOUR CODE BELOW ################################
             # Calculating a new temperature value by increasing the previous value (x) by 1.0°C
                          # Printing a message along with the value of y to showcase 
                                                    # the updated meteorological data
########################################################################################
```

_output:_
```
Updated Average Temperature is:  6.0 °C
```

## Integer Numbers

In the context of weather monitoring using geostationary data, integer numbers can represent various types of data such as temperature readings in whole numbers, the count of certain weather events in a given time period, or categorizations based on satellite imagery analysis.


```python
################################# WRITE YOUR CODE BELOW ################################
      # This could represent a meteorological category, such as a Category 5 hurricane 
            # as per the Saffir-Simpson scale.
                      # Printing a message to contextualize 
                                             # the meteorological data represented by x_int
########################################################################################
```

_output:_
```
Current Hurricane Category:  5
```

## Decimal Numbers

In weather monitoring using geostationary data, decimal numbers often play a significant role. They can represent finer details in meteorological data such as precise temperature readings, humidity levels, or precipitation amounts. These finer data points assist in more accurate analysis and predictions.

```python
################################# WRITE YOUR CODE BELOW ################################
          # This might represent a precise temperature reading of 5.5°C in weather monitoring.
          # Displaying the value of x_flt, illustrating the use of decimal numbers in meteorological data
########################################################################################
```

_result:_
```
5.5
```

## Operations Between Integers and Decimals

Working with geostationary data for weather monitoring often involves performing operations between integers and decimals. For example, calculating the dew point, a key parameter


```python
# In this scenario, let's assume that 'x_int' represents the category number of a hurricane (on a scale of 1 to 5),
# and 'x_flt' represents the current temperature in degrees Celsius at the eye of the hurricane.

################################# WRITE YOUR CODE BELOW ################################
            # Category 5 hurricane, indicating a severe hurricane as per the Saffir-Simpson scale.
             # Current temperature at the eye of the hurricane is 5.5°C.
########################################################################################

# Here, we are calculating a hypothetical parameter that is the product 
#of the hurricane category and the temperature at the hurricane's eye. 
#This is a fabricated parameter for the purpose of this exercise.
################################# WRITE YOUR CODE BELOW ################################


########################################################################################

# Displaying the result of the operation, which could be used in further analyses or models related 
# to weather monitoring and predictions.
################################# WRITE YOUR CODE BELOW ################################


########################################################################################
```

_result:_
```
27.5
```

## Strings

In the realm of weather monitoring through geostationary data,strings can hold vital information. They might represent satellite names, meteorological terms, annotations on weather maps, or descriptions in data metadata.

```python
# In weather monitoring, strings can be used to store various types of information. 
# Here, we're storing the name of a geostationary satellite.
################################# WRITE YOUR CODE BELOW ################################

                                                              # Using a formatted string to create a more 
                                                            # descriptive and contextual message
    
########################################################################################
```

_output:_
```
Currently accessing data from satellite: GOES-16
```

## Text String Formatting

Text string formatting is a powerful tool when dealing with meteorological data analysis. It allows us to neatly organize and present data in a readable format, which is vital when conveying complex weather information. Whether it's labeling geostationary satellite imagery, creating descriptive annotations on weather maps, or formatting output reports, understanding how to effectively use text string formatting can enhance the clarity and professionalism of your data presentations.


```python
# Here we are concatenating a string literal with a variable that holds the name of a geostationary satellite.
# This can be a simple way to create descriptive labels or annotations in data analysis scripts or reports.

################################# WRITE YOUR CODE BELOW ################################

                      # This will print a message indicating the source of the current data, 
                    # demonstrating string concatenation in Python.
########################################################################################
```

_output:_
```
Current data retrieved from satellite: GOES-16
```

```python
# In this cell, we are initializing a variable 'x_02' which could represent a meteorological parameter, 
# such as wind speed measured in meters per second.

################################# WRITE YOUR CODE BELOW ################################
        # This might represent a wind speed of 5 m/s, a relevant parameter in weather monitoring.

# Printing a message to provide context to the variable.
################################# WRITE YOUR CODE BELOW ################################
                                                    # This print statement contextualizes 
                                                 # the value of 'x_02' in terms of weather monitoring.
########################################################################################
```

_output:_
```
The current wind speed is: 5 m/s
```

```python
# In this script, we are utilizing Python's str.format method to create a formatted string. 
# This method can be very useful in formatting meteorological data in a structured and readable way.

################################# WRITE YOUR CODE BELOW ################################

########################################################################################

# Here, {:05d} will format x_02 as a five-digit integer, filled with zeros if necessary. 
# This can be used to maintain a consistent data format, for instance when 
# logging meteorological observations at regular intervals.

# The {} will be replaced by 7, which might represent another meteorological parameter, 
#such as the Beaufort scale for wind speed.

################################# WRITE YOUR CODE BELOW ################################
                         # This will print the formatted message, 
#demonstrating a way to structure meteorological data for readability and consistency.
########################################################################################
```

_output:_
```
Current data readings are: 00005 & 7
```

## Lists

In Python, lists are used to store multiple items in a single variable. Lists are one of the most versatile data types in Python, and they are used extensively in data science and meteorology.

For weather monitoring, lists can be employed to store a series of data points collected from geostationary satellites. This could include a range of information such as temperature readings over a period, wind speed data, or a collection of imagery data at different time intervals. 

In the following sections, we will explore how to create and manipulate lists in Python to efficiently handle meteorological data.

```python
# In this cell, we are defining a list called 'Num' which contains a series of meteorological readings. These readings could represent data like temperature or wind speed collected over a series of time intervals from a geostationary satellite.
################################# WRITE YOUR CODE BELOW ################################
                  # This list might represent data points collected at various time intervals, crucial in analyzing and monitoring weather patterns.
########################################################################################


# We will print the list to visualize the data points.
################################# WRITE YOUR CODE BELOW ################################

########################################################################################
```

_output:_
```
Meteorological data points: [10, 9, 8, 7.5, 9]
```

```python
# In this cell, we have a list named 'geostationary_satellites' that contains names of several geostationary satellites. These satellites play a vital role in weather monitoring by providing continuous data over a specific geographical area.
################################# WRITE YOUR CODE BELOW ################################

########################################################################################


# Let's print the list to visualize the names of the geostationary satellites.
################################# WRITE YOUR CODE BELOW ################################


########################################################################################
```

_output:_
```
List of geostationary satellites: ['GOES-16', 'GOES-17', 'Himawari-8', 'Meteosat-11', 'Elektro-L']
```

```python
# In this cell, we define a list named 'data_sample' that contains a mix of different data types typically encountered when processing geostationary satellite data. 
# This includes boolean values, floating-point numbers, strings, and even another list (which might represent a series of data points).

################################# WRITE YOUR CODE BELOW ################################

########################################################################################
# Here:
# - The boolean value (True) might represent the success status of data retrieval from the satellite.
# - The floating-point number (10.5) could be a specific meteorological reading (e.g., temperature or humidity).
# - The string ("Cloud Coverage") might denote the type of data or analysis being represented.
# - The nested list ([0, 1, 1]) could be a series of binary data points representing satellite imagery analysis results (e.g., cloud presence).

# Let's print the list to visualize the different elements and their data types.
################################# WRITE YOUR CODE BELOW ################################

########################################################################################
```

_output:_
```
Sample geostationary satellite data: [True, 10.5, 'Cloud Coverage', [0, 1, 1]]
```

## Tuples

In Python, a tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists, but the main difference is that tuples cannot be changed once declared. This makes them ideal for storing data that should not be altered, such as fixed geostationary satellite coordinates or constants used in meteorological calculations.

In the context of weather monitoring using geostationary data, tuples can be used to store a variety of data types, like the geographical coordinates of a satellite, date and time information for data collections, or sets of fixed parameters for various meteorological calculations.

In the following cells, we will see how to define and use tuples in Python to handle immutable data sets effectively in meteorological analyses.

```python
# In this cell, we define a tuple called 'satellite_instruments' that contains the names of various instruments commonly found on geostationary satellites. 
# These instruments are crucial for monitoring different meteorological variables such as temperature, humidity, wind speed, etc.

################################# WRITE YOUR CODE BELOW ################################

########################################################################################


# Let's print the tuple to visualize the names of the satellite instruments.

################################# WRITE YOUR CODE BELOW ################################

########################################################################################
```

_output:_
```
Common instruments on geostationary satellites: ('ABI', 'GLM', 'SEISS', 'EXIS', 'SUVI', 'MAG', 'SWEAP')
```

## Dictionaries

Dictionaries are a flexible data structure in Python that allow us to store and manage data in a key-value pair format. This structure is particularly helpful when we are working with complex datasets, such as the ones we obtain from geostationary satellites.

In the context of weather monitoring, dictionaries can serve as a structured and organized way to store various kinds of meteorological data. For instance, we can use dictionaries to store data on different weather parameters (like temperature, humidity, wind speed, etc.) collected by various instruments on a geostationary satellite, associating each parameter with a specific time stamp or geographical location.

In the following cells, we will explore how to create and manipulate dictionaries in Python to efficiently handle the diverse datasets we encounter in meteorological analysis.

```python
# In this cell, we create a dictionary named 'weather_parameters' that stores simulated data representing various weather parameters recorded by a geostationary satellite. 
# Each key represents a different parameter, and the associated value represents a recorded measurement.
################################# WRITE YOUR CODE BELOW ################################





########################################################################################


# Let's print the dictionary to visualize the weather parameters and their respective recorded values.
################################# WRITE YOUR CODE BELOW ################################

########################################################################################
```

_output:_
```
Recorded weather parameters: {'Temperature (°C)': 25, 'Humidity (%)': 70, 'Wind Speed (km/h)': 15, 'Cloud Coverage (%)': 30, 'Precipitation (mm)': 20}
```

```python
# In this cell, we update the 'weather_parameters' dictionary with new data. We add a new entry for "UV Index", a crucial parameter in meteorological analysis.
################################# WRITE YOUR CODE BELOW ################################

########################################################################################


# Let's print the updated dictionary to see all the weather parameters, including the newly added UV Index entry.
################################# WRITE YOUR CODE BELOW ################################

########################################################################################
```

_output:_
```
Updated weather parameters: {'Temperature (°C)': 25, 'Humidity (%)': 70, 'Wind Speed (km/h)': 15, 'Cloud Coverage (%)': 30, 'Precipitation (mm)': 20, 'UV Index': 8}
```

## Iterations

In the field of meteorology, especially when dealing with geostationary satellite data, we often need to perform operations repetitively, sometimes over large datasets. This is where iterations, a fundamental concept in programming, comes into play.

Through iterations, we can automate the process of collecting, analyzing, and visualizing data from geostationary satellites, making the data handling process more efficient and less prone to errors. Python provides several methods for performing iterations, including 'for' and 'while' loops.

In the following sections, we will explore how to use iterations in Python to manipulate and analyze satellite data more effectively.

- For Loop: This type of loop is used when we want to repeat a block of code a known number of times.
- While Loop: This loop continues to execute a block of code as long as a certain condition remains true.

Let's delve deeper into these concepts with practical examples related to weather monitoring.

```python
#Iteration_cell: 

# In this script, we use a for loop to iterate over the keys in the 'weather_parameters' dictionary. 
# This loop will print the name of each weather parameter stored in the dictionary, 
# simulating a simple data retrieval process from our geostationary satellite data set.

################################# WRITE YOUR CODE BELOW ################################


########################################################################################
```

_output:_
```
Temperature (°C)
Humidity (%)
Wind Speed (km/h)
Cloud Coverage (%)
Precipitation (mm)
UV Index
```

```python
#Adding_parameters_Cell

################################# WRITE YOUR CODE BELOW ################################






########################################################################################
```

_output:_
```
The current AP is 1013 hPa, and the DP is 15°C.
```

```python
#Exploring_itmes_cell

# In this cell, we are using a for loop to iterate over the keys in the 'weather_parameters' dictionary
# and print both the parameter name and its value. This simulates a process of reporting and analyzing 
# meteorological data collected by geostationary satellites.

################################# WRITE YOUR CODE BELOW ################################

    
########################################################################################
```

_output:_
```
Atmospheric Pressure: 1013 hPa
Dew Point (°C): 15°C
```

# Turn-in

### Student Task:

Now, it's your turn to add a new parameter to the `weather_parameters` dictionary!

1. Choose a weather parameter that is monitored by geostationary satellites (e.g., Atmospheric Pressure, Solar Radiation, etc.).
2. Add a new key-value pair to the `weather_parameters` dictionary with the chosen parameter and a hypothetical value.
3. Print the updated dictionary to verify that your new parameter has been successfully added.

Here's a template to get you started:

```python
# Step 1: Choose a weather parameter and a hypothetical value
new_parameter = "Your Chosen Parameter"
new_value = "Your Chosen Value"

# Step 2: Add the new parameter to the dictionary
weather_parameters[new_parameter] = new_value

# Step 3: Print the updated dictionary
print("Updated weather parameters with your new data:", weather_parameters)

```python
# In this script, we are using a formatted string literal (f-string) to create a message that includes the value of a variable representing a geostationary satellite.
# This technique can be particularly useful when we want to dynamically include variable data in our messages or outputs.

################################# WRITE YOUR CODE BELOW ################################


# The f-string includes the value of the 'x_str' variable, which holds the name of a geostationary satellite, dynamically integrating it into the message.
########################################################################################


################################# WRITE YOUR CODE BELOW ################################
              # This will print a message indicating the source of the current data, showcasing the use of f-strings in Python to create dynamic messages.
    
########################################################################################   
```

_output:_
```
Hello, this is data from the GOES-16 satellite
```

```python
# In this cell, we are adding a new weather parameter to our 'weather_parameters' dictionary. Here, we add a "Dew Point (°C)" entry with a value of 34, simulating a new piece of data collected by the geostationary satellite.

################################# WRITE YOUR CODE BELOW ################################


# Let's print the dictionary again to visualize all the weather parameters, including the newly added Dew Point entry.




########################################################################################
```

_output:_
```
Updated weather parameters with new Dew Point data: {'Temperature (°C)': 25, 'Humidity (%)': 70, 'Wind Speed (km/h)': 15, 'Cloud Coverage (%)': 30, 'Precipitation (mm)': 20, 'UV Index': 8, 'Dew Point (°C)': 34}
```

### Lecture 2: Web Scraping and Data Download (notebook)
*URL:* https://github.com/MAbdelkader94/Python-for-RS-applications/blob/main/Lecture_02/Web%20Scraping%20and%20Data%20Download.ipynb

# Lecture 2: Web Scraping and Data Download

## Introduction

In this second lecture, we will dive into web scraping and data download for meteorological analysis. You might already be familiar with the user-friendly data download page created by **Brian K. Blaylock**, which allows manual data retrieval:

[**Brian K. Blaylock - GOES-16 Data Download**](https://home.chpc.utah.edu/~u0553130/Brian_Blaylock/cgi-bin/goes16_download.cgi)

While this manual download method is convenient, it may not be suitable for automated data acquisition. That's why we will explore the concept of **"Web scraping"** to automate this process and make it more efficient.

Explore [**NOAA GOES on AWS**](https://docs.opendata.aws/noaa-goes16/cics-readme.html#accessing-goes-data-on-aws)

Let's get started!

```python
# Importing the datetime module to work with date and time information.
## complete you code here:


```

The basic date and time types could be obtained using the "datetime" Library
https://docs.python.org/3/library/datetime.html

```python
# Create a datetime object representing the current UTC time.
## complete you code here:


```

```python
# Display current date
## complete you code here:


```

```python
# Display a message along with the current UTC time.
## complete you code here:


```

```python
# Define a dictionary 'dini' containing parameters for data download URL construction.
dini = {
## complete you code here:    
    'src': ,                    # Data source
    'sat': ,                    # Satellite (GOES-16)
    'str': ,                    # Spatial domain (e.g., 'F' for full disk)
    'prd': ,                    # Product type (e.g., ABI-L1b-Rad for radiance data)
    'tme': dnow                 # Date and time (current UTC time)
}
```

```python
# Construct the URL for data download using the provided parameters.
url = (
    'https://home.chpc.utah.edu'
    '/~u0553130/Brian_Blaylock/cgi-bin/goes16_download.cgi?'
    'source={src}&'
    'satellite=noaa-goes{sat}&'
    'domain={str}&'
    'product={prd}&'
    ## complete you code here:
    'date=         '                # Format the date as 'YYYY-MM-DD'
    'hour=         '                # Format the hour as 'HH'
)
```

```python
# Print the constructed URL with parameter values applied using string formatting.
## complete you code here:



```

```python
# Import the 'requests' library for making HTTP requests.
## complete you code here:

# Import 'BeautifulSoup' from the 'bs4' library for web scraping and parsing HTML.
## complete you code here:

# Import 'minidom' from 'xml.dom' for working with XML data.
## complete you code here:

```

```python
# Construct the complete URL with parameter values applied.
## complete you code here:
urit = 

# Make an HTTP GET request to the constructed URL.
## complete you code here:
response = 

# Parse the HTML content of the response using BeautifulSoup.
## complete you code here:
dates = 

# Find all elements with class 'mybtn-group' in the parsed HTML.
## complete you code here:
alltimesxml = 


# Display the scraped HTML content stored in the 'alltimesxml' variable.
## complete you code here:
alltimesxml
```

```python
# Initialize an empty list to store the data to be downloaded.
## complete you code here:
ls2down = 

# Initialize 'nps' to -1 as an initial value.
nps = -1

# Iterate through the elements in 'alltimesxml'.
for i in range(len(alltimesxml)):
    # Find all 'a' tags within the current element.
    tags = alltimesxml[i].find_all('a')
    
    # Initialize an empty list to store time differences.
    nwdts = []
    
    # Iterate through the 'a' tags.
    for j in range(len(tags)):
        # Extract the date and time information from the 'href' attribute.
        dts = tags[j].attrs['href'].split('/',)[-1]
        
        # Split the date and time string to extract the timestamp.
        lsfst = dts.split('_')
        dtstr = lsfst[-3]
        
        # Convert the timestamp to a datetime object.
        ndnow = datetime.strptime(dtstr, 's%Y%j%H%M%S%f')
        
        # Calculate the time difference in minutes.
        tmdf = ndnow.minute - dnow.minute
        
        # Append the absolute time difference to the list.
        nwdts.append(abs(tmdf))
    
    # Find the index with the minimum time difference.
    id1 = min(nwdts)
    
    # If 'nps' is 0 and the minimum time difference is less than 'dtm', update 'nps'.
    if nps == 0 and id1 < dtm:
        nps = nwdts.index(id1)
    
    # Extract the filename and button text from the 'a' tag.
    lsfst = tags[nps].attrs['href'].split('/',)[-1]
    print(lsfst + ' - ' + tags[j].button.text)
    
    # Append the filename to the 'ls2down' list.
    ls2down.append(lsfst)
```

```python
# Check if the 'str' key in the dini dictionary contains 'M' (indicating a specific domain)
if 'M' in dini['str']:
    # If 'M' is found, update the 'str' key in the dini dictionary to 'M' for consistency
    dini.update({'str':'M'})

# Construct the base URL for downloading the data using formatted string. 
# This URL includes placeholders for satellite (sat), product (prd), and time (tme) parameters, 
# which are filled in from the dini dictionary.
url_base = 'https://noaa-goes{sat}.s3.amazonaws.com/{prd}{str}/{tme:%Y}/{tme:%j}/{tme:%H}/'.format(**dini)

# Initialize an empty list to store the complete URLs for downloading the data files
## complete you code here:

# Iterate over each item in the list of file identifiers (ls2down)
for urli in ls2down:
    # Uncomment the next line to print each constructed URL before adding it to the list (for debugging)
    # print(f'{url_base}{urli}')
    # Append the full URL for each file to the urls2dwn list. This URL is constructed by combining
    # the base URL with the specific file identifier (urli), allowing for direct access to each file.
    
    ## complete you code here:
    
```

```python
import requests
import os

# Prompt the user to enter the download folder path. 
download_folder = input("Enter the path to the download folder: ") # you can name the download folder "input"
 
# URL of the file to download.
urld = 'https://noaa-goes16.s3.amazonaws.com/ABI-L1b-RadM/2022/306/17/OR_ABI-L1b-RadM1-M6C13_G16_s20223061734250_e20223061734319_c20223061734351.nc'

# Send an HTTP GET request to the URL.
response = requests.get(urld)

# Check if the response is successful (status code 200).
if response.status_code == 200:
    # Extract the filename from the URL.
    filename = os.path.basename(urld)

    # Construct the complete path to save the file in the chosen download folder.
    file_path = os.path.join(download_folder, filename)

    # Write the content to the file in binary mode.
    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"File '{filename}' downloaded and saved to '{download_folder}'.")
    # Press enter if you want to save the file in the current directory 
else:
    print("Failed to download the file. Check the URL or your internet connection.")
```

```python
# Display the URLs for downloading the data files.


```

```python
import requests
import os

try:
    # Prompt the user to enter the download folder path.
    download_folder = input("Enter the path to the download folder: ") # you can name the download folder "input"

    # Ensure the download folder exists.
    if not os.path.isdir(download_folder):
        print(f"Creating download folder at '{download_folder}'.")
        os.makedirs(download_folder, exist_ok=True)

    # URL of the file to download.
    urld = 'https://noaa-goes16.s3.amazonaws.com/ABI-L1b-RadM/2022/306/17/OR_ABI-L1b-RadM1-M6C13_G16_s20223061734250_e20223061734319_c20223061734351.nc'

    print("Attempting to download the file...")
    # Send an HTTP GET request to the URL.
    response = requests.get(urld, stream=True)

    # Check if the response is successful (status code 200).
    if response.status_code == 200:
        # Extract the filename from the URL.
        filename = os.path.basename(urld)

        # Construct the complete path to save the file in the chosen download folder.
        file_path = os.path.join(download_folder, filename)

        # Write the content to the file in binary mode.
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File '{filename}' downloaded and saved to '{download_folder}'.")
    else:
        print(f"Failed to download the file. Server responded with status code: {response.status_code}. Check the URL or your internet connection.")
except Exception as e:
    print(f"An error occurred: {e}")
```

```python
import requests
import os

# Specify the local directory where you want to save the files. # you can name the download folder "input"
local_directory = input("Enter the path to the download folder: ")

# Ensure that the local directory exists; create it if it doesn't.
os.makedirs(local_directory, exist_ok=True)

# Iterate through the URLs and download files.
for urld in urls2dwn:
    # Extract the filename from the URL.
    ntw = urld.split('/')[-1]
    
    # Construct the complete path to save the file in the local directory.
    file_path = os.path.join(local_directory, ntw)
    
    # Send an HTTP GET request to the URL.
    resp = requests.get(urld)
    
    # Check if the response is successful (status code 200).
    if resp.status_code == 200:
        # Write the content to the file in binary mode.
        with open(file_path, "wb") as file:
            file.write(resp.content)
        print(f"File '{ntw}' downloaded and saved to '{local_directory}'.")
    else:
        print(f"Failed to download '{ntw}' from the URL: {urld}")

## complete you code here:


```

```python
# Import necessary AWS SDK and configuration modules.
## complete you code here:



```

```python
# Select the AWS S3 bucket name, remote file path, and local destination file name.
## complete you code here:
s3_bucket = 
bucket_file = 'ABI-L2-MCMIPF/2022/273/03/OR_ABI-L2-MCMIPF-M6_G16_s20222730350207_e20222730359521_c20222730400027.nc'
local_file = 'OR_ABI-L2-MCMIPF-M6_G16_s20222730350207_e20222730359521_c20222730400027.nc'
```

```python
# Connect to the AWS S3 bucket using the Boto3 client.
## complete you code here:


```

```python
# Download the file from the AWS S3 bucket to the local destination.
## complete you code here:


```

### Lecture 3: Reading NetCDF files with Python (notebook)
*URL:* https://github.com/MAbdelkader94/Python-for-RS-applications/blob/main/Lecture_03/Reading_NetCDF_Data_with_Python.ipynb

# Lecture 3: Reading NetCDF Data with Python

In this notebook, we will explore two of the most common libraries for reading data in NetCDF format: **netCDF4** and **Xarray**.

## netCDF4 Library
[netCDF4 Documentation](https://unidata.github.io/netcdf4-python/)

**netCDF4-python** is a Python interface to the **NetCDF-C library**. It provides a powerful set of tools for working with NetCDF data files.

## Xarray Library
[Xarray Documentation](https://docs.xarray.dev/en/stable/)

**Xarray** simplifies the process of working with labeled multidimensional arrays in Python. It offers efficiency and ease of use when handling complex datasets.

In this lecture, we will explore how to use these libraries to read and manipulate NetCDF data, enabling us to work effectively with meteorological datasets.

### Reading Data with netCDF4 in Python

Before delving into the process of reading and handling remote sensing data, we start by importing a crucial component from the netCDF4 library in Python:

**What is netCDF4?**

- `netCDF4` is a Python library that provides an interface to work with Network Common Data Form (netCDF) files. netCDF is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data.

**Why Dataset?**

- The `Dataset` class within the `netCDF4` library is fundamental for working with netCDF files. It allows us to open, inspect, manipulate, and create netCDF files in Python. 

**Key Functionalities:**

- **Reading Data:** `Dataset` can be used to open existing netCDF files in either read-only or write-access modes, allowing for the examination and analysis of the data stored in these files.
- **Metadata Exploration:** With this class, we can easily explore the metadata of the netCDF files, understanding dimensions, variables, and attributes that describe the data.
- **Data Manipulation:** Besides reading, the `Dataset` class also facilitates modifying existing data or creating new data within the netCDF files, making it a versatile tool for data processing in remote sensing.

**Application in Remote Sensing:**

- In the context of remote sensing, netCDF files are commonly used for storing multidimensional datasets, such as satellite imagery or atmospheric data models. Utilizing the `Dataset` class, we can efficiently handle these complex datasets for various applications, including climate analysis, weather prediction, and environmental monitoring.

As we progress through this course, you will learn how to effectively utilize the `Dataset` class from the `netCDF4` library to read, analyze, and manipulate remote sensing data stored in netCDF format, equipping you with essential skills for data-driven exploration and analysis in the field of remote sensing.

```python
# import necessary library

# Your code goes here:

```

```python
# Define the file path for the ABI data
path2data = "./Input_data/ABI-L2-CMIPC/s20180471917"

# Set the name of the netCDF data file
name2data = "OR_ABI-L2-CMIPC-M3C13_G16_s20180471917196_e20180471919581_c20180471920028.nc"

# Construct the full file path by combining the directory path and file name
# Your code goes here:


```

```python
# Open the netCDF file for the C08 channel using the Dataset class
# Your code goes here:



```

```python
#Access the Cloud and Moisture Imagery (CMI) variable 
# Your code goes here:


```

## Reading Data with Xarray

```python
# Import xarray library for working with labeled multi-dimensional arrays
# Your code goes here:


```

```python
# Define the full file path for the dataset
# Your code goes here:

# Load the dataset into an xarray object for easy data manipulation
# Your code goes here:

# Display the contents of the dataset
# Your code goes here:
```

```python
# Configure matplotlib to show figures embedded in the notebook
# Your code goes here:


# Plot the 'CMI' variable from the netCDF dataset using xarray's plotting capabilities
# Your code goes here:
```

```python
# Retrieve and display the attributes of the 'CMI' variable in the dataset
# Your code goes here:


```

```python
# Import the matplotlib.pyplot module for plotting graphs
# Your code goes here:


```

```python
# Create a figure with specific dimensions
# Your code goes here:



# Add a subplot to the figure
# Your code goes here:



# Display the 'CMI' variable data as an image with specified colormap and origin
# Your code goes here:


```

```python
# Import the NumPy library for numerical operations on arrays
# Your code goes here:


```

```python
# Define a custom color map for the infrared imagery
cmap = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#b6ffb6', '#79ff79', '#00ff00', '#ff8e8e', '#ff5151', '#ff0000', '#aa0000', '#550000', '#00ffff', '#00bef3', '#0079ca', 
        '#0028a2', '#000079', '#fbfb00', '#e7e700', '#d2d200', '#baba00', '#a6a600', '#8e8e00', '#797900', '#656500', '#dbdbdb', '#d2d2d2', '#cacaca', '#c2c2c2', '#bababa', '#b2b2b2', 
        '#aaaaaa', '#a6a6a6', '#9e9e9e', '#969696', '#8e8e8e', '#868686', '#7d7d7d', '#757575', '#6d6d6d', '#656565', '#5d5d5d', '#595959', '#515151', '#494949', '#414141', '#393939',
        '#313131', '#282828', '#202020', '#181818', '#141414', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',]

# Create evenly spaced levels for the color map ranging from -109 to 56
levels = np.linspace(-109, 56, num=len(cmap))

# Establish a boundary norm which maps values to intervals within the color map
norm = plt.cm.colors.BoundaryNorm(levels, len(levels))

# Create a ListedColormap object using the custom color map
# Your code goes here:


```

```python
# Create a figure with a specified size
# Your code goes here:



# Add a subplot to the figure
# Your code goes here:



# Display the 'CMI' variable data as an image, setting the color range and custom colormap
# Your code goes here:


```

```python
# Import the ticker module from matplotlib for customizing axis ticks
# Your code goes here:



# Import cartopy's coordinate reference system submodule for map projections
# Your code goes here:


```

```python
# Access the 'goes_imager_projection' variable from the dataset to get projection information
# Your code goes here:


```

```python
# Retrieve the projection variable from the dataset
# Your code goes here:



# Extract the satellite height from the projection variable
# Your code goes here:



# Get the longitude of the projection origin (central longitude)
# Your code goes here:



# Obtain the values for the semi-major and semi-minor axes of the Earth's ellipsoid
# Your code goes here:



# Determine the sweep angle axis (orientation of the satellite)
# Your code goes here:


```

```python
# Scale the x and y coordinates by the satellite height to get actual distances
# Your code goes here:



# Determine the number of lines (rows) and columns in the data based on y and x dimensions
# Your code goes here:



```

```python
# Create a figure with a specified size
# Your code goes here:
fig = 

# Set up a globe model using the semi-major and semi-minor axes values
# Your code goes here:
globe = 

# Initialize a geostationary projection using the central longitude and satellite height
# Your code goes here:
geos = 


# Add a subplot to the figure with the specified geostationary projection
# Your code goes here:
ax = 


# Display the 'CMI' variable data as an image with custom extent and colormap, using the geostationary projection
ir_img = ax.imshow(ncx['CMI'].data, origin='upper', extent=(x.min(), 
                            y.min(), x.max(), y.max()), cmap="Greys_r", transform=geos)
```

```python
# Import the glob module to find all the pathnames matching a specified pattern
# Your code goes here:


```

```python
# Define the directory path containing the .nc (netCDF) files
fllst = 'Input_data\ABI-L2-CMIPC\s20180471917'

# Use glob to retrieve a list of all .nc files in the specified directory
# Your code goes here:



# Display the list of .nc files
# Your code goes here:


```

```python
# Access the third file in the list of .nc files
# Your code goes here:


```

```python
# Open the 13th .nc file in the list using xarray
# Your code goes here:



# Display the contents of the opened dataset
# Your code goes here:


```

```python
# Create a figure with a specified size
# Your code goes here:



# Set up a globe model using the semi-major and semi-minor axes values
globe = ccrs.Globe(ellipse='sphere', semimajor_axis=semi_major, semiminor_axis=semi_minor)

# Initialize a geostationary projection using the central longitude and satellite height
geos = ccrs.Geostationary(central_longitude=central_lon, satellite_height=sat_h, sweep_axis=sweep, globe=globe)

# Add a subplot to the figure with the specified geostationary projection
ax = fig.add_subplot(1, 1, 1, projection=geos)

# Display the 'CMI' variable data from the second dataset as an image with custom extents and colormap, 
# using the geostationary projection
ir_img = ax.imshow(ncx2['CMI'].data, origin='upper', vmin=-109+273.15, vmax=56+273.15, extent=(x.min(), y.min(),                                                                             
                   x.max(), y.max()), cmap="jet_r", transform=geos)
```

```python
# Create a figure with a specified size for visualization
# Your code goes here:
fig = 

# Define a custom colormap for the image
 # A series of color codes representing different temperature ranges
cmap = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#b6ffb6', '#79ff79', '#00ff00', 
        '#ff8e8e', '#ff5151', '#ff0000', '#aa0000', '#550000', '#00ffff', '#00bef3', '#0079ca', 
        '#0028a2', '#000079', '#fbfb00', '#e7e700', '#d2d200', '#baba00', '#a6a600', '#8e8e00', 
        '#797900', '#656500', '#dbdbdb', '#d2d2d2', '#cacaca', '#c2c2c2', '#bababa', '#b2b2b2', 
        '#aaaaaa', '#a6a6a6', '#9e9e9e', '#969696', '#8e8e8e', '#868686', '#7d7d7d', '#757575', 
        '#6d6d6d', '#656565', '#5d5d5d', '#595959', '#515151', '#494949', '#414141', '#393939',
        '#313131', '#282828', '#202020', '#181818', '#141414', '#000000', '#000000', '#000000', 
        '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',]

# Create a range of levels corresponding to the colors in the custom colormap
# Your code goes here:
levels = 

# Set up a normalization scheme based on the defined levels
# Your code goes here:
norm = 


# Create a ListedColormap object with the custom colormap
# Your code goes here:
irmap = 

# Set up a globe model using the semi-major and semi-minor axes values
# Your code goes here:
globe = 

# Initialize a geostationary projection using the central longitude and satellite height
# Your code goes here:
geos = 

# Add a subplot to the figure with the specified geostationary projection
# Your code goes here:
ax = 


# Display the 'CMI' variable data from the second dataset as an image with custom extents and colormap, 
# using the geostationary projection
ir_img = ax.imshow(ncx2['CMI'].data, origin='upper', vmin=-109+273.15, vmax=56+273.15, extent=(x.min(), 
                                                y.min(), x.max(), y.max()), cmap=irmap, transform=geos)
```

```python
# Initialize a figure with a specified size (12 inches by 12 inches)
# Your code goes here:
fig = 

# Custom colormap defined by specific color codes, likely representing different data ranges or intensities
cmap = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#b6ffb6', '#79ff79', '#00ff00', 
        '#ff8e8e', '#ff5151', '#ff0000', '#aa0000', '#550000', '#00ffff', '#00bef3', '#0079ca', 
        '#0028a2', '#000079', '#fbfb00', '#e7e700', '#d2d200', '#baba00', '#a6a600', '#8e8e00', 
        '#797900', '#656500', '#dbdbdb', '#d2d2d2', '#cacaca', '#c2c2c2', '#bababa', '#b2b2b2', 
        '#aaaaaa', '#a6a6a6', '#9e9e9e', '#969696', '#8e8e8e', '#868686', '#7d7d7d', '#757575', 
        '#6d6d6d', '#656565', '#5d5d5d', '#595959', '#515151', '#494949', '#414141', '#393939',
        '#313131', '#282828', '#202020', '#181818', '#141414', '#000000', '#000000', '#000000', 
        '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000',]

# Create an array of levels corresponding to the custom colormap
# Your code goes here:
levels = 

# Establish a normalization rule using the defined levels for consistent data representation
# Your code goes here:
norm = 

# Create a colormap object from the custom list of colors
# Your code goes here:
irmap = 

# Define a globe model, considering Earth's shape as a sphere with given major and minor axes
# Your code goes here:
globe = 

# Set up a geostationary projection using satellite parameters
# Your code goes here:
geos = 

# Add a subplot to the figure using the geostationary projection
# Your code goes here:
ax = 

# Display the satellite data (CMI variable from ncx2) as an image in the subplot
# The 'origin' at 'upper' signifies the origin point of the coordinate system
# 'vmin' and 'vmax' set the data value limits for color mapping
# The 'extent' specifies the display boundaries in data coordinates
# The colormap 'irmap' is used for coloring, and 'transform' aligns the data with the specified projection
ir_img = ax.imshow(ncx2['CMI'].data, origin='upper', vmin=-109+273.15, vmax=56+273.15, extent=(x.min(), 
                                                y.min(), x.max(), y.max()), cmap=irmap, transform=geos)

# Set the extent of the map display to specific longitude and latitude limits

# Your code goes here:
                                                 # Set the map display boundaries
```
