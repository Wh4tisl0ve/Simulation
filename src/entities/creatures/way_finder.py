from src.map.coordinate import Coordinate
from src.map.map import Map
from typing import Type, List
from queue import Queue


class WayFinder:
    def __init__(self, map: Map):
        self.__map: Map = map

    def finding_shortest_way(self, start_coord: Coordinate, goals_ways: List[Coordinate]) -> List[Coordinate]:
        list_all_ways = [self.search_breadth_first(start_coord, coord) for coord in goals_ways]

        return min([way for way in list_all_ways if len(way) > 0], default=[], key=len)

    def search_breadth_first(self, start_coord: Coordinate, goal_coord: Coordinate) -> List[Coordinate]:
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
                    if self.__map.is_cell_empty(point) or goal_coord == point:
                        visited_point.add(point)
                        parent[point] = current_point
                        queue.put(point)

        return []

    def build_path(self, parent: dict, start_point: Coordinate, goal_point: Coordinate) -> List[Coordinate]:
        pointer = goal_point
        path = [pointer]

        while pointer != start_point:
            pointer = parent[pointer]
            path.append(pointer)

        return list(reversed(path))

    def get_list_moves(self, current_point: Coordinate) -> List[Coordinate]:
        coord_up = Coordinate(current_point.x - 1, current_point.y)
        coord_down = Coordinate(current_point.x + 1, current_point.y)
        coord_right = Coordinate(current_point.x, current_point.y + 1)
        coord_left = Coordinate(current_point.x, current_point.y - 1)

        list_moves = [coord_up, coord_down, coord_left, coord_right]
        return list_moves

    def get_goals_coords(self, entity_find: Type) -> List[Coordinate]:
        list_goals_point = [point for point, entity in self.__map.get_map().items() if isinstance(entity, entity_find)]

        return list_goals_point