from node import Node
from queue import PriorityQueue


grid =  [[8,7,1],[6,0,2],[5,4,3]]
grid = [[0,1,2],[4,5,3],[7,8,6]]

def isequal(arr1,arr2) -> bool:
    if not arr1 or not arr2:  # Check if either is None or empty
        return False
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            if arr1[i][j] != arr2[i][j]:
                return False
    return True

def arrCheck(arr, arrlist) -> bool:
    if arrlist == []:
        return True
    for n in arrlist:
        if isequal(arr,n):
            return False
    return True
                
def GraphSearch(type = None, grid = [[0,1,2],[4,5,3],[7,8,6]]):
    perf = [[1,2,3],[4,5,6],[7,8,0]]
    mygrid = Node(grid,0,None,type)
    q = PriorityQueue()
    explored = []
    maxq = 0
    nodecount = 0
    q.put(mygrid)
    while q.qsize() != 0:
        maxq = max(q.qsize(),maxq)
        cur: Node = q.get()

        if isequal(cur.getGrid(),perf): #checking goal state
            return cur,maxq,nodecount
        
        if cur.level > 31:
            return None,0,0

        explored.append(cur.getGrid()) #adding to explored
        # print(cur)
        #print(cur.level)
        # print(cur.heuristic)
        # print(cur.total)
        nextNodes = cur.getNext()
        
        for n in nextNodes:
            if arrCheck(n.getGrid(),explored): #checking if in explored
                nodecount+=1
                q.put(n)
        
    if q.qsize() == 0 or q.qsize() > 31:
        return None,0,0

# grid = [[1,2,3],[4,5,6],[7,8,0]]
# GraphSearch("misplaced",grid)

