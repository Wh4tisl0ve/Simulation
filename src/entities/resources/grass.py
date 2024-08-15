from src.entities.resources.resource import Resource
from src.map.coordinates import Coordinates


class Grass(Resource):
    def __init__(self, coord: Coordinates):
        super().__init__(coord)