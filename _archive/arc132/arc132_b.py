n = int(input())
P = list(map(int, input().split()))
pIndex = P.index(1)

P1 = [1] + P[pIndex + 1:] + P[: pIndex]
P2 = P[pIndex + 1:] + P[: pIndex + 1]

swiP1 = True
swiP2 = True

for i in range(n - 1):
    if P1[i + 1] - P1[i] != 1:
        swiP1 = False
    if P2[i] - P2[i + 1] != 1:
        swiP2 = False

ans = 10 ** 9

if swiP1:
    ans = min(ans, pIndex, n - pIndex + 2)

if swiP2:
    ans = min(ans, n - pIndex, pIndex + 2)

print(ans)
