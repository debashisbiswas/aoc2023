import textwrap
import unittest

from main import Day01


class Day01Tests(unittest.TestCase):
    def test_day01(self):
        input = textwrap.dedent(
        """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
        """
        )

        self.assertEqual(Day01.solve(input), 142)

    def test_day01_find_digit(self):
        input = "1abc2"
        self.assertEqual(Day01._find_first_digit(input), 1)
        self.assertEqual(Day01._find_last_digit(input), 2)

    def test_day01_find_digit_notends(self):
        input = "treb7uchet"
        self.assertEqual(Day01._find_first_digit(input), 7)
        self.assertEqual(Day01._find_last_digit(input), 7)
