from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Coordinates:
    x: int
    y: int

    def __hash__(self):
        return hash(self.x + self.y)
