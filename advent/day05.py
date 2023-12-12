from dataclasses import dataclass


@dataclass
class MapRule:
    source: int
    destination: int
    range_length: int

    def lookup(self, number: int) -> int | None:
        source_range = range(self.source, self.source + self.range_length)
        dest_range = range(self.destination, self.destination + self.range_length)

        if number in source_range:
            index = source_range.index(number)
            return dest_range[index]


@dataclass
class Map:
    rules: list[MapRule]

    def lookup(self, number: int) -> int:
        for rule in self.rules:
            if result := rule.lookup(number):
                return result

        return number


def part1(input: str) -> int:
    seed_line, *map_sections = input.split("\n" * 2)
    seeds = parse_seed_line(seed_line)
    maps = [parse_map(section) for section in map_sections]

    locations = get_location_numbers(seeds, maps)

    return min(locations)


def part2(input: str) -> int:
    return 0


def get_location_numbers(seeds: list[int], maps: list[Map]) -> list[int]:
    locations = []
    for seed in seeds:
        current_value = seed

        for map in maps:
            current_value = map.lookup(current_value)

        locations.append(current_value)

    return locations


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
