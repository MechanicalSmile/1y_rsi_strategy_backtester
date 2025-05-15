import pandas as pd

class Backtester:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.trades = []

    def run(self):
        in_position = False
        entry_price = 0.0
        entry_date = None

        for i, row in self.data.iterrows():
            signal = row['Signal'].item() if isinstance(row['Signal'], pd.Series) else row['Signal']
            if signal == 1 and not in_position:
                in_position = True
                entry_price = row['Close']
                entry_date = i
            elif signal == -1 and in_position:
                exit_price = row['Close']
                pnl = (exit_price - entry_price) / entry_price
                self.trades.append({
                    'entry_date': entry_date,
                    'exit_date': i,
                    'entry_price': float(entry_price.iloc[0]) if isinstance(entry_price, pd.Series) else float(entry_price),
                    'exit_price': float(exit_price.iloc[0]) if isinstance(exit_price, pd.Series) else float(exit_price),
                    'pnl': float(pnl.iloc[0]) if isinstance(pnl, pd.Series) else float(pnl)
                })
                in_position = False

        return self.trades
