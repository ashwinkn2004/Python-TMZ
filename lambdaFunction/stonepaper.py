import random

preVal = ["stone", "paper", "scissors"]
resComputer = 0
resPlayer = 0

for i in range(5):
    computer = 0
    player = 0
    computer = random.randint(1,3)
    player = int(input("1.Stone\n2.Paper\n3.Sissors\nEnter your choice : "))

    print("\nComputer choice = ",preVal[computer-1],"\nPlayer choice = ",preVal[player-1],"\n")
    if computer == 1 and player == 2:
        resPlayer += 1
        print("Player won this round\n")
    elif computer == 1 and player == 3:
        resComputer += 1
        print("Computer won this round\n")
    elif computer == 2 and player == 1:
        resComputer += 1
        print("Computer won this round\n")
    elif computer == 2 and player == 3:
        resPlayer += 1
        print("Player won this round\n")
    elif computer == 3 and player == 1:
        resPlayer += 1
        print("Player won this round\n")
    elif computer == 3 and player == 2:
        resComputer += 1
        print("Computer won this round\n")
    elif computer == player:
        print("\nTIE on this round\n")
    else:
        print("Invalid choice : try again\n")
    
    print(f"Player : {resPlayer}    |   Computer : {resComputer}\n")

print(f"\nPlayer Score : {resPlayer}\nComputer Score : {resComputer}\n")
if resPlayer < resComputer:
    print("Computer Won the game")
elif resPlayer == resComputer:
    print("\nTIE\n")
else:
    print("Player Won the game")