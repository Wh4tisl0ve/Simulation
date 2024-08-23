from src.actions.action import Action
from src.entities.creatures.creature import Creature


class MoveAction(Action):

    def perform(self):
        list_coord_creatures = [
            coord for coord in self._map.get_map()
            if isinstance(self._map.get_entity(coord), Creature)
        ]

        for coord in list_coord_creatures:
            entity = self._map.get_entity(coord)
            entity.make_move(self._map)
            self._map.update()
