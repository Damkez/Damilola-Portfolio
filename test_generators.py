"""Quick test to validate generators work"""
import json

try:
    from agricultural_suitability_generator import generate_agricultural_suitability_notebook
    nb = json.loads(generate_agricultural_suitability_notebook())
    print(f"Agricultural: {len(nb['cells'])} cells - OK")
except Exception as e:
    print(f"Agricultural: ERROR - {e}")

try:
    from geospatial_timeseries_generator import generate_geospatial_timeseries_notebook  
    nb = json.loads(generate_geospatial_timeseries_notebook())
    print(f"Time Series: {len(nb['cells'])} cells - OK")
except Exception as e:
    print(f"Time Series: ERROR - {e}")

try:
    from population_density_generator import generate_population_density_notebook
    nb = json.loads(generate_population_density_notebook())
    print(f"Population: {len(nb['cells'])} cells - OK")
except Exception as e:
    print(f"Population: ERROR - {e}")

try:
    from remaining_use_case_generators import generate_retail_site_selection_notebook
    nb = json.loads(generate_retail_site_selection_notebook())
    print(f"Retail: {len(nb['cells'])} cells - OK")
except Exception as e:
    print(f"Retail: ERROR - {e}")

try:
    from remaining_use_case_generators import generate_service_area_notebook
    nb = json.loads(generate_service_area_notebook())
    print(f"Service Area: {len(nb['cells'])} cells - OK")
except Exception as e:
    print(f"Service Area: ERROR - {e}")

try:
    from final_use_case_generators import generate_spatial_clustering_notebook
    nb = json.loads(generate_spatial_clustering_notebook())
    print(f"Clustering: {len(nb['cells'])} cells - OK")
except Exception as e:
    print(f"Clustering: ERROR - {e}")

try:
    from final_use_case_generators import generate_transportation_network_notebook
    nb = json.loads(generate_transportation_network_notebook())
    print(f"Transportation: {len(nb['cells'])} cells - OK")
except Exception as e:
    print(f"Transportation: ERROR - {e}")
