from src.entities.creatures.creature import Creature
from src.map.map import Map
from src.reader import read_json
from src.actions.actions_utils import ActionsUtils


class Actions:
    def __init__(self, map: Map):
        self.__map = map
        self.__proportion = read_json('data/proportion.json')

    def init_actions(self) -> None:
        dict_entity = self.get_dict_entity(self.__proportion)
        self.generate_entities(dict_entity)

    def turn_actions(self) -> None:
        map = self.__map.get_map()
        for entity in list(map.values()):
            if isinstance(entity, Creature):
                entity.make_move(self.__map)
                self.__map.update()
        self.generate_entities(self.calc_cnt_missing_entity(self.__map.calc_entity_on_map()))

    def calc_cnt_missing_entity(self, dict_entity_on_map: dict) -> dict:
        dict_diff = {}
        dict_entity_necessary = self.get_dict_entity(self.__proportion)

        for i in dict_entity_necessary.keys():
            if i in dict_entity_on_map.keys():
                dict_diff[i] = dict_entity_necessary[i] - dict_entity_on_map[i]
            else:
                dict_diff[i] = dict_entity_necessary[i]

        return dict_diff

    def generate_entities(self, dict_entity: dict) -> None:
        for entity, cnt_entity in dict_entity.items():
            self.add_entity(entity, cnt_entity)

    def get_dict_entity(self, proportion: dict) -> dict:
        dict_entity_necessary = ActionsUtils().get_concrete_entities(proportion, self.__map.get_square_map())
        return dict_entity_necessary

    def add_entity(self, entity, count) -> None:
        for _ in range(count):
            coord = self.__map.get_random_empty_coord()
            self.__map.add_entity_on_map(entity(coord), coord)
