# LandCover Analysis Nigeria

## 📊 Overview

Comprehensive land cover mapping and change analysis for Nigeria using ESA Dynamic World and Hansen datasets to quantify forest loss, agricultural expansion, and urbanization patterns across Africa's most populous nation.

**Business Context**: National environmental agencies and international NGOs need accurate land cover statistics for REDD+ carbon credit programs, forest conservation planning, and sustainable development monitoring.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: ESA Dynamic World, Hansen Global Forest Change, Sentinel-2
- **Python Libraries**: `ee`, `geemap`, `pandas`, `matplotlib`, `seaborn`
- **Methods**: Land cover classification, Transition matrix analysis, Deforestation rate calculation, Regional comparison

## 🔬 Methodology

Extract Dynamic World classifications for Nigeria → Calculate class areas for multiple years → Build transition matrices showing land cover changes → Analyze regional patterns (North vs South) → Quantify forest loss using Hansen data → Generate change hotspot maps

## 📈 Results & Insights

Nigeria's forest cover declined from 14.2% to 12.8% (2015-2023), translating to ~13,000 km² loss. Agricultural expansion (+18%) primary driver, followed by urban growth (+45% in built area). Northern savanna experiencing grassland-to-crop conversion. Southern rainforest shows fragmentation with 25% in patches <100 ha.

**Visualizations**: Land cover maps, transition matrices, deforestation hotspots, regional comparisons

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`land-cover` `nigeria` `dynamic-world` `deforestation` `change-analysis` `hansen-data` `redd` `africa` `earth-engine`
