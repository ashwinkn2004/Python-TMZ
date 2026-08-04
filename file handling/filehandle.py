name = input("Enter the name : ")

f = open("./Python/file handling/name.txt", "w")

f.write(name)
f.close()