def checkBalance(balance):
    print(f"\nAvailable Balance = {balance}\n")

def depositMoney(balance):
    money = int(input("\nEnter the money : "))
    balance += money
    return balance

def withdrawMoney(balance):
    withdraw = int(input(("\nEnter the money to withdraw : ")))
    if withdraw > balance:
        print("\nInsufficient balance\n")
        return balance
    else:
        balance -= withdraw
        print(f"\nWithdraw of {withdraw} was successful")
        checkBalance(balance)
        return balance

balance = 0

while True:
    print("\n1. Check Balance\n2. Deposit Money \n3. Withdraw Money\n4. Exit")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        checkBalance(balance)
    elif ch == 2:
        balance = depositMoney(balance)
    elif ch == 3:
        balance = withdrawMoney(balance)
    elif ch == 4:
        print("\nExiting...\n")
        break
    else:
        print("\nInvalid input, try again..\n")
