def sDetails(name, age, dept = "CSE"):
    print("Name = ", name)
    print("Age = ", age)
    print("DEPT = ", dept)
    print("")

sDetails("Ashwin", 22)
sDetails("Ananya", 21)
sDetails("Rohan", 22, "ME")



#reading multiple inputs from the user to the function
# * takes input as a tuple
# ** takes input as a dictionary


def tup(*a):
    print(a)

tup(4, 5, 6)

def dict(**a):
    print(a)

dict(a=1,b=2,c=3,d=4)

#sum from tuple
def sumTup(*a):
    summ = 0
    for i in a:
        summ+= i
    print(summ)

sumTup(4, 5, 6)