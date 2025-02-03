#!/bin/bash

# Change to the directory where the Python scripts are located
cd /path/to/your/project/api-integration-stock-data

# Activate your virtual environment (if using one)
source venv/bin/activate

# Run the Python script to fetch the stock data
python src/fetch_data.py

# Deactivate the virtual environment after running the script
deactivate
