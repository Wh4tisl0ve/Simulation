from src.entities.creatures.creature import Creature
from src.map.map import Map
from src.reader import read_json
from math import ceil
from src.actions.child_classes import get_concrete_entities


class Actions:
    def __init__(self, map: Map):
        self.__map = map

    def init_actions(self):
        proportion = read_json('data/proportion.json')
        self.generate_entities(proportion)

    def turn_actions(self):
        map = self.__map.get_map()
        for entity in map.values():
            if isinstance(entity, Creature):
                entity.make_move(self.__map)

    def generate_entities(self, proportion: dict):
        dict_entity = get_concrete_entities(proportion)
        for entity, value_proportion in dict_entity.items():
            cnt_entity = ceil((value_proportion * self.__map.get_square_map()) / 2)
            self.add_entity(cnt_entity, entity)

    def add_entity(self, count, entity):
        for _ in range(count):
            coord = self.__map.get_random_empty_coord()
            self.__map.add_entity_on_map(entity(coord), coord)
