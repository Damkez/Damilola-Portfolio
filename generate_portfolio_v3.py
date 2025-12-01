"""
Portfolio Generator v3 - Custom Generators Approach

This script creates truly unique, sophisticated notebooks for each use case
rather than using generic templates.
"""

import os
import json

BASE_DIR = os.path.join(os.path.dirname(__file__), "Projects")

# ======================================================================================
# CUSTOM GENERATOR: FLOOD RISK ASSESSMENT
# ======================================================================================

def generate_flood_risk_notebook():
    """Generate comprehensive Flood Risk Assessment notebook with hydrology analysis."""
    
    cells = [
        # Header
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Flood Risk Assessment - Comprehensive Hydrology Analysis\n\n",
                "## 📊 Business Context\n",
                "Identify flood-prone areas using advanced hydrological modeling, topographic analysis, and proximity-based risk assessment.\n\n",
                "**Analytical Approach**: Multi-criteria flood risk modeling\n",
                "- Topographic Wetness Index (TWI)\n",
                "- Flow accumulation analysis\n",
                "- Distance to water bodies\n",
                "- Population exposure estimation"
            ]
        },
        
        # Imports
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Import Libraries\n",
                "import ee\n",
                "import geemap\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "import numpy as np\n",
                "import pandas as pd\n",
                "\n",
                "# Initialize Earth Engine\n",
                "try:\n",
                "    ee.Initialize()\n",
                "except:\n",
                "    ee.Authenticate()\n",
                "    ee.Initialize()\n",
                "\n",
                "print('Earth Engine initialized successfully')"
            ]
        },
        
        # AOI Definition
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Define Area of Interest (Lagos, Nigeria)\n",
                "# Known for coastal flooding and low-lying terrain\n",
                "center_point = [3.3792, 6.5244]\n",
                "AOI = ee.Geometry.Point(center_point).buffer(30000)  # 30km radius\n",
                "\n",
                "print(f'Analysis Area: {AOI.area().divide(1e6).getInfo():.2f} sq km')"
            ]
        },
        
        # Data Loading
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Load Geospatial Datasets\n",
                "print('Loading datasets...')\n",
                "\n",
                "# 1. SRTM Digital Elevation Model (30m resolution)\n",
                "dem = ee.Image('USGS/SRTMGL1_003').select('elevation').clip(AOI)\n",
                "\n",
                "# 2. Calculate Slope (degrees)\n",
                "slope = ee.Terrain.slope(dem)\n",
                "\n",
                "# 3. JRC Global Surface Water (water bodies)\n",
                "water = ee.Image('JRC/GSW1_4/GlobalSurfaceWater').select('occurrence').clip(AOI)\n",
                "\n",
                "# 4. WorldPop Population Density\n",
                "population = ee.ImageCollection('WorldPop/GP/100m/pop') \\\n",
                "    .filterBounds(AOI) \\\n",
                "    .sort('system:time_start', False) \\\n",
                "    .first() \\\n",
                "    .clip(AOI)\n",
                "\n",
                "print('✓ All datasets loaded')"
            ]
        },
        
        # TWI Calculation
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Calculate Topographic Wetness Index (TWI)\n",
                "# TWI = ln(Flow Accumulation / tan(Slope))\n",
                "# Higher TWI = Higher flood risk\n",
                "\n",
                "def calculate_twi(dem_image):\n",
                "    # Flow accumulation (simplified using slope as proxy)\n",
                "    slope_rad = slope.multiply(np.pi).divide(180)\n",
                "    tan_slope = slope_rad.tan()\n",
                "    \n",
                "    # Prevent division by zero\n",
                "    tan_slope = tan_slope.where(tan_slope.gt(0.001), 0.001)\n",
                "    \n",
                "    # For this demo, use elevation as proxy for contributing area\n",
                "    # In production, use proper flow accumulation algorithm\n",
                "    contributing_area = dem_image.multiply(-1).add(1000)\n",
                "    \n",
                "    # Calculate TWI\n",
                "    twi = contributing_area.divide(tan_slope).log()\n",
                "    \n",
                "    return twi\n",
                "\n",
                "twi = calculate_twi(dem)\n",
                "print('✓ TWI calculated')"
            ]
        },
        
        # Distance to Water
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Calculate Distance to Water Bodies\n",
                "# Areas near water have higher flood risk\n",
                "\n",
                "# Identify permanent water (occurrence > 50%)\n",
                "permanent_water = water.gt(50)\n",
                "\n",
                "# Calculate Euclidean distance (in meters)\n",
                "distance_to_water = permanent_water.fastDistanceTransform(256).sqrt() \\\n",
                "    .multiply(ee.Image.pixelArea().sqrt())\n",
                "\n",
                "# Invert: closer = higher risk\n",
                "water_proximity_risk = distance_to_water.multiply(-1).add(5000).divide(5000)\n",
                "water_proximity_risk = water_proximity_risk.clamp(0, 1)\n",
                "\n",
                "print('✓ Water proximity calculated')"
            ]
        },
        
        # Risk Integration
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Multi-Criteria Flood Risk Model\n",
                "# Combine: Low Elevation + High TWI + Proximity to Water + Low Slope\n",
                "\n",
                "# Normalize each factor to 0-1 scale\n",
                "elevation_risk = dem.lt(20).multiply(1.0)  # Below 20m elevation\n",
                "slope_risk = slope.lt(5).multiply(1.0)     # Flat areas (<5°)\n",
                "twi_normalized = twi.unitScale(0, 15)      # Normalize TWI\n",
                "\n",
                "# Weighted combination\n",
                "flood_risk_score = elevation_risk.multiply(0.3) \\\n",
                "    .add(twi_normalized.multiply(0.25)) \\\n",
                "    .add(water_proximity_risk.multiply(0.25)) \\\n",
                "    .add(slope_risk.multiply(0.2))\n",
                "\n",
                "# Classify risk levels\n",
                "risk_classes = flood_risk_score.gt(0.7).multiply(3) \\\n",
                "    .add(flood_risk_score.gt(0.5).multiply(1)) \\\n",
                "    .add(flood_risk_score.gt(0.3).multiply(1))\n",
                "# 3 = Very High, 2 = High, 1 = Moderate, 0 = Low\n",
                "\n",
                "print('✓ Flood risk model completed')"
            ]
        },
        
        # Statistics
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Calculate Risk Statistics\n",
                "\n",
                "def calculate_risk_stats():\n",
                "    pixel_area = ee.Image.pixelArea()\n",
                "    \n",
                "    # Area by risk class\n",
                "    stats = {}\n",
                "    for risk_level in range(4):\n",
                "        mask = risk_classes.eq(risk_level)\n",
                "        area_km2 = mask.multiply(pixel_area).reduceRegion(\n",
                "            reducer=ee.Reducer.sum(),\n",
                "            geometry=AOI,\n",
                "            scale=100,\n",
                "            maxPixels=1e9\n",
                "        ).get('elevation').getInfo() / 1e6\n",
                "        \n",
                "        stats[f'Level_{risk_level}'] = area_km2\n",
                "    \n",
                "    # Population in high-risk areas\n",
                "    high_risk_pop = population.updateMask(risk_classes.gte(2)).reduceRegion(\n",
                "        reducer=ee.Reducer.sum(),\n",
                "        geometry=AOI,\n",
                "        scale=100,\n",
                "        maxPixels=1e9\n",
                "    ).get('population').getInfo()\n",
                "    \n",
                "    return stats, high_risk_pop\n",
                "\n",
                "area_stats, exposed_pop = calculate_risk_stats()\n",
                "\n",
                "print('\\n=== Flood Risk Statistics ===')\n",
                "print(f'Low Risk Area: {area_stats[\"Level_0\"]:.2f} km²')\n",
                "print(f'Moderate Risk Area: {area_stats[\"Level_1\"]:.2f} km²')\n",
                "print(f'High Risk Area: {area_stats[\"Level_2\"]:.2f} km²')\n",
                "print(f'Very High Risk Area: {area_stats[\"Level_3\"]:.2f} km²')\n",
                "print(f'\\nPopulation in High/Very High Risk Zones: {exposed_pop:,.0f} people')"
            ]
        },
        
        # Visualization
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Create Interactive Map\n",
                "\n",
                "m = geemap.Map(center=[center_point[1], center_point[0]], zoom=11)\n",
                "\n",
                "# Visualization parameters\n",
                "dem_vis = {'min': 0, 'max': 100, 'palette': ['blue', 'green', 'yellow', 'brown']}\n",
                "risk_vis = {'min': 0, 'max': 3, 'palette': ['green', 'yellow', 'orange', 'red']}\n",
                "water_vis = {'min': 0, 'max': 100, 'palette': ['white', 'blue']}\n",
                "pop_vis = {'min': 0, 'max': 100, 'palette': ['white', 'purple']}\n",
                "\n",
                "# Add layers\n",
                "m.addLayer(dem, dem_vis, 'Elevation (m)', False)\n",
                "m.addLayer(water, water_vis, 'Water Occurrence (%)', False)\n",
                "m.addLayer(population, pop_vis, 'Population Density', False)\n",
                "m.addLayer(risk_classes, risk_vis, 'Flood Risk Classes', True)\n",
                "\n",
                "# Add legend\n",
                "m.add_colorbar(risk_vis, label='Flood Risk (0=Low, 3=Very High)', position='bottomright')\n",
                "\n",
                "m"
            ]
        },
        
        # Charts
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# Static Visualizations\n",
                "\n",
                "fig, axes = plt.subplots(2, 2, figsize=(16, 12))\n",
                "\n",
                "# 1. Risk Area Distribution\n",
                "risk_labels = ['Low', 'Moderate', 'High', 'Very High']\n",
                "risk_areas = [area_stats[f'Level_{i}'] for i in range(4)]\n",
                "colors = ['green', 'yellow', 'orange', 'red']\n",
                "\n",
                "axes[0,0].bar(risk_labels, risk_areas, color=colors, alpha=0.7, edgecolor='black')\n",
                "axes[0,0].set_ylabel('Area (km²)')\n",
                "axes[0,0].set_title('Flood Risk Area Distribution', fontsize=14, fontweight='bold')\n",
                "axes[0,0].grid(axis='y', alpha=0.3)\n",
                "\n",
                "# 2. Pie Chart\n",
                "axes[0,1].pie(risk_areas, labels=risk_labels, colors=colors, autopct='%1.1f%%',\n",
                "              startangle=90, explode=[0.05]*4)\n",
                "axes[0,1].set_title('Risk Proportion', fontsize=14, fontweight='bold')\n",
                "\n",
                "# 3. Cumulative Risk\n",
                "cumulative_risk = np.cumsum(risk_areas[::-1])[::-1]\n",
                "axes[1,0].plot(risk_labels, cumulative_risk, marker='o', linewidth=3, color='darkred')\n",
                "axes[1,0].fill_between(range(4), cumulative_risk, alpha=0.3, color='red')\n",
                "axes[1,0].set_ylabel('Cumulative Area (km²)')\n",
                "axes[1,0].set_title('Cumulative Flood Risk Exposure', fontsize=14, fontweight='bold')\n",
                "axes[1,0].grid(alpha=0.3)\n",
                "\n",
                "# 4. Summary Table\n",
                "axes[1,1].axis('off')\n",
                "summary_data = [\n",
                "    ['Total Analysis Area', f'{sum(risk_areas):.2f} km²'],\n",
                "    ['High + Very High Risk', f'{area_stats[\"Level_2\"] + area_stats[\"Level_3\"]:.2f} km²'],\n",
                "    ['% High Risk', f'{((area_stats[\"Level_2\"] + area_stats[\"Level_3\"])/sum(risk_areas)*100):.1f}%'],\n",
                "    ['Exposed Population', f'{exposed_pop:,.0f} people'],\n",
                "    ['Risk Density', f'{exposed_pop/(area_stats[\"Level_2\"] + area_stats[\"Level_3\"]):.0f} people/km²']\n",
                "]\n",
                "table = axes[1,1].table(cellText=summary_data, colLabels=['Metric', 'Value'],\n",
                "                        cellLoc='left', loc='center', bbox=[0, 0.2, 1, 0.6])\n",
                "table.auto_set_font_size(False)\n",
                "table.set_fontsize(11)\n",
                "table.scale(1, 2)\n",
                "axes[1,1].set_title('Summary Statistics', fontsize=14, fontweight='bold', pad=20)\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        
        # Recommendations
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 🎯 Key Findings & Recommendations\n\n",
                "### Risk Assessment Summary\n",
                "1. **High-Risk Zones Identified**: Areas with elevation <20m, flat terrain, and proximity to water bodies\n",
                "2. **Population Exposure**: Significant number of people living in flood-prone areas\n",
                "3. **Topographic Vulnerability**: TWI analysis reveals natural drainage convergence zones\n\n",
                "### Strategic Recommendations\n\n",
                "#### 1. Infrastructure Planning\n",
                "- Restrict new development in Very High Risk zones (red areas)\n",
                "- Require elevated foundations in High Risk zones\n",
                "- Implement green infrastructure (retention ponds, permeable surfaces)\n\n",
                "#### 2. Early Warning Systems\n",
                "- Install flood sensors in identified high-risk areas\n",
                "- Develop community alert systems using identified population clusters\n",
                "- Create evacuation routes avoiding low-lying areas\n\n",
                "#### 3. Mitigation Measures\n",
                "- Improve drainage capacity in TWI hotspots\n",
                "- Construct flood barriers along water body proximities\n",
                "- Restore natural wetlands for water absorption\n\n",
                "#### 4. Further Analysis Needed\n",
                "- Historical flood event validation\n",
                "- Climate change scenario modeling (sea-level rise)\n",
                "- Economic impact assessment\n",
                "- Detailed hydraulic modeling (HEC-RAS)\n\n",
                "### Data Sources\n",
                "- **DEM**: SRTM 30m (USGS)\n",
                "- **Water Bodies**: JRC Global Surface Water\n",
                "- **Population**: WorldPop (100m resolution)"
            ]
        }
    ]
    
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return json.dumps(notebook, indent=1)


# Test generation
if __name__ == "__main__":
    print("Generating Flood Risk Assessment notebook...")
    
    notebook_path = os.path.join(BASE_DIR, "GIS analytics", "Flood_Risk_Assessment")
    os.makedirs(notebook_path, exist_ok=True)
    
    # Generate notebook
    nb_content = generate_flood_risk_notebook()
    
    # Write to file
    with open(os.path.join(notebook_path, "analysis.ipynb"), 'w', encoding='utf-8') as f:
        f.write(nb_content)
    
    print(f"✓ Created: {notebook_path}/analysis.ipynb")
