import re
from dataclasses import dataclass


@dataclass
class RGB:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    id: int
    sets: list[RGB]

    @classmethod
    def from_string(cls, string: str):
        game_header, game_sets = string.split(":")
        _game_string, id_string = game_header.split()
        id = int(id_string)

        set_list = game_sets.split(";")
        sets = [cls._process_one_set(set) for set in set_list]
        return cls(id, sets)

    @staticmethod
    def _process_one_set(string: str) -> RGB:
        def _count_color(color: str) -> int:
            match = re.search(f"(\\d+) {color}", string)
            count = int(match.group(1)) if match else 0
            return count

        reds = _count_color("red")
        greens = _count_color("green")
        blues = _count_color("blue")

        return RGB(reds, greens, blues)

    def _minimum_possible(self) -> RGB:
        required_reds = max(set.red for set in self.sets)
        required_greens = max(set.green for set in self.sets)
        required_blues = max(set.blue for set in self.sets)
        return RGB(required_reds, required_greens, required_blues)

    def is_possible(self, rgb: RGB) -> bool:
        sets_possible = [
            set.red <= rgb.red and set.green <= rgb.green and set.blue <= rgb.blue
            for set in self.sets
        ]
        return all(sets_possible)

    def power(self) -> int:
        minimum = self._minimum_possible()
        return minimum.red * minimum.green * minimum.blue


def part1(input: str) -> int:
    lines = input.splitlines()
    games = [Game.from_string(line) for line in lines]
    possible_game_ids = [game.id for game in games if game.is_possible(RGB(12, 13, 14))]
    return sum(possible_game_ids)


def part2(input: str) -> int:
    lines = input.splitlines()
    games = [Game.from_string(line) for line in lines]
    return sum(game.power() for game in games)
