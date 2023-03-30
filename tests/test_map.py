from unittest import TestCase
from levelup.map import GameMap


class TestMap(TestCase):
    def test_init(self):
        testWorld = GameMap()
        self.assertEqual(testWorld.get_total_positions(), 100)

    def test_get_positions(self):
        testMap = GameMap()
        pos = testMap.get_positions()
        self.assertEqual(len(pos), 100)

        