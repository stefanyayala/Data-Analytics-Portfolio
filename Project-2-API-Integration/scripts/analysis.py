import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load Processed Stock Data
STOCK_SYMBOL = "AAPL"
df = pd.read_csv(f"../data/processed/{STOCK_SYMBOL}.csv", index_col=0, parse_dates=True)

# print first few rows
print(df.head())

# Summary Statistics
print("Stock Data Summary:")
print(df.describe())

# Moving Averages
df['50_MA'] = df['Close'].rolling(window=50).mean()
df['200_MA'] = df['Close'].rolling(window=200).mean()

# Volatility (Standard Deviation over 30-day window)
df['Volatility'] = df['Close'].rolling(window=30).std()

# Plot Closing Prices with Moving Averages
plt.figure(figsize=(12,6))
plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
plt.plot(df.index, df['50_MA'], label='50-Day MA', color='red', linestyle='dashed')
plt.plot(df.index, df['200_MA'], label='200-Day MA', color='green', linestyle='dashed')
plt.title(f"{STOCK_SYMBOL} Stock Closing Prices & Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

# Interactive Price Chart using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price'))
fig.add_trace(go.Scatter(x=df.index, y=df['50_MA'], mode='lines', name='50-Day MA', line=dict(dash='dash')))
fig.add_trace(go.Scatter(x=df.index, y=df['200_MA'], mode='lines', name='200-Day MA', line=dict(dash='dot')))
fig.update_layout(title=f"{STOCK_SYMBOL} Stock Prices", xaxis_title="Date", yaxis_title="Price (USD)")
fig.show()

# Volatility Plot
plt.figure(figsize=(12,6))
plt.plot(df.index, df['Volatility'], label='30-Day Volatility', color='purple')
plt.title(f"{STOCK_SYMBOL} Stock Volatility Over Time")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.grid(True)
plt.show()

# Correlation Matrix
corr_matrix = df[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

print("Analysis Complete ✅")
