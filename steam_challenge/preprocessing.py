"""Preprocessing functions."""
import pandas as pd


def sentiment_process(x: str):
    """Tweak the 'sentiment' feature."""
    if x is None:
        return 0
    elif "Negative" in x:
        return -1
    elif "Positive" in x:
        return 1
    else:
        return 0


def helpful_processing(x: str):
    """Tweak the 'helpful' feature."""
    begin = x.find("(")
    end = x.find("%")
    if begin > -1:
        return x[begin + 1 : end]
    else:
        return None


def funny_processing(x: str):
    """Tweak the 'funny' feature."""
    end = x.find("p")
    if end > -1:
        return 1
    else:
        return 0


def review_processing(data: pd.DataFrame):
    """Process the 'reviews' dataset."""
    data = data.drop(columns=["review", "posted", "last_edited"])
    data.helpful = data.helpful.apply(helpful_processing)
    data.funny = data.funny.apply(funny_processing)
    data = data.drop_duplicates()
    return data


def items_processing(data: pd.DataFrame):
    """Process the 'items' dataset."""
    data = data.drop(columns=["url", "reviews_url", "title", "discount_price", "metascore"])
    data = data.drop_duplicates(subset="id")
    data = data.dropna(subset=["id", "app_name"])
    data.sentiment = data.sentiment.apply(sentiment_process)
    return data


def users_processing(data: pd.DataFrame):
    """Process the 'users' dataset."""
    data = data.drop_duplicates()
    return data


def get_dup(data: pd.DataFrame):
    """Frequence od duplicated rows."""
    dup = round(data.duplicated().sum() / len(data), 2)
    return f"Frequence of duplicated rows: \n{dup}"


def get_missing(data: pd.DataFrame):
    """Frequence of missing values."""
    mis = data.isna().sum() / len(data)
    return f"Frequence of missing values in each columns:\n {mis}"
