---
title: "Justice in Data: Data Visualization"
unit_id: 143
course_id: 10
level: "Foundation"
slug: justice-in-data-data-visualization
is_course: 0
---

# Justice in Data: Data Visualization

Foundation-level module on visual representation of data for analysis and communication. Platform: mygeohub.org Jupyter Notebooks. Course material includes slides (Data_Visualization_V2.pdf), video lecture transcript, pre-survey, and two hands-on activities (Activity_Vis.ipynb, Activity 2).

## Fundamentals

Data visualization: field dealing with visual representation of data through graphical plotting. Effective for communicating inferences from data. Provides visual summary of data, especially crucial for large datasets (impossible to examine individually). Human mind better processes pictures/maps than lists of numbers or prose. Enables detection of trends, outliers, and non-normal distributions; informs appropriate analytical methods.

## Chart Types & Applications

**Line Graph (Line Chart)**: Visualize values over continuous period (time, distance, etc.). Single or multiple lines showing trends. Example: sales units for products A, B, C over years 2012-2019; energy use over time; streamflow time series.

**Scatter Plot**: Represent relationship between two numerical variables (independent/dependent). No relationship shows points scattered randomly; positive/negative correlations show directional patterns. Example: online advertising costs vs. e-commerce sales; streamflow at different locations; remote sensing vs. drone data.

**Bar Chart (Bar Graph)**: Represent categorical data using bars of different heights (vertical or horizontal). Compare values across categories. Example: revenue by division; land surface temperature by area type. Height represents frequency/value; width non-significant (unlike histograms).

**Histogram**: Display statistical frequency distribution of numerical data. Rectangles (colored/shaded, variable area) show frequency in successive intervals of equal size. No gaps between adjacent bars (distinguishes from bar charts). Y-axis always represents frequency measure (count, fraction). Example: exam score distribution; reveals skewness, bimodality, normality.

**Pie Chart**: Circular graph using "pie slices" showing relative sizes/percentages of data. Entire pie = 100%. Example: web traffic sources; market share by category. Human perception: easy to digest portions-of-whole relationships.

**Box Plot (Box and Whisker Plot)**: Use boxes and whiskers to depict distribution of numerical data across groups. Construction based on quartiles: Q1 (25%), Q2/median (50%), Q3 (75%). Shows central tendency, spread, skewness. Outliers plotted separately beyond whiskers. Example: rainfall distribution by location; temperature variation across sites.

**Violin Plot**: Hybrid of box plot showing distribution density. Combines box plot (median, quartiles) with probability density visualization. Wider sections indicate data concentration; tails show sparse regions. Reveals bimodal or skewed distributions not visible in box plots. Example: surface temperature distribution by land use type.

## Effective Visualization Practices

**Multi-Component Figures**: Combine multiple data types, plots, statistics within single figure for comprehensive data storytelling. Include: raw scatter + regression lines + equations + R² values; time series with confidence bands (mean ± std); spatial/temporal data overlay; drone vs. satellite comparisons. Maximizes information density without confusion; aids reader comprehension vs. flipping between separate figures.

**Colorblind-Friendly Design**: Scientific community increasingly prioritizing accessibility. Tools: colorblind simulator websites (view figures under different color-blindness types). Palette options: viridis, spectral, twilight (colorblind-friendly). Ensures non-colorblind colleagues can interpret data.

## Python Libraries

**Matplotlib**: Easy-to-use, built on NumPy arrays. Plots: scatter, line, histogram, bar, etc. Highly customizable; pairs well with pandas and NumPy. Function: plt.plot(), plt.scatter(), plt.bar(), plt.hist() with arguments for color, line width/style, marker type, font size, axis limits.

**Seaborn**: High-level interface built on Matplotlib. Provides beautiful default styles, color palettes, statistical themes. Function: sns.lineplot(), sns.scatterplot(), sns.barplot(), sns.histplot(), sns.boxplot(), sns.violinplot(). Arguments: data (DataFrame), x, y, hue (categorical coloring), palette (color scheme), style (marker/line variation).

**Bokeh**: Interactive chart visualization. Interactive legends (click_policy: hide glyphs). Hover tool detection of outliers/anomalies. Customizable.

**Plotly**: Interactive visualizations. Hover tools for data point inspection. Dropdown menus for dynamic figure customization. Visually attractive. Customizable.

## Customization & Arguments

**Color Palettes**: dark, spectral, blues, hot, twilight, viridis (colorblind-friendly), twilight_shifted. Set via palette parameter. List available: run with non-existent palette name to display error message with all supported options.

**Markers & Line Styles**: Color codes (R=red, G=green, K=black, W=white, RGB tuples); line width (varying thickness); line style (solid, dashed, dotted); marker types (circle, square, etc.). Examples: color='red', linewidth=4, linestyle='dashed'.

**Formatting**: Font size (X/Y labels, title, legend, tick marks); X/Y axis limits (zoom in/out); legend location ('upper left', 'best', 'lower center', etc.); number of legend columns; marker size; figure size; DPI (dots per inch) for export resolution (96 minimum for personal use; 600 for publications).

**Export**: plt.savefig(filename, format='jpeg', dpi=600) saves figures in JPEG, PNG, PDF, SVG formats at specified resolution.

## Hands-On Activities

**Activity 1 (Activity_Vis.ipynb)**: Load dataset (Place 1-8 temperature data, daily). Create various chart types: line plots (multiple series), scatter plots (with markers/colors), bar plots (vertical/horizontal, stacked), histograms (variable bin numbers), box plots (by category), violin plots (with/without inner box plot). Customize colors, line styles, font sizes, axis limits, legends. Compare Matplotlib vs. Seaborn syntax. Apply hue parameter for categorical coloring; use different color palettes.

**Activity 2**: Use for loops to automate multi-figure generation. Create multiple line plots on single axes. Create multiple individual plots (one per category): 8 separate line plots, 8 scatter plots, 8 bar plots. Syntax: `for i in range(8): plt.plot(x, df['place' + str(i+1)]); plt.savefig(...); plt.clf()` (clear figure between iterations). Stack chart: combine all data on single bar chart (plt.bar() automatically stacks when multiple series plotted). Application: generate research video by stitching saved PNG/JPEG sequences.

## Data Sources & References

**Example Datasets**: Fortune 500 companies (50+ years), rainfall in Indian urban centers, drone/satellite surface temperature observations, e-commerce sales vs. advertising, student exam scores, web traffic sources.

**References**:
- Pingale et al. 2014: Spatial/temporal trends of mean/extreme rainfall and temperature, 33 urban centers, Rajasthan, India. Atmospheric Research 138: 73-90.
- Naughton & McDonald 2019: Urban land surface temperature variability via drone observations. Remote Sensing 11(14): 1722.

## Learning Outcomes

Select appropriate chart type for data/story. Customize visualizations for clarity/accessibility. Implement colorblind-friendly design. Create multi-panel figures with overlapping data types. Automate figure generation via loops. Export publication-quality figures. Communicate research findings effectively through visual media.

## Summarized attachments

- **Data Visualization Slides** (`Data_Visualization_V2.pdf`, file): Comprehensive slide deck covering data visualization concepts, comparison of chart types (line, scatter, bar, histogram, pie, box, violin plots), effectiveness of presenting data through visual media rather than tabular representations, Python visualization libraries (Matplotlib, Seaborn, Bokeh, Plotly) with customization options for colors, line styles, fonts, and axis limits, and examples from energy/water resources domains.

- **Data Visualization Pre-Survey** (https://utaedu.questionpro.com/a/TakeSurvey?tt=bIrtFe6pZ/EECHrPeIW9eQ%3D%3D, survey): Web-based assessment instrument administered before the module to measure baseline understanding of data visualization principles and practices.

- **Data Visualization Recording** (https://www.youtube.com/watch?v=9uvQVIs9hrk, video lecture): Complete video lecture (transcript provided) delivered by an instructor explaining data visualization field, visual representation techniques, chart selection for different data types, Python libraries for visualization, and practical demonstrations of plotting with Matplotlib and Seaborn.

- **Activity_Vis.ipynb** (Jupyter notebook, not directly linked): Hands-on exercise notebook referenced in the lecture where students load temperature datasets, create various chart types (line plots with multiple series, scatter plots, bar charts, histograms, box plots, violin plots), customize visualization parameters (colors, line widths, font sizes, legend positions), compare Matplotlib vs. Seaborn syntax, and apply categorical coloring via hue parameters with different color palettes.
