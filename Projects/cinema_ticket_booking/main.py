import sqlite3
import time

conn = sqlite3.connect("./Projects/cinema_ticket_booking/cinema.db")
cur = conn.cursor()



# Users table creation

cur.execute('''
    CREATE TABLE IF NOT EXISTS USERS(
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')



# Main menu

def mainMenu():
    print("\nMain Menu\n")
    print("1. Register\n2. Login\n3. Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        register()
    elif ch == 2:
        login()
    elif ch == 3:
        print("Exiting...")
        return 1
    else:
        print("\nInvalid input. Please try again..\n")



# Admin menu

def adminMenu():
    print("1. Logout\n")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print("\nLogging out...\n")
        return time.sleep(1)




# User menu

def userMenu():
    return



# Checks whether the username already exists in db

def checkUsername(username):
    cur.execute('''
        SELECT * FROM USERS WHERE username = ?
    ''', (username,))
    return cur.fetchone()



# User registration based on roles

def register():
    username = input("\nEnter username : ")
    if checkUsername(username):
        print("Username already exists!")
        return register()

    password = input("Enter password : ")
    role = input("Enter role (admin/user) : ")

    cur.execute('''
        INSERT INTO USERS(username, password, role)
        VALUES(?, ?, ?)
    ''', (username, password, role))

    conn.commit()



# user login

def login():
    username = input("\nEnter username : ")
    password = input("Enter password : ")

    cur.execute('''
        SELECT * FROM USERS WHERE username = ? AND password = ?
    ''', (username, password))

    user = cur.fetchone()

    if user:
        print(f"\nLogin successfull\n Welcome {user[1]} ({user[3]})")
        if user[3] == "admin":
            adminMenu()
        else:
            userMenu()
    else:
        print("\nInvalid username or password. Please try again..\n")



# Program starts here

while True:
    try:
        res = mainMenu()
        if res == 1:
            break
    except ValueError:
        print("\nInvalid input. Please try again..\n")
