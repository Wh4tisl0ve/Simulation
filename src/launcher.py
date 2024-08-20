from src.simulation import Simulation
from src import view
import threading


class Launcher:
    def __init__(self):
        self.__simulation = Simulation()

    def run(self) -> None:
        view.show_menu()
        user_cmd = self.__input_cmd_menu()
        self.select_item_menu(user_cmd)

    def select_item_menu(self, cmd) -> None:
        match cmd:
            case 1:
                view.show_information()
                thread_start = threading.Thread(target=self.__simulation.start_simulation)
                thread_pause = threading.Thread(target=self.__simulation.pause_simulation)
                thread_pause.start()
                thread_start.start()
            case 2:
                exit()
            case _:
                view.show_incorrect_command_error()
                self.run()

    def __input_cmd_menu(self) -> int:
        choice_user = input('Введите команду -> ')
        if choice_user.isdigit() and len(choice_user) == 1:
            if choice_user in ['1', '2']:
                return int(choice_user)

        return -1
