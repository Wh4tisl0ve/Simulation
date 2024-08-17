from typing import Type

from src.entities.entity import Entity
from abc import abstractmethod

from src.map.coordinates import Coordinates
from src.map.map import Map


class Creature(Entity):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
        self.__cnt_cells_pass: int = None
        self.__health_point: int = None

    @abstractmethod
    def make_move(self, map: Map) -> None:
        pass
