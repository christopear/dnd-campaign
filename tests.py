from enum import Enum


class Poop:
    def __init__(self, id, level):
        self.level = level
        self.id = id


class ID(Enum):
    poop = 1
    poopy = 2


z = [Poop(ID.poop, 4), Poop(ID.poop, 2), Poop(ID.poop, 3), Poop(ID.poop, 6), Poop(ID.poopy, 1), Poop(ID.poopy, 2)]


