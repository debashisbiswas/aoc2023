from dataclasses import dataclass
from functools import reduce


@dataclass
class Race:
    time_in_ms: int
    record_distance_in_mm: int

    @property
    def winning_numbers(self) -> list[int]:
        winning_numbers = []
        for button_hold_time in range(self.time_in_ms):
            speed = button_hold_time
            remaining_time = self.time_in_ms - button_hold_time

            distance_traveled = speed * remaining_time
            if distance_traveled > self.record_distance_in_mm:
                winning_numbers.append(button_hold_time)

        return winning_numbers


def parse_races(string: str) -> list[Race]:
    time_line, dist_line = string.splitlines()

    _time_prefix, time_values = time_line.split(":")
    _dist_prefix, dist_values = dist_line.split(":")

    times = [int(time) for time in time_values.split()]
    dists = [int(dist) for dist in dist_values.split()]

    return [Race(time, dist) for time, dist in zip(times, dists)]


def parse_race_part_2(string: str) -> Race:
    time_line, dist_line = string.splitlines()

    _time_prefix, time_values = time_line.split(":")
    _dist_prefix, dist_values = dist_line.split(":")

    time = int("".join(time_values.split()))
    dist = int("".join(dist_values.split()))

    return Race(time, dist)


def part1(input: str) -> int:
    races = parse_races(input)
    winning_strat_count = (len(race.winning_numbers) for race in races)
    return reduce(lambda x, y: x * y, winning_strat_count)


def part2(input: str) -> int:
    race = parse_race_part_2(input)
    return len(race.winning_numbers)
