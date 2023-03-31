from enum import Enum
from typing import Tuple, List
from levelup.position import Position


class Direction(Enum):
    UP = "UP"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"


class GameMap:
    starting_position: Position = Position(5, 5)
    size: Tuple[int, int] = (10, 10)
    position_count: int
    positions: List[Position]

    def __init__(self):
        self.positions = list()
        self.create_positions()

    def create_positions(self) -> None:
        for x in list(range(1, self.size[0] + 1)):
            for y in list(range(1, self.size[1] + 1)):
                self.positions.append(Position(x, y))
        self.position_count = len(self.positions)

    def is_valid_position(self, position: Position) -> bool:
        testX = position.coordinates[0]
        testY = position.coordinates[1]
        if testX > self.size[0] or testX < 1:
            return False
        if testY > self.size[1] or testY < 1:
            return False
        return True

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        startX = starting_position.coordinates[0]
        startY = starting_position.coordinates[1]

        if direction is Direction.UP:
            startY += 1
        if direction is Direction.DOWN:
            startY -= 1
        if direction is Direction.RIGHT:
            startX += 1
        if direction is Direction.LEFT:
            startX -= 1

        if self.is_valid_position(Position(startX, startY)):
            return Position(startX, startY)
        else:
            return starting_position

    def get_total_positions(self) -> int:
        return self.size[0] * self.size[1]

    def get_positions(self) -> List:
        return self.positions
