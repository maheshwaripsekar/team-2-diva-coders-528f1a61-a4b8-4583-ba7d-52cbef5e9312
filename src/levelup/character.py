from levelup.position import Position
from levelup.map import GameMap, Direction

DEFAULT_CHARACTER_NAME = "Diva"


class InvalidMoveException(Exception):
    pass


class Character:
    name: str
    map: GameMap = None
    position: Position = None

    def __init__(self, name: str = None):
        self.name = name or DEFAULT_CHARACTER_NAME

    def enter_map(self, game_map: GameMap):
        pass

    def move(self, direction: Direction):
        pass

    def get_name(self) -> str:
        return self.name