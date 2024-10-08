from src.actions.action import Action
from src.actions.move_action import MoveAction
from src.actions.spawn_action.deer_spawn_action import DeerSpawnAction
from src.actions.spawn_action.grass_spawn_action import GrassSpawnAction
from src.actions.spawn_action.rock_spawn_action import RockSpawnAction
from src.actions.spawn_action.tree_spawn_action import TreeSpawnAction
from src.actions.spawn_action.wolf_spawn_action import WolfSpawnAction
from src.map.map import Map
from src.map.renderer import MapConsoleRenderer
import time


class Simulation:
    def __init__(self):
        self.__map: Map = Map((10, 10))
        self.__console_renderer = MapConsoleRenderer()
        self.__move_action: Action = MoveAction(self.__map)
        self.__list_spawn_action = []
        self.__is_running = True

    def start_simulation(self) -> None:
        self.perform_spawn_action()
        self.__console_renderer.render(self.__map)
        while True:
            if not self.__is_running:
                continue
            time.sleep(3)
            self.__move_action.perform()
            self.__console_renderer.render(self.__map)

    def pause_simulation(self) -> None:
        while True:
            try:
                command = input()
                if command != "":
                    self.__is_running = not self.__is_running
            except Exception:
                pass

    def perform_spawn_action(self):
        self.__fill_spawn_action()
        for spawn_action in self.__list_spawn_action:
            spawn_action.perform()

    def __fill_spawn_action(self):
        self.__list_spawn_action.append(RockSpawnAction(0.15, self.__map))
        self.__list_spawn_action.append(TreeSpawnAction(0.1, self.__map))
        self.__list_spawn_action.append(DeerSpawnAction(0.2, self.__map))
        self.__list_spawn_action.append(WolfSpawnAction(0.2, self.__map))
        self.__list_spawn_action.append(GrassSpawnAction(0.4, self.__map))
