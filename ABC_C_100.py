n = int(input())
a = list(map(int, input().split()))
aCnt = 0

for i in range(n):
    while a[i] % 2 == 0:
        aCnt += 1
        a[i] /= 2

print(aCnt)
