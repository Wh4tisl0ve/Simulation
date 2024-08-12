from src.map import Map


class MapConsoleRenderer:
    def render(self, map: Map):
        map_size = map.get_map_size()
        map_width = map_size[0]
        map_height = map_size[1]

        for i in range(map_width):
            for j in range(map_height):
                print('*', end=' ')
            print(' ')
