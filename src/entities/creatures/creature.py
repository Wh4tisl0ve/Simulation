from typing import Type

from src.entities.entity import Entity
from abc import abstractmethod, ABC

from src.map.coordinates import Coordinates
from src.map.map import Map


class Creature(Entity, ABC):
    def __init__(self, coord: Coordinates, age: int, weight: int):
        super().__init__(coord)
        self._age = age
        self._weight = weight

    @abstractmethod
    def make_move(self, map: Map) -> None:
        pass
