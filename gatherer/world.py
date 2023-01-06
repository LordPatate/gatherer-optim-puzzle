from random import randint
from typing import Set

from gatherer import const as const
from gatherer.model.moveable_objects import Item


def generate(n: int) -> Set[Item]:
    world = set()
    for i in range(n):
        x = randint(0, const.WINDOW_W - const.ITEM_W)
        y = randint(0, const.WINDOW_H - const.ITEM_H)
        world.add(Item((x, y)))

    return world


def serialize_game_state(hero, world) -> str:
    serialized_items = (
        item.serialize()
        for item in world
    )
    return "\n".join(
        (hero.serialize(), *serialized_items)
    )
