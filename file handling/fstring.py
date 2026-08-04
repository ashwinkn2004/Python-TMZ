f = open("./Python/file handling/fstring.txt", "w")

print("Enter Name, Age, Dept \n")
strr = list(map(str, input("Enter details : ").split()))

f.write(f"Name = {strr[0]}\nAge = {strr[1]}\nDept = {strr[2]}")
f.close()

