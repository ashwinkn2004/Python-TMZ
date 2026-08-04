import random

computer_score = [44, 23, 87, 43, 23]
max_score = max(computer_score)
user_score = 0
flag = 0


print(f"current max score of computer = {max_score}\n")

while(user_score < max_score+1):
    computer = random.randint(1,6)
    player = int(input("Enter 1 - 6 : "))
    if(player > 6 or player == 0):
        print("Invalid Choice\n")
    else:
        print(f"computer = {computer}\n")
        if(computer == player):
            flag = 1
            break
        else:
            user_score += player
        print(f"User Updated Score = {user_score}\n")
if flag == 1:
    print(f"OUT\nScore = {user_score}\nComputer WON\n")
else:
    print(f"Player won\nFinal Score = {user_score}\n")