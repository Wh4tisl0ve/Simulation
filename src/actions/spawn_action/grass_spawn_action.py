from src.entities.resources.grass import Grass
from src.actions.spawn_action.spawn_action import SpawnAction
from src.map.coordinate import Coordinate


class GrassSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinate) -> Grass:
        return Grass(coord)
