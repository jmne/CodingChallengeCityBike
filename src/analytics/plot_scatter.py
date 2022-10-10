#  Copyright (c) 2022 by jmne.
#  File: plot_scatter.py

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, LogNorm

# "Viridis-like" colormap with white background
white_viridis = LinearSegmentedColormap.from_list('white_viridis', [
    (0, '#ffffff'),
    (1e-60, '#0a000d'),
    (0.1, '#440053'),
    (0.2, '#404388'),
    (0.4, '#2a788e'),
    (0.6, '#21a784'),
    (0.8, '#78d151'),
    (1, '#fde624'),
], N=256)


# plot hierarchical cluster (+density)
def plot_with_density(df):
    """
    Plots a 2D dataframe with a density map.

    Args:
        df: write your description
    """
    # create figure and axis objects with subplots()
    fig, axs = plt.subplots(round(len(df.columns) / 2), 2)
    fig.suptitle('Scatter of Variables (With density)', fontsize=20)
    a = 0
    b = 0
    fig.set_size_inches(10, 10)
    h = None

    # iterate over columns and create scatter plots
    for column in df.columns:
        x = df[column]
        y = df["usertype"]
        if df[column].nunique() > 20:
            h = axs[a, b].hist2d(x, y, (150, 25), cmap=white_viridis, norm=LogNorm())
        else:
            h = axs[a, b].hist2d(x, y, (20, 25), cmap=white_viridis, norm=LogNorm())
        axs[a, b].set_xlabel(column)
        axs[a, b].set_ylabel('usertype')

        # select the right subplot
        if b == 0:
            b = 1
        else:
            a += 1
            b = 0

    fig.colorbar(h[3], ax=axs)
    plt.show()


# plot hierarchical cluster
def plot(df):
    """
    Plots the dataframe df.

    Args:
        df: write your description
    """
    # create figure and axis objects with subplots()
    fig, axs = plt.subplots(round(len(df.columns) / 2), 2)
    fig.suptitle('Scatter of Variables', fontsize=20)
    a = 0
    b = 0
    fig.set_size_inches(10, 10)

    # iterate over columns and create scatter plots
    for column in df.columns:
        x = df[column]
        y = df["usertype"]
        axs[a, b].scatter(x, y)
        axs[a, b].set_xlabel(column)
        axs[a, b].set_ylabel('usertype')

        # select the right subplot
        if b == 0:
            b = 1
        else:
            a += 1
            b = 0

    plt.show()
