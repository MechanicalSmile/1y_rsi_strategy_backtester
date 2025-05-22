import yfinance as yf
import pandas as pd

class DataFetcher:
    def __init__(self, ticker, start, end, interval='1d'):
        """
        Initialize the DataFetcher with parameters for the data request.
        
        Parameters:
        - ticker (str): The stock symbol to download data for (e.g., "AAPL").
        - start (str): The start date for the data range, formatted as 'YYYY-MM-DD'.
        - end (str): The end date for the data range, formatted as 'YYYY-MM-DD'.
        - interval (str): Data granularity, e.g., '1d' (daily), '1h' (hourly). Default is daily.
        """
        self.ticker = ticker
        self.start = start
        self.end = end
        self.interval = interval

    def fetch(self):
        """
        Download historical market data using yfinance for the specified ticker and date range.
        
        Returns:
        - A pandas DataFrame containing the historical OHLCV (Open, High, Low, Close, Volume) data.
        
        Behavior:
        - Automatically drops any rows with missing data to ensure clean dataset.
        - Data is not adjusted for splits/dividends by default (auto_adjust=False).
        """
        data = yf.download(
            self.ticker,
            start=self.start,
            end=self.end,
            interval=self.interval,
            auto_adjust=False  # Prices reflect raw market prices, not adjusted for dividends/splits
        )
        
        # Remove rows with any missing values to avoid issues in downstream calculations
        data.dropna(inplace=True)
        
        return data
