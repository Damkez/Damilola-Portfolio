# Price Optimization

## 📊 Overview

Dynamic pricing analysis using price elasticity estimation and profit maximization to determine optimal price points across product categories and customer segments.

**Business Context**: Pricing teams need data-driven strategies to maximize revenue and profit while remaining competitive, accounting for demand sensitivity and customer willingness-to-pay.

## 🛠️ Tools & Technologies

- **Data Sources**: Historical prices, sales volumes, competitor prices, customer segments
- **Python Libraries**: `sklearn`, `scipy`, `pandas`, `matplotlib`, `statsmodels`
- **Methods**: Price elasticity of demand calculation, Linear/Logistic regression, Profit maximization (Revenue - Cost), A/B test design

## 🔬 Methodology

Collect price-volume data →Estimate demand curve (Volume = a - b×Price) → Calculate price elasticity (% change in demand / % change in price) → Model profit function → Find optimal price using calculus/optimization → Segment analysis (price-sensitive vs premium customers)

## 📈 Results & Insights

Average price elasticity: -1.8 (elastic demand - 1% price increase → 1.8% volume decrease). Current pricing ($49.99) is below optimal ($54.99) leaving $180K annual profit on table. Segment analysis shows premium customers (25%) have elasticity of -0.8 (inelastic) - candidates for +15% price increase. Price-sensitive segment (45%) require competitive pricing. Recommended: tiered pricing with $44.99 basic, $59.99 premium. Projected profit improvement: 12% (+$215K/year).

**Visualizations**: Demand curves, elasticity by segment, profit landscapes, optimal price points

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`price-optimization` `elasticity` `revenue-management` `profit-maximization` `dynamic-pricing` `pricing-strategy` `economics`