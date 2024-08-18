from src.entities.creatures.creature import Creature
from src.map.map import Map
from src.reader import read_json
from math import ceil
from src.actions.actions_utils import ActionsUtils


class Actions:
    def __init__(self, map: Map):
        self.__map = map

    def init_actions(self) -> None:
        proportion = read_json('data/proportion.json')
        self.generate_entities(proportion)

    def turn_actions(self) -> None:
        map = self.__map.get_map()
        for entity in list(map.values()):
            if isinstance(entity, Creature):
                print(entity)
                entity.make_move(self.__map)
                self.__map.update()

    def generate_entities(self, proportion: dict) -> None:
        dict_entity = ActionsUtils().get_concrete_entities(proportion)
        for entity, value_proportion in dict_entity.items():
            cnt_entity = ceil((value_proportion * self.__map.get_square_map()) / 2)
            self.add_entity(cnt_entity, entity)

    def add_entity(self, count, entity) -> None:
        for _ in range(count):
            coord = self.__map.get_random_empty_coord()
            self.__map.add_entity_on_map(entity(coord), coord)
