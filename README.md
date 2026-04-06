# Market Equity Analysis using Python: Apple vs Microsoft 2016 - 2026

## Project Overview
This [project](https://roadmap.sh/projects/stock-price-time-series) provides a comprehensive quantitative analysis of historical stock data for two technology giants **Apple Inc. (AAPL)** and **Microsoft Corp. (MSFT)**. By leveraging the `yfinance` API, the system retrieves real-time and historical market data, performs time-series manipulation using `pandas`, and generates professional-grade visualizations for market trend analysis. The analysis covers price evolution, monthly resampling, technical indicators (Moving Averages), and market liquidity through trading volume comparisons. All data is retrieved via the [Yahoo Finance API](https://finance.yahoo.com/). The dataset includes Open, High, Low, Close, Adjusted Close, and Volume for the period of 2016 to early 2026.

## Features
* **Automated Data Acquisition**: Pulls high-fidelity data directly from Yahoo Finance.
* **Data Export**: Automatically exports the full raw dataset to a `.csv` file for external audit or Excel analysis.
* **Static Inspection**: Provides a baseline statistical summary (Mean, Std Dev, Min/Max) before processing.
* **Professional Visualization**: Generates and auto-saves four distinct analytical charts in high resolution.

## Technical Stack
* **Language**: Python 3
* **Libraries**: 
    * `pandas`: For data manipulation and time-series resampling.
    * `yfinance`: For fetching financial market data.
    * `matplotlib`: For professional data visualization.
    * `os`: For automated directory and file management.
      
---
## Analysis & Visualization Explained

### 1. Historical Price Evolution
![](https://github.com/nailatul-fadhilah-R/Market-Equity-Analysis-using-Python/blob/main/01_price_evolution_comparison.png) 
The long-term trend for both AAPL and MSFT over the last decade has been remarkably bullish. While both companies have followed a similar upward path—driven by the digital transformation and the expansion of cloud/AI services—their volatility profiles differ.
* **Growth Drivers**: The steady incline reflects strong fiscal health and dominant market positions. Significant "price jumps" visible in the charts often correlate with product launches (iPhone cycles for Apple) or major breakthroughs in enterprise software and Azure Cloud (Microsoft).
* **Correlation**: There is a high degree of correlation between the two. When the tech sector faces headwinds (like interest rate hikes or supply chain issues), both stocks tend to dip simultaneously, though one may recover faster depending on its quarterly earnings strength.

### 2. Monthly Resampled Trends
![](https://github.com/nailatul-fadhilah-R/Market-Equity-Analysis-using-Python/blob/main/02_monthly_resampled_trends.png)
By looking at the monthly mean rather than daily closing prices, we can observe the "true" direction of the market. Daily trading is often influenced by "noise"—short-term panic or over-excitement that doesn't reflect the company's value. 
* **The Smoothing Effect**: The monthly chart highlights that despite temporary daily crashes, the monthly floor (support level) has consistently risen. This suggests that for long-term investors, the "buy and hold" strategy has historically outperformed trying to "time the market" on a daily basis.

### 3. Technical Indicators: Moving Averages (MSFT)
![](https://github.com/nailatul-fadhilah-R/Market-Equity-Analysis-using-Python/blob/main/03_technical_indicators_msft.png)
Using Microsoft as our primary example for technical indicators, we observe the interaction between the 20-Day and 200-Day Moving Averages (MA).
* **The 200-Day MA (The Baseline)**: This serves as the "health check" for the stock. As long as the grey price line remains above the red 200-Day MA line, the stock is in a confirmed long-term uptrend.
* **The 20-Day MA (Momentum)**: This blue line follows the price more closely. When the 20-Day MA crosses above the 200-Day MA, it is technically known as a "Golden Cross", a strong buy signal indicating that short-term momentum is accelerating upward.

### 4. Market Liquidity: Volume Comparison
![](https://github.com/nailatul-fadhilah-R/Market-Equity-Analysis-using-Python/blob/main/04_market_volume_comparison.png)
The volume analysis reveals the "conviction" behind the price movements.
* **Apple’s Volume Dominance**: Historically, Apple often sees higher trading volumes than Microsoft. This is partly due to its massive retail investor base and high frequency of share turnover.
* **Volume Spikes**: Noticeable spikes in the volume chart usually indicate major news events or earnings calls. If a price increase happens on low volume, it is considered a weak trend. However, when the price rises on high volume (as seen in several sections of the chart), it confirms that institutional investors are heavily buying in, giving the trend more credibility.

---
