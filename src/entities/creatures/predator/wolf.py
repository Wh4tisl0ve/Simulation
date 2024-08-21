from src.entities.creatures.predator.predator import Predator
from src.find_way import WayFinder
from src.map.coordinates import Coordinates
from src.map.map import Map
import random


class Wolf(Predator):
    def __init__(self, coord: Coordinates):
        super().__init__(coord=coord,
                         age=random.randint(1, 6),
                         weight=random.randint(60, 100),
                         attack_range=2,
                         cnt_cells_pass=4)

    def make_move(self, map: Map) -> None:
        finder = WayFinder(map, self.get_food())
        way = finder.finding_shortest_way(self.get_coord())

        if len(way) >= 1:
            self.migrate(way[1:], map)

    def __str__(self):
        return f'Волк({self.get_coord()}), сила: {self._attack_power}'
