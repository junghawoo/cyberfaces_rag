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

Data 101 for Machine Learning beginner-level workshop. Sponsored by Purdue's Women in HPC (WHPC) group. Presenter: Sarah Rodenbeck, Senior Research Data Scientist. Prerequisites: none. GitHub: https://github.com/srodenbeck/DataPreparationWorkshop.git.

Learning outcomes: Understand data's role in ML/data science; understand data types/collection; exploratory data analysis (EDA) considerations; basic Pandas data processing.

Topics: Types of data (structured/unstructured), Data collection, Basic Pandas, EDA considerations.

Data types: Structured (organized tables/databases) vs Unstructured (images, text, video); Labeled (with annotations) vs Unlabeled; Supervised (labeled, uses ground truth) vs Unsupervised (unlabeled clustering, anomaly detection).

Machine learning context: Model development cycle; intended model dictates data needs; available data dictates possible models.

Data annotation: Natural collection (test results), pre-existing labeled data (Kaggle), or annotation process. Best practices: clear guidelines, alignment meetings, pre-test calibration, inter-annotator accuracy assessment, tools (Doccano open-source).

Data annotation challenges: Inconsistent labeling, false positive vs false negative trade-offs, tedious/error-prone process, "garbage in garbage out." Balance false positives/negatives based on use case.

Data preprocessing (80% of data scientist's time): Missing data handling (delete rows with missing labels, interpolate for time series), outlier detection (use case dependent), anonymization (delete/substitute identifiable info), standardize categories, rename columns, data encoding, feature engineering, binning, feature selection/dimensionality reduction.

Dataframes: Python Pandas structures with data and metadata; 2D organization; no size limitations (unlike Excel).

Data splitting: Training (70%), Validation (20%), Test (10%); ensures model evaluation with unseen data.

Exploratory Data Analysis (EDA): Understand data characteristics before training; identify issues; select appropriate model. Common aspects: average/median/min/max values, column correlations, data quality trends, unnecessary columns, null/outlier analysis, visualization, bias identification.

Data bias: Systematic unfairness in data representation; can affect model fairness.

Pandas operations: import pandas, read_csv (load data), concat (merge dataframes), drop_duplicates, merge (join on values), info (summary), filtering, dropna/fillna (null handling), describe (statistics), hist (distribution), standardize (mean=0, std=1), normalize (0-1 range), train_test_split (sklearn).

Visualization libraries: matplotlib, seaborn.

Key takeaway: Data preparation often takes longer than model development; quality of preparation directly impacts outcome quality.

## Summarized attachments
- **Intro to Data and Data Processing** (Intro to Data and Data Processing.pdf, file): PDF presentation by Sarah Rodenbeck, Senior Research Data Scientist, for Purdue Women in HPC "Data 101 for Machine Learning" workshop. Covers data basics (structured/unstructured, labeled/unlabeled, supervised/unsupervised), data annotation (guidelines, calibration, inter-annotator agreement, Doccano tool), data preprocessing challenges (missing data, outliers, anonymization, standardization, feature engineering), model development cycle, data splitting (70/20/10), exploratory data analysis (EDA) with statistics and visualization, data bias identification, and Pandas operations for data manipulation (read_csv, concat, drop_duplicates, merge, dropna, fillna, describe, visualization).
