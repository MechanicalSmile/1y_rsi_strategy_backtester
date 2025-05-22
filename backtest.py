import pandas as pd

class Backtester:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the backtester with historical data containing trading signals.
        
        Parameters:
        - data: pandas DataFrame expected to include at least:
            - 'Close': closing price for each period
            - 'Signal': trading signal per period (1 for buy, -1 for sell, 0 or None for hold)
        """
        self.data = data
        self.trades = []  # List to store completed trades with entry/exit details and PnL

    def run(self):
        """
        Execute the backtest simulation by iterating through the data and simulating trades
        according to the signals.
        
        Returns:
        - A list of dictionaries, each representing a completed trade with:
            - 'entry_date', 'exit_date': timestamps of trade open/close
            - 'entry_price', 'exit_price': prices at trade open/close
            - 'pnl': profit or loss for the trade expressed as a decimal fraction (e.g., 0.05 = 5%)
        """
        in_position = False   # Flag to track if currently holding a position
        entry_price = 0.0     # Price at which the current position was entered
        entry_date = None     # Timestamp of entry

        # Iterate over each row in the DataFrame, where 'i' is the index (date) and 'row' the data
        for i, row in self.data.iterrows():
            # Extract signal safely:
            # If 'Signal' column contains pd.Series (rare, but defensive coding), take the scalar
            signal = row['Signal'].item() if isinstance(row['Signal'], pd.Series) else row['Signal']

            if signal == 1 and not in_position:
                # Enter a new long position if signal is buy (1) and currently not in position
                in_position = True
                entry_price = row['Close']
                entry_date = i

            elif signal == -1 and in_position:
                # Exit the current position if signal is sell (-1) and currently in position
                exit_price = row['Close']
                # Calculate profit or loss as a fractional return: (exit - entry) / entry
                pnl = (exit_price - entry_price) / entry_price

                # Append the completed trade's details to the trade list
                # Defensive conversions to float in case data are wrapped in pandas types or Series
                self.trades.append({
                    'entry_date': entry_date,
                    'exit_date': i,
                    'entry_price': float(entry_price.iloc[0]) if isinstance(entry_price, pd.Series) else float(entry_price),
                    'exit_price': float(exit_price.iloc[0]) if isinstance(exit_price, pd.Series) else float(exit_price),
                    'pnl': float(pnl.iloc[0]) if isinstance(pnl, pd.Series) else float(pnl)
                })

                # Mark that we have exited the position
                in_position = False

        # Return the list of trades executed during the backtest
        return self.trades
