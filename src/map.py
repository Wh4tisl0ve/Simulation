import random

from src.entities.entity import Entity
from src.coordinates import Coordinates


class Map:
    def __init__(self, size: tuple):
        self.__size = size
        self.__map = dict()

    def get_entity(self, coord: Coordinates) -> Entity:
        return self.__map[coord]

    def get_map_size(self) -> tuple:
        return self.__size

    def get_random_empty_coord(self) -> Coordinates:
        x = random.randint(0, self.__size[0])
        y = random.randint(0, self.__size[1])

        coord = Coordinates(x, y)

        if self.is_cell_empty(coord):
            return coord
        else:
            return self.get_random_empty_coord()

    def add_entity_on_map(self, entity: Entity, point: Coordinates) -> None:
        entity.set_coord(point)
        self.__map[point] = entity

    def is_cell_empty(self, coord: Coordinates) -> bool:
        return not (coord in self.__map.keys())



