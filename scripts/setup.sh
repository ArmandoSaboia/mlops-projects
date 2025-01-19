#!/bin/bash

# Setup script for MLOps projects
echo "Setting up MLOps environment..."

# Install dependencies
pip install -r requirements.txt

# Setup infrastructure
if [ -d "infrastructure" ]; then
    cd infrastructure
    terraform init
fi 