---
title: "Advancing Weather Monitoring with Animation Techniques"
unit_id: 235
course_id: 0
level: "Developer"
slug: advancing-weather-monitoring-with-animation-techniques
is_course: 0
objectives:
  - "Weather Animation Using HydroEstimator Data"
  - "Weather Animation Using GEOS-R Data"
---

# Advancing Weather Monitoring with Animation Techniques

**Description:** This advanced module aims to enhance the capabilities of participants in employing satellite data for dynamic weather visualization. Participants will learn to manipulate, analyze, and animate geospatial datasets to create visual representations of weather patterns, enhancing both scientific understanding and data presentation skills.

## Extracted resources (local files)

### Instructions
*Source file:* `Instructions.pdf`  ·  *type:* file

Advancing Weather Monitoring with Animation 
Techniques  
 
Prepared by  
Mohamed Abdelkader1, Jorge Bravo1, Marouane Temimi1, and Jibin Joseph2  
1Civil, Environmental, and Ocean Engineering Department, Stevens Institute of 
Technology 
2School of Civil Engineering, Purdue University 
mabdelka@stevens.edu 
 
FAIR Science in Climate 
 
 
Objective 
This advanced module aims to enhance the capabilities of participants in employing satellite data 
for dynamic weather visualization. Participants will learn to manipulate, analyze, and animate 
geospatial datasets to create visual representations of weather patterns, enhancing both scientific 
understanding and data presentation skills. 
 
Overview of Steps 
Introduction to Tools and Techniques: Participants will familiarize themselves with the key 
tools and computational techniques necessary for handling and processing satellite imagery. 
Weather Animation Using HydroEstimator Data: This section delves into using 
HydroEstimator data for precipitation mapping and animation, illustrating the movement and 
intensity of rainfall. 
Weather Animation Using GEOS-R Data: Focuses on employing GEOS-R satellite data to 
visualize atmospheric conditions in high resolution, highlighting techniques for animating cloud 
movements and other meteorological phenomena. 
 
Instructions 
- Navigating the Notebooks: Start with the "Introduction to Tools and Techniques" to build a 
foundational understanding. Progress through the notebooks sequentially to develop a 
comprehensive skill set in satellite data animation. 
- Executing the Exercises: Carefully follow the step-by-step instructions in each notebook. 
Execute the provided code and adjust parameters to explore different visual outputs. 
- Consulting the PDF Solutions: Refer to the solution documents for detailed explanations and 
guidance on the expected results. These documents serve as a vital resource for verifying 
outcomes and understanding complex concepts: 
- Applying Skills to New Data: Encouraged to apply the learned techniques to different datasets 
or parameters to explore further and enhance learning. 
- Resource Utilization: Leverage additional resources linked within the notebooks and PDFs to 
expand your knowledge and troubleshooting capabilities.

## Image text (OCR)

### `Advancing.png`
< , ADDVANCING Wen;

a
THERMONTORNG
+] WI ANIIMARTION RMON NIQUES

## Fetched resources (external URLs)

### Lecture Materials (notebook)
*URL:* https://github.com/MAbdelkader94/Advancing-Weather-Monitoring-with-Animation-Techniques/blob/main/Lecture1__Introduction%20to%20Tools%20and%20Techniques.ipynb

## Creating Weather Animation Part 1 - Introduction to Tools and Techniques

```python
# Enable inline plotting for animations and interactive visualizations in Jupyter Notebooks.
%matplotlib inline

# Import essential libraries for numerical operations and plotting.
# You code goes here


#####################

# Import the animation module from matplotlib to create dynamic visualizations and the HTML module to display animations in the notebook.
# You code goes here


#####################

# Create a figure and a single subplot with axes. This will be the canvas for our animation.
# You code goes here


#####################

# Set the x and y axis limits of the plot. These limits provide the range of data to be displayed.
ax.set_xlim((0, 2))  # x-axis from 0 to 2
ax.set_ylim((-2, 2))  # y-axis from -2 to 2, useful for showing full amplitude of sine wave

# Initialize an empty line object with line width 2. This line will be updated in the animation.
line, = ax.plot([], [], lw=2)

# Define the initialization function for the animation. This function clears previous frames' data, setting the stage for new data.
def init():
    line.set_data([], [])  # Clear line data
    return (line,)

# Define the animation function which updates the content of the plot. This function will be called for each frame of the animation.
def animate(i):
    x = np.linspace(0, 2, 1000)  # Generate x values evenly spaced between 0 and 2
    y = np.sin(2 * np.pi * (x - 0.01 * i))  # Generate sine wave y values, creating a phase shift dependent on the frame
    line.set_data(x, y)  # Update the line's data for the new frame
    return (line,)

# Create an animation object. This object manages the dynamic redrawing of the line plot for each frame of the animation.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)  # 100 frames, updating every 20 milliseconds, with blitting to improve performance.

# Display the animation in HTML format within the Jupyter Notebook to ensure it plays seamlessly.
# You code goes here


#####################
```

_result:_
```
<IPython.core.display.HTML object>
```

_result:_
```
<Figure size 640x480 with 1 Axes>
```

```python
# Import necessary libraries for numerical computations and visualizations.
# You code goes here


#####################

# Create a matplotlib figure object. This figure will serve as the container for our animation.
fig = plt.figure()

# Define a function 'f' that takes x and y arrays as input and returns the sum of their sine and cosine.
# This function generates a dynamic pattern by combining two periodic functions, which we'll visualize.
def f(x, y):
    return np.sin(x) + np.cos(y)

# Generate arrays of x and y values that range from 0 to 2*pi.
# These arrays will be used as inputs to the function 'f' to create our visualization's grid.
x = np.linspace(0, 2 * np.pi, 120)  # 120 points along the x-axis
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)  # 100 points along the y-axis, reshaped to a column vector

# Initialize a list to store each frame of the animation.
# Each frame will be an image created by plotting the function 'f'.
ims = []

# Loop through 60 iterations to generate 60 frames for the animation.
# In each iteration, slightly shift x and y to create a moving effect in the resulting plot.
for i in range(60):
    x += np.pi / 15.  # Increment x slightly to shift the sine function horizontally.
    y += np.pi / 20.  # Increment y slightly to shift the cosine function vertically.
    # Calculate the function 'f' using the updated x and y, and create an image from the result.
    im = plt.imshow(f(x, y), animated=True)  # 'imshow' plots the 2D array returned by 'f'.
    ims.append([im])  # Add the resulting image to the list of frames.

# Close the plot to prevent it from showing statically in the output.
plt.close()

# Create an animation object using ArtistAnimation. This object will compile our list of images into a continuous animation.
# 'interval' sets the speed of the animation (50 ms between frames), and 'blit=True' optimizes the rendering.
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

# Display the animation within the Jupyter Notebook as an HTML5 video.
# This method allows the animation to be played interactively in the notebook.
# You code goes here


#####################
```

_result:_
```
<IPython.core.display.HTML object>
```

### Operational Hydro-Estimator Satellite Rainfall Estimates (link)
*URL:* https://www.ospo.noaa.gov/Products/atmosphere/ghe/

# Hydro-Estimator Rainfall Estimates | OSPO

Hydro-Estimator Rainfall Estimates | OSPO
Skip to main content
Official websites use .gov
A
.gov
website belongs to an official government
								organization in the United States.
Secure .gov websites use HTTPS
A
lock
(
) or
https://
means you’ve safely connected to
								the .gov website. Share sensitive information only on official,
								secure websites.
Operational Hydro-Estimator Satellite Rainfall Estimates
Hydro-Estimator (HE) rainfall rate estimates have
            been available over the CONUS and in operational use by the National Weather Service for monitoring
            potential flash flood events since 2002. The HE algorithm uses infrared (IR) brightness temperatures to
            identify regions of rainfall and retrieve rainfall rate, while using National Centers for Environmental
            Prediction (NCEP) Global Forecast System (GFS) model fields to account for the effects of moisture
            availability, evaporation, orographic modulation, and thermodynamic profile effects. Estimates of rainfall
            from satellites can provide critical rainfall information in regions where data from gauges or radar are
            unavailable or unreliable, such as over oceans or sparsely populated regions. Recently the HE has been
            extended to the entire globe equator-ward of 60 degrees to meet user community's need for support of global
            flash flood guidance efforts.
The HE rainfall rate estimates are produced
            routinely every 15 minutes for the continental United States using the data from NOAA's Geostationary
            Operational Environmental Satellites (GOES), and also for the rest of the world using available
            geostationary data over Europe, Africa, and western Asia (METEOSAT), and eastern Asia (MTSAT). The global
            rainfall composite is then generated from those estimates from multiple satellites and updated every 30
            minutes. The operational global HE products available include instantaneous rain rates and 1-hour, 3-hour,
            6-hour, 24-hour and multi-day precipitation accumulations.
Global Product
Loops
CONUS Product
Loops
Monitoring
Product
Satellite
                Sector
Other Information
Algorithm Description
Validation
Data
IPT Members
Related Links
