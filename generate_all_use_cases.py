"""
Master Script to Generate All 7 GIS Use Case Notebooks
Run this to create all notebooks in their respective directories.
"""

import os
import json

# Import all generators
from agricultural_suitability_generator import generate_agricultural_suitability_notebook
from geospatial_timeseries_generator import generate_geospatial_timeseries_notebook
from population_density_generator import generate_population_density_notebook
from wildfire_risk_generator import generate_wildfire_risk_notebook

# Import from combined files
from remaining_use_case_generators import (
    generate_retail_site_selection_notebook,
    generate_service_area_notebook
)

from final_use_case_generators import (
    generate_spatial_clustering_notebook,
    generate_transportation_network_notebook
)

# Base directory
BASE_DIR = os.path.join(os.path.dirname(__file__), "Projects", "GIS analytics")

# Notebook configurations
NOTEBOOKS = [
    {
        'name': 'Agricultural Suitability Analysis',
        'folder': 'Agricultural_Suitability_Analysis',
        'generator': generate_agricultural_suitability_notebook
    },
    {
        'name': 'Geospatial Time Series Analysis',
        'folder': 'Geospatial_Time_Series_Analysis',
        'generator': generate_geospatial_timeseries_notebook
    },
    {
        'name': 'Population Density Mapping',
        'folder': 'Population_Density_Mapping',
        'generator': generate_population_density_notebook
    },
    {
        'name': 'Retail Site Selection',
        'folder': 'Retail_Site_Selection',
        'generator': generate_retail_site_selection_notebook
    },
    {
        'name': 'Service Area Analysis',
        'folder': 'Service_Area_Analysis',
        'generator': generate_service_area_notebook
    },
    {
        'name': 'Spatial Clustering Analysis',
        'folder': 'Spatial_Clustering_Analysis',
        'generator': generate_spatial_clustering_notebook
    },
    {
        'name': 'Transportation Network Analysis',
        'folder': 'Transportation_Network_Analysis',
        'generator': generate_transportation_network_notebook
    },
    {
        'name': 'Wildfire Risk Modeling',
        'folder': 'Wildfire_Risk_Modeling',
        'generator': generate_wildfire_risk_notebook
    }
]

def generate_all_notebooks():
    """Generate all 7 notebooks to their directories."""
    print("=" * 60)
    print("GENERATING ALL GIS USE CASE NOTEBOOKS")
    print("=" * 60)
    
    results = []
    
    for nb_config in NOTEBOOKS:
        try:
            print(f"\n> Generating: {nb_config['name']}")
            
            # Generate notebook JSON
            nb_json = nb_config['generator']()
            nb_data = json.loads(nb_json)
            
            # Create directory if doesn't exist
            nb_dir = os.path.join(BASE_DIR, nb_config['folder'])
            os.makedirs(nb_dir, exist_ok=True)
            
            # Write notebook file
            nb_path = os.path.join(nb_dir, "analysis.ipynb")
            with open(nb_path, 'w', encoding='utf-8') as f:
                json.dump(nb_data, f, indent=2, ensure_ascii=False)
            
            # Validation
            cell_count = len(nb_data['cells'])
            code_cells = sum(1 for c in nb_data['cells'] if c['cell_type'] == 'code')
            
            print(f"   [OK] Success: {cell_count} total cells ({code_cells} code cells)")
            print(f"   [OK] Saved to: {nb_path}")
            
            results.append({
                'name': nb_config['name'],
                'status': 'SUCCESS',
                'cells': cell_count,
                'code_cells': code_cells,
                'path': nb_path
            })
            
        except Exception as e:
            print(f"   [ERROR] {str(e)}")
            results.append({
                'name': nb_config['name'],
                'status': 'FAILED',
                'error': str(e)
            })
    
    # Summary
    print("\n" + "=" * 60)
    print("GENERATION SUMMARY")
    print("=" * 60)
    
    successful = sum(1 for r in results if r['status'] == 'SUCCESS')
    print(f"\n[OK] Successfully generated: {successful}/8 notebooks")
    
    if successful == 8:
        print("\n*** ALL NOTEBOOKS GENERATED SUCCESSFULLY! ***")
        print("\nNotebook Statistics:")
        for result in results:
            if result['status'] == 'SUCCESS':
                print(f"  - {result['name']}: {result['code_cells']} code cells")
    else:
        print("\n[WARNING] Some notebooks failed. See errors above.")
    
    return results

if __name__ == "__main__":
    results = generate_all_notebooks()
    
    # Print paths for user reference
    print("\n>> Generated notebook locations:")
    for result in results:
        if result['status'] == 'SUCCESS':
            print(f"  {result['name']}")
            print(f"    -> {result['path']}")

