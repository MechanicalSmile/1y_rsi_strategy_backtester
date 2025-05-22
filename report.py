import pandas as pd

class ReportGenerator:
    def __init__(self, trades, position_size=1):
        """
        Initialize the report generator.
        
        Parameters:
        - trades: list or iterable of trade dictionaries containing trade details (entry/exit price, pnl, dates, etc.)
        - position_size: number of shares/contracts per trade or fixed capital amount used per trade (default is 1)
        """
        self.trades = trades
        self.position_size = position_size  # Allows scaling profit calculations by trade size

    def generate(self):
        """
        Process the trades data and print a summary report including:
        - Each trade's profit/loss in percent and cash terms
        - Total cumulative profit/loss
        - Total percent return relative to capital invested
        
        Returns:
        - A pandas DataFrame with detailed trade results and computed metrics.
        """
        # Convert list of trade dictionaries into a pandas DataFrame for easier analysis
        df = pd.DataFrame(self.trades)

        # Calculate percentage profit/loss per trade and convert to percentage (e.g., 0.05 -> 5%)
        df['pnl_percent'] = df['pnl'] * 100

        # Calculate cash profit per trade based on the difference between exit and entry price,
        # scaled by position size (number of shares/contracts)
        df['cash_profit'] = (df['exit_price'] - df['entry_price']) * self.position_size

        # Sum of all cash profits/losses across all trades
        total_cash_profit = df['cash_profit'].sum()

        # Total capital invested is the sum of entry prices times position size,
        # which approximates the total money allocated across all trades
        total_invested = df['entry_price'].sum() * self.position_size

        # Calculate total percent return: total profit relative to total invested capital,
        # expressed as a percentage. Guard against division by zero.
        total_percent_return = (total_cash_profit / total_invested) * 100 if total_invested != 0 else 0

        # Display a subset of the DataFrame with relevant trade information
        print(df[['entry_date', 'exit_date', 'entry_price', 'exit_price', 'pnl_percent', 'cash_profit']])

        # Display aggregate performance statistics
        print(f"\nTotal Cash Profit: ${total_cash_profit:.2f}")
        print(f"Total Percent Return: {total_percent_return:.2f}%")

        # Return the DataFrame for further use if needed (e.g., exporting, visualization)
        return df
