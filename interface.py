from search import GraphSearch
from node import Node

def getLineage(sol:Node) -> list[Node]:
    lin = []
    cur = sol
    while cur.level != 0:
        lin.append(cur)
        cur = cur.parent
    return lin


choice = int(input("Welcome to aneva018 8 puzzle solver Type \"1\" to use defualt puzzle, or \"2\" to enter your own puzzle \n"))
if choice == 1:
    grid = [[0,1,2],[4,5,3],[7,8,6]]
else:
    print("Enter your puzzle, use a zero to represent the blank")
    grid = [[],[],[]]
    row1 = input("Enter the first row, use space or tabs between numebers: ")
    grid[0] = [int(n) for n in row1.split()]
    row1 = input("Enter the second row, use space or tabs between numebers: ")
    grid[1] = [int(n) for n in row1.split()]
    row1 = input("Enter the third row, use space or tabs between numebers: ")
    grid[2] = [int(n) for n in row1.split()]

print("\n")
print("Enter your choice of algorithm")
choice = int(input(  "Uniform Cost Search[1] \n A* with the Misplaced Tile heuristic.[2] \n A* with the Euclidean distance heuristic.[3] \n"))


if choice == 1:
    sol = GraphSearch(None,grid)
elif choice == 2:
    sol,maxq,nodecount = GraphSearch("misplaced",grid)
elif choice == 3:
    sol,maxq,nodecount = GraphSearch("eucleadian",grid)

if not isinstance(sol,Node):
    print("This puzzle is unsolvable")
    exit() 


mygrid = Node(grid,0,None)

lin = getLineage(sol)
depth = len(lin)-1
print("Expanding State")
print(mygrid)

for _ in range(len(lin)):
    cur = lin.pop()
    print(f"The best next step is with g(n)= {cur.level} and h(n)= {cur.heuristic}")
    print(cur)

print("GOAL!!!!!!")


print(f"To solve this problem the search algorithm expanded a total of {nodecount} nodes.")
print(f"The maximum number of nodes in the queue at any one time: {maxq}.")
print(f"The depth of the goal node was {depth}")
