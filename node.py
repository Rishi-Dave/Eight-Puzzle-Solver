from functools import total_ordering
import copy
@total_ordering
class Node:
    grid = [[]]
    level = 0
    parent = None
    search = None
    total = 0
    def __init__(self,grid: list[list[int]],level, parent = None,search = None):
        self.grid = grid
        self.level = level
        self.parent = parent
        self.search = search
        if search == None:
            self.heuristic = 0 
        elif search == "misplaced":
            self.heuristic = misplacedH(self)
        elif search == "eucleadian":
            self.heuristic = eucleadianH(self)

        self.total = self.heuristic + self.level

    def __str__(self): 
        return '\n'.join(str(row) for row in self.grid) + '\n'

    def getGrid(self):
        return self.grid

    def getParent(self):
        return self.parent
    
    def getHtype(self):
        return self.heuristic
    
    def getTotal(self):
        return self.total
    
    def getLevel(self):
        return self.level
    
    def __le__(self, obj):
        return self.total <= obj.total
    
    def __ge__(self,obj):
        return self.total >= obj.total

    def __eq__(self,obj):
         return self.total == obj.total
    
    def getNext(self):
        #find zero
        x,y = 0,0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 0:
                    x = i
                    y = j
                    break
        next = []

        if x+1 in range(len(self.grid)):
            cur = copy.deepcopy(self.grid)
            cur[x][y], cur[x+1][y] = cur[x+1][y], cur[x][y]
            next.append(cur)

        if x-1 in range(len(self.grid)):
            cur = copy.deepcopy(self.grid)
            cur[x][y], cur[x-1][y] = cur[x-1][y], cur[x][y]
            next.append(cur)
        if y-1 in range(len(self.grid[0])):
            cur = copy.deepcopy(self.grid)
            cur[x][y], cur[x][y-1] = cur[x][y-1], cur[x][y]
            next.append(cur)
        if y+1 in range(len(self.grid[0])):
            cur = copy.deepcopy(self.grid)
            cur[x][y], cur[x][y+1] = cur[x][y+1], cur[x][y]
            next.append(cur)

        nextNodes = []
        for n in next:
            nextNodes.append(Node(n,self.level+1,self,self.search))

        return nextNodes
    
#Heuretstic function---------
def misplacedH(current:Node) -> int:
    perfect = [[1,2,3],[4,5,6],[7,8,0]]
    diff = 0
    for i in range(len(perfect)):
        for j in range(len(perfect[0])):
            if current.grid[i][j] == 0:
                continue  #ignoring 0 for misplaced heurstic
            if perfect[i][j] != current.grid[i][j]:
                diff+=1
    return diff

def eucleadianH(current:Node) -> int:
    perfect = [[1,2,3],[4,5,6],[7,8,0]]
    perfectcoords = {perfect[i][j]:[i,j] for i in range(len(perfect)) for j in range(len(perfect[0]))}
    currentcoords = {current.grid[i][j]:[i,j] for i in range(len(current.grid)) for j in range(len(current.grid[0]))}
    distance = 0
    for i in range(len(perfect)):
        for j in range(len(perfect[0])):
            if current.grid[i][j] == 0:
                continue  #ignoring 0 for misplaced heurstic
            if current.grid[i][j] != 0 and current.grid[i][j] != perfect[i][j]:
                addition = pow(perfectcoords[current.grid[i][j]][0] - currentcoords[current.grid[i][j]][0], 2) + pow(perfectcoords[current.grid[i][j]][1] - currentcoords[current.grid[i][j]][1], 2)
                distance += pow(addition,0.5)
    return distance/2 # divding by two since pairs are counted twice



