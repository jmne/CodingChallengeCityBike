#  Copyright (c) 2022 by jmne.
#  File: plot_histogram.py
from matplotlib import pyplot as plt


# plot histogram
def plot(df):
    """
    Plots histogram of a DataFrame.

    Args:
        df: write your description
    """
    plt.rcParams["figure.figsize"] = (10, 10)
    hm = df.hist()
    plt.show()
