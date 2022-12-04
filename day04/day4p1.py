# Day 4, Part 1 of Advent of Code 2022
# Find the overlap in pairs of floor-cleaning assignments

# Define parsing & helper functions
def jobify(jobstring: str):
        lowerbound, upperbound = jobstring.split("-")
        return set((range(int(lowerbound), int(upperbound)+1)))

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        plan = []
        lines = open(filename).read().splitlines()
        for line in lines:
            job1, job2 = line.split(",")
            plan.append([jobify(job1), jobify(job2)])
        self.plan = plan
        return

# Define a function to evaluate key figures of merit 



def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day04\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day04\\input.txt")

    # Set up state variables 
    total = 0

    # Find the total scores 
    for plan in p.plan:
        if plan[0].issubset(plan[1]):
            total += 1
        elif plan[0].issuperset(plan[1]):
            total += 1
        else:
            pass
    
    print("Total number of overlapping assignments is {}".format(total))
    return

if __name__ == "__main__":
    main()