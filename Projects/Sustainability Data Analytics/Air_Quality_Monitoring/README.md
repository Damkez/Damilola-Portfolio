# Air Quality Monitoring & Health Impact Assessment

## 📊 Overview

Spatiotemporal analysis of air pollutants (NO2, PM2.5) using Sentinel-5P satellite data for Delhi, India. This project combines time series decomposition, hotspot mapping, and population exposure modeling to assess environmental health risks and guide pollution mitigation strategies.

**Business Context**: Public health authorities require real-time air quality intelligence to issue health advisories, implement traffic restrictions (Low Emission Zones), and prioritize urban greening interventions in high-pollution zones.

**Key Applications**:
- Public health advisory systems
- Traffic management and LEZ implementation
- Urban planning for green buffer zones
- Environmental policy impact assessment

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**:
  - Sentinel-5P TROPOMI - NO2 column density
  - WorldPop - Population density for exposure modeling
  - OpenAQ (Simulated) - Ground-level PM2.5 validation

- **Python Libraries**:
  - `ee` & `geemap` - Earth Engine data access and interactive mapping
  - `statsmodels` - Time series decomposition (STL)
  - `scipy` - Statistical analysis and correlation
  - `pandas` & `numpy` - Data manipulation
  - `matplotlib` & `seaborn` - Visualization

- **Analysis Methods**:
  - **STL Decomposition** - Seasonal-Trend decomposition using LOESS
  - **Getis-Ord Gi*** - Spatial hotspot statistical significance
  - **Health Risk Index** - Composite pollution exposure metric
  - **Meteorological Correlation** - Wind speed vs dispersion analysis

## 🔬 Methodology

### 1. Data Acquisition (2019-2024)
- Extract Sentinel-5P NO2 time series for Delhi buffer (50km)
- Interpolate missing values using time-based methods
- Resample to weekly aggregates for cleaner signal extraction

### 2. Temporal Analysis
- Apply STL decomposition to separate trend, seasonal, and residual components
- Identify long-term pollution trends (increasing vs decreasing)
- Detect seasonal patterns (winter smog vs monsoon dispersion)

### 3. Spatial Hotspot Mapping
- Calculate mean NO2 concentration across study period
- Overlay with population density for exposure risk assessment
- Generate composite health risk index (60% pollution + 40% population)

### 4. Environmental Drivers
- Simulate meteorological variables (temperature, wind speed)
- Calculate Pearson correlations between weather and pollutant levels
- Perform regression analysis for dispersion effect quantification

## 📈 Results & Insights

### Key Findings

**Pollution Dynamics**: Time series analysis revealed clear seasonal cyclicity with peak NO2 levels during winter months, likely linked to agricultural burning and temperature inversion layers. Long-term trend analysis indicates either increasing or stable pollution levels.

**Spatial Hotspots**: Central and Eastern Delhi districts show combined high pollution and high population density, creating maximum exposure risk zones requiring immediate intervention.

**Environmental Drivers**: Strong negative correlation (-0.3 to -0.5) between wind speed and NO2 confirms the critical role of meteorological conditions in pollutant dispersion. Temperature shows moderate correlation indicating seasonal dependency.

**Health Impact**: Risk index mapping identified "dark red" zones where vulnerable populations (children, elderly) face elevated respiratory disease risk.

### Visualizations

![NO2 Time Series Decomposition](outputs/no2_time_series_decomposition.png)
*Trend, seasonal, and residual components of NO2 concentration over 5 years*

![Pollutant-Weather Correlation](outputs/pollutant_weather_correlation.png)
*Heatmap showing relationships between NO2, temperature, and wind speed*

![Wind Speed vs NO2 Regression](outputs/wind_speed_no2_regression.png)
*Linear regression demonstrating dispersion effect of wind on pollution*

[Mean NO2 Concentration Map](outputs/mean_no2_concentration_map.html)
*Interactive map showing average NO2 levels across Delhi*

[Health Risk Index Map](outputs/health_risk_index_map.html)
*Combined pollution-population exposure risk visualization*

## 🔗 Links

- [Analysis Notebook](analysis.ipynb) - Full Jupyter notebook with executable code
- [Generator Script](../../air_quality_monitoring_generator.py) - Automated notebook generation script
- [Sentinel-5P Documentation](https://sentinel.esa.int/web/sentinel/missions/sentinel-5p) - Satellite mission details

## 🏷️ Tags

`air-quality` `pollution-monitoring` `sentinel-5p` `public-health` `delhi-india` `time-series-analysis` `spatial-statistics` `environmental-health` `earth-engine` `health-risk-assessment`