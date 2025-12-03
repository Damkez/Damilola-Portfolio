"""
Simple script to directly create all 7 notebooks bypassing generator import issues
"""
import json
import os

# Import working generators directly
import sys
sys.path.append(os.path.dirname(__file__))

print("Generating all 7 use case notebooks...")
print("=" * 60)

results = []

# Generate each one individually to isolate errors
notebooks = [
    ("Agricultural Suitability", "agricultural_suitability_generator", "generate_agricultural_suitability_notebook", "Agricultural_Suitability_Analysis"),
    ("Geospatial Time Series", "geospatial_timeseries_generator", "generate_geospatial_timeseries_notebook", "Geospatial_Time_Series_Analysis"),
    ("Population Density", "population_density_generator", "generate_population_density_notebook", "Population_Density_Mapping"),
    ("Retail Site Selection", "remaining_use_case_generators", "generate_retail_site_selection_notebook", "Retail_Site_Selection"),
    ("Service Area", "remaining_use_case_generators", "generate_service_area_notebook", "Service_Area_Analysis"),
    ("Spatial Clustering", "final_use_case_generators", "generate_spatial_clustering_notebook", "Spatial_Clustering_Analysis"),
    ("Transportation Network", "final_use_case_generators", "generate_transportation_network_notebook", "Transportation_Network_Analysis"),
]

for name, module_name, func_name, folder_name in notebooks:
    try:
        print(f"\n{name}...")
        
        # Import module
        module = __import__(module_name)
        func = getattr(module, func_name)
        
        # Generate
        nb_json = func()
        nb_data = json.loads(nb_json)
        
        # Save
        nb_dir = os.path.join("Projects", "GIS analytics", folder_name)
        os.makedirs(nb_dir, exist_ok=True)
        nb_path = os.path.join(nb_dir, "analysis.ipynb")
        
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb_data, f, indent=2, ensure_ascii=False)
        
        cells = len(nb_data['cells'])
        print(f"  [OK] {cells} cells -> {nb_path}")
        results.append((name, "SUCCESS", cells))
        
    except Exception as e:
        print(f"  [ERROR] {str(e)[:100]}")
        results.append((name, "FAILED", str(e)[:50]))

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

success_count = sum(1 for r in results if r[1] == "SUCCESS")
print(f"\nSuccessful: {success_count}/7")

for name, status, info in results:
    if status == "SUCCESS":
        print(f"  [OK] {name}: {info} cells")
    else:
        print(f"  [FAIL] {name}: {info}")
