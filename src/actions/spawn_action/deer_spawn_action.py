from src.entities.creatures.herbivore.deer import Deer
from src.actions.spawn_action.spawn_action import SpawnAction
from src.map.coordinate import Coordinate


class DeerSpawnAction(SpawnAction):
    def spawn_entity(self, coord: Coordinate) -> Deer:
        return Deer(coord)
