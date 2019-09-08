x = int(input())
xSum = (x // 11) * 2
x = x % 11
print(xSum if x == 0 else xSum + 2 if x >= 7 else xSum + 1)
