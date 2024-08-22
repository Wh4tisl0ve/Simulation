from src.entities.creatures.herbivore.deer import Deer
from src.actions.spawn_action.spawn_action import SpawnAction
from src.map.coordinates import Coordinates


class DeerSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinates) -> Deer:
        return Deer(coord)
