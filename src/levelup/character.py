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
        self.map = game_map
        self.position = self.map.get_positions()[0]

    def move(self, direction: Direction):
        self.position = self.map.calculate_position(self.position, direction)
        

    def get_name(self) -> str:
        return self.name

    def get_position(self):
        return self.position