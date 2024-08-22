from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinate import Coordinate
from typing import List
import random

from src.map.map import Map


class Deer(Herbivore):
    def __init__(self, coord: Coordinate):
        super().__init__(coord=coord,
                         age=random.randint(5, 20),
                         weight=random.randint(75, 200),
                         cnt_cells_pass=3)

    def migrate(self, way: List[Coordinate], map: Map) -> None:
        if way:
            steps = min(self._cnt_cells_pass, len(way) - 1)
            self.set_coord(way[steps])

    def set_hp(self, hp: int) -> None:
        self._health_point = hp

    def get_hp(self) -> int:
        return self._health_point

    def __str__(self) -> str:
        return f'Олень({self.get_coord()}), HP: {self._health_point}'
