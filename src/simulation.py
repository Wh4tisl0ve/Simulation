class Simulation:
    def __init__(self, map: Map, renderer: Renderer):
        self.__map = map
        self.__cnt_round = 0
        self.__field_renderer = renderer

    def next_turn(self):
        pass

    def start_simulation(self):
        pass

    def pause_simulation(self):
        pass
