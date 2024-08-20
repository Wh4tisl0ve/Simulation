from src.entities.creatures.herbivore.herbivore import Herbivore
from src.entities.creatures.predator.predator import Predator
from src.entities.resources.resource import Resource
from src.entities.static_objects.static_object import StaticObject
from math import ceil
from typing import Dict, Type, List


class ActionsUtils:
    def get_concrete_entities(self, proportion: dict, map_square: int) -> Dict[Type, int]:
        dict_subclasses = self.__get_all_subclasses()
        dict_concrete_entity = dict()

        for i in dict_subclasses.keys():
            proportion_value = proportion[i.__name__]
            list_subclasses = dict_subclasses[i]
            for entity in list_subclasses:
                if len(list_subclasses) >= 2:
                    dict_concrete_entity[entity] = ceil(((proportion_value / len(list_subclasses)) * map_square) / 2)
                else:
                    dict_concrete_entity[entity] = ceil((proportion_value * map_square) / 2)

        return dict_concrete_entity

    def __get_all_subclasses(self) -> Dict[Type, List[Type]]:
        list_parent_object = [Predator, Herbivore, Resource, StaticObject]
        dict_result = dict()
        for parent in list_parent_object:
            subclasses = list()

            for child in parent.__subclasses__():
                subclasses.append(child)

            dict_result[parent] = subclasses

        return dict_result
