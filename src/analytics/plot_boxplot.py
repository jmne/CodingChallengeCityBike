#  Copyright (c) 2022 by jmne.
#  File: plot_boxplot.py
from matplotlib import pyplot as plt


# plot boxplot
def plot(df):
    """
    Plots a DataFrame.

    Args:
        df: dataframe of data
    """
    # create figure and axis objects with subplots()
    fig, axs = plt.subplots(round(len(df.columns) / 2), 2)
    fig.suptitle('Boxplot of Variables', fontsize=20)
    a = 0
    b = 0
    fig.set_size_inches(10, 10)

    # iterate over columns and create scatter plots
    for column in df.columns:
        x = df[column]
        y = df["usertype"]
        axs[a, b].boxplot(x)
        axs[a, b].set_xlabel(column)
        axs[a, b].set_ylabel('usertype')

        # select the right subplot
        if b == 0:
            b = 1
        else:
            a += 1
            b = 0

    plt.show()
