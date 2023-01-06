from math import sqrt

from gatherer.model.type_aliases import Coordinate


def dist(a: Coordinate, b: Coordinate):
    xa, ya = a
    xb, yb = b
    return sqrt((xb - xa)*(xb - xa) + (yb - ya)*(yb - ya))


def parse_coordinate(source: str) -> Coordinate:
    x, y = source.split()
    return float(x), float(y)


def serialize_coordinate(pos: Coordinate) -> str:
    x, y = pos
    return f"{x} {y}"
