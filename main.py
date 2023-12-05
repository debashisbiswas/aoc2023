import os


class Day01:
    @classmethod
    def solve(cls, input):
        input = input.split(os.linesep)
        input = [line.strip() for line in input]
        input = [line for line in input if line]
        return sum(cls._process_line(line) for line in input)

    @classmethod
    def _find_first_digit(cls, string):
        for c in string:
            try:
                return int(c)
            except:
                continue

    @classmethod
    def _find_last_digit(cls, string):
        return cls._find_first_digit(reversed(string))

    @classmethod
    def _process_line(cls, line):
        first = cls._find_first_digit(line)
        last = cls._find_last_digit(line)

        return int(str(first) + str(last))


def main():
    with open("inputs/day01.txt") as file:
        input = file.read()

    print(Day01.solve(input))


if __name__ == "__main__":
    main()
