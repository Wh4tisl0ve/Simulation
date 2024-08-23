from src.actions.action import Action
from src.map.map import Map
from math import floor


class SpawnAction(Action):
    def __init__(self, spawn_rate: float, map: Map):
        super().__init__(map)
        self.__spawn_rate = spawn_rate

    def perform(self) -> None:
        for _ in range(self.calc_cnt_entity()):
            coord = self._map.get_random_empty_coord()
            self._map.add_entity_on_map(self.spawn_entity(coord), coord)

    def calc_cnt_entity(self) -> int:
        return floor((self.__spawn_rate * self._map.get_square_map()) / 2)
