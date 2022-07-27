from typing import Union
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier


GRID_RESOLUTION = 0.02
COLOR_MAP = plt.cm.binary


def plot_decision_boundary(
    data: pd.DataFrame,
    y: pd.Series,
    pair: list,
    ax,
    colormap=COLOR_MAP,
    resolution: float = GRID_RESOLUTION,
):
    X = data[pair]
    xx, yy = get_meshgrid(X, resolution)

    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    xlabel, ylabel = X.columns
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.contourf(xx, yy, Z, cmap=colormap)

    return ax


def get_meshgrid(X: Union[pd.DataFrame, np.array], resolution: float):
    x_min, x_max = get_bounds(X.iloc[0])
    y_min, y_max = get_bounds(X.iloc[1])
    grid_x = np.arange(x_min, x_max, resolution)
    grid_y = np.arange(y_min, y_max, resolution)
    xx, yy = np.meshgrid(grid_x, grid_y)
    return xx, yy


def get_bounds(series: pd.Series, offset: float = 2):
    series_min, series_max = series.min() - offset, series.max() + offset
    return series_min, series_max


def plot_training_points(
    data: pd.DataFrame,
    target_series: pd.Series,
    pair: list,
    n_classes: int,
    plot_colors: list,
    target_names: dict,
    ax,
    color_map=COLOR_MAP,
):
    plot_kwargs = dict(cmap=color_map, edgecolor="black", s=60)
    X = data[pair]
    x_series, y_series = X.iloc[:, 0], X.iloc[:, 1]

    for target_class, color in zip(range(n_classes), plot_colors):
        mask_target_class = target_series == target_class
        x = x_series[mask_target_class]
        y = y_series[mask_target_class]
        ax.scatter(x, y, c=color, label=target_names[target_class], **plot_kwargs)
    plt.suptitle("Decision surface of a decision tree using paired features")
    plt.legend(loc="lower right", borderpad=0, handletextpad=0)
    plt.axis("tight")
    return ax


def representation_woe(summary_tabl, data_missing):
    # Build the figure
    fig = plt.figure(figsize=(12, 8))
    grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)

    # construct the axes
    main_ax = fig.add_subplot(grid[1:, :])
    volume_ax = fig.add_subplot(grid[0, :], sharex=main_ax)

    # draw the graphs on the respective axis
    summary_tabl.plot(
        ax=volume_ax,
        kind="bar",
        y="perc",
        color="red",
        label="Size of each Bucket",
        alpha=0.5,
    )
    if len(data_missing) != 0:
        main_ax.axhline(
            data_missing["woe"][0],
            color="green",
            label="WoE of the observations with missing values",
        )

    summary_tabl.plot(
        ax=main_ax, kind="bar", y="woe", label="Weight of evidence", color="blue"
    )
    main_ax.legend()
    plt.show()

    return fig
