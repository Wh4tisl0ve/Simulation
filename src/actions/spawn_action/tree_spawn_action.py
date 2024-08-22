from src.actions.spawn_action.spawn_action import SpawnAction
from src.entities.static_objects.tree import Tree
from src.map.coordinate import Coordinate


class TreeSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinate) -> Tree:
        return Tree(coord)
