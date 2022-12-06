# Day 5, Part 1 of Advent of Code 2022
# Manipulate a stack of crates

# Turn this ugly-ass format into CSV
def normalize(inputline: str):
    a = inputline.replace('    ', ',')
    a = a.replace('] [', ',')
    a = a.replace('[','')
    a = a.replace(']',',')
    outputrow = a.split(',')
    return outputrow

# Crates() is my class that ingests the day's input and structures it for easy computation
class Crates():
    def __init__(self, filename):
        lines = open(filename).read().split('\n\n')
        boardlines, movelines = lines[0].splitlines(), lines[1].splitlines()
        
        # From the last (popped) row of boardlines, make a list of 
        # nonwhitespace characters, sort them, and take the largest, 
        # converting it to an int(). This should be the number of 
        # stacks we need.
        a = int(sorted(boardlines.pop(-1).split(), reverse=True)[0])
        board = [[] for x in range(a)]
        
        # From the remaining 'boardlines', find all the crates and store them
        # in the list 'board' we just initialized.
        # A 'stack' is a column, a 'height' is how tall the stack is. 
        for line in reversed(boardlines):
            for stack, crate in enumerate(normalize(line)):
                if crate != '':
                    board[stack].append(crate)

        # TODO: Get moves
        moves = []
        for line in movelines: 
            qty, src, dst = line.replace('move ', '').replace(' from ', ',').replace(' to ',',').split(',')
            moves.append([int(qty), int(src), int(dst)])

        self.moves = moves
        self.board = board 
        return            

    def process(self):
        for move in self.moves:
            # print("-=-=-")
            qty, src, dst = move[0], move[1]-1, move[2]-1
            # print("Moving {} from {} to {}".format(qty, src, dst))
            # print("Stack {} has {} crates".format(qty, len(self.board[src])))
            for i in range(qty):
                crate = self.board[src].pop()
                self.board[dst].append(crate)
            # print(self.board)

    def newprocess(self):
        for move in self.moves:
            # print("-=-=-")
            qty, src, dst = move[0], move[1]-1, move[2]-1
            # print("Moving {} from {} to {}".format(qty, src, dst))
            # print("Stack {} has {} crates".format(qty, len(self.board[src])))
            cranehold = []
            for i in range(qty):
                a = self.board[src].pop()
                cranehold.append(a)
            for j in range(qty):
                b = cranehold.pop()
                self.board[dst].append(b)
            # print(self.board)


def main():
    # Ingest and format the data
    t = Crates("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day05\\test.txt")
    p = Crates("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2022\\day05\\input.txt")

    # Set up state variables 
    readout = ''
    p.newprocess()
    for stack in p.board:
        readout += str(stack[-1])

    print("The top crate readout is {}".format(readout))
    return

if __name__ == "__main__":
    main()