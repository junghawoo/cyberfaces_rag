---
title: "Baseflow separation analysis"
unit_id: 105
course_id: 4
level: "Foundation"
slug: baseflow-separation-analysis
is_course: 0
---

# Baseflow Separation Analysis

This unit covers hydrological baseflow separation techniques for decomposing streamflow into direct (surface) runoff and baseflow components. Prepared by Jibin Joseph and Venkatesh Merwade (School of Civil Engineering, Purdue University) as part of FAIR Science in Water Resources (Spring 2020). Contact: vmerwade@purdue.edu.

## Objective

Determine baseflow from observed hydrographs to isolate direct surface runoff from excess rainfall. In perennial/continuous flow regimes (humid climates), non-varying baseflow occurs during rainless periods due to infiltrated water from previous rainfall events and groundwater flow through watershed. Separating baseflow from total streamflow yields direct runoff (total flow minus baseflow) needed for analyzing current rainfall event impacts. Discharge hydrographs show both direct runoff (quick response) and baseflow (slow response) components.

## Baseflow Separation Methods

**Method 1: Arnold et al. (1995, 1999) - Digital Filter Approach**

Uses signal analysis/processing digital filter technique. Filter equation:

qt = β·qt-1 + (1+β)/2·(Qt - Qt-1)

where:
- qt = filtered surface runoff (quick response) at time step t (one day)
- Q = original streamflow
- β = filter parameter (0.925)

Baseflow bt = Qt - qt

Implementation: Filters passed over streamflow data three passes (forward, backward, forward) depending on user-selected baseflow estimates. Each pass reduces baseflow percentage of total flow. References: Arnold & Allen (1999, 1995); Arnold et al. (published Ground Water vol 33(6)).

**Method 2: Eckhardt (2005) - Recursive Digital Filtering**

Special separation technique involving recursive digital filtering of hydrographs. Partitions streamflow into direct runoff and baseflow:

yk = fk + bk

where:
- y = total streamflow
- f = direct runoff  
- b = baseflow
- k = time step number

General form expressed with filter parameter (α) and BFImax (maximum baseflow index):

bk = [(1 - BFImax) × α × bk-1 + (1 - α) × BFImax × yk] / [1 - α × BFImax]

Parameters: α = 0.98, BFImax = 0.8 (long-term ratio baseflow to total streamflow, always <1). Reference: Eckhardt (2005, Hydrological Processes 19(2): 507-515).

## Data Source

Daily streamflow obtained from USGS NWIS interface: https://waterdata.usgs.gov/nwis/sw. Tutorial automates data retrieval via Python hydrofunctions library. Jupyter notebook baseflow.ipynb provided.

## Practical Implementation Workflow

**Python Libraries Required**: hydrofunctions (hf), pandas (pd), numpy (np), matplotlib.pyplot (plt).

**Analysis Inputs**: USGS station code (string), start date (YYYY-MM-DD format), end date (YYYY-MM-DD format). One-year period recommended for hydrograph visualization clarity.

**Example Case Study**: Wabash River at Lafayette, IN (Station 03335500), period 2017-01-01 to 2017-01-31. Expected mean baseflow: 7121.417 ft³/s (Arnold method), 10941.493 ft³/s (Eckhardt method).

**Key Steps**:

1. Define AR_baseflow() and EK_baseflow() Python function blocks for both methods (provided).
2. Create cell prompting user USGS station code, start/end dates; assign to variables USGS_StationCode, Start_Date, End_Date.
3. Use hydrofunctions to download data: `data = hf.NWIS(USGS_StationCode, 'dv', Start_Date, End_Date)` then `data.get_data()`.
4. Check data using `data.df().head()` (shows first 5 rows).
5. Store data in pandas DataFrame; drop qualifier column; rename discharge column from long name (e.g., "USGS:03335500:00060:00003") to "Total_Runoff" for handling. Parameter code 00060 = Discharge (cfs), stat code 00003 = daily mean.
6. Plot total discharge hydrograph using pyplot without baseflow separation.
7. Apply AR_baseflow and EK_baseflow functions to separate baseflow; verify consistency with mean value checks.
8. Plot discharge hydrograph showing total runoff and two baseflow curves from both methods.

## Homework Assignment

1. Separate baseflow using both methods for Cedar Creek (Station 04180000), March 1, 2019 to May 31, 2019.
2. Plot total discharge hydrograph for Cedar Creek.
3. Plot total discharge hydrograph showing two baseflow curves (Arnold and Eckhardt methods).
4. Compute mean baseflow values (cfs) using both methods.
5. Write code computing total streamflow volume, direct runoff volume, and baseflow volume for specified period in cubic meters.

**Deliverable**: PDF document with items 2-5 (due April 2, 2020, 5pm).

## Summarized attachments
- **Baseflow Separation** (baseflow_separation.pdf, file): Tutorial document by Jibin Joseph and Venkatesh Merwade describing baseflow separation methods including Arnold et al digital filter technique and Eckhardt recursive digital filtering approach with applications to Wabash River streamflow data using USGS station 03335500 from 2017.
- **Jupyter Notebook Exercise** (https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP2/Coursepage_DP2_baseflow_v03.ipynb, notebook): Interactive notebook implementing baseflow separation using hydrofunctions to download USGS streamflow data and apply both AR and EK baseflow separation methods with visualization of discharge hydrographs showing separated baseflow components.

## External Resources

**GitHub Repository**: https://github.com/PurdueCyberTraining/fairclimatewater/blob/main/DP2/Coursepage_DP2_baseflow_v03.ipynb

**Hydrograph Example**: ResearchGate figure showing simple graphical baseflow separation methods (https://www.researchgate.net/figure/Examples-of-simple-graphical-base-flow-separation-methods_fig6_228905789)

## Technical References

- Arnold, J.G., Allen, P.M. (1999). Automated methods for estimating baseflow and groundwater recharge from streamflow records. Journal of the American Water Resources Association, 35(2): 411-424.
- Arnold, J.G., Allen, P.M., Muttiah, R., Bernhardt, G. Automated baseflow separation and recession analysis techniques. Ground Water, 33(6): 1010-1018.
- Eckhardt, K. (2005). How to construct recursive digital filters for baseflow separation. Hydrological Processes: An International Journal, 19(2): 507-515.

## Key Concepts

- Streamflow decomposition (direct runoff vs. baseflow)
- Groundwater contribution quantification
- Digital filter signal processing hydrological applications
- Recursive filtering algorithms
- Hydrograph analysis and interpretation
- USGS NWIS data access and Python automation
- Comparative method evaluation
