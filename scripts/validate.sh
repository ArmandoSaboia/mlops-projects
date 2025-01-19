#!/bin/bash

# Validation script
echo "Validating projects..."

# Run tests
for d in projects/*/; do
    if [ -f "${d}setup.py" ]; then
        cd "$d"
        pytest tests/
        cd ../../
    fi
done 