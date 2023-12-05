from advent import Day01, Day02


def main():
    with open("inputs/day01.txt") as file:
        input01 = file.read()
        print(Day01.part1(input01))
        print(Day01.part2(input01))

    print()

    with open("inputs/day02.txt") as file:
        input02 = file.read()
        print(Day02.part1(input02))
        print(Day02.part2(input02))

    print()


if __name__ == "__main__":
    main()
