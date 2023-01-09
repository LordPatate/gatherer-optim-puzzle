from functools import singledispatch
from uuid import UUID

from gatherer.game_state import GameState
from gatherer.model.actions import Action, ActionType, MoveAction
from gatherer.model.moveable_objects import Hero, Item
from gatherer.model.type_aliases import Coordinate

SEP = ':'


@singledispatch
def serialize(arg) -> str:
    return str(arg)


@serialize.register(tuple)
def serialize_coordinate(pos: Coordinate) -> str:
    x, y = pos
    return f"{x} {y}"


def parse_coordinate(source: str) -> Coordinate:
    x, y = source.split()
    return float(x), float(y)


@serialize.register
def serialize_item(item: Item) -> str:
    return f"{item.uuid.hex}{SEP}{serialize_coordinate(item.pos)}"


def parse_item(source: str) -> Item:
    uuid_hex, pos_source = source.split(sep=SEP)
    return Item(UUID(uuid_hex), parse_coordinate(pos_source))


def parse_hero(source: str) -> Hero:
    uuid_hex, pos_source = source.split(sep=SEP)
    return Hero(UUID(uuid_hex), parse_coordinate(pos_source))


@serialize.register
def serialize_game_state(game_state: GameState) -> str:
    serialized_items = (
        serialize(item)
        for item in game_state.world
    )
    return "\n".join(
        (serialize(game_state.hero), *serialized_items)
    )


@serialize.register
def serialize_action(action: Action) -> str:
    return str(action.action_type.value)


@serialize.register
def serialize_move_action(action: MoveAction) -> str:
    return f"{serialize_action(action)}{SEP}{serialize(action.dest)}"


def parse_action(source: str) -> Action:
    split_source = source.split(sep=SEP)
    action_type = ActionType(int(split_source[0]))
    if action_type == ActionType.MOVE:
        dest = parse_coordinate(split_source[1])
        return MoveAction(dest)
    return Action(action_type)
