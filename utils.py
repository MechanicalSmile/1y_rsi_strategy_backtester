import pandas as pd
from ta.momentum import RSIIndicator

def calculate_rsi(data: pd.DataFrame, period=14):
    # Ensure 'Close' is a Series, not a DataFrame
    if isinstance(data['Close'], pd.DataFrame):
        close_series = data['Close'].squeeze()
    else:
        close_series = data['Close']

    rsi = RSIIndicator(close=close_series, window=period)
    data['RSI'] = rsi.rsi()
    return data
