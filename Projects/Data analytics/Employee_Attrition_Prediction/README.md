# Employee Attrition Prediction

## 📊 Overview

HR analytics using classification models to predict employee turnover risk, identify key drivers of attrition, and enable proactive retention interventions.

**Business Context**: HR teams need early warning systems to identify at-risk employees, understand root causes of turnover, and implement targeted retention strategies to reduce costly attrition.

## 🛠️ Tools & Technologies

- **Data Sources**: Employee data (demographics, job role, satisfaction scores, tenure)
- **Python Libraries**: `sklearn`, `xgboost`, `pandas`, `matplotlib`, `shap`
- **Methods**: Logistic Regression, Random Forest, XGBoost, SHAP feature importance, Threshold optimization

## 🔬 Methodology

Load employee dataset → Engineer features (tenure bands, satisfaction ratios) → Handle class imbalance with SMOTE → Train multiple classifiers → Optimize for recall (catch at-risk) → Interpret using SHAP → Generate retention recommendations

## 📈 Results & Insights

XGBoost achieves 86% recall, 78% precision. Top attrition drivers: low satisfaction score (32% importance), overtime frequency (24%), low salary relative to peers (18%), lack of promotions (15%). High-risk profile: tenure 2-4 years, satisfaction <3/5, no promotion in 2+ years. Model flags 120 at-risk employees. Targeted interventions (raises, mentorship) for top 50 could retain 28-35 employees annually, saving $840K-$1.05M in replacement costs.

**Visualizations**: Feature importance, SHAP values, risk score distributions, retention ROI

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`hr-analytics` `attrition-prediction` `employee-retention` `xgboost` `shap` `people-analytics` `machine-learning`