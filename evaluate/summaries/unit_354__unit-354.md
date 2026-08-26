---
title: "Unit 354"
unit_id: 354
---

# Unit 354

Spatial Clustering tutorial for geospatial analysis. Teaching time: 100 minutes, exercises: 1. Core content from cluster.md lesson file.

Learning objectives: Understand spatial clustering concept; prepare point data for clustering; apply K-Means, Hierarchical Clustering, and DBSCAN in Python; visualize clustering results on scatterplots and maps.

Questions addressed: What is spatial clustering and why use it? How to perform basic clustering on geographic point data? How do algorithms K-Means, Hierarchical Clustering, and DBSCAN differ?

Spatial clustering identifies patterns in point distribution: geographic hotspots, proximity-based grouping, high/low density regions, clustered/dispersed/random patterns, spatial relationships in social/environmental/urban data. Applications: public health (disease outbreaks), crime analysis, ecology, urban planning, environmental monitoring, archaeology.

Clustering algorithms comparison:
- K-Means: simple, fast; best for well-separated circular clusters; requires knowing k value
- Hierarchical Clustering: produces dendrogram visualization; useful for unknown k, multi-scale grouping, irregular shapes
- DBSCAN: finds irregular shapes and noise; ideal for spatial hotspots and natural patterns

Python libraries: pandas, geopandas, matplotlib, sklearn (KMeans, AgglomerativeClustering, DBSCAN), scipy.

Workflow: Load point data from CSV (lon/lat columns); visualize raw points via scatter plot; prepare coordinates (df[['lon', 'lat']]). K-Means: fit_predict() with n_clusters parameter, color by kmeans_label. Hierarchical (AgglomerativeClustering): build clusters step-wise, fit_predict() with n_clusters. DBSCAN: density-based, eps (distance threshold) and min_samples parameters, labels=-1 indicate noise/outliers.

DBSCAN math: density = neighbors / π*ε²; point belongs to cluster if ≥min_samples neighbors within distance ε; higher density regions form clusters.

Challenges: Load own spatial coordinates; apply K-Means and DBSCAN; compare results (DBSCAN better for irregular patterns); adjust DBSCAN eps parameter (larger eps=larger clusters, smaller eps=more clusters/noise). Visualization with colormaps (tab10, viridis, Accent).

Beginner lesson: Introduction to Spatial Clustering using Crime Datasets (available on Google Colab: https://colab.research.google.com/github/SpatialTurn/DataCollection-Notebooks/blob/main/Census/spatialclustering.ipynb). Advanced lesson: to be added.

## Summarized attachments
- **Spatial Clustering** (cluster.md, md): Markdown lesson file on spatial clustering covering concepts, importance, and applications. Includes learning questions and objectives on understanding spatial clustering, preparing point data, and applying K-Means, Hierarchical Clustering, and DBSCAN algorithms in Python. Provides algorithm comparison table (K-Means for well-separated circular clusters, Hierarchical for multi-scale grouping, DBSCAN for irregular shapes and hotspots), code examples using pandas, geopandas, matplotlib, and sklearn libraries.
- **Introduction to Spatial Clustering using Crime Datasets** (colab.research.google.com/github/SpatialTurn/DataCollection-Notebooks, notebook): Google Colab beginner Jupyter Notebook demonstrating spatial clustering techniques on crime datasets with explanations of K-Means, Hierarchical, and DBSCAN algorithms.
