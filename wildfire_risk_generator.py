"""
Wildfire Risk Modeling Generator
Creates sophisticated notebook for wildfire susceptibility analysis using machine learning
"""

import json

def create_notebook(cells):
    """Helper to create notebook structure."""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def generate_wildfire_risk_notebook():
    """Generate comprehensive wildfire risk modeling notebook."""
    
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": [
            "# Wildfire Risk Modeling & Susceptibility Mapping\n\n",
            "## 🔥 Business Context\n",
            "Machine learning-based wildfire susceptibility analysis for California.\n\n",
            "**Key Objectives**:\n",
            "- Train Random Forest classifier on historical fire occurrences\n",
            "- Extract environmental predictors (slope, aspect, NDVI, temperature)\n",
            "- Generate probability surface for wildfire risk\n",
            "- Validate model performance using ROC-AUC\n",
            "- Identify high-risk zones for fuel management\n\n",
            "**Study Area**: Sierra Nevada, California\n\n",
            "**Applications**: Fire prevention, resource allocation, zoning policy"
        ]},
        
        {"cell_type": "code", "metadata": {}, "source": [
            "# Import Libraries\n",
            "import ee\n",
            "import geemap\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report\n",
            "import os\n",
            "\n",
            "# Initialize Earth Engine\n",
            "try:\n",
            "    ee.Initialize()\n",
            "except Exception as e:\n",
            "    ee.Authenticate()\n",
            "    ee.Initialize()\n",
            "\n",
            "# Create outputs directory\n",
            "if not os.path.exists('outputs'):\n",
            "    os.makedirs('outputs')\n",
            "\n",
            "# Configuration\n",
            "ROI = ee.Geometry.Rectangle([-121.0, 37.0, -119.0, 39.0])  # Sierra Nevada\n",
            "START_DATE = '2020-01-01'\n",
            "END_DATE = '2023-12-31'\n",
            "\n",
            "print('Earth Engine Initialized')\n",
            "print(f'Study Area: Sierra Nevada, CA')"
        ]},
        
        {"cell_type": "markdown", "metadata": {}, "source": [
            "## 1. Data Acquisition\n",
            "Simulating historical fire points and non-fire reference points."
        ]},
        
        {"cell_type": "code", "metadata": {}, "source": [
            "# Simulate Fire and Non-Fire Points\n",
            "# In production, would use FIRMS dataset\n",
            "np.random.seed(42)\n",
            "\n",
            "# Generate synthetic fire points (high slope, low NDVI areas)\n",
            "n_fire = 500\n",
            "n_non_fire = 1500\n",
            "\n",
            "# Fire points: biased toward steep slopes\n",
            "fire_slope = np.random.gamma(3, 10, n_fire)\n",
            "fire_aspect = np.random.uniform(0, 360, n_fire)\n",
            "fire_ndvi = np.random.beta(2, 5, n_fire)  # Lower NDVI\n",
            "fire_temp = np.random.normal(305, 5, n_fire)  # Higher temp (Kelvin)\n",
            "\n",
            "# Non-fire points: more varied\n",
            "non_fire_slope = np.random.gamma(2, 5, n_non_fire)\n",
            "non_fire_aspect = np.random.uniform(0, 360, n_non_fire)\n",
            "non_fire_ndvi = np.random.beta(5, 2, n_non_fire)  # Higher NDVI\n",
            "non_fire_temp = np.random.normal(295, 5, n_non_fire)  # Lower temp\n",
            "\n",
            "# Combine into DataFrame\n",
            "df = pd.DataFrame({\n",
            "    'Slope': np.concatenate([fire_slope, non_fire_slope]),\n",
            "    'Aspect': np.concatenate([fire_aspect, non_fire_aspect]),\n",
            "    'NDVI': np.concatenate([fire_ndvi, non_fire_ndvi]),\n",
            "    'Temp': np.concatenate([fire_temp, non_fire_temp]),\n",
            "    'Fire': [1]*n_fire + [0]*n_non_fire\n",
            "})\n",
            "\n",
            "print(f'Dataset: {len(df)} samples ({n_fire} fire, {n_non_fire} non-fire)')\n",
            "df.head()"
        ]},
        
        {"cell_type": "markdown", "metadata": {}, "source": [
            "## 2. Exploratory Data Analysis\n",
            "Comparing environmental conditions between fire and non-fire locations."
        ]},
        
        {"cell_type": "code", "metadata": {}, "source": [
            "# Feature Distributions\n",
            "fig, axes = plt.subplots(2, 2, figsize=(12, 10))\n",
            "\n",
            "sns.boxplot(data=df, x='Fire', y='Slope', ax=axes[0,0], palette='Reds')\n",
            "axes[0,0].set_title('Slope Distribution', fontweight='bold')\n",
            "axes[0,0].set_xticklabels(['Non-Fire', 'Fire'])\n",
            "\n",
            "sns.boxplot(data=df, x='Fire', y='NDVI', ax=axes[0,1], palette='Greens')\n",
            "axes[0,1].set_title('NDVI Distribution', fontweight='bold')\n",
            "axes[0,1].set_xticklabels(['Non-Fire', 'Fire'])\n",
            "\n",
            "sns.boxplot(data=df, x='Fire', y='Temp', ax=axes[1,0], palette='Oranges')\n",
            "axes[1,0].set_title('Temperature Distribution (K)', fontweight='bold')\n",
            "axes[1,0].set_xticklabels(['Non-Fire', 'Fire'])\n",
            "\n",
            "sns.histplot(data=df, x='Aspect', hue='Fire', kde=True, ax=axes[1,1], palette='Set1')\n",
            "axes[1,1].set_title('Aspect Distribution', fontweight='bold')\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.savefig('outputs/feature_distributions.png', dpi=300, bbox_inches='tight')\n",
            "plt.show()"
        ]},
        
        {"cell_type": "markdown", "metadata": {}, "source": [
            "## 3. Model Training\n",
            "Training a Random Forest classifier to predict fire susceptibility."
        ]},
        
        {"cell_type": "code", "metadata": {}, "source": [
            "# Train/Test Split\n",
            "X = df[['Slope', 'Aspect', 'NDVI', 'Temp']]\n",
            "y = df['Fire']\n",
            "\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
            "\n",
            "# Train Random Forest\n",
            "rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)\n",
            "rf.fit(X_train, y_train)\n",
            "\n",
            "# Predictions\n",
            "y_pred = rf.predict(X_test)\n",
            "y_prob = rf.predict_proba(X_test)[:, 1]\n",
            "\n",
            "# Feature Importance\n",
            "importance = pd.DataFrame({\n",
            "    'Feature': X.columns,\n",
            "    'Importance': rf.feature_importances_\n",
            "}).sort_values('Importance', ascending=False)\n",
            "\n",
            "plt.figure(figsize=(8, 5))\n",
            "sns.barplot(data=importance, x='Importance', y='Feature', palette='viridis')\n",
            "plt.title('Feature Importance for Wildfire Prediction', fontweight='bold')\n",
            "plt.savefig('outputs/feature_importance.png', dpi=300, bbox_inches='tight')\n",
            "plt.show()\n",
            "\n",
            "print(f'Training Accuracy: {rf.score(X_train, y_train):.3f}')\n",
            "print(f'Test Accuracy: {rf.score(X_test, y_test):.3f}')"
        ]},
        
        {"cell_type": "markdown", "metadata": {}, "source": [
            "## 4. Model Evaluation\n",
            "Assessing performance using confusion matrix and ROC curve."
        ]},
        
        {"cell_type": "code", "metadata": {}, "source": [
            "# Confusion Matrix\n",
            "cm = confusion_matrix(y_test, y_pred)\n",
            "plt.figure(figsize=(6, 5))\n",
            "sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)\n",
            "plt.xlabel('Predicted')\n",
            "plt.ylabel('Actual')\n",
            "plt.title('Confusion Matrix', fontweight='bold')\n",
            "plt.savefig('outputs/confusion_matrix.png', dpi=300, bbox_inches='tight')\n",
            "plt.show()\n",
            "\n",
            "# ROC Curve\n",
            "fpr, tpr, _ = roc_curve(y_test, y_prob)\n",
            "roc_auc = auc(fpr, tpr)\n",
            "\n",
            "plt.figure(figsize=(8, 6))\n",
            "plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')\n",
            "plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')\n",
            "plt.xlabel('False Positive Rate')\n",
            "plt.ylabel('True Positive Rate')\n",
            "plt.title('Receiver Operating Characteristic (ROC)', fontweight='bold')\n",
            "plt.legend(loc='lower right')\n",
            "plt.grid(alpha=0.3)\n",
            "plt.savefig('outputs/roc_curve.png', dpi=300, bbox_inches='tight')\n",
            "plt.show()\n",
            "\n",
            "print('\\nClassification Report:')\n",
            "print(classification_report(y_test, y_pred, target_names=['Non-Fire', 'Fire']))"
        ]},
        
        {"cell_type": "markdown", "metadata": {}, "source": [
            "## 5. Risk Mapping\n",
            "Generating a spatial risk surface for the study area."
        ]},
        
        {"cell_type": "code", "metadata": {}, "source": [
            "# Create Risk Grid\n",
            "grid_size = 50\n",
            "slope_grid = np.random.gamma(2.5, 8, (grid_size, grid_size))\n",
            "aspect_grid = np.random.uniform(0, 360, (grid_size, grid_size))\n",
            "ndvi_grid = np.random.beta(3, 3, (grid_size, grid_size))\n",
            "temp_grid = np.random.normal(300, 8, (grid_size, grid_size))\n",
            "\n",
            "# Flatten for prediction\n",
            "X_grid = pd.DataFrame({\n",
            "    'Slope': slope_grid.flatten(),\n",
            "    'Aspect': aspect_grid.flatten(),\n",
            "    'NDVI': ndvi_grid.flatten(),\n",
            "    'Temp': temp_grid.flatten()\n",
            "})\n",
            "\n",
            "# Predict probabilities\n",
            "risk_prob = rf.predict_proba(X_grid)[:, 1].reshape(grid_size, grid_size)\n",
            "\n",
            "# Visualize Risk Map\n",
            "plt.figure(figsize=(10, 8))\n",
            "im = plt.imshow(risk_prob, cmap='YlOrRd', interpolation='bilinear')\n",
            "plt.colorbar(im, label='Fire Probability')\n",
            "plt.title('Wildfire Susceptibility Map', fontweight='bold', fontsize=14)\n",
            "plt.xlabel('Longitude (relative)')\n",
            "plt.ylabel('Latitude (relative)')\n",
            "plt.savefig('outputs/wildfire_susceptibility_map.png', dpi=300, bbox_inches='tight')\n",
            "plt.show()\n",
            "\n",
            "# Risk Statistics\n",
            "high_risk_pct = (risk_prob > 0.7).sum() / risk_prob.size * 100\n",
            "print(f'High Risk Areas (>70% probability): {high_risk_pct:.1f}% of study area')"
        ]},
        
        {"cell_type": "code", "metadata": {}, "source": [
            "# Generate Dynamic Summary Report\n",
            "from IPython.display import Markdown, display\n",
            "\n",
            "top_feature = importance.iloc[0]['Feature']\n",
            "top_importance = importance.iloc[0]['Importance']\n",
            "accuracy = rf.score(X_test, y_test)\n",
            "\n",
            "summary_md = f\"\"\"\n",
            "## 🎯 Key Findings & Recommendations\n\n",
            "### Model Performance\n",
            "- **Accuracy**: The Random Forest model achieved **{accuracy:.1%}** accuracy on the test set.\n",
            "- **ROC-AUC**: Area under the curve is **{roc_auc:.2f}**, indicating strong discriminative ability.\n",
            "- **Key Driver**: **{top_feature}** is the most important predictor (importance: {top_importance:.2f}).\n\n",
            "### Risk Distribution\n",
            "- **High Risk Zones**: **{high_risk_pct:.1f}%** of the study area has >70% fire probability.\n",
            "- **Pattern**: Steep slopes with low NDVI (dry vegetation) and high temperatures show highest susceptibility.\n\n",
            "### Strategic Recommendations\n",
            "1. **Fuel Management**: Prioritize prescribed burns in high-risk zones (red areas on map).\n",
            "2. **Early Warning**: Deploy additional sensors in areas with probability >0.7.\n",
            "3. **Zoning Policy**: Restrict new development in the top 10% risk percentile.\n",
            "4. **Resource Allocation**: Pre-position firefighting resources near identified hotspots.\n\n",
            "### Limitations\n",
            "- Model trained on synthetic data for demonstration purposes.\n",
            "- Production model should use FIRMS historical fire data.\n",
            "- Consider adding wind speed and humidity for improved accuracy.\n",
            "\"\"\"\n",
            "display(Markdown(summary_md))"
        ]}
    ]
    
    return json.dumps(create_notebook(cells), indent=2)

if __name__ == "__main__":
    print("Generating Wildfire Risk Modeling notebook...")
    nb_json = generate_wildfire_risk_notebook()
    print(f"✓ Generated notebook with {len(json.loads(nb_json)['cells'])} cells")
