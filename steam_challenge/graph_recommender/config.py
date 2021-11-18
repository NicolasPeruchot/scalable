"""Config file for graphs."""

from collections import namedtuple


User = namedtuple("User", "user_id")
Game = namedtuple("Game", "item_id")
Developer = namedtuple("Dev", "developer")
Genre = namedtuple("Genre", "genres")
Spec = namedtuple("Spec", "specs")
Tag = namedtuple("Tag", "tags")
