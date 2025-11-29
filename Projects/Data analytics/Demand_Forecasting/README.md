# Demand Forecasting

## 📋 Project Overview

Predict future product demand using machine learning

## 🎯 Objectives

- Build demand prediction models\n- Incorporate seasonality and trends\n- Account for promotions and external factors\n- Support supply chain planning

## 📊 Key Findings

1. XGBoost model: MAPE 8.2% (excellent accuracy)\n2. Strong weekly and annual seasonality detected\n3. Promotions increase demand by avg 34%\n4. Weather impacts demand ±12% for certain products

## 💡 Recommendations

**1. Adopt ML-based forecasting for top 200 SKUs**\n\n**2. Build promotion impact model for better planning**\n\n**3. Integrate weather data for seasonal products**\n\n**4. Share forecasts with suppliers for better collaboration**\n

## 🛠️ Technologies Used

- **Python 3.8+**
- **Domain**: Data analytics
- **Libraries**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Geemap (for GIS)

## 📁 Project Structure

```
Demand_Forecasting/
├── analysis.ipynb          # Main Jupyter notebook with complete analysis
├── README.md              # This file
└── outputs/               # Generated visualizations
```

## 🚀 How to Run

1. Install required dependencies:
```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn jupyter geemap
```

2. Launch Jupyter Notebook:
```bash
jupyter notebook analysis.ipynb
```

3. Run all cells to generate the analysis and visualizations

---

**Author**: Damilola  
**Domain**: Data analytics  
**Date**: 2025  
**License**: MIT
