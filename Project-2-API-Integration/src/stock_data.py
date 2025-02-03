import requests
import json
import pandas as pd
import os
import logging
from logging_config import setup_logging
import sys

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Setup logging configuration (only needs to be done once)
setup_logging()

# Now you can log messages in this script
logging.info('Fetching stock data...')
logging.error('Error occurred while fetching data.')

class StockData:
    def __init__(self, stock_symbol, api_key):
        self.stock_symbol = stock_symbol
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def fetch_data(self):
        url = f"{self.base_url}?function=TIME_SERIES_DAILY&symbol={self.stock_symbol}&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.save_raw_data(data)
            return data
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None

    def save_raw_data(self, data):
        os.makedirs("../data/raw", exist_ok=True)
        file_path = f"../data/raw/{self.stock_symbol}.json"
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Raw data saved to {file_path}")

    def process_data(self):
        file_path = f"../data/raw/{self.stock_symbol}.json"
        with open(file_path, "r") as file:
            data = json.load(file)

        time_series = data.get("Time Series (Daily)", {})
        if not time_series:
            print("No data found in JSON file.")
            return None

        df = pd.DataFrame.from_dict(time_series, orient="index")
        df.columns = ["Open", "High", "Low", "Close", "Volume"]
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)

        os.makedirs("../data/processed", exist_ok=True)
        processed_file = f"../data/processed/{self.stock_symbol}.csv"
        df.to_csv(processed_file)
        print(f"Processed data saved to {processed_file}")
        return df
