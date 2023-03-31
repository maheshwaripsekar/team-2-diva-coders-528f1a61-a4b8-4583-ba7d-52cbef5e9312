from unittest import TestCase
from levelup.character import Character, InvalidMoveException
from levelup.map import GameMap, Direction
from levelup.position import Position


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.name, expected_name)
        expected_position = None
        self.assertEqual(testobj.position, expected_position)

    def test_custom_name(self):
        testCharacter = Character("Aida Lovelace")
        self.assertEqual(testCharacter.get_name(), "Aida Lovelace")

    def test_default_name(self):
        testCharacter = Character()
        self.assertEqual(testCharacter.get_name(), "Diva")

    def test_enter_map(self):
        tMap = GameMap()
        tCharacter = Character("Trogdor")
        tCharacter.enter_map(tMap)
        self.assertEqual(tCharacter.map, tMap)

    def test_get_position(self):
        tChar = Character("Hiro Protagonist")
        tMap = GameMap()
        tChar.enter_map(tMap)
        currentPosition = tChar.get_position()
        self.assertIsNotNone(currentPosition)
        self.assertIsNotNone(currentPosition.coordinates[0])
        self.assertIsNotNone(currentPosition.coordinates[1])

    def test_move(self):
        testCharacter = Character()
        testMap = GameMap()
        testCharacter.enter_map(testMap)
        startingPosition = testCharacter.get_position()
        testCharacter.move(Direction.RIGHT)
        newPosition = testCharacter.get_position()
        self.assertEqual(startingPosition.coordinates[0], newPosition.coordinates[0] - 1)
        self.assertEqual(startingPosition.coordinates[1], newPosition.coordinates[1])