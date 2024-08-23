from src.entities.entity import Entity
from src.map.coordinate import Coordinate
from src.map.map import Map
from src.way_finder import WayFinder
from typing import Type


class Creature(Entity):
    def __init__(self, coord: Coordinate, age: int, weight: int, cnt_cells_pass: int, food: Type):
        super().__init__(coord)
        self._age = age
        self._weight = weight
        self._health_point: int = int((self._age * self._weight) / 10)
        self._cnt_cells_pass: int = cnt_cells_pass
        self.__food = food

    def make_move(self, map: Map) -> None:
        way_finder = WayFinder(map)
        goals_ways = way_finder.get_goals_coords(self.get_food())
        way = way_finder.finding_shortest_way(self.get_coord(), goals_ways)
        self.migrate(way, map)

    def get_food(self) -> Type:
        return self.__food
