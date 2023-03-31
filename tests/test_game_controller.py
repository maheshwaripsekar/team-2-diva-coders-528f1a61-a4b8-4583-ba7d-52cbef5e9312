from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.controller import GameController, CharacterNotFoundException
from levelup.character import DEFAULT_CHARACTER_NAME, InvalidMoveException, Character
from levelup.map import Direction
from levelup.position import Position
from typing import Tuple

class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        self.assertEqual(testobj.status.move_count, 0)
        self.assertEqual(
            testobj.status.current_position,
            None,
        )

    def test_move(self):
        testGame = GameController()
        testGame.create_character("Bob the Builder")
        testGame.start_game()
        startPosition = testGame.character.get_position()
        testGame.move(Direction.UP)
        newPosition = testGame.character.get_position()
        self.assertEqual(startPosition.coordinates[0], newPosition.coordinates[0])
        self.assertEqual(startPosition.coordinates[1], newPosition.coordinates[1] -1)

    def test_game_status(self):
        testGame = GameController()
        testGame.create_character("Bob the Builder")
        testGame.start_game()
        testStatus = testGame.get_status()
        self.assertEqual(testStatus.character_name, "Bob the Builder")
        self.assertIsNotNone(testStatus.current_position)

    def test_total_positions(self):
        testGame = GameController()
        testGame.create_character("Morgan Freeman")
        testGame.start_game()
        totalPositions = testGame.get_total_positions()
        self.assertEqual(100, totalPositions)

    def test_set_character_position(self):
        testGame = GameController()
        testGame.create_character("Edward James Olmos")
        testGame.start_game()
        testGame.set_character_position(tuple((3,4)))
        newPosition = testGame.character.get_position()
        self.assertEqual(newPosition[0], 3)
        self.assertEqual(newPosition[1], 4)