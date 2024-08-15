from src.entities.creatures.herbivore.herbivore import Herbivore
from src.entities.creatures.predator.predator import Predator
from src.entities.resources.resource import Resource
from src.entities.static_objects.static_object import StaticObject


class Actions:
    def init_actions(self):
        self.create_proportion()
        pass

    def turn_actions(self):
        pass

    def generate_entities(self):
        pass

    def create_proportion(self):
        # get_subclasses
        list_parent_object = [Predator, Herbivore, Resource, StaticObject]
        for parent in list_parent_object:
            classType = parent
            subclasses = list()

            print(parent.__name__, ":")
            for child in classType.__subclasses__():
                subclasses.append(child.__name__)

            print(subclasses)
