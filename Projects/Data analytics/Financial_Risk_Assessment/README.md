# Financial Risk Assessment

## 📊 Overview

Credit risk modeling using logistic regression and machine learning to predict loan default probability, calculate expected loss, and optimize lending decisions.

**Business Context**: Banks need automated risk assessment to approve loans efficiently, price interest rates appropriately, and maintain healthy loan portfolios while managing regulatory capital requirements.

## 🛠️ Tools & Technologies

- **Data Sources**: Loan application data (income, credit score, debt-to-income, loan amount)
- **Python Libraries**: `sklearn`, `xgboost`, `pandas`, `matplotlib`, `shap`
- **Methods**: Logistic Regression, XGBoost, Probability calibration, Expected Loss calculation (PD × EAD × LGD)

## 🔬 Methodology

Load historical loan data with default labels → Engineer features (DTI ratio, credit utilization) → Train Logistic Regression and XGBoost → Calibrate probabilities → Calculate risk-adjusted pricing → Set acceptance thresholds

## 📈 Results & Insights

XGBoost achieves AUC of 0.82. Key risk factors: credit score (38% importance), DTI ratio (28%), loan-to-income (22%). Default probability ranges 2-45% across applicants. Risk-based pricing model suggests interest rates from 4.5% (low risk) to 12% (high risk). Optimized threshold (PD <15%) achieves 8% default rate vs 12% baseline, improving portfolio quality by 33%.

**Visualizations**: ROC curves, feature importance, PD distributions, risk-adjusted pricing curves

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`credit-risk` `financial-modeling` `logistic-regression` `xgboost` `loan-default-prediction` `risk-management` `banking`