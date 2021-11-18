"""Features engineerings functions."""
import ast

from typing import Dict, List

import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler


def transform_feature(data: pd.DataFrame, feature: str):
    """Feature engineering for the items dataset, creating columns for categorical features."""
    all_types = set()
    for i in range(len(data)):
        if data.iloc[i][feature] is not None:
            type = ast.literal_eval(data.iloc[i][feature])
            for x in type:
                all_types.add(x)
    list_types: Dict[str, List[int]] = {x: [] for x in all_types}
    for i in range(len(data)):
        sentence = data.iloc[i][feature]
        for type in all_types:
            if sentence is None:
                list_types[type].append(0)
            else:
                if type in sentence:
                    list_types[type].append(1)

                else:
                    list_types[type].append(0)
    for type in list_types.keys():
        data = pd.concat([data, pd.Series(list_types[type], name=type, index=data.index)], axis=1,)
    data = data.drop(columns=[feature])
    return data


def dataset_creation(reviews: pd.DataFrame, users: pd.DataFrame, items: pd.DataFrame):
    """Create the dataset."""
    time_per_user = (
        users.drop(columns=["item_id"])
        .groupby("user_id")
        .sum()
        .rename(columns={"playtime": "Total playtime on Steam for this user"})
        .reset_index()
    )
    time_per_game = (
        users.groupby("item_id")
        .sum()
        .rename(columns={"playtime": "Total playtime for this game among all users"})
        .reset_index()
    )
    dataset = pd.merge(reviews, users)
    dataset = pd.merge(items, pd.merge(pd.merge(dataset, time_per_user), time_per_game))
    dataset = pd.merge(items, dataset)
    dataset["ind"] = "Game: " + dataset["app_name"] + ", User: " + dataset["user_id"]
    dataset = dataset.set_index("ind")
    dataset = dataset.drop(columns=["item_id"])
    return dataset


def features_creation(data: pd.DataFrame):
    """Feature engineering for second supervised model."""
    for feature in ["genres", "specs", "tags"]:
        data = transform_feature(data=data, feature=feature)
    le = LabelEncoder()
    data.developer = le.fit_transform(data.developer)
    data.release_date = data.release_date.view(int)
    sd = StandardScaler()
    data_scaled = pd.DataFrame(sd.fit_transform(data), columns=data.columns, index=data.index)
    pca = PCA(n_components=0.95)
    data_pca = pd.DataFrame(pca.fit_transform(data_scaled), index=data_scaled.index)
    return data_pca
