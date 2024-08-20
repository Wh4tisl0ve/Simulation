from src.actions.actions import Actions
from src.map.map import Map
from src.map.renderer import MapConsoleRenderer
import time


class Simulation:
    def __init__(self):
        self.__map = Map((10, 10))
        self.__field_renderer = MapConsoleRenderer()
        self.__actions = Actions(self.__map, 'data/proportion.json')
        self.__cnt_round = 0
        self.__is_running = True

    def __next_turn(self) -> None:
        self.__actions.turn_actions()

    def start_simulation(self) -> None:
        self.__actions.init_actions()
        self.__field_renderer.render(self.__map)
        while True:
            if not self.__is_running:
                continue
            time.sleep(1.5)
            self.__next_turn()
            self.__field_renderer.render(self.__map)
            self.__cnt_round += 1

    def pause_simulation(self) -> None:
        while True:
            try:
                command = input()
                if command != "":
                    self.__is_running = not self.__is_running
            except Exception:
                pass
