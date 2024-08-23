from src.entities.creatures.herbivore.deer import Deer
from src.entities.creatures.predator.wolf import Wolf
from src.entities.entity import Entity
from src.entities.resources.grass import Grass
from src.entities.static_objects.rock import Rock
from src.entities.static_objects.tree import Tree


class IconRepository:
    def __init__(self):
        self.__icon_map = {
            Rock: "⛰️",
            Deer: "🦌",
            Grass: "🌾",
            Tree: "🌳",
            Wolf: "🐺"
        }

    def get_icon(self, entity: Entity) -> str:
        return self.__icon_map.get(type(entity), '👽')
