import pandas as pd

class ReportGenerator:
    def __init__(self, trades, position_size=1):
        self.trades = trades
        self.position_size = position_size  # Number of shares per trade or fixed capital

    def generate(self):
        df = pd.DataFrame(self.trades)
        df['pnl_percent'] = df['pnl'] * 100
        # Calculate cash profit per trade assuming position_size shares
        df['cash_profit'] = (df['exit_price'] - df['entry_price']) * self.position_size

        total_cash_profit = df['cash_profit'].sum()
        # Percent return relative to total invested capital (position_size * sum(entry prices))
        total_invested = df['entry_price'].sum() * self.position_size
        total_percent_return = (total_cash_profit / total_invested) * 100 if total_invested != 0 else 0

        print(df[['entry_date', 'exit_date', 'entry_price', 'exit_price', 'pnl_percent', 'cash_profit']])
        print(f"\nTotal Cash Profit: ${total_cash_profit:.2f}")
        print(f"Total Percent Return: {total_percent_return:.2f}%")
        return df
