# Ocean Pollution Tracking & Accumulation Modeling

## 📊 Overview

Lagrangian particle tracking simulation modeling marine plastic debris transport through ocean gyres to predict accumulation zones (garbage patches) and optimize cleanup array deployment.

**Business Context**: Marine conservation NGOs need evidence-based targeting for ocean cleanup operations, policy advocacy for source reduction, and assessment of riverine inputs to marine pollution.

## 🛠️ Tools & Technologies

- **Data Sources**: Simulated ocean current vector fields, Coastal plastic source points
- **Python Libraries**: `numpy`, `matplotlib`, `seaborn`, `scipy`
- **Methods**: Lagrangian particle tracking, Kernel density estimation, Gyre modeling, Concentration factor calculation

## 🔬 Methodology

Initialize particles at coastal sources → Simulate transport using ocean current model + random diffusion → Track 50 timesteps → Calculate accumulation density using KDE → Identify garbage patch centroid → Estimate cleanup capture efficiency

## 📈 Results & Insights

Particles concentrate in gyre center with 8.5x density increase from initial dispersal. Centroid at coordinates showing 67% of particles within 2-unit radius. Optimal cleanup array placement captures 73% of debris. Source control at river mouths could reduce accumulation by 40-50%. Concentration highest in convergence zones with low turbulence.

**Visualizations**: Particle trajectories, density maps, accumulation zones, cleanup efficiency

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)
- [Generator Script](../../ocean_pollution_generator.py)

## 🏷️ Tags

`ocean-pollution` `plastic-debris` `lagrangian-tracking` `marine-conservation` `garbage-patch` `cleanup-optimization` `gyre-modeling`