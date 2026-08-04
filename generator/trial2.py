# arr = []

# for i in range(2,102,2):
#     arr.append(i)
# print(arr)

import sys

def evenNumbers(limit):
    for i in range(2,limit+1,2):
        yield i

limit = 100

num = evenNumbers(limit)
arr = []
for i in range(limit//2):
    arr.append(next(num))
print(arr)
print(sys.getsizeof(evenNumbers(limit)))



