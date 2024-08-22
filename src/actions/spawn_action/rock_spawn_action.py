from src.entities.static_objects.rock import Rock
from src.actions.spawn_action.spawn_action import SpawnAction
from src.map.coordinate import Coordinate


class RockSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinate) -> Rock:
        return Rock(coord)
