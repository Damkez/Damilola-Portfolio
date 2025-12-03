"""Detailed test to find exact error"""
import json
import traceback

print("=" * 60)
print("TESTING GENERATORS")
print("=" * 60)

# Test 1
print("\n1. Agricultural Suitability...")
try:
    from agricultural_suitability_generator import generate_agricultural_suitability_notebook
    nb = json.loads(generate_agricultural_suitability_notebook())
    print(f"   SUCCESS: {len(nb['cells'])} cells")
except Exception as e:
    print(f"   ERROR: {e}")
    traceback.print_exc()

# Test 2
print("\n2. Geospatial Time Series...")
try:
    from geospatial_timeseries_generator import generate_geospatial_timeseries_notebook  
    nb = json.loads(generate_geospatial_timeseries_notebook())
    print(f"   SUCCESS: {len(nb['cells'])} cells")
except Exception as e:
    print(f"   ERROR: {e}")
    traceback.print_exc()

# Test 3
print("\n3. Population Density...")
try:
    from population_density_generator import generate_population_density_notebook
    nb = json.loads(generate_population_density_notebook())
    print(f"   SUCCESS: {len(nb['cells'])} cells")
except Exception as e:
    print(f"   ERROR: {e}")
    traceback.print_exc()

# Test 4
print("\n4. Retail Site Selection...")
try:
    from remaining_use_case_generators import generate_retail_site_selection_notebook
    nb = json.loads(generate_retail_site_selection_notebook())
    print(f"   SUCCESS: {len(nb['cells'])} cells")
except Exception as e:
    print(f"   ERROR: {e}")
    traceback.print_exc()

# Test 5
print("\n5. Service Area...")
try:
    from remaining_use_case_generators import generate_service_area_notebook
    nb = json.loads(generate_service_area_notebook())
    print(f"   SUCCESS: {len(nb['cells'])} cells")
except Exception as e:
    print(f"   ERROR: {e}")
    traceback.print_exc()

# Test 6
print("\n6. Spatial Clustering...")
try:
    from final_use_case_generators import generate_spatial_clustering_notebook
    nb = json.loads(generate_spatial_clustering_notebook())
    print(f"   SUCCESS: {len(nb['cells'])} cells")
except Exception as e:
    print(f"   ERROR: {e}")
    traceback.print_exc()

# Test 7
print("\n7. Transportation Network...")
try:
    from final_use_case_generators import generate_transportation_network_notebook
    nb = json.loads(generate_transportation_network_notebook())
    print(f"   SUCCESS: {len(nb['cells'])} cells")
except Exception as e:
    print(f"   ERROR: {e}")
    traceback.print_exc()

print("\n" + "=" * 60)
print("TESTING COMPLETE")
print("=" * 60)
