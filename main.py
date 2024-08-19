from src.map.map import Map
from src.simulation import Simulation


def main():
    map = Map((8, 5))
    simulation = Simulation(map)
    simulation.start_simulation()


if __name__ == '__main__':
    main()
