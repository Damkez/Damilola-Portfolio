# ESG Performance Scoring & Sentiment Analysis

## 📊 Overview

Corporate sustainability benchmarking using composite ESG scoring and NLP sentiment analysis of annual reports. Evaluates Environmental, Social, and Governance performance across 50 companies to identify investment opportunities and greenwashing risks.

**Business Context**: Investment firms need quantitative ESG metrics to screen portfolios, identify sustainable investment opportunities, and detect companies with inflated sustainability claims relative to actual performance.

## 🛠️ Tools & Technologies

- **Data Sources**: Synthetic corporate ESG metrics, Sustainability report excerpts, Stock performance data
- **Python Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `textblob`, `scikit-learn`
- **Methods**: Composite ESG scoring (weighted 40% E, 30% S, 30% G), TextBlob sentiment analysis, Correlation analysis with financial ROI

## 🔬 Methodology

Generate synthetic ESG data for 50 companies → Calculate weighted composite scores → Apply NLP sentiment analysis to report text → Identify greenwashing candidates (high sentiment, low scores) → Correlate ESG scores with financial performance

## 📈 Results & Insights

Technology sector leads with highest ESG scores. Correlation of 0.35 between ESG and ROI suggests positive relationship. Identified 8 greenwashing candidates with positive rhetoric but poor underlying metrics. High-ESG companies outperformed by 3.5% ROI on average.

**Visualizations**: ESG score distributions, sector comparisons, sentiment analysis, correlation matrices

![ESG Score Distribution](outputs/esg_score_distribution.png)
![ESG Sector Comparison](outputs/esg_sector_comparison.png)
![ESG Sentiment Analysis](outputs/esg_sentiment_analysis.png)
![Financial Correlation](outputs/esg_financial_correlation.png)

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)
- [Generator Script](../../esg_performance_generator.py)

## 🏷️ Tags

`esg` `sustainability-metrics` `corporate-governance` `nlp` `sentiment-analysis` `greenwashing-detection` `investment-analysis` `benchmarking`