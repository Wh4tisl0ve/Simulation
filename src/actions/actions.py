from src.entities.creatures.creature import Creature
from src.map.map import Map
from src.actions.action_spawner import ActionsSpawner
from src.reader import read_json


class Actions:
    def __init__(self, map: Map):
        self.__map = map
        self.__proportion = read_json('data/proportion.json')
        self.__actions_spawner = ActionsSpawner(self.__proportion, self.__map)

    def init_actions(self) -> None:
        dict_entity = self.__actions_spawner.get_dict_entity(self.__proportion)
        self.__actions_spawner.generate_entities(dict_entity)

    def turn_actions(self) -> None:
        map = self.__map.get_map()
        for entity in list(map.values()):
            if isinstance(entity, Creature):
                entity.make_move(self.__map)
                self.__map.update()
        self.__actions_spawner.generate_entities(
            self.__actions_spawner.calc_cnt_missing_entity(self.__map.calc_entity_on_map()))
