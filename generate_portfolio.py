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
            "from sklearn.model_selection import train_test_split, cross_val_score\n",
            "from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, precision_recall_curve\n",
            "from sklearn.preprocessing import StandardScaler, LabelEncoder\n",
            "from sklearn.impute import SimpleImputer\n",
            "\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
            "\n",
            "plt.style.use('seaborn-v0_8-whitegrid')\n",
            "sns.set_palette('viridis')"
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
            "        '{feat4}': np.random.choice(['A', 'B', 'C'], n, p=[0.5, 0.3, 0.2]),\n",
            "        'Tenure': np.random.randint(1, 60, n),\n",
            "        'Age': np.random.normal(35, 10, n)\n",
            "    })\n",
            "    \n",
            "    # Introduce some missing values\n",
            "    data.loc[np.random.choice(data.index, size=int(n*0.05)), '{feat1}'] = np.nan\n",
            "    \n",
            "    # Generate target with complex logic\n",
            "    prob = (data['{feat1}'].fillna(50)/100 + data['{feat3}']/200) / 2\n",
            "    prob += np.where(data['{feat4}'] == 'C', 0.2, 0)\n",
            "    prob -= data['Tenure'] / 100\n",
            "    \n",
            "    data['{target}'] = (prob + np.random.normal(0, 0.1, n) > 0.55).astype(int)\n",
            "    return data\n",
            "\n",
            "df = generate_data({data_points})\n",
            "print(f'Dataset Shape: {df.shape}')\n",
            "display(df.head())\n",
            "display(df.describe())"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Exploratory Data Analysis (EDA)\n",
            "def perform_eda(df, target):\n",
            "    fig, axes = plt.subplots(2, 2, figsize=(15, 10))\n",
            "    \n",
            "    # Target Distribution\n",
            "    sns.countplot(x=target, data=df, ax=axes[0,0])\n",
            "    axes[0,0].set_title('Target Distribution')\n",
            "    \n",
            "    # Numerical Feature Distribution\n",
            "    sns.histplot(data=df, x='{feat1}', hue=target, kde=True, ax=axes[0,1])\n",
            "    axes[0,1].set_title('Feature 1 Distribution by Target')\n",
            "    \n",
            "    # Categorical Feature\n",
            "    sns.countplot(x='{feat4}', hue=target, data=df, ax=axes[1,0])\n",
            "    axes[1,0].set_title('Feature 4 vs Target')\n",
            "    \n",
            "    # Correlation Heatmap\n",
            "    numeric_cols = df.select_dtypes(include=[np.number]).columns\n",
            "    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=axes[1,1])\n",
            "    axes[1,1].set_title('Correlation Matrix')\n",
            "    \n",
            "    plt.tight_layout()\n",
            "    plt.show()\n",
            "\n",
            "perform_eda(df, '{target}')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Preprocessing & Feature Engineering\n",
            "class DataPreprocessor:\n",
            "    def __init__(self, df, target):\n",
            "        self.df = df.copy()\n",
            "        self.target = target\n",
            "        self.scaler = StandardScaler()\n",
            "        self.imputer = SimpleImputer(strategy='median')\n",
            "        \n",
            "    def process(self):\n",
            "        # Handle Missing Values\n",
            "        num_cols = self.df.select_dtypes(include=[np.number]).columns.drop(self.target)\n",
            "        self.df[num_cols] = self.imputer.fit_transform(self.df[num_cols])\n",
            "        \n",
            "        # Feature Engineering\n",
            "        self.df['Interaction_1_3'] = self.df['{feat1}'] * self.df['{feat3}']\n",
            "        \n",
            "        # Encoding\n",
            "        self.df = pd.get_dummies(self.df, drop_first=True)\n",
            "        \n",
            "        # Split\n",
            "        X = self.df.drop(self.target, axis=1)\n",
            "        y = self.df[self.target]\n",
            "        \n",
            "        # Scaling\n",
            "        X_scaled = pd.DataFrame(self.scaler.fit_transform(X), columns=X.columns)\n",
            "        \n",
            "        return train_test_split(X_scaled, y, test_size=0.2, random_state=42)\n",
            "\n",
            "processor = DataPreprocessor(df, '{target}')\n",
            "X_train, X_test, y_train, y_test = processor.process()\n",
            "print('Data Processed. Train Shape:', X_train.shape)"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Model Training & Comparison\n",
            "models = {\n",
            "    'Logistic Regression': LogisticRegression(),\n",
            "    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),\n",
            "    'Gradient Boosting': GradientBoostingClassifier(random_state=42)\n",
            "}\n",
            "\n",
            "results = {}\n",
            "\n",
            "for name, model in models.items():\n",
            "    model.fit(X_train, y_train)\n",
            "    score = model.score(X_test, y_test)\n",
            "    results[name] = score\n",
            "    print(f'{name} Accuracy: {score:.4f}')\n",
            "\n",
            "best_model_name = max(results, key=results.get)\n",
            "best_model = models[best_model_name]\n",
            "print(f'\\nBest Model: {best_model_name}')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Detailed Evaluation\n",
            "y_pred = best_model.predict(X_test)\n",
            "y_prob = best_model.predict_proba(X_test)[:, 1]\n",
            "\n",
            "print('Classification Report:\\n')\n",
            "print(classification_report(y_test, y_pred))\n",
            "\n",
            "fig, axes = plt.subplots(1, 2, figsize=(14, 6))\n",
            "\n",
            "# Confusion Matrix\n",
            "sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', ax=axes[0])\n",
            "axes[0].set_title(f'Confusion Matrix ({best_model_name})')\n",
            "\n",
            "# ROC Curve\n",
            "fpr, tpr, _ = roc_curve(y_test, y_prob)\n",
            "roc_auc = auc(fpr, tpr)\n",
            "axes[1].plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')\n",
            "axes[1].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')\n",
            "axes[1].set_xlabel('False Positive Rate')\n",
            "axes[1].set_ylabel('True Positive Rate')\n",
            "axes[1].set_title('Receiver Operating Characteristic')\n",
            "axes[1].legend(loc='lower right')\n",
            "\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Feature Importance\n",
            "if hasattr(best_model, 'feature_importances_'):\n",
            "    importances = pd.DataFrame({\n",
            "        'feature': X_train.columns,\n",
            "        'importance': best_model.feature_importances_\n",
            "    }).sort_values('importance', ascending=False)\n",
            "    \n",
            "    plt.figure(figsize=(10, 6))\n",
            "    sns.barplot(x='importance', y='feature', data=importances.head(10), palette='viridis')\n",
            "    plt.title('Top 10 Feature Importance')\n",
            "    plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 💡 Business Recommendations\n",
            "\n",
            "Based on the analysis, we recommend:\n",
            "\n",
            "1. **Target High-Risk Segments**: Focus retention efforts on customers with high `{feat1}` and low tenure.\n",
            "2. **Monitor Key Indicators**: The top features identified (e.g., `{feat1}`) should be tracked on a dashboard.\n",
            "3. **Intervention Strategy**: Implement proactive outreach for customers showing patterns similar to the 'Churn' class."
        ]
    }
]

# 2. TIME SERIES FORECASTING (Sales, Demand)
CODE_FORECASTING = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from statsmodels.tsa.seasonal import seasonal_decompose\n",
            "from statsmodels.tsa.holtwinters import ExponentialSmoothing\n",
            "from statsmodels.tsa.stattools import adfuller, acf, pacf\n",
            "from statsmodels.graphics.tsaplots import plot_acf, plot_pacf\n",
            "from sklearn.metrics import mean_absolute_error, mean_squared_error\n",
            "\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
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
            "    np.random.seed(42)\n",
            "    dates = pd.date_range(start='2022-01-01', periods=n, freq='D')\n",
            "    t = np.arange(n)\n",
            "    \n",
            "    # Components\n",
            "    trend = 0.5 * t\n",
            "    season = 20 * np.sin(2 * np.pi * t / 30) + 10 * np.sin(2 * np.pi * t / 7) # Monthly + Weekly\n",
            "    noise = np.random.normal(0, 5, n)\n",
            "    events = np.zeros(n)\n",
            "    events[::60] = 50 # Spikes every 2 months\n",
            "    \n",
            "    values = 100 + trend + season + noise + events\n",
            "    \n",
            "    return pd.DataFrame({'Date': dates, '{target}': values}).set_index('Date')\n",
            "\n",
            "df = generate_timeseries({data_points})\n",
            "print(f'Time Series Length: {len(df)} days')\n",
            "df.plot(figsize=(14,6), title='Historical Data', linewidth=1)\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Exploratory Data Analysis (EDA)\n",
            "def analyze_timeseries(df, target):\n",
            "    # 1. Decomposition\n",
            "    decomposition = seasonal_decompose(df[target], model='additive', period=30)\n",
            "    fig = decomposition.plot()\n",
            "    fig.set_size_inches(12, 8)\n",
            "    plt.show()\n",
            "    \n",
            "    # 2. Stationarity Test (ADF)\n",
            "    result = adfuller(df[target])\n",
            "    print('ADF Statistic:', result[0])\n",
            "    print('p-value:', result[1])\n",
            "    if result[1] < 0.05:\n",
            "        print('Result: Series is Stationary')\n",
            "    else:\n",
            "        print('Result: Series is Non-Stationary (Differencing may be needed)')\n",
            "        \n",
            "    # 3. ACF & PACF\n",
            "    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))\n",
            "    plot_acf(df[target], ax=ax1, lags=40)\n",
            "    plot_pacf(df[target], ax=ax2, lags=40)\n",
            "    plt.show()\n",
            "\n",
            "analyze_timeseries(df, '{target}')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Forecasting Engine\n",
            "class Forecaster:\n",
            "    def __init__(self, df, target):\n",
            "        self.df = df\n",
            "        self.target = target\n",
            "        self.models = {}\n",
            "        \n",
            "    def train_evaluate(self, test_days=30):\n",
            "        # Split\n",
            "        train = self.df.iloc[:-test_days]\n",
            "        test = self.df.iloc[-test_days:]\n",
            "        \n",
            "        # Model 1: Holt-Winters (Triple Exponential Smoothing)\n",
            "        hw_model = ExponentialSmoothing(\n",
            "            train[self.target], \n",
            "            seasonal_periods=30, \n",
            "            trend='add', \n",
            "            seasonal='add'\n",
            "        ).fit()\n",
            "        self.models['Holt-Winters'] = hw_model.forecast(test_days)\n",
            "        \n",
            "        # Model 2: Simple Moving Average (Baseline)\n",
            "        self.models['Moving Average (7D)'] = test.copy()\n",
            "        self.models['Moving Average (7D)'][self.target] = train[self.target].rolling(window=7).mean().iloc[-1]\n",
            "        self.models['Moving Average (7D)'] = self.models['Moving Average (7D)'][self.target]\n",
            "        \n",
            "        # Evaluation\n",
            "        results = []\n",
            "        plt.figure(figsize=(14, 7))\n",
            "        plt.plot(train.index[-60:], train[self.target][-60:], label='Train (Last 60 Days)')\n",
            "        plt.plot(test.index, test[self.target], label='Actual Test', color='black', linewidth=2)\n",
            "        \n",
            "        for name, preds in self.models.items():\n",
            "            mae = mean_absolute_error(test[self.target], preds)\n",
            "            rmse = np.sqrt(mean_squared_error(test[self.target], preds))\n",
            "            results.append({'Model': name, 'MAE': mae, 'RMSE': rmse})\n",
            "            \n",
            "            plt.plot(test.index, preds, label=f'{name} (MAE={mae:.1f})', linestyle='--')\n",
            "            \n",
            "        plt.title('Forecast Model Comparison')\n",
            "        plt.legend()\n",
            "        plt.show()\n",
            "        \n",
            "        return pd.DataFrame(results)\n",
            "\n",
            "forecaster = Forecaster(df, '{target}')\n",
            "metrics = forecaster.train_evaluate(test_days=30)\n",
            "display(metrics)"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Future Forecast\n",
            "best_model_name = metrics.sort_values('MAE').iloc[0]['Model']\n",
            "print(f'Generating future forecast using best model: {best_model_name}')\n",
            "\n",
            "# Refit on full data\n",
            "final_model = ExponentialSmoothing(\n",
            "    df['{target}'], \n",
            "    seasonal_periods=30, \n",
            "    trend='add', \n",
            "    seasonal='add'\n",
            ").fit()\n",
            "\n",
            "future_days = 60\n",
            "future_forecast = final_model.forecast(future_days)\n",
            "\n",
            "plt.figure(figsize=(14, 6))\n",
            "plt.plot(df.index[-90:], df['{target}'][-90:], label='Historical (Last 90 Days)')\n",
            "plt.plot(future_forecast.index, future_forecast, label='Future Forecast', color='green', linestyle='--')\n",
            "plt.title(f'Future {future_days}-Day Forecast')\n",
            "plt.legend()\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 📈 Strategic Insights\n",
            "\n",
            "1. **Trend Analysis**: The overall trend indicates a steady increase/decrease, suggesting...\n",
            "2. **Seasonality**: Strong monthly patterns observed. Peak demand occurs around...\n",
            "3. **Anomalies**: Spikes in the data correlate with specific events, requiring buffer stock planning.\n",
            "4. **Action Plan**: Optimize inventory levels based on the 30-day forecast to reduce holding costs."
        ]
    }
]

# 3. CLUSTERING (Segmentation)
CODE_CLUSTERING = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.cluster import KMeans, DBSCAN\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "from sklearn.decomposition import PCA\n",
            "from sklearn.metrics import silhouette_score\n",
            "\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
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
            "    np.random.seed(42)\n",
            "    # Generate 4 distinct blobs with some overlap\n",
            "    c1 = np.random.normal(20, 5, (n//4, 3))\n",
            "    c2 = np.random.normal(50, 10, (n//4, 3))\n",
            "    c3 = np.random.normal(80, 5, (n//4, 3))\n",
            "    c4 = np.random.normal(35, 15, (n//4, 3)) # Noisier cluster\n",
            "    \n",
            "    data = np.vstack([c1, c2, c3, c4])\n",
            "    df = pd.DataFrame(data, columns=['{feat1}', '{feat2}', '{feat3}'])\n",
            "    \n",
            "    # Add a categorical feature\n",
            "    df['Region'] = np.random.choice(['North', 'South', 'East', 'West'], size=len(df))\n",
            "    \n",
            "    return df\n",
            "\n",
            "df = generate_clusters({data_points})\n",
            "print('Dataset Shape:', df.shape)\n",
            "display(df.head())\n",
            "display(df.describe())"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Exploratory Data Analysis (EDA)\n",
            "def perform_eda(df):\n",
            "    # Pairplot to see potential clusters\n",
            "    sns.pairplot(df, hue='Region', diag_kind='kde', corner=True)\n",
            "    plt.suptitle('Feature Pairplot', y=1.02)\n",
            "    plt.show()\n",
            "    \n",
            "    # Correlation\n",
            "    plt.figure(figsize=(8, 6))\n",
            "    numeric_cols = df.select_dtypes(include=[np.number]).columns\n",
            "    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')\n",
            "    plt.title('Correlation Matrix')\n",
            "    plt.show()\n",
            "\n",
            "perform_eda(df)"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Clustering Engine\n",
            "class ClusterEngine:\n",
            "    def __init__(self, df):\n",
            "        self.raw_df = df\n",
            "        self.numeric_cols = df.select_dtypes(include=[np.number]).columns\n",
            "        self.scaler = StandardScaler()\n",
            "        self.scaled_data = self.scaler.fit_transform(df[self.numeric_cols])\n",
            "        \n",
            "    def find_optimal_k(self):\n",
            "        wcss = []\n",
            "        sil_scores = []\n",
            "        K = range(2, 11)\n",
            "        \n",
            "        for k in K:\n",
            "            kmeans = KMeans(n_clusters=k, random_state=42)\n",
            "            kmeans.fit(self.scaled_data)\n",
            "            wcss.append(kmeans.inertia_)\n",
            "            sil_scores.append(silhouette_score(self.scaled_data, kmeans.labels_))\n",
            "            \n",
            "        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))\n",
            "        \n",
            "        # Elbow Method\n",
            "        ax1.plot(K, wcss, 'bo-')\n",
            "        ax1.set_title('Elbow Method')\n",
            "        ax1.set_xlabel('Number of Clusters (k)')\n",
            "        ax1.set_ylabel('WCSS')\n",
            "        \n",
            "        # Silhouette Score\n",
            "        ax2.plot(K, sil_scores, 'ro-')\n",
            "        ax2.set_title('Silhouette Score Analysis')\n",
            "        ax2.set_xlabel('Number of Clusters (k)')\n",
            "        ax2.set_ylabel('Silhouette Score')\n",
            "        \n",
            "        plt.show()\n",
            "        \n",
            "    def create_clusters(self, k=3):\n",
            "        kmeans = KMeans(n_clusters=k, random_state=42)\n",
            "        clusters = kmeans.fit_predict(self.scaled_data)\n",
            "        self.raw_df['Cluster'] = clusters\n",
            "        \n",
            "        # PCA Visualization\n",
            "        pca = PCA(n_components=2)\n",
            "        components = pca.fit_transform(self.scaled_data)\n",
            "        \n",
            "        plt.figure(figsize=(10, 6))\n",
            "        sns.scatterplot(x=components[:,0], y=components[:,1], hue=clusters, palette='viridis', s=100, alpha=0.8)\n",
            "        plt.title(f'Cluster Visualization (PCA) - K={k}')\n",
            "        plt.xlabel('PC1')\n",
            "        plt.ylabel('PC2')\n",
            "        plt.show()\n",
            "        \n",
            "        return self.raw_df\n",
            "\n",
            "engine = ClusterEngine(df)\n",
            "engine.find_optimal_k()"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Apply Clustering (Choosing Optimal K based on plots)\n",
            "final_df = engine.create_clusters(k=4)\n",
            "\n",
            "# Cluster Profiling\n",
            "cluster_means = final_df.groupby('Cluster')[engine.numeric_cols].mean()\n",
            "\n",
            "# Heatmap of Cluster Centers\n",
            "plt.figure(figsize=(10, 6))\n",
            "sns.heatmap(cluster_means.T, cmap='YlGnBu', annot=True, fmt='.2f')\n",
            "plt.title('Cluster Profiling: Feature Means by Cluster')\n",
            "plt.show()\n",
            "\n",
            "display(cluster_means)"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 🧩 Segment Profiles\n",
            "\n",
            "Based on the analysis, we identified 4 distinct segments:\n",
            "\n",
            "1. **Cluster 0**: High `{feat1}`, Moderate `{feat2}`. Likely represents...\n",
            "2. **Cluster 1**: Low across all features. Potential churn risk or low-value segment.\n",
            "3. **Cluster 2**: High `{feat3}`. Niche segment focused on...\n",
            "4. **Cluster 3**: Balanced profile. Core customer base.\n",
            "\n",
            "**Recommendation**: Tailor marketing campaigns specifically for Cluster 0 to maximize ROI."
        ]
    }
]

# 4. HYPOTHESIS TESTING (A/B Testing)
CODE_HYPOTHESIS = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from scipy import stats\n",
            "from statsmodels.stats.power import TTestIndPower\n",
            "\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
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
            "    np.random.seed(42)\n",
            "    # Control Group (Baseline)\n",
            "    control = np.random.normal(100, 20, n)\n",
            "    # Treatment Group (Intervention - slight uplift)\n",
            "    treatment = np.random.normal(103, 22, n)\n",
            "    \n",
            "    # Create DataFrame\n",
            "    df = pd.DataFrame({\n",
            "        'Group': ['Control']*n + ['Treatment']*n,\n",
            "        '{metric}': np.concatenate([control, treatment])\n",
            "    })\n",
            "    return df\n",
            "\n",
            "df = generate_ab_data({data_points})\n",
            "print('Dataset Shape:', df.shape)\n",
            "print('Group Sizes:\\n', df['Group'].value_counts())\n",
            "display(df.groupby('Group')['{metric}'].describe())"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Exploratory Data Analysis (EDA)\n",
            "def visualize_groups(df, metric):\n",
            "    fig, axes = plt.subplots(1, 2, figsize=(14, 6))\n",
            "    \n",
            "    # Boxplot with Swarm\n",
            "    sns.boxplot(x='Group', y=metric, data=df, ax=axes[0], palette='Set2')\n",
            "    axes[0].set_title('Distribution Comparison (Boxplot)')\n",
            "    \n",
            "    # KDE Plot\n",
            "    sns.kdeplot(data=df, x=metric, hue='Group', fill=True, ax=axes[1], palette='Set2')\n",
            "    axes[1].set_title('Density Distribution (KDE)')\n",
            "    \n",
            "    plt.show()\n",
            "\n",
            "visualize_groups(df, '{metric}')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Statistical Analysis Engine\n",
            "class ABTestEngine:\n",
            "    def __init__(self, df, metric):\n",
            "        self.control = df[df['Group']=='Control'][metric]\n",
            "        self.treatment = df[df['Group']=='Treatment'][metric]\n",
            "        \n",
            "    def check_assumptions(self):\n",
            "        print('--- Assumption Checks ---')\n",
            "        # 1. Normality (Shapiro-Wilk)\n",
            "        # Note: For large N, T-test is robust, but good to check\n",
            "        _, p_c = stats.shapiro(self.control)\n",
            "        _, p_t = stats.shapiro(self.treatment)\n",
            "        print(f'Shapiro-Wilk (Control): p={p_c:.4f}')\n",
            "        print(f'Shapiro-Wilk (Treatment): p={p_t:.4f}')\n",
            "        \n",
            "        # 2. Homogeneity of Variance (Levene)\n",
            "        _, p_l = stats.levene(self.control, self.treatment)\n",
            "        print(f'Levene Test: p={p_l:.4f}')\n",
            "        if p_l < 0.05:\n",
            "            print('-> Variances are NOT equal (Use Welch\\'s T-test)')\n",
            "            return False # Equal var is False\n",
            "        else:\n",
            "            print('-> Variances are equal')\n",
            "            return True\n",
            "            \n",
            "    def run_test(self, equal_var=True):\n",
            "        print('\\n--- Hypothesis Test Results ---')\n",
            "        t_stat, p_val = stats.ttest_ind(self.control, self.treatment, equal_var=equal_var)\n",
            "        \n",
            "        print(f'T-Statistic: {t_stat:.4f}')\n",
            "        print(f'P-Value: {p_val:.4f}')\n",
            "        \n",
            "        # Effect Size (Cohen\\'s d)\n",
            "        n1, n2 = len(self.control), len(self.treatment)\n",
            "        s1, s2 = np.var(self.control, ddof=1), np.var(self.treatment, ddof=1)\n",
            "        s_pooled = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))\n",
            "        cohens_d = (np.mean(self.control) - np.mean(self.treatment)) / s_pooled\n",
            "        \n",
            "        print(f'Cohen\\'s d (Effect Size): {abs(cohens_d):.4f}')\n",
            "        \n",
            "        if p_val < 0.05:\n",
            "            print('\\n✅ RESULT: Statistically Significant Difference Detected!')\n",
            "            print(f'The treatment group mean ({np.mean(self.treatment):.2f}) is significantly different from control ({np.mean(self.control):.2f}).')\n",
            "        else:\n",
            "            print('\\n❌ RESULT: No Significant Difference.')\n",
            "            \n",
            "        # Power Analysis\n",
            "        analysis = TTestIndPower()\n",
            "        power = analysis.solve_power(effect_size=abs(cohens_d), nobs1=n1, ratio=1.0, alpha=0.05)\n",
            "        print(f'Statistical Power: {power:.4f}')\n",
            "\n",
            "engine = ABTestEngine(df, '{metric}')\n",
            "equal_variance = engine.check_assumptions()\n",
            "engine.run_test(equal_var=equal_variance)"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 🧪 Conclusion & Recommendations\n",
            "\n",
            "1. **Significance**: The analysis shows a p-value of ... indicating...\n",
            "2. **Effect Size**: The observed effect size (Cohen's d) suggests a [Small/Medium/Large] practical difference.\n",
            "3. **Business Impact**: If implemented, this change could lead to a ...% improvement in `{metric}`.\n",
            "4. **Recommendation**: Proceed with full rollout / Iterate on the design."
        ]
    }
]

# 5. RASTER RISK ANALYSIS (GIS)
CODE_RASTER_RISK = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import ee\n",
            "import geemap\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "import pandas as pd\n",
            "\n",
            "# Initialize Earth Engine\n",
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
            "# Define Area of Interest (AOI)\n",
            "# Using a sample coordinate (e.g., Lagos, Nigeria or similar)\n",
            "AOI = ee.Geometry.Point([3.3792, 6.5244]).buffer(20000)\n",
            "\n",
            "def analyze_risk():\n",
            "    print('Loading datasets...')\n",
            "    # 1. Elevation (SRTM)\n",
            "    srtm = ee.Image('USGS/SRTMGL1_003').clip(AOI)\n",
            "    elevation = srtm.select('elevation')\n",
            "    slope = ee.Terrain.slope(elevation)\n",
            "    \n",
            "    # 2. Land Cover (ESA WorldCover)\n",
            "    landcover = ee.ImageCollection('ESA/WorldCover/v100').first().clip(AOI)\n",
            "    \n",
            "    # 3. Risk Calculation Logic\n",
            "    # Example: Flood Risk = Low Elevation (< 10m) AND Flat Slope (< 5 deg)\n",
            "    low_elevation = elevation.lt(10)\n",
            "    flat_slope = slope.lt(5)\n",
            "    \n",
            "    # Weighted Overlay\n",
            "    risk_score = low_elevation.multiply(0.6).add(flat_slope.multiply(0.4))\n",
            "    high_risk = risk_score.gt(0.8)\n",
            "    \n",
            "    # Calculate Risk Area\n",
            "    area_image = high_risk.multiply(ee.Image.pixelArea())\n",
            "    stats = area_image.reduceRegion(\n",
            "        reducer=ee.Reducer.sum(),\n",
            "        geometry=AOI,\n",
            "        scale=30,\n",
            "        maxPixels=1e9\n",
            "    )\n",
            "    risk_area_sqkm = stats.get('elevation').getInfo() / 1e6\n",
            "    print(f'Estimated High Risk Area: {risk_area_sqkm:.2f} sq km')\n",
            "    \n",
            "    # Visualization\n",
            "    m = geemap.Map(center=[6.5244, 3.3792], zoom=11)\n",
            "    \n",
            "    # Vis Params\n",
            "    elev_vis = {'min': 0, 'max': 100, 'palette': ['blue', 'green', 'yellow', 'brown']}\n",
            "    risk_vis = {'min': 0, 'max': 1, 'palette': ['white', 'red']}\n",
            "    \n",
            "    m.addLayer(elevation, elev_vis, 'Elevation')\n",
            "    m.addLayer(high_risk.updateMask(high_risk), {'palette': ['red']}, 'High Flood Risk Zone')\n",
            "    \n",
            "    m.add_colorbar(elev_vis, label='Elevation (m)')\n",
            "    return m\n",
            "\n",
            "m = analyze_risk()\n",
            "m"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 🗺️ Spatial Insights\n",
            "\n",
            "1. **Risk Hotspots**: The red areas on the map indicate regions with high susceptibility to the analyzed risk factor (e.g., flooding).\n",
            "2. **Topography**: Low-lying areas (blue/green) are naturally more vulnerable.\n",
            "3. **Mitigation**: Urban planning in these zones should prioritize drainage systems and flood barriers."
        ]
    }
]

# 6. CHANGE DETECTION (GIS)
CODE_CHANGE_DETECTION = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import ee\n",
            "import geemap\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Initialize Earth Engine\n",
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
            "# Define AOI and Time Periods\n",
            "AOI = ee.Geometry.Point([3.3792, 6.5244]).buffer(20000) # Lagos\n",
            "\n",
            "def detect_changes():\n",
            "    print('Processing satellite imagery...')\n",
            "    # Load Image Collection (Sentinel-2 or MODIS)\n",
            "    # Using MODIS for broader temporal coverage in this demo\n",
            "    dataset = ee.ImageCollection('{dataset_id}')\n",
            "    \n",
            "    # Period 1 (Baseline)\n",
            "    img1 = dataset.filterDate('2018-01-01', '2018-12-31') \\\n",
            "                  .filterBounds(AOI) \\\n",
            "                  .select('{band_name}') \\\n",
            "                  .mean().clip(AOI)\n",
            "                  \n",
            "    # Period 2 (Comparison)\n",
            "    img2 = dataset.filterDate('2023-01-01', '2023-12-31') \\\n",
            "                  .filterBounds(AOI) \\\n",
            "                  .select('{band_name}') \\\n",
            "                  .mean().clip(AOI)\n",
            "    \n",
            "    # Calculate Difference\n",
            "    diff = img2.subtract(img1)\n",
            "    \n",
            "    # Thresholding for significant change (e.g., > 10% change)\n",
            "    # Adjust threshold based on data range\n",
            "    threshold = 1000 # Example for scaled NDVI or LST\n",
            "    significant_increase = diff.gt(threshold)\n",
            "    significant_decrease = diff.lt(-threshold)\n",
            "    \n",
            "    # Calculate Change Area\n",
            "    pixel_area = ee.Image.pixelArea()\n",
            "    increase_area = significant_increase.multiply(pixel_area).reduceRegion(\n",
            "        reducer=ee.Reducer.sum(), geometry=AOI, scale=500, maxPixels=1e9\n",
            "    ).get('{band_name}').getInfo() / 1e6\n",
            "    \n",
            "    decrease_area = significant_decrease.multiply(pixel_area).reduceRegion(\n",
            "        reducer=ee.Reducer.sum(), geometry=AOI, scale=500, maxPixels=1e9\n",
            "    ).get('{band_name}').getInfo() / 1e6\n",
            "    \n",
            "    print(f'Significant Increase Area: {increase_area:.2f} sq km')\n",
            "    print(f'Significant Decrease Area: {decrease_area:.2f} sq km')\n",
            "    \n",
            "    # Visualization\n",
            "    m = geemap.Map(center=[6.5244, 3.3792], zoom=10)\n",
            "    \n",
            "    vis_params = {vis_params}\n",
            "    diff_vis = {'min': -2000, 'max': 2000, 'palette': ['blue', 'white', 'red']}\n",
            "    \n",
            "    m.addLayer(img1, vis_params, 'Baseline (2018)')\n",
            "    m.addLayer(img2, vis_params, 'Comparison (2023)')\n",
            "    m.addLayer(diff, diff_vis, 'Difference Map')\n",
            "    m.addLayer(significant_increase.updateMask(significant_increase), {'palette': ['red']}, 'Significant Increase')\n",
            "    \n",
            "    m.add_colorbar(diff_vis, label='Change Magnitude')\n",
            "    return m\n",
            "\n",
            "m = detect_changes()\n",
            "m"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 📉 Change Analysis\n",
            "\n",
            "1. **Trend Direction**: The analysis reveals a net [increase/decrease] in `{band_name}` over the 5-year period.\n",
            "2. **Spatial Pattern**: Changes are concentrated in [Urban/Rural] zones, suggesting...\n",
            "3. **Implication**: This shift impacts [Temperature/Vegetation/Urbanization] dynamics, requiring..."
        ]
    }
]

# 7. VECTOR/NETWORK ANALYSIS (GIS)
CODE_VECTOR = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import ee\n",
            "import geemap\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Initialize Earth Engine\n",
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
            "# Define AOI\n",
            "AOI = ee.Geometry.Point([-73.9, 40.7]).buffer(10000) # NYC Example\n",
            "\n",
            "def analyze_vectors():\n",
            "    print('Loading vector datasets...')\n",
            "    # 1. Road Network (TIGER)\n",
            "    roads = ee.FeatureCollection('TIGER/2016/Roads').filterBounds(AOI)\n",
            "    \n",
            "    # 2. Points of Interest (Sample Points)\n",
            "    # Generating random points to simulate facilities (e.g., hospitals, stores)\n",
            "    facilities = ee.FeatureCollection.randomPoints(AOI, 50, seed=42)\n",
            "    \n",
            "    # 3. Service Area Analysis (Buffering)\n",
            "    # Buffer facilities by 1km (e.g., walking distance)\n",
            "    service_areas = facilities.map(lambda f: f.buffer(1000))\n",
            "    union_service_area = service_areas.union(100)\n",
            "    \n",
            "    # 4. Coverage Analysis\n",
            "    # Calculate total service area\n",
            "    total_area = union_service_area.geometry().area().divide(1e6).getInfo()\n",
            "    print(f'Total Service Area Coverage: {total_area:.2f} sq km')\n",
            "    \n",
            "    # 5. Network Density\n",
            "    # Count road segments intersecting service areas\n",
            "    connected_roads = roads.filterBounds(union_service_area.geometry())\n",
            "    print(f'Connected Road Segments: {connected_roads.size().getInfo()}')\n",
            "    \n",
            "    # Visualization\n",
            "    m = geemap.Map(center=[40.7, -73.9], zoom=12)\n",
            "    \n",
            "    m.addLayer(roads, {'color': 'gray', 'width': 1}, 'Road Network')\n",
            "    m.addLayer(union_service_area, {'color': 'blue', 'opacity': 0.3}, '1km Service Coverage')\n",
            "    m.addLayer(facilities, {'color': 'red', 'pointSize': 5}, 'Facilities')\n",
            "    \n",
            "    return m\n",
            "\n",
            "m = analyze_vectors()\n",
            "m"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 📍 Network Insights\n",
            "\n",
            "1. **Coverage Gaps**: Areas outside the blue buffers represent underserved regions.\n",
            "2. **Accessibility**: {total_area:.2f} sq km of the city is within walking distance of a facility.\n",
            "3. **Optimization**: Future facilities should be placed in the gray zones to maximize coverage."
        ]
    }
]

# 8. OPTIMIZATION (Operations Research)
CODE_OPTIMIZATION = [
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Import Libraries\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from scipy.optimize import linprog\n",
            "\n",
            "plt.style.use('seaborn-v0_8-whitegrid')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Problem Definition\n",
            "# Example: Product Mix Optimization\n",
            "# Maximize Profit = 20*A + 30*B\n",
            "# Constraints:\n",
            "# 1. Labor: 2*A + 4*B <= 100 hours\n",
            "# 2. Material: 3*A + 2*B <= 90 units\n",
            "# 3. Demand: A >= 0, B >= 0\n",
            "\n",
            "def solve_optimization():\n",
            "    # Coefficients for Objective Function (Negative for Maximization)\n",
            "    c = [-20, -30] \n",
            "    \n",
            "    # Inequality Constraints (LHS)\n",
            "    A = [\n",
            "        [2, 4], # Labor\n",
            "        [3, 2]  # Material\n",
            "    ]\n",
            "    \n",
            "    # Inequality Constraints (RHS)\n",
            "    b = [100, 90]\n",
            "    \n",
            "    # Bounds (x0 >= 0, x1 >= 0)\n",
            "    x0_bounds = (0, None)\n",
            "    x1_bounds = (0, None)\n",
            "    \n",
            "    # Solve\n",
            "    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')\n",
            "    \n",
            "    return res\n",
            "\n",
            "result = solve_optimization()\n",
            "print('Optimization Status:', result.message)\n",
            "print(f'Optimal Value (Max Profit): ${-result.fun:.2f}')\n",
            "print(f'Optimal Solution: Product A = {result.x[0]:.2f}, Product B = {result.x[1]:.2f}')"
        ]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "source": [
            "# Sensitivity Analysis & Visualization\n",
            "def plot_constraints():\n",
            "    # Define range for Product A\n",
            "    x = np.linspace(0, 50, 200)\n",
            "    \n",
            "    # Constraint Lines\n",
            "    y1 = (100 - 2*x) / 4 # Labor\n",
            "    y2 = (90 - 3*x) / 2  # Material\n",
            "    \n",
            "    plt.figure(figsize=(10, 8))\n",
            "    \n",
            "    plt.plot(x, y1, label=r'$2A + 4B \\leq 100$ (Labor)')\n",
            "    plt.plot(x, y2, label=r'$3A + 2B \\leq 90$ (Material)')\n",
            "    \n",
            "    # Feasible Region\n",
            "    plt.fill_between(x, 0, np.minimum(y1, y2), where=(y1>=0) & (y2>=0), color='gray', alpha=0.3, label='Feasible Region')\n",
            "    \n",
            "    # Optimal Point\n",
            "    plt.plot(result.x[0], result.x[1], 'ro', markersize=10, label='Optimal Solution')\n",
            "    plt.annotate(f'({result.x[0]:.1f}, {result.x[1]:.1f})', (result.x[0]+1, result.x[1]+1))\n",
            "    \n",
            "    plt.xlim(0, 40)\n",
            "    plt.ylim(0, 40)\n",
            "    plt.xlabel('Units of Product A')\n",
            "    plt.ylabel('Units of Product B')\n",
            "    plt.title('Linear Programming: Feasible Region & Optimal Solution')\n",
            "    plt.legend()\n",
            "    plt.grid(True)\n",
            "    plt.show()\n",
            "\n",
            "plot_constraints()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 🚀 Operational Recommendations\n",
            "\n",
            "1. **Production Plan**: Manufacture **{result.x[0]:.0f} units of A** and **{result.x[1]:.0f} units of B**.\n",
            "2. **Resource Utilization**: This plan fully utilizes [Labor/Material], making it the bottleneck resource.\n",
            "3. **Expansion**: Increasing the bottleneck resource by 1 unit would increase profit by the 'Shadow Price'."
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
