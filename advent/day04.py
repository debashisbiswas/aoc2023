import os
from dataclasses import dataclass


@dataclass
class Card:
    id: int
    winning_numbers: set[int]
    my_numbers: set[int]

    @classmethod
    def from_string(cls, string: str):
        header, numbers = string.split(":")

        _word, num = header.split()
        id = int(num)

        winning_str, my_str = numbers.split("|")
        winning_numbers = set(map(int, winning_str.split()))
        my_numbers = set(map(int, my_str.split()))

        return cls(id, winning_numbers, my_numbers)

    def get_matching_numbers(self):
        return self.my_numbers & self.winning_numbers

    @property
    def match_count(self) -> int:
        return len(self.get_matching_numbers())

    @property
    def score(self) -> int:
        return 2 ** (self.match_count - 1) if self.match_count else 0


# repeat 3 times before DRY or something...
def _preprocess_input(input: str) -> list[str]:
    lines = input.split(os.linesep)
    stripped_lines = [line.strip() for line in lines]
    nonempty_lines = [line for line in stripped_lines if line]
    return nonempty_lines

def _process_cards(cards_index: dict[int, Card], remaining: list[Card]) -> int:
    cards = [1] * len(cards_index)

    for id, card in cards_index.items():
        for j in range(card.match_count):
            index = id - 1 + j + 1
            cards[index] += cards[id - 1]

    return sum(cards)


def part1(input: str) -> int:
    processed_input = _preprocess_input(input)
    scores = [Card.from_string(line).score for line in processed_input]
    return sum(scores)


def part2(input: str) -> int:
    processed_input = _preprocess_input(input)
    cards = [Card.from_string(line) for line in processed_input]

    index = {card.id: card for card in cards}
    final_card_count = _process_cards(index, cards.copy())
    return final_card_count
