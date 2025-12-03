# Spatial Clustering Analysis

## 📊 Overview

Crime hotspot identification using DBSCAN and K-Means clustering algorithms on geospatial incident data to guide police patrol allocation and predict high-risk zones.

**Business Context**: Law enforcement agencies need data-driven patrol strategies to reduce response times, allocate resources efficiently, and implement predictive policing in high-crime areas.

## 🛠️ Tools & Technologies

- **Data Sources**: Synthetic crime incident records (lat/lon, type, timestamp)
- **Python Libraries**: `sklearn`, `scipy`, `pandas`, `matplotlib`, `seaborn`, `folium`
- **Methods**: DBSCAN clustering, K-Means++ initialization, Silhouette analysis, Temporal pattern detection

## 🔬 Methodology

Load crime incident data → Apply DBSCAN to identify spatial clusters with varying density → Use K-Means for hotspot centroid detection → Analyze temporal patterns (day/night, weekday/weekend) → Generate patrol zone recommendations

## 📈 Results & Insights

Identified 8 major crime hotspots using DBSCAN (eps=0.5km, min_samples=10). K-Means analysis reveals optimal 5-zone patrol division. Night-time incidents concentrated in entertainment district (42%), residential burglaries in suburbs (28%). Hotspot areas show 3-5x higher incident density than baseline.

**Visualizations**: Cluster maps, density heatmaps, temporal distributions, patrol zone recommendations

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`spatial-clustering` `dbscan` `crime-analysis` `hotspot-detection` `predictive-policing` `machine-learning` `public-safety`