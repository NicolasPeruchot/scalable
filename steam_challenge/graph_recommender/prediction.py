"""Graph results."""
import networkx as nx
import pandas as pd

from steam_challenge.graph_recommender.utils import recommender_games, recommender_users


def plot_result_games(
    G: nx.classes.graph.Graph, data: pd.DataFrame, item_id: int = 48190, top: int = 5
):
    """Show result for game based recommendation."""
    root_game = data[data.item_id == item_id].app_name.values[0]
    print(f"{top} recommendation(s) for: {root_game}:")
    print("\n")
    for x in recommender_games(root_app=item_id, G=G, n=top, data=data):
        print(data[data.item_id == x[0]].app_name.values[0])
    return None


def plot_result_users(
    G: nx.classes.graph.Graph, data: pd.DataFrame, root_user: int = "Beave-", top: int = 5
):
    """Show result for user based recommendation."""
    recommendation, owned_games = recommender_users(root_user=root_user, G=G, n=top, data=data)
    for x in owned_games:
        print("Owned: " + data[data.item_id == x].app_name.values[0])
    print("Recommendations:")
    for x in recommendation:
        print(data[data.item_id == x].app_name.values[0])
    return None
