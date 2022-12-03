# Day 3, Part 1 of Advent of Code 2022
# [state the problem here]

# Problem() is my class that ingests the day's input and structures it for easy computation

class Problem():
    def __init__(self, filename):
        strings = []
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
        self.strings = strings
        return

# Define a function to evaluate key figures of merit 
def stuff(inputrow):
    value = 42
    return value

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day03\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day03\\input.txt")

    # Set up state variables 
    total = 0

    # Find the total scores 
    for row in t.strings:
        total += stuff(row)
    print(total)

    return

if __name__ == "__main__":
    main()