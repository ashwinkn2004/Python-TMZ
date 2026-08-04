numm = int(input("Enter a number: "))
cnt = 0

for i in range(1, numm):
    if numm % i == 0:
        cnt += 1
if cnt == 1:
    print(f"{numm} is Prime")
else:
    print(f"{numm} is NOT Prime")