from datetime import datetime, timedelta
from data import DataFetcher               # Module/class responsible for fetching historical market data
from utils import calculate_rsi            # Function to compute the Relative Strength Index (RSI) indicator
from strategy import RSIStrategy           # Strategy class implementing trading logic based on RSI
from backtest import Backtester            # Class to simulate trades on historical data to evaluate strategy performance
from report import ReportGenerator         # Class to generate performance reports from backtest results

# Parameters
ticker = "NCNA"                           # Stock ticker symbol to analyze
end = datetime.today()                    # End date for historical data fetch (today)
start = end - timedelta(days=365)        # Start date for historical data fetch (1 year before end date)
rsi_threshold = 35                       # RSI threshold to trigger buy signals (oversold level)
profit_target = 0.05                     # Profit target of 5% for closing trades
stop_loss = 0.02                        # Stop loss threshold of 2% to limit downside risk

# Fetch & preprocess data
fetcher = DataFetcher(ticker, start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
# Instantiate the data fetcher with ticker and date range formatted as strings

data = fetcher.fetch()
# Retrieve historical price data (e.g., OHLCV) for the specified ticker and period

data = calculate_rsi(data)
# Calculate RSI values for the fetched data, adding the RSI as a new column for later signal generation

# Strategy
strategy = RSIStrategy(rsi_threshold, profit_target, stop_loss)
# Initialize the trading strategy object with defined parameters for RSI threshold, profit target, and stop loss

data = strategy.generate_signals(data)
# Apply the strategy's signal generation logic to the dataset
# This typically marks each row with a buy/sell/hold signal based on RSI and trade management rules

# Backtest
backtester = Backtester(data)
# Create a backtester object with the data containing trading signals

trades = backtester.run()
# Execute the backtest, simulating trades over historical data according to the signals
# Returns a summary of trades executed, including entry/exit points, returns, etc.

# Report
report = ReportGenerator(trades)
# Initialize the report generator with the trade results

report.generate()
# Generate a report analyzing the backtest results, including performance metrics, trade statistics, and possibly visualizations
