from random import randint

import const
from utils import dist

class Item:
    def __init__(self, pos):
        self.pos = pos
        
    def toward(self, dest):
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
        
    def generate(n):
        world = set()
        for i in range(n):
            
            x = randint(0, const.WINDOW_W - const.ITEM_W)
            y = randint(0, const.WINDOW_H - const.ITEM_H)
            world.add(Item((x, y)))
        
        return world
        

class Hero(Item):
    def __init__(self, pos):
        self.pos = pos
        self.bag = set()
        
    def pick(self, world):
        for item in world:
            if dist(self.pos, item.pos) <= const.LEASH_LENGTH \
            and item not in self.bag \
            and len(self.bag) < const.BAG_LIMIT:
                self.bag.add(item)
