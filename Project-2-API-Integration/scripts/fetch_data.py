import requests
import json
import os
 
API_KEY = "your_api_here"
STOCK_SYMBOL = "AAPL"
URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&apikey={API_KEY}"

def fetch_stock_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        os.makedirs("../data/raw", exist_ok=True)
        with open(f"../data/raw/{STOCK_SYMBOL}.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Stock data for {STOCK_SYMBOL} saved successfully.")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_stock_data()
