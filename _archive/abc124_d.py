from collections import *


def str2intWithArray(Array):
    return list(map(lambda x: int(x), Array))


n, k = map(int, input().split())
S = str2intWithArray(list(input()))

np = S[0]
cnt = 1
NPs = deque([[1 - np, 0]])

for i in range(n - 1):
    if np == S[i + 1]:
        cnt += 1
        continue
    NPs.append([np, cnt])
    cnt = 1
    np = S[i + 1]
NPs.append([np, cnt])
NPs.append([1 - np, 0])
print(NPs)

ans = 0

for i in range(len(NPs) - 2):
    a = NPs[i]
    b = NPs[i + 1]
    c = NPs[i + 2]
    if b[0] == 0:
        ans = max(ans, a[1] + b[1] + c[1])
    else:
        ans = max(ans, a[1] + b[1], b[1] + c[1])

print(ans)
