import pandas as pd
from ta.momentum import RSIIndicator

def calculate_rsi(data: pd.DataFrame, period=14):
    """
    Calculate the Relative Strength Index (RSI) for the given price data and add it as a new column.
    
    Parameters:
    - data: pandas DataFrame containing at least a 'Close' price column.
    - period: the window length for RSI calculation, default is 14 periods.
    
    Returns:
    - The original DataFrame augmented with a new 'RSI' column containing the RSI values.
    """
    
    # Defensive check: if 'Close' column is a DataFrame (multi-column), convert to Series
    if isinstance(data['Close'], pd.DataFrame):
        close_series = data['Close'].squeeze()  # Converts single-column DataFrame to Series
    else:
        close_series = data['Close']             # Already a Series
    
    # Create an RSIIndicator object from the ta library, specifying the close prices and period
    rsi = RSIIndicator(close=close_series, window=period)
    
    # Calculate RSI values and assign them to a new 'RSI' column in the DataFrame
    data['RSI'] = rsi.rsi()
    
    return data
