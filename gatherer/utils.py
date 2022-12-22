from math import sqrt


def dist(a, b):
    xa, ya = a
    xb, yb = b
    return sqrt((xb - xa)*(xb - xa) + (yb - ya)*(yb - ya))
