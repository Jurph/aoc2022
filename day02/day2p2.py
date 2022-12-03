# Day 2, Part 1 of Advent of Code 2022
# Scoring a rock-paper-scissors tournament 

# The first column is what your opponent is going to play: 
#   A for Rock, B for Paper, and C for Scissors. 
# The second column [...] must be the outcome: 
#   X for losing, Y for draw, and Z for winning.

# X is losing, so AX = scissors, BX = rock, and CX = paper 
# Y is a draw, so AY = rock, BY = paper, CY = scissors
# X is a win, so AZ = paper, BZ = scissors, CZ = rock 

# Problem() is my class that ingests the day's input and structures it for easy computation

class Problem():
    def __init__(self, filename):
        strings = []
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
        self.strings = strings
        return

# Score an individual line of the tournament 
def score(row):
    # ...plus the score for the outcome of the round 
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).
    [theirplay, outcome] = row.split(" ")
    outcomes = {"X" : 0, "Y" : 3, "Z" : 6}
    scoreoutcome = outcomes.get(outcome)
    print("Scored {} for an outcome of {}".format(scoreoutcome, outcome))

    # "The score for a single round is the score for the outcome  
    # (1 for Rock, 2 for Paper, and 3 for Scissors)"
    rocks = ["B X", "A Y", "C Z"]
    papers = ["C X", "B Y", "A Z"]
    scissors = ["A X", "C Y", "B Z"]
    choices = {tuple(rocks) : 1, tuple(papers) : 2, tuple(scissors) : 3}
    for k in choices.keys():
        if row in k:
            scorechoice = choices.get(k)
    print("Scored {} for the choice of {}".format(scorechoice, row))
    score = scorechoice + scoreoutcome 
    return score

def main():
    # Ingest and format the data
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day02\\input.txt")

    # Set up state variables 
    total = 0

    # Find the total scores 
    for row in p.strings:
        newscore = score(row)
        print("Scored {} as {} points".format(row, newscore))
        total += newscore

    print(total)

    return

if __name__ == "__main__":
    main()