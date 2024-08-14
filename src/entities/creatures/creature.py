from src.entities.entity import Entity
from abc import ABC, abstractmethod

from src.coordinates import Coordinates


class Creature(Entity):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self.__cnt_cells_pass = None
        self.__health_point = None
        self.__food = None

    @abstractmethod
    def make_move(self) -> None:
        pass
