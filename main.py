import threading

from src.simulation import Simulation


def main():
    simulation = Simulation()
    thread_start = threading.Thread(target=simulation.start_simulation)
    thread_pause = threading.Thread(target=simulation.pause_simulation)
    thread_pause.start()
    thread_start.start()



if __name__ == '__main__':
    main()
