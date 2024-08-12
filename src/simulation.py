from src.actions import Actions
from src.map import Map
from src.renderer import MapConsoleRenderer


class Simulation:
    def __init__(self, map: Map, renderer: MapConsoleRenderer, actions: Actions):
        self.__map = map
        self.__field_renderer = renderer
        self.__actions = actions
        self.__cnt_round = 0

    def next_turn(self):
        pass

    def start_simulation(self):
        pass

    def pause_simulation(self):
        pass
