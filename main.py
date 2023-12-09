import os
from dataclasses import dataclass
from time import time
from types import ModuleType

from advent import day01, day02, day03, day04


@dataclass
class Day:
    title: str
    input_filename: str
    module: ModuleType


def create_header_string() -> str:
    parts = []
    parts += [f"         | Part 1     | (time)     | Part 2     | (time)     "]
    parts += [f"---------+------------+------------+------------+------------"]
    return os.linesep.join(parts)


def create_solution_string(
    title, part_one, part_two, part_one_time: float, part_two_time: float
) -> str:
    part_one_time_str = f"{round(part_one_time, 5)}s"
    part_two_time_str = f"{round(part_two_time, 5)}s"
    return f"{title:8} | {str(part_one).ljust(10)} | {str(part_one_time_str).ljust(10)} | {str(part_two).ljust(10)} | {str(part_two_time_str).ljust(10)}"


def print_solutions(days: list[Day]):
    print(create_header_string())

    for day in days:
        with open(day.input_filename) as file:
            input = file.read()

        part_one_start = time()
        part_one_solution = day.module.part1(input)
        part_one_end = time()

        part_two_start = time()
        part_two_solution = day.module.part2(input)
        part_two_end = time()
        print(
            create_solution_string(
                day.title,
                part_one_solution,
                part_two_solution,
                part_one_end - part_one_start,
                part_two_end - part_two_start,
            )
        )


def main():
    days = [
        Day("Day 01", "inputs/day01.txt", day01),
        Day("Day 02", "inputs/day02.txt", day02),
        Day("Day 03", "inputs/day03.txt", day03),
        Day("Day 04", "inputs/day04.txt", day04),
    ]

    print_solutions(days)


if __name__ == "__main__":
    main()
