# Land Cover Analysis & Visualization (Nigeria)

## Project Overview
This project analyzes land cover changes in **Nigeria** from **2020 to 2024** using **ESA Dynamic World** data. The analysis is performed using Google Earth Engine (GEE) and Python.

The goal is to understand how land use patterns are shifting over time, with a specific focus on deforestation, urbanization, and agricultural expansion.

## Key Features

### 1. Interactive Area Charts
Visualizes the total area (in hectares) for each land cover class (Trees, Crops, Built Area, etc.) over the 5-year period. This allows for quick identification of major trends.

### 2. Land Cover Maps & Change Detection
- **Annual Maps**: Displays land cover classification for any selected year.
- **Change Detection**: Highlights specific pixels that have changed class between the start and end years, providing a spatial view of dynamic areas.

### 3. Transition Matrix & Robust Insights
A detailed transition matrix quantifies exactly how much land has moved from one class to another. The analysis automatically generates a report on:
- **Deforestation**: Tracking the conversion of forests to crops, bare ground, or built-up areas.
- **Urbanization**: Measuring the expansion of built-up areas (cities, towns, infrastructure).
- **Agricultural Expansion**: Quantifying the increase in crop areas.
- **Forest Regrowth**: Identifying areas where tree cover has increased.

## Usage
1.  Open `LandCover_Analysis_Nigeria.ipynb` in Jupyter Notebook or VS Code.
2.  Ensure you have the required packages installed:
    ```bash
    pip install geemap earthengine-api rasterio geopandas matplotlib numpy seaborn pandas folium ipyleaflet altair
    ```
3.  Run the cells sequentially. You may need to authenticate with Google Earth Engine on the first run.

## Data Source
- **ESA Dynamic World V1**: A near real-time 10m resolution global land use/land cover dataset.
