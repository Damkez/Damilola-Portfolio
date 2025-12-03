# Customer Segmentation

## 📊 Overview

RFM-based customer segmentation using K-Means clustering on transactional data to identify high-value segments, personalize marketing strategies, and optimize customer retention programs.

**Business Context**: Marketing teams need data-driven customer groups to tailor campaigns, allocate budgets efficiently, and maximize customer lifetime value through targeted retention and up-sell strategies.

## 🛠️ Tools & Technologies

- **Data Sources**: Synthetic transaction history (Recency, Frequency, Monetary), Customer demographics
- **Python Libraries**: `pandas`, `sklearn`, `matplotlib`, `seaborn`, `scipy`
- **Methods**: RFM scoring, K-Means++ clustering, Elbow method, Silhouette analysis, Segment profiling

## 🔬 Methodology

Calculate RFM metrics for each customer → Normalize scores → Apply K-Means (k=4) → Profile segments by avg RFM, demographics → Label segments (Champions, Loyal, At-Risk, Lost) → Generate retention strategies

## 📈 Results & Insights

Identified 4 segments: Champions (15%, high RFM), Loyal (32%, high F/M), At-Risk (28%, declining R), Lost (25%, low all). Champions generate 42% of revenue from 15% of customers. At-Risk segment shows 35% churn risk - priority for win-back campaigns. Personalized retention could save $180K annual revenue.

**Visualizations**: RFM distributions, cluster plots, segment profiles, retention strategies

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`customer-segmentation` `rfm-analysis` `k-means` `marketing-analytics` `retention` `clv` `personalization`