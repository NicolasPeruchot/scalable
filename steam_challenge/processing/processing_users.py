"""Preprocessing functions for users dataset."""
import pandas as pd


def users_processing(data: pd.DataFrame):
    """Process the 'users' dataset."""
    data = data.drop_duplicates()
    data = data.reset_index(drop=True)
    data = data[data.playtime < 50000]
    return data
