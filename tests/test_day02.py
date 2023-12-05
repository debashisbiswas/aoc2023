import textwrap
import unittest

from advent import Day02


class Day02Tests(unittest.TestCase):
    def test_part1(self):
        input = textwrap.dedent(
            """
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """
        )

        self.assertEqual(Day02.part1(input), 8)

    def test_game_from_string(self):
        input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game = Day02.Game.from_string(input)
        self.assertEqual(game.id, 1)
        self.assertEqual(game.sets, [(4, 0, 3), (1, 2, 6), (0, 2, 0)])

    def test_game_from_string_double_digit_it(self):
        input = "Game 10: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game = Day02.Game.from_string(input)
        self.assertEqual(game.id, 10)

    def test_game_process_set(self):
        input = "3 blue, 4 red"
        self.assertEqual(Day02.Game._process_one_set(input), (4, 0, 3))

    def test_game_process_set_double_digt(self):
        input = "3 blue, 40 red"
        self.assertEqual(Day02.Game._process_one_set(input), (40, 0, 3))

    def test_game_is_possible(self):
        input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game = Day02.Game.from_string(input)
        self.assertEqual(game.is_possible(12, 13, 14), True)

    def test_game_not_possible(self):
        input = (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        game = Day02.Game.from_string(input)
        self.assertEqual(game.is_possible(12, 13, 14), False)
