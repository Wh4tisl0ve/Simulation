from src.entities.entity import Entity
from src.map.coordinates import Coordinates


class StaticObject(Entity):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
