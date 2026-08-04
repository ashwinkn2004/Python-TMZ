def addDetails():
    f = open("./Python/file handling/ExpenseTracker/addDetails.txt", "a")
    print("Enter the Category, Rate, Date : \n")
    details = list(map(str, input().split()))
    f.write(f"{details[0]}, {details[1]}, {details[2]}\n")
    f.close()

def displayDetails():
    f = open("./Python/file handling/ExpenseTracker/addDetails.txt", "r")
    print("\n")
    print(f.read())
    f.close()

def sumExpense():
    f = open("./Python/file handling/ExpenseTracker/addDetails.txt", "r")
    lst = f.read().split(", ")
    summ = 0
    for i in range(1,len(lst),2):
        summ += int(lst[i])
    print("Total Expense = ",summ,"\n")

while True:
    print("1. Add Details\n2. Display Details\n3.Sum Expense\n4.Exit\n")
    ch = int(input("Enter your choice : "))
    if(ch == 1):
        addDetails()
    elif(ch == 2):
        displayDetails()
    elif(ch == 3):
        sumExpense()
    elif(ch == 4):
        print("Program exited successfully\n")
        break
    else:
        print("Invalid input\n")