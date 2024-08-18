from abc import ABC, abstractmethod

from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass
from src.map.coordinates import Coordinates
from typing import List
from typing import Type
import random


class Herbivore(Creature, ABC):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self.__food: Type = Grass

    @abstractmethod
    def migrate(self, way: List[Coordinates]):
        pass

    @abstractmethod
    def eat(self):
        pass

    def get_food(self) -> Type:
        return self.__food
