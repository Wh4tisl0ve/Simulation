from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass
from src.map.coordinates import Coordinates
from typing import List
from typing import Type
import random


class Herbivore(Creature):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self._age = random.randint(5, 20)
        self._weight = random.randint(75, 200)
        self._health_point: int = int((self._age * self._weight) / 10)
        self.__food: Type = Grass

    def migrate(self, way: List[Coordinates]):
        pass

    def eat(self):
        pass

    def get_food(self) -> Type:
        return self.__food
