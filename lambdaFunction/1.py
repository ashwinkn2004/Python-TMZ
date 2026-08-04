# findRem = lambda a,b:a%b
# summ = lambda a,b,c:a+b+c
# isEven = lambda a:a%2==0

# print(findRem(5,2))
# print(summ(1,2,3))
# print(isEven(10))

# lst = [5, 3, 6, 2, 8, 9, 7]
# square = lambda num:num*num

# ans = list(map(square, lst))
# print(ans)

# ans = []

# for num in lst:
#     ans.append(square(num))
# print(ans)

# lst = ["red", "green", "orange", "blue"]
# ans = list(map(lambda strr:strr.upper(), lst))
# print(ans)

lst = [2, 4, 6, 8, 10, 1, 5, 3, 9, 7]
# lst = list(map(int, input().split()))
findEven = lambda num: num%2==0

ans = list(filter(findEven, lst))
print(ans)