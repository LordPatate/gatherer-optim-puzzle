from gatherer.model.actions import Action, ActionType, MoveAction
from gatherer.model.type_aliases import Coordinate
from gatherer.utils import dist
import gatherer.const as const

HOME_POS: Coordinate = (
    (const.WINDOW_W - const.HERO_W) / 2,
    (const.WINDOW_H - const.HERO_H) / 2,
)


def update(hero, world) -> Action:
    """
    Returns the next action to take
    """
    if len(hero.bag) > const.BAG_LIMIT - 1 or remaining(hero, world) == 0:
        if hero.pos == HOME_POS:
            return Action(ActionType.DROP)

        return MoveAction(HOME_POS)

    item = nearest(hero, world)
    if dist(hero.pos, item.pos) <= const.LEASH_LENGTH:
        return Action(ActionType.PICK)

    return MoveAction(item.pos)


def nearest(hero, world):
    """
    Returns the nearest item that is not in the bag or at HOME_POS
    """
    target, d = None, float('inf')

    for item in world:
        if dist(item.pos, HOME_POS) < const.LEASH_LENGTH + const.ITEM_W \
                or item in hero.bag:
            continue

        item_dist = dist(item.pos, hero.pos)
        if item_dist < d:
            target, d = item, item_dist

    return target


def remaining(hero, world):
    """
    Counts the number of item not in the bag or at HOME_POS
    """
    count = 0

    for item in world:
        if dist(item.pos, HOME_POS) > const.LEASH_LENGTH + const.ITEM_W \
                and item not in hero.bag:
            count += 1

    return count