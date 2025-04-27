

def misplacedH(current):
    perfect = [[1,2,3],[4,5,6],[7,8,0]]
    diff = 0
    for i in range(len(perfect)):
        for j in range(len(perfect[0])):
            if current.grid[i][j] == 0:
                continue  #ignoring 0 for misplaced heurstic
            if perfect[i][j] != current.grid[i][j]:
                diff+=1
    return diff

def eucleadianH(current):
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

perfect = [[1,2,3],[4,5,6],[7,8,0]]
mygrid = [[5,2,3],[4,1,6],[7,8,0]]


myNode = Node(mygrid,0)

print(mygrid.getHtype())
print(eucleadianH(myNode))