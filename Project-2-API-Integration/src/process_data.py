from config_loader import load_config  # Import the load_config function
import logging
from logging_config import setup_logging
from stock_data import StockData

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

    # Now use the loaded config values for the StockData object
    stock_data = StockData(stock_symbol, api_key)
    df = stock_data.process_data()

    if df is not None:
        logging.info(f"Data processed successfully for {stock_symbol}.")
        print("Data processed successfully.")
    else:
        logging.error(f"Data processing failed for {stock_symbol}.")
        print("Data processing failed.")

if __name__ == "__main__":
    main()
