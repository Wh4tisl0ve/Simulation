from src.map.coordinate import Coordinate
from src.entities.entity import Entity
from typing import Dict, Tuple
import random


class Map:
    def __init__(self, size: tuple):
        self.__size = size
        self.__map = dict()

    def get_entity(self, coord: Coordinate) -> Entity:
        return self.__map[coord]

    def get_map_size(self) -> Tuple[int]:
        return self.__size

    def get_random_empty_coord(self) -> Coordinate:
        x = random.randint(0, self.__size[0] - 1)
        y = random.randint(0, self.__size[1] - 1)

        coord = Coordinate(x, y)

        if self.is_cell_empty(coord):
            return coord
        else:
            return self.get_random_empty_coord()

    def get_map(self) -> Dict[Coordinate, Entity]:
        return self.__map

    def update(self) -> None:
        for point, entity in list(self.__map.items()):
            if entity.get_coord() != point:
                self.__map[entity.get_coord()] = entity
                self.__map.pop(point)

    def add_entity_on_map(self, entity: Entity, coord: Coordinate) -> None:
        self.__map[coord] = entity

    def is_cell_empty(self, coord: Coordinate) -> bool:
        return not (coord in self.__map.keys())

    def is_correct_point(self, point: Coordinate) -> bool:
        map_size = self.__size
        return 0 <= point.x <= map_size[0] - 1 and 0 <= point.y <= map_size[1] - 1

    def get_square_map(self) -> int:
        return self.__size[0] * self.__size[1]