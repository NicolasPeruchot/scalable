"""Config file for graphs, with different kind of nodes."""

from collections import namedtuple


User = namedtuple("User", "user_id")
Game = namedtuple("Game", "item_id")
Developer = namedtuple("Dev", "developer")
Genre = namedtuple("Genre", "genres")
Spec = namedtuple("Spec", "specs")
Tag = namedtuple("Tag", "tags")
