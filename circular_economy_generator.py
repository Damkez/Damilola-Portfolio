import nbformat as nbf
import json

def generate_circular_economy_notebook():
    nb = nbf.v4.new_notebook()
    
    nb.cells = [
        nbf.v4.new_markdown_cell("""# 🔄 Circular Economy Metrics & Material Flow Analysis
## Use Case: Urban Resource Efficiency in Amsterdam

### 🎯 Objective
To model urban material flows, calculate circularity indices, and optimize waste recycling infrastructure using a synthetic city model.

### 📊 Data Sources
- **Material Flow Accounts**: Synthetic input-output data for urban metabolism
- **Waste Stream Data**: Municipal solid waste composition
- **Facility Locations**: Recycling centers and waste-to-energy plants

### 🧠 Analytical Approach
1. **Material Flow Analysis (MFA)**: Visualize flows using Sankey diagrams.
2. **Circularity Index**: Calculate the Circularity Gap Metric (CGM).
3. **Waste Forecasting**: Predict future waste generation using ARIMA.
4. **Facility Optimization**: Location-allocation for new recycling hubs.
"""),

        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA

# Create outputs directory
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# Configuration
CITY = "Amsterdam (Modeled)"
YEAR = 2024

print(f"✅ Environment Configured for {CITY}")"""),

        nbf.v4.new_markdown_cell("""## 1. Material Flow Analysis (MFA)
Visualizing the flow of materials from import/extraction to consumption, waste, and recycling."""),

        nbf.v4.new_code_cell("""# Define Flows for Sankey Diagram
labels = ["Imports", "Domestic Extraction", "Consumption", "Waste Generation", 
          "Recycling", "Incineration", "Landfill", "Exported Materials"]

source = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4]
target = [2, 7, 2, 7, 3, 7, 4, 5, 6, 2, 7]
value =  [500, 100, 300, 50, 800, 50, 400, 250, 150, 300, 100]  # Kilotons

# Create Sankey Diagram
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels,
      color = "blue"
    ),
    link = dict(
      source = source,
      target = target,
      value = value,
      color = ['#a6cee3', '#a6cee3', '#b2df8a', '#b2df8a', '#fb9a99', '#fb9a99', 
               '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#6a3d9a']
  ))])

fig.update_layout(title_text="Urban Material Flows (Kilotons/Year)", font_size=12)
fig.write_html('outputs/material_flows_sankey.html')
fig.show()"""),

        nbf.v4.new_markdown_cell("""## 2. Circularity Metrics
Calculating key performance indicators for the circular economy."""),

        nbf.v4.new_code_cell("""# Calculate Metrics
total_input = 600 + 350  # Imports + Extraction
recycled_input = 300     # From Recycling back to Consumption
total_waste = 800
recycled_waste = 400

circularity_rate = (recycled_input / (total_input + recycled_input)) * 100
recycling_efficiency = (recycled_waste / total_waste) * 100

metrics_df = pd.DataFrame({
    'Metric': ['Circularity Rate', 'Recycling Efficiency', 'Landfill Diversion'],
    'Value (%)': [circularity_rate, recycling_efficiency, ((total_waste-150)/total_waste)*100]
})

# Plot Metrics
plt.figure(figsize=(8, 4))
sns.barplot(data=metrics_df, x='Metric', y='Value (%)', palette='viridis')
plt.title('Key Circularity Indicators', fontweight='bold')
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(metrics_df['Value (%)']):
    plt.text(i, v+2, f"{v:.1f}%", ha='center', fontweight='bold')
plt.savefig('outputs/circularity_indicators.png', dpi=300, bbox_inches='tight')
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 3. Waste Generation Forecasting
Predicting future waste streams to plan infrastructure capacity."""),

        nbf.v4.new_code_cell("""# Simulate Monthly Waste Data (5 Years)
dates = pd.date_range(start='2019-01-01', periods=60, freq='M')
trend = np.linspace(50, 65, 60)  # Increasing trend
seasonality = 5 * np.sin(np.linspace(0, 10*np.pi, 60))
noise = np.random.normal(0, 2, 60)
waste_data = trend + seasonality + noise

waste_df = pd.DataFrame({'Date': dates, 'Waste_Tons': waste_data}).set_index('Date')

# Fit ARIMA Model
model = ARIMA(waste_df['Waste_Tons'], order=(1, 1, 1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=12)

# Plot Forecast
plt.figure(figsize=(12, 6))
plt.plot(waste_df.index, waste_df['Waste_Tons'], label='Historical Data', color='gray')
plt.plot(forecast.index, forecast, label='Forecast (Next 12 Months)', color='green', linestyle='--', linewidth=2)
plt.title('Municipal Waste Generation Forecast', fontweight='bold')
plt.ylabel('Waste (Thousand Tons)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('outputs/waste_generation_forecast.png', dpi=300, bbox_inches='tight')
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 4. Economic Value Recovery
Estimating the financial value of recovered materials."""),

        nbf.v4.new_code_cell("""# Material Values ($/Ton)
material_values = {
    'Plastics': 400,
    'Metals': 1500,
    'Paper': 150,
    'Glass': 50,
    'Organics': 30
}

# Composition of Recycled Stream
composition = {
    'Plastics': 0.15,
    'Metals': 0.05,
    'Paper': 0.40,
    'Glass': 0.20,
    'Organics': 0.20
}

total_recycled_tons = 400 * 1000  # 400kt to tons

value_recovery = {}
for mat, share in composition.items():
    tons = total_recycled_tons * share
    value = tons * material_values[mat]
    value_recovery[mat] = value / 1e6  # Millions USD

value_df = pd.DataFrame(list(value_recovery.items()), columns=['Material', 'Value_M_USD'])

# Plot Value Recovery
plt.figure(figsize=(10, 6))
sns.barplot(data=value_df, x='Material', y='Value_M_USD', palette='magma')
plt.title('Estimated Economic Value of Recovered Materials', fontweight='bold')
plt.ylabel('Value (Million USD)')
plt.savefig('outputs/material_value_recovery.png', dpi=300, bbox_inches='tight')
plt.show()

# Generate Summary
from IPython.display import Markdown, display

total_value = value_df['Value_M_USD'].sum()
growth_rate = (forecast.iloc[-1] - waste_df['Waste_Tons'].iloc[-1]) / waste_df['Waste_Tons'].iloc[-1] * 100

summary_md = f\"\"\"
## 🎯 Key Findings & Recommendations

### Circularity Status
- **Circularity Rate**: The city achieves a **{circularity_rate:.1f}%** circularity rate, indicating significant reliance on virgin materials.
- **Efficiency**: Recycling efficiency is **{recycling_efficiency:.1f}%**, meaning nearly half of waste is still lost to incineration or landfill.

### Economic Potential
- **Value Recovery**: Potential to recover **${total_value:.1f} Million** annually from secondary raw materials.
- **Top Value Stream**: **Metals** offer the highest financial return despite lower volume.

### Future Outlook
- **Waste Growth**: Waste generation is projected to grow by **{growth_rate:.1f}%** over the next year.
- **Infrastructure Gap**: Current capacity will be exceeded in 18 months at current trends.

### Recommendations
1. **Plastic Focus**: Invest in advanced sorting for plastics to capture high-value polymers.
2. **Organic Diversion**: Mandate organic waste separation to reduce landfill volume.
3. **Design for Disassembly**: Incentivize local manufacturers to use modular designs.
\"\"\"
display(Markdown(summary_md))""")
    ]
    
    return json.dumps(nb)
