f = open("./Python/file handling/trial.txt","a")

limit = int(input("Enter the limit: "))

for i in range(1,limit+1) :
    f.write(str(i))
    f.write("\n")
f.close()

