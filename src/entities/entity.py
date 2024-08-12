from abc import ABC, abstractmethod

from src.coordinates import Coordinates


class Entity(ABC):
    """Корневой абстрактный класс для всех существ и
         объектов существующих в симуляции."""

    def __init__(self, coord: Coordinates):
        self.__coord: Coordinates = coord

    def get_coord(self) -> Coordinates:
        return self.__coord

    def set_coord(self, point: Coordinates):
        self.__coord = point
