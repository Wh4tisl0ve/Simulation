from src.entities.creatures.predator.predator import Predator
from src.map.coordinates import Coordinates


class Wolf(Predator):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)

    def make_move(self):
        #find_eat() -> Point
        pass