# AB Testing Analysis

## 📊 Overview

Statistical A/B test evaluation using hypothesis testing to measure impact of website changes on conversion rates and provide data-driven recommendations for product decisions.

**Business Context**: Product managers need rigorous statistical evidence to validate that UI/UX changes improve business metrics before full rollout, avoiding costly mistakes.

## 🛠️ Tools & Technologies

- **Data Sources**: Synthetic user session data (variant A vs B, conversion yes/no)
- **Python Libraries**: `pandas`, `scipy.stats`, `matplotlib`, `seaborn`, `statsmodels`
- **Methods**: Two-proportion z-test, Chi-square test, Power analysis, Confidence intervals, Effect size calculation

## 🔬 Methodology

Define hypothesis (variant B > variant A) → Collect data (n=5000 per variant) → Calculate conversion rates → Perform two-proportion z-test (α=0.05) → Calculate effect size and confidence intervals → Make recommendation

## 📈 Results & Insights

Variant A: 12.3% conversion (615/5000), Variant B: 14.8% conversion (740/5000). Absolute lift: +2.5 percentage points. Z-statistic: 4.12, p-value: 0.00004 (highly significant). 95% CI for lift: [1.4%, 3.6%]. Effect size (Cohen's h): 0.074 (small but meaningful). Recommendation: Deploy variant B. Expected annual revenue impact: +$520K based on traffic projections.

**Visualizations**: Conversion rate comparisons, confidence intervals, statistical power curves, funnel analysis

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`ab-testing` `hypothesis-testing` `conversion-optimization` `statistical-analysis` `experimentation` `cro` `product-analytics`