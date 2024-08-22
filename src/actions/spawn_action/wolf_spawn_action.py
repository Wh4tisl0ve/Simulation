from src.actions.spawn_action.spawn_action import SpawnAction
from src.entities.creatures.predator.wolf import Wolf
from src.map.coordinates import Coordinates


class WolfSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinates) -> Wolf:
        return Wolf(coord)
