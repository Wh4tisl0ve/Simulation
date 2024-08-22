from src.entities.static_objects.rock import Rock
from src.actions.spawn_action.spawn_action import SpawnAction
from src.map.coordinates import Coordinates


class RockSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinates) -> Rock:
        return Rock(coord)
