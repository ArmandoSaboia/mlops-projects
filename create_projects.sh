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

# Base directory
base_dir="projects"

# Create the base directory if it doesn't exist
mkdir -p "$base_dir"

# Loop through each project and create the folder structure
for project in "${projects[@]}"; do
    # Create the project directory
    project_dir="$base_dir/$project"
    mkdir -p "$project_dir"

    # Create subdirectories
    mkdir -p "$project_dir/data/raw"
    mkdir -p "$project_dir/data/processed"
    mkdir -p "$project_dir/data_ingestion"
    mkdir -p "$project_dir/features"
    mkdir -p "$project_dir/models"
    mkdir -p "$project_dir/training"
    mkdir -p "$project_dir/inference"
    mkdir -p "$project_dir/streamlit_app"
    mkdir -p "$project_dir/tests"
    mkdir -p "$project_dir/dags"

    # Create empty files
    touch "$project_dir/README.md"
    touch "$project_dir/requirements.txt"
    touch "$project_dir/Dockerfile"
    touch "$project_dir/docker-compose.yml"
    touch "$project_dir/data_ingestion/api_client.py"
    touch "$project_dir/data_ingestion/db_client.py"
    touch "$project_dir/features/build_features.py"
    touch "$project_dir/features/feature_utils.py"
    touch "$project_dir/training/train_churn.py"
    touch "$project_dir/training/train_recommendation.py"
    touch "$project_dir/inference/main.py"
    touch "$project_dir/inference/model_loader.py"
    touch "$project_dir/streamlit_app/app.py"
    touch "$project_dir/streamlit_app/utils.py"
    touch "$project_dir/tests/test_api.py"
    touch "$project_dir/tests/test_features.py"
    touch "$project_dir/dags/data_pipeline.py"

    echo "Created project structure for $project"
done

echo "All project folders created successfully!"
