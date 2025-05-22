import pandas as pd

class RSIStrategy:
    def __init__(self, rsi_threshold, profit_target, stop_loss):
        """
        Initialize the RSI-based trading strategy.
        
        Parameters:
        - rsi_threshold: RSI value below which a buy signal is triggered (e.g., 35, indicating oversold)
        - profit_target: target profit level as a decimal (e.g., 0.05 for 5%)
        - stop_loss: maximum tolerable loss as a decimal (e.g., 0.02 for 2%)
        """
        self.rsi_threshold = rsi_threshold
        self.profit_target = profit_target
        self.stop_loss = stop_loss

    def generate_signals(self, data: pd.DataFrame):
        """
        Generate trading signals based on RSI threshold, profit target, and stop loss.
        
        Args:
        - data: pandas DataFrame containing at least 'RSI' and 'Close' columns.
        
        Returns:
        - Modified DataFrame with an additional 'Signal' column:
          1 = buy, -1 = sell, 0 = hold.
        """
        data = data.copy()           # Work on a copy to avoid mutating original data
        data['Signal'] = 0           # Initialize all signals as 'hold' (0)
        
        in_position = False          # Tracks whether currently holding a position
        entry_price = 0.0            # Price at which current position was opened

        # Iterate over data starting from second row (index 1) to avoid indexing issues
        for i in range(1, len(data)):
            if not in_position and data['RSI'].iloc[i] < self.rsi_threshold:
                # Entry condition: RSI below threshold and currently flat
                data.at[data.index[i], 'Signal'] = 1    # Buy signal
                entry_price = float(data['Close'].iloc[i].item())  # Record entry price
                in_position = True

            elif in_position:
                current_price = float(data['Close'].iloc[i].item())
                # Calculate return relative to entry price
                change = (current_price - entry_price) / entry_price

                # Exit conditions: either target profit reached or stop loss triggered
                if change >= self.profit_target or change <= -self.stop_loss:
                    data.at[data.index[i], 'Signal'] = -1  # Sell signal
                    in_position = False                     # Exit position

        return data
