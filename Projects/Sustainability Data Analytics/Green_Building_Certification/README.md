# Green Building Certification & Energy Efficiency

## 📊 Overview

Urban building energy performance analysis mapping green certifications (LEED/BREEAM/Green Mark), analyzing Energy Use Intensity (EUI), and identifying retrofit candidates for Singapore's commercial building stock.

**Business Context**: Building owners and policymakers need data-driven retrofit prioritization to meet net-zero targets, reduce operational costs, and improve building sustainability ratings.

## 🛠️ Tools & Technologies

- **Data Sources**: Synthetic building inventory (500 buildings), Energy consumption data, Certification records
- **Python Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `scikit-learn`
- **Methods**: EUI benchmarking, Spatial clustering of green buildings, K-Means zone classification, Carbon savings estimation

## 🔬 Methodology

Generate building dataset with age, size, certification → Calculate EUI metrics → Compare certified vs non-certified performance → Identify retrofit candidates (age >20, EUI >250, uncertified) → Estimate carbon reduction potential

## 📈 Results & Insights

Certified buildings use 32% less energy than non-certified. Identified 127 retrofit candidates with potential  to save 15,600 tons CO2/year. Platinum buildings average 180 kWh/m²/yr vs 265 for non-certified. Top 10 buildings account for 45% of total savings potential.

**Visualizations**: Building distribution maps, EUI comparisons, retrofit candidate rankings, density heatmaps

![Green Building Distribution](outputs/green_building_distribution.png)
![EUI by Certification](outputs/eui_by_certification.png)
![Retrofit Candidates](outputs/retrofit_candidates.png)
[Building Density Map](outputs/green_building_density_map.html)

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)
- [Generator Script](../../green_building_generator.py)

## 🏷️ Tags

`green-building` `energy-efficiency` `eui` `building-retrofit` `leed` `carbon-reduction` `urban-sustainability` `singapore`