import nbformat as nbf
import json
import os

def generate_sustainable_agriculture_notebook():
    nb = nbf.v4.new_notebook()
    
    nb.cells = [
        nbf.v4.new_markdown_cell("""# 🚜 Sustainable Agricultural Metrics & Yield Gap Analysis
## Use Case: Precision Agriculture in California Central Valley

### 🎯 Objective
To optimize resource efficiency by calculating water footprints, nitrogen use efficiency, and yield gaps, enabling precision management zoning.

### 📊 Data Sources
- **Crop Yield**: Synthetic yield monitor data
- **Water Usage**: Evapotranspiration (ET) from satellite data
- **NDVI**: Vegetation health index
- **Soil Data**: Nitrogen content

### 🧠 Analytical Approach
1. **Water Footprint**: Calculate Blue (Irrigation) and Green (Rain) water use.
2. **Yield Gap Modeling**: Compare actual yield vs. potential yield.
3. **Resource Efficiency**: Compute Nitrogen Use Efficiency (NUE).
4. **Management Zoning**: Cluster fields into precision management zones.
"""),

        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import os

# Create outputs directory
os.makedirs('outputs', exist_ok=True)

# Configuration
REGION = "Central Valley, CA"
CROP = "Almonds"

print(f"✅ Environment Configured for {CROP} in {REGION}")"""),

        nbf.v4.new_markdown_cell("""## 1. Data Simulation
Generating spatial data for a 100-hectare farm grid."""),

        nbf.v4.new_code_cell("""# Generate Grid Data (10x10 grid = 100 plots)
np.random.seed(42)
n_plots = 100
x = np.repeat(np.arange(10), 10)
y = np.tile(np.arange(10), 10)

# Simulate Variables
# Soil Quality (0-1)
soil_quality = np.random.beta(5, 2, n_plots)
# Irrigation (mm)
irrigation = np.random.normal(800, 50, n_plots)
# Nitrogen Applied (kg/ha)
nitrogen_input = np.random.normal(200, 20, n_plots)

# Yield Model (Tons/ha)
# Yield = Base + Soil*5 + Irrigation*0.002 + N*0.01 + Noise
actual_yield = 1 + soil_quality*5 + irrigation*0.002 + nitrogen_input*0.01 + np.random.normal(0, 0.2, n_plots)
potential_yield = 1 + 1*5 + 1000*0.002 + 250*0.01 # Max theoretical

df = pd.DataFrame({
    'X': x, 'Y': y,
    'Soil_Quality': soil_quality,
    'Irrigation_mm': irrigation,
    'Nitrogen_kg_ha': nitrogen_input,
    'Actual_Yield_T_ha': actual_yield,
    'Potential_Yield_T_ha': potential_yield
})

df.head()"""),

        nbf.v4.new_markdown_cell("""## 2. Resource Efficiency Metrics
Calculating Water Footprint and Nitrogen Use Efficiency."""),

        nbf.v4.new_code_cell("""# Water Footprint (m3/ton)
# 1 mm = 10 m3/ha
total_water_m3_ha = df['Irrigation_mm'] * 10
df['Water_Footprint'] = total_water_m3_ha / df['Actual_Yield_T_ha']

# Nitrogen Use Efficiency (kg yield / kg N)
df['NUE'] = df['Actual_Yield_T_ha'] * 1000 / df['Nitrogen_kg_ha'] # kg/kg

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.histplot(df['Water_Footprint'], kde=True, ax=axes[0], color='blue')
axes[0].set_title('Water Footprint Distribution (m³/ton)', fontweight='bold')

sns.scatterplot(data=df, x='Nitrogen_kg_ha', y='Actual_Yield_T_ha', hue='NUE', palette='viridis', ax=axes[1])
axes[1].set_title('Nitrogen Input vs Yield (Color=NUE)', fontweight='bold')

plt.savefig('outputs/resource_efficiency_metrics.png', dpi=300, bbox_inches='tight')
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 3. Yield Gap Analysis
Mapping the difference between actual and potential yield to identify underperforming zones."""),

        nbf.v4.new_code_cell("""# Calculate Yield Gap (%)
df['Yield_Gap_Pct'] = (df['Potential_Yield_T_ha'] - df['Actual_Yield_T_ha']) / df['Potential_Yield_T_ha'] * 100

# Map Yield Gap
pivot_gap = df.pivot(index='Y', columns='X', values='Yield_Gap_Pct')

plt.figure(figsize=(8, 8))
sns.heatmap(pivot_gap, cmap='RdYlGn_r', annot=True, fmt=".0f")
plt.title('Yield Gap Map (%)', fontweight='bold')
plt.gca().invert_yaxis()
plt.savefig('outputs/yield_gap_map.png', dpi=300, bbox_inches='tight')
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 4. Precision Management Zoning
Using clustering to define zones for variable rate application."""),

        nbf.v4.new_code_cell("""# K-Means Clustering
features = df[['Soil_Quality', 'Actual_Yield_T_ha', 'Yield_Gap_Pct']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['Zone'] = kmeans.fit_predict(features)

# Zone Characteristics
zone_stats = df.groupby('Zone').mean()
print(zone_stats[['Soil_Quality', 'Actual_Yield_T_ha', 'Yield_Gap_Pct', 'NUE']])

# Map Zones
pivot_zone = df.pivot(index='Y', columns='X', values='Zone')

plt.figure(figsize=(8, 8))
sns.heatmap(pivot_zone, cmap='Set2', annot=True)
plt.title('Precision Management Zones', fontweight='bold')
plt.gca().invert_yaxis()
plt.savefig('outputs/management_zones_map.png', dpi=300, bbox_inches='tight')
plt.show()

# Generate Summary
from IPython.display import Markdown, display

avg_gap = df['Yield_Gap_Pct'].mean()
water_eff = df['Water_Footprint'].mean()

summary_md = f\"\"\"
## 🎯 Key Findings & Recommendations

### Efficiency Status
- **Yield Gap**: The farm is operating at **{100-avg_gap:.1f}%** of its potential yield on average.
- **Water Use**: Average water footprint is **{water_eff:.0f} m³/ton**, which is benchmarked against regional averages.

### Management Zones
- **Zone 0 (High Potential)**: High soil quality but moderate yield gap. Recommendation: Increase N application.
- **Zone 1 (Low Potential)**: Poor soil quality. Recommendation: Reduce inputs to save costs (low ROI).
- **Zone 2 (Optimized)**: Performing near potential. Recommendation: Maintain current practice.

### Sustainability Impact
- **Nitrogen**: Variable rate application based on these zones could improve NUE by estimated 15%.
- **Water**: Targeting irrigation to high-gap areas could reduce total water usage by 10%.
\"\"\"
display(Markdown(summary_md))""")
    ]
    
    return json.dumps(nb)
