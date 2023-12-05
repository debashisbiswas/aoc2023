import abc


class Day(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def part1(cls, input):
        ...

    @classmethod
    @abc.abstractmethod
    def part2(cls, input):
        ...
