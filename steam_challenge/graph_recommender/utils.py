"""Graph related functions."""
import ast

from typing import List, Tuple

import networkx as nx
import pandas as pd

from steam_challenge.graph_recommender.config import Developer, Game, Genre, Spec, Tag, User


def create_graph(reviews: pd.DataFrame, items: pd.DataFrame):
    """Create the graph."""
    G = nx.Graph()
    reviews = reviews[reviews.recommend == True]
    edges = []
    for feature in ["tags", "specs", "genres"]:
        items[feature] = items[feature].fillna("['None']")
    for row in items.itertuples(index=False):
        tags = ast.literal_eval(row.tags)
        genres = ast.literal_eval(row.genres)
        specs = ast.literal_eval(row.specs)
        for tag in tags:
            edges.append(
                (
                    Game(row.item_id),
                    Tag(tag),
                )
            )
        for spec in specs:
            edges.append(
                (
                    Game(row.item_id),
                    Spec(spec),
                )
            )
        for genre in genres:
            edges.append(
                (
                    Game(row.item_id),
                    Genre(genre),
                )
            )
        edges.append(
            (
                Game(row.item_id),
                Developer(row.developer),
            )
        )
    for row in reviews.itertuples(index=False):

        edges.append(
            (
                Game(row.item_id),
                User(row.user_id),
            ),
        )

    G.add_edges_from(edges)
    return G


def sorted_nodes(games: List[Tuple], data: pd.DataFrame, G: nx.classes.graph.Graph, n: int = 5):
    """Returns sorted nodes, from a list of tuples"""
    games_unique = set(games)
    recommendations = []
    distance = {}
    for x in games_unique:
        result = nx.adamic_adar_index(G, [x])
        for _, _, c in result:
            distance[x[1]] = c
    distance_sorted = sorted(distance.items(), key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while j < n:
        print
        ID = distance_sorted[i][0].item_id
        name = data[data.item_id == ID].item_id.values
        if name:
            recommendations.append((name[0], distance_sorted[i][1]))
            j += 1
        i += 1
    return recommendations


def recommender_users(root_user: str, G: nx.classes.graph.Graph, data: pd.DataFrame, n: int = 5):
    """Return the recommended games for a user, and the games this user owns."""
    owned_games = []
    recommendations = []
    recommended_games = []
    for game in G.neighbors(User(user_id=root_user)):
        owned_games.append(game.item_id)

    for game in owned_games:
        recommended_games += [x for x in recommender_games(root_app=game, G=G, n=200, data=data)]
    recommended_games = sorted(recommended_games, key=lambda tup: tup[1])
    i = 0
    while i < n:
        if recommended_games[i][0] not in recommendations:
            recommendations.append(recommended_games[i][0])
            i += 1

    return (recommendations, owned_games)


def recommender_games(root_app: int, G: nx.classes.graph.Graph, data: pd.DataFrame, n: int = 5):
    """Recommender for similar games."""
    games = []
    recommendations = []
    for node in G.neighbors(Game(item_id=root_app)):
        for game in G.neighbors(node):
            if game.item_id != root_app:
                games.append((Game(root_app), Game(game.item_id)))
    recommendations = sorted_nodes(games=games, data=data, G=G, n=n)
    return recommendations
