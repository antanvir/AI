import math

board = []
# goalState = [1, 2, 3, 8, 0, 4, 7, 6, 5]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
frontier = []
previousState = []
result = []
size = 0
counter = 0


def readFile():
    file = open("sample4.txt", "r+")
    initialState = file.readlines()

    for line in initialState:
        line = line.split()
        line = [int(_) for _ in line]
        board.extend(line)
        # board.append(line)

    print("Initial state: ", board)
    print("Goal state: ", goalState)
    # print(board[1])



def compare(list1, list2):
    if not list1 or not list2:
        return False
    if list1 != list2:
        return False
    return True
  

def stepCounter(i):
    result.append(goalState)
    parent = previousState[i]
    while(parent):
        result.append(parent)
        global counter
        counter += 1
        index = frontier.index(parent)
        parent = previousState[index]
    result.reverse()




def move(state, pos0, steps):
    newState = state[:]
    newState[pos0], newState[pos0 + steps] =  newState[pos0 + steps], newState[pos0]
    return newState


def heuristicFunction(state):
    count = 0
    for i in range(0, len(goalState)):
        gRow = i // 3
        gCol = i % 3
        pos = state.index(goalState[i])
        cRow = pos // 3
        cCol = pos % 3
        count += abs(gRow - cRow) + abs(gCol - cCol)
    return count



def getSuccessor(state, i):
    heuristicValue = 0
    successor = None
    possibleSuccessors = []
    heuristics = []
    parentOfCurrentNode = previousState[i]

    pos0 = state.index(0)
    row = pos0 // 3
    col = pos0 % 3

    if row > 0:
        newState = move(state, pos0, -3)
        if not compare(newState, parentOfCurrentNode):
            heuristics.append(heuristicFunction(newState))
            possibleSuccessors.append(newState)
    if col > 0:
        newState = move(state, pos0, -1)
        if not compare(newState, parentOfCurrentNode):
           heuristics.append(heuristicFunction(newState))
           possibleSuccessors.append(newState)
    if row < 2:
        newState = move(state, pos0, 3)
        if not compare(newState, parentOfCurrentNode):
            heuristics.append(heuristicFunction(newState))
            possibleSuccessors.append(newState)
    if col < 2:
        newState = move(state, pos0, 1)
        if not compare(newState, parentOfCurrentNode):
            heuristics.append(heuristicFunction(newState))
            possibleSuccessors.append(newState)
    posMin =   heuristics.index(min(heuristics))
    successor = possibleSuccessors[posMin]
    # print(possibleSuccessors)
    # print(heuristics)
    # print(successor)
    return successor


def GreedyBestFirst():
    global size
    frontier.append(board)
    previousState.append(None)

    size += 1
    i = 0
    while not compare(frontier[i], goalState):
        successor = getSuccessor(frontier[i], i)
        frontier.append(successor)
        previousState.append(frontier[i])
        size += 1
        i += 1
    stepCounter(i)
    return
        


def main():
    readFile()
    GreedyBestFirst();
    print("It took ", counter, " steps to solve the 8-puzzle.")
    print("Solving steps:")
    for _ in result:
        print(_) 


if __name__ == "__main__":
    main()
    # 8_puzle_GreedyBestFirst.py
