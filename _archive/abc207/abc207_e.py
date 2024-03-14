from itertools import accumulate
from collections import defaultdict
from functools import lru_cache  # 同じものは再計算しない

mod = 10**9 + 7

n = int(input())
A = list(map(int, input().split()))
accA = [0] + list(accumulate(A))

dic = {i + 1: defaultdict(int) for i in range(n)}

for i in range(1, n + 1):
    dic[i][1] = 1


@lru_cache
def d(a, b):
    return a % b == 0


for i in range(1, n):
    for key, value in dic[i].items():
        for j in range(i + 1, n + 1):
            if not (d(accA[j] - accA[i], key + 1)) != 0:
                continue
            dic[j][key + 1] += value

print(sum(dic[n].values()) % mod)
