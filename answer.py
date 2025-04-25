from heapq import heappop, heappush
from heuristics import findH
from node import node 

def isGoal(node):
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '']]
    return node.board == goal

def solve(problem, algorithm):
    queue = []
    heappush(queue, (0,node(0, 0, problem, None)))
    visited = set()
    maxQueue = 0
    while queue:
        maxQueue = max(maxQueue, len(queue))
        f, curNode = heappop(queue)
        tupleBoard = curNode.boardToList()
        if(tupleBoard in visited):
            continue
        visited.add(tupleBoard)
        if(isGoal(curNode)):
            return curNode, maxQueue, len(visited)
        moves = curNode.getMoves()
        for move in moves:
            h = findH(curNode.board, algorithm)
            heappush(queue, (curNode.g + 1+ h, node(curNode.g + 1, h, move, curNode)))

    return None

def printSolution(node, count, maxQueue, numNodes):
    if(node is None):
        return
    count = printSolution(node.prev, count + 1, maxQueue, numNodes)
    if(isGoal(node)):
        print("Goal!!!\n\nTo solve this problem the search algorithm expanded a total of " + str(numNodes) + " nodes.\nThe maximum number of nodes in the queue at any one time: " + str(maxQueue) + ".\nThe depth of the goal node was "+ str(node.g) + ".\n")
        return
    elif(node.prev is  None):
        print("Expanding state")
    else:
        print('The best state to expand with g(n) = ' + str(node.g) + " and h(n) = " +  str(node.h)  + ' is...')
    print(node)
    return count
