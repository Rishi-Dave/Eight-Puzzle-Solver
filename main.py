from answer import solve , printSolution
    




def main():
    myNode, maxQueue = solve([['', '1', '2'], ['4', '5', '3'], ['7', '8', '6']], 3)
    printSolution(myNode, 0, maxQueue)
if __name__=="__main__":
    main()