import textwrap
import unittest

from advent import day01


class Day01Tests(unittest.TestCase):
    def test_part1(self):
        input = textwrap.dedent(
            """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
            """
        )
        self.assertEqual(day01.part1(input), 142)

    def test_part2(self):
        input = textwrap.dedent(
            """
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
            """
        )
        self.assertEqual(day01.part2(input), 281)

    def test_find_digit(self):
        input = "1abc2"
        self.assertEqual(day01._find_first_digit(input), 1)
        self.assertEqual(day01._find_last_digit(input), 2)

    def test_find_digit_notends(self):
        input = "treb7uchet"
        self.assertEqual(day01._find_first_digit(input), 7)
        self.assertEqual(day01._find_last_digit(input), 7)

    def test_get_all_digits_one_word(self):
        input = "eight"
        self.assertEqual(day01._get_all_digits_on_line(input), [(0, 8)])

    def test_get_all_digits_one_word_and_number(self):
        input = "eight2"
        self.assertEqual(day01._get_all_digits_on_line(input), [(0, 8), (5, 2)])

    def test_mean_case_that_started_this_whole_thing(self):
        input = "eightwothree"
        self.assertEqual(day01._get_all_digits_on_line(input), [(0, 8), (4, 2), (7, 3)])

    def test_process_line_part2(self):
        input = "two1nine"
        self.assertEqual(day01._process_line_part2(input), 29)

    def test_process_line_part2_overlap(self):
        input = "eightwothree"
        self.assertEqual(day01._process_line_part2(input), 83)
