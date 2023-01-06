from dataclasses import dataclass, field
from enum import Enum, auto
from typing import IO

from gatherer.model.type_aliases import Coordinate
from gatherer.utils import parse_coordinate, serialize_coordinate


class ActionType(Enum):
    NOTHING = auto()
    MOVE = auto()
    PICK = auto()
    DROP = auto()


@dataclass
class Action:
    action_type: ActionType

    def serialize(self) -> str:
        return str(self.action_type.value)


@dataclass
class MoveAction(Action):
    dest: Coordinate
    action_type: ActionType = field(default=ActionType.MOVE, init=False)

    def serialize(self) -> str:
        return super().serialize() + f"\n{serialize_coordinate(self.dest)}"


def parse_action(source: IO[str]) -> Action:
    action_type_line = source.readline()
    action_type = ActionType(int(action_type_line))
    if action_type == ActionType.MOVE:
        dest_line = source.readline()
        dest = parse_coordinate(dest_line)
        return MoveAction(dest)
    return Action(action_type)
