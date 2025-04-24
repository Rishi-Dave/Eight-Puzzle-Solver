from math import sqrt

def count_misplaced(board):
    misplaced = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != '' and board[i][j] != str(i*3 + j + 1):
                misplaced +=1
    return misplaced



def edistance(board):
    edistance = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != '' and board[i][j] != str(i*3 + j + 1):
                trueI = int(board[i][j]) // 3
                trueJ = (int(board[i][j]) - 1)% 3
                edistance += sqrt(pow(i - trueI, 2) + pow(j - trueJ, 2))
    return int(edistance)

def findH(board, algorithm):
    if algorithm == 1:
        return 0
    elif algorithm == 2:
        return count_misplaced(board)
    elif algorithm == 3:
        return edistance(board)
    return