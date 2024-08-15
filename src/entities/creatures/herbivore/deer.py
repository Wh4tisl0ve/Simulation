from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinates import Coordinates


class Deer(Herbivore):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
