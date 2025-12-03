# Sustainable Supply Chain & Scope 3 Emission Tracking

## 📊 Overview

Global logistics carbon footprint analysis mapping supplier networks, calculating transport emissions (air/sea/road), and comparing "fastest" vs "greenest" routing scenarios for supply chain decarbonization.

**Business Context**: Corporations need Scope 3 transparency to report climate impacts, identify emission reduction opportunities, and meet customer/regulatory sustainability requirements in logistics.

## 🛠️ Tools & Technologies

- **Data Sources**: Global supplier coordinates, Transport mode data, Emission factors (CO2e per ton-km)
- **Python Libraries**: `pandas`, `numpy`, `plotly`, `networkx`, `matplotlib`
- **Methods**: Network mapping, Haversine distance calculation, Modal emission factors, Scenario optimization

## 🔬 Methodology

Map supplier locations and transport modes → Calculate distances using Haversine formula → Apply emission factors by mode (Sea: 0.01, Air: 0.50, Road: 0.06 kg CO2e/ton-km) → Compute total Scope 3 transport emissions → Model green scenario (shift air to sea) → Quantify reduction potential

## 📈 Results & Insights

Total transport emissions: 8,450 kg CO2e with air freight contributing 62% despite being only 28% of routes. Top emitter: Supplier delivering via air from Asia (3,200 kg CO2e). Modal shift scenario reduces emissions by 68% but increases lead time 20-30 days. Green routing achieves 5,750 kg CO2e savings annually worth $115,000 at $20/ton carbon price.

**Visualizations**: Network maps, emission breakdowns, modal comparisons, optimization scenarios

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)
- [Generator Script](../../sustainable_supply_chain_generator.py)

## 🏷️ Tags

`supply-chain` `scope-3-emissions` `logistics-optimization` `carbon-footprint` `modal-shift` `green-routing` `decarbonization`