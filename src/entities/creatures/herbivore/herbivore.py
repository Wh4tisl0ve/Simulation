from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass
from src.map.coordinates import Coordinates
from abc import ABC


class Herbivore(Creature, ABC):
    def __init__(self, coord: Coordinates, age: int, weight: int, cnt_cells_pass: int):
        super().__init__(coord, age, weight, cnt_cells_pass, Grass)
