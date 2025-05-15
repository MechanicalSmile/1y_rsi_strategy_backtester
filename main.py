from datetime import datetime, timedelta
from data import DataFetcher
from utils import calculate_rsi
from strategy import RSIStrategy
from backtest import Backtester
from report import ReportGenerator

# Parameters
ticker = "NCNA"
end = datetime.today()
start = end - timedelta(days=365)
rsi_threshold = 35
profit_target = 0.05 # 5%
stop_loss = 0.02      # 2%

# Fetch & preprocess data
fetcher = DataFetcher(ticker, start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
data = fetcher.fetch()
data = calculate_rsi(data)

# Strategy
strategy = RSIStrategy(rsi_threshold, profit_target, stop_loss)
data = strategy.generate_signals(data)

# Backtest
backtester = Backtester(data)
trades = backtester.run()

# Report
report = ReportGenerator(trades)
report.generate()
