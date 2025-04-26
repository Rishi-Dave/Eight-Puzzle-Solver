from heuristic import misplacedH, eucleadianH

class Node:
    def __init__(self,grid,level, parent = None,search = None):
        self.grid = grid
        self.level = level
        self.parent = parent
        if search == None:
            self.heuristic = 0 
        elif search == "misplaced":
            self.heuristic = misplacedH(self)
        elif search == "eucleadian":
            self.heuristic = eucleadianH(self)
        self.total = self.heuristic + level

    def getGrid(self):
        return self.grid
