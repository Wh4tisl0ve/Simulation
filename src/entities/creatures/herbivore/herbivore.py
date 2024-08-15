from typing import Type

from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass
from src.map.coordinates import Coordinates


class Herbivore(Creature):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self.__resource: Type = Grass

    def make_move(self):
        pass

    def eat(self, grass: Grass):
        pass
