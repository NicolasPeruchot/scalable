"""Plot functions."""

import pandas as pd
import seaborn as sns


def plot_sns(data: pd.DataFrame, feature: str, hue: str):
    """Plot with seaborn."""
    sns.displot(data, x=feature, hue=hue, stat="density", common_norm=False)
    return None


def get_dup(data: pd.DataFrame):
    """Frequence od duplicated rows."""
    dup = round(data.duplicated().sum() / len(data), 2)
    return f"Frequence of duplicated rows: \n{dup}"


def get_missing(data: pd.DataFrame):
    """Frequence of missing values."""
    mis = data.isna().sum() / len(data)
    return f"Frequence of missing values in each columns:\n {mis}"
