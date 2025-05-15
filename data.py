import yfinance as yf
import pandas as pd

class DataFetcher:
    def __init__(self, ticker, start, end, interval='1d'):
        self.ticker = ticker
        self.start = start
        self.end = end
        self.interval = interval

    def fetch(self):
        data = yf.download(self.ticker, start=self.start, end=self.end, interval=self.interval, auto_adjust=False)
        data.dropna(inplace=True)
        return data
