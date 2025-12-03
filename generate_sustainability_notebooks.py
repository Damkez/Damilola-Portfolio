import os
import json
from air_quality_monitoring_generator import generate_air_quality_notebook
from biodiversity_impact_generator import generate_biodiversity_notebook
from circular_economy_generator import generate_circular_economy_notebook
from esg_performance_generator import generate_esg_notebook
from green_building_generator import generate_green_building_notebook
from ocean_pollution_generator import generate_ocean_pollution_notebook
from renewable_energy_generator import generate_renewable_energy_notebook
from sustainable_agriculture_generator import generate_sustainable_agriculture_notebook
from sustainable_supply_chain_generator import generate_supply_chain_notebook
from waste_management_generator import generate_waste_management_notebook
from water_resource_generator import generate_water_resource_notebook

def main():
    base_dir = "Projects/Sustainability Data Analytics"
    
    generators = {
        "Air_Quality_Monitoring": generate_air_quality_notebook,
        "Biodiversity_Impact_Assessment": generate_biodiversity_notebook,
        "Circular_Economy_Metrics": generate_circular_economy_notebook,
        "ESG_Performance_Scoring": generate_esg_notebook,
        "Green_Building_Certification": generate_green_building_notebook,
        "Ocean_Pollution_Tracking": generate_ocean_pollution_notebook,
        "Renewable_Energy_Potential": generate_renewable_energy_notebook,
        "Sustainable_Agriculture_Metrics": generate_sustainable_agriculture_notebook,
        "Sustainable_Supply_Chain": generate_supply_chain_notebook,
        "Waste_Management_Optimization": generate_waste_management_notebook,
        "Water_Resource_Management": generate_water_resource_notebook
    }
    
    print("🚀 Starting Generation of 11 Sustainability Notebooks...")
    print("-" * 60)
    
    for folder, generator_func in generators.items():
        try:
            # Create directory
            target_dir = os.path.join(base_dir, folder)
            os.makedirs(target_dir, exist_ok=True)
            
            # Generate notebook content
            nb_json = generator_func()
            nb_data = json.loads(nb_json)
            
            # Inject 'Save Results' cell
            save_cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Save Results to Outputs Folder\n",
                    "import os\n",
                    "os.makedirs('outputs', exist_ok=True)\n",
                    "\n",
                    "# Save Summary Report\n",
                    "try:\n",
                    "    with open('outputs/summary_report.md', 'w', encoding='utf-8') as f:\n",
                    "        f.write(summary_md)\n",
                    "    print('✅ Summary report saved to outputs/summary_report.md')\n",
                    "except NameError:\n",
                    "    print('⚠️ summary_md not found, skipping report save')\n",
                    "\n",
                    "# Save Current Figure\n",
                    "try:\n",
                    "    plt.savefig('outputs/analysis_chart.png', dpi=300, bbox_inches='tight')\n",
                    "    print('✅ Analysis chart saved to outputs/analysis_chart.png')\n",
                    "except Exception as e:\n",
                    "    print(f'⚠️ Could not save chart: {e}')"
                ]
            }
            nb_data['cells'].append(save_cell)
            
            # Save file
            output_path = os.path.join(target_dir, "analysis.ipynb")
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(nb_data, f, indent=2)
                
            # Create outputs folder
            os.makedirs(os.path.join(target_dir, "outputs"), exist_ok=True)
            
            print(f"✅ {folder:<35} | {len(nb_data['cells']):<3} cells | Saved to {output_path}")
            
        except Exception as e:
            print(f"❌ {folder:<35} | Failed: {str(e)}")

    print("-" * 60)
    print("🎉 Generation Complete!")

if __name__ == "__main__":
    main()
