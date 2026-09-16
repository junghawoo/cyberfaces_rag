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

Advanced module on satellite data for dynamic weather visualization. Prepared by Mohamed Abdelkader, Jorge Bravo, Marouane Temimi (Civil, Environmental, and Ocean Engineering Department, Stevens Institute of Technology, mabdelka@stevens.edu) and Jibin Joseph (School of Civil Engineering, Purdue University). Part of FAIR Science in Climate.

Objective: Enhance participants' capabilities in employing satellite data for dynamic weather visualization; learn to manipulate, analyze, and animate geospatial datasets; create visual representations of weather patterns; enhance scientific understanding and data presentation skills.

Learning structure: Introduction to Tools and Techniques (foundational understanding); Weather Animation Using HydroEstimator Data (precipitation mapping and animation, rainfall movement/intensity); Weather Animation Using GEOS-R Data (atmospheric conditions visualization, cloud movements, meteorological phenomena animation).

Instructions: Start with Introduction to Tools and Techniques notebook; progress sequentially; execute provided code and adjust parameters; refer to solution PDFs for detailed explanations; apply techniques to different datasets/parameters.

Lecture materials: Jupyter Notebook (GitHub: https://github.com/MAbdelkader94/Advancing-Weather-Monitoring-with-Animation-Techniques/blob/main/Lecture1__Introduction%20to%20Tools%20and%20Techniques.ipynb).

Python libraries: matplotlib (animation module, FuncAnimation, ArtistAnimation), numpy, IPython.display (HTML module). Animation techniques: FuncAnimation (frame-by-frame updates with init_func and animate functions); ArtistAnimation (compile image list into animation). Example: sine wave animation (100 frames, 20ms interval, x-axis 0-2, y-axis -2 to 2); 2D function animation (60 frames, 50ms interval, f(x,y)=sin(x)+cos(y), x/y from 0 to 2π).

Hydro-Estimator (HE) rainfall estimates: Operational since 2002 via NOAA OSPO (https://www.ospo.noaa.gov/Products/atmosphere/ghe/). Uses infrared brightness temperatures to identify rainfall regions and retrieve rainfall rate; incorporates NCEP GFS model fields (moisture availability, evaporation, orographic modulation, thermodynamic profile). Estimated every 15 minutes for CONUS using GOES data; global estimates using METEOSAT, MTSAT satellites; updated every 30 minutes. Products: instantaneous rain rates, 1-hour/3-hour/6-hour/24-hour/multi-day precipitation accumulations; global composites; CONUS product loops; monitoring product loops; algorithm descriptions; validation data; IPT members; related links.

## Summarized attachments
- **Instructions** (Instructions.pdf, file): PDF tutorial on advancing weather monitoring with animation techniques prepared by Mohamed Abdelkader, Jorge Bravo, and Marouane Temimi (Stevens Institute of Technology) and Jibin Joseph (Purdue University). Covers introduction to tools and techniques, weather animation using HydroEstimator data for precipitation mapping, and GEOS-R data for atmospheric visualization. Includes step-by-step instructions for executing exercises, adjusting parameters, consulting solution PDFs, and applying techniques to new datasets.
- **Advancing.png** (Advancing.png, image): Image showing the title "Advancing Weather Monitoring with Animation Techniques."
- **Lecture Materials** (github.com/MAbdelkader94/Advancing-Weather-Monitoring-with-Animation-Techniques, notebook): Jupyter Notebook (Lecture 1 - Introduction to Tools and Techniques) demonstrating weather animation creation using matplotlib animation module (FuncAnimation, ArtistAnimation), numpy, and IPython.display. Examples include sine wave animation (100 frames, 20ms intervals) and 2D function animation (60 frames, 50ms intervals) showing animation techniques for geospatial data visualization.
