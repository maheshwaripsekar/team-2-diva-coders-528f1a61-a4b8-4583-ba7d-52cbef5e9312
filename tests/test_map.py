from unittest import TestCase
from levelup.map import GameMap


class TestMap(TestCase):
    def test_init(self):
        testWorld = GameMap()
        self.assertEqual(testWorld.get_total_positions(), 100)
