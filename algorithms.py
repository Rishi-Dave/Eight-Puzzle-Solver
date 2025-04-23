def getMoves(board):
    moves = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == '':
                if i > 0:
                    newBoard = board.copy()
                    newBoard[i][j], newBoard[i-1][j] = newBoard[i-1][j], newBoard[i][j]
                    moves.append(newBoard)
                if i < 2:
                    newBoard = board.copy()
                    newBoard[i][j], newBoard[i+1][j] = newBoard[i+1][j], newBoard[i][j]
                    moves.append(newBoard)
                if j > 0:
                    newBoard = board.copy()
                    newBoard[i][j], newBoard[i][j-1] = newBoard[i][j-1], newBoard[i][j]
                    moves.append(newBoard)
                if j < 2:
                    newBoard = board.copy()
                    newBoard[i][j], newBoard[i][j+1] = newBoard[i][j+1], newBoard[i][j]
                    moves.append(newBoard)
    return moves

def isGoal(board):
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '']]
    return board == goal

def count_misplaced(board):
    misplaced = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != '' and board[i][j] != str(i*3 + j + 1):
                misplaced +=1
    return misplaced

from collections import deque
def unfcost(g):
    return g + 1
def solve(problem):
    queue = deque()
    queue.heappush((0, g, problem))
    visited = set()
    while queue:
        board, g, h = queue.popleft()
        moves = moves(getMoves(board))
        for move in move():
            queue.append((g + unfcost(g), g + 1, 0))

    return
def A_misplaced(problem):
    return
def A_eDistance(problem):
    return


def main():
    print(count_misplaced([['1', '6', '3'], ['4', '5', ''], ['7', '8', '2']]))

if __name__=="__main__":
    main()