from src.entities.creatures.herbivore.deer import Deer
from src.entities.creatures.predator.wolf import Wolf
from src.entities.entity import Entity

from src.map.coordinate import Coordinate

from src.entities.resources.grass import Grass
from src.entities.static_objects.rock import Rock
from src.entities.static_objects.tree import Tree

from src.map.map import Map


class MapConsoleRenderer:
    def render(self, map: Map) -> None:
        map_width, map_height = map.get_map_size()

        for i in range(map_height):
            print(f'\t{str(i)}', end='')
        print()

        for i in range(map_width):
            print(f'{i}', end='')
            for j in range(map_height):
                if map.is_cell_empty(Coordinate(i, j)):
                    print('\t🏾', end='')
                else:
                    icon_entity = self.select_icon_entities(map.get_entity(Coordinate(i, j)))
                    print(f'\t{icon_entity}', end='')
            print(' ')
        print()

    def select_icon_entities(self, entity: Entity) -> str:
        ICON_MAP = {
            Rock: "⛰️",
            Deer: "🦌",
            Grass: "🌾",
            Tree: "🌳",
            Wolf: "🐺"
        }
        return ICON_MAP.get(type(entity))

