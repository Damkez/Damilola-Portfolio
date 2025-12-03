# Fraud Detection

## 📊 Overview

Machine learning fraud classification using anomaly detection and supervised learning on transaction data to identify suspicious patterns and reduce financial losses.

**Business Context**: Financial institutions need automated fraud detection to minimize losses, reduce false positives that frustrate customers, and comply with regulatory requirements.

## 🛠️ Tools & Technologies

- **Data Sources**: Synthetic transaction data (amount, location, time, merchant), Labeled fraud cases
- **Python Libraries**: `sklearn`, `xgboost`, `pandas`, `matplotlib`, `imblearn`
- **Methods**: Isolation Forest, Random Forest, XGBoost, SMOTE for class imbalance, Precision-Recall optimization

## 🔬 Methodology

Load imbalanced transaction data (1% fraud) → Apply SMOTE resampling → Train Random Forest and XGBoost → Optimize for high recall (catch fraud) while managing precision (reduce false positives) → Evaluate on test set → Generate risk scores

## 📈 Results & Insights

XGBoost achieves 94% recall, 89% precision (AUC: 0.96). Catches 94% of fraud with 11% false positive rate. Key indicators: unusual transaction amounts (3x normal), foreign locations, rapid succession. Model saves estimated $450K/year in prevented fraud vs $85K in false positive customer friction. Recommended threshold: 0.65 probability for flagging.

**Visualizations**: Confusion matrices, ROC curves, feature importance, precision-recall tradeoffs

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`fraud-detection` `anomaly-detection` `machine-learning` `xgboost` `financial-services` `risk-management` `classification`