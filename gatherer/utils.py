from math import sqrt

from gatherer.model import Coordinate


def dist(a: Coordinate, b: Coordinate):
    xa, ya = a
    xb, yb = b
    return sqrt((xb - xa)*(xb - xa) + (yb - ya)*(yb - ya))
