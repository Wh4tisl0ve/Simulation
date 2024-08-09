from abc import ABC, abstractmethod


class Entity(ABC):
    '''Корневой абстрактный класс для всех существ и
         объектов существующих в симуляции.'''

    def __init__(self, coord: Point):
        self.__coord: Point = coord

    @abstractmethod
    def get_coord(self) -> Point:
        pass
