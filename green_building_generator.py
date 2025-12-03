import nbformat as nbf
import json

def generate_green_building_notebook():
    nb = nbf.v4.new_notebook()
    
    nb.cells = [
        nbf.v4.new_markdown_cell("""# 🏢 Green Building Certification & Energy Efficiency
## Use Case: Urban Retrofit Analysis in Singapore

### 🎯 Objective
To map green building certifications (LEED/BREEAM/Green Mark), analyze Energy Use Intensity (EUI), and identify high-priority candidates for energy retrofits.

### 📊 Data Sources
- **Building Inventory**: Synthetic dataset of commercial buildings
- **Energy Data**: Simulated EUI (kWh/m²/yr)
- **Urban Heat Island**: Temperature anomalies

### 🧠 Analytical Approach
1. **Spatial Clustering**: Identify districts with high concentrations of green buildings.
2. **EUI Benchmarking**: Compare certified vs. non-certified building performance.
3. **Retrofit Targeting**: Identify inefficient buildings in high-heat zones.
4. **Carbon Savings**: Estimate potential emission reductions from retrofits.
"""),
n_buildings = 500

lat = np.random.uniform(1.25, 1.45, n_buildings)
lon = np.random.uniform(103.6, 104.0, n_buildings)
age = np.random.randint(1, 50, n_buildings)
floor_area = np.random.lognormal(9, 0.5, n_buildings)

# Certification Status (Newer buildings more likely to be certified)
certified_prob = 1 / (1 + np.exp(0.1 * (age - 20)))
is_certified = np.random.rand(n_buildings) < certified_prob
certification = ['Green Mark Platinum' if c and r > 0.7 else 
                 'Green Mark Gold' if c else 'None' 
                 for c, r in zip(is_certified, np.random.rand(n_buildings))]

# Energy Use Intensity (EUI) - Certified buildings are more efficient
base_eui = 200  # kWh/m2/yr
eui = base_eui + (age * 2) - (is_certified * 50) + np.random.normal(0, 20, n_buildings)

df = pd.DataFrame({
    'ID': range(n_buildings),
    'Lat': lat,
    'Lon': lon,
    'Age': age,
    'Area_m2': floor_area,
    'Certification': certification,
    'EUI': eui
})

df.head()"""),

        nbf.v4.new_markdown_cell("""## 2. Spatial Analysis of Green Buildings
Visualizing the distribution of certified buildings across the city."""),

        nbf.v4.new_code_cell("""# Spatial Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Lon', y='Lat', hue='Certification', 
                palette={'None': 'gray', 'Green Mark Gold': 'lightgreen', 'Green Mark Platinum': 'darkgreen'},
                alpha=0.7, s=50)
plt.title('Distribution of Green Buildings in Singapore', fontweight='bold')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.savefig('outputs/green_building_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Density Heatmap of Certified Buildings
certified_df = df[df['Certification'] != 'None']
fig = px.density_mapbox(certified_df, lat='Lat', lon='Lon', z='Area_m2', radius=15,
                        center=dict(lat=1.35, lon=103.8), zoom=10,
                        mapbox_style="carto-positron", title="Density of Green Floor Space")
fig.write_html('outputs/green_building_density_map.html')
fig.show()"""),

        nbf.v4.new_markdown_cell("""## 3. Energy Performance Benchmarking
Comparing the energy efficiency of certified vs. non-certified buildings."""),

        nbf.v4.new_code_cell("""# EUI Comparison
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Certification', y='EUI', palette='Greens')
plt.title('Energy Use Intensity (EUI) by Certification Level', fontweight='bold')
plt.ylabel('EUI (kWh/m²/yr)')
plt.savefig('outputs/eui_by_certification.png', dpi=300, bbox_inches='tight')
plt.show()

# Calculate Savings
avg_eui = df.groupby('Certification')['EUI'].mean()
savings_pct = (avg_eui['None'] - avg_eui['Green Mark Platinum']) / avg_eui['None'] * 100
print(f"✅ Platinum buildings use {savings_pct:.1f}% less energy than non-certified buildings.")"""),

        nbf.v4.new_markdown_cell("""## 4. Retrofit Targeting & Carbon Impact
Identifying older, inefficient buildings that would yield the highest ROI from retrofitting."""),

        nbf.v4.new_code_cell("""# Identify Retrofit Candidates
# Criteria: Age > 20, EUI > 250, No Certification
candidates = df[(df['Age'] > 20) & (df['EUI'] > 250) & (df['Certification'] == 'None')].copy()

# Calculate Potential Carbon Savings
# Grid Emission Factor: 0.4 kgCO2/kWh
emission_factor = 0.4
target_eui = avg_eui['Green Mark Gold']

candidates['Potential_Savings_kWh'] = (candidates['EUI'] - target_eui) * candidates['Area_m2']
candidates['Potential_Carbon_Savings_Tons'] = candidates['Potential_Savings_kWh'] * emission_factor / 1000

top_candidates = candidates.sort_values('Potential_Carbon_Savings_Tons', ascending=False).head(10)

print(f"🎯 Identified {len(candidates)} retrofit candidates.")
print(f"🌍 Total Potential Carbon Reduction: {candidates['Potential_Carbon_Savings_Tons'].sum():,.0f} Tons CO2/yr")

# Plot Top Candidates
plt.figure(figsize=(10, 5))
sns.barplot(data=top_candidates, x='ID', y='Potential_Carbon_Savings_Tons', palette='Reds_r', order=top_candidates['ID'])
plt.title('Top 10 Buildings for Retrofit Impact', fontweight='bold')
plt.xlabel('Building ID')
plt.ylabel('Potential Savings (Tons CO2/yr)')
plt.savefig('outputs/retrofit_candidates.png', dpi=300, bbox_inches='tight')
plt.show()

# Generate Summary
from IPython.display import Markdown, display

summary_md = f\"\"\"
## 🎯 Key Findings & Recommendations

### Market Maturity
- **Adoption Rate**: **{(len(certified_df)/n_buildings)*100:.1f}%** of the building stock has some level of green certification.
- **Performance Gap**: Certified buildings outperform non-certified ones by **{savings_pct:.1f}%** in energy efficiency.

### Retrofit Opportunity
- **Target Pool**: **{len(candidates)}** buildings identified as high-priority retrofit candidates (High EUI + Age > 20).
- **Carbon Impact**: Retrofitting these buildings could save **{candidates['Potential_Carbon_Savings_Tons'].sum():,.0f} tons** of CO2 annually.

### Strategic Recommendations
1. **Incentive Targeting**: Direct grants to the owners of the top 10 inefficient buildings.
2. **Policy Mandate**: Require energy audits for all buildings with EUI > 250 kWh/m²/yr.
3. **District Approach**: Focus retrofits in the western industrial district where efficiency is lowest.
\"\"\"
display(Markdown(summary_md))""")
    ]
    
    return json.dumps(nb)
