from enum import Enum
from typing import Tuple, List
from levelup.position import Position


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


class GameMap:
    starting_position: Position = Position(5, 5)
    size: Tuple[int, int] = (10, 10)
    position_count: int
    positions: List[Position]

    def __init__(self):
        self.positions = list()
        self.create_positions()

    def create_positions(self) -> None:
        for x in list(range(0, self.size[0])):
            for y in list(range(0, self.size[1])):
                self.positions.append(Position(x, y))
        self.position_count = len(self.positions)

    def is_valid_position(self, position: Position) -> bool:
        pass

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        pass

    def get_total_positions(self) -> int:
        return self.size[0] * self.size[1]

    def get_positions(self) -> List:
        return self.positions
