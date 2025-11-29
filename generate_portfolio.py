"""
Portfolio Use Case Generator - Archetype Edition
Generates 36 unique, professional-grade Jupyter notebooks using distinct analytical archetypes.
"""

import os
import json

# Base directory
BASE_DIR = r"c:\Users\damil\OneDrive\Documents\Notebook\Damilola-Portfolio\Projects"

# ======================================================================================
# ARCHETYPE CODE TEMPLATES
# ======================================================================================

# 1. PREDICTIVE CLASSIFICATION (Fraud, Churn, Risk)
CODE_CLASSIFICATION = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "plt.style.use('seaborn-v0_8-whitegrid')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Data Generation\n",
            "def generate_data(n=1000):\n",
            "    np.random.seed(42)\n",
            "    # Generate synthetic features\n",
            "    data = pd.DataFrame({\n",
            "        '{feat1}': np.random.normal(50, 15, n),\n",
            "        '{feat2}': np.random.exponential(10, n),\n",
            "        '{feat3}': np.random.randint(0, 100, n),\n",
            "        '{feat4}': np.random.choice(['A', 'B', 'C'], n)\n",
            "    })\n",
            "    # Generate target with some logic\n",
            "    prob = (data['{feat1}']/100 + data['{feat3}']/200) / 2\n",
            "    data['{target}'] = (prob + np.random.normal(0, 0.1, n) > 0.6).astype(int)\n",
            "    return data\n",
            "\n",
            "df = generate_data({data_points})\n",
            "print(f'Dataset Shape: {{df.shape}}')\n",
            "df.head()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Preprocessing & Modeling\n",
            "class ClassifierEngine:\n",
            "    def __init__(self, df, target):\n",
            "        self.df = df\n",
            "        self.target = target\n",
            "        self.model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
            "        \n",
            "    def train(self):\n",
            "        # Encoding\n",
            "        X = pd.get_dummies(self.df.drop(self.target, axis=1), drop_first=True)\n",
            "        y = self.df[self.target]\n",
            "        \n",
            "        # Split\n",
            "        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)\n",
            "        \n",
            "        # Fit\n",
            "        self.model.fit(self.X_train, self.y_train)\n",
            "        print('Model Trained Successfully')\n",
            "        \n",
            "    def evaluate(self):\n",
            "        preds = self.model.predict(self.X_test)\n",
            "        print(classification_report(self.y_test, preds))\n",
            "        \n",
            "        # Confusion Matrix\n",
            "        plt.figure(figsize=(6,5))\n",
            "        sns.heatmap(confusion_matrix(self.y_test, preds), annot=True, fmt='d', cmap='Blues')\n",
            "        plt.title('Confusion Matrix')\n",
            "        plt.show()\n",
            "\n",
            "engine = ClassifierEngine(df, '{target}')\n",
            "engine.train()\n",
            "engine.evaluate()"
        ]
    }
]

# 2. TIME SERIES FORECASTING (Sales, Demand)
CODE_FORECASTING = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from statsmodels.tsa.holtwinters import ExponentialSmoothing\n",
            "from sklearn.metrics import mean_absolute_error\n",
            "\n",
            "plt.style.use('seaborn-v0_8-darkgrid')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Data Generation\n",
            "def generate_timeseries(n=365):\n",
            "    dates = pd.date_range(start='2023-01-01', periods=n, freq='D')\n",
            "    t = np.arange(n)\n",
            "    # Trend + Seasonality + Noise\n",
            "    trend = 0.5 * t\n",
            "    season = 10 * np.sin(2 * np.pi * t / 30) # Monthly seasonality\n",
            "    noise = np.random.normal(0, 5, n)\n",
            "    values = 100 + trend + season + noise\n",
            "    \n",
            "    return pd.DataFrame({'Date': dates, '{target}': values}).set_index('Date')\n",
            "\n",
            "df = generate_timeseries({data_points})\n",
            "df.plot(figsize=(12,6), title='Historical Data')\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Forecasting Engine\n",
            "class Forecaster:\n",
            "    def __init__(self, df):\n",
            "        self.df = df\n",
            "        self.model = None\n",
            "        \n",
            "    def train_predict(self, days=30):\n",
            "        # Train/Test Split\n",
            "        train = self.df.iloc[:-days]\n",
            "        test = self.df.iloc[-days:]\n",
            "        \n",
            "        # Holt-Winters Exponential Smoothing\n",
            "        self.model = ExponentialSmoothing(train, seasonal='add', seasonal_periods=30).fit()\n",
            "        preds = self.model.forecast(days)\n",
            "        \n",
            "        # Evaluation\n",
            "        mae = mean_absolute_error(test, preds)\n",
            "        print(f'MAE: {mae:.2f}')\n",
            "        \n",
            "        # Plot\n",
            "        plt.figure(figsize=(12,6))\n",
            "        plt.plot(train.index, train, label='Train')\n",
            "        plt.plot(test.index, test, label='Test')\n",
            "        plt.plot(test.index, preds, label='Forecast', linestyle='--')\n",
            "        plt.legend()\n",
            "        plt.title('Forecast vs Actuals')\n",
            "        plt.show()\n",
            "        return preds\n",
            "\n",
            "forecaster = Forecaster(df)\n",
            "forecast = forecaster.train_predict(30)"
        ]
    }
]

# 3. CLUSTERING (Segmentation)
CODE_CLUSTERING = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.cluster import KMeans\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "from sklearn.decomposition import PCA\n",
            "\n",
            "plt.style.use('seaborn-v0_8-muted')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Data Generation\n",
            "def generate_clusters(n=500):\n",
            "    # Generate 3 distinct blobs\n",
            "    c1 = np.random.normal(20, 5, (n//3, 3))\n",
            "    c2 = np.random.normal(50, 10, (n//3, 3))\n",
            "    c3 = np.random.normal(80, 5, (n//3, 3))\n",
            "    data = np.vstack([c1, c2, c3])\n",
            "    \n",
            "    df = pd.DataFrame(data, columns=['{feat1}', '{feat2}', '{feat3}'])\n",
            "    return df\n",
            "\n",
            "df = generate_clusters({data_points})\n",
            "print('Data Generated')\n",
            "df.head()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Clustering Engine\n",
            "class ClusterEngine:\n",
            "    def __init__(self, df):\n",
            "        self.df = df\n",
            "        self.scaler = StandardScaler()\n",
            "        \n",
            "    def find_optimal_k(self):\n",
            "        wcss = []\n",
            "        scaled = self.scaler.fit_transform(self.df)\n",
            "        for i in range(1, 11):\n",
            "            kmeans = KMeans(n_clusters=i, random_state=42)\n",
            "            kmeans.fit(scaled)\n",
            "            wcss.append(kmeans.inertia_)\n",
            "            \n",
            "        plt.plot(range(1, 11), wcss, marker='o')\n",
            "        plt.title('Elbow Method')\n",
            "        plt.show()\n",
            "        \n",
            "    def cluster_and_plot(self, k=3):\n",
            "        scaled = self.scaler.fit_transform(self.df)\n",
            "        kmeans = KMeans(n_clusters=k, random_state=42)\n",
            "        clusters = kmeans.fit_predict(scaled)\n",
            "        self.df['Cluster'] = clusters\n",
            "        \n",
            "        # PCA for visualization\n",
            "        pca = PCA(n_components=2)\n",
            "        components = pca.fit_transform(scaled)\n",
            "        \n",
            "        plt.figure(figsize=(10,6))\n",
            "        sns.scatterplot(x=components[:,0], y=components[:,1], hue=clusters, palette='viridis', s=100)\n",
            "        plt.title(f'Cluster Visualization (K={k})')\n",
            "        plt.show()\n",
            "        return self.df.groupby('Cluster').mean()\n",
            "\n",
            "engine = ClusterEngine(df)\n",
            "engine.find_optimal_k()\n",
            "profile = engine.cluster_and_plot(3)\n",
            "display(profile)"
        ]
    }
]

# 4. HYPOTHESIS TESTING (A/B Testing)
CODE_HYPOTHESIS = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from scipy import stats\n",
            "\n",
            "plt.style.use('seaborn-v0_8-whitegrid')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Data Generation\n",
            "def generate_ab_data(n=1000):\n",
            "    # Control Group\n",
            "    control = np.random.normal(100, 20, n)\n",
            "    # Treatment Group (slightly better)\n",
            "    treatment = np.random.normal(105, 22, n)\n",
            "    \n",
            "    df = pd.DataFrame({\n",
            "        'Group': ['Control']*n + ['Treatment']*n,\n",
            "        '{metric}': np.concatenate([control, treatment])\n",
            "    })\n",
            "    return df\n",
            "\n",
            "df = generate_ab_data({data_points})\n",
            "sns.boxplot(x='Group', y='{metric}', data=df)\n",
            "plt.title('Group Comparison')\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Statistical Analysis\n",
            "control = df[df['Group']=='Control']['{metric}']\n",
            "treatment = df[df['Group']=='Treatment']['{metric}']\n",
            "\n",
            "# T-Test\n",
            "t_stat, p_val = stats.ttest_ind(control, treatment)\n",
            "print(f'T-Statistic: {t_stat:.4f}')\n",
            "print(f'P-Value: {p_val:.4f}')\n",
            "\n",
            "if p_val < 0.05:\n",
            "    print('RESULT: Statistically Significant Difference Detected!')\n",
            "else:\n",
            "    print('RESULT: No Significant Difference.')"
        ]
    }
]

# 5. RASTER RISK ANALYSIS (GIS)
CODE_RASTER_RISK = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "import ee\n",
            "import geemap\n",
            "\n",
            "try:\n",
            "    ee.Initialize()\n",
            "except:\n",
            "    ee.Authenticate()\n",
            "    ee.Initialize()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Define AOI and Datasets\n",
            "AOI = ee.Geometry.Point([9.0820, 8.6753]).buffer(50000)\n",
            "\n",
            "def analyze_risk():\n",
            "    # 1. Elevation (SRTM)\n",
            "    srtm = ee.Image('USGS/SRTMGL1_003').clip(AOI)\n",
            "    elevation = srtm.select('elevation')\n",
            "    slope = ee.Terrain.slope(elevation)\n",
            "    \n",
            "    # 2. Land Cover\n",
            "    landcover = ee.Image('COPERNICUS/Landcover/100m/Proba-V-C3/Global/2019').select('discrete_classification').clip(AOI)\n",
            "    \n",
            "    # 3. Risk Calculation (Simple Weighted Overlay)\n",
            "    # Low elevation + Flat slope = High Flood Risk\n",
            "    risk = elevation.lt(200).And(slope.lt(5))\n",
            "    \n",
            "    # Visualization\n",
            "    m = geemap.Map(center=[9.0820, 8.6753], zoom=9)\n",
            "    m.addLayer(elevation, {'min': 0, 'max': 500}, 'Elevation')\n",
            "    m.addLayer(risk.updateMask(risk), {'palette': ['red']}, 'High Risk Areas')\n",
            "    return m\n",
            "\n",
            "m = analyze_risk()\n",
            "m"
        ]
    }
]

# 6. CHANGE DETECTION (GIS)
CODE_CHANGE_DETECTION = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "import ee\n",
            "import geemap\n",
            "\n",
            "try:\n",
            "    ee.Initialize()\n",
            "except:\n",
            "    ee.Authenticate()\n",
            "    ee.Initialize()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Change Detection Analysis\n",
            "AOI = ee.Geometry.Point([9.0820, 8.6753]).buffer(20000)\n",
            "\n",
            "def detect_changes():\n",
            "    # Load Image Collection\n",
            "    dataset = ee.ImageCollection('{dataset_id}')\n",
            "    \n",
            "    # Year 1\n",
            "    img1 = dataset.filterDate('2020-01-01', '2020-12-31').filterBounds(AOI).select('{band_name}').mean().clip(AOI)\n",
            "    # Year 2\n",
            "    img2 = dataset.filterDate('2023-01-01', '2023-12-31').filterBounds(AOI).select('{band_name}').mean().clip(AOI)\n",
            "    \n",
            "    # Calculate Difference\n",
            "    diff = img2.subtract(img1)\n",
            "    \n",
            "    # Visualization\n",
            "    m = geemap.Map(center=[9.0820, 8.6753], zoom=10)\n",
            "    m.addLayer(img1, {vis_params}, '2020')\n",
            "    m.addLayer(img2, {vis_params}, '2023')\n",
            "    m.addLayer(diff, {'min': -500, 'max': 500, 'palette': ['blue', 'white', 'red']}, 'Difference')\n",
            "    return m\n",
            "\n",
            "m = detect_changes()\n",
            "m"
        ]
    }
]

# 7. VECTOR/NETWORK ANALYSIS (GIS)
CODE_VECTOR = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "import ee\n",
            "import geemap\n",
            "\n",
            "try:\n",
            "    ee.Initialize()\n",
            "except:\n",
            "    ee.Authenticate()\n",
            "    ee.Initialize()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Vector Analysis\n",
            "def analyze_vectors():\n",
            "    # Load Roads (using TIGER lines as proxy for demo)\n",
            "    roads = ee.FeatureCollection('TIGER/2016/Roads').filterBounds(ee.Geometry.Point([-73.9, 40.7]).buffer(10000))\n",
            "    \n",
            "    # Buffer Analysis (Service Areas)\n",
            "    buffers = roads.map(lambda f: f.buffer(500))\n",
            "    \n",
            "    m = geemap.Map(center=[40.7, -73.9], zoom=12)\n",
            "    m.addLayer(roads, {'color': 'blue'}, 'Roads')\n",
            "    m.addLayer(buffers, {'color': 'red', 'opacity': 0.3}, 'Service Buffers')\n",
            "    return m\n",
            "\n",
            "m = analyze_vectors()\n",
            "m"
        ]
    }
]

# 8. OPTIMIZATION/SIMULATION (Sustainability)
CODE_OPTIMIZATION = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "\n",
            "plt.style.use('seaborn-v0_8-paper')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Simulation Engine\n",
            "def run_simulation(n_scenarios=5):\n",
            "    results = []\n",
            "    for i in range(n_scenarios):\n",
            "        # Scenario parameters\n",
            "        efficiency = 0.8 + (i * 0.05)\n",
            "        cost = 1000 * (1.2 - (i * 0.05))\n",
            "        impact = 500 * (1 - (i * 0.1))\n",
            "        \n",
            "        results.append({\n",
            "            'Scenario': f'Scenario {{i+1}}',\n",
            "            'Efficiency': efficiency,\n",
            "            'Cost': cost,\n",
            "            'Environmental_Impact': impact\n",
            "        })\n",
            "    return pd.DataFrame(results)\n",
            "\n",
            "df = run_simulation()\n",
            "print('Simulation Results:')\n",
            "display(df)\n",
            "\n",
            "# Trade-off Visualization\n",
            "fig, ax1 = plt.subplots(figsize=(10,6))\n",
            "sns.barplot(x='Scenario', y='Cost', data=df, ax=ax1, color='lightblue', alpha=0.6)\n",
            "ax2 = ax1.twinx()\n",
            "sns.lineplot(x='Scenario', y='Efficiency', data=df, ax=ax2, color='green', marker='o', linewidth=3)\n",
            "plt.title('Cost vs Efficiency Trade-off')\n",
            "plt.show()"
        ]
    }
]

# ======================================================================================
# USE CASE MAPPING
# ======================================================================================

FULL_USE_CASES = {
    "GIS analytics": [
        {"name": "Flood_Risk_Assessment", "archetype": "RASTER_RISK", "title": "Flood Risk Assessment", "description": "Identify flood-prone areas using elevation and slope.", "params": {}},
        {"name": "Wildfire_Risk_Modeling", "archetype": "RASTER_RISK", "title": "Wildfire Risk Modeling", "description": "Assess wildfire risk based on vegetation and temp.", "params": {}},
        {"name": "Agricultural_Suitability_Analysis", "archetype": "RASTER_RISK", "title": "Agricultural Suitability", "description": "Map optimal crop zones.", "params": {}},
        {"name": "Land_Use_Change_Detection", "archetype": "CHANGE_DETECTION", "title": "Land Use Change Detection", "description": "Monitor urban expansion.", "params": {"dataset_id": "COPERNICUS/S2", "band_name": "B8", "vis_params": "{'min': 0, 'max': 3000}"}},
        {"name": "Urban_Heat_Island_Analysis", "archetype": "CHANGE_DETECTION", "title": "Urban Heat Island Analysis", "description": "Analyze thermal hotspots.", "params": {"dataset_id": "MODIS/006/MOD11A2", "band_name": "LST_Day_1km", "vis_params": "{'min': 14000, 'max': 16000, 'palette': ['blue', 'red']}"}},
        {"name": "Geospatial_Time_Series_Analysis", "archetype": "CHANGE_DETECTION", "title": "Geospatial Time Series", "description": "Track vegetation health over time.", "params": {"dataset_id": "MODIS/006/MOD13Q1", "band_name": "NDVI", "vis_params": "{'min': 0, 'max': 8000, 'palette': ['brown', 'green']}"}},
        {"name": "Transportation_Network_Analysis", "archetype": "VECTOR", "title": "Transportation Network Analysis", "description": "Analyze road connectivity.", "params": {}},
        {"name": "Service_Area_Analysis", "archetype": "VECTOR", "title": "Service Area Analysis", "description": "Map facility coverage.", "params": {}},
        {"name": "Retail_Site_Selection", "archetype": "RASTER_RISK", "title": "Retail Site Selection", "description": "Find optimal store locations.", "params": {}},
        {"name": "Population_Density_Mapping", "archetype": "RASTER_RISK", "title": "Population Density Mapping", "description": "Visualize demographic shifts.", "params": {}},
        {"name": "Spatial_Clustering_Analysis", "archetype": "VECTOR", "title": "Spatial Clustering", "description": "Identify incident clusters.", "params": {}},
        {"name": "Viewshed_Analysis", "archetype": "RASTER_RISK", "title": "Viewshed Analysis", "description": "Calculate visibility.", "params": {}}
    ],
    "Sustainability Data Analytics": [
        {"name": "Carbon_Footprint_Assessment", "archetype": "OPTIMIZATION", "title": "Carbon Footprint Assessment", "description": "Track and optimize emissions.", "params": {}},
        {"name": "Renewable_Energy_Potential", "archetype": "OPTIMIZATION", "title": "Renewable Energy Potential", "description": "Simulate energy output.", "params": {}},
        {"name": "Water_Resource_Management", "archetype": "FORECASTING", "title": "Water Resource Management", "description": "Forecast water usage.", "params": {"target": "Water_Usage_Liters", "data_points": 730}},
        {"name": "Waste_Management_Optimization", "archetype": "OPTIMIZATION", "title": "Waste Management Optimization", "description": "Optimize collection routes.", "params": {}},
        {"name": "Sustainable_Supply_Chain", "archetype": "CLASSIFICATION", "title": "Sustainable Supply Chain", "description": "Classify supplier risk.", "params": {"feat1": "Distance", "feat2": "Emissions", "feat3": "Cost", "feat4": "Region", "target": "High_Risk", "data_points": 500}},
        {"name": "Air_Quality_Monitoring", "archetype": "FORECASTING", "title": "Air Quality Monitoring", "description": "Predict PM2.5 levels.", "params": {"target": "PM2.5_Level", "data_points": 1000}},
        {"name": "Biodiversity_Impact_Assessment", "archetype": "OPTIMIZATION", "title": "Biodiversity Impact Assessment", "description": "Assess habitat scenarios.", "params": {}},
        {"name": "Circular_Economy_Metrics", "archetype": "OPTIMIZATION", "title": "Circular Economy Metrics", "description": "Track material loops.", "params": {}},
        {"name": "ESG_Performance_Scoring", "archetype": "CLUSTERING", "title": "ESG Performance Scoring", "description": "Cluster companies by ESG score.", "params": {"feat1": "Env_Score", "feat2": "Social_Score", "feat3": "Gov_Score", "data_points": 200}},
        {"name": "Green_Building_Certification", "archetype": "CLASSIFICATION", "title": "Green Building Certification", "description": "Predict certification success.", "params": {"feat1": "Energy_Use", "feat2": "Water_Use", "feat3": "Materials", "feat4": "Type", "target": "Certified", "data_points": 300}},
        {"name": "Ocean_Pollution_Tracking", "archetype": "FORECASTING", "title": "Ocean Pollution Tracking", "description": "Forecast debris accumulation.", "params": {"target": "Debris_Tons", "data_points": 500}},
        {"name": "Sustainable_Agriculture_Metrics", "archetype": "HYPOTHESIS", "title": "Sustainable Agriculture", "description": "Compare crop yields.", "params": {"metric": "Yield_Per_Hectare", "data_points": 200}}
    ],
    "Data analytics": [
        {"name": "Customer_Segmentation", "archetype": "CLUSTERING", "title": "Customer Segmentation", "description": "Segment users by behavior.", "params": {"feat1": "Recency", "feat2": "Frequency", "feat3": "Monetary", "data_points": 2000}},
        {"name": "Sales_Forecasting", "archetype": "FORECASTING", "title": "Sales Forecasting", "description": "Predict future revenue.", "params": {"target": "Revenue", "data_points": 1095}},
        {"name": "Marketing_Campaign_Performance", "archetype": "HYPOTHESIS", "title": "Marketing Campaign Analysis", "description": "A/B test campaigns.", "params": {"metric": "Conversion_Rate", "data_points": 5000}},
        {"name": "Product_Recommendation_System", "archetype": "CLUSTERING", "title": "Product Recommendation", "description": "Group similar items.", "params": {"feat1": "Price", "feat2": "Rating", "feat3": "Popularity", "data_points": 500}},
        {"name": "Financial_Risk_Assessment", "archetype": "CLASSIFICATION", "title": "Financial Risk Assessment", "description": "Predict credit default.", "params": {"feat1": "Income", "feat2": "Debt", "feat3": "Credit_Score", "feat4": "Employment", "target": "Default", "data_points": 5000}},
        {"name": "Employee_Attrition_Prediction", "archetype": "CLASSIFICATION", "title": "Employee Attrition Prediction", "description": "Predict turnover.", "params": {"feat1": "Satisfaction", "feat2": "Tenure", "feat3": "Salary", "feat4": "Dept", "target": "Left", "data_points": 1500}},
        {"name": "Inventory_Optimization", "archetype": "FORECASTING", "title": "Inventory Optimization", "description": "Forecast stock levels.", "params": {"target": "Stock_Level", "data_points": 730}},
        {"name": "AB_Testing_Analysis", "archetype": "HYPOTHESIS", "title": "A/B Testing Analysis", "description": "Compare page variants.", "params": {"metric": "Click_Through_Rate", "data_points": 10000}},
        {"name": "Sentiment_Analysis", "archetype": "CLASSIFICATION", "title": "Sentiment Analysis", "description": "Classify text sentiment.", "params": {"feat1": "Word_Count", "feat2": "Polarity", "feat3": "Subjectivity", "feat4": "Source", "target": "Positive_Sentiment", "data_points": 2000}},
        {"name": "Demand_Forecasting", "archetype": "FORECASTING", "title": "Demand Forecasting", "description": "Predict product demand.", "params": {"target": "Units_Sold", "data_points": 1000}},
        {"name": "Price_Optimization", "archetype": "OPTIMIZATION", "title": "Price Optimization", "description": "Simulate pricing scenarios.", "params": {}},
        {"name": "Fraud_Detection", "archetype": "CLASSIFICATION", "title": "Fraud Detection", "description": "Detect fraudulent txns.", "params": {"feat1": "Amount", "feat2": "Time_Diff", "feat3": "Location_Score", "feat4": "Type", "target": "Is_Fraud", "data_points": 10000}}
    ]
}

# ======================================================================================
# GENERATOR LOGIC
# ======================================================================================

def generate_notebook_content(domain, use_case):
    """Generates notebook content based on archetype."""
    archetype = use_case['archetype']
    params = use_case['params']
    
    # Select Template
    if archetype == "CLASSIFICATION":
        template_cells = CODE_CLASSIFICATION
    elif archetype == "FORECASTING":
        template_cells = CODE_FORECASTING
    elif archetype == "CLUSTERING":
        template_cells = CODE_CLUSTERING
    elif archetype == "HYPOTHESIS":
        template_cells = CODE_HYPOTHESIS
    elif archetype == "RASTER_RISK":
        template_cells = CODE_RASTER_RISK
    elif archetype == "CHANGE_DETECTION":
        template_cells = CODE_CHANGE_DETECTION
    elif archetype == "VECTOR":
        template_cells = CODE_VECTOR
    elif archetype == "OPTIMIZATION":
        template_cells = CODE_OPTIMIZATION
    else:
        template_cells = CODE_CLASSIFICATION # Default
        
    # Header Cell
    header_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# {use_case['title']}\n\n",
            f"## 📊 Business Context\n{use_case['description']}\n\n",
            f"**Analytical Approach:** {archetype.replace('_', ' ').title()}\n",
            "This notebook utilizes advanced analytics to derive actionable insights."
        ]
    }
    
    # Process Cells
    final_cells = [header_cell]
    for cell in template_cells:
        new_source = []
        for line in cell['source']:
            # Inject Params
            for k, v in params.items():
                line = line.replace(f'{{{k}}}', str(v))
            new_source.append(line)
        
        final_cells.append({
            "cell_type": cell['cell_type'],
            "metadata": cell['metadata'],
            "source": new_source
        })
        
    # Construct Notebook
    notebook = {
        "cells": final_cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.8.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return json.dumps(notebook, indent=1)

def generate_readme(domain, use_case):
    return f"# {use_case['title']}\n\n{use_case['description']}\n\nGenerated using {use_case['archetype']} archetype."

def main():
    print("Generating Archetype-Based Portfolio...")
    
    for domain, cases in FULL_USE_CASES.items():
        print(f"Processing {domain}...")
        domain_path = os.path.join(BASE_DIR, domain)
        if not os.path.exists(domain_path):
            os.makedirs(domain_path)
            
        for use_case in cases:
            case_path = os.path.join(domain_path, use_case['name'])
            if not os.path.exists(case_path):
                os.makedirs(case_path)
            
            # Create outputs dir
            if not os.path.exists(os.path.join(case_path, "outputs")):
                os.makedirs(os.path.join(case_path, "outputs"))
                
            # Generate Notebook
            nb_content = generate_notebook_content(domain, use_case)
            with open(os.path.join(case_path, "analysis.ipynb"), 'w', encoding='utf-8') as f:
                f.write(nb_content)
                
            # Generate README
            readme_content = generate_readme(domain, use_case)
            with open(os.path.join(case_path, "README.md"), 'w', encoding='utf-8') as f:
                f.write(readme_content)
                
            print(f"  - Created {use_case['name']} ({use_case['archetype']})")

if __name__ == "__main__":
    main()
