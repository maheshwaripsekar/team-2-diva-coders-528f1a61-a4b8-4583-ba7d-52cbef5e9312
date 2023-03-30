from unittest import TestCase
from levelup.map import GameMap
from levelup.position import Position
from levelup.map import Direction

class TestMap(TestCase):
    def test_init(self):
        testWorld = GameMap()
        self.assertEqual(testWorld.get_total_positions(), 100)

    def test_get_positions(self):
        testMap = GameMap()
        pos = testMap.get_positions()
        self.assertEqual(len(pos), 100)

    def test_calculate_position(self):
        tPos = Position(5,5)
        tDirection = Direction.UP
        tWorld = GameMap()
        newPosition = tWorld.calculate_position(tPos, tDirection)
        self.assertEqual(newPosition.coordinates[0], 5)
        self.assertEqual(newPosition.coordinates[1], 6)

    def test_calculate_position(self):
        tPos = Position(10,10)
        tDirection = Direction.UP
        tWorld = GameMap()
        newPosition = tWorld.calculate_position(tPos, tDirection)
        self.assertEqual(newPosition.coordinates[0], 10)
        self.assertEqual(newPosition.coordinates[1], 10)
        