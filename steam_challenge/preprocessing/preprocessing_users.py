"""Preprocessing functions for users dataset."""
import pandas as pd


def users_preprocessing(data: pd.DataFrame):
    """Process the 'users' dataset."""
    data = data.drop_duplicates()
    data = data[data.playtime < 50000]
    data = data.reset_index(drop=True)
    return data
