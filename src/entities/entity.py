from abc import ABC

from src.map.coordinates import Coordinates


class Entity(ABC):

    def __init__(self, coord: Coordinates):
        self.__coord: Coordinates = coord

    def get_coord(self) -> Coordinates:
        return self.__coord

    def set_coord(self, coord: Coordinates) -> None:
        self.__coord = coord
