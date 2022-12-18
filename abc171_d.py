from collections import Counter
n = int(input())
A = list(map(int, input().split()))
cA = Counter(A)
ans = sum(A)

q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    ans += (c - b) * cA[b]
    cA[c] += cA[b]
    cA[b] = 0
    print(ans)
