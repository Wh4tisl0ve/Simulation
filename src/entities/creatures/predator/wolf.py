import random
from typing import List

from src.entities.creatures.predator.predator import Predator
from src.find_way import WayFinder
from src.map.coordinates import Coordinates
from src.map.map import Map


class Wolf(Predator):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self._age = random.randint(1, 6)
        self._weight = random.randint(60, 100)
        self._attack_power: int = int((self._age * self._weight) * 0.1)
        self.__cnt_cells_pass = 4

    def make_move(self, map: Map):
        finder = WayFinder(map, self.get_food())
        way = finder.finding_shortest_way(self.get_coord())

        if len(way) >= 1:
            self.migrate(way)

    def migrate(self, way: List[Coordinates]) -> None:
        steps = self.__cnt_cells_pass
        if steps > len(way):
            steps = len(way) - 1
        else:
            steps = self.__cnt_cells_pass - 1

        self.set_coord(way[steps])
