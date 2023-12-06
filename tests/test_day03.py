import textwrap
import unittest

from advent import day03

EXAMPLE = textwrap.dedent(
    """
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
"""
)


class TestDay03(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day03.part1(EXAMPLE), 4361)

    def test_part2(self):
        self.assertEqual(day03.part2(EXAMPLE), 467835)

    def test_get_part_numbers(self):
        input = day03._preprocess_input(EXAMPLE)
        self.assertEqual(
            day03._get_part_numbers(input), [467, 35, 633, 617, 592, 755, 664, 598]
        )

    def test_get_gear_numbers(self):
        input = day03._preprocess_input(EXAMPLE)
        self.assertEqual(day03._get_gear_ratios(input), [16345, 451490])
