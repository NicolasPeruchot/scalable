"""Plot functions."""

import pandas as pd
import seaborn as sns


def plot_helpful_reviews(data: pd.DataFrame):
    """Plot recommended games for 'helpful' feature."""
    reviews_plot = data.dropna()
    reviews_plot["helpful"] = reviews_plot["helpful"].astype(int)
    sns.displot(reviews_plot, x="helpful", hue="recommend", stat="density", common_norm=False)
    return None


def plot_funny_reviews(data: pd.DataFrame):
    """Plot recommended games for 'funny' feature."""
    sns.displot(data, x="funny", hue="recommend", stat="density", common_norm=False)
    return None
