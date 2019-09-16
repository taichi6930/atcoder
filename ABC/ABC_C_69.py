n = int(input())
a = map(int, input().split())
num4 = 0
num1 = 0
for i in a:
    if i % 4 == 0:
        num4 += 1
        continue
    if i % 2 == 1:
        num1 += 1
plus, minus = num4 + num1, num4 - num1
if minus >= 0 or minus == -1 and plus % 2 == 1 and n - plus == 0:
    print("Yes")
else:
    print("No")
