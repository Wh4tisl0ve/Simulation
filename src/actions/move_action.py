from src.actions.action import Action
from src.entities.creatures.creature import Creature
from src.way_finder import WayFinder


class MoveAction(Action):

    def perform(self):
        way_finder = WayFinder(self._map)

        list_coord_creatures = [
            coord for coord in self._map.get_map()
            if isinstance(self._map.get_entity(coord), Creature)
        ]

        for coord in list_coord_creatures:
            entity = self._map.get_entity(coord)
            goals_ways = way_finder.get_goals_coords(entity.get_food())
            way = way_finder.finding_shortest_way(entity.get_coord(), goals_ways)
            entity.make_move(way, self._map)
            self._map.update()
