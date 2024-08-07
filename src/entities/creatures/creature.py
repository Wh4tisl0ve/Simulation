from src.entities.entity import Entity
from abc import ABC, abstractmethod


class Creature(ABC, Entity):
    def __init__(self):
        self.__cnt_cells_pass = None
        self.__hit_point = None

    @abstractmethod
    def make_move(self):
        pass
