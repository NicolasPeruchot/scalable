"""Plot functions."""

import pandas as pd
import seaborn as sns


def plot_reviews(data: pd.DataFrame, feature: str, hue: str):
    """Plot with seaborn."""
    sns.displot(data, x=feature, hue=hue, stat="density", common_norm=False)
    return None
