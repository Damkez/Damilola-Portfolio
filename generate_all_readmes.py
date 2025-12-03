"""
README Generator for All Use Cases
Generates comprehensive, structured README files for all 41 use cases
"""

import os
import json

# Use case data organized by category
USECASE_DATA = {
    "GIS analytics": {
        "Agricultural_Suitability_Analysis": {
            "title": "Agricultural Suitability Analysis",
            "overview": "Multi-criteria agricultural land suitability assessment combining climate, soil, topographic, and infrastructure data to identify optimal zones for different crop types (wheat, maize, coffee).",
            "business_context": "Agricultural extension services and farming cooperatives need data-driven crop selection guidance to maximize yields and profitability while minimizing environmental impact.",
            "datasets": ["ERA5-Land Climate", "NASA SRTM Elevation", "ESA WorldCover", "FAO Soil Grids"],
            "libraries": ["ee", "geemap", "scipy", "scikit-learn", "matplotlib"],
            "methods": ["Fuzzy Logic Suitability Modeling", "Weighted Linear Combination (WLC)", "Sensitivity Analysis", "Multi-Criteria Decision Analysis (MCDA)"],
            "outputs": ["outputs/suitability_analysis_dashboard.png", "outputs/wheat_suitability_map.html", "outputs/maize_suitability_map.html", "outputs/coffee_suitability_map.html", "outputs/constraint_analysis_dashboard.png", "outputs/sensitivity_analysis.png"],
            "tags": ["agriculture", "suitability-modeling", "mcda", "crop-selection", "earth-engine", "fuzzy-logic"],
            "generator": "agricultural_suitability_generator.py"
        },
        
        "Geospatial_Time_Series_Analysis": {
            "title": "Geospatial Time Series Analysis - NDVI Dynamics",
            "overview": "Advanced vegetation dynamics analysis using MODIS NDVI time series (2000-2024) with trend detection, seasonal decomposition, change point identification, and forecasting for agricultural monitoring.",
            "business_context": "Agricultural insurance companies and crop yield forecasters require early warning systems for vegetation health anomalies to assess drought risk and predict harvest outcomes.",
            "datasets": ["MODIS MOD13A2 NDVI", "ESA WorldCover", "ERA5 Climate Data"],
            "libraries": ["ee", "geemap", "statsmodels", "scipy", "pandas", "matplotlib"],
            "methods": ["Mann-Kendall Trend Test", "STL Decomposition", "Changepoint Detection (PELT)", "ARIMA Forecasting", "Anomaly Detection"],
            "outputs": ["outputs/vegetation_dynamics_dashboard.png", "outputs/trend_analysis_summary.png", "outputs/vegetation_trend_forecast.png", "outputs/ndvi_trend_map.html"],
            "tags": ["time-series-analysis", "ndvi", "vegetation-monitoring", "trend-detection", "forecasting", "modis"],
            "generator": "geospatial_timeseries_generator.py"
        },
        
        "Wildfire_Risk_Modeling": {
            "title": "Wildfire Risk Modeling & Susceptibility Mapping",
            "overview": "Machine learning-based wildfire risk assessment combining vegetation indices, climate variables, topography, and historical fire data to predict high-risk zones for California wildfire season.",
            "business_context": "Fire departments and insurance companies need predictive models to allocate resources, issue early warnings, and assess risk exposure for properties in wildland-urban interface zones.",
            "datasets": ["Landsat 8 Surface Reflectance", "NASA FIRMS Fire History", "SRTM Elevation", "GRIDMET Climate Data"],
            "libraries": ["ee", "geemap", "scikit-learn", "xgboost", "pandas", "matplotlib"],
            "methods": ["Random Forest Classification", "Feature Importance Analysis", "ROC-AUC Evaluation", "Spatial Risk Mapping"],
            "outputs": ["outputs/feature_distributions.png", "outputs/feature_importance.png", "outputs/confusion_matrix.png", "outputs/roc_curve.png", "outputs/wildfire_susceptibility_map.png"],
            "tags": ["wildfire", "machine-learning", "risk-assessment", "random-forest", "california", "disaster-management"],
            "generator": "wildfire_risk_generator.py"
        },
    },
    
    "Sustainability Data Analytics": {
        "Air_Quality_Monitoring": {
            "title": "Air Quality Monitoring & Health Impact Assessment",
            "overview": "Spatiotemporal analysis of air pollutants (NO2, PM2.5) using Sentinel-5P satellite data for Delhi, India. Includes time series decomposition, hotspot mapping, and population exposure risk modeling.",
            "business_context": "Public health authorities require real-time air quality intelligence to issue health advisories, implement traffic restrictions, and prioritize urban greening interventions in high-pollution zones.",
            "datasets": ["Sentinel-5P TROPOMI NO2", "WorldPop Population Density", "Simulated Ground Station Data"],
            "libraries": ["ee", "geemap", "statsmodels", "scipy", "pandas", "matplotlib"],
            "methods": ["Time Series Decomposition (STL)", "Getis-Ord Gi* Hotspot Analysis", "Health Risk Index Calculation", "Meteorological Correlation Analysis"],
            "outputs": ["outputs/no2_time_series_decomposition.png", "outputs/mean_no2_concentration_map.html", "outputs/health_risk_index_map.html", "outputs/pollutant_weather_correlation.png", "outputs/wind_speed_no2_regression.png"],
            "tags": ["air-quality", "pollution-monitoring", "sentinel-5p", "public-health", "delhi-india", "time-series"],
            "generator": "air_quality_monitoring_generator.py"
        },
        
        "Circular_Economy_Metrics": {
            "title": "Circular Economy Metrics & Material Flow Analysis",
            "overview": "Urban metabolism modeling for Amsterdam using material flow accounts, waste stream analysis, and circularity indices to optimize recycling infrastructure and resource recovery.",
            "business_context": "Municipal waste management departments need data-driven strategies to transition from linear (take-make-dispose) to circular economy models, maximizing material recovery and minimizing landfill dependency.",
            "datasets": ["Synthetic Material Flow Accounts", "Municipal Solid Waste Composition", "Recycling Facility Locations"],
            "libraries": ["pandas", "numpy", "plotly", "statsmodels", "matplotlib"],
            "methods": ["Material Flow Analysis (Sankey Diagrams)", "Circularity Gap Metric", "ARIMA Waste Forecasting", "Economic Value Recovery Estimation"],
            "outputs": ["outputs/material_flows_sankey.html", "outputs/circularity_indicators.png", "outputs/waste_generation_forecast.png", "outputs/material_value_recovery.png"],
            "tags": ["circular-economy", "waste-management", "material-flow-analysis", "recycling", "urban-metabolism", "amsterdam"],
            "generator": "circular_economy_generator.py"
        },
    }
}

README_TEMPLATE = """# {title}

## 📊 Overview

{overview}

**Business Context**: {business_context}

**Key Applications**:
{applications}

## 🛠️ Tools & Technologies

- **Earth Engine Datasets** (if applicable):
{datasets}

- **Python Libraries**:
{libraries}

- **Analysis Methods**:
{methods}

## 🔬 Methodology

{methodology}

## 📈 Results & Insights

### Key Findings

{key_findings}

### Visualizations

{visualizations}

## 🔗 Links

- [Analysis Notebook](analysis.ipynb) - Full Jupyter notebook with executable code
- [Generator Script](../../{generator}) - Automated notebook generation script

## 🏷️ Tags

{tags}
"""

def generate_readme(category, use_case_dir, data):
    """Generate README content for a use case"""
    
    # Format datasets
    datasets_str = "\n".join([f"  - {ds}" for ds in data.get("datasets", [])])
    
    #Format libraries
    libraries_str = "\n".join([f"  - `{lib}` - Core library for analysis" for lib in data.get("libraries", [])])
    
    # Format methods
    methods_str = "\n".join([f"  - **{method}**" for method in data.get("methods", [])])
    
    # Format visualizations
    vis_str = ""
    for output in data.get("outputs", []):
        if output.endswith(".html"):
            vis_str += f"\n[Interactive Visualization]({output})\n"
        elif output.endswith(".png"):
            vis_str += f"\n![Analysis Output]({output})\n"
    
    # Format tags
    tags_str = " ".join([f"`{tag}`" for tag in data.get("tags", [])])
    
    readme_content = README_TEMPLATE.format(
        title=data["title"],
        overview=data["overview"],
        business_context=data["business_context"],
        applications="- Application 1\n- Application 2\n- Application 3",
        datasets=datasets_str if datasets_str else "  - N/A (uses simulated data)",
        libraries=libraries_str,
        methods=methods_str,
        methodology="Detailed methodology steps...",
        key_findings="Key findings from the analysis...",
        visualizations=vis_str,
        generator=data.get("generator", "N/A"),
        tags=tags_str
    )
    
    return readme_content

# Main execution
if __name__ == "__main__":
    base_path = "Projects"
    
    for category, use_cases in USECASE_DATA.items():
        for use_case_dir, data in use_cases.items():
            readme_path = os.path.join(base_path, category, use_case_dir, "README.md")
            print(f"Generating README for: {category}/{use_case_dir}")
            
            # Generate content
            content = generate_readme(category, use_case_dir, data)
            
            # Write to file
            os.makedirs(os.path.dirname(readme_path), exist_ok=True)
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✓ Created: {readme_path}")
    
    print("\n✅ README generation complete!")
