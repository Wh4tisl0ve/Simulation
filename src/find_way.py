from src.map.coordinates import Coordinates
from src.map.map import Map
from typing import Type, List
from queue import Queue


class WayFinder:
    def __init__(self, map: Map, entity_find: Type):
        self.__map = map
        self.__entity_find = entity_find

    def finding_shortest_way(self, start_coord: Coordinates) -> List[Coordinates]:
        list_goals_point = self.get_goals_point(self.__entity_find, self.__map.get_map())
        list_ways = []
        for goal_point in list_goals_point:
            list_ways.append(self.search_breadth_first(start_coord, goal_point))

        return min([way for way in list_ways if len(way) > 0], default=[], key=len)

    def search_breadth_first(self, start_coord: Coordinates, goal_coord: Coordinates) -> List[Coordinates]:
        visited_point = set()
        queue = Queue()
        queue.put(start_coord)
        parent = {}

        while not queue.empty():
            current_point = queue.get()
            visited_point.add(current_point)

            if current_point == goal_coord:
                return self.build_path(parent, start_coord, goal_coord)

            list_moves = self.get_list_moves(current_point)

            for point in list_moves:
                if point not in visited_point and self.__map.is_correct_point(point):
                    if self.__map.is_cell_empty(point) or isinstance(self.__map.get_entity(point), self.__entity_find):
                        visited_point.add(point)
                        parent[point] = current_point
                        queue.put(point)

        return []

    def build_path(self, parent: dict, start_point: Coordinates, goal_point: Coordinates) -> List[Coordinates]:
        pointer = goal_point
        path = [pointer]

        while pointer != start_point:
            pointer = parent[pointer]
            path.append(pointer)

        return list(reversed(path))

    def get_list_moves(self, current_point: Coordinates) -> List[Coordinates]:
        coord_up = Coordinates(current_point.get_x() - 1, current_point.get_y())
        coord_down = Coordinates(current_point.get_x() + 1, current_point.get_y())
        coord_right = Coordinates(current_point.get_x(), current_point.get_y() + 1)
        coord_left = Coordinates(current_point.get_x(), current_point.get_y() - 1)

        list_moves = [coord_up, coord_down, coord_left, coord_right]
        return list_moves

    def get_goals_point(self, entity_find: Type, entity_coord: dict) -> List[Coordinates]:
        list_goals_point = []

        for point, entity in entity_coord.items():
            if isinstance(entity, entity_find):
                list_goals_point.append(point)

        return list_goals_point
