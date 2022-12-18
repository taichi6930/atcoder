from collections import Counter
n, m = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))

A = [0]

for i in range(n - 1):
    A.append(S[i] - A[-1])

k = Counter()
for i, a in enumerate(A):
    for x in X:
        k[((-1) ** i) * (x - a)] += 1

print(k.most_common()[0][1])
