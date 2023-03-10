from dataclasses import dataclass, field
from enum import Enum, auto

from gatherer.model.type_aliases import Coordinate


class ActionType(Enum):
    NOTHING = auto()
    MOVE = auto()
    PICK = auto()
    DROP = auto()


@dataclass
class Action:
    action_type: ActionType


@dataclass
class MoveAction(Action):
    dest: Coordinate
    action_type: ActionType = field(default=ActionType.MOVE, init=False)
