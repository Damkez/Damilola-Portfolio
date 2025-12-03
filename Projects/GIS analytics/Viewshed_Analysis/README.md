# Viewshed Analysis

## 📊 Overview

3D visibility analysis using DEMs to assess scenic viewpoints, telecommunications tower coverage, and wind turbine visual impact for infrastructure siting and environmental impact assessment.

**Business Context**: Telecommunications companies and wind energy developers need viewshed analyses to assess signal coverage, minimize visual impact on landscapes, and comply with environmental regulations.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: SRTM 30m DEM, ASTER GDEM
- **Python Libraries**: `ee`, `geemap`, `numpy`, `scipy`, `matplotlib`
- **Methods**: Viewshed calculation, Line-of-sight analysis, Cumulative visibility mapping, Observer height adjustments

## 🔬 Methodology

Extract DEM for study area → Define observer locations (tower sites) → Calculate line-of-sight for each cell → Generate binary viewshed (visible/not visible) → Create cumulative visibility map showing number of towers visible from each location

## 📈 Results & Insights

Proposed tower locations provide 87% coverage of target zone. Cumulative viewshed shows 15% of protected landscape will have visual impact from ≥1 tower. Adjusted tower placement reduces impact to 8% while maintaining 82% coverage. Ridge-top sites maximize coverage efficiency.

**Visualizations**: Viewshed maps, cumulative visibility, coverage analysis, impact zones

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`viewshed analysis` `visibility` `dem` `telecommunications` `visual-impact` `3d-analysis` `siting` `earth-engine`