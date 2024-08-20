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
        dict_entity = self.get_dict_entity(proportion)
        self.generate_entities(dict_entity)

    def turn_actions(self) -> None:
        map = self.__map.get_map()
        for entity in list(map.values()):
            if isinstance(entity, Creature):
                entity.make_move(self.__map)
                self.__map.update()
        print(self.__map.calc_entity_on_map())

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
