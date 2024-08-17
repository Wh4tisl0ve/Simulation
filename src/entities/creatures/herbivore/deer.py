from typing import Type

from src.entities.creatures.herbivore.herbivore import Herbivore
from src.entities.resources.grass import Grass
from src.find_way import WayFinder
from src.map.coordinates import Coordinates
from src.map.map import Map


class Deer(Herbivore):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self.__resource: Type = Grass

    def make_move(self, map: Map):
        finder = WayFinder(map, self.__resource)
        way = finder.finding_shortest_way(self.get_coord())

    def __repr__(self):
        return f'Олень с координатами {self.get_coord()}'
