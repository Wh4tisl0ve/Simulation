import random
from typing import List

from src.entities.creatures.predator.predator import Predator
from src.find_way import WayFinder
from src.map.coordinates import Coordinates
from src.map.map import Map


class Wolf(Predator):
    def __init__(self, coord: Coordinates):
        super().__init__(coord, random.randint(1, 6), random.randint(60, 100))
        self.__cnt_cells_pass: int = 4
        self.__attack_range: int = 2

    def make_move(self, map: Map) -> None:
        finder = WayFinder(map, self.get_food())
        way = finder.finding_shortest_way(self.get_coord())

        if len(way) >= 1:
            self.migrate(way[1:], map)

    def migrate(self, way: List[Coordinates], map: Map) -> None:
        steps = self.__cnt_cells_pass
        if steps > len(way):
            steps = len(way) - 1
        else:
            steps = self.__cnt_cells_pass - 1

        print(way)

        if self.is_attack_possible(way, steps):
            self.attack(way, steps, map)
        else:
            self.set_coord(way[steps])

    def attack(self, way: list, steps: int, map: Map) -> None:
        herbivore_attacked = map.get_entity(way[-1])
        print('АТАКА', self)
        print('Атакуемый:', herbivore_attacked)

    def is_attack_possible(self, way: list, steps: int) -> bool:
        food_coord_index = len(way) - 1

        if abs(steps - food_coord_index) <= self.__attack_range:
            return True

        return False

    def __repr__(self):
        return f'Волк с координатами {self.get_coord()}'
