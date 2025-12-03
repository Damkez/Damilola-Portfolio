# Inventory Optimization

## 📊 Overview

Multi-echelon inventory optimization using EOQ models, safety stock calculations, and ABC classification to minimize carrying costs while maintaining target service levels.

**Business Context**: Supply chain teams need to balance inventory investment against stockout risk, optimize reorder points, and allocate warehouse space efficiently across thousands of SKUs.

## 🛠️ Tools & Technologies

- **Data Sources**: SKU-level sales history, lead times, carrying costs, stockout costs
- **Python Libraries**: `pandas`, `scipy`, `numpy`, `matplotlib`, `seaborn`
- **Methods**: Economic Order Quantity (EOQ), Reorder Point (ROP) calculation, ABC classification, Service level optimization

## 🔬 Methodology

Calculate demand statistics (mean, std dev) per SKU → Apply ABC classification (70-20-10 revenue rule) → Compute EOQ and ROP using Z-scores for target service level → Simulate inventory policy → Compare costs vs current state

## 📈 Results & Insights

ABC analysis: A-items (15% of SKUs, 70% revenue), B-items (25%, 20%), C-items (60%, 10%). EOQ model reduces order frequency by 28% and carrying costs by 18%. Optimized safety stock maintains 95% service level with 12% less inventory investment ($420K reduction). A-items require higher safety stock (1.8σ) than C-items (1.2σ). Annual savings: $180K carrying cost + $95K ordering cost.

**Visualizations**: ABC Pareto charts, EOQ cost curves, inventory turnover by category, service level tradeoffs

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`inventory-optimization` `eoq` `supply-chain` `abc-analysis` `safety-stock` `operations-research` `logistics`