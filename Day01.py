#!/usr/bin/python

import sys


def part1():
    with open(filename, "r") as f:
        lines = f.readlines()
        numbers = [int(str(line).strip()) for line in lines]

        for i in range(len(numbers)-2):
            for j in range(i+1, len(numbers)-1):
                if numbers[i] + numbers[j] == 2020:
                    return (numbers[i] * numbers[j])


def part2():
    with open(filename, "r") as f:
        lines = f.readlines()
        numbers = [int(str(line).strip()) for line in lines]

        for i in range(len(numbers)-2):
            for j in range(i+1, len(numbers)-1):
                for k in range(j+1, len(numbers)):
                    if numbers[i] + numbers[j] + numbers[k] == 2020:
                        return (numbers[i] * numbers[j] * numbers[k])


if __name__ == "__main__":
    filename = sys.argv[1]

    print(f"Part 01: {part1()}")
    print(f"Part 02: {part2()}")
