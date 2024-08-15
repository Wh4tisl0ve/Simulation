from math import ceil, floor

from src.entities.creatures.herbivore.herbivore import Herbivore
from src.entities.creatures.predator.predator import Predator
from src.entities.resources.resource import Resource
from src.entities.static_objects.static_object import StaticObject
from src.map.map import Map
from src.reader import read_json


class Actions:
    def __init__(self, map: Map):
        self.__map = map

    def init_actions(self):
        proportion = read_json('data/proportion.json')
        self.generate_entities(proportion)

    def turn_actions(self):
        pass

    def generate_entities(self, proportion: dict):
        dict_entity = self.get_concrete_entities(proportion)
        for entity, value_proportion in dict_entity.items():
            cnt_entity = floor(value_proportion * self.__map.get_square_map())
            self.add_entity(cnt_entity, entity)

    def add_entity(self, count, entity):
        for cnt in range(count):
            coord = self.__map.get_random_empty_coord()
            self.__map.add_entity_on_map(entity(coord), coord)

    def get_concrete_entities(self, proportion: dict) -> dict:
        dict_subclasses = self.get_all_subclasses()
        dict_concrete_entity = dict()

        for i in dict_subclasses.keys():
            proportion_value = proportion[i.__name__]
            list_subclasses = dict_subclasses[i]
            for entity in list_subclasses:
                if len(list_subclasses) >= 2:
                    dict_concrete_entity[entity] = proportion_value / len(list_subclasses)
                else:
                    dict_concrete_entity[entity] = proportion_value

        return dict_concrete_entity

    def get_all_subclasses(self) -> dict:
        list_parent_object = [Predator, Herbivore, Resource, StaticObject]
        dict_result = dict()
        for parent in list_parent_object:
            subclasses = list()

            for child in parent.__subclasses__():
                subclasses.append(child)

            dict_result[parent] = subclasses
        return dict_result

