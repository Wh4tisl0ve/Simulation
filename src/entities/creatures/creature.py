from typing import Type

from src.entities.entity import Entity
from abc import abstractmethod, ABC

from src.map.coordinates import Coordinates
from src.map.map import Map


class Creature(Entity, ABC):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)

    @abstractmethod
    def make_move(self, map: Map) -> None:
        pass
