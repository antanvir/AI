import math

board = []
goalState = [1, 2, 3, 8, 0, 4, 7, 6, 5]
frontier = []
previousState = []
result = []
size = 0
counter = 0


def readFile():
    file = open("sample3.txt", "r+")
    initialState = file.readlines()

    for line in initialState:
        line = line.split()
        line = [int(_) for _ in line]
        board.extend(line)
        # board.append(line)

    print("Initial state: ", board)
    print("Goal state: ", goalState)
    # print(board[1])


def isSolvable(state):
    i = 0
    count = 0
    length = len(state)
    while i < length:
        j = i + 1
        while j < length:
            if state[j] != 0 and state[i] > state[j]:
                count += 1
            j += 1
        i += 1
    print(count)
    return count % 2 == 0




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



def getSuccessors(state, i):
    # print("==============================")
    successors = []
    parentOfCurrentNode = previousState[i]

    pos0 = state.index(0)
    row = pos0 // 3
    col = pos0 % 3

    if row > 0:
        newState = move(state, pos0, -3)
        if not compare(newState, parentOfCurrentNode):
            # print(newState)
            successors.append(newState)
            previousState.append(state)
    if col > 0:
        newState = move(state, pos0, -1)
        if not compare(newState, parentOfCurrentNode):
            # print(newState)
            successors.append(newState)
            previousState.append(state)
    if row < 2:
        newState = move(state, pos0, 3)
        if not compare(newState, parentOfCurrentNode):
            # print(newState)
            successors.append(newState)
            previousState.append(state)
    if col < 2:
        newState = move(state, pos0, 1)
        if not compare(newState, parentOfCurrentNode):
            # print(newState)
            successors.append(newState)
            previousState.append(state)
    return successors



def BFS():
    global size
    frontier.append(board)
    previousState.append(None)

    size += 1
    i = 0
    while i < size:
        if compare(frontier[i], goalState):
            # print("matched\tsize: ", size, "\nstate: ", frontier[i])
            stepCounter(i)
            return
        else:
            successors = getSuccessors(frontier[i], i)
            # for _ in successors:
            #     print(_)
            for j in range(0, len(successors)):
                frontier.append(successors[j])
                size += 1
                # print(size)
        i += 1


def main():
    readFile()
    BFS();
    # global counter
    print("It took ", counter, " steps to solve the 8-puzzle.")
    print("Solving steps:")
    for _ in result:
        print(_)
    # if isSolvable(board):
    #     BFS();
    #     global counter
    #     print("It took ", counter, " steps to solve the 8-puzzle.")
    #     print("Solving steps:")
    #     for _ in result:
    #         print(_)
    # else:
    #     print("This configuration of the board is not solvable.")


if __name__ == "__main__":
    main()
