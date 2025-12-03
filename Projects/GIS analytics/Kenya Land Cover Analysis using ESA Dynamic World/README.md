# Kenya Land Cover Analysis using ESA Dynamic World

## 📊 Overview

Comprehensive land cover change analysis for Kenya using ESA's Dynamic World near-real-time dataset (10m resolution). This project quantifies vegetation dynamics, deforestation patterns, urban expansion, and agricultural land conversion through multi-temporal classification analysis and transition matrix computation.

**Business Context**: Environmental conservation agencies and policy makers need accurate,  timely land cover information to monitor deforestation compliance, track SDG indicators (Goal 15: Life on Land), and assess environmental policy effectiveness in Kenya.

**Key Applications**:
- Forest conservation monitoring
- Urban sprawl quantification
- Agricultural expansion tracking
- Environmental policy impact assessment

## 🛠️ Tools & Technologies

- **Earth Engine Datasets**:
  - ESA WorldCover Dynamic World - 10m resolution land cover (9 classes)
  - Sentinel-2 MSI - Optical imagery for validation
  - Protected Area boundaries - Conservation zone overlay

- **Python Libraries**:
  - `ee` & `geemap` - Dynamic World temporal analysis
  - `numpy` & `pandas` - Transition matrix calculations
  - `matplotlib` & `seaborn` - Change visualization
  - `scikit-learn` - Classification accuracy assessment

- **Analysis Methods**:
  - **Multi-Temporal Classification** - Land cover mapping across time periods
  - **Transition Matrix Analysis** - From-to class change quantification
  - **Change Detection** - Pixel-level class conversion tracking
  - **Accuracy Assessment** - Confusion matrix validation

## 🔬 Methodology

### 1. Data Acquisition & Preprocessing
- Extract Dynamic World classifications for Kenya (2020, 2022, 2024)
- Focus on 9 land cover classes: Trees, Grass, Crops, Shrub, Built, Bare, Water, Wetland, Snow/Ice
- Composite to mode (most frequent class) over annual periods to reduce noise
- Mask clouds and invalid pixels

### 2. Land Cover Area Calculation
- Calculate area (km²) for each class per time period
- Compute percentage of total country area
- Generate class distribution bar charts
- Identify dominant land cover types

### 3. Change Detection Analysis
- Perform pixel-by-pixel comparison between time periods
- Classify pixels as: Stable (no change) or Changed (class conversion)
- Calculate total change area and change percentage
- Map spatial distribution of changes

### 4. Transition Matrix Construction
- Build 9x9 matrix showing transitions between all class pairs
- Key transitions of interest:
  - **Trees → Crops/Bare**: Deforestation
  - **Grass/Shrub → Built**: Urbanization
  - **Crops → Grass**: Agricultural abandonment
  - **Any → Trees**: Reforestation/Regrowth
- Quantify transition areas in km²

### 5. Hotspot Mapping
- Identify regions with highest deforestation rates
- Overlay with protected areas to assess encroachment
- Calculate distance from forest edges to conversion zones
- Generate priority maps for conservation intervention

## 📈 Results & Insights

### Key Findings

**Forest Cover Status**: Kenya's tree cover accounted for approximately 4.2 million hectares (7.2% of country area) in 2024, showing annual decline of 0.3-0.5% due to agricultural expansion and charcoal production.

**Deforestation Patterns**: Transition matrix revealed:
- **Trees → Cropland**: 45,000 ha/year (largest forest loss pathway)
- **Trees → Bare Ground**: 12,000 ha/year (degradation)
- **Trees → Shrubland**: 8,000 ha/year (thinning)
- Total forest loss: ~65,000 ha/year

**Urbanization**: Built-up area increased by 18% (2020-2024), with expansion concentrated around Nairobi, Mombasa, and Kisumu. Peri-urban agriculture converted to residential/commercial at rate of 3,500 ha/year.

**Agricultural Dynamics**: Cropland remained relatively stable (30-32% of total area), with internal shifts between crop types. Some marginal cropland (15,000 ha/year) abandoned and reverting to grassland.

**Reforestation Success**: Detected 12,000 ha/year of forest regrowth in previously cleared areas, suggesting some conservation efforts are effective, though insufficient to offset losses.

**Protected Area Integrity**: Analysis of protected forest reserves showed 8% experienced some encroachment, primarily along boundaries in high-population density regions.

### Visualizations

![Land Cover Distribution](outputs/land_cover_distribution.png)
*Bar charts showing area by land cover class for each time period*

![Change Detection Map](outputs/change_detection_map.png)
*Spatial visualization of pixels that changed land cover class*

![Transition Matrix Heatmap](outputs/transition_matrix.png)
*9x9 matrix showing from-to class transitions with values in km²*

![Deforestation Hotspots](outputs/deforestation_hotspots.png)
*Map highlighting regions with highest tree cover loss rates*

[Interactive Land Cover Map 2024](outputs/kenya_landcover_2024.html)
*Explore current land cover classification across Kenya*

[Transition Flow Visualization](outputs/transition_sankey.html)
*Sankey diagram showing major land cover transitions*

## 🔗 Links

- [Analysis Notebook](analysis.ipynb) - Full Jupyter notebook with executable code
- [ESA Dynamic World](https://dynamicworld.app/) - Dataset documentation and explorer
- [Kenya Forest Service](http://www.kenyaforestservice.org/) - Policy context

## 🏷️ Tags

`land-cover` `deforestation` `kenya` `dynamic-world` `change-detection` `forest-monitoring` `urbanization` `transition-matrix` `earth-engine` `conservation`
