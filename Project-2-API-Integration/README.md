# API Integration for Stock Data Analysis

## Project Overview

This project demonstrates an end-to-end integration of stock data from an external API, the processing of the raw data, and its subsequent analysis and visualization. The system fetches stock data for a given stock symbol, processes it, performs exploratory data analysis (EDA), and generates meaningful insights such as moving averages and volatility. The results are stored, visualized interactively, and logged for traceability. 

This solution is designed to showcase key skills in API integration, data processing, logging, testing, and analysis, which are integral to data engineering, business intelligence, and data science roles.

## Key Technologies

- **Python 3.x**  
- **pandas** for data manipulation
- **matplotlib & seaborn** for data visualization
- **plotly** for interactive visualizations
- **unittest** for testing
- **yaml** for configuration management
- **logging** for logging API requests, errors, and general processes
- **pytest** for running unit tests
- **dotenv** for environment variable management
- **Git** for version control
- **Cron Jobs** for scheduling fetch operations

## Folder Structure

```bash
api-integration-stock-data/
├── data/                    
│   ├── raw/                 
│   └── processed/           
├── src/                     
│   ├── __init__.py          
│   ├── stock_data.py        
│   ├── fetch_data.py        
│   ├── process_data.py      
│   └── analysis.py          
├── tests/                   
│   ├── __init__.py          
│   └── test_stock_data.py   
├── notebooks/               
│   └── stock_analysis.ipynb 
├── logs/                    
│   └── app.log              
├── config/                  
│   └── config.yaml          
├── requirements.txt         
├── README.md                
├── .gitignore               
└── cron_jobs/               
    └── fetch_data_cron.sh 
```

### Description of Folders

- **data/**: Contains raw and processed stock data files.
- **src/**: Contains the Python scripts for fetching, processing, and analyzing the stock data.
- **tests/**: Unit tests for validating the functionality of the project.
- **notebooks/**: Jupyter notebook for exploratory analysis and visualizations.
- **logs/**: Application logs to trace the processing flow and errors.
- **config/**: Contains the `config.yaml` file for API configuration (API key, stock symbol).
- **cron_jobs/**: Shell scripts for scheduling periodic fetch operations.

## Features

- **Stock Data Fetching**: Fetch stock data using the Alpha Vantage API.
- **Data Processing**: Clean and transform raw data into structured data using pandas.
- **Moving Averages & Volatility**: Calculate and visualize moving averages (50-day and 200-day) and volatility (30-day standard deviation).
- **Exploratory Data Analysis (EDA)**: Perform EDA using statistical summaries and correlation matrices.
- **Visualization**: Generate both static and interactive charts to display the stock data and analysis results.
- **Logging**: Implement logging to track the application's activity and errors.
- **Testing**: Comprehensive unit tests to ensure the correctness of the implemented features.

## Installation

To get started with this project, you'll need Python 3.7 or higher installed. You can set up the project by following these steps:

1. Clone the repository:

```bash
git clone https://github.com/stefanyayala/Data-Analytics-Portfolio.git
cd Project-2-API-Integration
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - **Windows**: 
     ```bash
     .\venv\Scripts\activate
     ```

   - **Mac/Linux**: 
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Set up environment variables or modify `config.yaml` for your API key and stock symbol:
   - Add your API key and the desired stock symbol in the `config.yaml`.

## Configuration

The configuration for the project is stored in the `config/config.yaml` file. Below is the structure of the `config.yaml`:

```yaml
api:
  key: "your_api_key_here"
  url: "https://api.example.com/stock_data?symbol={symbol}&apikey={key}"

stock:
  symbol: "AAPL"
```

You can also use environment variables instead of storing the API key directly in the file. Modify your environment variables and ensure the API key is retrieved dynamically during runtime.

## Logging

All interactions, including data fetching and errors, are logged using Python's `logging` module. Logs are stored in `logs/app.log`.

The `logging_config.py` file sets up the logging format, log level, and output location.

Example of log entry:

```bash
2025-02-03 12:34:56,789 - INFO - Fetching stock data for AAPL
2025-02-03 12:35:10,234 - ERROR - Failed to fetch data: 400
```

## Cron Jobs

You can schedule the fetching of stock data periodically using cron jobs. A sample cron job script `fetch_data_cron.sh` is included to run the fetch operation at set intervals (e.g., every hour).

### Sample Cron Job Script

```bash
#!/bin/bash

# Run the fetch_data.py script
python /path/to/fetch_data.py
```

To schedule it, you can use the `cron` utility on Unix-based systems.

## Running the Project

### Fetching Data

To fetch stock data manually, run the `fetch_data.py` script:

```bash
python src/fetch_data.py
```

### Processing Data

Once the data is fetched, you can process the raw data by running the `process_data.py` script:

```bash
python src/process_data.py
```

### Analyzing Data

To perform analysis and generate visualizations, run the `analysis.py` script:

```bash
python src/analysis.py
```

Alternatively, you can explore the data analysis interactively in the Jupyter notebook (`notebooks/stock_analysis.ipynb`).

## Testing

The project includes unit tests located in the `tests/test_stock_data.py` file. To run the tests, you can use `pytest`:

```bash
pytest tests/test_stock_data.py
```

This will run the unit tests for the project and validate that the functionality is working as expected.

## Example of Unit Tests

The tests include functions for:

- **`test_fetch_data()`**: Verifying that data is fetched successfully.
- **`test_process_data()`**: Checking if the raw data is processed into a pandas DataFrame correctly.

## Contributing

Contributions to this project are welcomed. If you wish to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a description of the changes.

## License

This project is licensed under the MIT License.
