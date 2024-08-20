import threading

from src.simulation import Simulation


class Launcher:
    def __init__(self, simulation: Simulation):
        self.__simulation = simulation

    def run(self) -> None:
        user_cmd = self.input_cmd_menu()
        self.select_item_menu(user_cmd)

    def select_item_menu(self, cmd) -> None:
        t1 = threading.Thread(target=self.__simulation.start_simulation)
        t2 = threading.Thread(target=self.__simulation.pause_simulation)
        match cmd:
            case 1:
                t1.start()
                t2.start()
                self.run()
            case 2:

                self.run()
            case 3:
                exit()
            case _:
                self.run()

    def input_cmd_menu(self) -> int:
        choice_user = input('Введите команду -> ')
        if choice_user.isdigit() and len(choice_user) == 1:
            if choice_user in ['1', '2', '3']:
                return int(choice_user)

        return -1
