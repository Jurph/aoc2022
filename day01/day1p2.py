# Day 1, Part 1 of Advent of Code 2022
# [restate the problem here]

from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation

class Problem():
    def __init__(self, filename):
        strings = [] # We don't need strings in this chapter but it's a neat feature
        integers = []
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
            try:
                integers.append(int(line))
            except(ValueError):
                integers.append(int(0))
        self.strings = strings
        self.integers = integers
        return

# Find the total calories carried by all the elves 
def elfsums(problem):
    elves = []
    elfcalories = 0
    for snack in problem.integers:
        if snack > 0:
            elfcalories += snack
        elif snack == 0:
            elves.append(elfcalories)
            elfcalories = 0       
        else:
            print("Elf with negative calories detected")
    return elves

def main():
    # Ingest and format the data
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day01\\input.txt")

    # Set up state variables 
    total = 0
    previous = -1

    # Find the total calories carried by the three elves with the most calories
    elves = elfsums(p)
    answer = sorted(elves, reverse=True)[0] + sorted(elves, reverse=True)[1] + sorted(elves, reverse=True)[2]
    print(answer)

    return

if __name__ == "__main__":
    main()