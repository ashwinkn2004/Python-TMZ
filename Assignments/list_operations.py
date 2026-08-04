lst = list(map(int, input("Enter the elements : ").split()))

#By Built-in functions

print("Max by function= ", max(lst))
print("Min by function = ", min(lst))

#By Logic

maxx = 0
minn = lst[0]

for i in lst:
    if i >= maxx:
        maxx = i
    if i <= minn:
        minn = i
print("Max by logic= ", maxx)
print("Min by logic = ", minn)