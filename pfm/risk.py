import pandas as pd
import numpy as np


def volatility(df: pd.Series, periods: int = 0):
    std = df.std()

    if periods:
        std *= np.sqrt(periods)

    return df.std()


def return_on_risk_ratio(return_value, risk):
    return return_value / risk


def sharpe_ratio(return_value: float, free_risk_rate: float, volatility: float):
    return (return_value - free_risk_rate) / volatility


def wealth_index(return_series: pd.Series, money: int = 1):
    return money * (1 + return_series).cumprod()


def monthly_return(return_series: pd.Series):
    series = return_series.asfreq('BM').pct_change()
    series.index = series.index.to_period('M')
    series = series.dropna()

    return series


def drawdowns(return_series: pd.Series, money: int = 1):
    wealth = wealth_index(return_series, money)
    previous_peak = wealth.cummax()
    drawdowns = (wealth - previous_peak) / previous_peak

    return pd.DataFrame({
        'wealth': wealth,
        'previous_peak': previous_peak,
        'drawdowns': drawdowns
    })
