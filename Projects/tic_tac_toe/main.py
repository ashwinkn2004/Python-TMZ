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
    flag = 0

    result = [[board[0][0], board[0][1], board[0][2]],
              [board[1][0], board[1][1], board[1][2]],
              [board[2][0], board[2][1], board[2][2]],
              [board[0][0], board[1][0], board[2][0]],
              [board[0][1], board[1][1], board[2][1]],
              [board[0][2], board[1][2], board[2][2]],
              [board[0][0], board[1][1], board[2][2]],
              [board[0][2], board[1][1], board[2][0]]]
    
    for i in result:
        if i[0] == i[1] and i[1] == i[2]:
            flag = 1
            break
    return flag


def game(board):

    global x_cnt, o_cnt

    while True:

        board = placeX(board)
        display(board)

        game_over = checkGameOver(board)
        game_won = checkGameWon(board)
        if game_over or game_won:
            if game_won:
                print("\nX won the game\n")
                x_cnt += 1
            else:
                print("\nTIE\n")
            break

        board = placeO(board)
        display(board)

        game_over = checkGameOver(board)
        game_won = checkGameWon(board)
        if game_over or game_won:
            if game_won:
                print("\nO won the game\n")
                o_cnt += 1
            else:
                print("\nTIE\n")
            break
    return board

                

print("\nWelcome to Tic Tac Toe\n")
time.sleep(1)

board = [[1,2,3],[4,5,6],[7,8,9]]

x_cnt = 0
o_cnt = 0

print("Player 1 : X\nPlayer 2 : O\n")
display(board)


while True:

    board = game(board)

    ch = input("Do you want to play again? (y/n) : ")
    if ch.lower() == 'y':
        board = reset(board)
        display(board)
    else:
        print("\nFinal Score : \n")
        print(f"\nX: {x_cnt}\nO: {o_cnt}")
        if x_cnt > o_cnt:
            print("\nX won the game\n")
        elif o_cnt > x_cnt:
            print("\nO won the game\n")
        else:
            print("\nTIE\n")
        print("\nExiting...\n")
        break


