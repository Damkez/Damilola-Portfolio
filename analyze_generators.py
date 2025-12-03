"""
Script to add output-saving functionality to all remaining sustainability generators.
This adds:
1. import os
2. os.makedirs('outputs') 
3. plt.savefig() before plt.show()
4. Map.to_html() for geemap maps
"""

import re

GENERATORS = [
    'biodiversity_impact_generator.py',
    'circular_economy_generator.py',
    'esg_performance_generator.py',
    'green_building_generator.py',
    'ocean_pollution_generator.py',
    'sustainable_agriculture_generator.py',
    'sustainable_supply_chain_generator.py',
    'waste_management_generator.py',
    'water_resource_generator.py'
]

def add_output_saving(filename):
    """Add output-saving code to a generator file."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track changes
    changes = []
    
    # 1. Add import os if not present
    if 'import os' not in content:
        # Find first nbf.v4.new_code_cell after imports
        pattern = r'(import matplotlib\.pyplot as plt\n)'
        replacement = r'\1import os\n'
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            changes.append("Added 'import os'")
    
    # 2. Add outputs directory creation after ee.Initialize()
    pattern = r'(ee\.Initialize\(\)[\s\S]{1,100}?)(\n\n# Configuration)'
    replacement = r'\1\n\n# Create outputs directory\nif not os.path.exists(\'outputs\'):\n    os.makedirs(\'outputs\')\2'
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content, count=1)
        changes.append("Added outputs directory creation")
    
    # 3. Add plt.savefig() before plt.show()
    # This is complex because we need unique filenames - just report locations
    show_matches = list(re.finditer(r'plt\.show\(\)', content))
    changes.append(f"Found {len(show_matches)} plt.show() calls that need savefig")
    
    # 4. Find Map references (geemap)
    map_matches = list(re.finditer(r'\nMap\"\"\"\)', content))
    changes.append(f"Found {len(map_matches)} Map displays that may need to_html")
    
    print(f"\n{filename}:")
    for change in changes:
        print(f"  - {change}")
    
    return content

# Run analysis
print("=" * 60)
print("ANALYSIS OF SUSTAINABILITY GENERATORS")
print("=" * 60)

for gen in GENERATORS:
    try:
        add_output_saving(gen)
    except FileNotFoundError:
        print(f"\n{gen}: FILE NOT FOUND")
    except Exception as e:
        print(f"\n{gen}: ERROR - {e}")

print("\n" + "=" * 60)
print("Manual modifications needed - creating detailed list...")
