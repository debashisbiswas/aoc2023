import os
import re
import string

SYMBOLS = set(string.punctuation) - set(".")


def _preprocess_input(input: str) -> list[str]:
    lines = input.split(os.linesep)
    stripped_lines = [line.strip() for line in lines]
    nonempty_lines = [line for line in stripped_lines if line]
    return nonempty_lines


def _get_part_numbers(input: list[str]) -> list[int]:
    result = []

    for y, line in enumerate(input):
        matches = re.finditer(r"(\d+)", line)
        for match in matches:
            is_part = False

            for x in range(*match.span()):
                coords = [
                    (y - 1, x - 1),
                    (y - 1, x),
                    (y - 1, x + 1),
                    (y, x + 1),
                    (y + 1, x + 1),
                    (y + 1, x),
                    (y + 1, x - 1),
                    (y, x - 1),
                ]

                for coord in coords:
                    try:
                        char = input[coord[0]][coord[1]]
                    except IndexError:
                        continue

                    if char in SYMBOLS:
                        is_part = True
                        break

            if is_part:
                result.append(int(match.group(1)))

    return result


def part1(input: str) -> int:
    processed_input = _preprocess_input(input)
    part_numbers = _get_part_numbers(processed_input)
    return sum(part_numbers)


def part2(input: str) -> int:
    return 0
