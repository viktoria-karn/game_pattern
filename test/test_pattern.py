from unittest import TestCase, main
from game_pattern import Game_pattern
#import game_pattern as gp

class GameTest(TestCase):
    def test_construction(self):
        assert Game_pattern()

    def test_singleton(self):
        g = Game_pattern()
        r_a,a = g.singleton_p()
        self.assertEqual(r_a,"singleton")

