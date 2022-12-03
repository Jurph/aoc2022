# Day 2, Part 1 of Advent of Code 2022
# Scoring a rock-paper-scissors tournament 

# The first column is what your opponent is going to play: 
#   A for Rock, B for Paper, and C for Scissors. 
# The second column [...] must be what you should play in response: 
#   X for Rock, Y for Paper, and Z for Scissors.

# X wins over C, Y wins over A, Z wins over B
# X draws with A, Y draws with B, Z draws with C 
# X loses to B, Y loses to C, Z loses to A

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
    # "The score for a single round is the score for the shape you selected 
    # (1 for Rock, 2 for Paper, and 3 for Scissors)"
    [theirplay, myplay] = row.split(" ")
    plays = {"X" : 1, "Y" : 2, "Z" : 3}
    scorechoice = plays.get(myplay)
    print("Scored {} for playing {}".format(scorechoice, myplay))

    # ...plus the score for the outcome of the round 
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).
    wins = ["C X", "A Y", "B Z"]
    draws = ["A X", "B Y", "C Z"]
    losses = ["B X", "C Y", "A Z"]
    outcomes = {tuple(wins) : 6, tuple(draws) : 3, tuple(losses) : 0}
    for k in outcomes.keys():
        if row in k:
            scoreoutcome = outcomes.get(k)
    print("Scored {} for the outcome of {}".format(scoreoutcome, row))
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