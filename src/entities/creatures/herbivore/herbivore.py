from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass
from src.map.coordinates import Coordinates
from typing import List, Type


class Herbivore(Creature):
    def __init__(self, coord: Coordinates, age: int, weight: int, cnt_cells_pass: int):
        super().__init__(coord, age, weight, cnt_cells_pass)
        self._food: Type = Grass

    def migrate(self, way: List[Coordinates]) -> None:
        steps = self._cnt_cells_pass
        if steps > len(way):
            steps = len(way) - 1
        else:
            steps = self._cnt_cells_pass - 1
        self.set_coord(way[steps])

    def get_food(self) -> Type:
        return self._food
