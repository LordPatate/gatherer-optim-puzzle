from functools import singledispatch
from typing import IO

from gatherer.model.actions import Action, ActionType, MoveAction
from gatherer.model.moveable_objects import Hero, Item
from gatherer.model.type_aliases import Coordinate
from gatherer.game_state import GameState


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
    return f"{serialize_action(action)}\n{serialize(action.dest)}"


def parse_coordinate(source: str) -> Coordinate:
    x, y = source.split()
    return float(x), float(y)


def parse_action(source: IO[str]) -> Action:
    action_type_line = source.readline()
    action_type = ActionType(int(action_type_line))
    if action_type == ActionType.MOVE:
        dest_line = source.readline()
        dest = parse_coordinate(dest_line)
        return MoveAction(dest)
    return Action(action_type)