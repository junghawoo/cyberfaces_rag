---
title: "Justice in Data: Coding practice for ML"
unit_id: 146
course_id: 10
level: "Foundation"
slug: justice-in-data-coding-proctice-for-ml
is_course: 0
---

# Justice in Data: Coding practice for ML

Hands-on machine-learning coding module from the Justice in Data bootcamp. Presenters: Steven Tanner McCullough (PhD Student Researcher), Jessica Eisma, PhD (Assistant Professor), and June Young Park, PhD (Assistant Professor). Lecture content spans (1) Introduction to ML, (2) ML algorithms — supervised learning (Decision Tree, Nearest Neighbors), unsupervised learning (k-means clustering), reinforcement learning (Markov Decision Process) — and (3) a coding practice using building energy data to learn classification algorithms (KNN and decision tree).

## Extracted resources (local files)

### Coding practice for ML
*Source file:* `Lecture_Friday_3_final.pdf` — Slides for the coding exercise. Objective: classify building location (urban / urban cluster / rural, coded 1/2/3) from energy consumption patterns using the DOE RECS dataset (https://www.eia.gov/consumption/residential/). Train set: 4,000 buildings; hidden test set: 1,686 buildings; 26 electricity-usage features in kilowatthours (2015): KWHSPH (space heating), KWHCOL (air conditioning), KWHWTH (water heating), KWHRFG/KWHRFG1/KWHRFG2 (refrigerators), KWHFRZ (freezers), KWHCOK (cooking), KWHMICRO (microwaves), KWHCW (clothes washers), KWHCDR (clothes dryers), KWHDWH (dishwashers), KWHLGT (lighting), KWHTVREL/KWHTV1/KWHTV2 (televisions), KWHAHUHEAT/KWHAHUCOL (air handlers), KWHEVAPCOL (evaporative coolers), KWHCFAN (ceiling fans), KWHDHUM (dehumidifiers), KWHHUM (humidifiers), KWHPLPMP (pool pumps), KWHHTBPMP/KWHHTBHEAT (hot tub pumps/heaters), KWHNEC (not elsewhere classified). Eight major steps: read libraries, read data, split data by features and target, train original models (decision tree, KNN), cross-validate, tune the KNN model, test the final model on unseen test data, report final results. Students open the Jupyter notebook `ml_python_empty.ipynb` on MyGeoHub.

## Fetched resources (external URLs)

### Coding Practice for Machine Learning Pre-Survey (link)
QuestionPro survey at utaedu.questionpro.com (TakeSurvey link).

### Coding Practice for Machine Learning Recording (link)
YouTube recording (watch?v=mIUcvsFFj3E) — a full walkthrough of the notebook. Recaps supervised (KNN, decision tree; classification/regression, needs labeled output), unsupervised (k-means, pattern learning), and reinforcement learning (reward from environment; smart lighting system learning occupant comfort while saving energy) in the built environment. Code walkthrough: imports pandas (pd), numpy (np), matplotlib.pyplot (plt), seaborn (sns), collections, requests; downloads `data_all.csv`, `data_test.csv`, `data_train.csv` from a repository URL via a for-loop (echoing the earlier Building Genome / data-access example); `pd.read_csv`, `data.head()`, `len(data)` (4000 rows); feature/target split with `data.iloc` (first 26 columns) and `y = data.location`, class counts via `collections.Counter` (~2,759 urban, ~400 urban cluster, ~840 rural); `from sklearn import tree, neighbors` — `tree.DecisionTreeClassifier()` and `neighbors.KNeighborsClassifier()` (default n_neighbors=1), `.fit(X, y)`; cross-validation with `sklearn.model_selection.cross_validate` (scoring='precision_macro', cv=5 then 10, return_train_score=False), both models scoring ~0.39; hyperparameter tuning with `GridSearchCV` over `n_neighbors: range(1, 1001, 10)`, plotting mean_test_score with `plt.scatter`, yielding best_params_ n_neighbors=391 and best_score_ ~0.4426; final evaluation with `sklearn.metrics` `accuracy_score` and `confusion_matrix` on the hidden test set — original KNN ~0.59 accuracy vs tuned KNN ~0.69, with a 3x3 confusion matrix interpreted row-by-row (e.g., 881 urban buildings correctly classified; tuned model predicts no urban-cluster buildings, showing why accuracy alone is misleading). Q&A covers bias-variance tradeoff, underfitting/overfitting, why cross-validation (split-and-repeat, 5-fold/10-fold, train/validation/final-test separation, e.g., 700/300 splits of 1,000 with 100 held out), Jupyter Tab-completion to discover scikit-learn estimators (DecisionTreeRegressor, ExtraTreeClassifier, KNeighborsRegressor, NearestCentroid, SVM, MLP neural networks), confusion-matrix size scaling with number of classes, improving accuracy via finer grid search, and adapting the notebook framework to other CSV datasets/features/models. The completed Jupyter notebook is uploaded to MyGeoHub.

## Summarized attachments

- **Coding practice for ML** (`Lecture_Friday_3_final.pdf`, PDF): Slides for hands-on machine learning coding practice led by Steven Tanner McCullough, Jessica Eisma, and June Young Park. Uses DOE RECS building energy dataset (4,000 training + 1,686 hidden test buildings) with 26 electricity-usage features (space heating, air conditioning, water heating, refrigerators, cooking, lighting, televisions, HVAC, pools, etc. in kilowatthours). Objective: classify building location (urban/urban cluster/rural) from energy consumption patterns. Eight major steps: read libraries, read data, split features/target, train models (Decision Tree, KNN), cross-validate, tune KNN, test on unseen data, report results. Jupyter notebook `ml_python_empty.ipynb` on MyGeoHub.

- **Coding Practice for Machine Learning Pre-Survey** (QuestionPro link, survey): Pre-workshop survey at utaedu.questionpro.com for participants to establish baseline understanding before the coding exercise.

- **Coding Practice for Machine Learning Recording** (YouTube watch?v=mIUcvsFFj3E, video): Full video walkthrough of the notebook exercise including supervised/unsupervised/reinforcement learning overview, code execution walkthrough with data loading, train-test split, model training (DecisionTreeClassifier, KNeighborsClassifier), cross-validation (cv=5/10 precision_macro scoring), hyperparameter tuning (GridSearchCV over n_neighbors 1-1001 step 10, optimal n_neighbors=391), and final accuracy/confusion matrix evaluation (original KNN 0.59, tuned KNN 0.69). Includes live participant questions on bias-variance, underfitting/overfitting, cross-validation methodology, and adapting the framework to new datasets.
