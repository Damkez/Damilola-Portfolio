# Demand Forecasting

## 📊 Overview

Multi-product demand forecasting using machine learning and time series methods to predict weekly sales, optimize inventory levels, and reduce stockouts and overstock costs.

**Business Context**: Retail operations need accurate demand predictions to balance inventory costs (carrying vs stockout), optimize warehouse space, and ensure product availability.

## 🛠️ Tools & Technologies

- **Data Sources**: Historical weekly sales by product (50 SKUs, 2 years)
- **Python Libraries**: `sklearn`, `xgboost`, `statsmodels`, `pandas`, `matplotlib`
- **Methods**: Random Forest Regression, XGBoost, Seasonal decomposition, Feature engineering (lag features, rolling averages)

## 🔬 Methodology

Extract historical sales → Engineer features (lags, moving averages, seasonality indicators) → Train XGBoost model per product category → Generate 4-week ahead forecast → Calculate safety stock requirements → Optimize reorder points

## 📈 Results & Insights

XGBoost achieves MAPE of 12.5% across all SKUs. High-velocity products (top 20%) predicted with 8% error. Seasonal products show higher error (18%) but still actionable. Model identifies upcoming demand spike for Product A (+42% week 3). Optimized inventory policy reduces carrying costs by 18% while maintaining 95% fill rate. Prevented 12 stockout events in validation period.

**Visualizations**: Forecast vs actual, error distributions by product, inventory optimization curves

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`demand-forecasting` `inventory-optimization` `xgboost` `supply-chain` `retail-analytics` `time-series` `machine-learning`