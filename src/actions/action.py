from src.map.map import Map
from abc import ABC, abstractmethod


class Action(ABC):
    def __init__(self, map: Map):
        self._map = map

    @abstractmethod
    def perform(self) -> None:
        pass
