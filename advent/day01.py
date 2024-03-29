import collections
import re

NumberIndex = collections.namedtuple("NumberIndex", ["index", "number"])


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


def part1(input: str) -> int:
    lines = input.splitlines()
    return sum(_process_line(line) for line in lines)


def part2(input: str) -> int:
    lines = input.splitlines()
    return sum(_process_line_part2(line) for line in lines)


def _process_line(line: str) -> int:
    first = _find_first_digit(line)
    last = _find_last_digit(line)
    return int(f"{first}{last}")


def _process_line_part2(line: str) -> int:
    numbers = _get_all_digits_on_line(line)
    first = numbers[0].number
    last = numbers[-1].number
    return int(f"{first}{last}")


def _find_first_digit(string) -> int:
    for c in string:
        try:
            return int(c)
        except ValueError:
            continue

    return 0


def _find_last_digit(string) -> int:
    return _find_first_digit(reversed(string))


def _get_all_digits_on_line(line: str) -> list[NumberIndex]:
    result: list[NumberIndex] = []

    for word, num in NUMBERS.items():
        matches = re.finditer(word, line)
        result += [NumberIndex(match.start(), num) for match in matches]

    digit_matches = re.finditer(r"\d", line)
    result += [
        NumberIndex(match.start(), int(match.group())) for match in digit_matches
    ]

    result.sort()
    return result
