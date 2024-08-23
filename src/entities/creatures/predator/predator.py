from src.entities.creatures.creature import Creature
from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinate import Coordinate
from typing import List

from src.map.map import Map


class Predator(Creature):

    def __init__(self, coord: Coordinate, age: int, weight: int, attack_range: int, cnt_cells_pass: int):
        super().__init__(coord=coord,
                         age=age,
                         weight=weight,
                         cnt_cells_pass=cnt_cells_pass,
                         food=Herbivore)
        self._attack_power: int = int((self._age * self._weight) * 0.1)
        self._attack_range = attack_range

    def migrate(self, way: List[Coordinate], map: Map) -> None:
        if way:
            steps = min(self._cnt_cells_pass, len(way) - 1)
            if self.is_attack_possible(way, steps):
                steps = self._cnt_cells_pass - abs(len(way) - self._cnt_cells_pass - self._attack_range - 1)
                self.set_coord(way[steps])
                self.attack(way, map)
            else:
                self.set_coord(way[steps])

    def attack(self, way: List[Coordinate], map: Map) -> None:
        herbivore_attacked = map.get_entity(way[-1])

        if herbivore_attacked.get_hp() >= 0:
            herbivore_attacked.set_hp(herbivore_attacked.get_hp() - self._attack_power)
        else:
            self.set_coord(herbivore_attacked.get_coord())

    def is_attack_possible(self, way: List[Coordinate], steps: int) -> bool:
        food_coord_index = len(way) - 1

        if abs(steps - food_coord_index) <= self._attack_range:
            return True

        return False
