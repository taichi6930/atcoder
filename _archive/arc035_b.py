from math import factorial
from collections import Counter
from itertools import accumulate
n = int(input())
T = sorted([int(input()) for _ in range(n)])
accT = list(accumulate(T))
couT = Counter(T)
ans = 1

print(sum(accT))
for i in list(couT.values()):
    ans = pow(ans * factorial(i), 1, 1000000007)

print(ans)
