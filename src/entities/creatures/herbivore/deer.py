from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinate import Coordinate
from src.map.map import Map
from typing import List
import random


class Deer(Herbivore):
    age_range = random.randint(5, 20)
    weight_range = random.randint(75, 200)

    def __init__(self, coord: Coordinate):
        super().__init__(coord=coord,
                         age=self.age_range,
                         weight=self.weight_range,
                         cnt_cells_pass=3)

    def migrate(self, way_food: List[Coordinate], map: Map) -> None:
        if way_food:
            steps = min(self._cnt_cells_pass, len(way_food) - 1)
            self.set_coord(way_food[steps])

    def set_hp(self, hp: int) -> None:
        self._health_point = hp

    def get_hp(self) -> int:
        return self._health_point

    def __str__(self) -> str:
        return f'Олень({self.get_coord()}), HP: {self._health_point}'
