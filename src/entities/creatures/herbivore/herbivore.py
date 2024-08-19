from abc import ABC, abstractmethod

from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass
from src.map.coordinates import Coordinates
from typing import List
from typing import Type
import random


class Herbivore(Creature, ABC):
    def __init__(self, coord: Coordinates, age: int, weight: int):
        super().__init__(coord, age, weight)
        self._health_point: int = int((self._age * self._weight) / 10)
        self._food: Type = Grass

    @abstractmethod
    def migrate(self, way: List[Coordinates]):
        pass

    def get_food(self) -> Type:
        return self._food
