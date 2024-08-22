from src.actions.action import Action


class SpawnAction(Action):
    def perform(self) -> None:
        coord = self._map.get_random_empty_coord()
        self._map.add_entity_on_map(self.spawn_entity(coord), coord)