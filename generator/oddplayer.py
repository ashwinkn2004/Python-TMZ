from time import sleep
import random

def choosePlay():
    choice = input("bat or ball : ")
    return choice

def computerPlay(target=None):
    score = 0

    while True:
        computer_input = random.randint(1, 6)
        user_input = int(input("Enter 1 - 6 : "))

        if user_input > 6 or user_input < 1:
            print("Invalid Choice\n")
            continue

        print(f"Computer : {computer_input}")

        if computer_input == user_input:
            print("OUT\n")
            print(f"Computer Score = {score}\n")
            break

        score += computer_input
        print(f"Computer Updated Score = {score}\n")

        if target is not None and score >= target:
            break

    return score

def userPlay(target=None):
    score = 0

    while True:
        computer_input = random.randint(1, 6)
        user_input = int(input("Enter 1 - 6 : "))

        if user_input > 6 or user_input < 1:
            print("Invalid Choice\n")
            continue

        print(f"Computer : {computer_input}")

        if computer_input == user_input:
            print("OUT\n")
            print(f"Player Score = {score}\n")
            break

        score += user_input
        print(f"Player Updated Score = {score}\n")

        if target is not None and score >= target:
            break

    return score


def play(batting):

    if batting == "computer":

        print("\n\n\t\t FIRST INNINGS \n\n")
        print("Computer is Batting\n")

        computer_score = computerPlay()

        target = computer_score + 1

        print(f"\nTarget for Player = {target}\n")

        print("\n\n\t\t SECOND INNINGS \n\n")
        print("Player is Batting\n")

        player_score = userPlay(target)

    else:

        print("\n\n\t\t FIRST INNINGS \n\n")
        print("Player is Batting\n")

        player_score = userPlay()

        target = player_score + 1

        print(f"\nTarget for Computer = {target}\n")

        print("\n\n\t\t SECOND INNINGS \n\n")
        print("Computer is Batting\n")

        computer_score = computerPlay(target)

    print("\n\n\t\t GAME OVER \n\n")

    print(f"Player Score   : {player_score}")
    print(f"Computer Score : {computer_score}\n")

    if player_score > computer_score:
        print(f"Player Won by {player_score - computer_score} runs!\n")
    elif computer_score > player_score:
        print(f"Computer Won by {computer_score - player_score} runs!\n")
    else:
        print("TIE\n")

odd_even = ["odd", "even"]
choose_play = ["bat", "ball"]
game = {}

player = input("Odd or Even : ").lower()

if player == "odd":
    computer = "even"
else:
    computer = "odd"

print(f"Computer : {computer}\n")

print("Tossing...")
sleep(2)

toss = random.choice(odd_even)

print(f"\nToss Result : {toss}\n")

if toss == player:

    print("Player won the toss\n")

    choice = choosePlay()

    if choice == "bat":
        game["bat"] = "player"
        game["ball"] = "computer"
    else:
        game["bat"] = "computer"
        game["ball"] = "player"

else:

    print("Computer won the toss\n")

    choice = random.choice(choose_play)

    print(f"Computer chooses to {choice}\n")

    if choice == "bat":
        game["bat"] = "computer"
        game["ball"] = "player"
    else:
        game["bat"] = "player"
        game["ball"] = "computer"

play(game["bat"])