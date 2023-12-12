import unittest

from advent import day05
from tests.helpers import like_file

EXAMPLE = like_file(
    """
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4
    """
)


class TestDay05(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day05.part1(EXAMPLE), 35)

    @unittest.skip("Haven't solved this one yet!")
    def test_part2(self):
        self.assertEqual(day05.part2(EXAMPLE), 46)

    def test_parse_seed_line(self):
        seed_line = "seeds: 79 14 55 13"
        self.assertEqual(day05.parse_seed_line(seed_line), [79, 14, 55, 13])

    def test_parse_map_rule(self):
        map_line = "50 98 2"
        self.assertEqual(
            day05.parse_map_rule(map_line),
            day05.MapRule(source=98, destination=50, range_length=2),
        )

    def test_parse_map_section(self):
        map_line = "seed-to-soil map:\n50 98 2\n52 50 48\n"
        self.assertEqual(
            day05.parse_map(map_line),
            day05.Map(
                [
                    day05.MapRule(source=98, destination=50, range_length=2),
                    day05.MapRule(source=50, destination=52, range_length=48),
                ]
            ),
        )

    def test_map_lookup(self):
        map = day05.Map(
            [
                day05.MapRule(source=98, destination=50, range_length=2),
                day05.MapRule(source=50, destination=52, range_length=48),
            ]
        )

        self.assertEqual(map.lookup(79), 81)
        self.assertEqual(map.lookup(14), 14)
        self.assertEqual(map.lookup(55), 57)
        self.assertEqual(map.lookup(13), 13)


    def test_parse_seed_line_part_2(self):
        seed_line = "seeds: 79 14 55 13"
        self.assertEqual(day05.parse_seed_line_part_2(seed_line), [range(79, 93), range(55, 68)])
