from src.entities.static_objects.static_object import StaticObject
from src.map.coordinates import Coordinates


class Rock(StaticObject):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)
