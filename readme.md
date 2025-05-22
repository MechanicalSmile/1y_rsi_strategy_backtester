# RSI-Based Trading Strategy Backtester

This project implements a simple RSI (Relative Strength Index) based trading strategy with configurable profit target and stop loss levels. It includes modules for data fetching, RSI calculation, signal generation, backtesting, and performance reporting.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Modules](#modules)  
- [Parameters](#parameters)  
- [Output](#output)  
- [Future Improvements](#future-improvements)  

---

## Overview

This project demonstrates an end-to-end workflow for algorithmic trading strategy development:

1. **Fetch historical price data** using Yahoo Finance (`yfinance`)  
2. **Calculate RSI** technical indicator using `ta` library  
3. **Generate buy/sell signals** based on RSI threshold, profit target, and stop loss  
4. **Backtest the strategy** to simulate trades  
5. **Generate a performance report** summarizing trade outcomes and returns  

---

## Features

- Fetch historical OHLC data from Yahoo Finance  
- Calculate RSI indicator with customizable period  
- Generate trading signals with entry and exit logic  
- Backtest trades with simple profit & loss calculation  
- Report total cash profit and percentage returns  

---

## Installation

1. Clone the repository or download the source code.  
2. Install dependencies (preferably in a virtual environment):

```bash
pip install yfinance pandas ta
```

---

## Usage

Modify the parameters in the main script to set:

- `ticker`: stock symbol (e.g., `"NCNA"`)  
- `start` and `end`: date range for data  
- `rsi_threshold`: RSI level to trigger buy signals  
- `profit_target`: fractional profit target (e.g., 0.05 for 5%)  
- `stop_loss`: fractional stop loss level (e.g., 0.02 for 2%)  

Run the script to fetch data, generate signals, backtest, and print a trade report.

---

## Modules

### `DataFetcher`

- Fetches historical market data from Yahoo Finance for a given ticker and date range.

### `calculate_rsi`

- Calculates the RSI indicator over closing prices and adds it as a new column.

### `RSIStrategy`

- Generates buy and sell signals based on RSI threshold, profit target, and stop loss.

### `Backtester`

- Simulates trades using the generated signals and records entry/exit dates, prices, and PnL.

### `ReportGenerator`

- Summarizes the trade results including total cash profit and percentage return.

---

## Parameters

| Parameter      | Description                             | Example        |
|----------------|---------------------------------------|----------------|
| `ticker`       | Stock symbol                          | `"NCNA"`       |
| `start`, `end` | Data range for historical prices      | `"2024-05-21"` |
| `rsi_threshold`| RSI level to trigger buy signal       | `35`           |
| `profit_target`| Target profit fraction for exit       | `0.05` (5%)    |
| `stop_loss`    | Stop loss fraction for exit            | `0.02` (2%)    |

---

## Output

The final output is a console report showing:

- Entry and exit dates/prices for each trade  
- Percentage and cash profit/loss per trade  
- Aggregate total cash profit and total percentage return  

Example:

```
  entry_date  exit_date  entry_price  exit_price  pnl_percent  cash_profit
0 2024-06-01 2024-06-10        10.00       10.50         5.00          50.0

Total Cash Profit: $50.00  
Total Percent Return: 5.00%
```

---

## Future Improvements

- Add commission and slippage modeling  
- Support multiple simultaneous positions and short selling  
- Enhance signal logic with other technical indicators  
- Visualize performance with equity curves and trade markers  
- Add parameter optimization for thresholds  

---

Feel free to customize or extend this project for your own trading strategy research!
