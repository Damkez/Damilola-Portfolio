# Service Area Analysis

## 📊 Overview

Healthcare facility service area mapping using drive-time isochrones and population coverage analysis to assess accessibility gaps and optimize emergency response capacity.

**Business Context**: Healthcare administrators need service area definitions for capacity planning, ambulance dispatch optimization, and identifying underserved populations requiring new facilities.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: OpenStreetMap Road Network, WorldPop Demographics
- **Python Libraries**: `networkx`, `geemap`, `scipy`, `pandas`, `matplotlib`
- **Methods**: Network analysis, Isochrone generation, Population coverage calculation, Gap analysis

## 🔬 Methodology

Extract road network → Define facility locations → Generate drive-time isochrones (10, 20, 30 min) → Calculate population within each zone → Identify gaps (areas >30min from facility) → Propose new facility locations

## 📈 Results & Insights

78% of population within 20-min drive time of facilities. Identified 3 underserved zones (22% population, >30min access) requiring new facilities. Optimal placement of 2 new facilities would achieve 95% coverage. Rural areas disproportionately affected by access gaps.

**Visualizations**: Isochrone maps, coverage analysis, gap identification, optimal facility locations

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`service-area` `healthcare-access` `network-analysis` `isochrones` `accessibility-planning` `gis` `public-health`