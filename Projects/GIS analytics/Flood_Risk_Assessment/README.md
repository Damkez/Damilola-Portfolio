# Flood Risk Assessment

## 📊 Overview

Hydrological flood hazard modeling combining rainfall intensity, topographic flow accumulation, and land cover runoff coefficients to generate flood risk maps for urban drainage planning.

**Business Context**: Municipal drainage departments and insurance companies need flood hazard zones to prioritize infrastructure upgrades, issue property risk ratings, and plan emergency evacuation routes.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: CHIRPS Precipitation, SRTM Elevation, ESA WorldCover, HydroSHEDS Flow Direction
- **Python Libraries**: `ee`, `geemap`, `scipy`, `numpy`, `matplotlib`
- **Methods**: Flow accumulation analysis, Runoff coefficient mapping, 100-year rainfall modeling, Flood extent delineation

## 🔬 Methodology

Extract extreme precipitation (100-year return period) → Calculate slope and flow accumulation from DEM → Assign runoff coefficients by land cover → Model flood extent using terrain analysis → Classify risk zones (high/medium/low)

## 📈 Results & Insights

Identified 15% of urban area in high flood risk zones. Low-lying areas (<5m elevation) with >80% impervious cover most vulnerable. Flow accumulation analysis reveals 3 major drainage  bottlenecks requiring infrastructure intervention. Climate projections suggest 12% increase in risk extent by 2050.

**Visualizations**: Flood risk maps, flow accumulation, elevation profiles, risk zone classifications

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`flood-risk` `hydrological-modeling` `drainage-planning` `disaster-management` `urban-resilience` `climate-adaptation` `earth-engine`