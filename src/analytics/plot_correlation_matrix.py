#  Copyright (c) 2022 by jmne.
#  File: plot_correlation_matrix.py

import matplotlib.pyplot as plt
import seaborn as sn


def plot(df):
    """
    Plot correlation matrix.

    Args:
        df: dataframe of data
    """
    # print correlation matrix
    corr_matrix = df.corr().round(3)

    # plot correlation matrix
    hm = sn.heatmap(corr_matrix, annot=True, cmap='coolwarm', cbar=False, linewidths=0.5, annot_kws={"size": 12})
    hm.figure.set_size_inches(12, 12)
    hm.set_title(label='Correlation Matrix', fontsize=18)
    plt.show()
