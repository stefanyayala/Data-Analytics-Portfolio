import json
import pandas as pd
import os

STOCK_SYMBOL = "AAPL"


def process_stock_data():
    file_path = f"../data/raw/{STOCK_SYMBOL}.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    time_series = data.get("Time Series (Daily)", {})

    if not time_series:
        print("No data found in JSON file.")
        return

    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    os.makedirs("../data/processed", exist_ok=True)
    df.to_csv(f"../data/processed/{STOCK_SYMBOL}.csv")
    print(f"Processed data saved: ../data/processed/{STOCK_SYMBOL}.csv")


if __name__ == "__main__":
    process_stock_data()
