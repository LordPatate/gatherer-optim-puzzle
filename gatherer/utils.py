from math import sqrt

from gatherer.model.type_aliases import Coordinate


def dist(a: Coordinate, b: Coordinate):
    xa, ya = a
    xb, yb = b
    return sqrt((xb - xa)*(xb - xa) + (yb - ya)*(yb - ya))
