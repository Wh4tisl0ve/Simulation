from src.map.coordinate import Coordinate
from src.map.icon_repository import IconRepository
from src.map.map import Map


class MapConsoleRenderer:
    def __init__(self):
        self.__icon_repo = IconRepository()

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
                    entity = map.get_entity(Coordinate(i, j))
                    icon_entity = self.__icon_repo.get_icon(entity)
                    print(f'\t{icon_entity}', end='')
            print(' ')
        print()

