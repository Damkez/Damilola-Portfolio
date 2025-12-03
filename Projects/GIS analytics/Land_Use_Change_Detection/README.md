# Land Use Change Detection

## 📊 Overview

Multi-temporal satellite image classification using supervised machine learning to detect and quantify land use changes (urban expansion, deforestation, agricultural conversion) over 20-year period.

**Business Context**: Environmental agencies need accurate land use change statistics for policy compliance monitoring, carbon accounting, and sustainable development goal (SDG) tracking.

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**: Landsat Collection 2, Sentinel-2, ESA WorldCover Validation
- **Python Libraries**: `ee`, `geemap`, `sklearn`, `numpy`, `pandas`, `matplotlib`
- **Methods**: Random Forest classification, Change detection matrices, Accuracy assessment, Trend analysis

## 🔬 Methodology

Select cloud-free imagery for 2000, 2010, 2020 → Extract spectral indices (NDVI, NDBI, NDWI) → Train Random Forest classifier on 6 classes (forest, agriculture, urban, water, bare, grass) → Classify all time periods → Generate change detection matrix → Quantify transitions

## 📈 Results & Insights

Urban area expanded by 135% (12,000 to 28,200 ha). Forest decreased 8.5% primarily to agriculture conversion (4,200 ha lost). Cropland remained stable with 15% internal transitions between crop types. Water bodies decreased 12% due to reservoir sedimentation. Overall accuracy: 89-92% across time periods.

**Visualizations**: Classified maps, change matrices, transition flows, trend charts

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`land-use-change` `change-detection` `landsat` `random-forest` `classification` `urbanization` `deforestation` `earth-engine`