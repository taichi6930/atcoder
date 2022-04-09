import collections
n, k = map(int, input().split())
A = list(map(int, input().split()))

aNum = -1
B = [0]
ASUM = [A[0]]

for i in range(k - 1):
    b = ASUM[-1] % n
    if b in B:
        aNum = B.index(b)
        break
    B.append(b)
    xPlus = A[b]
    ASUM.append(ASUM[-1] + xPlus)

if aNum == -1:
    print(ASUM[-1])
    exit()

ans = 0

c1List = B[0:aNum]
c1ListLen = len(c1List)

ans = ASUM[c1ListLen - 1]

c2List = B[aNum:]
c2ListLen = len(c2List)

ansda = ASUM[-1] - ASUM[c1ListLen - 1]

ans += ansda * (((k - c1ListLen) // c2ListLen))

c3ListLen = k - c1ListLen - (((k - c1ListLen) // c2ListLen)) * c2ListLen

if c3ListLen > 0:
    ans += ASUM[c3ListLen + c1ListLen - 1] - ASUM[c1ListLen - 1]

print(ans)
