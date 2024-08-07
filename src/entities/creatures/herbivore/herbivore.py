from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass


class Herbivore(Creature):

    def __init__(self):
        self.__resource: Grass = None

    def make_move(self):
        pass