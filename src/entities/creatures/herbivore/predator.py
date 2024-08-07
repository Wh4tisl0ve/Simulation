from src.entities.creatures.creature import Creature
from src.entities.resources.grass import Grass


class Predator(Creature):

    def __init__(self):
        self.__resource: Grass = None
        self.__attack_power = None

    def make_move(self):
        pass