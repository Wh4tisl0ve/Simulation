from src.entities.creatures.predator.predator import Predator
from src.map.coordinate import Coordinate
import random


class Wolf(Predator):
    age_range = random.randint(1, 6)
    weight_range = random.randint(60, 100)

    def __init__(self, coord: Coordinate):
        super().__init__(coord=coord,
                         age=self.age_range,
                         weight=self.weight_range,
                         attack_range=1,
                         cnt_cells_pass=4)

    def __str__(self):
        return f'Волк({self.get_coord()}), сила: {self._attack_power}'
