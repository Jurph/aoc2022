# Day 4, Part 1 of Advent of Code 2022
# Find the overlap in pairs of floor-cleaning assignments

# Define parsing & helper functions
def jobify(jobstring: str):
        lowerbound, upperbound = jobstring.split("-")
        return set((range(int(lowerbound), int(upperbound)+1)))

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        plans = []
        lines = open(filename).read().splitlines()
        for line in lines:
            job1, job2 = line.split(",")
            plans.append([jobify(job1), jobify(job2)])
        self.plans = plans
        return

# Define a function to evaluate key figures of merit 



def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day04\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day04\\input.txt")

    # Set up state variables 
    redundant = 0
    collides = 0

    # Find the overlaps
    for plan in p.plan:
        if plan[0].issubset(plan[1]) or plan[0].issuperset(plan[1]):
            collides += 1
            redundant += 1
        elif len(plan[0].intersection(plan[1])) != 0:
            collides += 1
        else:
            pass
           
    print("Total number of wholly redundant assignments is {}".format(redundant))
    print("Total number of assignments with collisions at all is {}".format(collides))
    return

if __name__ == "__main__":
    main()