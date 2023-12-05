import os
import re
from dataclasses import dataclass

from advent import Day


# repeat 3 times before DRY or something...
def _preprocess_input(input: str) -> list[str]:
    lines = input.split(os.linesep)
    stripped_lines = [line.strip() for line in lines]
    nonempty_lines = [line for line in stripped_lines if line]
    return nonempty_lines


class Day02(Day):
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

        @classmethod
        def _process_one_set(cls, string: str) -> tuple[int, int, int]:
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

            return (reds, greens, blues)

        def is_possible(self, red: int, green: int, blue: int) -> bool:
            for set in self.sets:
                if any([set[0] > red, set[1] > green, set[2] > blue]):
                    return False

            return True

    @classmethod
    def part1(cls, input: str) -> int:
        processed_input = _preprocess_input(input)
        games = [cls.Game.from_string(line) for line in processed_input]
        possible_game_ids = [game.id for game in games if game.is_possible(12, 13, 14)]
        return sum(possible_game_ids)

    @classmethod
    def part2(cls, input: str) -> int:
        return 0