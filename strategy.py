import pandas as pd

class RSIStrategy:
    def __init__(self, rsi_threshold, profit_target, stop_loss):
        self.rsi_threshold = rsi_threshold
        self.profit_target = profit_target
        self.stop_loss = stop_loss

    def generate_signals(self, data: pd.DataFrame):
        data = data.copy()
        data['Signal'] = 0  # 1 = buy, -1 = sell, 0 = hold
        in_position = False
        entry_price = 0.0

        for i in range(1, len(data)):
            if not in_position and data['RSI'].iloc[i] < self.rsi_threshold:
                data.at[data.index[i], 'Signal'] = 1
                entry_price = float(data['Close'].iloc[i].item())
                in_position = True
            elif in_position:
                current_price = float(data['Close'].iloc[i].item())
                change = (current_price - entry_price) / entry_price

                if change >= self.profit_target or change <= -self.stop_loss:
                    data.at[data.index[i], 'Signal'] = -1
                    in_position = False

        return data
