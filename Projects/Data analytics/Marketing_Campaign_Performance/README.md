# Marketing Campaign Performance

## 📊 Overview

Multi-channel marketing attribution analysis using conversion funnel tracking, ROI calculation by channel, and budget optimization to maximize customer acquisition efficiency.

**Business Context**: Marketing teams need to allocate limited budgets across channels (email, social, search, display) based on data-driven ROI rather than intuition or legacy spending patterns.

## 🛠️ Tools & Technologies

- **Data Sources**: Campaign spend by channel, Conversions, Customer journey touchpoints
- **Python Libraries**: `pandas`, `matplotlib`, `seaboard`, `scipy`
- **Methods**: Multi-touch attribution, Conversion funnel analysis, ROI calculation, Statistical significance testing

## 🔬 Methodology

Track campaign performance metrics (impressions, clicks, conversions, CAC) → Calculate channel-level ROI → Build attribution model (first-touch, last-touch, linear) → Perform statistical tests on channel differences → Optimize budget allocation

## 📈 Results & Insights

Email achieves highest ROI (520%) with $26 revenue per $1 spent. Social has lowest CAC ($18 vs $45 avg). Search drives 48% of conversions despite 30% of budget. Display has poor ROI (110%) - candidate for reallocation. Multi-touch attribution reveals email often assists conversions closed by search. Optimization model: +40% email, +20% search, -60% display budget improves overall ROAS from 380% to 455%. Expected uplift: $280K additional revenue with same $500K budget.

**Visualizations**: Channel ROI comparison, conversion funnels, attribution models, budget optimization scenarios

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`marketing-analytics` `attribution-modeling` `roi-optimization` `campaign-analysis` `performance-marketing` `budget-allocation` `cac`