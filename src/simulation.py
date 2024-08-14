from src.actions import Actions
from src.map import Map
from src.renderer import MapConsoleRenderer


class Simulation:
    def __init__(self, map: Map, actions: Actions):
        self.__map = map
        self.__field_renderer = MapConsoleRenderer()
        self.__actions = actions
        self.__cnt_round = 0

    def __next_turn(self):
        pass

    def start_simulation(self):
        self.__field_renderer.render(self.__map)

    def pause_simulation(self):
        pass
