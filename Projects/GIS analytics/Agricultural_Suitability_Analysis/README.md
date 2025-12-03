# Agricultural Suitability Analysis

## 📊 Overview

Multi-criteria agricultural land suitability assessment combining climate, soil, topographic, and infrastructure data to identify optimal zones for different crop types (wheat, maize, coffee). This analysis uses fuzzy logic and weighted linear combination to produce actionable crop recommendation maps for agricultural extension services.

**Business Context**: Agricultural extension services and farming cooperatives need data-driven crop selection guidance to maximize yields and profitability while minimizing environmental impact. This analysis helps farmers make informed decisions about which crops to plant in specific locations based on comprehensive environmental suitability scores.

**Key Applications**:
- Crop selection and rotation planning
- Agricultural investment site selection
- Climate adaptation strategy development
- Precision agriculture zoning

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**:
  - ERA5-Land Daily Aggregated - Temperature and precipitation
  - NASA SRTM Digital Elevation Model - Elevation and slope
  - ESA WorldCover v100 - Land use classification
  - FAO Soil Grids - Soil properties and fertility

- **Python Libraries**:
  - `ee` & `geemap` - Earth Engine data access and interactive mapping
  - `scipy` - Fuzzy membership functions and optimization
  - `scikit-learn` - Multi-criteria decision analysis
  - `numpy` & `pandas` - Data manipulation and numerical operations
  - `matplotlib` & `seaborn` - Advanced visualization

- **Analysis Methods**:
  - **Fuzzy Logic Suitability Modeling** - Continuous suitability scores (0-1)
  - **Weighted Linear Combination (WLC)** - Multi-criteria aggregation
  - **Sensitivity Analysis** - Weight parameter robustness testing
  - **Constraint Mapping** - Binary exclusion zones (slope, water bodies)

## 🔬 Methodology

### 1. Environmental Data Acquisition
- Extract temperature, precipitation, elevation, and soil data for study region
- Calculate derived metrics (mean annual temperature, growing degree days, slope)
- Normalize all variables to 0-1 scale for comparability

### 2. Fuzzy Suitability Functions
- Define crop-specific optimal ranges for each environmental variable:
  - **Wheat**: Cool temperatures (15-25°C), moderate rainfall (400-600mm)
  - **Maize**: Warm temperatures (18-30°C), higher rainfall (500-800mm)
  - **Coffee**: Moderate temperatures (15-24°C), high elevation (1000-2000m)
- Apply Gaussian, S-shaped, and trapezoidal fuzzy membership functions

### 3. Multi-Criteria Aggregation
- Assign expert-derived weights to criteria (temperature: 30%, rainfall: 25%, soil: 20%, elevation: 15%, slope: 10%)
- Calculate weighted sum of fuzzy suitability scores
- Generate composite suitability maps (0-100 scale)

### 4. Constraint Application
- Apply hard constraints:
  - Exclude slopes >25% (erosion risk)
  - Exclude water bodies and urban areas
  - Exclude protected conservation zones
- Classify final scores: Highly Suitable (>75), Suitable (50-75), Marginal (25-50), Not Suitable (<25)

### 5. Sensitivity Analysis
- Vary weight parameters ±20% to test robustness
- Identify spatial areas where suitability is sensitive to weight assumptions
- Generate uncertainty maps

## 📈 Results & Insights

### Key Findings

**Wheat Suitability**: Highland regions (>800m elevation) with moderate temperatures show highest suitability (>80 scores). Approximately 35-40% of the study area rated as "Highly Suitable" or "Suitable" for wheat cultivation.

**Maize Optimal Zones**: Lowland valleys with warm temperatures and adequate rainfall demonstrate best conditions. Maize shows broader suitability range (45-50% of area) compared to more specialized crops.

**Coffee Premium Zones**: High-elevation zones (1200-1800m) with cooler temperatures and good drainage rated highest. Coffee suitability is most constrained by elevation requirements, with only 15-20% of area highly suitable.

**Best Crop Recommendations**: Spatial overlay analysis identified dominant crop per pixel. Highland areas favor wheat/coffee, while lowlands favor maize. Mixed zones (suitability scores within 10 points) identified for crop rotation opportunities.

**Sensitivity Insights**: Temperature and rainfall weights most influential on final scores. Areas near fuzzy function transition zones show higher sensitivity to parameter changes.

### Visualizations

![Suitability Analysis Dashboard](outputs/suitability_analysis_dashboard.png)
*Comprehensive comparison of wheat, maize, and coffee suitability scores across the study region*

![Constraint Analysis](outputs/constraint_analysis_dashboard.png)
*Visualization of exclusion zones and constraint layers affecting agricultural suitability*

![Sensitivity Analysis](outputs/sensitivity_analysis.png)
*Heat map showing spatial sensitivity of suitability scores to weight parameter variations*

![Best Crop Recommendation Chart](outputs/best_crop_recommendation_chart.png)
*Bar chart showing area distribution by recommended crop type*

[Wheat Suitability Map](outputs/wheat_suitability_map.html)
*Interactive map - explore wheat suitability scores across the landscape*

[Maize Suitability Map](outputs/maize_suitability_map.html)
*Interactive map - explore maize suitability scores across the landscape*

[Coffee Suitability Map](outputs/coffee_suitability_map.html)
*Interactive map - explore coffee suitability scores across the landscape*

[Best Crop Recommendation Map](outputs/best_crop_recommendation_map.html)
*Interactive map - see recommended crop for each location*

## 🔗 Links

- [Analysis Notebook](analysis.ipynb) - Full Jupyter notebook with executable code
- [Generator Script](../../agricultural_suitability_generator.py) - Automated notebook generation script
- [FAO Crop Suitability Guide](http://www.fao.org/land-water/databases-and-software/crop-information/en/) - Crop requirement reference

## 🏷️ Tags

`agriculture` `suitability-modeling` `mcda` `crop-selection` `earth-engine` `fuzzy-logic` `precision-agriculture` `geospatial-analysis` `land-use-planning` `climate-adaptation`