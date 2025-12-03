# Urban Heat Island Analysis

## 📊 Overview

Landsat thermal infrared analysis mapping urban heat island intensity, identifying vulnerable populations, and assessing green infrastructure cooling effects for climate adaptation planning.

**Business Context**: Urban planners need heat vulnerability maps to target green infrastructure investments, protect at-risk populations, and mitigate urban heat effects in climate change adaptation strategies.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: Landsat 8 Thermal Band, NDVI, WorldPop Demographics, ESA WorldCover  
- **Python Libraries**: `ee`, `geemap`, `numpy`, `pandas`, `matplotlib`
- **Methods**: Land Surface Temperature (LST) retrieval, Heat Island Intensity calculation, Correlation with NDVI, Vulnerability indexing

## 🔬 Methodology

Retrieve Landsat Band 10 thermal data → Convert digital numbers to LST (°C) → Calculate Heat Island Intensity (urban LST - rural LST) → Correlate with vegetation (NDVI) → Overlay with population to identify vulnerable zones

## 📈 Results & Insights

Urban core experiences 6-8°C higher temperatures than surrounding rural areas. Strong negative correlation (r=-0.72) between NDVI and LST confirms vegetation cooling effect. Identified 25,000 residents in high-heat, low-vegetation zones requiring intervention. Parks provide 2-3°C cooling within 200m radius.

**Visualizations**: LST maps, heat island intensity, NDVI correlation, vulnerability zones

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`urban-heat-island` `thermal-remote-sensing` `landsat` `climate-adaptation` `green-infrastructure` `public-health` `earth-engine`