x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))

print("Sum = ", x+y)

def division(x, y):
    try:
        print("Division = ", x/y)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        y = int(input("Enter 2nd number again : "))
        if(y != 0):
            print("Division = ", x/y)
        else:
            division(x, y)
    except ValueError:
        print("ValueError")
    except:
        print("Error")
division(x, y)

