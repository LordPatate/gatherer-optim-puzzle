from dataclasses import dataclass
from typing import Set

from gatherer.model.moveable_objects import Hero, Item


@dataclass
class GameState:
    hero: Hero
    world: Set[Item]
