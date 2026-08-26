---
title: "Justice in Data: Introduction to Machine Learning"
unit_id: 144
course_id: 10
level: "Foundation"
slug: justice-in-data-introduction-to-machine-learning
is_course: 0
---

# Justice in Data: Introduction to Machine Learning

Foundation bootcamp on machine learning fundamentals presented by Steven Tanner McCullough (PhD Student), Jessica Eisma (Assistant Professor), and June Young Park (Assistant Professor), taught July 2024 from South Korea across distributed participants (El Paso, Dallas, Georgia, Peru, Pakistan, Virginia, USA).

**Bootcamp Objectives & Philosophy:**
ML learning requires foundational mathematics (linear algebra, calculus, statistics, probability) plus programming (Python/R). Course introduces basic algorithms (k-nearest neighbors, decision tree, k-means clustering, Markov Decision Process reinforcement learning) as journey starting points requiring self-study beyond classroom. Focus on small data (more common in business than big data) rather than comprehensive algorithm coverage. Emphasizes learning from real-world datasets, community engagement (Reddit, Stack Overflow, GitHub), patience, and practice. ChatGPT guidance: start with basics, take courses (Coursera, edX, Udemy), read papers/books, practice with real data, join communities.

**ML Definitions & Motivation:**
Alan Turing (1950): "Why not produce a program simulating a child's learning?" Arthur Samuel (1959): ML gives computers ability to learn without explicit programming. Tom Mitchell (1997): Program learns if task performance improves with experience. Data-driven approach using experience (data) rather than hardcoded logic. DIKW Pyramid: Data (facts with no meaning) → Information (meaningful interpretation) → Knowledge (orderly synthesis) → Wisdom (appropriate applications).

**Data Understanding for ML:**
Data types: Text, Date, Binary, Ordinal, Category, Numeric. Feature engineering converts raw data into meaningful features (flags, ratios, mappings, aggregates). Building energy example: compress daily consumption profiles (850+ time points) into four letters (A-D) representing peak/trough patterns for anomaly detection and consumption categorization.

**Bias-Variance Tradeoff & Model Evaluation:**
Underfitting (high bias, too simplistic model missing relationships) vs. Overfitting (high variance, too complex model capturing noise). Split data: 70% training, 30% validation; test set kept hidden until final evaluation. Cross-validation (k-fold, usually k=5 or 10) avoids single random train-test split bias, enables repeated training/validation/testing with shuffled splits, more computationally expensive but provides stable generalization estimates.

**Classification Performance:**
Confusion matrix (binary): True Positive (TP), True Negative (TN), False Positive (FP), False Negative (FN). Accuracy = (TP+TN)/Total. Example: 155 correct (105 TP + 50 TN) out of 166 = 0.93 accuracy.

**ML Algorithms Overview:**
- Supervised Learning: Decision Tree, k-Nearest Neighbors (KNN) for classification
- Unsupervised Learning: k-means clustering
- Reinforcement Learning: Markov Decision Process

**Application Domain:** Building energy performance analysis using building energy data for KNN and decision tree implementation (afternoon breakout coding practice).

**Survey & Recording:** Pre-session survey available via questionpro.com; YouTube recording (ID: Z-ZuQ01XGRc) documents full presentation with interactive Q&A from geographically distributed attendees.

**Key Terminology:** Embedding, embeddings, feature extraction, model complexity, generalization error, training error, validation sets, holdout testing.

## Summarized attachments

- **Introduction to Machine Learning Lecture** (`Lecture_Friday_1_Final.pdf`, PDF): Foundation-level bootcamp lecture by Steven Tanner McCullough, Jessica Eisma, and June Young Park covering machine learning fundamentals, definitions (Turing, Samuel, Mitchell), DIKW pyramid, data types, feature engineering, bias-variance tradeoff, model evaluation metrics, classification performance (confusion matrices), and introduction to supervised learning (decision trees, k-nearest neighbors), unsupervised learning (k-means clustering), and reinforcement learning (Markov Decision Process) with building energy performance application.
