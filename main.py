from advent import Day01


def main():
    with open("inputs/day01.txt") as file:
        input = file.read()

    print(Day01.part1(input))
    print(Day01.part2(input))


if __name__ == "__main__":
    main()
