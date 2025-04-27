import copy
class node:
    def __init__(self,g, h, board, prev):
        self.g = g
        self.h = h
        self.board = copy.deepcopy(board) #ensures the same board is not being edited by multiple nodes
        self.prev = prev
    def boardToList(self):
        boardList = []
        for i in range(0,3):
            for j in range(0,3):
                boardList.append(self.board[i][j])
        return tuple(boardList)

    def getMoves(self):
        moves = []
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == '': #check all four possible moves if they are in range and he current spot is the blank
                    if i > 0:
                        newBoard = copy.deepcopy(self.board)
                        newBoard[i][j] = newBoard[i-1][j]
                        newBoard[i-1][j] = ''
                        moves.append(newBoard)
                    if i < 2:
                        newBoard = copy.deepcopy(self.board)
                        newBoard[i][j] = newBoard[i+1][j]
                        newBoard[i+1][j] = ''
                        moves.append(newBoard)
                    if j > 0:
                        newBoard = copy.deepcopy(self.board)
                        newBoard[i][j] = newBoard[i][j-1]
                        newBoard[i][j-1] = ''
                        moves.append(newBoard)
                    if j < 2:
                        newBoard = copy.deepcopy(self.board)
                        newBoard[i][j] = newBoard[i][j+1]
                        newBoard[i][j+1] = ''
                        moves.append(newBoard)
                    break
        return moves
    # Node Compartors for prioitry Queue
    def __eq__(self, other_node):
        if not isinstance(other_node, node):
            raise TypeError('Can only compare two nodes')   
        if self.board == other_node.board:
            return True
        else:
            return False
        
    def __lt__(self, other_node):
        if not isinstance(other_node, node):
            raise TypeError('Can only use less than comparison on two nodes')
        if self.g < other_node.g:
            return True
        else:
            return False
        
    def __str__(self): #string to easily print during and testing and output to interface
        string = ''
        for i in range(0,3):
            for j in range(0,3):
                if(self.board[i][j] != ''):
                    string += self.board[i][j] + ' '
                else:
                    string += 'b '
            string += '\n'
        return string


