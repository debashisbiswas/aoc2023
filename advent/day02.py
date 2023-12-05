import os
import re
from dataclasses import dataclass
from functools import reduce


# repeat 3 times before DRY or something...
def _preprocess_input(input: str) -> list[str]:
    lines = input.split(os.linesep)
    stripped_lines = [line.strip() for line in lines]
    nonempty_lines = [line for line in stripped_lines if line]
    return nonempty_lines


@dataclass
class Game:
    id: int
    sets: list[tuple]

    @classmethod
    def from_string(cls, string: str):
        game_header, game_sets = string.split(":")
        _game_string, id_string = game_header.split()
        id = int(id_string)

        set_list = game_sets.split(";")
        sets = [cls._process_one_set(set) for set in set_list]
        return cls(id, sets)

    @staticmethod
    def _process_one_set(string: str) -> tuple[int, int, int]:
        red_match = re.search(r"(\d+) red", string)
        reds = 0
        if red_match:
            reds = int(red_match.group(1))

        blue_match = re.search(r"(\d+) blue", string)
        blues = 0
        if blue_match:
            blues = int(blue_match.group(1))

        green_match = re.search(r"(\d+) green", string)
        greens = 0
        if green_match:
            greens = int(green_match.group(1))

        return reds, greens, blues

    def is_possible(self, red: int, green: int, blue: int) -> bool:
        for set in self.sets:
            if any([set[0] > red, set[1] > green, set[2] > blue]):
                return False

        return True

    def minimum_possible(self) -> tuple[int, int, int]:
        required_reds = max(set[0] for set in self.sets)
        required_blues = max(set[1] for set in self.sets)
        required_greens = max(set[2] for set in self.sets)
        return required_reds, required_blues, required_greens


def part1(input: str) -> int:
    processed_input = _preprocess_input(input)
    games = [Game.from_string(line) for line in processed_input]
    possible_game_ids = [game.id for game in games if game.is_possible(12, 13, 14)]
    return sum(possible_game_ids)


def _get_power(game: Game) -> int:
    return reduce(lambda x, y: x * y, game.minimum_possible())


def part2(input: str) -> int:
    processed_input = _preprocess_input(input)
    games = [Game.from_string(line) for line in processed_input]
    return sum(_get_power(game) for game in games)
