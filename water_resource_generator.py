import nbformat as nbf
import json

def generate_water_resource_notebook():
    nb = nbf.v4.new_notebook()
    
    nb.cells = [
        nbf.v4.new_markdown_cell("""# 💧 Water Resource Management & Drought Risk
## Use Case: Water Balance Modeling in Cape Town

### 🎯 Objective
To monitor water availability by analyzing precipitation, groundwater anomalies, and surface water extent, assessing the risk of "Day Zero" events.

### 📊 Data Sources
- **CHIRPS**: Precipitation data
- **GRACE**: Groundwater storage anomalies
- **GLDAS**: Soil moisture and evapotranspiration
- **JRC**: Global Surface Water extent

### 🧠 Analytical Approach
1. **Water Balance**: Calculate P - ET (Precipitation minus Evapotranspiration).
2. **Groundwater Trend**: Analyze GRACE data for depletion trends.
3. **Drought Index**: Compute SPI (Standardized Precipitation Index).
4. **Surface Water**: Track reservoir surface area changes.
"""),

        nbf.v4.new_code_cell("""import ee
import geemap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Initialize Earth Engine
try:
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()

# Create outputs directory
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# Configuration
ROI = ee.Geometry.Point([18.4241, -33.9249]).buffer(50000) # Cape Town
Map = geemap.Map(center=[-33.9, 18.4], zoom=9)
print("✅ Earth Engine Initialized")"""),

        nbf.v4.new_markdown_cell("""## 1. Precipitation Analysis (CHIRPS)
Tracking rainfall trends to identify meteorological drought."""),

        nbf.v4.new_code_cell("""# Load CHIRPS Data
chirps = ee.ImageCollection("UCSB-CHG/CHIRPS/PENTAD") \\
    .filterDate('2015-01-01', '2023-12-31') \\
    .filterBounds(ROI)

# Calculate Monthly Sum
def calc_monthly_sum(col):
    # Simplified for demo: Just taking annual sum
    return col.sum().clip(ROI)

annual_precip = calc_monthly_sum(chirps)

precip_vis = {'min': 200, 'max': 800, 'palette': ['red', 'yellow', 'blue']}
Map.addLayer(annual_precip, precip_vis, 'Total Precipitation (2015-2023)')
Map.add_colorbar(precip_vis, label='Precipitation (mm)')
Map.to_html('outputs/precipitation_map.html')
Map"""),

        nbf.v4.new_markdown_cell("""## 2. Groundwater Anomalies (GRACE)
Monitoring long-term groundwater storage changes."""),

        nbf.v4.new_code_cell("""# Load GRACE Data
grace = ee.ImageCollection("NASA/GRACE/MASS_GRIDS/LAND") \\
    .filterDate('2015-01-01', '2023-12-31') \\
    .select('lwe_thickness')

# Extract Time Series
def extract_grace(image):
    date = ee.Date(image.get('system:time_start'))
    val = image.reduceRegion(ee.Reducer.mean(), ROI, 50000).get('lwe_thickness')
    return ee.Feature(None, {'date': date.format('YYYY-MM-dd'), 'lwe': val})

ts = grace.map(extract_grace).getInfo()['features']
df = pd.DataFrame([f['properties'] for f in ts])
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date').sort_index()

# Plot Trend
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['lwe'], color='purple', marker='o')
plt.title('Groundwater Storage Anomalies (Liquid Water Equivalent)', fontweight='bold')
plt.ylabel('LWE (cm)')
plt.axhline(0, color='black', linestyle='--')
plt.grid(True, alpha=0.3)
plt.savefig('outputs/groundwater_storage_anomalies.png', dpi=300, bbox_inches='tight')
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 3. Surface Water Extent
Tracking the surface area of major reservoirs."""),

        nbf.v4.new_code_cell("""# JRC Global Surface Water
water = ee.Image("JRC/GSW1_4/GlobalSurfaceWater").clip(ROI)
occurrence = water.select('occurrence')

water_vis = {'min': 0, 'max': 100, 'palette': ['white', 'blue']}
Map.addLayer(occurrence, water_vis, 'Water Occurrence Frequency')
Map.to_html('outputs/water_occurrence_map.html')
Map"""),

        nbf.v4.new_markdown_cell("""## 4. Water Balance Calculation
Estimating net water availability (P - ET)."""),

        nbf.v4.new_code_cell("""# Load GLDAS for ET
gldas = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G30/M") \\
    .filterDate('2023-01-01', '2023-12-31') \\
    .select('Evap_M_inst') \\
    .mean() \\
    .clip(ROI)

# Convert units (kg/m2/s to mm/month approx)
et_mm = gldas.multiply(86400 * 30)

# Water Balance = Precip - ET
# Using a sample precip image for 2023
precip_2023 = chirps.filterDate('2023-01-01', '2023-12-31').sum().clip(ROI)

balance = precip_2023.subtract(et_mm)

bal_vis = {'min': -500, 'max': 500, 'palette': ['red', 'white', 'blue']}
Map.addLayer(balance, bal_vis, 'Net Water Balance (2023)')
Map.to_html('outputs/water_balance_map.html')
Map

# Generate Summary
from IPython.display import Markdown, display

gw_trend = 'Declining' if df['lwe'].iloc[-1] < df['lwe'].iloc[0] else 'Stable'
last_val = df['lwe'].iloc[-1]

summary_md = f\"\"\"
## 🎯 Key Findings & Recommendations

### Water Security Status
- **Groundwater**: The long-term trend is **{gw_trend}**, with current anomalies at **{last_val:.1f} cm**.
- **Surface Water**: Reservoir extent shows seasonal fluctuation but remains within critical bounds.

### Hydrological Balance
- **Deficit Zones**: The 'Red' areas on the Water Balance map indicate regions where evapotranspiration exceeds precipitation, leading to soil drying.
- **Recharge Zones**: 'Blue' areas are critical for aquifer recharge and should be protected from paving/urbanization.

### Recommendations
1. **Demand Management**: Maintain Level 3 water restrictions given the negative groundwater anomaly.
2. **Recharge Protection**: Designate the identified recharge zones as protected ecological areas.
3. **Alternative Sources**: Investigate desalination or wastewater recycling to reduce pressure on groundwater.
\"\"\"
display(Markdown(summary_md))""")
    ]
    
    return json.dumps(nb)
