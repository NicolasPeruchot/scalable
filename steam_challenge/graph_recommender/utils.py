"""Graph related functions."""

import networkx as nx
import pandas as pd

from steam_challenge.graph_recommender.config import Game, User


def create_graph_reviews(data: pd.DataFrame):
    """Create the graph for the 'reviews' dataset."""
    G = nx.Graph()
    edges = [
        (User(row.user_id), Game(row.item_id),)
        for row in data.itertuples(index=False)
        if row.recommend
    ]
    G.add_edges_from(edges)
    return G


def recommender_games(root_id: int, G: nx.classes.graph.Graph, items: pd.DataFrame, n: int = 5):
    """Return the recommended games."""
    games = []
    recommendations = []
    for user in G.neighbors(Game(item_id=root_id)):
        for game in G.neighbors(user):
            if game.item_id != root_id:
                games.append((Game(root_id), Game(game.item_id)))
    games_unique = set(games)
    distance = {}
    for x in games_unique:
        result = nx.adamic_adar_index(G, [x])
        for _, _, c in result:
            distance[x[1]] = c
    distance_sorted = sorted(distance.items(), key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while j < n:
        ID = distance_sorted[i][0].item_id
        name = items[items.id == ID].app_name.values
        if name:
            recommendations.append(name[0])
            j += 1
        i += 1
    return recommendations
