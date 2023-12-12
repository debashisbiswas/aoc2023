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
    # TODO
    return 0
    seed_line, *map_sections = input.split("\n" * 2)
    seed_ranges = parse_seed_line_part_2(seed_line)
    maps = [parse_map(section) for section in map_sections]

    seeds = []
    for start, length in seed_ranges:
        seeds.extend(range(start, start + length))

    locations = get_location_numbers(seeds, maps)

    return min(locations)


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


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def parse_seed_line_part_2(seed_line: str) -> list[range]:
    values = seed_line.removeprefix("seeds: ")

    values_as_ints = [int(number) for number in values.split()]
    seed_pairs = [
        range(start, start + length) for (start, length) in chunks(values_as_ints, 2)
    ]

    return seed_pairs
