from typing import Type, List

from src.entities.creatures.creature import Creature
from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinates import Coordinates
from src.map.map import Map


class Predator(Creature):

    def __init__(self, coord: Coordinates, age: int, weight: int):
        super().__init__(coord, age, weight)
        self._attack_power: int = int((self._age * self._weight) * 0.1)
        self._food: Type = Herbivore

    def migrate(self, way: List[Coordinates], map: Map) -> None:
        pass

    def attack(self, way: list, steps: int, map: Map) -> None:
        print('Атака!', self)

    def get_food(self) -> Type:
        return self._food
