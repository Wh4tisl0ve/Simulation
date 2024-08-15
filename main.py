from src.map import Map
from src.simulation import Simulation


def main():
    map = Map((5, 5))
    actions = Actions()
    simulation = Simulation(map, actions)
    simulation.start_simulation()




if __name__ == '__main__':
    main()
