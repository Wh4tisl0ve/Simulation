from src.map import Map
from src.renderer import MapConsoleRenderer


def main():
    map = Map((20, 20))
    renderer = MapConsoleRenderer()
    renderer.render(map)


if __name__ == '__main__':
    main()

