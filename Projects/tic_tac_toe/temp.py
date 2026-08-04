import time

print("\nWelcome to Tic Tac Toe\n")

time.sleep(1)

board = [[1,2,3],[4,5,6],[7,8,9]]

print("Reference : ")
for i in range(3):
    print("|", end = " ")
    for j in range(3):
        print(board[i][j], end = " | ")
    print()

def display():
    for i in range(3):
        print("|", end = " ")
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                print(" ", end = " | ")
            else:
                print(board[i][j], end = " | ")
        print()

display()

inp = int(input("\nEnter the number where you want to place your X : "))
for i in range(3):
    for j in range(3):
        if board[i][j] == inp:
            board[i][j] = "X"

display()


inp = int(input("\nEnter the number where you want to place your X : "))
for i in range(3):
    for j in range(3):
        if board[i][j] == inp:
            board[i][j] = "X"

display()