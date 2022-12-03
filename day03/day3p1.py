# Day 3, Part 1 of Advent of Code 2022
# Identify and score the relevant item in a jumbled rucksack 

# Problem() is my class that ingests the day's input and structures it for easy computation

class Problem():
    def __init__(self, filename):
        bags = []
        lines = open(filename).read().splitlines()
        for line in lines:
            bags.append(line)
        self.bags = bags
        return

# Define a function to evaluate key figures of merit 
# To help prioritize item rearrangement, every item type can be converted to a priority:
# Lowercase item types a through z have priorities 1 through 26. 
# Uppercase item types A through Z have priorities 27 through 52. 

def priority(ch: str):
    p = ord(ch)
    if p > 94:      # ord('a') returns 97, we need to return 1...
        return p - 96 
    elif p > 65:    # ord('A') returns 65, we need to return 27...
        return p - 38
    else:
        quit()

def cleave(bag: str):
    half = int(len(bag)/2)
    return bag[0:half], bag[half:]

def findcommon(bagstring: str):
    listi, listj = cleave(bagstring)
    for i in listi:
        for j in listj:
            if i == j:
                print("Found   {}   in {} and {}".format(i, listi, listj))
                return i

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day03\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day03\\input.txt")

    # Set up state variables 
    total = 0

    # Find the total scores 
    for bag in p.bags:
        total += priority(findcommon(bag))
    
    print("Total priority is {}".format(total))
    return

if __name__ == "__main__":
    main()