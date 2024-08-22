from src.entities.resources.grass import Grass
from src.actions.spawn_action.spawn_action import SpawnAction
from src.map.coordinates import Coordinates


class GrassSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinates) -> Grass:
        return Grass(coord)
