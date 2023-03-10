from dataclasses import dataclass, field
from typing import Set
from uuid import UUID

import gatherer.const as const
from gatherer.model.type_aliases import Coordinate
from gatherer.utils import dist


@dataclass(eq=False)
class Item:
    uuid: UUID
    pos: Coordinate

    def toward(self, dest: Coordinate):
        d = dist(self.pos, dest)
        if d < const.STEP_LENGTH:
            self.pos = dest
            return

        xd, yd = dest
        xp, yp = self.pos
        ratio = const.STEP_LENGTH / d
        x = (xd - xp) * ratio
        y = (yd - yp) * ratio
        self.pos = xp + x, yp + y

    def __hash__(self):
        return self.uuid.int


@dataclass(eq=False)
class Hero(Item):
    bag: Set[Item]

    def pick(self, world):
        for item in world:
            if dist(self.pos, item.pos) <= const.LEASH_LENGTH \
                    and item not in self.bag \
                    and len(self.bag) < const.BAG_LIMIT:
                self.bag.add(item)


@dataclass(eq=False)
class PartiallyInitializedHero(Item):
    bag: Set[str]
