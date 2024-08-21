from src.entities.creatures.creature import Creature
from src.entities.creatures.herbivore.herbivore import Herbivore
from src.map.coordinates import Coordinates
from src.map.map import Map
from typing import Type, List


class Predator(Creature):

    def __init__(self, coord: Coordinates, age: int, weight: int, attack_range: int, cnt_cells_pass: int):
        super().__init__(coord, age, weight, cnt_cells_pass)
        self._attack_power: int = int((self._age * self._weight) * 0.1)
        self._food: Type = Herbivore
        self._attack_range = attack_range

    def migrate(self, way: List[Coordinates], map: Map) -> None:
        steps = self._cnt_cells_pass
        if steps > len(way):
            steps = len(way) - 1
        else:
            steps = self._cnt_cells_pass - 1

        if self.is_attack_possible(way, steps):
            steps_attack = self._cnt_cells_pass - abs(len(way) - self._cnt_cells_pass - self._attack_range - 1)
            if steps_attack >= 0:
                self.set_coord(way[steps_attack])
            self.attack(way, map)
        else:
            self.set_coord(way[steps])

    def attack(self, way: list, map: Map) -> None:
        herbivore_attacked = map.get_entity(way[-1])

        if herbivore_attacked.get_hp() <= 0:
            print(f'{self} съел {herbivore_attacked}')
            self.set_coord(herbivore_attacked.get_coord())
            return

        print(f'{self} атаковал {herbivore_attacked}')

        herbivore_attacked.set_hp(herbivore_attacked.get_hp() - self._attack_power)

    def is_attack_possible(self, way: list, steps: int) -> bool:
        food_coord_index = len(way) - 1

        if abs(steps - food_coord_index) <= self._attack_range:
            return True

        return False

    def get_food(self) -> Type:
        return self._food
