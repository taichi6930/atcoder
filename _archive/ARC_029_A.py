n = int(input())
tList = sorted([int(input()) for _ in range(n)], reverse=True)

a, b = 0, 0

for i in range(n):
    if a >= b:
        b += tList[i]
        continue
    else:
        a += tList[i]
print(max(a, b))
