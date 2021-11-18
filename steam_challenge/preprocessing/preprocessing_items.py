"""Preprocessing functions for items dataset."""

import re

from datetime import datetime

import pandas as pd


def sentiment_preprocess(x: str):
    """Tweak the 'sentiment' feature."""
    if x is None:
        return 0
    elif "Negative" in x:
        return -1
    elif "Positive" in x:
        return 1
    else:
        return 0


def find_price(x: str):
    """Tweak the 'price' feature."""
    regex = r"[\d]+(\.)?[\d]+"
    if x is None:
        return 0.0
    else:
        matches = re.finditer(regex, x, re.MULTILINE)
        for _, match in enumerate(matches, start=1):
            if type(x[match.start() : match.end()]) == str:
                return float(x[match.start() : match.end()])
            else:
                return 0.0
    return 0.0


def to_date(x: str):
    """Convert string to date."""
    try:
        return datetime.strptime(x, "%Y-%m-%d")
    except TypeError:
        return None
    except ValueError:
        return None


def items_preprocessing(data: pd.DataFrame):
    """Process the 'items' dataset by applying all the transformations."""
    data = data.drop(
        columns=["url", "reviews_url", "title", "discount_price", "metascore", "publisher"]
    )
    data = data.drop_duplicates(subset="id")
    data = data.dropna(subset=["id", "app_name"])
    data.id = data.id.astype(int)
    data = data.rename(columns={"id": "item_id"})
    data = data.reset_index(drop=True)

    data.sentiment = data.sentiment.apply(sentiment_preprocess)
    data.price = data.price.apply(find_price)
    data.release_date = data.release_date.apply(to_date)

    items_sorted_date = data.sort_values("release_date").dropna()
    median_date = items_sorted_date.release_date.iloc[round(len(items_sorted_date) / 2)]
    data.release_date = data.release_date.fillna(median_date)
    data.developer = data.developer.fillna("Unknown")
    data.early_access = data.early_access.astype(int)
    return data
