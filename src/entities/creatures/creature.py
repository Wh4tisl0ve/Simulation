from src.entities.entity import Entity
from src.map.coordinates import Coordinates
from src.map.map import Map
from abc import abstractmethod, ABC


class Creature(Entity, ABC):
    def __init__(self, coord: Coordinates, age: int, weight: int, cnt_cells_pass: int):
        super().__init__(coord)
        self._age = age
        self._weight = weight
        self._health_point: int = int((self._age * self._weight) / 10)
        self._cnt_cells_pass: int = cnt_cells_pass

    @abstractmethod
    def make_move(self, map: Map) -> None:
        pass
