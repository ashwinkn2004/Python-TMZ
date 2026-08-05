from admin import adminMenu
from user import userMenu
from database_operations import createUserTable, checkUsername, userRegisterInDb, validateUser



# User Table is created

createUserTable()   # imported from database_operations.py



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



# User registration based on roles

def register():
    username = input("\nEnter username : ")
    if checkUsername(username):                     # Checks whether the username already exists in db, imported from database_operations.py
        print("Username already exists!")
        return register()

    password = input("Enter password : ")
    role = input("Enter role (admin/user) : ")

    userRegisterInDb(username, password, role)



# user login

def login():
    username = input("\nEnter username : ")
    password = input("Enter password : ")

    user = validateUser(username, password)

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
