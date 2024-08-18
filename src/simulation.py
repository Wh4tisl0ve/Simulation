import time

from src.actions.actions import Actions
from src.map.map import Map
from src.map.renderer import MapConsoleRenderer


class Simulation:
    def __init__(self, map: Map):
        self.__map = map
        self.__field_renderer = MapConsoleRenderer()
        self.__actions = Actions(self.__map)
        self.__cnt_round = 0

    def __next_turn(self):
        self.__actions.turn_actions()

    def start_simulation(self):
        self.__actions.init_actions()
        self.__field_renderer.render(self.__map)
        while True:
            time.sleep(2)
            self.__next_turn()
            self.__field_renderer.render(self.__map)

    def pause_simulation(self):
        pass
