import os
from dataclasses import dataclass


@dataclass
class MapRule:
    source: int
    destination: int
    range_length: int


@dataclass
class Map:
    rules: list[MapRule]

    def lookup(self, number: int) -> int:
        for rule in self.rules:
            source_range = range(rule.source, rule.source + rule.range_length)
            dest_range = range(rule.destination, rule.destination + rule.range_length)

            if number in source_range:
                idx = source_range.index(number)
                return dest_range[idx]

        return number

def part1(input: str) -> int:
    seed_line, *map_sections = input.split("\n" * 2)
    seeds = parse_seed_line(seed_line)
    maps = [parse_map(section) for section in map_sections]

    locations = []
    for seed in seeds:
        current_value = seed

        for map in maps:
            current_value = map.lookup(current_value)

        locations.append(current_value)

    return min(locations)


def part2(input: str) -> int:
    return 0


def parse_map(map_section: str) -> Map:
    _prefix, *lines = map_section.splitlines()
    rules = [parse_map_rule(line.strip()) for line in lines]
    return Map(rules)


def parse_map_rule(map_line: str) -> MapRule:
    destination, source, range_length = map_line.split()
    return MapRule(
        source=int(source), destination=int(destination), range_length=int(range_length)
    )


def parse_seed_line(seed_line: str) -> list[int]:
    values = seed_line.removeprefix("seeds: ")
    return [int(number) for number in values.split()]
