# 📊 Portfolio Analytics
## 🧠 Overview
The Portfolio Analytics project is designed to evaluate the performance of your SuperTrend trading strategy by comparing it against the BTC benchmark. This project uses the QuantStats library to generate detailed HTML reports, providing key performance metrics such as Sharpe ratio, Sortino ratio, and maximum drawdown, along with visualizations of portfolio growth and drawdowns. The reports are generated for multiple timeframes (15m, 1h, 4h, 1d).

### Key Features:
Compare SuperTrend strategy performance to Bitcoin’s benchmark returns.

Generate detailed performance reports using QuantStats.

<b>Visualize key metrics:</b> cumulative returns, equity curves, and drawdowns.

### 🛠️ Dependencies
To run the project, you need to install the required dependencies. You can install them via pip:

<pre>
pip install pandas quantstats
</pre>

### ⚙️ Setup & Configuration

<b>Data Requirements:</b> Ensure that you have the combined returns data in the CSV format with columns: datetime, superTrend_return, and btc_return.

The data should be in a directory like data/Combined-Returns/, with one file for each timeframe (15m, 1h, 4h, 1d), for example:

- SuperTrend_vs_BTC_Benchmark_15m_returns.csv
- SuperTrend_vs_BTC_Benchmark_1h_returns.csv
- SuperTrend_vs_BTC_Benchmark_4h_returns.csv
- SuperTrend_vs_BTC_Benchmark_1d_returns.csv

<b>Output Directory:</b>

The generated HTML reports will be saved in the data/Analytics-Reports/ directory. Make sure this directory exists, or it will be created automatically.

🏃‍♂️ Running the Portfolio Analytics
To generate performance reports for different timeframes, simply run the following Python script:

<pre>
python portfolio_analytics.py</pre>

<b>The script will:</b>

- Read the returns data for each timeframe.
- Compute the performance metrics.
- Generate and save an HTML report for each timeframe (15m, 1h, 4h, 1d).

The reports will be saved as:

<pre>
data/Analytics-Reports/SuperTrend_vs_BTC_15m.html
data/Analytics-Reports/SuperTrend_vs_BTC_1h.html
data/Analytics-Reports/SuperTrend_vs_BTC_4h.html
data/Analytics-Reports/SuperTrend_vs_BTC_1d.html
</pre>

### 📊 Results & Outputs

#### Performance Reports:
Each report will include:

- Cumulative Returns: Comparison of SuperTrend strategy returns vs. BTC.
- Sharpe Ratio: A measure of risk-adjusted return.
- Sortino Ratio: A ratio similar to Sharpe but focuses on downside risk.
- Maximum Drawdown: The largest loss from a peak to a trough in the portfolio.
- Time in the market

Example metrics from the report:

<pre>
metric,value
Annualized Return,0.12
Sharpe Ratio,1.45
Sortino Ratio,2.10
Max Drawdown,-0.25
</pre>

Visuals:
Equity Curve: Shows the growth of your portfolio over time.

Cumulative Returns: Visual comparison between the SuperTrend strategy and BTC.

Drawdown Chart: Highlights the largest drawdowns during the period.

### 🏅 Performance Comparison
Based on the analysis of returns across the different timeframes, the performance of the strategy showed the following order:

| Timeframe             | Performance Ranking | Notes                                                                                                                                                |
|-----------------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **4-hour** (`4h`)     | 🥇 Best Performing  | The **4-hour** timeframe provided the highest returns, showing strong outperformance against the BTC benchmark.                                      |
| **1-day** (`1d`)      | 🥈 Second Best      | The **1-day** timeframe performed well but generated lower returns compared to the 4-hour strategy.                                                  |
| **1-hour** (`1h`)     | 🥉 Third Place      | The **1-hour** timeframe showed decent results but underperformed compared to the higher timeframes.                                                 |
| **15-minute** (`15m`) | ❌ Worst Performing  | The **15-minute** timeframe had the lowest returns, likely due to higher noise and smaller market moves, resulting in less profitable opportunities. |

### ✅ Conclusion
This project allows you to:

Evaluate and compare the performance of your SuperTrend strategy against BTC over different timeframes.

Use the QuantStats library to generate detailed performance metrics and visualizations, helping you make informed decisions about strategy optimization and risk management.

After running the project, you'll have the necessary insights to:

Understand the risk-return profile of your strategy.

Optimize trading decisions based on detailed analytics.

Make improvements to your strategy for better performance.

## ❓ Troubleshooting
**Missing Data Files:** If the CSV files are not found or incorrectly formatted, the script will fail. Ensure that the data/Combined-Returns/ directory contains the correct files.

**Output Directory Not Found:** If the data/Analytics-Reports/ directory does not exist, the script will create it automatically.

