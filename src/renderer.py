from src.entities.entity import Entity

from src.coordinates import Coordinates

from src.entities.creatures.herbivore.deer import Deer
from src.entities.creatures.predator.wolf import Wolf

from src.entities.resources.grass import Grass
from src.entities.static_objects.rock import Rock
from src.entities.static_objects.tree import Tree

from src.map import Map


class MapConsoleRenderer:
    def render(self, map: Map):
        map_size = map.get_map_size()
        map_width = map_size[0]
        map_height = map_size[1]

        for i in range(map_width):
            for j in range(map_height):
                if map.is_cell_empty(Coordinates(i, j)):
                    print('*', end=' ')
                else:
                    icon_entity = self.select_icon_entities(map.get_entity(Coordinates(i, j)))
                    print(icon_entity)
            print(' ')

    def select_icon_entities(self, entity: Entity) -> str:
        if isinstance(entity, Deer):
            return "🦌"
        elif isinstance(entity, Wolf):
            return "🐺"
        elif isinstance(entity, Rock):
            return "⛰️"
        elif isinstance(entity, Grass):
            return "🌾"
        elif isinstance(entity, Tree):
            return "🌳"
