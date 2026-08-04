
try:
    x = int(input("Enter 1st number : "))
    y = int(input("Enter 2nd number : "))
    print(x+y)
    print(x/y)
except:
    while(y == 0):
        print("Error")
        y = int(input("Enter 2nd number again : "))
        if(y != 0):
            print(x/y)



def sample(a, b, c="CSE"):
    print(a, b, c)

sample("hi", "a")
sample("hello", "b")
sample("bye", "c", "ME")