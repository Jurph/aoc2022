# Day 3, Part 2 of Advent of Code 2022
# Count off the elves in groups of three
# Figure out what badge they should be wearing 
# Identify and score the relevant item in their jumbled rucksacks 

import itertools

# Problem() is my class that ingests the day's input and structures it for easy computation

class Problem():
    def __init__(self, filename):
        bags = []
        elfgroups = []
        thisgroup = []
        lines = open(filename).read().splitlines()
        # Push the elves into groups of three
        for line in lines:
            bags.append(line)
            thisgroup.append(line)
            if len(thisgroup) == 3:
                elfgroups.append(thisgroup)
                thisgroup = []
        self.bags = bags
        self.elfgroups = elfgroups
        return

# Define a function to evaluate key figures of merit 

def priority(ch: str):
    # To help prioritize item rearrangement, every item type can be converted to a priority:
    # Lowercase item types a through z have priorities 1 through 26. 
    # Uppercase item types A through Z have priorities 27 through 52. 
    p = ord(ch)
    if p > 94:      # ord('a') returns 97, we need to return 1...
        return p - 96 
    elif p > 65:    # ord('A') returns 65, we need to return 27...
        return p - 38
    else:
        quit()

def findbadge(listi: str, listj: str, listk: str):
    for i in listi:
        if (i in listj) and (i in listk):
            # print("Found   {}   in {} and {} and {}".format(i, listi, listj, listk))
            return i

def findcommon(bagstring: str):
    half = int(len(bagstring)/2)
    listi, listj = bagstring[0:half], bagstring[half:]
    for i in listi:
        for j in listj:
            if i == j:
                #print("Found   {}   in {} and {}".format(i, listi, listj))
                return i

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day03\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day03\\input.txt")

    # Set up state variables 
    bagtotal = 0
    grouptotal = 0 

    # Find the total scores 
    for bag in p.bags:
        bagtotal += priority(findcommon(bag))

    for group in p.elfgroups:
        badge = findbadge(group[0], group[1], group[2])
        grouptotal += priority(badge)
    
    print("Total priority of items in bags is {}".format(bagtotal))
    print("Total priority of badges is {}".format(grouptotal))
    return

if __name__ == "__main__":
    main()