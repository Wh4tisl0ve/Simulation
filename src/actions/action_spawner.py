from src.actions.actions_utils import ActionsUtils
from src.map.map import Map
from typing import Dict, Type


class ActionsSpawner:
    def __init__(self, proportion: dict, map: Map):
        self.__proportion = proportion
        self.__map = map

    def get_dict_entity(self, proportion: dict) -> Dict[Type, int]:
        dict_entity_necessary = ActionsUtils().get_concrete_entities(proportion, self.__map.get_square_map())
        return dict_entity_necessary

    def generate_entities(self, dict_entity: dict) -> None:
        for entity, cnt_entity in dict_entity.items():
            self.__add_entity(entity, cnt_entity)

    def __add_entity(self, entity, count) -> None:
        for _ in range(count):
            coord = self.__map.get_random_empty_coord()
            self.__map.add_entity_on_map(entity(coord), coord)

    def calc_cnt_missing_entity(self, dict_entity_on_map: dict) -> Dict[Type, int]:
        dict_diff = {}
        dict_entity_necessary = self.get_dict_entity(self.__proportion)

        for i in dict_entity_necessary.keys():
            if i in dict_entity_on_map.keys():
                dict_diff[i] = dict_entity_necessary[i] - dict_entity_on_map[i]
            else:
                dict_diff[i] = dict_entity_necessary[i]

        return dict_diff
