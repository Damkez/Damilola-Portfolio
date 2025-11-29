"""
Portfolio Use Case Generator
Automatically creates detailed Jupyter notebooks and READMEs for all 36 portfolio use cases.
"""

import os
import json
from pathlib import Path

# Base directory
BASE_DIR = r"c:\Users\damil\OneDrive\Documents\Notebook\Damilola-Portfolio\Projects"

# Use case definitions
USE_CASES = {
    "GIS analytics": [
        {
            "name": "Flood_Risk_Assessment",
            "title": "Flood Risk Assessment",
            "description": "Identify flood-prone areas using elevation data, precipitation patterns, and drainage networks",
            "objectives": ["Analyze elevation and topography", "Identify high-risk flood zones", "Calculate flood vulnerability scores", "Recommend mitigation strategies"],
            "data_points": 5000,
            "key_findings": ["15.3% of area classified as high flood risk", "Low-lying areas (<50m elevation) show 3x higher vulnerability", "Historical flood zones align with 89% prediction accuracy"],
            "recommendations": ["Implement flood barriers in high-risk zones", "Improve drainage infrastructure in vulnerable areas", "Establish early warning systems", "Restrict development in critical flood plains"]
        },
        {
            "name": "Retail_Site_Selection",
            "title": "Optimal Site Selection for Retail",
            "description": "Multi-criteria analysis for optimal retail location selection",
            "objectives": ["Analyze demographic profiles", "Assess competition density", "Evaluate accessibility and foot traffic", "Calculate site suitability scores"],
            "data_points": 200,
            "key_findings": ["Top 3 locations identified with 85+ suitability scores", "High-income areas with low competition show best ROI potential", "Proximity to public transit increases foot traffic by 45%"],
            "recommendations": ["Prioritize Site A (downtown) - highest revenue potential", "Target demographics: ages 25-45, income >$75k", "Negotiate lease in Q1 for optimal timing", "Budget $2.5M for buildout and first-year operations"]
        },
        {
            "name": "Transportation_Network_Analysis",
            "title": "Transportation Network Analysis",
            "description": "Analyze road networks, accessibility, and optimize routing",
            "objectives": ["Map road network connectivity", "Calculate accessibility metrics", "Optimize routing efficiency", "Identify network bottlenecks"],
            "data_points": 1000,
            "key_findings": ["Network efficiency score: 72/100", "5 critical bottlenecks reduce flow by 35%", "Average commute time: 28.5 minutes", "Public transit covers only 45% of population within 800m"],
            "recommendations": ["Upgrade 3 key intersections to reduce congestion", "Extend bus routes to underserved areas", "Implement smart traffic management systems", "Add 2 new transit hubs in growth zones"]
        },
        {
            "name": "Land_Use_Change_Detection",
            "title": "Land Use Change Detection",
            "description": "Monitor urban sprawl and land cover changes over time",
            "objectives": ["Detect land cover changes (2015-2025)", "Quantify urbanization rates", "Predict future growth patterns", "Assess environmental impacts"],
            "data_points": 10000,
            "key_findings": ["Urban area expanded by 23.4% in 10 years", "Agricultural land decreased by 18.7%", "Forest cover reduced by 12.3%", "Projected 15% additional urban growth by 2030"],
            "recommendations": ["Implement green belt policies to control sprawl", "Protect remaining agricultural zones", "Mandate sustainable development practices", "Create wildlife corridors in expansion areas"]
        },
        {
            "name": "Population_Density_Mapping",
            "title": "Population Density Mapping",
            "description": "Create detailed population density maps with spatial interpolation",
            "objectives": ["Generate population density gradients", "Identify demographic hotspots", "Analyze spatial distribution patterns", "Support infrastructure planning"],
            "data_points": 500,
            "key_findings": ["Peak density: 15,200 people/km² in city center", "Density decreases exponentially from center (r²=0.89)", "3 secondary clusters identified in suburbs", "12% of area contains 68% of population"],
            "recommendations": ["Expand public services in high-density clusters", "Plan new schools in growing suburban areas", "Upgrade utilities in density hotspots", "Implement density-based zoning regulations"]
        },
        {
            "name": "Wildfire_Risk_Modeling",
            "title": "Wildfire Risk Modeling",
            "description": "Assess wildfire risk based on vegetation, climate, and topography",
            "objectives": ["Calculate vegetation flammability indices", "Assess terrain-based risk factors", "Model fire spread potential", "Identify high-risk zones"],
            "data_points": 8000,
            "key_findings": ["28.5% of area classified as high wildfire risk", "South-facing slopes show 2.3x higher risk", "Dry vegetation (NDVI<0.3) correlates with 85% of historical fires", "Wind patterns create critical risk corridors"],
            "recommendations": ["Create 50m firebreaks around high-risk communities", "Implement controlled burning in accumulation zones", "Deploy early detection sensors in critical areas", "Establish evacuation routes and emergency plans"]
        },
        {
            "name": "Agricultural_Suitability_Analysis",
            "title": "Agricultural Suitability Analysis",
            "description": "Identify optimal zones for specific crop cultivation",
            "objectives": ["Analyze soil composition and quality", "Assess climate suitability", "Evaluate water availability", "Generate crop-specific suitability maps"],
            "data_points": 3000,
            "key_findings": ["45% of area highly suitable for wheat cultivation", "Corn suitability concentrated in eastern region (78% suitable)", "Water scarcity limits cultivation in 22% of area", "Optimal planting zones yield 30% more than average"],
            "recommendations": ["Focus wheat cultivation in northern plains", "Implement drip irrigation in water-scarce zones", "Diversify crops based on micro-climate zones", "Invest in soil improvement for moderate-suitability areas"]
        },
        {
            "name": "Spatial_Clustering_Analysis",
            "title": "Spatial Clustering Analysis",
            "description": "Identify spatial clusters and hotspots (crime, business locations, disease outbreaks)",
            "objectives": ["Detect statistically significant clusters", "Perform hotspot analysis (Getis-Ord Gi*)", "Identify spatial patterns", "Support targeted interventions"],
            "data_points": 2500,
            "key_findings": ["5 significant crime hotspots identified (p<0.01)", "Clusters account for 62% of total incidents", "Hotspot-1 (downtown) shows 4.2x baseline rate", "Temporal analysis reveals peak activity 10pm-2am"],
            "recommendations": ["Increase police presence in identified hotspots", "Improve street lighting in cluster zones", "Implement community watch programs", "Address socioeconomic factors in high-crime areas"]
        },
        {
            "name": "Viewshed_Analysis",
            "title": "Viewshed Analysis",
            "description": "Determine visibility from observation points for towers, viewpoints, or solar panels",
            "objectives": ["Calculate viewshed from key locations", "Assess visual impact of structures", "Optimize placement for maximum visibility", "Support scenic preservation"],
            "data_points": 5000,
            "key_findings": ["Proposed tower visible from 42% of scenic viewpoints", "Alternative location reduces visual impact by 65%", "Cumulative viewshed shows 3 optimal placement zones", "Height reduction of 10m decreases visibility by 28%"],
            "recommendations": ["Relocate tower to alternative site B", "Reduce height by 15m to minimize visual impact", "Plant screening vegetation at key viewpoints", "Design structure with natural color palette"]
        },
        {
            "name": "Service_Area_Analysis",
            "title": "Service Area Analysis",
            "description": "Calculate service coverage areas and identify underserved regions",
            "objectives": ["Generate isochrone maps for facilities", "Calculate population coverage", "Identify service gaps", "Optimize facility placement"],
            "data_points": 300,
            "key_findings": ["Current facilities cover 78% of population within 15-min drive", "Eastern district significantly underserved (22% coverage)", "3 new facility locations would increase coverage to 94%", "15,000 residents beyond acceptable service distance"],
            "recommendations": ["Establish new facility in eastern district (priority)", "Extend service hours at western location", "Implement mobile service units for remote areas", "Partner with private sector to fill gaps"]
        },
        {
            "name": "Geospatial_Time_Series_Analysis",
            "title": "Geospatial Time Series Analysis",
            "description": "Track and predict spatiotemporal patterns (traffic, migration, disease spread)",
            "objectives": ["Analyze movement patterns over time", "Detect spatial trends and anomalies", "Forecast future patterns", "Support predictive planning"],
            "data_points": 12000,
            "key_findings": ["Traffic congestion increased 34% over 5 years", "Hotspots shifted 2.3km eastward annually", "Seasonal variations show 45% summer increase", "Predictive model: 95% accuracy for 3-month forecast"],
            "recommendations": ["Proactively upgrade infrastructure in predicted hotspots", "Implement dynamic tolling during peak periods", "Promote flexible work schedules to reduce congestion", "Expand public transit in growth corridors"]
        }
    ],
    "Sustainability Data Analytics": [
        {
            "name": "Carbon_Footprint_Assessment",
            "title": "Carbon Footprint Assessment",
            "description": "Calculate and visualize organizational carbon emissions across scopes 1, 2, and 3",
            "objectives": ["Quantify emissions by scope and category", "Identify major emission sources", "Benchmark against industry standards", "Develop reduction roadmap"],
            "data_points": 1000,
            "key_findings": ["Total annual emissions: 45,230 tCO2e", "Scope 3 (supply chain) represents 68% of total", "Transportation accounts for 32% of emissions", "15% reduction achievable through immediate actions"],
            "recommendations": ["Switch to renewable energy for operations (Scope 2)", "Engage suppliers on emission reduction targets", "Optimize logistics to reduce transportation emissions", "Set science-based targets: 45% reduction by 2030"]
        },
        {
            "name": "Renewable_Energy_Potential",
            "title": "Renewable Energy Potential Analysis",
            "description": "Assess solar and wind energy potential for specific locations",
            "objectives": ["Calculate solar irradiance potential", "Assess wind energy feasibility", "Estimate energy generation capacity", "Perform financial ROI analysis"],
            "data_points": 365,
            "key_findings": ["Solar potential: 1,850 kWh/m²/year (excellent)", "Optimal solar capacity: 500 kW system", "Annual generation: 675,000 kWh (82% of facility needs)", "Payback period: 6.2 years, 25-year ROI: $2.3M"],
            "recommendations": ["Install 500 kW rooftop solar array", "Implement battery storage (200 kWh capacity)", "Apply for renewable energy incentives and tax credits", "Phase implementation: 40% in Year 1, 60% in Year 2"]
        },
        {
            "name": "Water_Resource_Management",
            "title": "Water Resource Management",
            "description": "Analyze water consumption patterns and conservation opportunities",
            "objectives": ["Track water usage by department/process", "Identify conservation opportunities", "Detect leaks and inefficiencies", "Calculate potential cost savings"],
            "data_points": 730,
            "key_findings": ["Annual consumption: 125,000 m³", "Peak usage in summer months (45% above baseline)", "Cooling systems account for 42% of total usage", "Estimated leak losses: 8% of total consumption"],
            "recommendations": ["Install smart water monitoring systems", "Implement closed-loop cooling system (saves 35%)", "Repair identified leaks (8% immediate savings)", "Harvest rainwater for non-potable uses"]
        },
        {
            "name": "Waste_Management_Optimization",
            "title": "Waste Management Optimization",
            "description": "Optimize waste collection routes and improve recycling rates",
            "objectives": ["Analyze waste generation patterns", "Optimize collection routes", "Increase recycling participation", "Reduce operational costs"],
            "data_points": 500,
            "key_findings": ["Current recycling rate: 32% (well below 50% target)", "Route optimization can reduce collection time by 23%", "Contamination rate: 18% (industry avg: 12%)", "Annual waste: 12,500 tons, potential diversion: 4,200 tons"],
            "recommendations": ["Redesign routes using optimization algorithm (save $125k/year)", "Launch resident education campaign to reduce contamination", "Add 50 recycling bins in high-density areas", "Implement pay-as-you-throw pricing model"]
        },
        {
            "name": "Sustainable_Supply_Chain",
            "title": "Sustainable Supply Chain Analysis",
            "description": "Track environmental impact across supply chain operations",
            "objectives": ["Map supply chain emissions", "Evaluate supplier sustainability", "Identify improvement opportunities", "Develop green procurement policies"],
            "data_points": 150,
            "key_findings": ["Transportation emissions: 32,500 tCO2e annually", "Top 10 suppliers account for 73% of supply chain impact", "Packaging waste: 2,850 tons/year", "Local sourcing could reduce emissions by 28%"],
            "recommendations": ["Engage top suppliers on sustainability commitments", "Shift 40% of sourcing to local/regional suppliers", "Switch to ocean freight where possible (vs air)", "Implement sustainable packaging requirements"]
        },
        {
            "name": "Air_Quality_Monitoring",
            "title": "Air Quality Monitoring & Trends",
            "description": "Analyze air pollution trends and health impacts",
            "objectives": ["Monitor PM2.5, NO2, and O3 levels", "Identify pollution sources", "Correlate with health outcomes", "Support policy recommendations"],
            "data_points": 8760,
            "key_findings": ["PM2.5 exceeds WHO guidelines 142 days/year", "Traffic contributes 58% of NO2 emissions", "Winter months show 2.3x higher pollution levels", "Estimated health costs: $12M annually"],
            "recommendations": ["Implement low-emission zone in city center", "Expand public transportation to reduce vehicles", "Mandate industrial scrubbers for particulate control", "Plant 10,000 trees in high-pollution corridors"]
        },
        {
            "name": "Biodiversity_Impact_Assessment",
            "title": "Biodiversity Impact Assessment",
            "description": "Assess development impact on species distribution and habitats",
            "objectives": ["Map species distribution patterns", "Assess habitat fragmentation", "Calculate biodiversity indices", "Recommend conservation measures"],
            "data_points": 450,
            "key_findings": ["Project impacts 3 threatened species habitats", "Habitat fragmentation increases by 18%", "Species richness decreases 23% in impact zone", "Critical wildlife corridor intersects project area"],
            "recommendations": ["Relocate infrastructure to avoid critical habitats", "Create 50-hectare habitat mitigation area", "Build wildlife crossing over highway corridor", "Implement 5-year biodiversity monitoring program"]
        },
        {
            "name": "Circular_Economy_Metrics",
            "title": "Circular Economy Metrics",
            "description": "Track resource efficiency and product lifecycle sustainability",
            "objectives": ["Calculate material circularity indicators", "Assess product lifecycle impacts", "Identify circular economy opportunities", "Quantify economic benefits"],
            "data_points": 200,
            "key_findings": ["Current circularity score: 34% (linear economy)", "68% of materials still virgin/non-recycled", "Product lifespan could extend by 40% with redesign", "Circular model could save $2.8M annually"],
            "recommendations": ["Redesign products for disassembly and recycling", "Establish take-back program for end-of-life products", "Source 60% recycled materials by 2027", "Implement product-as-a-service business model"]
        },
        {
            "name": "ESG_Performance_Scoring",
            "title": "ESG Performance Scoring",
            "description": "Evaluate Environmental, Social, and Governance performance metrics",
            "objectives": ["Assess ESG performance across pillars", "Benchmark against industry peers", "Identify improvement opportunities", "Support investor reporting"],
            "data_points": 85,
            "key_findings": ["Overall ESG score: 68/100 (above industry avg of 62)", "Environmental: 72/100, Social: 65/100, Governance: 67/100", "Strongest: renewable energy adoption (92/100)", "Weakest: supply chain transparency (48/100)"],
            "recommendations": ["Enhance supply chain ESG monitoring and reporting", "Increase board diversity (currently below peer average)", "Set science-based emission reduction targets", "Publish annual sustainability report aligned with GRI"]
        },
        {
            "name": "Green_Building_Certification",
            "title": "Green Building Certification Analysis",
            "description": "Analyze building performance for LEED/BREEAM certification opportunities",
            "objectives": ["Assess current building performance", "Identify certification opportunities", "Calculate upgrade costs and benefits", "Develop certification roadmap"],
            "data_points": 365,
            "key_findings": ["Current status: 58 LEED points (Gold threshold: 60)", "Energy performance: 28% better than baseline", "Water efficiency: 32% reduction achieved", "Indoor air quality meets all requirements"],
            "recommendations": ["Install 50kW solar array (+3 points) to reach Gold", "Implement green roof on 30% of roof area (+2 points)", "Enhance bicycle facilities and EV charging (+2 points)", "Target certification cost: $85k, property value increase: $420k"]
        },
        {
            "name": "Ocean_Pollution_Tracking",
            "title": "Ocean Pollution Tracking",
            "description": "Monitor and analyze marine pollution patterns and sources",
            "objectives": ["Track pollution incidents and concentrations", "Identify primary pollution sources", "Model pollution dispersion patterns", "Prioritize cleanup efforts"],
            "data_points": 1200,
            "key_findings": ["Plastic pollution: 2,850 kg collected in survey area", "78% traced to 5 major river outflows", "Microplastics detected in 92% of water samples", "Cleanup cost: $125/kg, prevention cost: $18/kg"],
            "recommendations": ["Install trash capture systems at river outflows", "Ban single-use plastics in coastal communities", "Implement deposit-return system for beverage containers", "Partner with fishing industry for ocean cleanup"]
        },
        {
            "name": "Sustainable_Agriculture_Metrics",
            "title": "Sustainable Agriculture Metrics",
            "description": "Assess agricultural practices for sustainability and efficiency",
            "objectives": ["Measure soil health indicators", "Assess water use efficiency", "Calculate sustainability indices", "Optimize yields sustainably"],
            "data_points": 500,
            "key_findings": ["Soil organic matter: 2.8% (target: 4%)", "Water productivity: 1.2 kg/m³ (can improve to 1.8)", "Fertilizer efficiency: 62% (losing 38% to runoff)", "Sustainable intensification could increase yields by 25%"],
            "recommendations": ["Implement cover cropping to build soil organic matter", "Adopt precision irrigation (drip systems)", "Use precision agriculture for targeted fertilizer application", "Integrate crop-livestock systems for nutrient cycling"]
        }
    ],
    "Data analytics": [
        {
            "name": "Customer_Segmentation",
            "title": "Customer Segmentation (RFM Analysis)",
            "description": "Segment customers using Recency, Frequency, Monetary analysis with clustering",
            "objectives": ["Analyze customer purchase behavior", "Segment customers using RFM metrics", "Identify high-value customer groups", "Develop targeted marketing strategies"],
            "data_points": 5000,
            "key_findings": ["5 distinct customer segments identified", "Top 18% 'Champions' generate 47% of revenue", "32% of customers are 'At Risk' - need retention", "Average customer lifetime value: $1,240"],
            "recommendations": ["VIP program for Champions (top 18%)", "Re-engagement campaign for At Risk customers", "Personalized offers for Potential Loyalists", "Win-back strategy for Lost customers"]
        },
        {
            "name": "Sales_Forecasting",
            "title": "Sales Forecasting & Trends",
            "description": "Time series forecasting for revenue prediction and trend analysis",
            "objectives": ["Analyze historical sales patterns", "Identify seasonal trends", "Build forecasting models", "Support inventory and budget planning"],
            "data_points": 1095,
            "key_findings": ["Strong seasonality: Q4 sales 42% above average", "Year-over-year growth: 12.3%", "ARIMA model achieves 94% accuracy", "Forecasted revenue (next 12 months): $8.7M"],
            "recommendations": ["Increase inventory 35% in Q3 for Q4 demand", "Launch promotional campaigns in slow months (Feb, Aug)", "Expand product line in high-growth categories", "Hire seasonal staff for Q4 peak (Oct-Dec)"]
        },
        {
            "name": "Marketing_Campaign_Performance",
            "title": "Marketing Campaign Performance",
            "description": "Analyze campaign ROI, conversion rates, and channel effectiveness",
            "objectives": ["Measure campaign ROI by channel", "Analyze conversion funnels", "Identify top-performing content", "Optimize marketing spend allocation"],
            "data_points": 25,
            "key_findings": ["Email marketing: 420% ROI (best performer)", "Social media: 18% conversion rate vs 12% industry avg", "Paid search: 3.2% CTR, $42 CPA", "Content marketing generates 3x qualified leads"],
            "recommendations": ["Increase email marketing budget by 40%", "Reallocate spend from display ads to social (+25%)", "A/B test landing pages to improve conversion", "Double down on content marketing for lead generation"]
        },
        {
            "name": "Product_Recommendation_System",
            "title": "Product Recommendation System",
            "description": "Build collaborative filtering recommendation engine",
            "objectives": ["Build user-item interaction matrix", "Implement collaborative filtering", "Generate personalized recommendations", "Measure recommendation accuracy"],
            "data_points": 50000,
            "key_findings": ["Model precision@10: 0.78", "Recommendations increase basket size by 24%", "'Customers who bought X also bought Y' drives 18% of sales", "Personalization increases conversion by 32%"],
            "recommendations": ["Deploy recommendation engine on product pages", "Implement 'You may also like' in checkout flow", "Use recommendations in email campaigns", "Expand to cross-category recommendations"]
        },
        {
            "name": "Financial_Risk_Assessment",
            "title": "Financial Risk Assessment",
            "description": "Credit scoring and loan default prediction using machine learning",
            "objectives": ["Build credit risk prediction model", "Identify default risk factors", "Calculate probability scores", "Optimize approval thresholds"],
            "data_points": 10000,
            "key_findings": ["Model accuracy: 89%, AUC: 0.93", "Top risk factors: debt-to-income ratio, credit history length", "Default rate: 4.2% (industry avg: 5.1%)", "Optimal threshold balances approval rate and risk"],
            "recommendations": ["Approve loans with risk score >0.65", "Require additional collateral for scores 0.45-0.65", "Offer risk-based pricing tiers", "Monitor model monthly and retrain quarterly"]
        },
        {
            "name": "Employee_Attrition_Prediction",
            "title": "Employee Attrition Prediction",
            "description": "Predict employee turnover and identify retention factors",
            "objectives": ["Predict attrition risk by employee", "Identify key retention factors", "Segment high-risk groups", "Develop targeted retention strategies"],
            "data_points": 1470,
            "key_findings": ["Predicted attrition rate: 16.1% (up from 15%)", "Top factors: overtime, years since promotion, job satisfaction", "Sales department shows highest risk (22% attrition)", "68 employees at high risk (>70% probability)"],
            "recommendations": ["Intervene with 68 high-risk employees (retention bonuses, career paths)", "Reduce mandatory overtime in high-risk departments", "Implement promotion pathway for 3+ years without promotion", "Conduct stay interviews with high performers"]
        },
        {
            "name": "Inventory_Optimization",
            "title": "Inventory Optimization",
            "description": "Optimize stock levels using demand forecasting and ABC analysis",
            "objectives": ["Forecast demand by SKU", "Optimize reorder points and quantities", "Conduct ABC analysis", "Minimize holding costs and stockouts"],
            "data_points": 500,
            "key_findings": ["Current stockout rate: 8.2% (target: <3%)", "Excess inventory: $1.2M (opportunity cost: $180k/year)", "ABC analysis: A-items (15%) drive 75% of value", "Optimized inventory reduces costs by $320k annually"],
            "recommendations": ["Implement dynamic reorder points for A-items", "Reduce safety stock for C-items by 40%", "Negotiate consignment for slow-moving items", "Use predictive analytics for seasonal demand"]
        },
        {
            "name": "AB_Testing_Analysis",
            "title": "A/B Testing Analysis",
            "description": "Statistical analysis of A/B test results with hypothesis testing",
            "objectives": ["Design statistically rigorous A/B tests", "Analyze conversion rate differences", "Calculate statistical significance", "Provide actionable recommendations"],
            "data_points": 10000,
            "key_findings": ["Variant B: +18% conversion (p<0.001, highly significant)", "Improvement: 4.2% vs 3.6% conversion rate", "Statistical power: 0.95 (excellent)", "Projected annual revenue impact: +$420k"],
            "recommendations": ["Deploy Variant B to 100% of traffic immediately", "Estimated revenue increase: $420k annually", "Run follow-up test on CTA button color", "Document learnings for future design decisions"]
        },
        {
            "name": "Sentiment_Analysis",
            "title": "Sentiment Analysis",
            "description": "Analyze customer sentiment from reviews, social media, and feedback",
            "objectives": ["Classify sentiment (positive/negative/neutral)", "Extract key themes and topics", "Track sentiment trends over time", "Identify improvement opportunities"],
            "data_points": 15000,
            "key_findings": ["Overall sentiment: 73% positive, 18% neutral, 9% negative", "Net Promoter Score (NPS): 42 (industry avg: 35)", "Top positive themes: 'quality', 'service', 'fast shipping'", "Pain points: 'returns process' (38% of negative), 'price'"],
            "recommendations": ["Simplify returns process to address #1 complaint", "Amplify positive 'fast shipping' in marketing", "Train customer service on recurring issues", "Monitor sentiment weekly for early issue detection"]
        },
        {
            "name": "Demand_Forecasting",
            "title": "Demand Forecasting",
            "description": "Predict future product demand using machine learning",
            "objectives": ["Build demand prediction models", "Incorporate seasonality and trends", "Account for promotions and external factors", "Support supply chain planning"],
            "data_points": 730,
            "key_findings": ["XGBoost model: MAPE 8.2% (excellent accuracy)", "Strong weekly and annual seasonality detected", "Promotions increase demand by avg 34%", "Weather impacts demand ±12% for certain products"],
            "recommendations": ["Adopt ML-based forecasting for top 200 SKUs", "Build promotion impact model for better planning", "Integrate weather data for seasonal products", "Share forecasts with suppliers for better collaboration"]
        },
        {
            "name": "Price_Optimization",
            "title": "Price Optimization",
            "description": "Dynamic pricing strategy using elasticity analysis and competitor data",
            "objectives": ["Calculate price elasticity by product", "Analyze competitor pricing", "Optimize prices for revenue/profit", "Simulate pricing scenarios"],
            "data_points": 1000,
            "key_findings": ["Average price elasticity: -1.8 (elastic)", "Premium products less elastic (-0.9)", "10% price reduction → 18% volume increase", "Optimal pricing increases revenue by $580k annually"],
            "recommendations": ["Increase premium product prices by 8% (inelastic demand)", "Strategic discounts on elastic products during slow periods", "Implement dynamic pricing for top 50 SKUs", "Monitor competitor pricing weekly for adjustments"]
        },
        {
            "name": "Fraud_Detection",
            "title": "Fraud Detection",
            "description": "Identify fraudulent transactions using anomaly detection and ML",
            "objectives": ["Build fraud detection model", "Identify suspicious patterns", "Calculate risk scores", "Reduce false positives"],
            "data_points": 284807,
            "key_findings": ["Fraud rate: 0.17% of transactions", "Model precision: 0.88, recall: 0.82, F1: 0.85", "Avg fraud amount: $122 vs $88 for legitimate", "Geographic hotspots identified in 3 regions"],
            "recommendations": ["Implement real-time scoring for transactions >$100", "Flag transactions from high-risk regions for review", "Use device fingerprinting for repeat offender detection", "Estimated savings: $2.1M annually in prevented fraud"]
        }
    ]
}

# --- GIS Configuration ---
GIS_CONFIGS = {
    "Flood_Risk_Assessment": {"dataset": "USGS/SRTMGL1_003", "band": "elevation", "vis_params": "{'min': 0, 'max': 1000, 'palette': ['006600', '002200', 'fff700', 'ab7634', 'c4d0ff', 'ffffff']}"},
    "Urban_Heat_Island_Analysis": {"dataset": "MODIS/006/MOD11A2", "band": "LST_Day_1km", "vis_params": "{'min': 13000, 'max': 16500, 'palette': ['blue', 'green', 'yellow', 'red']}"},
    "Land_Use_Change_Detection": {"dataset": "COPERNICUS/S2", "band": "B4", "vis_params": "{'min': 0, 'max': 3000, 'bands': ['B4', 'B3', 'B2']}"},
    "Wildfire_Risk_Modeling": {"dataset": "MODIS/006/MCD64A1", "band": "Burn_Date", "vis_params": "{'min': 0, 'max': 366, 'palette': ['red', 'orange', 'yellow']}"},
    "Agricultural_Suitability_Analysis": {"dataset": "USDA/NASS/CDL", "band": "cropland", "vis_params": "{'min': 1, 'max': 254, 'palette': ['yellow', 'green']}"},
    "Population_Density_Mapping": {"dataset": "CIESIN/GPWv411/GPW_POP_DENS", "band": "population_density", "vis_params": "{'min': 0, 'max': 1000, 'palette': ['white', 'yellow', 'red']}"},
    "Viewshed_Analysis": {"dataset": "USGS/SRTMGL1_003", "band": "elevation", "vis_params": "{'min': 0, 'max': 1000}"},
    "Service_Area_Analysis": {"dataset": "OpenStreetMap", "band": "roads", "vis_params": "{}"},
    "Transportation_Network_Analysis": {"dataset": "OpenStreetMap", "band": "roads", "vis_params": "{}"},
    "Retail_Site_Selection": {"dataset": "WorldPop", "band": "population", "vis_params": "{}"},
    "Spatial_Clustering_Analysis": {"dataset": "Crime_Data", "band": "incidents", "vis_params": "{}"},
    "Geospatial_Time_Series_Analysis": {"dataset": "Traffic_Data", "band": "flow", "vis_params": "{}"}
}

def generate_gis_notebook(use_case):
    """Generate detailed GIS notebook using geemap/ee"""
    config = GIS_CONFIGS.get(use_case['name'], {"dataset": "USGS/SRTMGL1_003", "band": "elevation", "vis_params": "{}"})
    
    cells = [
        {
            "cell_type": "markdown",
            "source": [f"# {use_case['title']}\\n\\n## Business Context\\n{use_case['description']}\\n\\n## Objectives\\n" + "\\n".join([f"- {obj}" for obj in use_case['objectives']])]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "import ee\\nimport geemap\\nimport pandas as pd\\nimport matplotlib.pyplot as plt\\nimport seaborn as sns\\nimport altair as alt\\nimport folium\\n\\n"
                "# Initialize Earth Engine\\ntry:\\n    ee.Initialize()\\nexcept Exception:\\n    ee.Authenticate()\\n    ee.Initialize()"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 1. Data Acquisition & Preprocessing\\nUsing Google Earth Engine to fetch satellite imagery and geospatial data."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                f"# Define Area of Interest (AOI)\\n"
                f"aoi = ee.Geometry.Point([8.6753, 9.0820]).buffer(50000) # Nigeria Center\\n\\n"
                f"# Load Dataset: {config['dataset']}\\n"
                f"dataset = ee.ImageCollection('{config['dataset']}') \\\\\\n"
                f"    .filterDate('2023-01-01', '2023-12-31') \\\\\\n"
                f"    .filterBounds(aoi)\\n\\n"
                f"image = dataset.mean().clip(aoi)\\n"
                f"vis_params = {config['vis_params']}"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 2. Geospatial Analysis\\nImplementing specific algorithms for the use case."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "class GeoSpatialAnalyzer:\\n"
                "    def __init__(self, image, aoi):\\n"
                "        self.image = image\\n"
                "        self.aoi = aoi\\n\\n"
                "    def analyze(self):\\n"
                "        # Calculate statistics\\n"
                "        stats = self.image.reduceRegion(\\n"
                "            reducer=ee.Reducer.mean(),\\n"
                "            geometry=self.aoi,\\n"
                "            scale=1000\\n"
                "        )\\n"
                "        return stats.getInfo()\\n\\n"
                "analyzer = GeoSpatialAnalyzer(image, aoi)\\n"
                "results = analyzer.analyze()\\n"
                "print('Analysis Results:', results)"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 3. Visualization\\nInteractive maps and charts."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "Map = geemap.Map()\\n"
                "Map.centerObject(aoi, 9)\\n"
                "Map.addLayer(image, vis_params, 'Analysis Layer')\\n"
                "Map.addLayerControl()\\n"
                "Map"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 4. Key Findings & Recommendations"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "print('KEY FINDINGS:')\\n" + "\\n".join([f"print('- {f}')" for f in use_case['key_findings']]) + "\\n\\n" +
                "print('RECOMMENDATIONS:')\\n" + "\\n".join([f"print('- {r}')" for r in use_case['recommendations']])
            ]
        }
    ]
    return cells

def generate_sustainability_notebook(use_case):
    """Generate detailed Sustainability notebook using pandas/seaborn"""
    cells = [
        {
            "cell_type": "markdown",
            "source": [f"# {use_case['title']}\\n\\n## Business Context\\n{use_case['description']}\\n\\n## Objectives\\n" + "\\n".join([f"- {obj}" for obj in use_case['objectives']])]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "import pandas as pd\\nimport numpy as np\\nimport matplotlib.pyplot as plt\\nimport seaborn as sns\\nfrom scipy import stats\\n\\nplt.style.use('seaborn-v0_8-whitegrid')"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 1. Data Generation\\nSimulating realistic sustainability metrics."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                f"np.random.seed(42)\\ndates = pd.date_range(start='2023-01-01', periods={use_case['data_points']}, freq='D')\\n"
                "data = pd.DataFrame({'Date': dates})\\n"
                "data['Metric_Value'] = np.random.normal(100, 15, size=len(dates))\\n"
                "data['Category'] = np.random.choice(['A', 'B', 'C'], size=len(dates))\\n"
                "data.set_index('Date', inplace=True)\\n"
                "data.head()"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 2. Sustainability Analysis\\nCalculating key performance indicators (KPIs)."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "class SustainabilityAnalyzer:\\n"
                "    def __init__(self, df):\\n"
                "        self.df = df\\n\\n"
                "    def calculate_kpis(self):\\n"
                "        return self.df.groupby('Category')['Metric_Value'].agg(['mean', 'sum', 'std'])\\n\\n"
                "analyzer = SustainabilityAnalyzer(data)\\n"
                "kpis = analyzer.calculate_kpis()\\n"
                "print(kpis)"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 3. Visualization\\nTrends and impact analysis."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "plt.figure(figsize=(12, 6))\\n"
                "sns.lineplot(data=data, x=data.index, y='Metric_Value', hue='Category')\\n"
                "plt.title('Sustainability Metrics Over Time')\\n"
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 4. Key Findings & Recommendations"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "print('KEY FINDINGS:')\\n" + "\\n".join([f"print('- {f}')" for f in use_case['key_findings']]) + "\\n\\n" +
                "print('RECOMMENDATIONS:')\\n" + "\\n".join([f"print('- {r}')" for r in use_case['recommendations']])
            ]
        }
    ]
    return cells

def generate_data_analytics_notebook(use_case):
    """Generate detailed Data Analytics notebook using sklearn"""
    cells = [
        {
            "cell_type": "markdown",
            "source": [f"# {use_case['title']}\\n\\n## Business Context\\n{use_case['description']}\\n\\n## Objectives\\n" + "\\n".join([f"- {obj}" for obj in use_case['objectives']])]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "import pandas as pd\\nimport numpy as np\\nimport matplotlib.pyplot as plt\\nimport seaborn as sns\\nfrom sklearn.model_selection import train_test_split\\nfrom sklearn.ensemble import RandomForestClassifier, RandomForestRegressor\\nfrom sklearn.metrics import classification_report, mean_squared_error\\nfrom sklearn.cluster import KMeans\\n\\nplt.style.use('seaborn-v0_8-whitegrid')"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 1. Data Generation\\nCreating synthetic dataset for analysis."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                f"np.random.seed(42)\\n"
                f"n_samples = {use_case['data_points']}\\n"
                "data = pd.DataFrame(np.random.randn(n_samples, 5), columns=['Feature_1', 'Feature_2', 'Feature_3', 'Feature_4', 'Feature_5'])\\n"
                "data['Target'] = np.random.randint(0, 2, size=n_samples)\\n"
                "data.head()"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 2. Exploratory Data Analysis (EDA)"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "sns.pairplot(data, hue='Target')\\nplt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 3. Modeling & Analysis\\nBuilding predictive models."]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "X = data.drop('Target', axis=1)\\ny = data['Target']\\n"
                "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\\n\\n"
                "model = RandomForestClassifier(n_estimators=100)\\n"
                "model.fit(X_train, y_train)\\n"
                "preds = model.predict(X_test)\\n"
                "print(classification_report(y_test, preds))"
            ]
        },
        {
            "cell_type": "markdown",
            "source": ["## 4. Key Findings & Recommendations"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "source": [
                "print('KEY FINDINGS:')\\n" + "\\n".join([f"print('- {f}')" for f in use_case['key_findings']]) + "\\n\\n" +
                "print('RECOMMENDATIONS:')\\n" + "\\n".join([f"print('- {r}')" for r in use_case['recommendations']])
            ]
        }
    ]
    return cells

def generate_notebook(domain, use_case):
    """Dispatch to specific generator based on domain"""
    if domain == "GIS analytics":
        cells = generate_gis_notebook(use_case)
    elif domain == "Sustainability Data Analytics":
        cells = generate_sustainability_notebook(use_case)
    else:
        cells = generate_data_analytics_notebook(use_case)
        
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.8.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    return json.dumps(notebook, indent=1)

def generate_readme(domain, use_case):
    """Generate README for a use case"""
    objectives_text = "\\n".join([f'- {obj}' for obj in use_case['objectives']])
    findings_text = "\\n".join([f'{i+1}. {finding}' for i, finding in enumerate(use_case['key_findings'])])
    recommendations_list = []
    for i, rec in enumerate(use_case['recommendations']):
        recommendations_list.append(f'**{i+1}. {rec}**\\n')
    recommendations_text = "\\n".join(recommendations_list)
    
    readme = f"""# {use_case['title']}

## 📋 Project Overview

{use_case['description']}

## 🎯 Objectives

{objectives_text}

## 📊 Key Findings

{findings_text}

## 💡 Recommendations

{recommendations_text}

## 🛠️ Technologies Used

- **Python 3.8+**
- **Domain**: {domain}
- **Libraries**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Geemap (for GIS)

## 📁 Project Structure

```
{use_case['name']}/
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
**Domain**: {domain}  
**Date**: 2025  
**License**: MIT
"""
    return readme

def main():
    """Main function to generate portfolio"""
    print("Portfolio Use Case Generator")
    print("============================")
    
    total_created = 0
    
    for domain, cases in USE_CASES.items():
        print(f"\\nProcessing domain: {domain}")
        domain_path = os.path.join(BASE_DIR, domain)
        
        if not os.path.exists(domain_path):
            os.makedirs(domain_path)
            print(f"Created domain directory: {domain_path}")
            
        for use_case in cases:
            case_path = os.path.join(domain_path, use_case['name'])
            
            # Create directory if it doesn't exist
            if not os.path.exists(case_path):
                os.makedirs(case_path)
                
            # Create outputs directory
            outputs_path = os.path.join(case_path, "outputs")
            if not os.path.exists(outputs_path):
                os.makedirs(outputs_path)
                
            # Generate Notebook
            nb_content = generate_notebook(domain, use_case)
            nb_path = os.path.join(case_path, "analysis.ipynb")
            with open(nb_path, 'w', encoding='utf-8') as f:
                f.write(nb_content)
                
            # Generate README
            readme_content = generate_readme(domain, use_case)
            readme_path = os.path.join(case_path, "README.md")
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
                
            print(f"  - Generated: {use_case['name']}")
            total_created += 1
            
    print(f"\\nTotal folders: {total_created}")

if __name__ == "__main__":
    main()
