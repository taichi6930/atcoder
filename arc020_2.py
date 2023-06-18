from collections import Counter
n, c = map(int, input().split())
A = [int(input()) for _ in range(n)]
A0, A1 = A[0::2], A[1::2]
cA0, cA1 = Counter(A0), Counter(A1)
maxA0, maxA1 = cA0.most_common()[0][1], cA1.most_common()[0][1]

ans = n * c
swi = False

for i, a in enumerate(list(cA0.keys())):
    ans0 = len(A0) - cA0[a]
    for j, b in enumerate(list(cA1.keys())):
        if a == b:
            continue
        swi = True
        ans1 = len(A1) - cA1[b]
        ans = min(ans, c * (ans0 + ans1))

print(ans if swi else c * len(A1))
