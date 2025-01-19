#!/bin/bash

# List of projects
projects=(
    "customer_insights"
    "sales_marketing"
    "operational_efficiency"
    "product_development"
    "fraud_detection"
    "financial_forecasting"
    "hr_talent_management"
    "healthcare_life_sciences"
    "retail_ecommerce"
    "cybersecurity"
    "energy_sustainability"
    "real_estate"
    "transportation_logistics"
    "media_entertainment"
    "agriculture"
    "legal_compliance"
    "education"
    "telecommunications"
)

# Path to the README template
template_path="templates/README_template.md"

# Loop through each project and generate a README.md file
for project in "${projects[@]}"; do
    # Path to the project's README.md
    readme_path="projects/$project/README.md"

    # Copy the template to the project's README.md
    cp "$template_path" "$readme_path"

    # Replace placeholders with project-specific details
    sed -i "s/Project Name/${project//_/ }/g" "$readme_path"
    sed -i "s/project_name/$project/g" "$readme_path"

    echo "Generated README.md for $project"
done

echo "All README.md files generated successfully!"
