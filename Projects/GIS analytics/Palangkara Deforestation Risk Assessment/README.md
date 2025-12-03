# Palangkara Deforestation Risk Assessment

## 📊 Overview

District-level deforestation risk modeling for Palangkara using machine learning to predict areas at high risk of forest conversion based on proximity to roads, settlements, and historical clearing patterns.

**Business Context**: Forest Service departments need predictive risk maps to prioritize patrol zones, allocate limited enforcement resources, and implement preemptive conservation measures in high-risk areas.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: Hansen Forest Loss, OSM Roads, Population Density, Elevation
- **Python Libraries**: `ee`, `geemap`, `sklearn`, `numpy`, `matplotlib`
- **Methods**: Logistic Regression risk modeling, Proximity analysis, Feature importance ranking, Risk zone classification

## 🔬 Methodology

Map historical forest loss (2010-2023) → Extract risk factors (distance to roads, settlements, elevation, slope, existing forest edge) → Train Logistic Regression on loss/no-loss pixels → Predict risk scores for remaining forest → Classify into risk categories → Identify priority intervention zones

## 📈 Results & Insights

Model achieves 81% accuracy in predicting forest loss locations. Top risk factors: distance to roads (42% importance), distance to forest edge (28%), distance to settlements (18%). Identified 8,500 ha of high-risk forest requiring immediate protection. Risk concentrated in accessible lowlands (<500m elevation) within 2km of roads.

**Visualizations**: Risk probability maps, historical loss patterns, feature importance, priority zones

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`deforestation-risk` `predictive-modeling` `forest-conservation` `logistic-regression` `hansen-data` `spatial-analysis` `earth-engine`
