from typing import Type

from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass
from src.map.coordinates import Coordinates


class Herbivore(Creature):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self.__food: Type = Grass

    def eat(self, grass: Grass):
        pass

    def get_food(self) -> Type:
        return self.__food
