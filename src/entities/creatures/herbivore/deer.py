from src.entities.creatures.herbivore.herbivore import Herbivore
from src.find_way import WayFinder
from src.map.coordinates import Coordinates
from src.map.map import Map
import random


class Deer(Herbivore):
    def __init__(self, coord: Coordinates):
        super().__init__(coord=coord,
                         age=random.randint(5, 20),
                         weight=random.randint(75, 200),
                         cnt_cells_pass=3)

    def make_move(self, map: Map) -> None:
        finder = WayFinder(map, self._food)
        way = finder.finding_shortest_way(self.get_coord())

        if len(way) >= 1:
            self.migrate(way[1:])

    def set_hp(self, hp: int) -> None:
        self._health_point = hp

    def get_hp(self) -> int:
        return self._health_point

    def __repr__(self) -> str:
        return f'Олень с координатами {self.get_coord()} и здоровьем: {self._health_point}'
