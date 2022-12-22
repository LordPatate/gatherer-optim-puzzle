from random import randint

from gatherer import const as const
from gatherer.model.moveable_objects import Item


def generate(n):
    world = set()
    for i in range(n):
        x = randint(0, const.WINDOW_W - const.ITEM_W)
        y = randint(0, const.WINDOW_H - const.ITEM_H)
        world.add(Item((x, y)))

    return world
