from src.actions.spawn_action.spawn_action import SpawnAction
from src.entities.creatures.predator.wolf import Wolf
from src.map.coordinate import Coordinate


class WolfSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinate) -> Wolf:
        return Wolf(coord)
