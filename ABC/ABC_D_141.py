import math
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
a = list(map(lambda x: math.log2(x), a))
print(a)
for i in range(m):
    a[-1] -= 1
    if a[-1] != max(a):
        a = sorted(a)
print(sum(list(map(lambda x: int(2 ** x), a))))
