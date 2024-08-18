from typing import Type, List

from src.entities.creatures.creature import Creature
from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinates import Coordinates


class Predator(Creature):

    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self._food: Type = Herbivore

    def migrate(self, way: List[Coordinates]) -> None:
        pass

    def attack(self) -> None:
        pass

    def get_food(self) -> Type:
        return self._food
