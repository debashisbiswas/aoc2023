import collections
import os
import re

NumberIndex = collections.namedtuple("NumberIndex", ["index", "number"])


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
    def part1(cls, input) -> int:
        input = input.split(os.linesep)
        input = [line.strip() for line in input]
        input = [line for line in input if line]
        return sum(cls._process_line(line) for line in input)

    @classmethod
    def part2(cls, input) -> int:
        input = input.split(os.linesep)
        input = [line.strip() for line in input]
        input = [line for line in input if line]
        return sum(cls._process_line_part2(line) for line in input)

    @classmethod
    def _process_line(cls, line) -> int:
        first = cls._find_first_digit(line)
        last = cls._find_last_digit(line)
        return int(str(first) + str(last))

    @classmethod
    def _process_line_part2(cls, line) -> int:
        numbers = cls._get_all_digits_on_line(line)
        return int(str(numbers[0].number) + str(numbers[-1].number))

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


def main():
    with open("inputs/day01.txt") as file:
        input = file.read()

    print(Day01.part1(input))
    print(Day01.part2(input))


if __name__ == "__main__":
    main()
