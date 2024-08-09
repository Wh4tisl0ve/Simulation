from src.entities.creatures.creature import Creature
from src.entities.creatures.herbivore.herbivore import Herbivore


class Predator(Creature):

    def __init__(self):
        self.__food: Herbivore = None
        self.__attack_power = None

    def make_move(self):
        pass

    def attack(self, herbivore: Herbivore):
        # herbivore.set_HP(herbivore.get_HP() - self.__attack_power)
        pass

    def moving(self):
        pass
