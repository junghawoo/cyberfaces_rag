---
title: "Data Preparation Workshop"
unit_id: 248
course_id: 0
level: "Foundation"
slug: data-preparation-workshop
is_course: 0
objectives:
  - "Learning this module enables users to preprocess raw data"
---

# Data Preparation Workshop

**Description:** Material prepared for Purdue's Women in HPC (WHPC) "Data 101 for Machine Learning" workshop. This workshop is a beginner-level discussion about data, focusing on how data fits into machine learning and data science workflows.

Topics:

Types of data
Data collection
Basic data processing with Pandas
Considerations for exploratory data analyses
Basic Pandas code, data, and a PDF of the presentation can be found in this repository.

Code, presentation, and data are from Sarah Rodenbeck's Github repository.

## Text content

### Data 101 for Machine Learning Workshop Information
This workshop is a beginner-level discussion about data, focusing on how data fits into machine learning and data science workflows. This workshop is sponsored by Purdue's Women in High-Performance Computing (WHPC) group.

Prerequisites:
* None

Topics:
* Types of data
* Data collection
* Basic data processing with Pandas
* Considerations for exploratory data analyses

## Extracted resources (local files)

### Intro to Data and Data Processing
*Source file:* `Intro to Data and Data Processing.pdf`  ·  *type:* file

DATA 101: 
INTRODUCTION 
TO DATA AND 
DATA 
PROCESSING
SPONSORED BY PURDUE 
WOMEN IN HPC
SARAH RODENBECK, SENIOR RESEARCH 
DATA SCIENTIST

Present your research
at conferences
Attend trainings
and events
Join the conversation
on Slack

OUTCOMES
Understand how data is used in machine 
learning and data science
Data types and data collection
Topics to consider when doing an Exploratory 
Data Analysis
Basic data processing using Pandas

DATA BASICS

MODEL 
DEVELOPMENT 
CYCLE
cv

WHAT IS DATA?

WHY DOES THIS MATTER?
Intended model 
dictates data 
needs 
Available data 
dictates 
possible models

STRUCTURED VS UNSTRUCTURED DATA

LABELLED VS UNLABELLED DATA
Labeled Data
Unlabeled Data
Je m’appelle Sarah =  
My name is Sarah
Je m’appelle Sarah.

SUPERVISED VS UNSUPERVISED LEARNING
• Most Machine Learning 
and Statistical Models
• Image Recognition
• Neural Machine 
Translation
• Loan Default Prediction
• Relies on Labelled Data as 
the ”ground truth”
• Data preparation and 
limited models
• Clustering for anomaly 
detection
• Dimensionality 
reduction
• Association and 
Recommender systems
• Does not require labelled 
data

SUPERVISED 
LEARNING
¡
More data preparation
¡
More performant
¡
More types of models

ON LABELED 
DATA
¡
You need a lot of labeled data 
for most ML systems!
¡
Typically on the scale of 
thousands or tens of 
thousands of data points
¡
Transfer learning reduces 
data needs but you still need 
enough to fine tune the 
model for your specific task

DATA ANNOTATION
• Some times labelled data 
is naturally collected (e.g. 
engineers marking if a test 
worked or not)
• Other times you can use 
pre-existing labelled data 
(e.g. Kaggle dataset)
• Most of the time you will 
need to go through a data 
annotation process

DATA ANNOTATION DIFFICULTIES
• Clear and consistent guidelines 
are key
• Inconsistent labelling can 
confuse the model’s training
• It can be helpful to think 
about whether false positives 
or false negatives are more 
acceptable for your model 
and advise your annotators 
to err on that side
• Annotation can be a tedious and 
error prone process but is one of 
the most important
• Garbage in, garbage out!
Coming off Zoloft is $%&@*#! weird
Does ”weird” 
count as 
experiencing a 
side-effect?
Does this count 
as a car?

BEST PRACTICES FOR DATA ANNOTATION
• If multiple annotators:
• Create common guidelines
• Hold an alignment meeting to go 
through examples together and calibrate
• Have everyone complete a pre-test by 
annotating a limited number of 
examples and assess inter-annotator 
accuracy and analyze common 
misconceptions
• Tools like Doccano (open-source) can make 
data annotation easier

DATA PRE-PROCESSING

MODEL 
DEVELOPMENT 
CYCLE

¡DATA CLEANING AND DATA 
PREPARATION ACCOUNTS FOR 
AS MUCH AS 80% OF A DATA 
SCIENTIST’S TIME

DATAFRAMES
¡ An extremely common tool used for working with data are dataframes
¡ Contains both data and metadata
¡ Dataframes are structures that organizes data into a two-dimensional data
¡ Doesn’t have size limitations like Excel!
*All provided commands in this presentation are for use with the Pandas 
DataFrames package in Python

MISSING DATA
¡ What you do with missing 
outliers depends on your 
use case and the columns
¡ If you are missing data in 
the label column you may 
be best to delete the row
¡ For other columns you may 
be able to interpolate data
¡ e.g. in a time series 
analysis you could 
average the previous 
and next data point

ACCOUNT FOR OUTLIERS
• What you do with outliers 
depends on your use case
• Are outliers important in your 
data (e.g. anomaly detection) or 
are they representative of 
someone not labelling the data 
well?
• With the annotation data 
visualized here, I might want 
to not use annotator 11’s 
data for model training

ANONYMIZE 
DATA
If you have a column with the 
subject name or identifiable 
information you can:
¡ Delete the column
¡ Substitute an 
anonymized value 
instead

DATA SETS
Training Data (70%)
Data used by the model for training
Validation Data (20%)
Used to assess model performance 
during training
Test Data (10%)
Data used after training is complete 
for evaluation metrics

OTHER POTENTIAL STEPS IN PRE-PROCESSING
• Ensure consistent descriptors/categories (e.g. ‘female’ and ‘woman’ should be 
the same)
• Rename columns
• Data encoding
• Data must be in a specific format for training.  For example, with text data 
you will need to get the word embeddings
• Feature engineering
• Using domain knowledge to manipulate raw data into a format that better 
captures key characteristics of the data 
• Binning data for easier analysis
• Feature Selection/Dimensionality reduction
• Reduces the data used to help the model identify what’s most important
• Etc…

EXPLORATORY DATA ANALYSIS

EXPLORATORY 
DATA ANALYSIS
¡Understand and summarize the 
main characteristics of a data set 
prior to model training

WHY PERFORM 
AN EDA?
Better understand data and 
data patterns
Can uncover data issues
Help select the right model for 
your data

COMMON ASPECTS 
OF AN EDA
¡ Average, median, high and low 
values for each column
¡ Relationships between columns 
(correlations)
¡ Explore data quality trends
¡ Identify unnecessary columns
¡ Null and outlier analysis
¡ Visualize data
¡ Identify data biases

VISUALIZATIONS
Recommended 
Introductory Python 
Visualization Libraries: 
•
matplotlib
•
seaborn

DATA BIAS

CONCLUSION
cv
•
Preparation for building a model 
often takes longer than building the 
model itself
•
Steps are not strictly linear
•
The quality of each of these 
preparation steps directly impacts 
the quality of your outcome

Present your research
at conferences
Attend trainings
and events
Join the conversation
on Slack

APPENDIX

GETTING STARTED WITH PANDAS DATAFRAMES
Standard import statement
Reads the specified CSV file 
into a DataFrame

COMBINE DATASETS AND REMOVE DUPLICATES
This concatenates the given 
dataframes (essentially stacks 
them on top of one another) 
Deletes duplicates and keeps only 
the first value of each duplicate

SOMETIMES YOU WANT TO MERGE DATAFRAMES ON 
CERTAIN VALUES AS WELL 
Merges df1 and df2 on the ID 
column in each and keeps all 
values

INFORMATION
Gives summary information 
about the dataframe

FILTERING DATA
Shows only data matching the 
specified condition

DROP OR FILL NULL VALUES
Deletes rows where there is a 
null value in the ‘Utilities’ 
column
Fills null values with zeroes

INFORMATION ABOUT THE DATA
Output a statistical description 
of the column
Histogram of the distribution of 
the column

STANDARDIZE/NORMALIZE DATA
Standardize data to have 
mean of 0 and standard 
deviation of 1
Normalize data so all values 
are between 0 and 1

TRAIN-VAL-TEST SPLIT
Common package for working 
with arrays
Splits the data into 
three data sets
Randomizes data 
before splitting
Specifies where the splits should 
happen (i.e. between train and val at 
the 70% and between val and test at 
90%)

## Fetched resources (external URLs)

### Data 101 for Machine Learning (notebook)
*URL:* https://github.com/srodenbeck/DataPreparationWorkshop.git

[github: could not resolve raw content]
