import os
import pandas as pd


def load_stock_from_file(base_dir: str, stock_name: str):
    df = pd.read_csv(os.path.join(base_dir, stock_name + '.mst'), 
                     parse_dates=[1], infer_datetime_format=True)
    df.columns = ['stock', 'date', 'open', 'high', 'low', 'close', 'vol']
    df['return'] = df['close'].pct_change().fillna(0)
    df = df.set_index('date').sort_index()

    return df