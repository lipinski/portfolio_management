import seaborn as sns


def plot_pct_change(df):
    ax = df.plot()
    ax.axhline(y=df.mean(), xmin=-1, xmax=1, color='r', linestyle='-', lw=1)
