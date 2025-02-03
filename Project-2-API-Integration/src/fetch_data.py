from config_loader import load_config  # Import the load_config function
from stock_data import StockData
import logging
from logging_config import setup_logging

# Setup logging configuration (only needs to be done once)
setup_logging()

# Now you can log messages in this script
logging.info('Fetching stock data...')
logging.error('Error occurred while fetching data.')


def main():
    # Load the configuration values (API key and stock symbol) from config.yaml
    config = load_config()
    api_key = config['api']['key']  # Access the API key from the config
    stock_symbol = config['stock']['symbol']  # Access the stock symbol from the config

    stock_data = StockData(stock_symbol, api_key)
    data = stock_data.fetch_data()
    if data:
        print("Data fetched successfully.")
    else:
        print("Data fetch failed.")


if __name__ == "__main__":
    main()