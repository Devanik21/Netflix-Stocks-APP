# Netflix Stocks APP

![Language](https://img.shields.io/badge/Language-Jupyter%20Notebook-DA5B0B?style=flat-square) ![Stars](https://img.shields.io/github/stars/Devanik21/Netflix-Stocks-APP?style=flat-square&color=yellow) ![Forks](https://img.shields.io/github/forks/Devanik21/Netflix-Stocks-APP?style=flat-square&color=blue) ![Author](https://img.shields.io/badge/Author-Devanik21-black?style=flat-square&logo=github) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> Netflix stock intelligence — technical analysis, trend detection, and forecasting in an interactive Streamlit dashboard.

---

**Topics:** `data-science` · `deep-learning` · `financial-analysis` · `lstm-stock-prediction` · `machine-learning` · `neural-networks` · `python` · `streamlit` · `time-series-forecasting` · `yahoo-finance`

## Overview

This application is a comprehensive financial analytics dashboard for Netflix Inc. (NFLX) stock price history, built with Streamlit and Plotly for institutional-grade interactive charting. It fetches historical OHLCV (Open, High, Low, Close, Volume) data via the yfinance library and computes a full suite of technical indicators commonly used by quantitative analysts and active traders.

The dashboard is organised into three analytical layers. The first is a price action layer: interactive candlestick charts with configurable date ranges and volume overlays. The second is a technical indicator layer: Simple Moving Averages (SMA-20, SMA-50, SMA-200), Exponential Moving Averages, Bollinger Bands, Relative Strength Index (RSI), MACD with signal line, and Average True Range (ATR) for volatility measurement. The third is a statistical layer: rolling volatility, historical Value-at-Risk (VaR) at configurable confidence levels, and maximum drawdown analysis.

An optional ML forecasting module uses a simple ARIMA or Prophet model to project short-term price trends, with clearly labelled uncertainty bands to prevent over-interpretation of point estimates.

---

## Motivation

Financial data literacy — the ability to read price charts, understand indicator signals, and contextualise stock performance — is a skill that should not require expensive proprietary software. This project was built to provide a fully open-source, self-hosted stock analysis dashboard that brings together the most important technical analysis tools in a single, reproducible Python application.

---

## Architecture

```
yfinance API → OHLCV DataFrame
        │
  Technical Indicator Computation (pandas_ta / custom)
  (SMA, EMA, BB, RSI, MACD, ATR, OBV)
        │
  ┌────────────────────────────────┐
  │  Plotly Interactive Dashboard  │
  │  - Candlestick + Volume         │
  │  - Indicator Overlays           │
  │  - Statistical Metrics Panel   │
  └────────────────────────────────┘
        │
  Optional: ARIMA / Prophet Forecast
```

---

## Features

### Interactive Candlestick Chart
Full-featured OHLCV candlestick chart with Plotly — zoom, pan, hover OHLC values, and configurable date range selector from 1 month to 10 years.

### Moving Average Suite
SMA-20, SMA-50, SMA-200, EMA-12, EMA-26 overlaid on the price chart with colour-coded lines and toggle visibility controls.

### Bollinger Bands
20-period Bollinger Bands with configurable standard deviation multiplier, upper/lower band fill, and %B indicator subplot.

### RSI and MACD Subplots
Relative Strength Index (14-period) with overbought/oversold threshold lines, and MACD histogram with signal line in a dedicated subplot.

### Volatility and Risk Metrics
Rolling 30-day historical volatility, annualised volatility (σ√252), Value-at-Risk at 95%/99% confidence, and maximum drawdown from peak.

### Volume Profile Analysis
Volume bar chart with colour-coding (up/down days) and On-Balance Volume (OBV) cumulative indicator for trend confirmation.

### ML Price Forecast (Optional)
ARIMA or Facebook Prophet short-term price forecast with 80% and 95% confidence intervals, clearly marked as projections not predictions.

### Data Export
Download the full OHLCV + indicators DataFrame as a CSV file for use in external analysis tools like Excel or R.

---

## Tech Stack

| Library / Tool | Role | Why This Choice |
|---|---|---|
| **Streamlit** | Dashboard framework | Sidebar controls, layout, widget state |
| **yfinance** | Market data source | Historical OHLCV data via Yahoo Finance API |
| **pandas** | Data manipulation | Rolling calculations, indicator computation |
| **Plotly** | Interactive charting | Candlestick, subplots, dual-axis charts |
| **NumPy** | Numerical operations | VaR computation, array operations |
| **statsmodels** | ARIMA forecasting | Time-series forecasting model |
| **Prophet (optional)** | Facebook Prophet | Trend + seasonality decomposition forecast |

> **Key packages detected in this repo:** `scikit-learn` · `numpy` · `pandas` · `matplotlib` · `seaborn` · `scipy` · `xgboost` · `lightgbm` · `catboost` · `tensorflow`

---

## Getting Started

### Prerequisites

- Python 3.9+ (or Node.js 18+ for TypeScript/JS projects)
- `pip` or `npm` package manager
- Relevant API keys (see Configuration section)

### Installation

```bash
git clone https://github.com/Devanik21/Netflix-Stocks-APP.git
cd Netflix-Stocks-APP
python -m venv venv && source venv/bin/activate
pip install streamlit yfinance pandas plotly numpy statsmodels
streamlit run app.py
```

---

## Usage

```bash
# Launch dashboard
streamlit run app.py

# Download Netflix data programmatically
python -c "import yfinance as yf; yf.download('NFLX','2015-01-01').to_csv('nflx.csv')"

# Run ARIMA forecast standalone
python forecast.py --ticker NFLX --horizon 30
```

---

## Configuration

| Variable | Default | Description |
|---|---|---|
| `TICKER` | `NFLX` | Stock ticker symbol |
| `DEFAULT_PERIOD` | `2y` | Default historical data window |
| `BB_WINDOW` | `20` | Bollinger Band moving average window |
| `RSI_PERIOD` | `14` | RSI computation period |
| `VAR_CONFIDENCE` | `0.95` | Value-at-Risk confidence level |

> Copy `.env.example` to `.env` and populate all required values before running.

---

## Project Structure

```
Netflix-Stocks-APP/
├── README.md
├── requirements.txt
├── about.py
├── analyze.py
├── app.py
├── feedback.py
├── home.py
├── ADV_stock-NETFLIX.ipynb
├── .devcontainer/devcontainer.json
├── NFLX.csv
└── ...
```

---

## Roadmap

- [ ] Portfolio-level dashboard supporting multiple tickers simultaneously
- [ ] Earnings calendar overlay with analyst estimate vs. actual EPS display
- [ ] Options chain viewer with implied volatility surface plot
- [ ] Sentiment analysis integration from financial news headlines (FinBERT)
- [ ] Backtesting module for simple technical trading strategies

---

## Contributing

Contributions, issues, and feature requests are welcome. Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow conventional commit messages and ensure any new code is documented.

---

## Notes

All market data is sourced from Yahoo Finance via yfinance. Data may have minor inaccuracies for splits and dividends. This dashboard is for educational and informational purposes only and does not constitute financial advice.

---

## Author

**Devanik Debnath**  
B.Tech, Electronics & Communication Engineering  
National Institute of Technology Agartala

[![GitHub](https://img.shields.io/badge/GitHub-Devanik21-black?style=flat-square&logo=github)](https://github.com/Devanik21)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-devanik-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/devanik/)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Crafted with curiosity, precision, and a belief that good software is worth building well.*
