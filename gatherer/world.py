from random import randint
from typing import Set
from uuid import uuid4

from gatherer import const as const
from gatherer.model.moveable_objects import Item
from gatherer.model.type_aliases import Coordinate


def generate_item_at(pos: Coordinate) -> Item:
    uuid = uuid4()
    return Item(uuid, pos)


def generate(n: int) -> Set[Item]:
    world = set()
    for _ in range(n):
        x = randint(0, const.WINDOW_W - const.ITEM_W)
        y = randint(0, const.WINDOW_H - const.ITEM_H)
        item = generate_item_at((x, y))
        world.add(item)

    return world
