from src.map.coordinate import Coordinate
from abc import ABC


class Entity(ABC):

    def __init__(self, coord: Coordinate):
        self.__coord: Coordinate = coord

    def get_coord(self) -> Coordinate:
        return self.__coord

    def set_coord(self, coord: Coordinate) -> None:
        self.__coord = coord
