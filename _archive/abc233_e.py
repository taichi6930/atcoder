from collections import deque


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


X = str2intWithArray(list(input()))[::-1]
sumX = sum(X)
ans = sumX

for i, x in enumerate(X):
    sumX -= x
    ans += (10 ** (i + 1)) * sumX

print(ans)
