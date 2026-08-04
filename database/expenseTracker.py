import sqlite3

conn = sqlite3.connect("./Python/database/expenseTracker.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS EXPENSE (
        CATEGORY TEXT,
        RATE INTEGER,
        DATE DATE
    )
''')

def addDetails():
    
    print("Enter the Category, Rate, Date : \n")
    details = list(map(str, input().split()))

    c.execute('''
        INSERT INTO EXPENSE (CATEGORY, RATE, DATE)
        VALUES(?, ?, ?);
    ''', (details[0], details[1], details[2]))

    conn.commit()
    print()

def displayDetails():
    print("\nEXPENSES\n")
    c.execute('''
        SELECT * FROM EXPENSE;
    ''')
    for i in c.fetchall():
        for j in i:
            print(j,  end = " ")
        print()
    print("\n")

def sumExpense():
    c.execute('''
            SELECT SUM(rate) FROM EXPENSE;
    ''')
    
    for i in c.fetchall():
        print("\nTotal Expense = ",i[0],"\n", end = " ")
    print()

def editExpense():
    details = list(map(str, input("Enter the updated rate and for what : ").split()))
    c.execute('''
        UPDATE EXPENSE SET RATE = ? WHERE CATEGORY = ?
    ''', (details[0], details[1]))
    conn.commit()
    displayDetails()

def deleteExpense():
    dell = input("Enter the category to delete : ")
    c.execute('''
        DELETE FROM EXPENSE WHERE CATEGORY = ?
    ''', (dell,))
    conn.commit()
    displayDetails()


while True:
    print("1. Add Details\n2. Display Details\n3.Sum Expense\n4.Edit expense\n5.Delete Expense\n6.Exit\n")
    ch = int(input("Enter your choice : "))
    
    if(ch == 1):
        addDetails()
    elif(ch == 2):
        displayDetails()
    elif(ch == 3):
        sumExpense()
    elif(ch == 4):
        editExpense()
    elif(ch == 5):
        deleteExpense()
    elif(ch == 6):
        print("Program exited successfully\n")
        break
    else:
        print("Invalid input\n")