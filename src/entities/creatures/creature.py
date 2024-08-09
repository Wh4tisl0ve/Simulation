from src.entities.entity import Entity
from abc import ABC, abstractmethod


class Creature(ABC, Entity):
    def __init__(self, point: Point):
        super(self).__init__(point)
        self.__cnt_cells_pass = None
        self.__health_point = None
        self.__food = None

    @abstractmethod
    def make_move(self) -> None:
        pass
