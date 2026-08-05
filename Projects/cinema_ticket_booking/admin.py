import time


# Admin menu

def adminMenu():
    print("1. Logout\n")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print("\nLogging out...\n")
        return time.sleep(1)
