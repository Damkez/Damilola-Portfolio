# Biodiversity Impact Assessment

## 📊 Overview

Forest loss and biodiversity monitoring using Hansen Global Forest Change and protected area datasets. Analyzes annual deforestation rates, patch fragmentation, and impacts on conservation zones to assess biodiversity risk and guide protection strategies.

**Business Context**: Conservation organizations need quantitative metrics on forest loss to prioritize intervention zones, allocate ranger patrols, and demonstrate conservation impact to donors and policymakers.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: Hansen Global Forest Change, WDPA Protected Areas, ESA WorldCover
- **Python Libraries**: `ee`, `geemap`, `scipy`, `pandas`, `matplotlib`, `seaborn`
- **Methods**: Deforestation rate calculation, Patch size distribution analysis, Protected area overlap assessment

## 🔬 Methodology

Extract annual forest loss from Hansen dataset → Calculate deforestation metrics (area, rate) → Analyze spatial patterns and fragmentation → Overlay with protected areas to assess encroachment → Generate biodiversity risk maps

## 📈 Results & Insights

Annual deforestation averaging 2.5-3% with accelerating trend. Patch analysis shows increasing fragmentation reducing habitat connectivity. Protected areas experiencing 8-12% encroachment along boundaries. Priority zones identified for enhanced protection measures.

**Visualizations**: Annual forest loss trends, patch size distributions, protected area overlay maps

![Annual Forest Loss](outputs/annual_forest_loss.png)
![Forest Patch Distribution](outputs/forest_patch_distribution.png)
[Biodiversity Overlay Map](outputs/biodiversity_overlay_map.html)

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)
- [Generator Script](../../biodiversity_impact_generator.py)

## 🏷️ Tags

`biodiversity` `deforestation` `forest-monitoring` `hansen-data` `protected-areas` `conservation` `habitat-fragmentation` `earth-engine`