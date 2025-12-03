# Retail Site Selection

## 📊 Overview

Multi-criteria retail location optimization using demographic data, competitor proximity, accessibility metrics, and purchasing power analysis to identify optimal store locations.

**Business Context**: Retail chains need data-driven site selection to maximize foot traffic, minimize cannibalization of existing stores, and ensure market penetration in underserved areas.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: WorldPop Demographics, OpenStreetMap POIs, Road Networks
- **Python Libraries**: `ee`, `geemap`, `pandas`, `scipy`, `sklearn`
- **Methods**: Gravity model, Competitor buffer analysis, Huff model market share prediction, Multi-criteria scoring

## 🔬 Methodology

Extract population density and demographics → Map existing competitors → Calculate accessibility (drive-time isochrones) → Apply gravity model for catchment areas → Score locations using weighted criteria (population: 40%, competitors: 30%, access: 30%)

## 📈 Results & Insights

Identified top 10 expansion locations with combined catchment of 850,000 residents. Optimal sites show >15,000 pop within 2km, >5km from competitors, and <500m from major roads. Market share projections: 18-25% in new catchments using Huff model.

**Visualizations**: Site suitability maps, competitor analysis, catchment zones, accessibility heatmaps

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`retail-analytics` `site-selection` `location-intelligence` `gravity-model` `market-analysis` `gis` `business-geography`