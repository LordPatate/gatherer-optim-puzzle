from functools import singledispatch

from gatherer.game_state import GameState
from gatherer.model.actions import Action, ActionType, MoveAction
from gatherer.model.moveable_objects import Item
from gatherer.model.type_aliases import Coordinate

MOVE_ACTION_SEP = ':'


@singledispatch
def serialize(arg) -> str:
    return str(arg)


@serialize.register(tuple)
def serialize_coordinate(pos: Coordinate) -> str:
    x, y = pos
    return f"{x} {y}"


@serialize.register
def serialize_item(item: Item) -> str:
    return serialize_coordinate(item.pos)


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
    return f"{serialize_action(action)}{MOVE_ACTION_SEP}{serialize(action.dest)}"


def parse_coordinate(source: str) -> Coordinate:
    x, y = source.split()
    return float(x), float(y)


def parse_action(source: str) -> Action:
    split_source = source.split(sep=MOVE_ACTION_SEP)
    action_type = ActionType(int(split_source[0]))
    if action_type == ActionType.MOVE:
        dest = parse_coordinate(split_source[1])
        return MoveAction(dest)
    return Action(action_type)
