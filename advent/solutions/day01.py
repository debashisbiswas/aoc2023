import collections
import os
import re

NumberIndex = collections.namedtuple("NumberIndex", ["index", "number"])


# TODO: put this somewhere reusable
def _preprocess_input(input: str) -> list[str]:
    lines = input.split(os.linesep)
    stripped_lines = [line.strip() for line in lines]
    nonempty_lines = [line for line in stripped_lines if line]
    return nonempty_lines


class Day01:
    NUMBERS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    @classmethod
    def part1(cls, input: str) -> int:
        processed_input = _preprocess_input(input)
        return sum(cls._process_line(line) for line in processed_input)

    @classmethod
    def part2(cls, input: str) -> int:
        processed_input = _preprocess_input(input)
        return sum(cls._process_line_part2(line) for line in processed_input)

    @classmethod
    def _process_line(cls, line: str) -> int:
        first = cls._find_first_digit(line)
        last = cls._find_last_digit(line)
        return int(f"{first}{last}")

    @classmethod
    def _process_line_part2(cls, line) -> int:
        numbers = cls._get_all_digits_on_line(line)
        first = numbers[0].number
        last = numbers[-1].number
        return int(f"{first}{last}")

    @classmethod
    def _find_first_digit(cls, string) -> int:
        for c in string:
            try:
                return int(c)
            except ValueError:
                continue

        return 0

    @classmethod
    def _find_last_digit(cls, string) -> int:
        return cls._find_first_digit(reversed(string))

    @classmethod
    def _get_all_digits_on_line(cls, line: str) -> list[NumberIndex]:
        result: list[NumberIndex] = []

        for word, num in cls.NUMBERS.items():
            matches = re.finditer(word, line)
            result += [NumberIndex(match.start(), num) for match in matches]

        digit_matches = re.finditer(r"\d", line)
        result += [
            NumberIndex(match.start(), int(match.group())) for match in digit_matches
        ]

        result.sort()
        return result
