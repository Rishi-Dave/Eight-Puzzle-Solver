from answer import solve , printSolution

def main():
    gameMode = 8
    while(gameMode != 0):
        gameMode = int(input("""Welcome to rdave009 and aneva018's 8 puzzle solver.\nType “1” to use a default puzzle, “2” to enter your own puzzle, or "0" to quit.\n"""))
        board = []
        if(gameMode == 0):
            print("Thanks for playing! Hope to see you again soon.")
            break
        elif(gameMode == 1):
            print("Choose your difficulty:\n- Trivial(t)\n- Very Easy(v)\n- Easy(e)\n- Doable(d)\n- Oh Boy(o)\n- Impossible(i)")
            difficulty = input()
            problems = {
                't' : [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '']],
                'v' : [['1', '2', '3'], ['4', '5', '6'], ['7', '', '8']],
                'e' : [['1', '2', ''], ['4', '5', '3'], ['7', '8', '6']],
                'd' : [['', '1', '2'], ['4', '5', '3'], ['7', '8', '6']],
                'o' : [['8', '7', '1'], ['6', '', '2'], ['5', '4', '3']],
                'i': [['1', '2', '3'], ['4', '5', '6'], ['8', '7', '']]
            }
            if difficulty not in problems:
                print("Sorry, this difficulty was not listed above, please enter a valid input")
                continue
            else:
                board = problems[difficulty]
        elif(gameMode == 2):
            print("Enter your puzzle, use a zero to represent the blank")
            prompts = ['first', 'second', 'third']
            for i in range(0,3):
                numInput = input('Enter the ' + prompts[i] + ' row, use space or tabs between numbers: ')
                numList = numInput.split()
                nums = [int(num) for num in numList]
                board.append(nums)
            for i in range(0,3):
                for j in range(0,3):
                    if board[i][j] > 0:
                        board[i][j] = str(board[i][j])
                    else:
                        board[i][j] = ''
        heuristic = ''
        while(True):
            heuristic = input("Enter your choice of algorithm(enter in a number):\n1 - Uniform Cost Search\n2 - A* with the Misplaced Tile heuristic\n3 - A* with the Euclidean distance heuristic\n")
            if heuristic != '1' or heuristic != '2' or heuristic != '3':
                break
            else:
                print("This heuristic is not a given option, please try again\n")
        print()
        myNode, maxQueue, numNodes = solve(board, int(heuristic))
        
        printSolution(myNode, 0, maxQueue,numNodes)
if __name__=="__main__":
    main()