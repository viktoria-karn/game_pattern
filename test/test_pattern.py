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

    def test_builder(self):
        g = Game_pattern()
        r_a,a = g.builder_p()
        self.assertEqual(r_a,"builder")

    def test_bridge(self):
        g = Game_pattern()
        r_a,a = g.bridge_p()
        self.assertEqual(r_a,"bridge")

    def test_decorator(self):
        g = Game_pattern()
        r_a,a = g.decorator_p()
        self.assertEqual(r_a,"decorator")

    def test_adapter(self):
        g = Game_pattern()
        r_a,a = g.adapter_p()
        self.assertEqual(r_a,"adapter")

    def test_right_answer_true(self):
        g = Game_pattern()
        res = g.check_answer("singleton","singleton")
        self.assertEqual(res, 0)

    def test_right_answer_false(self):
        g = Game_pattern()
        res = g.check_answer("singleton","fabrica")
        self.assertEqual(res, 1)

