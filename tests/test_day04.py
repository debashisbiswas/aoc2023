import unittest

from advent import day04
from tests.helpers import like_file

EXAMPLE = like_file(
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """
)


class TestDay04(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day04.part1(EXAMPLE), 13)

    def test_part2(self):
        self.assertEqual(day04.part2(EXAMPLE), 30)

    def test_parse_card(self):
        line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        expected_card = day04.Card(
            1, {41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}
        )
        actual_card = day04.Card.from_string(line)
        self.assertEqual(actual_card, expected_card)

    def test_matching_numbers(self):
        line = "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
        card = day04.Card.from_string(line)

        match_count = card.match_count
        matches = card.get_matching_numbers()

        self.assertEqual(match_count, 2)
        self.assertEqual(matches, {32, 61})

    def test_score(self):
        line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        card = day04.Card.from_string(line)
        self.assertEqual(card.score, 8)

    def test_score_one(self):
        line = "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"
        card = day04.Card.from_string(line)
        self.assertEqual(card.score, 1)

    def test_score_zero(self):
        line = "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        card = day04.Card.from_string(line)
        self.assertEqual(card.score, 0)
