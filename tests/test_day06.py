import unittest

from advent import day06
from tests.helpers import like_file

EXAMPLE = like_file(
    """
    Time:      7  15   30
    Distance:  9  40  200
    """
)


class TestDay06(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day06.part1(EXAMPLE), 288)

    def test_part2(self):
        self.assertEqual(day06.part2(EXAMPLE), 71503)

    def test_parse_input(self):
        self.assertEqual(
            day06.parse_races(EXAMPLE),
            [day06.Race(7, 9), day06.Race(15, 40), day06.Race(30, 200)],
        )

    def test_winning_numbers(self):
        race = day06.Race(7, 9)
        self.assertEqual(race.winning_numbers, [2, 3, 4, 5])

    def test_parse_races_part_2(self):
        self.assertEqual(
            day06.parse_race_part_2(EXAMPLE),
            day06.Race(71530, 940200),
        )
