import time

def reset(board):
    
    board = [[1,2,3],[4,5,6],[7,8,9]]
    return board

def display(board):
    
    print("\n")
    for i in range(3):
        print("\t|", end = " ")
        for j in range(3):
            print(board[i][j], end = " | ")
        print()
    print("\n")

def placeX(board):
    inp = int(input("Enter the number to place x : "))

    flag = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == inp:
                flag = 1
                break

    if flag == 0:
        print("\nAlready filled, try again\n")
        placeX(board)

    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == inp:
                    board[i][j] = "X"
                    break

    return board

def placeO(board):

    inp = int(input("Enter the number to place o : "))

    flag = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == inp:
                flag = 1
                break

    if flag == 0:
        print("\nAlready filled, try again\n")
        placeO(board)

    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == inp:
                    board[i][j] = "O"
                    break
    return board

def checkGameOver(board):
    flag = 1
    temp = [1,2,3,4,5,6,7,8,9]

    for i in range(3):
        for j in range(3):
            if board[i][j] in temp:
                flag = 0
                break

    return flag

def checkGameWon(board):
    return 0


def game(board):

    while True:
        print("\n")

        board = placeX(board)
        display(board)

        game_over = checkGameOver(board)
        game_won = checkGameWon(board)
        if game_over or game_won:
            if game_won:
                print("\nX won the game\n")
            break
        print("\n")

        board = placeO(board)
        display(board)

        game_over = checkGameOver(board)
        game_won = checkGameWon(board)
        if game_over or game_won:
            if game_won:
                print("\nO won the game\n")
            break

                

print("\nWelcome to Tic Tac Toe\n")
time.sleep(1)

board = [[1,2,3],[4,5,6],[7,8,9]]

print("Player 1 : X\nPlayer 2 : O\n")
display(board)


while True:

    game(board)

    ch = input("Do you want to play again? (y/n) : ")
    if ch.lower() == 'y':
        board = reset(board)
        display(board)
    else:
        print("\nExiting...\n")
        break


