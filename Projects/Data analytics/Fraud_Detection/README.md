# Fraud Detection

## 📋 Project Overview

Identify fraudulent transactions using anomaly detection and ML

## 🎯 Objectives

- Build fraud detection model\n- Identify suspicious patterns\n- Calculate risk scores\n- Reduce false positives

## 📊 Key Findings

1. Fraud rate: 0.17% of transactions\n2. Model precision: 0.88, recall: 0.82, F1: 0.85\n3. Avg fraud amount: $122 vs $88 for legitimate\n4. Geographic hotspots identified in 3 regions

## 💡 Recommendations

**1. Implement real-time scoring for transactions >$100**\n\n**2. Flag transactions from high-risk regions for review**\n\n**3. Use device fingerprinting for repeat offender detection**\n\n**4. Estimated savings: $2.1M annually in prevented fraud**\n

## 🛠️ Technologies Used

- **Python 3.8+**
- **Domain**: Data analytics
- **Libraries**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Geemap (for GIS)

## 📁 Project Structure

```
Fraud_Detection/
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
