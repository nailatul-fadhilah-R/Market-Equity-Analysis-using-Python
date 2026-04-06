import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

output_dir = 'stock_analysis_results'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' created.")

tickers = ['AAPL', 'MSFT']
print("Downloading historical data for Apple and Microsoft...")
raw_data = yf.download(tickers, start="2016-04-05", end="2026-04-05")

# STATIC DATA INSPECTION
print("\n PRELIMINARY STATIC DATA INSPECTION")
print("---"*20)
print(f"Dataset Shape: {raw_data.shape}")
print("\nData Types and Structure:")
print(raw_data.info())

print("\nFirst 5 Rows of Closing Prices:")
print(raw_data['Close'].head())

print("\nMissing Values per Ticker:")
print(raw_data['Close'].isnull().sum())

print("\nStatistical Overview:")
print(raw_data['Close'].describe())
print("---"*20 + "\n")

plt.figure(figsize=(14, 7), dpi=100)
plt.plot(raw_data['Close']['AAPL'], label='Apple (AAPL)', color='#555555', linewidth=1.5)
plt.plot(raw_data['Close']['MSFT'], label='Microsoft (MSFT)', color='#00a4ef', linewidth=1.5)

plt.title('Closing Price Evolution: AAPL vs MSFT (2016 - 2026)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Stock Price (USD)', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, linestyle=':', alpha=0.6)

plt.savefig(f'{output_dir}/01_price_evolution_comparison.png')
print(f"Saved: {output_dir}/01_price_evolution_comparison.png")
plt.show()

# Monthly Resampling Analysis
monthly_data = raw_data['Close'].resample('M').mean()

plt.figure(figsize=(14, 7), dpi=100)
plt.plot(monthly_data['AAPL'], label='Apple Monthly Mean', marker='o', markersize=4)
plt.plot(monthly_data['MSFT'], label='Microsoft Monthly Mean', marker='s', markersize=4)
plt.title('Monthly Average Closing Prices (Resampled)', fontsize=16)
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

plt.savefig(f'{output_dir}/02_monthly_resampled_trends.png')
print(f"Saved: {output_dir}/02_monthly_resampled_trends.png")
plt.show()

# Moving Averages for Microsoft (Trend Analysis)
msft_trend = raw_data['Close']['MSFT'].to_frame()
msft_trend['MA_20'] = msft_trend['MSFT'].rolling(window=20).mean()
msft_trend['MA_200'] = msft_trend['MSFT'].rolling(window=200).mean()

plt.figure(figsize=(14, 7), dpi=100)
plt.plot(msft_trend['MSFT'], label='MSFT Actual Close', color='lightgray', alpha=0.5)
plt.plot(msft_trend['MA_20'], label='20-Day Short-term MA', color='#0078d4')
plt.plot(msft_trend['MA_200'], label='200-Day Long-term MA', color='#d83b01')
plt.title('Microsoft (MSFT) Technical Analysis: Moving Averages', fontsize=16)
plt.legend()

plt.savefig(f'{output_dir}/03_technical_indicators_msft.png')
print(f"Saved: {output_dir}/03_technical_indicators_msft.png")
plt.show()

# Trading Volume Comparison
plt.figure(figsize=(14, 6), dpi=100)
plt.fill_between(raw_data.index, raw_data['Volume']['AAPL'], label='Apple Volume', alpha=0.3, color='gray')
plt.fill_between(raw_data.index, raw_data['Volume']['MSFT'], label='Microsoft Volume', alpha=0.3, color='blue')
plt.title('Market Liquidity: Trading Volume Comparison', fontsize=16)
plt.ylabel('Volume Units')
plt.legend()

plt.savefig(f'{output_dir}/04_market_volume_comparison.png')
print(f"Saved: {output_dir}/04_market_volume_comparison.png")
plt.show()
