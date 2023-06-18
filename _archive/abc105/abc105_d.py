from collections import Counter
from itertools import accumulate

n, m = map(int, input().split())
cA = Counter(list(map(lambda x: x %
             m, [0] + list(accumulate(list(map(int, input().split())))))))

print(sum([cA[key] * (cA[key] - 1) // 2 for key in cA.keys()]))
