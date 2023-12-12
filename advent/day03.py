import re
import string
from collections import defaultdict
from dataclasses import dataclass

SYMBOLS = set(string.punctuation) - set(".")


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


def _get_surrounding_coordinates(coord: Coordinate) -> list[Coordinate]:
    return [
        Coordinate(coord.x + 1, coord.y + 1),
        Coordinate(coord.x + 1, coord.y - 1),
        Coordinate(coord.x + 1, coord.y),
        Coordinate(coord.x - 1, coord.y + 1),
        Coordinate(coord.x - 1, coord.y - 1),
        Coordinate(coord.x - 1, coord.y),
        Coordinate(coord.x, coord.y + 1),
        Coordinate(coord.x, coord.y - 1),
    ]


def _access_coordinate(matrix: list[str], coord: Coordinate) -> str:
    return matrix[coord.y][coord.x]


def _get_part_numbers(input: list[str]) -> list[int]:
    result = []

    for y, line in enumerate(input):
        matches = re.finditer(r"(\d+)", line)
        for match in matches:
            is_part = False

            for x in range(*match.span()):
                surroundings = _get_surrounding_coordinates(Coordinate(x, y))

                for neighbor in surroundings:
                    try:
                        char = _access_coordinate(input, neighbor)
                    except IndexError:
                        continue

                    if char in SYMBOLS:
                        is_part = True
                        break

            if is_part:
                result.append(int(match.group(1)))

    return result


def _get_gear_ratios(input: list[str]) -> list[int]:
    gear_tracker: defaultdict[Coordinate, list[int]] = defaultdict(list)

    for y, line in enumerate(input):
        matches = re.finditer(r"(\d+)", line)

        for match in matches:
            accounted_for = False

            for x in range(*match.span()):
                surroundings = _get_surrounding_coordinates(Coordinate(x, y))

                for neighbor in surroundings:
                    try:
                        char = _access_coordinate(input, neighbor)
                    except IndexError:
                        continue

                    if char == "*" and not accounted_for:
                        gear_tracker[neighbor].append(int(match.group(1)))
                        accounted_for = True
                        break

    result = []
    for nearby_numbers in gear_tracker.values():
        if len(nearby_numbers) == 2:
            result.append(nearby_numbers[0] * nearby_numbers[1])

    return result


def part1(input: str) -> int:
    lines = input.splitlines()
    part_numbers = _get_part_numbers(lines)
    return sum(part_numbers)


def part2(input: str) -> int:
    lines = input.splitlines()
    gear_ratios = _get_gear_ratios(lines)
    return sum(gear_ratios)
