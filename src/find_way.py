from typing import Type
from src.map.coordinates import Coordinates
from queue import Queue

from src.map.map import Map


class WayFinder:
    def __init__(self, map: Map):
        self.__map = map

    def start_finding_way(self, start_coord: Coordinates, entity_find: Type):
        list_goals_point = self.get_goals_point(entity_find, self.__map.get_map())
        for goal_point in list_goals_point:
            self.bfs(start_coord, goal_point)

    def bfs(self, start_coord: Coordinates, goal_coord: Coordinates):
        visited = []
        queue = Queue()
        queue.put(start_coord)

        while not queue.empty():
            current_point = queue.get()
            print('Текущая точка:', current_point)

            visited.append(current_point)

            list_moves = self.get_list_moves(current_point)

            for point in list_moves:
                if point == goal_coord:
                    print(point)
                    print('*******************Есть!*******************')
                    print('Цель:', goal_coord)
                    return
                if point not in visited:
                    if self.__map.is_correct_point(point) and self.__map.is_cell_empty(point):
                        print('Перемещения:', point)
                        queue.put(point)
                        visited.append(point)
        return []

    def get_list_moves(self, current_point: Coordinates) -> list:
        coord_up = Coordinates(current_point.get_x() - 1, current_point.get_y())
        coord_down = Coordinates(current_point.get_x() + 1, current_point.get_y())
        coord_right = Coordinates(current_point.get_x(), current_point.get_y() + 1)
        coord_left = Coordinates(current_point.get_x(), current_point.get_y() - 1)

        list_moves = [coord_up, coord_down, coord_left, coord_right]
        return list_moves

    def get_goals_point(self, entity_find: Type, entity_coord: dict) -> list:
        list_goals_point = []

        for point, entity in entity_coord.items():
            if isinstance(entity, entity_find):
                list_goals_point.append(point)

        return list_goals_point
