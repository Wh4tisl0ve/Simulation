import random
from typing import List

from src.entities.creatures.predator.predator import Predator
from src.find_way import WayFinder
from src.map.coordinates import Coordinates
from src.map.map import Map


class Wolf(Predator):
    def __init__(self, coord: Coordinates):
        super().__init__(coord=coord,
                         age=random.randint(1, 6),
                         weight=random.randint(60, 100),
                         attack_range=1,
                         cnt_cells_pass=4)

    def make_move(self, map: Map) -> None:
        finder = WayFinder(map, self.get_food())
        way = finder.finding_shortest_way(self.get_coord())

        if len(way) >= 1:
            self.migrate(way[1:], map)

    def __repr__(self):
        return f'Волк с координатами {self.get_coord()} и силой: {self._attack_power}'
