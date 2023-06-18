from math import ceil, log
a, b, k = map(int, input().split())

n = int(ceil(log(b / a) / log(k))) - 1

for i in range(10):
    if a * (k ** n) >= b:
        print(n)
        exit()
    n += 1
