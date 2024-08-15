from src.actions import Actions
from src.map.coordinates import Coordinates
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
        pass

    def start_simulation(self):
        self.__actions.init_actions()
        #while()

        self.__field_renderer.render(self.__map)
        #self.__next_turn()

    def pause_simulation(self):
        pass
