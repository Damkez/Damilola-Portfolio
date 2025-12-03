# Sales Forecasting

## 📊 Overview

Time series sales prediction using ARIMA and Prophet models to forecast monthly revenue, identify seasonal patterns, and support inventory and budgeting decisions.

**Business Context**: Finance and operations teams need accurate sales forecasts for inventory planning, cash flow management, and resource allocation to avoid stockouts or excess inventory.

## 🛠️ Tools & Technologies

- **Data Sources**: Historical monthly sales data (3 years)
- **Python Libraries**: `pandas`, `statsmodels`, `prophet`, `matplotlib`, `sklearn`
- **Methods**: ARIMA modeling, Prophet decomposition, Seasonal pattern detection, Forecast accuracy metrics (MAPE, RMSE)

## 🔬 Methodology

Load historical sales data → Decompose trend/seasonal components → Fit ARIMA(2,1,1) and Prophet models → Generate 12-month forecast → Calculate confidence intervals → Evaluate accuracy on holdout set

## 📈 Results & Insights

ARIMA achieves MAPE of 8.2%, Prophet: 9.5%. Strong seasonality detected (Q4 spike +35%). Forecast predicts 12% YoY growth next year. Model captures holiday effects accurately. Recommended: increase Q4 inventory by 30%, maintain lean stock in Q2. Forecast supports $2.5M revenue projection with ±$200K uncertainty.

**Visualizations**: Historical trends, seasonal decomposition, forecasts with confidence intervals, accuracy metrics

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`sales-forecasting` `time-series` `arima` `prophet` `demand-planning` `predictive-analytics` `inventory-optimization`