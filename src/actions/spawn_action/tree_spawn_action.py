from src.actions.spawn_action.spawn_action import SpawnAction
from src.entities.static_objects.tree import Tree
from src.map.coordinates import Coordinates


class TreeSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinates) -> Tree:
        return Tree(coord)
