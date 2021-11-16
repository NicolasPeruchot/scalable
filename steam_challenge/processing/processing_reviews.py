"""Preprocessing functions for reviews dataset."""

import pandas as pd


def helpful_processing(x: str):
    """Tweak the 'helpful' feature."""
    begin = x.find("(")
    end = x.find("%")
    if begin > -1:
        return x[begin + 1 : end]
    else:
        return 0


def funny_processing(x: str):
    """Tweak the 'funny' feature."""
    end = x.find("p")
    if end > -1:
        return 1
    else:
        return 0


def reviews_processing(data: pd.DataFrame):
    """Process the 'reviews' dataset."""
    data = data.drop(columns=["review", "posted", "last_edited"])
    data.helpful = data.helpful.apply(helpful_processing)
    data.funny = data.funny.apply(funny_processing)
    data = data.drop_duplicates()
    data = data.reset_index(drop=True)
    return data
