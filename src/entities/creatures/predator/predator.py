from typing import Type

from src.entities.creatures.creature import Creature
from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinates import Coordinates


class Predator(Creature):

    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self.__food: Type = Herbivore
        self.__attack_power = None

    def make_move(self):
        bfs(self.__food)
        pass

    def attack(self, herbivore: Herbivore):
        # herbivore.set_HP(herbivore.get_HP() - self.__attack_power)
        pass
